"""Phase 126: Regime Foundation Safety Boundary.

Defines NO-GO conditions and SAFE-GO principles governing Phase 126 execution.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

NO_GO_CONDITIONS: List[Dict[str, Any]] = [
    {"rule_id": "nogo_01", "name": "prohibit_live_trading", "category": "execution", "description": "No live exchange connection or trade order dispatch"},
    {"rule_id": "nogo_02", "name": "prohibit_broker_integration", "category": "execution", "description": "No broker API binding or credentials"},
    {"rule_id": "nogo_03", "name": "prohibit_real_order", "category": "execution", "description": "No real money or paper trading order generation"},
    {"rule_id": "nogo_04", "name": "prohibit_investment_advice", "category": "regulatory", "description": "No financial recommendation or asset advisory"},
    {"rule_id": "nogo_05", "name": "prohibit_regime_as_signal", "category": "signal", "description": "No treating regime state values as BUY/SELL triggers"},
    {"rule_id": "nogo_06", "name": "prohibit_directional_certainty", "category": "signal", "description": "No asserting bullish/bearish directional certainty"},
    {"rule_id": "nogo_07", "name": "prohibit_strategy_and_backtest", "category": "strategy", "description": "No strategy generation, backtesting, or optimizer runs"},
    {"rule_id": "nogo_08", "name": "prohibit_model_training", "category": "modeling", "description": "No unsupervised clustering or supervised model training"},
    {"rule_id": "nogo_09", "name": "prohibit_target_and_predictions", "category": "modeling", "description": "No future target generation or return predictions"},
    {"rule_id": "nogo_10", "name": "prohibit_official_and_prod_claims", "category": "governance", "description": "No claims of official approval, broker-ready, or production-ready"},
    {"rule_id": "nogo_11", "name": "prohibit_source_overwrite", "category": "storage", "description": "No destructive cleaning, file deletion, or overwriting raw data"},
    {"rule_id": "nogo_12", "name": "prohibit_auto_imputation_drop", "category": "data_integrity", "description": "No automatic column drop or silent NaN filling"},
    {"rule_id": "nogo_13", "name": "prohibit_full_article_news", "category": "content", "description": "No full article text, copyrighted scraping, or embeddings"},
    {"rule_id": "nogo_14", "name": "prohibit_web_scraping", "category": "network", "description": "No active web scraping or browser automation"},
    {"rule_id": "nogo_15", "name": "prohibit_cloud_and_docker_push", "category": "deployment", "description": "No cloud publishing, docker push, git tags, or archives"},
]

SAFE_GO_CONDITIONS: List[Dict[str, Any]] = [
    {"rule_id": "safego_01", "name": "local_offline_regime_taxonomy", "category": "taxonomy", "description": "Permit local, offline market behavior and regime state taxonomies"},
    {"rule_id": "safego_02", "name": "non_signal_regime_schema", "category": "schema", "description": "Enforce non-signal regime state output schemas with mandatory prefix"},
    {"rule_id": "safego_03", "name": "regime_family_contracts", "category": "contracts", "description": "Formalize volatility, trend, range, and liquidity family contracts"},
    {"rule_id": "safego_04", "name": "validation_aware_dependencies", "category": "validation", "description": "Link Phase 121 no-lookahead and timestamp validation requirements"},
    {"rule_id": "safego_05", "name": "quality_aware_dependencies", "category": "quality", "description": "Enforce Phase 123 quality and drift diagnostic prerequisites"},
    {"rule_id": "safego_06", "name": "metadata_only_news_context", "category": "content", "description": "Maintain strictly metadata-only news attention metrics"},
    {"rule_id": "safego_07", "name": "feature_store_dependency_mapping", "category": "feature_store", "description": "Map central Feature Store catalog references without mutation"},
    {"rule_id": "safego_08", "name": "phase_127_matrix_handoff", "category": "handoff", "description": "Deliver structured prerequisites to Phase 127 Regime Feature Matrix"},
]


def build_regime_foundation_no_go_conditions(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for NO-GO conditions."""
    df = pd.DataFrame(NO_GO_CONDITIONS)
    return df, {"total_no_go_rules": len(df), "all_enforced": True, "non_signal": True}


def build_regime_foundation_safe_go_conditions(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for SAFE-GO principles."""
    df = pd.DataFrame(SAFE_GO_CONDITIONS)
    return df, {"total_safe_go_rules": len(df), "all_active": True, "non_signal": True}


def build_regime_foundation_safety_boundary(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build unified DataFrame and summary for safety boundaries."""
    active_profile = profile or get_default_regime_foundation_profile()
    df_nogo, s_nogo = build_regime_foundation_no_go_conditions(active_profile)
    df_safego, s_safego = build_regime_foundation_safe_go_conditions(active_profile)

    combined_rows = []
    for _, r in df_nogo.iterrows():
        combined_rows.append({**r.to_dict(), "boundary_type": "NO_GO", "status": "ENFORCED"})
    for _, r in df_safego.iterrows():
        combined_rows.append({**r.to_dict(), "boundary_type": "SAFE_GO", "status": "ACTIVE"})

    df = pd.DataFrame(combined_rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_rules": len(df),
        "no_go_count": len(df_nogo),
        "safe_go_count": len(df_safego),
        "safety_status": "SECURE",
        "non_signal": True,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_regime_foundation_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    return {
        "total_rules": len(df),
        "no_go_rules": len(df[df["boundary_type"] == "NO_GO"]) if "boundary_type" in df.columns else 0,
        "safe_go_rules": len(df[df["boundary_type"] == "SAFE_GO"]) if "boundary_type" in df.columns else 0,
        "safety_status": "SECURE",
        "non_signal": True,
    }
