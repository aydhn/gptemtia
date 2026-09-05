"""Phase 129: Market Behavior Diagnostics Safety Boundary.

Defines NO-GO boundaries (prohibited operations) and SAFE-GO principles (permitted research actions).
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)

NO_GO_RULES = [
    ("no_live_trading", "Live order placement or direct market execution is strictly prohibited."),
    ("no_broker_integration", "Broker API connection or exchange credential usage is strictly prohibited."),
    ("no_real_order", "Real position opening or financial commitment is forbidden."),
    ("no_investment_advice", "Generation of financial or investment advice is strictly prohibited."),
    ("no_quality_as_signal", "Using behavior quality metrics as trading or execution signals is forbidden."),
    ("no_behavior_as_signal", "Using market behavior diagnostics as trade directional triggers is forbidden."),
    ("no_candidate_state_as_signal", "Using candidate states or pseudo-states as strategy rules is forbidden."),
    ("no_directional_certainty", "Generating directional claims such as bullish, bearish, long, or short is forbidden."),
    ("no_strategy_backtest_optimizer", "Executing backtesting engines, strategy routers, or optimizers is forbidden."),
    ("no_model_training_fit_predict", "Executing model fit, train, predict, or transform is strictly prohibited."),
    ("no_clustering_execution", "Running KMeans, DBSCAN, GMM, HDBSCAN, or SOM algorithms is forbidden."),
    ("no_dimensionality_reduction", "Executing PCA, UMAP, or t-SNE algorithms is forbidden."),
    ("no_target_label_generation", "Creating supervised target variables or forward labels is forbidden."),
    ("no_official_approval_claim", "Claiming official accreditation or regulatory endorsement is forbidden."),
    ("no_production_ready_claim", "Claiming production readiness or live deployment eligibility is forbidden."),
    ("no_broker_ready_claim", "Claiming broker readiness or platform certification is forbidden."),
    ("no_source_overwrite_or_deletion", "Overwriting or deleting raw/source tables or logs is strictly forbidden."),
    ("no_auto_imputation_or_feature_drop", "Destructive cleaning, automatic imputation, or column dropping is forbidden."),
    ("no_full_article_scraping", "Downloading or storing copyrighted news body text or scraping is forbidden."),
    ("no_credential_leakage", "Logging or writing API keys, tokens, or credentials is forbidden."),
    ("no_deployment", "Production deployment, cloud publishing, or docker pushing is forbidden."),
]

SAFE_GO_PRINCIPLES = [
    ("local_offline_diagnostics", "Conduct local, offline, dry-run compliant behavior quality diagnostics."),
    ("non_signal_quality_reports", "Produce non-signal candidate state quality and pseudo-state completeness reports."),
    ("candidate_diagnostics", "Evaluate candidate coverage, consistency, ambiguity, and stability diagnostically."),
    ("regime_family_diagnostics", "Assess regime family quality, coverage, and factor dependency health."),
    ("multi_domain_diagnostics", "Generate volatility, trend, range, macro, news, and cross-asset behavior diagnostics."),
    ("metadata_only_news_diagnostics", "Inspect news attention and event linkages strictly at headline/topic metadata level."),
    ("source_preserved_manifest", "Record immutable audit manifests maintaining full source preservation."),
    ("phase_130_transition_handoff", "Deliver clean, validation-aware prerequisites for Phase 130 transition analysis."),
]


def build_market_behavior_diagnostics_no_go_conditions(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> pd.DataFrame:
    """Return DataFrame of NO-GO safety rules."""
    rows = [
        {"rule_name": name, "rule_type": "NO_GO", "description": desc, "enforced": True, "non_signal": True}
        for name, desc in NO_GO_RULES
    ]
    return pd.DataFrame(rows)


def build_market_behavior_diagnostics_safe_go_conditions(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> pd.DataFrame:
    """Return DataFrame of SAFE-GO principles."""
    rows = [
        {"principle_name": name, "rule_type": "SAFE_GO", "description": desc, "active": True, "non_signal": True}
        for name, desc in SAFE_GO_PRINCIPLES
    ]
    return pd.DataFrame(rows)


def build_market_behavior_diagnostics_safety_boundary(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build unified safety boundary report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    no_go_df = build_market_behavior_diagnostics_no_go_conditions(profile)
    safe_go_df = build_market_behavior_diagnostics_safe_go_conditions(profile)

    combined_rows = []
    for _, r in no_go_df.iterrows():
        combined_rows.append(
            {
                "rule_name": r["rule_name"],
                "rule_type": "NO_GO",
                "description": r["description"],
                "is_active": True,
                "non_signal": True,
            }
        )
    for _, r in safe_go_df.iterrows():
        combined_rows.append(
            {
                "rule_name": r["principle_name"],
                "rule_type": "SAFE_GO",
                "description": r["description"],
                "is_active": True,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(combined_rows)
    summary = summarize_market_behavior_diagnostics_safety_boundary(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_market_behavior_diagnostics_safety_boundary(df: pd.DataFrame) -> dict:
    """Summarize safety boundary rules."""
    if df.empty:
        return {
            "safety_status": "UNKNOWN",
            "no_go_count": 0,
            "safe_go_count": 0,
            "non_signal": True,
        }
    no_go_count = int((df["rule_type"] == "NO_GO").sum()) if "rule_type" in df.columns else 0
    safe_go_count = int((df["rule_type"] == "SAFE_GO").sum()) if "rule_type" in df.columns else 0
    return {
        "safety_status": "SECURE",
        "no_go_count": no_go_count,
        "safe_go_count": safe_go_count,
        "total_rules": len(df),
        "non_signal": True,
    }
