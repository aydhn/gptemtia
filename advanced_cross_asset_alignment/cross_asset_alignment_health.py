"""Phase 119: Cross-Asset Alignment System Health Check.

Performs verification of Phase 113-118 integration readiness,
Phase 119 internal alignment modules, backward-only join contracts,
lookahead guards, and project folder structures.
"""

from pathlib import Path
from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


def build_cross_asset_alignment_health_check(
    project_root: Path,
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify health across previous phases and all Phase 119 components."""
    active_profile = profile or get_default_cross_asset_alignment_profile()
    checks: List[Dict[str, Any]] = []

    # 1. Prior phases health checks
    prior_phases = [
        ("phase_113_data_normalization", "advanced_data_normalization"),
        ("phase_114_data_lineage", "advanced_data_lineage"),
        ("phase_115_data_quality", "advanced_data_quality"),
        ("phase_116_feature_engine", "advanced_feature_engine"),
        ("phase_117_technical_indicators", "advanced_technical_indicators"),
        ("phase_118_feature_grid", "advanced_feature_grid"),
    ]

    for component_name, module_name in prior_phases:
        try:
            __import__(module_name)
            checks.append({
                "component": component_name,
                "category": "prior_phase",
                "status": "HEALTHY",
                "detail": f"Modül '{module_name}' başarıyla yüklendi.",
            })
        except Exception as exc:
            checks.append({
                "component": component_name,
                "category": "prior_phase",
                "status": "UNHEALTHY",
                "detail": f"Yükleme hatası: {exc}",
            })

    # 2. Phase 119 core modules check
    core_modules = [
        "advanced_cross_asset_alignment.cross_asset_alignment_config",
        "advanced_cross_asset_alignment.cross_asset_alignment_models",
        "advanced_cross_asset_alignment.cross_asset_alignment_labels",
        "advanced_cross_asset_alignment.cross_asset_alignment_profile_registry",
        "advanced_cross_asset_alignment.cross_asset_alignment_domain_registry",
        "advanced_cross_asset_alignment.asset_universe_alignment",
        "advanced_cross_asset_alignment.asset_symbol_mapping",
        "advanced_cross_asset_alignment.cross_domain_feature_namespace",
        "advanced_cross_asset_alignment.timestamp_alignment_contracts",
        "advanced_cross_asset_alignment.session_calendar_alignment",
        "advanced_cross_asset_alignment.feature_matrix_contracts",
        "advanced_cross_asset_alignment.feature_matrix_join_policies",
        "advanced_cross_asset_alignment.asof_join_policies",
        "advanced_cross_asset_alignment.no_lookahead_alignment_guard",
        "advanced_cross_asset_alignment.cross_domain_feature_matrix",
        "advanced_cross_asset_alignment.aligned_feature_matrix_manifest",
        "advanced_cross_asset_alignment.cross_asset_feature_metadata",
        "advanced_cross_asset_alignment.cross_asset_alignment_validation_rules",
        "advanced_cross_asset_alignment.cross_asset_alignment_quality_handoff",
    ]

    for mod_path in core_modules:
        try:
            __import__(mod_path)
            checks.append({
                "component": mod_path.split(".")[-1],
                "category": "phase_119_core",
                "status": "HEALTHY",
                "detail": "Modül hazır.",
            })
        except Exception as exc:
            checks.append({
                "component": mod_path.split(".")[-1],
                "category": "phase_119_core",
                "status": "UNHEALTHY",
                "detail": str(exc),
            })

    # 3. Domain alignment registries check
    domain_alignment_modules = [
        "advanced_cross_asset_alignment.fx_commodity_alignment",
        "advanced_cross_asset_alignment.fx_macro_alignment",
        "advanced_cross_asset_alignment.fx_calendar_alignment",
        "advanced_cross_asset_alignment.fx_news_metadata_alignment",
        "advanced_cross_asset_alignment.commodity_macro_alignment",
        "advanced_cross_asset_alignment.commodity_calendar_alignment",
        "advanced_cross_asset_alignment.commodity_news_metadata_alignment",
        "advanced_cross_asset_alignment.macro_calendar_alignment",
        "advanced_cross_asset_alignment.calendar_news_metadata_alignment",
    ]

    for mod_path in domain_alignment_modules:
        try:
            __import__(mod_path)
            checks.append({
                "component": mod_path.split(".")[-1],
                "category": "domain_alignment",
                "status": "HEALTHY",
                "detail": "Domain hizalama modülü hazır.",
            })
        except Exception as exc:
            checks.append({
                "component": mod_path.split(".")[-1],
                "category": "domain_alignment",
                "status": "UNHEALTHY",
                "detail": str(exc),
            })

    # 4. Critical function checks
    try:
        from advanced_cross_asset_alignment.asof_join_policies import safe_asof_join_backward
        checks.append({
            "component": "safe_asof_join_backward",
            "category": "engine_function",
            "status": "HEALTHY",
            "detail": "Geriye dönük asof join fonksiyonu erişilebilir.",
        })
    except Exception as exc:
        checks.append({
            "component": "safe_asof_join_backward",
            "category": "engine_function",
            "status": "UNHEALTHY",
            "detail": str(exc),
        })

    try:
        from advanced_cross_asset_alignment.no_lookahead_alignment_guard import validate_alignment_no_lookahead
        checks.append({
            "component": "validate_alignment_no_lookahead",
            "category": "guard_function",
            "status": "HEALTHY",
            "detail": "Lookahead koruma fonksiyonu aktif.",
        })
    except Exception as exc:
        checks.append({
            "component": "validate_alignment_no_lookahead",
            "category": "guard_function",
            "status": "UNHEALTHY",
            "detail": str(exc),
        })

    # 5. Directory structure checks
    for dir_name in ["scripts", "tests", "docs"]:
        target_dir = project_root / dir_name
        if target_dir.exists() and target_dir.is_dir():
            checks.append({
                "component": f"{dir_name}_directory",
                "category": "filesystem",
                "status": "HEALTHY",
                "detail": f"{dir_name} dizini mevcut.",
            })
        else:
            checks.append({
                "component": f"{dir_name}_directory",
                "category": "filesystem",
                "status": "UNHEALTHY",
                "detail": f"{dir_name} dizini bulunamadı.",
            })

    df = pd.DataFrame(checks)
    summary = summarize_cross_asset_alignment_health(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_cross_asset_alignment_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize system health check DataFrame."""
    if df.empty:
        return {"total_components": 0, "status": "EMPTY", "all_healthy": False}

    all_healthy = bool((df["status"] == "HEALTHY").all())
    return {
        "total_components": len(df),
        "healthy_components": int((df["status"] == "HEALTHY").sum()),
        "unhealthy_components": int((df["status"] == "UNHEALTHY").sum()),
        "all_healthy": all_healthy,
        "prior_phases_healthy": bool(
            (df[df["category"] == "prior_phase"]["status"] == "HEALTHY").all()
        ),
        "health_status": "HEALTHY" if all_healthy else "DEGRADED",
    }
