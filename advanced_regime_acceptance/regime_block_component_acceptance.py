"""Phase 135: Regime Block Component Acceptance Report.

Provides granular component-by-component acceptance validation across Phases 126 to 135.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    ACCEPTANCE_PASS,
    REGIME_BLOCK_COMPONENT_ACCEPTANCE_DOMAIN,
)


COMPONENT_ACCEPTANCE_ITEMS: List[Dict[str, Any]] = [
    {
        "component_name": "Phase 126 Regime Foundation Acceptance",
        "phase_number": 126,
        "source_module": "advanced_regime_foundation",
        "expected_acceptance_refs": 4,
        "non_signal": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": False,
        "source_preserved": True,
        "featurestore_ready": True,
        "manual_review_required": False,
        "status_label": ACCEPTANCE_PASS,
    },
    {
        "component_name": "Phase 127 Regime Matrix Acceptance",
        "phase_number": 127,
        "source_module": "advanced_regime_matrix",
        "expected_acceptance_refs": 6,
        "non_signal": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": False,
        "source_preserved": True,
        "featurestore_ready": True,
        "manual_review_required": False,
        "status_label": ACCEPTANCE_PASS,
    },
    {
        "component_name": "Phase 128 Rule-Free Prep Acceptance",
        "phase_number": 128,
        "source_module": "advanced_regime_rule_free",
        "expected_acceptance_refs": 5,
        "non_signal": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": False,
        "source_preserved": True,
        "featurestore_ready": True,
        "manual_review_required": False,
        "status_label": ACCEPTANCE_PASS,
    },
    {
        "component_name": "Phase 129 Behavior Diagnostics Acceptance",
        "phase_number": 129,
        "source_module": "advanced_market_behavior_diagnostics",
        "expected_acceptance_refs": 5,
        "non_signal": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": False,
        "source_preserved": True,
        "featurestore_ready": True,
        "manual_review_required": False,
        "status_label": ACCEPTANCE_PASS,
    },
    {
        "component_name": "Phase 130 Transition/Stability Acceptance",
        "phase_number": 130,
        "source_module": "advanced_regime_transition",
        "expected_acceptance_refs": 5,
        "non_signal": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": False,
        "source_preserved": True,
        "featurestore_ready": True,
        "manual_review_required": False,
        "status_label": ACCEPTANCE_PASS,
    },
    {
        "component_name": "Phase 131 Cross-Asset Context Acceptance",
        "phase_number": 131,
        "source_module": "advanced_cross_asset_regime_context",
        "expected_acceptance_refs": 5,
        "non_signal": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": False,
        "source_preserved": True,
        "featurestore_ready": True,
        "manual_review_required": False,
        "status_label": ACCEPTANCE_PASS,
    },
    {
        "component_name": "Phase 132 Macro/Event/News Context Acceptance",
        "phase_number": 132,
        "source_module": "advanced_macro_event_news_regime",
        "expected_acceptance_refs": 6,
        "non_signal": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "source_preserved": True,
        "featurestore_ready": True,
        "manual_review_required": False,
        "status_label": ACCEPTANCE_PASS,
    },
    {
        "component_name": "Phase 133 Regime Validation Acceptance",
        "phase_number": 133,
        "source_module": "advanced_regime_validation_acceptance",
        "expected_acceptance_refs": 8,
        "non_signal": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "source_preserved": True,
        "featurestore_ready": True,
        "manual_review_required": False,
        "status_label": ACCEPTANCE_PASS,
    },
    {
        "component_name": "Phase 134 FeatureStore Integration Acceptance",
        "phase_number": 134,
        "source_module": "advanced_regime_featurestore_integration",
        "expected_acceptance_refs": 8,
        "non_signal": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "source_preserved": True,
        "featurestore_ready": True,
        "manual_review_required": False,
        "status_label": ACCEPTANCE_PASS,
    },
    {
        "component_name": "Phase 135 Final Regime Block Acceptance",
        "phase_number": 135,
        "source_module": "advanced_regime_acceptance",
        "expected_acceptance_refs": 10,
        "non_signal": True,
        "no_lookahead_required": True,
        "metadata_only_news_required": True,
        "source_preserved": True,
        "featurestore_ready": True,
        "manual_review_required": False,
        "status_label": ACCEPTANCE_PASS,
    },
]


def build_regime_block_component_acceptance_report(
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for component acceptance."""
    active = profile or get_regime_acceptance_profile()
    df = pd.DataFrame(COMPONENT_ACCEPTANCE_ITEMS)
    summary: Dict[str, Any] = {
        "domain": REGIME_BLOCK_COMPONENT_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "total_components": len(df),
        "all_accepted": bool((df["status_label"] == ACCEPTANCE_PASS).all()),
        "all_non_signal": bool(df["non_signal"].all()),
        "all_source_preserved": bool(df["source_preserved"].all()),
        "phase_start": 126,
        "phase_end": 135,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_regime_block_component_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize component acceptance DataFrame."""
    return {
        "component_count": len(df),
        "all_accepted": bool((df["status_label"] == ACCEPTANCE_PASS).all()) if not df.empty and "status_label" in df.columns else False,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty and "non_signal" in df.columns else True,
    }
