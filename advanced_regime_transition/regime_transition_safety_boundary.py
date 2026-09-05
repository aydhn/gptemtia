"""Phase 130: Regime Transition Safety Boundary.

Enforces explicit NO-GO boundaries and SAFE-GO principles for the Phase 130
Regime Transition and Stability Analysis layer.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

NO_GO_CONDITIONS: List[Dict[str, Any]] = [
    {"rule_type": "NO-GO", "condition": "live_trading", "description": "Strictly no connection to live execution brokers or account orders"},
    {"rule_type": "NO-GO", "condition": "broker_integration", "description": "No broker API bindings, authentication, or protocol connections"},
    {"rule_type": "NO-GO", "condition": "real_orders", "description": "No placement, simulation, or transmission of live financial orders"},
    {"rule_type": "NO-GO", "condition": "investment_advice", "description": "No financial, investment, or legal trade recommendations"},
    {"rule_type": "NO-GO", "condition": "transition_as_signal", "description": "No presentation of transition diagnostics as trading signals"},
    {"rule_type": "NO-GO", "condition": "stability_as_signal", "description": "No interpretation of stability scores as trade entry/exit triggers"},
    {"rule_type": "NO-GO", "condition": "directional_claim", "description": "No directional bias or market certainty claims"},
    {"rule_type": "NO-GO", "condition": "strategy_backtest_optimizer", "description": "No strategy generation, portfolio backtest, or parameter optimization"},
    {"rule_type": "NO-GO", "condition": "model_training_fit_predict", "description": "No model training, fitting, predicting, or ML inference execution"},
    {"rule_type": "NO-GO", "condition": "clustering_unsupervised", "description": "No KMeans, DBSCAN, GMM, HDBSCAN, SOM, PCA, or UMAP execution"},
    {"rule_type": "NO-GO", "condition": "target_label_generation", "description": "No generation of supervised machine learning target labels"},
    {"rule_type": "NO-GO", "condition": "production_broker_approval", "description": "No claims of official approval, production-ready, or broker-ready status"},
    {"rule_type": "NO-GO", "condition": "source_overwrite_destruction", "description": "No destructive file modifications or overwriting raw source inputs"},
    {"rule_type": "NO-GO", "condition": "auto_imputation_feature_drop", "description": "No automated data imputation or silent dropping of features"},
    {"rule_type": "NO-GO", "condition": "full_article_scraping", "description": "No scraping, HTML parsing, or full text article ingestion"},
    {"rule_type": "NO-GO", "condition": "credentials_exposure", "description": "No credential, API key, token, or secret exposure in outputs"},
    {"rule_type": "NO-GO", "condition": "deployment_execution", "description": "No production deployment, docker push, git tagging, or cloud publishing"},
    {"rule_type": "NO-GO", "condition": "lookahead_leakage", "description": "No future returns, forward deltas, or negative shifts (shift(-1))"},
]

SAFE_GO_CONDITIONS: List[Dict[str, Any]] = [
    {"rule_type": "SAFE-GO", "condition": "local_offline_sequence_contracts", "description": "Local, offline contracts governing candidate/pseudo state sequences"},
    {"rule_type": "SAFE-GO", "condition": "non_signal_transition_diagnostics", "description": "Purely non-signal transition frequency, rate, and ambiguity diagnostics"},
    {"rule_type": "SAFE-GO", "condition": "persistence_continuity_stability", "description": "Descriptive persistence run-lengths, continuity, and stability indices"},
    {"rule_type": "SAFE-GO", "condition": "metadata_only_news_context", "description": "Topic tags, headline metadata frequency, and publication timestamp lags only"},
    {"rule_type": "SAFE-GO", "condition": "cross_asset_transition_prep", "description": "Cross-asset currency/commodity alignment prep for Phase 131"},
    {"rule_type": "SAFE-GO", "condition": "no_lookahead_enforcement", "description": "Strict monotonic chronological ordering and historical-only joins"},
    {"rule_type": "SAFE-GO", "condition": "source_preservation_manifest", "description": "Immutable source preservation and integrity manifest auditing"},
    {"rule_type": "SAFE-GO", "condition": "phase_131_handoff", "description": "Formal handoff report transitioning cleanly to Phase 131 Cross-Asset Context"},
]


def build_regime_transition_no_go_conditions(
    profile: Optional[RegimeTransitionProfile] = None,
) -> pd.DataFrame:
    """Return dataframe of all NO-GO rules."""
    rows = []
    for i, c in enumerate(NO_GO_CONDITIONS):
        row = dict(c)
        row["rule_id"] = f"NO-GO-{i+1:03d}"
        row["is_active"] = True
        rows.append(row)
    return pd.DataFrame(rows)


def build_regime_transition_safe_go_conditions(
    profile: Optional[RegimeTransitionProfile] = None,
) -> pd.DataFrame:
    """Return dataframe of all SAFE-GO principles."""
    rows = []
    for i, c in enumerate(SAFE_GO_CONDITIONS):
        row = dict(c)
        row["rule_id"] = f"SAFE-GO-{i+1:03d}"
        row["is_active"] = True
        rows.append(row)
    return pd.DataFrame(rows)


def build_regime_transition_safety_boundary(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build unified safety boundary dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df_nogo = build_regime_transition_no_go_conditions(profile)
    df_safego = build_regime_transition_safe_go_conditions(profile)
    df = pd.concat([df_nogo, df_safego], ignore_index=True)
    summary = summarize_regime_transition_safety_boundary(df)
    summary["active_profile"] = profile.profile_name
    return df, summary



def summarize_regime_transition_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary rules."""
    no_go_count = int((df["rule_type"] == "NO-GO").sum()) if not df.empty and "rule_type" in df.columns else len(NO_GO_CONDITIONS)
    safe_go_count = int((df["rule_type"] == "SAFE-GO").sum()) if not df.empty and "rule_type" in df.columns else len(SAFE_GO_CONDITIONS)
    return {
        "total_safety_rules": len(df),
        "no_go_count": no_go_count,
        "safe_go_count": safe_go_count,
        "safety_status": "SECURE",
        "live_trading_prohibited": True,
        "zero_model_execution": True,
        "non_signal_mandate": True,
    }
