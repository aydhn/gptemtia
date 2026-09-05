from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_provider_metadata_quality_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {"rule_name": "provider_credential_hygiene", "rule_domain": "provider_metadata_quality", "severity_label": "quality_critical"},
        {"rule_name": "provider_policy_presence", "rule_domain": "provider_metadata_quality", "severity_label": "quality_high"},
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_provider_metadata_quality_rules(df)


def check_provider_metadata_quality(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_provider_metadata"

    # 1. Credential leakage detection (CRITICAL)
    leak_suspicious_cols = [c for c in df.columns if any(k in c.lower() for k in ["api_key", "secret", "token", "password", "credential_value"])]
    for c in leak_suspicious_cols:
        non_empty = df[df[c].notna() & (df[c].astype(str).str.strip() != "")]
        if len(non_empty) > 0:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_prov_leak", dataset_type, c),
                    rule_id="rule_provider_metadata_quality_provider_metadata_credential_leak",
                    finding_type="finding_provider_metadata_issue",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=c,
                    severity_label="quality_critical",
                    status_label="quality_fail",
                    message=f"CRITICAL: Potential credential/secret value exposed in metadata column '{c}'!",
                    recommendation="Immediately sanitize credential output. Credentials must NEVER be stored in DataLake/metadata.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    # 2. Check no_scraping_policy presence (HIGH)
    if "no_scraping_policy" not in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_prov_no_scraping", dataset_type, "no_scraping_policy"),
                rule_id="rule_provider_metadata_quality_provider_no_scraping_policy",
                finding_type="finding_missing_required_field",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="no_scraping_policy",
                severity_label="quality_high",
                status_label="quality_fail",
                message="Provider metadata lacks explicit 'no_scraping_policy' declaration.",
                recommendation="Declare no_scraping_policy=True in Phase 113 provider metadata.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )
    else:
        violating = df[df["no_scraping_policy"] == False]
        if len(violating) > 0:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_prov_scraping_violation", dataset_type, "no_scraping_policy"),
                    rule_id="rule_provider_metadata_quality_provider_no_scraping_policy",
                    finding_type="finding_provider_metadata_issue",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name="no_scraping_policy",
                    severity_label="quality_critical",
                    status_label="quality_fail",
                    message="Provider has no_scraping_policy set to False. Scraping is strictly forbidden!",
                    recommendation="Revert to official APIs, manual fixtures, or local cache only.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    # 3. Check license_note presence (MEDIUM)
    if "license_note" not in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_prov_license", dataset_type, "license_note"),
                rule_id="rule_provider_metadata_quality_provider_policy_presence",
                finding_type="finding_missing_required_field",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="license_note",
                severity_label="quality_medium",
                status_label="quality_pass_with_warnings",
                message="Provider metadata lacks 'license_note'.",
                recommendation="Document provider usage license terms in Phase 113/114.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )

    # 4. Check manual_review_required presence (MEDIUM)
    if "manual_review_required" not in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_prov_manual_rev", dataset_type, "manual_review_required"),
                rule_id="rule_provider_metadata_quality_provider_policy_presence",
                finding_type="finding_missing_required_field",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="manual_review_required",
                severity_label="quality_medium",
                status_label="quality_pass_with_warnings",
                message="Provider metadata lacks 'manual_review_required' flag.",
                recommendation="Include manual review indicator in Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )

    return findings


def summarize_provider_metadata_quality_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "provider_metadata_quality",
    }
