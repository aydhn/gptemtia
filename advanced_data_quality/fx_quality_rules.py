from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_fx_quality_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {"rule_name": "fx_quote_integrity", "rule_domain": "fx_quality", "severity_label": "quality_high"},
        {"rule_name": "fx_ohlcv_integrity", "rule_domain": "fx_quality", "severity_label": "quality_high"},
        {"rule_name": "fx_spread_sanity", "rule_domain": "fx_quality", "severity_label": "quality_high"},
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_fx_quality_rules(df)


def check_fx_quote_quality(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_fx_quote"
    required_cols = ["pair", "timestamp", "bid", "ask"]
    for col in required_cols:
        if col not in df.columns:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_fx_quote_col", dataset_type, col),
                    rule_id="rule_fx_quality_fx_quote_integrity",
                    finding_type="finding_missing_required_field",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=col,
                    severity_label="quality_high",
                    status_label="quality_fail",
                    message=f"FX quote is missing required column '{col}'.",
                    recommendation="Ensure quote provider populates required schema fields in Phase 113.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    if "bid" in df.columns and "ask" in df.columns:
        valid_quotes = df.dropna(subset=["bid", "ask"])
        inverted = valid_quotes[valid_quotes["bid"] > valid_quotes["ask"]]
        if len(inverted) > 0:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_fx_quote_inverted", dataset_type, "bid_ask"),
                    rule_id="rule_fx_quality_fx_spread_sanity",
                    finding_type="finding_quote_inconsistency",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name="bid",
                    severity_label="quality_high",
                    status_label="quality_fail",
                    message=f"Found {len(inverted)} records with inverted quotes (bid > ask).",
                    recommendation="Quarantine or review inverted quotes in Manual Review Queue.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

        if "mid" in df.columns:
            # check mid is approximately (bid+ask)/2
            mid_diff = (valid_quotes["mid"] - (valid_quotes["bid"] + valid_quotes["ask"]) / 2.0).abs()
            divergent = valid_quotes[mid_diff > 0.05]
            if len(divergent) > 0:
                findings.append(
                    QualityFinding(
                        finding_id=build_quality_finding_id("rule_fx_mid_diff", dataset_type, "mid"),
                        rule_id="rule_fx_quality_fx_quote_integrity",
                        finding_type="finding_quote_inconsistency",
                        dataset_type=dataset_type,
                        provider_name=provider_name or "unknown_provider",
                        field_name="mid",
                        severity_label="quality_medium",
                        status_label="quality_pass_with_warnings",
                        message=f"Found {len(divergent)} records where mid diverges significantly from (bid+ask)/2.",
                        recommendation="Canonicalize mid price computation in Phase 113 Normalization.",
                        future_phase_owner="Phase 113",
                        manual_review_required=True,
                    )
                )

    if "pair" in df.columns:
        pairs = df["pair"].dropna().astype(str)
        non_canonical = [p for p in pairs.unique() if "/" not in p and len(p) != 6]
        if non_canonical:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_fx_pair_format", dataset_type, "pair"),
                    rule_id="rule_fx_quality_fx_quote_integrity",
                    finding_type="finding_schema_mismatch",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name="pair",
                    severity_label="quality_low",
                    status_label="quality_pass_with_warnings",
                    message=f"Non-canonical pair format detected: {non_canonical}.",
                    recommendation="Normalize FX pair representation (e.g. BASE/QUOTE) in Phase 113.",
                    future_phase_owner="Phase 113",
                    manual_review_required=False,
                )
            )

    return findings


def check_fx_ohlcv_quality(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_fx_ohlcv"
    required_cols = ["pair", "timestamp", "open", "high", "low", "close"]
    for col in required_cols:
        if col not in df.columns:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_fx_ohlcv_col", dataset_type, col),
                    rule_id="rule_fx_quality_fx_ohlcv_integrity",
                    finding_type="finding_missing_required_field",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=col,
                    severity_label="quality_high",
                    status_label="quality_fail",
                    message=f"FX OHLCV is missing required column '{col}'.",
                    recommendation="Ensure bar schema conformity during Phase 113 Normalization.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    if "volume" not in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_fx_volume_missing", dataset_type, "volume"),
                rule_id="rule_fx_quality_fx_ohlcv_integrity",
                finding_type="finding_missing_value",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="volume",
                severity_label="quality_low",
                status_label="quality_pass_with_warnings",
                message="Volume column is omitted in FX OHLCV data (tick volume may be substituted).",
                recommendation="Document tick vs traded volume in Phase 114 Lineage.",
                future_phase_owner="Phase 114",
                manual_review_required=False,
            )
        )

    # OHLC geometry checks
    cols_present = all(c in df.columns for c in ["open", "high", "low", "close"])
    if cols_present:
        valid_bars = df.dropna(subset=["open", "high", "low", "close"])
        bad_high_low = valid_bars[valid_bars["high"] < valid_bars["low"]]
        if len(bad_high_low) > 0:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_fx_high_low", dataset_type, "high_low"),
                    rule_id="rule_fx_quality_fx_ohlcv_integrity",
                    finding_type="finding_ohlc_inconsistency",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name="high",
                    severity_label="quality_high",
                    status_label="quality_fail",
                    message=f"Found {len(bad_high_low)} bars where high < low.",
                    recommendation="Flag invalid bars for review; do not auto-clean destructively.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )
        bad_bounds = valid_bars[
            (valid_bars["open"] > valid_bars["high"]) |
            (valid_bars["open"] < valid_bars["low"]) |
            (valid_bars["close"] > valid_bars["high"]) |
            (valid_bars["close"] < valid_bars["low"])
        ]
        if len(bad_bounds) > 0:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_fx_open_close_bounds", dataset_type, "bounds"),
                    rule_id="rule_fx_quality_fx_ohlcv_integrity",
                    finding_type="finding_ohlc_inconsistency",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name="close",
                    severity_label="quality_high",
                    status_label="quality_fail",
                    message=f"Found {len(bad_bounds)} bars where open or close is outside [low, high].",
                    recommendation="Review corrupted bars in Manual Review Queue.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )
    return findings


def summarize_fx_quality_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "fx_quality",
    }
