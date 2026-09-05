from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import (
    DatasetQualityScore,
    build_dataset_quality_score_id,
)


def calculate_dataset_quality_score(
    findings_df: pd.DataFrame,
    dataset_name: str,
    dataset_type: str,
    row_count: int,
    checked_rules: int,
    profile: DataQualityProfile
) -> float:
    base_score = 1.0
    if findings_df is None or len(findings_df) == 0:
        return base_score

    # Filter findings for this dataset type or name
    d_findings = findings_df[
        (findings_df["dataset_type"] == dataset_type) |
        (findings_df["field_name"] == dataset_name)
    ]
    if len(d_findings) == 0:
        return base_score

    for _, row in d_findings.iterrows():
        sev = str(row.get("severity_label", ""))
        if sev == "quality_critical":
            base_score -= 0.40
        elif sev == "quality_high":
            base_score -= 0.20
        elif sev == "quality_medium":
            base_score -= 0.08
        elif sev == "quality_low":
            base_score -= 0.02

    return max(0.0, min(1.0, round(base_score, 4)))


def classify_dataset_quality_score(score: float, profile: DataQualityProfile) -> str:
    if score >= 0.85:
        return "quality_pass"
    elif score >= profile.min_dataset_quality_score:
        return "quality_pass_with_warnings"
    else:
        return "quality_fail"


def build_dataset_quality_score_report(
    findings_df: pd.DataFrame,
    profile: DataQualityProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    standard_datasets = [
        ("fx_ohlcv_sample", "dataset_fx_ohlcv", "fx_yahoo_finance_fixture", 100, 10),
        ("fx_quote_sample", "dataset_fx_quote", "fx_yahoo_finance_fixture", 50, 8),
        ("commodity_spot_sample", "dataset_commodity_spot", "commodity_cbot_fixture", 80, 8),
        ("commodity_ohlcv_sample", "dataset_commodity_ohlcv", "commodity_cbot_fixture", 120, 10),
        ("macro_timeseries_sample", "dataset_macro_timeseries", "macro_worldbank_fixture", 60, 8),
        ("calendar_event_sample", "dataset_calendar_event", "calendar_trading_economics_fixture", 40, 8),
        ("news_metadata_sample", "dataset_news_metadata", "news_reuters_fixture", 50, 10),
        ("provider_metadata_sample", "dataset_provider_metadata", "internal_provider_catalog", 10, 6),
    ]

    records: List[Dict[str, Any]] = []
    for d_name, d_type, p_name, rows, checked in standard_datasets:
        score = calculate_dataset_quality_score(findings_df, d_name, d_type, rows, checked, profile)
        status = classify_dataset_quality_score(score, profile)
        
        # Count failed rules for this dataset
        if findings_df is not None and len(findings_df) > 0 and "dataset_type" in findings_df.columns:
            failed_count = int((findings_df["dataset_type"] == d_type).sum())
        else:
            failed_count = 0

        item = DatasetQualityScore(
            score_id=build_dataset_quality_score_id(d_name, p_name),
            dataset_name=d_name,
            dataset_type=d_type,
            provider_name=p_name,
            score=score,
            status_label=status,
            row_count=rows,
            checked_rules=checked,
            failed_rules=failed_count,
            manual_review_required=(score < profile.min_dataset_quality_score or failed_count > 0),
            notes="İç kalite skorudur; AL/SAT veya trade sinyali olarak kullanılamaz."
        )
        records.append(item.to_dict())

    df = pd.DataFrame.from_records(records)
    summary = summarize_dataset_quality_scores(df)
    return df, summary


def summarize_dataset_quality_scores(df: pd.DataFrame) -> Dict[str, Any]:
    if df is None or len(df) == 0:
        return {
            "total_datasets_scored": 0,
            "average_score": 1.0,
            "passing_datasets": 0,
            "failing_datasets": 0,
            "current_phase": 112,
            "target_final_phase": 160,
        }

    return {
        "total_datasets_scored": len(df),
        "average_score": float(round(df["score"].mean(), 4)) if "score" in df.columns else 1.0,
        "passing_datasets": int((df["score"] >= 0.45).sum()) if "score" in df.columns else 0,
        "failing_datasets": int((df["score"] < 0.45).sum()) if "score" in df.columns else 0,
        "current_phase": 112,
        "target_final_phase": 160,
    }
