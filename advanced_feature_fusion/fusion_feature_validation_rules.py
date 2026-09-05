"""Fusion Feature Validation Rules.

Defines audit rules and diagnostic finding generation for multi-domain fusion features.
Strictly non-signal, research use only.
"""

from typing import Any, Dict, List
import pandas as pd
from advanced_feature_fusion.fusion_feature_models import FusionValidationFinding
from advanced_feature_fusion.no_lookahead_fusion_guard import FORBIDDEN_FUSION_TERMS, FULL_ARTICLE_TERMS


VALIDATION_RULES = [
    {
        "rule_id": "VR-001-FORBIDDEN-TERMS",
        "description": "Ensures no column names contain forbidden trade signal or prediction terms.",
        "severity": "CRITICAL",
    },
    {
        "rule_id": "VR-002-METADATA-ONLY",
        "description": "Ensures no news columns contain full article text, raw content, or scrapings.",
        "severity": "CRITICAL",
    },
    {
        "rule_id": "VR-003-TIMESTAMP-MONOTONIC",
        "description": "Ensures timestamps are monotonically increasing.",
        "severity": "HIGH",
    },
    {
        "rule_id": "VR-004-BINARY-FLAGS",
        "description": "Ensures binary flag features take only values in {0, 1, NaN}.",
        "severity": "MEDIUM",
    },
]


def get_fusion_feature_validation_rules() -> List[Dict[str, Any]]:
    """Return list of validation rules."""
    return [dict(r) for r in VALIDATION_RULES]


def run_all_fusion_feature_validation_rules(
    df: pd.DataFrame,
    timestamp_col: str = "timestamp",
) -> List[FusionValidationFinding]:
    """Execute all validation rules against a DataFrame and collect findings."""
    findings: List[FusionValidationFinding] = []

    if df.empty:
        findings.append(
            FusionValidationFinding(
                finding_id="FIND-EMPTY-001",
                rule_id="VR-GENERAL",
                severity="CRITICAL",
                target_field="DataFrame",
                message="Input DataFrame is empty.",
                is_blocking=True,
            )
        )
        return findings

    # Check forbidden terms
    for col in df.columns:
        c_lower = str(col).lower()
        for term in FORBIDDEN_FUSION_TERMS:
            if term in c_lower:
                findings.append(
                    FusionValidationFinding(
                        finding_id=f"FIND-FORBIDDEN-{col}",
                        rule_id="VR-001-FORBIDDEN-TERMS",
                        severity="CRITICAL",
                        target_field=str(col),
                        message=f"Column '{col}' violates non-signal policy with forbidden term '{term}'.",
                        is_blocking=True,
                    )
                )
        for term in FULL_ARTICLE_TERMS:
            if term in c_lower:
                findings.append(
                    FusionValidationFinding(
                        finding_id=f"FIND-ARTICLE-{col}",
                        rule_id="VR-002-METADATA-ONLY",
                        severity="CRITICAL",
                        target_field=str(col),
                        message=f"Column '{col}' violates metadata-only policy with article content term '{term}'.",
                        is_blocking=True,
                    )
                )

    # Check timestamp monotonicity
    if timestamp_col in df.columns:
        ts = pd.to_datetime(df[timestamp_col], utc=True)
        if not ts.is_monotonic_increasing:
            findings.append(
                FusionValidationFinding(
                    finding_id="FIND-TS-NON-MONOTONIC",
                    rule_id="VR-003-TIMESTAMP-MONOTONIC",
                    severity="HIGH",
                    target_field=timestamp_col,
                    message=f"Timestamp column '{timestamp_col}' is not monotonically increasing.",
                    is_blocking=True,
                )
            )

    # Check binary flags
    flag_cols = [c for c in df.columns if c.endswith("_flag") or c.startswith("has_") or c.startswith("is_")]
    for f_col in flag_cols:
        series = df[f_col].dropna()
        if not series.empty:
            unique_vals = set(series.unique())
            if not unique_vals.issubset({0, 1, 0.0, 1.0, True, False}):
                findings.append(
                    FusionValidationFinding(
                        finding_id=f"FIND-FLAG-{f_col}",
                        rule_id="VR-004-BINARY-FLAGS",
                        severity="MEDIUM",
                        target_field=f_col,
                        message=f"Flag column '{f_col}' contains non-binary values: {unique_vals}.",
                        is_blocking=False,
                    )
                )

    return findings


def get_validation_rules_summary() -> Dict[str, Any]:
    """Summary of validation rules."""
    rules = get_fusion_feature_validation_rules()
    return {
        "rule_count": len(rules),
        "rule_ids": [r["rule_id"] for r in rules],
        "zero_signal_mandate": True,
        "strictly_metadata_only": True,
    }
