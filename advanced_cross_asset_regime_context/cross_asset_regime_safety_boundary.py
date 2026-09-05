"""Phase 131: Cross-Asset Regime Safety Boundary Enforcement.

Defines strict operational safety boundaries, 18 NO-GO prohibitive conditions,
and 8 SAFE-GO approved principles for Phase 131 Cross-Asset Regime Context Expansion.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

NO_GO_CONDITIONS: List[Dict[str, Any]] = [
    {"rule_id": "nogo_live_trading", "rule_name": "No Live Trading", "category": "execution", "status": "ENFORCED"},
    {"rule_id": "nogo_broker_integration", "rule_name": "No Broker Integration", "category": "connectivity", "status": "ENFORCED"},
    {"rule_id": "nogo_real_orders", "rule_name": "No Real Orders", "category": "execution", "status": "ENFORCED"},
    {"rule_id": "nogo_investment_advice", "rule_name": "No Investment Advice", "category": "compliance", "status": "ENFORCED"},
    {"rule_id": "nogo_context_as_signal", "rule_name": "No Cross-Asset Context as Signal", "category": "analytics", "status": "ENFORCED"},
    {"rule_id": "nogo_correlation_as_signal", "rule_name": "No Correlation as Signal", "category": "analytics", "status": "ENFORCED"},
    {"rule_id": "nogo_divergence_as_signal", "rule_name": "No Divergence as Signal", "category": "analytics", "status": "ENFORCED"},
    {"rule_id": "nogo_directional_claims", "rule_name": "No Directional Claims", "category": "claims", "status": "ENFORCED"},
    {"rule_id": "nogo_strategy_backtest", "rule_name": "No Strategy / Backtest / Optimizer", "category": "modeling", "status": "ENFORCED"},
    {"rule_id": "nogo_model_training", "rule_name": "No Model Training", "category": "ml_execution", "status": "ENFORCED"},
    {"rule_id": "nogo_model_fit_predict", "rule_name": "No Model Fit / Inference", "category": "ml_execution", "status": "ENFORCED"},
    {"rule_id": "nogo_clustering_execution", "rule_name": "No Clustering / Unsupervised Fit", "category": "ml_execution", "status": "ENFORCED"},
    {"rule_id": "nogo_target_label_prediction", "rule_name": "No Target / Label / Prediction", "category": "data_engineering", "status": "ENFORCED"},
    {"rule_id": "nogo_commercial_claims", "rule_name": "No Official Approval / Production Ready Claims", "category": "claims", "status": "ENFORCED"},
    {"rule_id": "nogo_source_overwrite", "rule_name": "No Source Overwrite / Destructive Actions", "category": "governance", "status": "ENFORCED"},
    {"rule_id": "nogo_auto_imputation_drop", "rule_name": "No Auto-Imputation / Auto-Feature-Drop", "category": "data_engineering", "status": "ENFORCED"},
    {"rule_id": "nogo_full_article_scraping", "rule_name": "No Full Article Text / Scraping / NLP Sentiment", "category": "compliance", "status": "ENFORCED"},
    {"rule_id": "nogo_credential_deployment", "rule_name": "No Credential Output / Cloud Deployment", "category": "security", "status": "ENFORCED"},
]

SAFE_GO_CONDITIONS: List[Dict[str, Any]] = [
    {"rule_id": "safego_local_offline", "rule_name": "Local/Offline Cross-Asset Context", "status": "ACTIVE"},
    {"rule_id": "safego_non_signal_registries", "rule_name": "Non-Signal Entity/Pair Registries", "status": "ACTIVE"},
    {"rule_id": "safego_fx_cmd_macro_context", "rule_name": "FX/Commodity/Macro Context Mapping", "status": "ACTIVE"},
    {"rule_id": "safego_no_lookahead_contracts", "rule_name": "Timestamp/No-Lookahead Guarded Contracts", "status": "ACTIVE"},
    {"rule_id": "safego_metadata_news", "rule_name": "Metadata-Only News Context", "status": "ACTIVE"},
    {"rule_id": "safego_placeholders_only", "rule_name": "Correlation/Lead-Lag Placeholders Without Prediction", "status": "ACTIVE"},
    {"rule_id": "safego_source_preservation", "rule_name": "Source-Preserved Cross-Asset Manifest", "status": "ACTIVE"},
    {"rule_id": "safego_phase_132_handoff", "rule_name": "Phase 132 Macro/Event/News Context Handoff", "status": "ACTIVE"},
]


def build_cross_asset_regime_no_go_conditions(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> pd.DataFrame:
    """Build NO-GO condition records dataframe."""
    return pd.DataFrame(NO_GO_CONDITIONS)


def build_cross_asset_regime_safe_go_conditions(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> pd.DataFrame:
    """Build SAFE-GO principle records dataframe."""
    return pd.DataFrame(SAFE_GO_CONDITIONS)


def build_cross_asset_regime_safety_boundary(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build unified safety boundary dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    no_go_df = build_cross_asset_regime_no_go_conditions(profile)
    summary = summarize_cross_asset_regime_safety_boundary(no_go_df)
    summary["active_profile"] = profile.profile_name
    return no_go_df, summary


def summarize_cross_asset_regime_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary state."""
    total_nogo = len(df)
    total_safego = len(SAFE_GO_CONDITIONS)
    all_enforced = bool((df["status"] == "ENFORCED").all()) if not df.empty else True

    return {
        "no_go_count": total_nogo,
        "safe_go_count": total_safego,
        "all_no_go_enforced": all_enforced,
        "safety_status": "SECURE" if all_enforced else "BREACH",
        "live_trading_allowed": False,
        "model_execution_allowed": False,
        "non_signal": True,
        "source_preserved": True,
    }
