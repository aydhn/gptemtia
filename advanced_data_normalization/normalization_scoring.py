from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationScore,
    build_normalization_score_id,
)


def calculate_normalization_score(
    findings_df: pd.DataFrame,
    dataset_name: str,
    dataset_type: str,
    profile: DataNormalizationProfile,
) -> float:
    base_score = 1.0
    if findings_df.empty or "dataset_type" not in findings_df.columns:
        return base_score

    # Filter findings for this dataset type or all
    ds_findings = findings_df[findings_df["dataset_type"].isin([dataset_type, "dataset_all", "all"])]
    if ds_findings.empty:
        return base_score

    # Penalties for unnormalized or manual review items
    for _, row in ds_findings.iterrows():
        sev = row.get("severity_label", "normalization_medium")
        status = row.get("status_label", "")
        if status == "normalization_manual_review_required":
            if sev == "normalization_critical":
                base_score -= 0.15
            elif sev == "normalization_high":
                base_score -= 0.10
            elif sev == "normalization_medium":
                base_score -= 0.05
            else:
                base_score -= 0.02
        elif status == "normalization_failed":
            base_score -= 0.20
        elif status == "normalization_blocked_by_safety":
            base_score -= 0.10

    return max(0.0, min(1.0, round(base_score, 4)))


def classify_normalization_score(
    score: float,
    profile: DataNormalizationProfile,
) -> str:
    if score >= 0.85:
        return "normalization_excellent"
    elif score >= profile.min_normalization_score:
        return "normalization_acceptable"
    else:
        return "normalization_needs_review"


def build_normalization_score_report(
    findings_df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    datasets = [
        ("fx_quote_contract", "dataset_fx_quote", "fx_dry_run_fixture_provider"),
        ("fx_ohlcv_contract", "dataset_fx_ohlcv", "fx_dry_run_fixture_provider"),
        ("commodity_spot_contract", "dataset_commodity_spot", "commodity_dry_run_fixture_provider"),
        ("commodity_ohlcv_contract", "dataset_commodity_ohlcv", "commodity_dry_run_fixture_provider"),
        ("macro_timeseries_contract", "dataset_macro_timeseries", "macro_official_api_provider_placeholder"),
        ("calendar_event_contract", "dataset_calendar_event", "calendar_licensed_provider_placeholder"),
        ("news_metadata_contract", "dataset_news_metadata", "news_public_dataset_provider_placeholder"),
    ]

    scores = []
    for d_name, d_type, prov in datasets:
        sc = calculate_normalization_score(findings_df, d_name, d_type, profile)
        applied_cnt = 0
        manual_cnt = 0
        blocked_cnt = 0
        if not findings_df.empty and "dataset_type" in findings_df.columns:
            sub = findings_df[findings_df["dataset_type"].isin([d_type, "dataset_all", "all"])]
            applied_cnt = len(sub[sub["status_label"] == "normalization_applied"])
            manual_cnt = len(sub[sub["status_label"] == "normalization_manual_review_required"])
            blocked_cnt = len(sub[sub["status_label"] == "normalization_blocked_by_safety"])

        score_obj = NormalizationScore(
            score_id=build_normalization_score_id(d_name, prov),
            dataset_name=d_name,
            dataset_type=d_type,
            provider_name=prov,
            score=sc,
            status_label=classify_normalization_score(sc, profile),
            applied_rules=applied_cnt,
            manual_review_count=manual_cnt,
            blocked_count=blocked_cnt,
            notes="İç kalite metriğidir; kesinlikle AL/SAT sinyali veya resmi onay değildir.",
        )
        scores.append(score_obj.to_dict())

    df = pd.DataFrame.from_records(scores)
    summary = summarize_normalization_scores(df)
    return df, summary


def summarize_normalization_scores(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_scored_datasets": len(df),
        "mean_score": round(float(df["score"].mean()), 4) if "score" in df.columns and len(df) > 0 else 1.0,
        "min_score": round(float(df["score"].min()), 4) if "score" in df.columns and len(df) > 0 else 1.0,
        "max_score": round(float(df["score"].max()), 4) if "score" in df.columns and len(df) > 0 else 1.0,
        "is_trading_signal": False,
        "is_official_approval": False,
        "current_phase": 113,
        "target_final_phase": 160,
    }
