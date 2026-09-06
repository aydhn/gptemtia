"""Phase 135: Regime Acceptance Health Check.

Verifies the availability and health of all components, modules, and storage systems
across the Phase 126-135 regime classification block.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    ACCEPTANCE_PASS,
)


HEALTH_CHECK_MODULES: List[Dict[str, Any]] = [
    {"component": "Phase 126 Regime Foundation", "path": "advanced_regime_foundation", "kind": "module"},
    {"component": "Phase 127 Regime Matrix", "path": "advanced_regime_matrix", "kind": "module"},
    {"component": "Phase 128 Rule-Free Prep", "path": "advanced_regime_rule_free", "kind": "module"},
    {"component": "Phase 129 Behavior Diagnostics", "path": "advanced_market_behavior_diagnostics", "kind": "module"},
    {"component": "Phase 130 Regime Transition", "path": "advanced_regime_transition", "kind": "module"},
    {"component": "Phase 131 Cross-Asset Context", "path": "advanced_cross_asset_regime_context", "kind": "module"},
    {"component": "Phase 132 Macro/Event/News Regime", "path": "advanced_macro_event_news_regime", "kind": "module"},
    {"component": "Phase 133 Validation Acceptance", "path": "advanced_regime_validation_acceptance", "kind": "module"},
    {"component": "Phase 134 FeatureStore Integration", "path": "advanced_regime_featurestore_integration", "kind": "module"},
    {"component": "Phase 135 Regime Acceptance", "path": "advanced_regime_acceptance", "kind": "module"},
    {"component": "DataLake Storage", "path": "data/storage/data_lake.py", "kind": "storage"},
    {"component": "FeatureStore Core", "path": "ml/feature_store.py", "kind": "storage"},
    {"component": "Scripts Directory", "path": "scripts", "kind": "scripts"},
    {"component": "Tests Directory", "path": "tests", "kind": "tests"},
    {"component": "Documentation Directory", "path": "docs", "kind": "docs"},
]


def build_regime_acceptance_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build health check results for all regime components."""
    root = project_root or Path(".")
    active = profile or get_regime_acceptance_profile()

    rows = []
    for item in HEALTH_CHECK_MODULES:
        target = root / item["path"]
        exists = target.exists()
        rows.append({
            "component": item["component"],
            "path": item["path"],
            "kind": item["kind"],
            "healthy": exists,
            "non_signal": True,
            "status_label": ACCEPTANCE_PASS if exists else "acceptance_fail",
        })

    df = pd.DataFrame(rows)
    all_healthy = bool(df["healthy"].all())
    summary: Dict[str, Any] = {
        "active_profile": active.profile_name,
        "total_checks": len(df),
        "healthy_count": int(df["healthy"].sum()),
        "all_healthy": all_healthy,
        "non_signal": True,
        "status": "HEALTHY" if all_healthy else "UNHEALTHY",
    }
    return df, summary


def summarize_regime_acceptance_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health check DataFrame."""
    return {
        "total_checks": len(df),
        "all_healthy": bool(df["healthy"].all()) if not df.empty and "healthy" in df.columns else False,
        "non_signal": True,
    }
