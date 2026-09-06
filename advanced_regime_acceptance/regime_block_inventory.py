"""Phase 135: Regime Block Inventory Report.

Builds and summarizes the inventory of all modules in the regime classification block (Phases 126-135).
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    ACCEPTANCE_PASS,
    REGIME_BLOCK_INVENTORY_DOMAIN,
)


REGIME_BLOCK_MODULES: List[Dict[str, Any]] = [
    {
        "phase_number": 126,
        "module_name": "advanced_regime_foundation",
        "expected_scripts": 7,
        "expected_tests": 12,
        "expected_reports": 6,
        "expected_datalake_outputs": 8,
        "expected_docs": 4,
        "status_label": ACCEPTANCE_PASS,
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "phase_number": 127,
        "module_name": "advanced_regime_matrix",
        "expected_scripts": 8,
        "expected_tests": 15,
        "expected_reports": 8,
        "expected_datalake_outputs": 12,
        "expected_docs": 5,
        "status_label": ACCEPTANCE_PASS,
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "phase_number": 128,
        "module_name": "advanced_regime_rule_free",
        "expected_scripts": 8,
        "expected_tests": 14,
        "expected_reports": 7,
        "expected_datalake_outputs": 10,
        "expected_docs": 4,
        "status_label": ACCEPTANCE_PASS,
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "phase_number": 129,
        "module_name": "advanced_market_behavior_diagnostics",
        "expected_scripts": 8,
        "expected_tests": 14,
        "expected_reports": 8,
        "expected_datalake_outputs": 10,
        "expected_docs": 4,
        "status_label": ACCEPTANCE_PASS,
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "phase_number": 130,
        "module_name": "advanced_regime_transition",
        "expected_scripts": 8,
        "expected_tests": 14,
        "expected_reports": 7,
        "expected_datalake_outputs": 10,
        "expected_docs": 4,
        "status_label": ACCEPTANCE_PASS,
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "phase_number": 131,
        "module_name": "advanced_cross_asset_regime_context",
        "expected_scripts": 8,
        "expected_tests": 15,
        "expected_reports": 8,
        "expected_datalake_outputs": 11,
        "expected_docs": 4,
        "status_label": ACCEPTANCE_PASS,
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "phase_number": 132,
        "module_name": "advanced_macro_event_news_regime",
        "expected_scripts": 9,
        "expected_tests": 16,
        "expected_reports": 9,
        "expected_datalake_outputs": 12,
        "expected_docs": 5,
        "status_label": ACCEPTANCE_PASS,
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "phase_number": 133,
        "module_name": "advanced_regime_validation_acceptance",
        "expected_scripts": 10,
        "expected_tests": 20,
        "expected_reports": 11,
        "expected_datalake_outputs": 15,
        "expected_docs": 5,
        "status_label": ACCEPTANCE_PASS,
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "phase_number": 134,
        "module_name": "advanced_regime_featurestore_integration",
        "expected_scripts": 10,
        "expected_tests": 24,
        "expected_reports": 12,
        "expected_datalake_outputs": 18,
        "expected_docs": 6,
        "status_label": ACCEPTANCE_PASS,
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "phase_number": 135,
        "module_name": "advanced_regime_acceptance",
        "expected_scripts": 10,
        "expected_tests": 24,
        "expected_reports": 13,
        "expected_datalake_outputs": 19,
        "expected_docs": 6,
        "status_label": ACCEPTANCE_PASS,
        "manual_review_required": False,
        "non_signal": True,
        "source_preserved": True,
    },
]


def build_regime_block_inventory_report(
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for regime block inventory."""
    active = profile or get_regime_acceptance_profile()
    df = pd.DataFrame(REGIME_BLOCK_MODULES)
    summary: Dict[str, Any] = {
        "domain": REGIME_BLOCK_INVENTORY_DOMAIN,
        "active_profile": active.profile_name,
        "total_modules": len(df),
        "total_expected_scripts": int(df["expected_scripts"].sum()),
        "total_expected_tests": int(df["expected_tests"].sum()),
        "total_expected_reports": int(df["expected_reports"].sum()),
        "total_expected_datalake_outputs": int(df["expected_datalake_outputs"].sum()),
        "phase_range": "126-135",
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_regime_block_inventory(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize inventory DataFrame."""
    return {
        "module_count": len(df),
        "modules": df["module_name"].tolist() if not df.empty and "module_name" in df.columns else [],
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty and "non_signal" in df.columns else True,
    }
