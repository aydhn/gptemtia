"""Phase 123 Feature Quality and Drift Safety Boundary.

Defines explicit NO-GO boundaries (strictly prohibited operations) and SAFE-GO
principles (approved offline diagnostic activities) to enforce ironclad research guardrails.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)

NO_GO_CONDITIONS = [
    {"rule_id": "no_live_trading", "category": "execution", "description": "No live trading or real orders."},
    {"rule_id": "no_broker_integration", "category": "execution", "description": "No broker API connections or credentials."},
    {"rule_id": "no_investment_advice", "category": "legal", "description": "No investment recommendations or financial advice."},
    {"rule_id": "no_quality_drift_as_signal", "category": "signal", "description": "Quality and drift metrics must never be treated as trading signals."},
    {"rule_id": "no_directional_claims", "category": "signal", "description": "No long/short or directional assertions derived from drift."},
    {"rule_id": "no_strategy_backtest_training", "category": "ml_strategy", "description": "No strategy rule generation, backtesting, optimizer, or model training."},
    {"rule_id": "no_target_prediction_columns", "category": "features", "description": "No target, label, forecast, or future return columns."},
    {"rule_id": "no_auto_imputation", "category": "data_integrity", "description": "No automated imputation or overwriting of missing/infinite values."},
    {"rule_id": "no_auto_feature_drop", "category": "data_integrity", "description": "No automated dropping of columns or features upon drift/quality defect."},
    {"rule_id": "no_source_overwrite", "category": "storage", "description": "No in-place destructive mutation or overwrite of raw data files."},
    {"rule_id": "no_full_article_news", "category": "content", "description": "No raw article bodies, scraped HTML, or copyrighted text."},
    {"rule_id": "no_scraping_browser_automation", "category": "network", "description": "No web scraping, hidden API bypass, or browser automation."},
    {"rule_id": "no_production_readiness_claims", "category": "governance", "description": "No production approval, sign-off, or deployment readiness claims."},
]

SAFE_GO_CONDITIONS = [
    {"principle_id": "safe_local_offline_diagnostics", "description": "Run strictly local, offline, read-only quality diagnostics."},
    {"principle_id": "safe_missing_inf_detection", "description": "Detect missingness, inf, all-NaN, zero variance, and duplicates."},
    {"principle_id": "safe_distribution_drift_monitoring", "description": "Compute baseline vs current distribution shifts non-destructively."},
    {"principle_id": "safe_rolling_stability_monitoring", "description": "Track rolling statistics without generating trading recommendations."},
    {"principle_id": "safe_factor_family_aggregation", "description": "Audit input availability across all 10 factor families."},
    {"principle_id": "safe_manual_review_queue", "description": "Route diagnostic defects to human analyst queue instead of auto-fixing."},
    {"principle_id": "safe_phase_124_handoff", "description": "Generate immutable metadata and manifests for Phase 124 Feature Store integration."},
]


def build_feature_quality_drift_no_go_conditions(
    profile: FeatureQualityDriftProfile | None = None,
) -> pd.DataFrame:
    """Build DataFrame of enforced NO-GO boundary rules."""
    records = []
    for r in NO_GO_CONDITIONS:
        records.append({
            "rule_id": r["rule_id"],
            "type": "NO_GO",
            "category": r["category"],
            "description": r["description"],
            "enforced": True,
            "non_signal": True,
        })
    return pd.DataFrame(records)


def build_feature_quality_drift_safe_go_conditions(
    profile: FeatureQualityDriftProfile | None = None,
) -> pd.DataFrame:
    """Build DataFrame of permitted SAFE-GO research activities."""
    records = []
    for p in SAFE_GO_CONDITIONS:
        records.append({
            "principle_id": p["principle_id"],
            "type": "SAFE_GO",
            "description": p["description"],
            "active": True,
            "non_signal": True,
        })
    return pd.DataFrame(records)


def build_feature_quality_drift_safety_boundary(
    profile: FeatureQualityDriftProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build comprehensive safety boundary report."""
    active_profile = profile or get_default_feature_quality_drift_profile()
    df_no_go = build_feature_quality_drift_no_go_conditions(active_profile)
    df_safe_go = build_feature_quality_drift_safe_go_conditions(active_profile)

    combined_records = []
    for _, row in df_no_go.iterrows():
        combined_records.append({
            "rule_id": row["rule_id"],
            "type": "NO_GO",
            "description": row["description"],
            "status": "ENFORCED",
        })
    for _, row in df_safe_go.iterrows():
        combined_records.append({
            "rule_id": row["principle_id"],
            "type": "SAFE_GO",
            "description": row["description"],
            "status": "ACTIVE",
        })

    df = pd.DataFrame(combined_records)
    summary = summarize_feature_quality_drift_safety_boundary(df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return df, summary


def summarize_feature_quality_drift_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from safety boundary DataFrame."""
    if df.empty:
        return {
            "total_rules": 0,
            "no_go_count": 0,
            "safe_go_count": 0,
            "safety_status": "SECURE",
            "destructive_action_allowed": False,
        }

    no_go_cnt = int((df["type"] == "NO_GO").sum()) if "type" in df.columns else 0
    safe_go_cnt = int((df["type"] == "SAFE_GO").sum()) if "type" in df.columns else 0

    return {
        "total_rules": len(df),
        "no_go_count": no_go_cnt,
        "safe_go_count": safe_go_cnt,
        "safety_status": "SECURE",
        "destructive_action_allowed": False,
        "non_signal": True,
    }
