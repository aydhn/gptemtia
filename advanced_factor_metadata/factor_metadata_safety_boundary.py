"""Phase 122 Factor Metadata Safety Boundary.

Defines unambiguous NO-GO barriers and SAFE-GO principles safeguarding the offline,
non-signal, and non-destructive nature of factor metadata and family definitions.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)

NO_GO_RULES: List[Dict[str, Any]] = [
    {"rule_id": "NG-122-01", "name": "No Live Trading", "description": "Strictly no execution of live market orders or connections."},
    {"rule_id": "NG-122-02", "name": "No Broker Integration", "description": "Zero integration with broker APIs or accounts."},
    {"rule_id": "NG-122-03", "name": "No Real Orders", "description": "Never route real capital or simulated live positions."},
    {"rule_id": "NG-122-04", "name": "No Investment Advice", "description": "Factors never constitute financial or trading recommendations."},
    {"rule_id": "NG-122-05", "name": "No Factor as Signal", "description": "Factor values must not be presented or used as buy/sell signals."},
    {"rule_id": "NG-122-06", "name": "No Directional Claims", "description": "No claims that high/low factor scores ensure directional movement."},
    {"rule_id": "NG-122-07", "name": "No Strategy Rule Generation", "description": "No automated compilation of strategy execution rules."},
    {"rule_id": "NG-122-08", "name": "No Backtest Execution", "description": "Backtesting of factor strategies is prohibited in Phase 122."},
    {"rule_id": "NG-122-09", "name": "No Optimizer Execution", "description": "No portfolio optimization or parameter curve fitting."},
    {"rule_id": "NG-122-10", "name": "No Model Training", "description": "Zero ML model training or weight fitting in this phase."},
    {"rule_id": "NG-122-11", "name": "No Target or Label Generation", "description": "Zero forward returns, labels, or prediction target synthesis."},
    {"rule_id": "NG-122-12", "name": "No Sentiment Model Output", "description": "No NLP sentiment classification outputs or vector embeddings."},
    {"rule_id": "NG-122-13", "name": "No Full Article Usage", "description": "Zero ingestion or storage of copyrighted raw article texts."},
    {"rule_id": "NG-122-14", "name": "No Web Scraping", "description": "Zero web scraping, HTML parsing, or browser automation."},
    {"rule_id": "NG-122-15", "name": "No Paywall/Rate Limit Bypass", "description": "Strict prohibition of rate abuse or reverse engineering."},
    {"rule_id": "NG-122-16", "name": "No Credential Output", "description": "Never print, write, or export API keys or credentials."},
    {"rule_id": "NG-122-17", "name": "No Source Overwrite", "description": "Never overwrite or destructively mutate original data sources."},
    {"rule_id": "NG-122-18", "name": "No Destructive Cleaning", "description": "Never silently delete or drop anomalous records."},
    {"rule_id": "NG-122-19", "name": "No Production Approval Claim", "description": "Zero claims of production readiness or official compliance signoff."},
    {"rule_id": "NG-122-20", "name": "No Deployment", "description": "Zero cloud publishing, docker pushes, or git release tags."},
]

SAFE_GO_RULES: List[Dict[str, Any]] = [
    {"rule_id": "SG-122-01", "name": "Local Research Metadata", "description": "Compile structured offline factor metadata and descriptions."},
    {"rule_id": "SG-122-02", "name": "Factor Family Taxonomy", "description": "Classify factors into trend, momentum, volatility, macro, event, news, cross-asset."},
    {"rule_id": "SG-122-03", "name": "Factor Contracts", "description": "Establish formal contract schemas linking required features and validations."},
    {"rule_id": "SG-122-04", "name": "Namespace Registry", "description": "Enforce lowercase snake_case standard with mandatory factor_ prefix."},
    {"rule_id": "SG-122-05", "name": "Dependency Tracking", "description": "Map upstream indicator, grid, alignment, and fusion dependencies."},
    {"rule_id": "SG-122-06", "name": "Validation Dependency Mapping", "description": "Require no-lookahead, forbidden column, and causality check prerequisites."},
    {"rule_id": "SG-122-07", "name": "Quality Dependency Mapping", "description": "Require missingness, infinite value, and drift readiness prerequisites."},
    {"rule_id": "SG-122-08", "name": "Metadata-Only News Factors", "description": "Use solely frequency counts, tags, and category metadata for news."},
    {"rule_id": "SG-122-09", "name": "Regime Prep Placeholders", "description": "Structure candidate feature groups as research inputs for Phase 126+."},
    {"rule_id": "SG-122-10", "name": "Non-Destructive Manual Review", "description": "Queue anomalies and placeholders for human review without data loss."},
    {"rule_id": "SG-122-11", "name": "Phase 123 Drift Handoff", "description": "Provide complete factor inventory ready for drift and quality diagnostics."},
]


def build_factor_metadata_no_go_conditions(
    profile: FactorMetadataProfile | None = None,
) -> pd.DataFrame:
    """Return DataFrame of NO-GO safety constraints."""
    records = []
    for r in NO_GO_RULES:
        records.append(
            {
                "rule_id": r["rule_id"],
                "rule_type": "NO_GO",
                "name": r["name"],
                "description": r["description"],
                "enforcement": "STRICT_BARRIER",
                "non_signal": True,
            }
        )
    return pd.DataFrame(records)


def build_factor_metadata_safe_go_conditions(
    profile: FactorMetadataProfile | None = None,
) -> pd.DataFrame:
    """Return DataFrame of SAFE-GO operating principles."""
    records = []
    for r in SAFE_GO_RULES:
        records.append(
            {
                "rule_id": r["rule_id"],
                "rule_type": "SAFE_GO",
                "name": r["name"],
                "description": r["description"],
                "enforcement": "MANDATORY_PRACTICE",
                "non_signal": True,
            }
        )
    return pd.DataFrame(records)


def build_factor_metadata_safety_boundary(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build combined Safety Boundary DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    df_no_go = build_factor_metadata_no_go_conditions(active_profile)
    df_safe_go = build_factor_metadata_safe_go_conditions(active_profile)
    combined_df = pd.concat([df_no_go, df_safe_go], ignore_index=True)

    summary = {
        "active_profile": active_profile.name,
        "safety_status": "SECURE",
        "no_go_count": len(df_no_go),
        "safe_go_count": len(df_safe_go),
        "total_rules": len(combined_df),
        "destructive_action_allowed": False,
        "non_signal": True,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
    }
    return combined_df, summary


def summarize_factor_metadata_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    no_go = int((df["rule_type"] == "NO_GO").sum()) if "rule_type" in df else 0
    safe_go = int((df["rule_type"] == "SAFE_GO").sum()) if "rule_type" in df else 0
    return {
        "total_rules": len(df),
        "no_go_count": no_go,
        "safe_go_count": safe_go,
        "destructive_action_allowed": False,
        "non_signal": True,
        "safety_status": "SECURE",
    }
