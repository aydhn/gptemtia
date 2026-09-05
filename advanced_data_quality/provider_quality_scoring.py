from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import (
    ProviderQualityScore,
    build_provider_quality_score_id,
)


def calculate_provider_quality_score(
    findings_df: pd.DataFrame,
    provider_name: str,
    dataset_type: str,
    profile: DataQualityProfile
) -> float:
    base_score = 1.0
    if findings_df is None or len(findings_df) == 0:
        return base_score

    # Filter findings for this provider (and optionally dataset_type if present)
    p_findings = findings_df[findings_df["provider_name"] == provider_name]
    if dataset_type and dataset_type != "all" and "dataset_type" in p_findings.columns:
        p_findings = p_findings[p_findings["dataset_type"] == dataset_type]

    if len(p_findings) == 0:
        return base_score

    for _, row in p_findings.iterrows():
        sev = str(row.get("severity_label", ""))
        if sev == "quality_critical":
            base_score -= 0.35
        elif sev == "quality_high":
            base_score -= 0.15
        elif sev == "quality_medium":
            base_score -= 0.05
        elif sev == "quality_low":
            base_score -= 0.01

    return max(0.0, min(1.0, round(base_score, 4)))


def classify_provider_quality_score(score: float, profile: DataQualityProfile) -> str:
    if score >= 0.85:
        return "quality_pass"
    elif score >= profile.min_provider_quality_score:
        return "quality_pass_with_warnings"
    else:
        return "quality_fail"


def build_provider_quality_score_report(
    findings_df: pd.DataFrame,
    profile: DataQualityProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    known_providers = [
        ("fx_yahoo_finance_fixture", "dataset_fx_ohlcv"),
        ("commodity_cbot_fixture", "dataset_commodity_ohlcv"),
        ("macro_worldbank_fixture", "dataset_macro_timeseries"),
        ("calendar_trading_economics_fixture", "dataset_calendar_event"),
        ("news_reuters_fixture", "dataset_news_metadata"),
    ]

    # Collect any actual providers in findings_df as well
    if findings_df is not None and len(findings_df) > 0 and "provider_name" in findings_df.columns:
        for p in findings_df["provider_name"].unique():
            ds = "all"
            ds_match = findings_df[findings_df["provider_name"] == p]["dataset_type"].unique()
            if len(ds_match) > 0:
                ds = ds_match[0]
            if (p, ds) not in known_providers:
                known_providers.append((p, ds))

    records: List[Dict[str, Any]] = []
    for p_name, ds_type in known_providers:
        score = calculate_provider_quality_score(findings_df, p_name, ds_type, profile)
        status = classify_provider_quality_score(score, profile)
        
        p_find = findings_df[findings_df["provider_name"] == p_name] if findings_df is not None and len(findings_df) > 0 and "provider_name" in findings_df.columns else pd.DataFrame()
        crit = int((p_find["severity_label"] == "quality_critical").sum()) if len(p_find) > 0 else 0
        high = int((p_find["severity_label"] == "quality_high").sum()) if len(p_find) > 0 else 0
        med = int((p_find["severity_label"] == "quality_medium").sum()) if len(p_find) > 0 else 0
        low = int((p_find["severity_label"] == "quality_low").sum()) if len(p_find) > 0 else 0
        
        item = ProviderQualityScore(
            score_id=build_provider_quality_score_id(p_name, ds_type),
            provider_name=p_name,
            dataset_type=ds_type,
            score=score,
            status_label=status,
            critical_findings=crit,
            high_findings=high,
            medium_findings=med,
            low_findings=low,
            manual_review_required=(crit > 0 or high > 0 or score < profile.min_provider_quality_score),
            notes="İç kalite değerlendirmesidir; resmi sağlayıcı onayı veya benchmark değildir."
        )
        records.append(item.to_dict())

    df = pd.DataFrame.from_records(records)
    summary = summarize_provider_quality_scores(df)
    return df, summary


def summarize_provider_quality_scores(df: pd.DataFrame) -> Dict[str, Any]:
    if df is None or len(df) == 0:
        return {
            "total_providers_scored": 0,
            "average_score": 1.0,
            "passing_providers": 0,
            "failing_providers": 0,
            "current_phase": 112,
            "target_final_phase": 160,
        }

    return {
        "total_providers_scored": len(df),
        "average_score": float(round(df["score"].mean(), 4)) if "score" in df.columns else 1.0,
        "passing_providers": int((df["score"] >= 0.45).sum()) if "score" in df.columns else 0,
        "failing_providers": int((df["score"] < 0.45).sum()) if "score" in df.columns else 0,
        "current_phase": 112,
        "target_final_phase": 160,
    }
