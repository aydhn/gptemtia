from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_news_metadata_quality_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {"rule_name": "news_metadata_schema_integrity", "rule_domain": "news_metadata_quality", "severity_label": "quality_high"},
        {"rule_name": "news_copyright_safe_boundary", "rule_domain": "news_metadata_quality", "severity_label": "quality_critical"},
        {"rule_name": "news_sentiment_non_signal", "rule_domain": "news_metadata_quality", "severity_label": "quality_info"},
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_news_metadata_quality_rules(df)


def check_news_metadata_quality(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_news_metadata"
    required = ["item_id", "timestamp", "source_name"]
    for col in required:
        if col not in df.columns:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_news_col", dataset_type, col),
                    rule_id="rule_news_metadata_quality_news_metadata_integrity",
                    finding_type="finding_missing_required_field",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=col,
                    severity_label="quality_high",
                    status_label="quality_fail",
                    message=f"News metadata is missing mandatory field '{col}'.",
                    recommendation="Ensure news metadata feeds supply canonical identity and source in Phase 113.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    # Title or summary ref check
    has_ref = any(c in df.columns for c in ["title_or_summary_ref", "title_ref", "headline"])
    if not has_ref:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_news_title_ref", dataset_type, "title_or_summary_ref"),
                rule_id="rule_news_metadata_quality_news_metadata_integrity",
                finding_type="finding_missing_required_field",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="title_or_summary_ref",
                severity_label="quality_high",
                status_label="quality_fail",
                message="News metadata must have title_or_summary_ref (short reference).",
                recommendation="Provide short title reference in Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )

    # Forbidden full text / body / scraped HTML check -> CRITICAL
    forbidden_body_fields = ["full_text", "article_body", "raw_content", "scraped_html", "page_html", "content"]
    for col in forbidden_body_fields:
        if col in df.columns:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_news_forbidden_body", dataset_type, col),
                    rule_id="rule_news_metadata_quality_news_copyright_safe_boundary",
                    finding_type="finding_news_copyright_boundary",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=col,
                    severity_label="quality_critical",
                    status_label="quality_fail",
                    message=f"Forbidden full article / scraped body field '{col}' detected in news dataset!",
                    recommendation="Immediately remove raw article body; only metadata and references are permitted.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    # Check tags format
    tag_cols = [c for c in ["asset_tags", "macro_tags", "commodity_tags", "fx_tags"] if c in df.columns]
    for tc in tag_cols:
        invalid_tags = df[df[tc].apply(lambda x: not isinstance(x, (list, tuple, str)) and pd.notna(x))]
        if len(invalid_tags) > 0:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_news_tag_format", dataset_type, tc),
                    rule_id="rule_news_metadata_quality_news_metadata_integrity",
                    finding_type="finding_schema_mismatch",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=tc,
                    severity_label="quality_medium",
                    status_label="quality_pass_with_warnings",
                    message=f"Tag column '{tc}' contains non-standard data types.",
                    recommendation="Normalize news tags to list of strings in Phase 113.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    return findings


def check_news_item_reference_quality(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_news_metadata"
    if "sentiment_as_signal" in df.columns:
        signals = df[df["sentiment_as_signal"] == True]
        if len(signals) > 0:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_news_sentiment_signal_breach", dataset_type, "sentiment_as_signal"),
                    rule_id="rule_news_metadata_quality_news_sentiment_non_signal",
                    finding_type="finding_news_copyright_boundary",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name="sentiment_as_signal",
                    severity_label="quality_critical",
                    status_label="quality_fail",
                    message="Sentiment as trading signal breach detected! News sentiment must NEVER be a trade signal.",
                    recommendation="Strictly enforce research-only sentiment boundary.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    return findings


def summarize_news_metadata_quality_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "news_metadata_quality",
    }
