import pandas as pd
from pathlib import Path
from config.settings import default_advanced_continuation_profile
from data.storage.data_lake import DataLake
from .continuation_config import AdvancedContinuationProfile, get_advanced_continuation_profile
from .advanced_roadmap_registry import build_advanced_roadmap_registry
from .phase_master_plan import build_phase_101_160_master_plan
from .post_mvp_reopen import build_post_mvp_functional_reopen_manifesto
from .phase_output_audit import build_phase_1_100_output_audit
from .mvp_gap_register import build_mvp_to_advanced_gap_register
from .functional_continuation import build_functional_continuation_layer
from .dependency_map import build_advanced_module_dependency_map
from .milestone_map import build_advanced_delivery_milestone_map
from .development_risks import build_advanced_development_risk_register
from .continuation_no_go_safe_go import build_advanced_no_go_safe_go_boundary
from .continuation_scoring import build_advanced_development_readiness_score_report
from .continuation_validation import build_post_mvp_reopen_validation_report
from .continuation_quality import build_post_mvp_reopen_quality_report
from .continuation_report_builder import *

class AdvancedContinuationPipeline:
    def _write_file(self, rel_path: str, text: str):
        p = self.project_root / rel_path
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(text)
            
    def _write_df(self, rel_path_prefix: str, df: pd.DataFrame):
        p_csv = self.project_root / f"{rel_path_prefix}.csv"
        p_csv.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(p_csv, index=False)

    def __init__(self, data_lake: DataLake, settings=None, project_root: Path=None, profile: AdvancedContinuationProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root or Path(".")
        self.profile = profile or get_advanced_continuation_profile(default_advanced_continuation_profile)
    
    def build_advanced_roadmap_registry(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df, summary = build_advanced_roadmap_registry(self.profile)
        if save:
            self.data_lake.save_advanced_roadmap_registry(df, summary)
            txt = build_advanced_roadmap_markdown_report(summary, df)
            self._write_file("reports/output/advanced_continuation/markdown/advanced_roadmap.md", txt)
            self._write_file("docs/generated/advanced_continuation/roadmap/ADVANCED_ROADMAP.md", txt)
            self._write_df("reports/output/advanced_continuation/csv/advanced_roadmap", df)
        return df, summary

    def build_phase_101_160_master_plan(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df, summary = build_phase_101_160_master_plan(self.profile)
        if save:
            self.data_lake.save_phase_101_160_master_plan(df, summary)
            txt = build_phase_master_plan_markdown_report(summary, df)
            self._write_file("reports/output/advanced_continuation/markdown/master_plan.md", txt)
            self._write_file("docs/generated/advanced_continuation/roadmap/MASTER_PLAN_101_160.md", txt)
            self._write_df("reports/output/advanced_continuation/csv/master_plan", df)
        return df, summary

    def build_post_mvp_functional_reopen(self, save: bool = True) -> tuple[str, dict]:
        txt, summary = build_post_mvp_functional_reopen_manifesto(self.project_root, self.profile)
        if save:
            self.data_lake.save_post_mvp_functional_reopen_manifesto(txt, summary)
            md = build_post_mvp_reopen_markdown_report(summary, txt)
            self._write_file("reports/output/advanced_continuation/markdown/post_mvp_functional_reopen.md", md)
            self._write_file("docs/generated/advanced_continuation/reopen/POST_MVP_FUNCTIONAL_REOPEN.md", md)
        return txt, summary

    def build_phase_1_100_output_audit(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df, summary = build_phase_1_100_output_audit(self.project_root, self.profile)
        if save:
            self.data_lake.save_phase_1_100_output_audit(df, summary)
            txt = build_phase_output_audit_markdown_report(summary, df)
            self._write_file("reports/output/advanced_continuation/markdown/phase_1_100_output_audit.md", txt)
            self._write_file("docs/generated/advanced_continuation/audit/OUTPUT_AUDIT.md", txt)
            self._write_df("reports/output/advanced_continuation/csv/phase_1_100_output_audit", df)
        return df, summary

    def build_mvp_to_advanced_gap_register(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df, summary = build_mvp_to_advanced_gap_register(self.profile)
        if save:
            self.data_lake.save_mvp_to_advanced_gap_register(df, summary)
            txt = build_mvp_gap_register_markdown_report(summary, df)
            self._write_file("reports/output/advanced_continuation/markdown/mvp_to_advanced_gap_register.md", txt)
            self._write_file("docs/generated/advanced_continuation/gaps/GAP_REGISTER.md", txt)
            self._write_df("reports/output/advanced_continuation/csv/mvp_to_advanced_gap_register", df)
        return df, summary

    def build_functional_continuation_layer(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df, summary = build_functional_continuation_layer(self.profile)
        if save:
            self.data_lake.save_functional_continuation_layer(df, summary)
            txt = build_functional_continuation_markdown_report(summary, df)
            self._write_file("reports/output/advanced_continuation/markdown/functional_continuation_layer.md", txt)
            self._write_file("docs/generated/advanced_continuation/functional_continuation/FUNCTIONAL_CONTINUATION.md", txt)
            self._write_df("reports/output/advanced_continuation/csv/functional_continuation_layer", df)
        return df, summary

    def build_advanced_continuation_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        summary = {"status": "continuation_ready"}
        quality = build_post_mvp_reopen_quality_report(summary)
        if save:
            self.data_lake.save_post_mvp_reopen_quality_report(self.profile.name, quality)
            txt = build_advanced_continuation_quality_markdown_report(summary, quality)
            self._write_file("reports/output/advanced_continuation/markdown/quality_report.md", txt)
            import json
            self._write_file("reports/output/advanced_continuation/json/quality_report.json", json.dumps(quality))
        return quality, summary

    def build_advanced_continuation_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "continuation_ready"}])
        if save:
            self._write_df("reports/output/advanced_continuation/csv/status", df)
        return df, {"status": "continuation_ready"}
