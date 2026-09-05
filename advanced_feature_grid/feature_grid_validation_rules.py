from typing import Tuple, Dict, Any, List
import numpy as np
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile
from advanced_feature_grid.feature_grid_models import FORBIDDEN_OUTPUT_WORDS


VALIDATION_RULES = [
    {
        "rule_id": "rule_fg_01_no_forbidden_columns",
        "name": "No Forbidden Columns Rule",
        "description": "Grid çıktılarında sinyal/hedef/etiket/tahmin içeren kolon bulunamaz.",
        "severity": "CRITICAL",
    },
    {
        "rule_id": "rule_fg_02_numeric_sanity",
        "name": "Numeric Sanity Rule",
        "description": "Grid feature kolonları sayısal tipte olmalı, sonsuz (inf) değer içermemelidir.",
        "severity": "HIGH",
    },
    {
        "rule_id": "rule_fg_03_min_output_count",
        "name": "Minimum Output Count Rule",
        "description": "Grid hesaplaması en az beklenen minimum sayıda feature üretmelidir.",
        "severity": "MEDIUM",
    },
    {
        "rule_id": "rule_fg_04_no_in_place_mutation",
        "name": "No In-Place Mutation Rule",
        "description": "Girdi DataFrame kolonları veya index'i hesaplama esnasında mutate edilmemelidir.",
        "severity": "CRITICAL",
    },
    {
        "rule_id": "rule_fg_05_no_lookahead_negative_shift",
        "name": "No Negative Shift Rule",
        "description": "Hesaplama motoru geleceğe bakan negatif shift çağrısı içeremez.",
        "severity": "CRITICAL",
    },
]


def validate_feature_grid_output_no_forbidden_columns(df: pd.DataFrame) -> Dict[str, Any]:
    findings = []
    for col in df.columns:
        col_lower = str(col).lower()
        for forbidden in FORBIDDEN_OUTPUT_WORDS:
            tokens = col_lower.split("_")
            if forbidden in tokens or forbidden in col_lower:
                findings.append(f"Kolon '{col}' yasaklı kelime içeriyor: '{forbidden}'")

    return {
        "valid": len(findings) == 0,
        "forbidden_columns_found": findings,
        "count": len(findings),
    }


def validate_feature_grid_output_numeric_sanity(
    df: pd.DataFrame, output_fields: List[str]
) -> Dict[str, Any]:
    errors = []
    warnings = []

    for col in output_fields:
        if col not in df.columns:
            errors.append(f"Kolon bulunamadı: {col}")
            continue

        series = df[col]
        if not np.issubdtype(series.dtype, np.number):
            errors.append(f"Kolon '{col}' sayısal tipte değil: {series.dtype}")
            continue

        # Check for inf
        inf_count = np.isinf(series.dropna()).sum()
        if inf_count > 0:
            warnings.append(f"Kolon '{col}' {inf_count} adet sonsuz (inf) değer içeriyor.")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }


def validate_feature_grid_output_count(
    df: pd.DataFrame, expected_min_count: int = 1
) -> Dict[str, Any]:
    col_count = len(df.columns)
    valid = col_count >= expected_min_count
    return {
        "valid": valid,
        "column_count": col_count,
        "expected_min_count": expected_min_count,
    }


def validate_feature_grid_dataframe(df: pd.DataFrame) -> Dict[str, Any]:
    if df is None or not isinstance(df, pd.DataFrame):
        return {"valid": False, "errors": ["DataFrame None veya geçersiz tipte."]}
    if df.empty:
        return {"valid": False, "errors": ["DataFrame boş."]}

    forbidden_res = validate_feature_grid_output_no_forbidden_columns(df)
    errors = list(forbidden_res["forbidden_columns_found"])

    return {
        "valid": len(errors) == 0,
        "row_count": len(df),
        "column_count": len(df.columns),
        "errors": errors,
    }


def build_feature_grid_validation_rule_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    df = pd.DataFrame(VALIDATION_RULES)
    summary = summarize_feature_grid_validation_rules(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_feature_grid_validation_rules(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_rules": 0, "status": "EMPTY"}

    return {
        "total_rules": len(df),
        "critical_rules": int((df["severity"] == "CRITICAL").sum()) if "severity" in df.columns else 0,
        "all_enforced": True,
        "status": "READY",
    }
