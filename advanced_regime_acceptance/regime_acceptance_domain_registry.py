"""Phase 135: Regime Acceptance Domain Registry.

Builds and summarizes the domain registry covering Phases 126 through 136.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    ACCEPTANCE_PASS,
    REGIME_ACCEPTANCE_DOMAIN,
)


DOMAINS_DEFINITION = [
    {
        "phase": 126,
        "domain_id": "regime_foundation",
        "title": "Regime Classification and Market Behavior Foundation",
        "description": "Foundational taxonomy, regime definitions, families, and baseline policies.",
        "module": "advanced_regime_foundation",
        "non_signal": True,
    },
    {
        "phase": 127,
        "domain_id": "regime_matrix",
        "title": "Regime Feature Matrix and State Dataset Contracts",
        "description": "Multi-timeframe feature matrix contracts, state dataset schema, and backward asof alignment.",
        "module": "advanced_regime_matrix",
        "non_signal": True,
    },
    {
        "phase": 128,
        "domain_id": "regime_rule_free",
        "title": "Regime Rule-Free Labeling Contracts and Unsupervised Prep",
        "description": "Rule-free candidate states, pseudo-state contracts, and clustering input prep without directional labels.",
        "module": "advanced_regime_rule_free",
        "non_signal": True,
    },
    {
        "phase": 129,
        "domain_id": "market_behavior_diagnostics",
        "title": "Market Behavior Diagnostics and Regime Quality",
        "description": "Behavioral diagnostics, separation metrics, silhouette checks, and regime quality scores.",
        "module": "advanced_market_behavior_diagnostics",
        "non_signal": True,
    },
    {
        "phase": 130,
        "domain_id": "regime_transition",
        "title": "Regime Transition and Stability Analysis",
        "description": "Markovian transition matrices, state persistence, jump frequencies, and stability metrics.",
        "module": "advanced_regime_transition",
        "non_signal": True,
    },
    {
        "phase": 131,
        "domain_id": "cross_asset_regime_context",
        "title": "Cross-Asset Regime Context Expansion",
        "description": "Multi-asset regime alignment, cross-market divergence, and spillover context contracts.",
        "module": "advanced_cross_asset_regime_context",
        "non_signal": True,
    },
    {
        "phase": 132,
        "domain_id": "macro_event_news_regime",
        "title": "Macro/Event/News Regime Context Expansion",
        "description": "Macro indicator releases, calendar event windows, and metadata-only news context without full articles.",
        "module": "advanced_macro_event_news_regime",
        "non_signal": True,
    },
    {
        "phase": 133,
        "domain_id": "regime_validation_acceptance",
        "title": "Regime Validation and No-Lookahead Acceptance",
        "description": "Acceptance gates, no-lookahead audit, backward-asof verification, and non-signal compliance.",
        "module": "advanced_regime_validation_acceptance",
        "non_signal": True,
    },
    {
        "phase": 134,
        "domain_id": "regime_featurestore_integration",
        "title": "Regime FeatureStore Integration",
        "description": "FeatureStore namespaces, entities, catalogs, lineage references, and read/write/query contracts.",
        "module": "advanced_regime_featurestore_integration",
        "non_signal": True,
    },
    {
        "phase": 135,
        "domain_id": "regime_acceptance",
        "title": "Regime Classification Block Final Acceptance",
        "description": "Phase 126-135 block final acceptance, inventory, dependencies, compliance, and manifest.",
        "module": "advanced_regime_acceptance",
        "non_signal": True,
    },
    {
        "phase": 136,
        "domain_id": "advanced_ml_gpu_handoff",
        "title": "Advanced ML and GPU Runtime Handoff",
        "description": "Formal handoff to Phase 136 GPU acceleration and advanced ML runtime foundation.",
        "module": "advanced_ml_gpu_foundation",
        "non_signal": True,
    },
]


def build_regime_acceptance_domain_registry(
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of regime acceptance domains."""
    active = profile or get_regime_acceptance_profile()
    rows = []
    for d in DOMAINS_DEFINITION:
        rows.append({
            "phase": d["phase"],
            "domain_id": d["domain_id"],
            "title": d["title"],
            "description": d["description"],
            "source_module": d["module"],
            "non_signal": d["non_signal"],
            "status_label": ACCEPTANCE_PASS,
        })
    df = pd.DataFrame(rows)
    summary: Dict[str, Any] = {
        "domain": REGIME_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "total_domains": len(rows),
        "phase_start": 126,
        "phase_end": 135,
        "handoff_phase": 136,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_regime_acceptance_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize domain DataFrame."""
    return {
        "total_domains": len(df),
        "phases": df["phase"].tolist() if not df.empty and "phase" in df.columns else [],
        "non_signal": True,
    }
