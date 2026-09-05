from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_ohlc_consistency_rule_contract(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {"rule_name": "ohlc_geometry_high_ge_low", "rule_domain": "ohlc_consistency", "severity_label": "quality_high"},
        {"rule_name": "ohlc_geometry_open_close_in_bounds", "rule_domain": "ohlc_consistency", "severity_label": "quality_high"},
        {"rule_name": "ohlc_non_negative_prices", "rule_domain": "ohlc_consistency", "severity_label": "quality_high"},
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_ohlc_consistency_rules(df)


def check_ohlc_consistency(
    df: pd.DataFrame,
    dataset_type: str,
    provider_name: str = ""
) -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    cols = ["open", "high", "low", "close"]
    if not all(c in df.columns for c in cols):
        return findings

    valid = df.dropna(subset=cols)
    if len(valid) == 0:
        return findings

    # 1. High >= Low
    bad_hl = valid[valid["high"] < valid["low"]]
    if len(bad_hl) > 0:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_ohlc_high_low_violation", dataset_type, "high_low"),
                rule_id="rule_ohlc_consistency_ohlc_geometry_high_ge_low",
                finding_type="finding_ohlc_inconsistency",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="high",
                severity_label="quality_high",
                status_label="quality_fail",
                message=f"Detected {len(bad_hl)} bars where High is lower than Low.",
                recommendation="Flag inconsistent bars into Manual Review Queue.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )

    # 2. Open and Close bounds
    bad_oc = valid[
        (valid["open"] > valid["high"]) |
        (valid["open"] < valid["low"]) |
        (valid["close"] > valid["high"]) |
        (valid["close"] < valid["low"])
    ]
    if len(bad_oc) > 0:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_ohlc_oc_bounds_violation", dataset_type, "open_close"),
                rule_id="rule_ohlc_consistency_ohlc_geometry_open_close_in_bounds",
                finding_type="finding_ohlc_inconsistency",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="open_close",
                severity_label="quality_high",
                status_label="quality_fail",
                message=f"Detected {len(bad_oc)} bars where Open or Close violates [Low, High] bounds.",
                recommendation="Examine feed pricing anomalies non-destructively in Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )

    # 3. Non-negative prices (FX must strictly be positive; Commodity spot can exception WTI 2020)
    for c in cols:
        neg = valid[valid[c] < 0]
        if len(neg) > 0:
            sev = "quality_critical" if dataset_type == "dataset_fx_ohlcv" else "quality_medium"
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id(f"rule_ohlc_negative_{c}", dataset_type, c),
                    rule_id="rule_ohlc_consistency_ohlc_non_negative_prices",
                    finding_type="finding_ohlc_inconsistency",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=c,
                    severity_label=sev,
                    status_label="quality_fail" if sev == "quality_critical" else "quality_pass_with_warnings",
                    message=f"Detected {len(neg)} bars with negative values in '{c}'.",
                    recommendation="Review negative price regime in Phase 113 Normalization.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    # 4. Adjusted price flag note
    if "adjusted_flag" in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_ohlc_adjusted_note", dataset_type, "adjusted_flag"),
                rule_id="rule_ohlc_consistency_ohlc_bar_geometry",
                finding_type="finding_provider_metadata_issue",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="adjusted_flag",
                severity_label="quality_info",
                status_label="quality_pass",
                message="Adjusted prices present; corporate action adjustments to be tracked in Phase 114 Lineage.",
                recommendation="Document adjustment factors in Phase 114.",
                future_phase_owner="Phase 114",
                manual_review_required=False,
            )
        )

    return findings


def summarize_ohlc_consistency_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "ohlc_consistency",
    }
