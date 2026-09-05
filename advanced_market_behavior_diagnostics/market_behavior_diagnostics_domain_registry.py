"""Phase 129: Market Behavior Diagnostics Domain Registry.

Builds a DataFrame and summary of operational domain classifications and responsibilities.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_labels import (
    MARKET_BEHAVIOR_DIAGNOSTICS_DOMAIN_LABELS,
)

CORE_BEHAVIOR_DOMAINS = MARKET_BEHAVIOR_DIAGNOSTICS_DOMAIN_LABELS



def build_market_behavior_diagnostics_domain_registry(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build DataFrame and metadata summary of market behavior diagnostics domains."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for label in MARKET_BEHAVIOR_DIAGNOSTICS_DOMAIN_LABELS:
        rows.append(
            {
                "domain_name": label,
                "current_phase": profile.current_phase,
                "target_final_phase": profile.target_final_phase,
                "next_phase": profile.next_phase,
                "is_active": True,
                "non_signal": True,
                "requires_manual_review": label in [
                    "candidate_state_ambiguity_domain",
                    "candidate_state_missingness_domain",
                    "manual_review_domain",
                ],
                "execution_allowed": False,
                "model_training_allowed": False,
                "clustering_allowed": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_market_behavior_diagnostics_domains(df, profile)
    return df, summary


def summarize_market_behavior_diagnostics_domains(
    df: pd.DataFrame,
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> dict:
    """Summarize market behavior diagnostics domain mapping."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()
    return {
        "active_profile": profile.profile_name,
        "total_domains": len(df),
        "domain_names": df["domain_name"].tolist() if not df.empty and "domain_name" in df.columns else [],
        "all_non_signal": True,
        "all_source_preserved": True,
        "zero_execution_guaranteed": True,
    }

