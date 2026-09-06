"""Phase 133: Regime Validation Acceptance Health Check.

Verifies operational readiness of upstream phases, local packages, scripts, tests, and data storage.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_default_regime_validation_acceptance_profile,
)

HEALTH_CHECK_TARGETS = [
    ("Phase 132 Macro/Event/News Regime", "advanced_macro_event_news_regime", "package"),
    ("Phase 131 Cross-Asset Regime Context", "advanced_cross_asset_regime_context", "package"),
    ("Phase 130 Regime Transition", "advanced_regime_transition", "package"),
    ("Phase 129 Market Behavior Diagnostics", "advanced_market_behavior_diagnostics", "package"),
    ("Phase 128 Regime Rule-Free Labeling", "advanced_regime_rule_free", "package"),
    ("Phase 127 Regime Feature Matrix", "advanced_regime_matrix", "package"),
    ("Phase 126 Regime Foundation", "advanced_regime_foundation", "package"),
    ("Phase 124 Feature Store Integration", "advanced_feature_store_integration", "package"),
    ("Phase 123 Feature Quality Drift", "advanced_feature_quality_drift", "package"),
    ("Phase 121 Feature Validation", "advanced_feature_validation", "package"),
    ("Phase 133 Regime Validation Acceptance", "advanced_regime_validation_acceptance", "package"),
    ("DataLake Storage", "data/storage/data_lake.py", "file"),
    ("FeatureStore ML", "ml/feature_store.py", "file"),
    ("Scripts Directory", "scripts", "directory"),
    ("Tests Directory", "tests", "directory"),
    ("Docs Directory", "docs", "directory"),
]


def build_regime_validation_acceptance_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Evaluate filesystem presence and readiness of required components."""
    root = project_root or Path(".")
    p = profile or get_default_regime_validation_acceptance_profile()

    rows = []
    for label, rel_path, kind in HEALTH_CHECK_TARGETS:
        target_path = root / rel_path
        exists = target_path.exists()
        rows.append(
            {
                "subsystem": label,
                "relative_path": rel_path,
                "kind": kind,
                "present": exists,
                "status": "HEALTHY" if exists else "DEGRADED",
                "profile_name": p.profile_name,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    all_healthy = bool(df["present"].all())
    summary = {
        "total_subsystems": len(df),
        "healthy_subsystems": int(df["present"].sum()),
        "all_healthy": all_healthy,
        "health_status": "HEALTHY" if all_healthy else "DEGRADED",
        "profile_name": p.profile_name,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_regime_validation_acceptance_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health check DataFrame."""
    total = len(df)
    healthy = int(df["present"].sum()) if "present" in df.columns else 0
    return {
        "total_subsystems": total,
        "healthy_subsystems": healthy,
        "all_healthy": total == healthy,
    }
