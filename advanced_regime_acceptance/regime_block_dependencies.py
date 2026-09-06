"""Phase 135: Regime Block Dependency Map.

Models the sequential and cross-functional dependencies across Phases 126-136.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    ACCEPTANCE_PASS,
    REGIME_BLOCK_DEPENDENCY_DOMAIN,
)


REGIME_BLOCK_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "step_number": 1,
        "source_phase": 126,
        "target_phase": 127,
        "source_module": "advanced_regime_foundation",
        "target_module": "advanced_regime_matrix",
        "dependency_type": "taxonomy_to_matrix",
        "description": "Foundational regime families and taxonomy provide structural anchors for matrix contracts.",
        "satisfied": True,
        "non_signal": True,
    },
    {
        "step_number": 2,
        "source_phase": 127,
        "target_phase": 128,
        "source_module": "advanced_regime_matrix",
        "target_module": "advanced_regime_rule_free",
        "dependency_type": "matrix_to_rule_free_prep",
        "description": "Aligned state dataset schemas feed unsupervised candidate state generation without directional targets.",
        "satisfied": True,
        "non_signal": True,
    },
    {
        "step_number": 3,
        "source_phase": 128,
        "target_phase": 129,
        "source_module": "advanced_regime_rule_free",
        "target_module": "advanced_market_behavior_diagnostics",
        "dependency_type": "candidate_states_to_diagnostics",
        "description": "Candidate states and pseudo-state contracts supply inputs for behavior diagnostics.",
        "satisfied": True,
        "non_signal": True,
    },
    {
        "step_number": 4,
        "source_phase": 129,
        "target_phase": 130,
        "source_module": "advanced_market_behavior_diagnostics",
        "target_module": "advanced_regime_transition",
        "dependency_type": "diagnostics_to_transitions",
        "description": "Validated cluster quality metrics inform Markov transition matrix stability analysis.",
        "satisfied": True,
        "non_signal": True,
    },
    {
        "step_number": 5,
        "source_phase": 130,
        "target_phase": 131,
        "source_module": "advanced_regime_transition",
        "target_module": "advanced_cross_asset_regime_context",
        "dependency_type": "transitions_to_cross_asset",
        "description": "Asset-level regime transitions inform multi-market alignment and divergence context.",
        "satisfied": True,
        "non_signal": True,
    },
    {
        "step_number": 6,
        "source_phase": 131,
        "target_phase": 132,
        "source_module": "advanced_cross_asset_regime_context",
        "target_module": "advanced_macro_event_news_regime",
        "dependency_type": "cross_asset_to_macro_context",
        "description": "Cross-market alignment contexts integrate with macro indicators, calendar events, and news metadata.",
        "satisfied": True,
        "non_signal": True,
    },
    {
        "step_number": 7,
        "source_phase": 132,
        "target_phase": 133,
        "source_module": "advanced_macro_event_news_regime",
        "target_module": "advanced_regime_validation_acceptance",
        "dependency_type": "macro_to_validation_acceptance",
        "description": "Complete multi-domain context passes through no-lookahead and non-signal validation gates.",
        "satisfied": True,
        "non_signal": True,
    },
    {
        "step_number": 8,
        "source_phase": 133,
        "target_phase": 134,
        "source_module": "advanced_regime_validation_acceptance",
        "target_module": "advanced_regime_featurestore_integration",
        "dependency_type": "validation_to_featurestore",
        "description": "Accepted reference registries and compliance checks register in FeatureStore catalogs.",
        "satisfied": True,
        "non_signal": True,
    },
    {
        "step_number": 9,
        "source_phase": 134,
        "target_phase": 135,
        "source_module": "advanced_regime_featurestore_integration",
        "target_module": "advanced_regime_acceptance",
        "dependency_type": "featurestore_to_final_acceptance",
        "description": "FeatureStore catalogs and contracts underpin the final regime block acceptance report.",
        "satisfied": True,
        "non_signal": True,
    },
    {
        "step_number": 10,
        "source_phase": 135,
        "target_phase": 136,
        "source_module": "advanced_regime_acceptance",
        "target_module": "advanced_ml_gpu_foundation",
        "dependency_type": "acceptance_to_ml_gpu_handoff",
        "description": "Accepted regime manifest and governance contracts hand off cleanly to Phase 136 GPU/ML runtime.",
        "satisfied": True,
        "non_signal": True,
    },
]


def build_regime_block_dependency_report(
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for regime block dependencies."""
    active = profile or get_regime_acceptance_profile()
    df = pd.DataFrame(REGIME_BLOCK_DEPENDENCIES)
    summary: Dict[str, Any] = {
        "domain": REGIME_BLOCK_DEPENDENCY_DOMAIN,
        "active_profile": active.profile_name,
        "total_dependency_steps": len(df),
        "all_satisfied": bool(df["satisfied"].all()),
        "all_non_signal": bool(df["non_signal"].all()),
        "flow": "126 -> 127 -> 128 -> 129 -> 130 -> 131 -> 132 -> 133 -> 134 -> 135 -> 136",
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_regime_block_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize dependency DataFrame."""
    return {
        "dependency_count": len(df),
        "all_satisfied": bool(df["satisfied"].all()) if not df.empty and "satisfied" in df.columns else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty and "non_signal" in df.columns else True,
    }
