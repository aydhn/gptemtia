import pandas as pd
from pathlib import Path
from typing import Tuple, Dict, Optional

from data.storage.data_lake import DataLake
from config.settings import Settings

from .performance_config import PerformanceProfile, get_default_performance_profile
from .performance_models import build_batch_plan_id
from .cpu_gpu_awareness import build_cpu_gpu_awareness_report
from .runtime_profiler import RuntimeProfiler, build_default_profile_commands
from .memory_profiler import build_memory_profile_table, summarize_memory_profiles
from .resource_budget import (
    build_default_resource_budgets,
    resource_budgets_to_dataframe,
    build_resource_budget_violation_report
)
from .cache_registry import CacheRegistry
from .cache_inventory import scan_cache_directory, build_cache_hit_miss_report
from .cache_strategy import build_cache_policy_table, build_cache_invalidation_plan, summarize_cache_strategy
from .batch_planner import build_module_batch_plans
from .checkpointing import create_checkpoint_manifest, save_checkpoint_manifest, build_resume_plan_from_checkpoint
from .large_run_stability import evaluate_large_run_stability, summarize_large_run_stability
from .bottleneck_detection import build_bottleneck_report
from .optimization_recommendations import build_safe_optimization_recommendation_report
from .performance_quality import build_performance_quality_report
from .performance_report_builder import (
    build_performance_profile_markdown_report,
    build_resource_budget_markdown_report,
    build_cache_strategy_markdown_report,
    build_large_run_stability_markdown_report,
    build_runtime_optimization_markdown_report
)

class PerformancePipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[PerformanceProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_performance_profile()
        self.cache_dir = project_root / "data" / "lake" / "performance" / "cache"

    def build_performance_profile_report(
        self,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:

        dfs = {}

        # CPU/GPU Awareness
        cpu_df, cpu_summary = build_cpu_gpu_awareness_report(self.profile)
        dfs["cpu_gpu_awareness"] = cpu_df

        # Runtime Profiler
        profiler = RuntimeProfiler(self.project_root, self.profile)
        commands_df = build_default_profile_commands()
        rt_df, rt_summary = profiler.profile_command_registry(commands_df, limit=limit)
        dfs["runtime_profiles"] = rt_df

        # Mock memory profile
        mem_df = pd.DataFrame([{"command_name": "mock", "module_name": "performance", "peak_memory_mb": 50.0, "budget_status": "within_budget"}])
        mem_summary = summarize_memory_profiles(mem_df)
        dfs["memory_profiles"] = mem_df

        summary = {
            "profile_name": self.profile.name,
            "cpu_detected": cpu_summary.get("cpu_count", 0),
            "gpu_detected": cpu_summary.get("gpu_detected", False),
            "total_runtime_commands": rt_summary.get("total_commands", 0),
            "total_memory_profiles": mem_summary.get("total_profiles", 0)
        }

        if save and hasattr(self.data_lake, 'save_runtime_profiles'):
            self.data_lake.save_runtime_profiles(rt_df, summary)
            self.data_lake.save_memory_profiles(mem_df, summary)
            self.data_lake.save_cpu_gpu_awareness(cpu_df, summary)

            md = build_performance_profile_markdown_report(summary, rt_df, mem_df)
            self.data_lake.save_performance_report(f"{self.profile.name}_profile", summary, md)

        return dfs, summary

    def build_resource_budget_report(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:

        budgets = build_default_resource_budgets(self.profile)
        b_df = resource_budgets_to_dataframe(budgets)

        # Load from data lake if available, else use empty mock
        rt_df = pd.DataFrame()
        mem_df = pd.DataFrame()

        if hasattr(self.data_lake, 'load_runtime_profiles'):
            try:
                rt_df = self.data_lake.load_runtime_profiles()
            except Exception:
                pass

        if hasattr(self.data_lake, 'load_memory_profiles'):
            try:
                mem_df = self.data_lake.load_memory_profiles()
            except Exception:
                pass

        v_df, v_summary = build_resource_budget_violation_report(rt_df, mem_df, b_df)

        dfs = {
            "resource_budgets": b_df,
            "resource_budget_violations": v_df
        }

        summary = {
            "profile_name": self.profile.name,
            "total_budgets": len(b_df),
            "total_violations": v_summary.get("total_violations", 0)
        }

        if save and hasattr(self.data_lake, 'save_resource_budgets'):
            self.data_lake.save_resource_budgets(b_df, summary)
            self.data_lake.save_resource_budget_violations(v_df, summary)

            md = build_resource_budget_markdown_report(summary, b_df, v_df)
            self.data_lake.save_performance_report(f"{self.profile.name}_budget", summary, md)

        return dfs, summary

    def build_cache_strategy_report(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:

        policy_df = build_cache_policy_table(self.profile)

        inventory_df, inv_summary = scan_cache_directory(self.cache_dir)

        registry = CacheRegistry(self.cache_dir)
        registry_df = registry.load_cache_records()

        inval_df, inval_summary = build_cache_invalidation_plan(registry_df, self.profile)
        hit_df, hit_summary = build_cache_hit_miss_report(registry_df)

        dfs = {
            "cache_policy": policy_df,
            "cache_inventory": inventory_df,
            "cache_invalidation_plan": inval_df
        }

        summary = summarize_cache_strategy(policy_df, registry_df)
        summary.update({
            "inventory_size_mb": inv_summary.get("total_size_mb", 0),
            "total_to_invalidate": inval_summary.get("total_to_invalidate", 0),
            "hit_rate": hit_summary.get("overall_hit_rate", 0)
        })

        if save and hasattr(self.data_lake, 'save_cache_strategy'):
            self.data_lake.save_cache_strategy(policy_df, summary)
            self.data_lake.save_cache_inventory(inventory_df, summary)

            md = build_cache_strategy_markdown_report(summary, registry_df, policy_df)
            self.data_lake.save_performance_report(f"{self.profile.name}_cache", summary, md)

        return dfs, summary

    def build_large_run_stability_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:

        # Try to load existing data
        rt_df = pd.DataFrame()
        mem_df = pd.DataFrame()
        cache_df = pd.DataFrame()

        if hasattr(self.data_lake, 'load_runtime_profiles'):
            try: rt_df = self.data_lake.load_runtime_profiles()
            except: pass
        if hasattr(self.data_lake, 'load_memory_profiles'):
            try: mem_df = self.data_lake.load_memory_profiles()
            except: pass
        if hasattr(self.data_lake, 'load_cache_inventory'):
            try: cache_df = self.data_lake.load_cache_inventory()
            except: pass

        # Build batch plans
        modules = {"performance": ["A", "B", "C"]}
        batch_df, batch_summary = build_module_batch_plans(modules, self.profile)

        # Checkpoint example
        manifest = create_checkpoint_manifest("example", "perf", 100, 50, [])
        if save and hasattr(self.data_lake, 'save_checkpoint_manifest'):
            self.data_lake.save_checkpoint_manifest("example", manifest)

        stability_df = evaluate_large_run_stability(rt_df, mem_df, cache_df, batch_df, self.profile)
        summary = summarize_large_run_stability(stability_df)

        if save and hasattr(self.data_lake, 'save_large_run_stability_report'):
            self.data_lake.save_batch_plans(batch_df, batch_summary)
            self.data_lake.save_large_run_stability_report(stability_df, summary)

            md = build_large_run_stability_markdown_report(summary, stability_df)
            self.data_lake.save_performance_report(f"{self.profile.name}_stability", summary, md)

        return stability_df, summary

    def build_runtime_optimization_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:

        rt_df = pd.DataFrame()
        mem_df = pd.DataFrame()
        cache_df = pd.DataFrame()

        if hasattr(self.data_lake, 'load_runtime_profiles'):
            try: rt_df = self.data_lake.load_runtime_profiles()
            except: pass
        if hasattr(self.data_lake, 'load_memory_profiles'):
            try: mem_df = self.data_lake.load_memory_profiles()
            except: pass
        if hasattr(self.data_lake, 'load_cache_inventory'):
            try: cache_df = self.data_lake.load_cache_inventory()
            except: pass

        bn_df, bn_summary = build_bottleneck_report(rt_df, mem_df, cache_df, self.profile)

        rec_df, summary = build_safe_optimization_recommendation_report(bn_df, self.profile)
        summary["total_bottlenecks_detected"] = bn_summary.get("total_bottlenecks", 0)

        if save and hasattr(self.data_lake, 'save_optimization_recommendations'):
            self.data_lake.save_bottleneck_report(bn_df, bn_summary)
            self.data_lake.save_optimization_recommendations(rec_df, summary)

            md = build_runtime_optimization_markdown_report(summary, rec_df)
            self.data_lake.save_performance_report(f"{self.profile.name}_optimization", summary, md)

        return rec_df, summary

    def build_performance_status(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:

        items = []

        if hasattr(self.data_lake, 'list_performance_reports'):
            try:
                reports = self.data_lake.list_performance_reports()
                for _, r in reports.iterrows():
                    items.append({"item": r.get("name", "unknown"), "status": "Available"})
            except Exception as e:
                items.append({"item": "Reports list", "status": f"Error: {e}"})

        df = pd.DataFrame(items) if items else pd.DataFrame(columns=["item", "status"])
        summary = {"total_items": len(df)}

        if save and hasattr(self.data_lake, 'save_performance_report'):
            # Just save a simple summary
            self.data_lake.save_performance_report(f"{self.profile.name}_status", summary, None)

        return df, summary
