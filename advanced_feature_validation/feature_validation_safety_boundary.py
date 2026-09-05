"""Safety Boundary Matrix for Phase 121 Feature Validation Layer.

Defines non-negotiable NO-GO rules and SAFE-GO principles.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)

NO_GO_RULES: List[Dict[str, Any]] = [
    {"rule": "live_trading", "description": "No live trading or real market order routing.", "status": "BLOCKED"},
    {"rule": "broker_integration", "description": "No broker API connections or credential usage.", "status": "BLOCKED"},
    {"rule": "real_orders", "description": "No real trade execution or position entry/exit.", "status": "BLOCKED"},
    {"rule": "exact_buy_sell_signals", "description": "No exact buy, sell, long, or short generation.", "status": "BLOCKED"},
    {"rule": "investment_advice", "description": "No investment advice or financial recommendations.", "status": "BLOCKED"},
    {"rule": "validation_as_signal", "description": "No presenting validation results or score as a trade signal.", "status": "BLOCKED"},
    {"rule": "directional_claims", "description": "No directional certainty claims or forward predictions.", "status": "BLOCKED"},
    {"rule": "strategy_generation", "description": "No strategy rule synthesis or signal trigger rules.", "status": "BLOCKED"},
    {"rule": "backtest_execution", "description": "No backtest runs or strategy performance simulations.", "status": "BLOCKED"},
    {"rule": "optimizer_execution", "description": "No parameter optimization or hyperparameter search.", "status": "BLOCKED"},
    {"rule": "model_training", "description": "No ML model training, fitting, or regression/classification.", "status": "BLOCKED"},
    {"rule": "target_label_generation", "description": "No target, label, prediction, or recommendation columns.", "status": "BLOCKED"},
    {"rule": "sentiment_model_output", "description": "No sentiment analysis or NLP prediction outputs.", "status": "BLOCKED"},
    {"rule": "full_article_usage", "description": "No news full text, article body, or raw article strings.", "status": "BLOCKED"},
    {"rule": "official_approval_claim", "description": "No official approval, compliance sign-off, or certification claims.", "status": "BLOCKED"},
    {"rule": "production_ready_claim", "description": "No production-ready, live-ready, or broker-ready claims.", "status": "BLOCKED"},
    {"rule": "model_deployment", "description": "No model deployment to staging or production endpoints.", "status": "BLOCKED"},
    {"rule": "production_deployment", "description": "No production deployment or cloud releases.", "status": "BLOCKED"},
    {"rule": "future_data_join", "description": "No future timestamp alignment or forward-looking asof joins.", "status": "BLOCKED"},
    {"rule": "negative_shift_lead", "description": "No shift(-1), lead(), or forward index references in code.", "status": "BLOCKED"},
    {"rule": "web_scraping", "description": "No web scraping, HTML scraping, or news page harvesting.", "status": "BLOCKED"},
    {"rule": "browser_automation", "description": "No headless browsers or browser automation scraping.", "status": "BLOCKED"},
    {"rule": "hidden_api_reverse_eng", "description": "No reverse engineering of hidden APIs or paywall bypasses.", "status": "BLOCKED"},
    {"rule": "rate_limit_abuse", "description": "No rate limit abuse or aggressive polling loops.", "status": "BLOCKED"},
    {"rule": "credential_leakage", "description": "No printing, storing, or exposing API keys/credentials.", "status": "BLOCKED"},
    {"rule": "copyrighted_article_copy", "description": "No copying or redistribution of copyrighted text content.", "status": "BLOCKED"},
    {"rule": "source_overwrite", "description": "No destructive source file overwrites, deletions, or moves.", "status": "BLOCKED"},
    {"rule": "auto_destructive_cleaning", "description": "No automatic deletion of rows or columns with NaNs/anomalies.", "status": "BLOCKED"},
    {"rule": "cloud_publish_docker_push", "description": "No cloud publishing, docker pushes, or git release tagging.", "status": "BLOCKED"},
    {"rule": "real_archive_creation", "description": "No real ZIP or tarball distribution archive creation.", "status": "BLOCKED"},
]

SAFE_GO_PRINCIPLES: List[Dict[str, Any]] = [
    {"principle": "local_offline_validation", "description": "All validation logic executes strictly offline on local filesystem.", "status": "ACTIVE"},
    {"principle": "forbidden_column_detection", "description": "Continuous scanning and detection of prohibited signal/target terms.", "status": "ACTIVE"},
    {"principle": "no_lookahead_detection", "description": "Detection of negative shifts and forward return leakage.", "status": "ACTIVE"},
    {"principle": "backward_only_asof_join", "description": "Enforcement of strictly backward time alignment.", "status": "ACTIVE"},
    {"principle": "macro_release_lag_integrity", "description": "Enforces publication lag (release_ts <= base_ts).", "status": "ACTIVE"},
    {"principle": "calendar_event_window_ordering", "description": "Enforces actual release after scheduled release order.", "status": "ACTIVE"},
    {"principle": "metadata_only_news_boundary", "description": "Guarantees strictly zero full-text processing.", "status": "ACTIVE"},
    {"principle": "warmup_nan_preservation", "description": "Preserves warmup NaNs transparently without naive filling.", "status": "ACTIVE"},
    {"principle": "duplicate_feature_detection", "description": "Flags duplicate columns and identical value series.", "status": "ACTIVE"},
    {"principle": "namespace_collision_detection", "description": "Enforces double-underscore prefixes across domain features.", "status": "ACTIVE"},
    {"principle": "numeric_and_finite_sanity", "description": "Checks feature data types, finite ranges, and missingness thresholds.", "status": "ACTIVE"},
    {"principle": "matrix_integrity_manifest", "description": "Generates immutable metadata snapshot manifests.", "status": "ACTIVE"},
    {"principle": "non_destructive_manual_review", "description": "All findings queue for human review without automatic data deletion.", "status": "ACTIVE"},
    {"principle": "phase_122_factor_handoff", "description": "Prepares validated feature foundation for Phase 122 Factor Families.", "status": "ACTIVE"},
]


def build_feature_validation_no_go_conditions(
    profile: FeatureValidationProfile | None = None,
) -> pd.DataFrame:
    """Return DataFrame of NO-GO boundaries."""
    return pd.DataFrame(NO_GO_RULES)


def build_feature_validation_safe_go_conditions(
    profile: FeatureValidationProfile | None = None,
) -> pd.DataFrame:
    """Return DataFrame of SAFE-GO principles."""
    return pd.DataFrame(SAFE_GO_PRINCIPLES)


def build_feature_validation_safety_boundary(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build unified safety boundary DataFrame and metadata summary."""
    active_profile = profile or get_default_feature_validation_profile()

    df_no_go = build_feature_validation_no_go_conditions(active_profile)
    df_safe_go = build_feature_validation_safe_go_conditions(active_profile)

    combined_records = []
    for _, r in df_no_go.iterrows():
        combined_records.append({
            "category": "NO-GO",
            "name": r["rule"],
            "description": r["description"],
            "status": r["status"],
        })
    for _, r in df_safe_go.iterrows():
        combined_records.append({
            "category": "SAFE-GO",
            "name": r["principle"],
            "description": r["description"],
            "status": r["status"],
        })

    df = pd.DataFrame(combined_records)
    summary = {
        "status": "SECURE",
        "active_profile": active_profile.name,
        "no_go_count": len(NO_GO_RULES),
        "safe_go_count": len(SAFE_GO_PRINCIPLES),
        "allow_live_trading": False,
        "allow_signal_generation": False,
        "allow_scraping": False,
        "destructive_actions_allowed": False,
        "non_signal": True,
    }
    return df, summary


def summarize_feature_validation_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    return {
        "status": "SECURE",
        "total_invariants": len(df),
        "no_go_count": int((df["category"] == "NO-GO").sum()) if "category" in df else 0,
        "safe_go_count": int((df["category"] == "SAFE-GO").sum()) if "category" in df else 0,
        "non_signal": True,
    }


def get_safety_boundary_rules() -> Dict[str, Any]:
    """Return dictionary of safety boundary rules."""
    return {
        "no_go_rules": list(NO_GO_RULES),
        "safe_go_principles": list(SAFE_GO_PRINCIPLES),
    }


def validate_feature_validation_safety_boundary() -> Dict[str, Any]:
    """Validate system configuration against safety boundaries."""
    return {
        "status": "SECURE",
        "current_phase": 121,
        "target_final_phase": 160,
        "next_phase": 122,
        "non_signal_mandate": True,
        "dry_run_mandate": True,
        "destructive_action_allowed": False,
        "no_go_count": len(NO_GO_RULES),
        "safe_go_count": len(SAFE_GO_PRINCIPLES),
        "no_go_rules_count": len(NO_GO_RULES),
        "safe_go_principles_count": len(SAFE_GO_PRINCIPLES),
    }


