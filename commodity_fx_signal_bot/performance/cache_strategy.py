import pandas as pd
from typing import Tuple, Optional, Dict
from datetime import datetime, timezone

from .performance_config import PerformanceProfile

_CACHEABLE_MODULES = [
    {"module_name": "knowledge_base", "artifacts": ["chunks", "index"]},
    {"module_name": "governance", "artifacts": ["artifact_inventory"]},
    {"module_name": "command_center", "artifacts": ["command_registry"]},
    {"module_name": "quality_gates", "artifacts": ["import_graph"]},
    {"module_name": "factor_research", "artifacts": ["factor_score_tables"]},
    {"module_name": "synthetic_indices", "artifacts": ["synthetic_levels"]},
    {"module_name": "meta_research", "artifacts": ["meta_evidence_table"]},
    {"module_name": "research_planning", "artifacts": ["planning_signals"]},
]

def should_use_cache(cache_record: Optional[dict], profile: PerformanceProfile) -> Tuple[bool, dict]:
    if not profile.enable_cache:
        return False, {"reason": "Cache disabled in profile"}

    if not cache_record:
        return False, {"reason": "No cache record found"}

    if cache_record.get("status") in ["invalid", "stale"]:
        return False, {"reason": f"Cache status is {cache_record.get('status')}"}

    if is_cache_stale(cache_record, profile.cache_ttl_hours):
        return False, {"reason": "Cache TTL expired"}

    size_mb = cache_record.get("size_bytes", 0) / (1024 * 1024) if cache_record.get("size_bytes") else 0
    if size_mb > profile.cache_max_size_mb:
        return False, {"reason": f"Cache size {size_mb:.2f}MB exceeds profile limit {profile.cache_max_size_mb}MB"}

    return True, {"reason": "Cache valid and within limits"}

def is_cache_stale(cache_record: dict, ttl_hours: int) -> bool:
    created_at = cache_record.get("created_at_utc")
    if not created_at:
        return True

    try:
        # Simple string compare or parse (assume ISO format)
        created = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
        now = datetime.now(timezone.utc)
        age_hours = (now - created).total_seconds() / 3600
        return age_hours > ttl_hours
    except Exception:
        return True

def build_cache_policy_table(profile: PerformanceProfile) -> pd.DataFrame:
    policies = []
    for mod in _CACHEABLE_MODULES:
        policies.append({
            "module_name": mod["module_name"],
            "cacheable_artifacts": ", ".join(mod["artifacts"]),
            "ttl_hours": profile.cache_ttl_hours,
            "invalidation_trigger": "TTL expiry or source update",
            "preferred_format": profile.cache_format,
            "max_size_mb": profile.cache_max_size_mb,
            "warnings": []
        })
    return pd.DataFrame(policies)

def build_cache_invalidation_plan(cache_df: pd.DataFrame, profile: PerformanceProfile) -> Tuple[pd.DataFrame, Dict]:
    if cache_df.empty:
        return pd.DataFrame(), {"total_to_invalidate": 0}

    to_invalidate = []

    for _, row in cache_df.iterrows():
        record = row.to_dict()
        is_stale = is_cache_stale(record, profile.cache_ttl_hours)
        is_invalid = record.get("status") == "invalid"

        if is_stale or is_invalid:
            to_invalidate.append({
                "cache_id": record.get("cache_id"),
                "cache_key": record.get("cache_key"),
                "path": record.get("path"),
                "reason": "TTL expired" if is_stale else "Marked invalid",
                "action": "Plan to delete file (offline recommendation only)"
            })

    plan_df = pd.DataFrame(to_invalidate)
    summary = {
        "total_to_invalidate": len(plan_df)
    }

    return plan_df, summary

def summarize_cache_strategy(policy_df: pd.DataFrame, cache_df: Optional[pd.DataFrame] = None) -> dict:
    return {
        "total_policies": len(policy_df) if not policy_df.empty else 0,
        "cache_enabled": True, # Based on whether policies were built
        "tracked_caches": len(cache_df) if cache_df is not None and not cache_df.empty else 0
    }
