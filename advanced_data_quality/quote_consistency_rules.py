from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_quote_consistency_rule_contract(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {"rule_name": "quote_bid_le_ask", "rule_domain": "quote_consistency", "severity_label": "quality_high"},
        {"rule_name": "quote_spread_non_negative", "rule_domain": "quote_consistency", "severity_label": "quality_high"},
        {"rule_name": "quote_mid_within_spread", "rule_domain": "quote_consistency", "severity_label": "quality_medium"},
        {"rule_name": "quote_timestamp_presence", "rule_domain": "quote_consistency", "severity_label": "quality_high"},
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_quote_consistency_rules(df)


def check_quote_consistency(
    df: pd.DataFrame,
    dataset_type: str,
    provider_name: str = ""
) -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    # Check timestamp presence
    if "timestamp" not in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_quote_no_ts", dataset_type, "timestamp"),
                rule_id="rule_quote_consistency_quote_timestamp_presence",
                finding_type="finding_missing_required_field",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="timestamp",
                severity_label="quality_high",
                status_label="quality_fail",
                message="Quote records missing timestamp field.",
                recommendation="Enforce timestamp tagging on all quote streams in Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )

    if "bid" in df.columns and "ask" in df.columns:
        valid = df.dropna(subset=["bid", "ask"])
        # Bid <= Ask
        inverted = valid[valid["bid"] > valid["ask"]]
        if len(inverted) > 0:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_quote_inverted_contract", dataset_type, "bid_ask"),
                    rule_id="rule_quote_consistency_quote_bid_le_ask",
                    finding_type="finding_quote_inconsistency",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name="bid",
                    severity_label="quality_high",
                    status_label="quality_fail",
                    message=f"Contract breach: {len(inverted)} records have bid > ask.",
                    recommendation="Quarantine inverted quotes into Manual Review Queue.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

        # Spread non-negative
        if "spread" in df.columns:
            neg_spread = df[df["spread"] < 0]
            if len(neg_spread) > 0:
                findings.append(
                    QualityFinding(
                        finding_id=build_quality_finding_id("rule_quote_negative_spread", dataset_type, "spread"),
                        rule_id="rule_quote_consistency_quote_spread_non_negative",
                        finding_type="finding_quote_inconsistency",
                        dataset_type=dataset_type,
                        provider_name=provider_name or "unknown_provider",
                        field_name="spread",
                        severity_label="quality_high",
                        status_label="quality_fail",
                        message=f"Contract breach: {len(neg_spread)} records have negative spread.",
                        recommendation="Recompute spread as ask - bid in Phase 113 Normalization.",
                        future_phase_owner="Phase 113",
                        manual_review_required=True,
                    )
                )

        # Mid within spread
        if "mid" in df.columns:
            out_of_mid = valid[(valid["mid"] < valid["bid"]) | (valid["mid"] > valid["ask"])]
            if len(out_of_mid) > 0:
                findings.append(
                    QualityFinding(
                        finding_id=build_quality_finding_id("rule_quote_mid_bounds", dataset_type, "mid"),
                        rule_id="rule_quote_consistency_quote_mid_within_spread",
                        finding_type="finding_quote_inconsistency",
                        dataset_type=dataset_type,
                        provider_name=provider_name or "unknown_provider",
                        field_name="mid",
                        severity_label="quality_medium",
                        status_label="quality_pass_with_warnings",
                        message=f"Detected {len(out_of_mid)} records where mid is outside [bid, ask].",
                        recommendation="Recalculate mid price canonically in Phase 113.",
                        future_phase_owner="Phase 113",
                        manual_review_required=True,
                    )
                )

    return findings


def summarize_quote_consistency_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "quote_consistency",
    }
