from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_news_metadata_copyright_quality_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {"rule_name": "no_full_text_storage", "rule_domain": "news_copyright_quality", "severity_label": "quality_critical"},
        {"rule_name": "metadata_only_enforcement", "rule_domain": "news_copyright_quality", "severity_label": "quality_critical"},
        {"rule_name": "no_external_llm_embeddings", "rule_domain": "news_copyright_quality", "severity_label": "quality_critical"},
        {"rule_name": "copyright_status_declared", "rule_domain": "news_copyright_quality", "severity_label": "quality_high"},
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_news_copyright_quality_rules(df)


def check_news_copyright_boundary(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_news_metadata"

    # 1. Full text, raw content, HTML columns are strictly prohibited (CRITICAL)
    forbidden_cols = ["full_text", "article_body", "raw_content", "scraped_html", "page_html", "raw_body", "html"]
    for c in forbidden_cols:
        if c in df.columns:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_copyright_forbidden_col", dataset_type, c),
                    rule_id="rule_news_copyright_quality_no_full_text_storage",
                    finding_type="finding_news_copyright_boundary",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=c,
                    severity_label="quality_critical",
                    status_label="quality_fail",
                    message=f"CRITICAL COPYRIGHT BREACH: Column '{c}' contains scraped full text or raw HTML.",
                    recommendation="Remove raw body content immediately. Only store headline/summary metadata references.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    # 2. metadata_only flag check
    if "metadata_only" in df.columns:
        breaches = df[df["metadata_only"] == False]
        if len(breaches) > 0:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_copyright_metadata_only_breach", dataset_type, "metadata_only"),
                    rule_id="rule_news_copyright_quality_metadata_only_enforcement",
                    finding_type="finding_news_copyright_boundary",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name="metadata_only",
                    severity_label="quality_critical",
                    status_label="quality_fail",
                    message="CRITICAL: 'metadata_only' is False for news records!",
                    recommendation="Set metadata_only=True and purge any non-metadata artifacts.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    # 3. External LLM / Vector / Embedding references check (CRITICAL)
    ai_leak_cols = [c for c in df.columns if any(k in c.lower() for k in ["vector", "embedding", "llm_generated_text", "openai", "claude"])]
    for c in ai_leak_cols:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_copyright_ai_leak", dataset_type, c),
                rule_id="rule_news_copyright_quality_no_external_llm_embeddings",
                finding_type="finding_news_copyright_boundary",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name=c,
                severity_label="quality_critical",
                status_label="quality_fail",
                message=f"CRITICAL: Prohibited external LLM / vector DB artifact detected in column '{c}'.",
                recommendation="Remove external LLM and vector database dependencies.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )

    # 4. Copyright status declared (HIGH)
    if "copyright_status" not in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_copyright_status_missing", dataset_type, "copyright_status"),
                rule_id="rule_news_copyright_quality_copyright_status_declared",
                finding_type="finding_missing_required_field",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="copyright_status",
                severity_label="quality_high",
                status_label="quality_fail",
                message="News dataset lacks 'copyright_status' field declaration.",
                recommendation="Declare copyright boundary status ('metadata_reference_only') in Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )

    return findings


def summarize_news_copyright_quality_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "news_copyright_quality",
    }
