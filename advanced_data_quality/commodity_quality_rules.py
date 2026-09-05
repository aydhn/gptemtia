from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_commodity_quality_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {"rule_name": "commodity_spot_integrity", "rule_domain": "commodity_quality", "severity_label": "quality_high"},
        {"rule_name": "commodity_ohlcv_integrity", "rule_domain": "commodity_quality", "severity_label": "quality_high"},
        {"rule_name": "commodity_futures_metadata", "rule_domain": "commodity_quality", "severity_label": "quality_medium"},
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_commodity_quality_rules(df)


def check_commodity_spot_quality(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_commodity_spot"
    required = ["symbol", "spot_price", "unit", "quote_currency"]
    for col in required:
        if col not in df.columns:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_comm_spot_col", dataset_type, col),
                    rule_id="rule_commodity_quality_commodity_spot_sanity",
                    finding_type="finding_missing_required_field",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=col,
                    severity_label="quality_high",
                    status_label="quality_fail",
                    message=f"Commodity spot dataset is missing required field '{col}'.",
                    recommendation="Standardize spot schema attributes in Phase 113.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    if "spot_price" in df.columns:
        neg_prices = df[df["spot_price"] < 0]
        # In crude oil, negative prices happened historically (WTI May 2020), so medium severity warning
        if len(neg_prices) > 0:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_comm_spot_negative", dataset_type, "spot_price"),
                    rule_id="rule_commodity_quality_commodity_spot_sanity",
                    finding_type="finding_ohlc_inconsistency",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name="spot_price",
                    severity_label="quality_medium",
                    status_label="quality_pass_with_warnings",
                    message=f"Detected {len(neg_prices)} records with negative spot prices.",
                    recommendation="Verify historical context (e.g. WTI 2020) in Phase 113 Normalization.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )
    return findings


def check_commodity_ohlcv_quality(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_commodity_ohlcv"
    required = ["symbol", "timestamp", "open", "high", "low", "close"]
    for col in required:
        if col not in df.columns:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_comm_ohlcv_col", dataset_type, col),
                    rule_id="rule_commodity_quality_commodity_ohlcv_sanity",
                    finding_type="finding_missing_required_field",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=col,
                    severity_label="quality_high",
                    status_label="quality_fail",
                    message=f"Commodity OHLCV dataset is missing required field '{col}'.",
                    recommendation="Ensure bar fields are mapped during Phase 113 Normalization.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    if "open_interest" not in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_comm_oi_missing", dataset_type, "open_interest"),
                rule_id="rule_commodity_quality_commodity_ohlcv_sanity",
                finding_type="finding_missing_value",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="open_interest",
                severity_label="quality_low",
                status_label="quality_pass_with_warnings",
                message="Open interest field is missing from commodity futures bar data.",
                recommendation="Provide OI where available or treat as optional in Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=False,
            )
        )
    return findings


def check_futures_metadata_quality(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_commodity_ohlcv"
    meta_cols = ["root_symbol", "contract_month", "expiry_date"]
    for col in meta_cols:
        if col not in df.columns:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_comm_meta_col", dataset_type, col),
                    rule_id="rule_commodity_quality_commodity_futures_metadata_sanity",
                    finding_type="finding_missing_required_field",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=col,
                    severity_label="quality_medium",
                    status_label="quality_pass_with_warnings",
                    message=f"Futures contract metadata column '{col}' is missing.",
                    recommendation="Enrich contract metadata in Phase 113/114.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    if "is_continuous" in df.columns:
        # verify continuous contract is not claimed as executable
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_comm_continuous_notice", dataset_type, "is_continuous"),
                rule_id="rule_commodity_quality_commodity_futures_metadata_sanity",
                finding_type="finding_provider_metadata_issue",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="is_continuous",
                severity_label="quality_info",
                status_label="quality_pass",
                message="Continuous contract series must be treated as research placeholder, not executable contract.",
                recommendation="Document roll methodology in Phase 114 Lineage.",
                future_phase_owner="Phase 114",
                manual_review_required=False,
            )
        )

    return findings


def summarize_commodity_quality_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "commodity_quality",
    }
