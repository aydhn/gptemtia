"""Phase 134: Regime FeatureStore Health Check.

Verifies the operational readiness, module availability, and integrity of
subsystems across Phase 123 through Phase 134.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    HEALTH_DOMAIN,
    REGIME_STORE_READY,
)


def build_regime_featurestore_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute subsystem health checks and return tabular results with summary."""
    active_profile = profile or get_regime_featurestore_profile()
    root = project_root or Path(".")

    checks: List[Dict[str, Any]] = [
        {"subsystem": "phase_133_regime_validation_acceptance", "path": "advanced_regime_validation_acceptance"},
        {"subsystem": "phase_132_macro_event_news_regime", "path": "advanced_macro_event_news_regime"},
        {"subsystem": "phase_131_cross_asset_regime_context", "path": "advanced_cross_asset_regime_context"},
        {"subsystem": "phase_130_regime_transition", "path": "advanced_regime_transition"},
        {"subsystem": "phase_129_market_behavior_diagnostics", "path": "advanced_market_behavior_diagnostics"},
        {"subsystem": "phase_128_regime_rule_free", "path": "advanced_regime_rule_free"},
        {"subsystem": "phase_127_regime_matrix", "path": "advanced_regime_matrix"},
        {"subsystem": "phase_126_regime_foundation", "path": "advanced_regime_foundation"},
        {"subsystem": "phase_124_feature_store_integration", "path": "advanced_feature_store_integration"},
        {"subsystem": "phase_123_feature_quality_drift", "path": "advanced_feature_quality_drift"},
        {"subsystem": "phase_134_regime_featurestore_integration", "path": "advanced_regime_featurestore_integration"},
        {"subsystem": "data_lake_storage", "path": "data/storage/data_lake.py"},
        {"subsystem": "feature_store_module", "path": "ml/feature_store.py"},
        {"subsystem": "operational_scripts_dir", "path": "scripts"},
        {"subsystem": "test_suite_dir", "path": "tests"},
        {"subsystem": "documentation_dir", "path": "docs"},
    ]

    results = []
    for c in checks:
        target = root / c["path"]
        exists = target.exists()
        status = "HEALTHY" if exists else "MISSING"
        results.append({
            "subsystem": c["subsystem"],
            "target_path": str(c["path"]),
            "exists": exists,
            "status": status,
            "non_signal": True,
        })

    df = pd.DataFrame(results)
    all_healthy = bool((df["exists"] == True).all())

    summary = {
        "domain": HEALTH_DOMAIN,
        "total_checks": len(df),
        "healthy_checks": int((df["exists"] == True).sum()),
        "all_healthy": all_healthy,
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "status": REGIME_STORE_READY if all_healthy else "HEALTH_DEGRADED",
        "non_signal": True,
    }
    return df, summary


def summarize_regime_featurestore_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health check DataFrame."""
    return {
        "total_checks": len(df),
        "all_healthy": bool((df["exists"] == True).all()) if not df.empty else True,
        "missing_subsystems": df[df["exists"] == False]["subsystem"].tolist() if not df.empty else [],
    }
