"""Phase 132: Macro/Event/News Regime Safety Boundary (Strict NO-GO & SAFE-GO)."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

NO_GO_RULES: List[Dict[str, str]] = [
    {"rule_id": "nogo_01", "name": "live_trading", "desc": "Live execution or automated order transmission prohibited."},
    {"rule_id": "nogo_02", "name": "broker_integration", "desc": "Broker API connection or account routing prohibited."},
    {"rule_id": "nogo_03", "name": "real_orders", "desc": "Placing real money capital at risk prohibited."},
    {"rule_id": "nogo_04", "name": "investment_advice", "desc": "Offering buy/sell/hold investment recommendations prohibited."},
    {"rule_id": "nogo_05", "name": "macro_context_as_signal", "desc": "Using macro levels or changes directly as trade signals prohibited."},
    {"rule_id": "nogo_06", "name": "event_context_as_signal", "desc": "Using calendar releases or event windows as trade triggers prohibited."},
    {"rule_id": "nogo_07", "name": "news_context_as_signal", "desc": "Using news topic attention or tags as trade triggers prohibited."},
    {"rule_id": "nogo_08", "name": "directional_claims", "desc": "Making certainty claims on market directions prohibited."},
    {"rule_id": "nogo_09", "name": "strategy_backtest_optimizer", "desc": "Running automated strategy backtests or optimizers prohibited."},
    {"rule_id": "nogo_10", "name": "model_training_fit_predict", "desc": "Fitting machine learning models or generating predictions prohibited."},
    {"rule_id": "nogo_11", "name": "clustering_unsupervised_execution", "desc": "Running live unsupervised clustering execution prohibited."},
    {"rule_id": "nogo_12", "name": "target_label_generation", "desc": "Generating supervised target labels or return shifts prohibited."},
    {"rule_id": "nogo_13", "name": "sentiment_model_output", "desc": "Running sentiment models or producing positive/negative scores prohibited."},
    {"rule_id": "nogo_14", "name": "full_article_content_usage", "desc": "Storing or ingesting full article body or scraped HTML prohibited."},
    {"rule_id": "nogo_15", "name": "embeddings_vector_database", "desc": "Generating neural embeddings or writing to vector DB prohibited."},
    {"rule_id": "nogo_16", "name": "production_broker_approval", "desc": "Claiming official approval, production-ready, or broker-ready prohibited."},
    {"rule_id": "nogo_17", "name": "source_overwrite_destruction", "desc": "Destructive data cleaning or file overwriting prohibited."},
    {"rule_id": "nogo_18", "name": "auto_imputation_feature_drop", "desc": "Automated data imputation or silent feature dropping prohibited."},
    {"rule_id": "nogo_19", "name": "scraping_and_credentials", "desc": "Web scraping or outputting sensitive credentials prohibited."},
    {"rule_id": "nogo_20", "name": "deployment_execution", "desc": "Production or cloud deployment execution prohibited."},
]

SAFE_GO_RULES: List[Dict[str, str]] = [
    {"rule_id": "safego_01", "name": "local_offline_context", "desc": "Operating in local/offline dry-run research mode."},
    {"rule_id": "safego_02", "name": "non_signal_macro_context", "desc": "Reporting macro indicator and release context without signal generation."},
    {"rule_id": "safego_03", "name": "non_signal_calendar_context", "desc": "Observing calendar events and event windows non-predictively."},
    {"rule_id": "safego_04", "name": "metadata_only_news_context", "desc": "Using only news metadata tags, topics, timestamps, and sources."},
    {"rule_id": "safego_05", "name": "scheduled_actual_alignment", "desc": "Verifying actual release timestamps to prevent forward lookahead."},
    {"rule_id": "safego_06", "name": "backward_only_asof_joins", "desc": "Enforcing strictly backward time-series joining on right <= left."},
    {"rule_id": "safego_07", "name": "no_lookahead_guards", "desc": "Preventing negative shifts and forward return leakage."},
    {"rule_id": "safego_08", "name": "source_preserved_manifest", "desc": "Maintaining immutable lineage and source preservation manifest."},
    {"rule_id": "safego_09", "name": "phase_133_handoff", "desc": "Providing structured acceptance handoff to Phase 133."},
]


def build_macro_event_news_regime_no_go_conditions(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of enforced NO-GO boundaries."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in NO_GO_RULES:
        row = dict(item)
        row["category"] = "NO_GO"
        row["is_enforced"] = True
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    return df, {"total_no_go_rules": len(df), "all_enforced": True}


def build_macro_event_news_regime_safe_go_conditions(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of validated SAFE-GO operational principles."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in SAFE_GO_RULES:
        row = dict(item)
        row["category"] = "SAFE_GO"
        row["is_active"] = True
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    return df, {"total_safe_go_rules": len(df), "all_active": True}


def build_macro_event_news_regime_safety_boundary(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build consolidated safety boundary DataFrame."""
    p = profile or get_macro_event_news_regime_profile()
    no_go_df, _ = build_macro_event_news_regime_no_go_conditions(p)
    safe_go_df, _ = build_macro_event_news_regime_safe_go_conditions(p)
    df = pd.concat([no_go_df, safe_go_df], ignore_index=True)

    summary = {
        "safety_status": "SECURE",
        "no_go_count": len(no_go_df),
        "safe_go_count": len(safe_go_df),
        "total_rules": len(df),
        "live_trading_prohibited": True,
        "zero_model_execution": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_event_news_regime_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for safety boundary DataFrame."""
    no_go = int((df["category"] == "NO_GO").sum()) if "category" in df.columns else 0
    safe_go = int((df["category"] == "SAFE_GO").sum()) if "category" in df.columns else 0
    return {
        "total_safety_rules": len(df),
        "no_go_count": no_go,
        "safe_go_count": safe_go,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
