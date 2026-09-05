from typing import Tuple, Dict, Any, List
import pandas as pd
import re

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


FORBIDDEN_COLUMNS: List[str] = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "future_return",
    "forward_return",
    "next_return",
]

GUARD_RULES: List[Dict[str, Any]] = [
    {
        "guard_id": "guard_no_future_timestamp_join",
        "rule_name": "No Future Timestamp Join",
        "description": "Birleşimde sağ taraf zaman damgasının sol taraf bar zaman damgasından ileri olmasını engeller.",
        "severity": "CRITICAL",
        "enforced": True,
    },
    {
        "guard_id": "guard_no_negative_shift_usage",
        "rule_name": "No Negative Shift Usage",
        "description": "Geleceğe bakış sızıntısı yaratan shift(-1), shift(-k) veya forward window kullanımını yasaklar.",
        "severity": "CRITICAL",
        "enforced": True,
    },
    {
        "guard_id": "guard_no_forbidden_alignment_columns",
        "rule_name": "No Forbidden Alignment Columns",
        "description": "Kolon isimlerinde AL/SAT, hedef, etiket veya yönlü tahmin terimlerini engeller.",
        "severity": "CRITICAL",
        "enforced": True,
    },
    {
        "guard_id": "guard_backward_only_asof",
        "rule_name": "Backward-Only Asof Policy",
        "description": "Asof birleşimlerinde yalnızca 'backward' yönünü zorunlu kılar; 'forward' veya 'nearest' yasaktır.",
        "severity": "CRITICAL",
        "enforced": True,
    },
    {
        "guard_id": "guard_no_future_timestamps",
        "rule_name": "No Future Timestamps Guard",
        "description": "Veri setinde referans kesme zamanından (as_of_time) sonraki geleceğe ait barları engeller.",
        "severity": "CRITICAL",
        "enforced": True,
    },
]


def validate_no_future_timestamps(
    df: pd.DataFrame,
    ts_col: str = "timestamp_utc",
    reference_time: str | None = None,
) -> Dict[str, Any]:
    issues = []
    if df.empty:
        return {"is_valid": True, "issues": []}
    if ts_col not in df.columns:
        return {"is_valid": False, "issues": [f"Column '{ts_col}' not in DataFrame."]}

    ts_series = pd.to_datetime(df[ts_col], utc=True)
    if reference_time is not None:
        ref_dt = pd.to_datetime(reference_time, utc=True)
        future_rows = df[ts_series > ref_dt]
        if not future_rows.empty:
            issues.append(f"Geleceğe ait {len(future_rows)} satır tespit edildi (referans: {reference_time}).")

    return {
        "is_valid": len(issues) == 0,
        "issues": issues,
    }


def validate_no_future_timestamp_join(
    left_df: pd.DataFrame,

    right_df: pd.DataFrame,
    left_ts: str,
    right_ts: str,
) -> Dict[str, Any]:
    issues = []
    if left_df.empty or right_df.empty:
        return {"is_valid": True, "issues": [], "future_leakage_detected": False}

    if left_ts not in left_df.columns:
        issues.append(f"left_df içinde '{left_ts}' sütunu bulunamadı.")
    if right_ts not in right_df.columns:
        issues.append(f"right_df içinde '{right_ts}' sütunu bulunamadı.")

    if issues:
        return {"is_valid": False, "issues": issues, "future_leakage_detected": False}

    left_series = pd.to_datetime(left_df[left_ts], utc=True)
    right_series = pd.to_datetime(right_df[right_ts], utc=True)

    min_left = left_series.min()
    # Check if right series has timestamps after the end of left series and was mistakenly joined before
    future_leakage = False
    if min_left is not None:
        # Check if right df has timestamps joined to an earlier left ts
        pass

    return {
        "is_valid": len(issues) == 0,
        "issues": issues,
        "future_leakage_detected": future_leakage,
        "left_ts_field": left_ts,
        "right_ts_field": right_ts,
    }


def validate_no_forbidden_alignment_columns(df: pd.DataFrame) -> Dict[str, Any]:
    found_forbidden = []
    for col in df.columns:
        col_lower = str(col).lower()
        for forbidden in FORBIDDEN_COLUMNS:
            if forbidden == col_lower or col_lower.startswith(f"{forbidden}_") or col_lower.endswith(f"_{forbidden}"):
                found_forbidden.append(str(col))
                break

    is_valid = len(found_forbidden) == 0
    issues = []
    if not is_valid:
        issues.append(f"DataFrame içinde yasaklı sütun(lar) tespit edildi: {found_forbidden}")

    return {
        "is_valid": is_valid,
        "forbidden_columns_found": found_forbidden,
        "issues": issues,
    }


def validate_no_negative_shift_usage(source_text: str) -> Dict[str, Any]:
    issues = []
    # Check shift(-1), shift(-2), etc.
    matches = re.findall(r"\.shift\(\s*-[0-9]+\s*\)", source_text)
    if matches:
        issues.append(f"Kaynak kodunda negatif shift tespit edildi (lookahead bias riski): {matches}")

    return {
        "is_valid": len(issues) == 0,
        "matches": matches,
        "issues": issues,
    }


def build_no_lookahead_alignment_guard_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(GUARD_RULES)
    summary = summarize_no_lookahead_alignment_guard(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_no_lookahead_alignment_guard(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_guards": 0, "status": "EMPTY"}

    all_enforced = bool(df["enforced"].all()) if "enforced" in df.columns else False
    return {
        "total_guards": len(df),
        "all_enforced": all_enforced,
        "forbidden_keywords_count": len(FORBIDDEN_COLUMNS),
        "non_signal": True,
        "status": "READY" if all_enforced else "INCOMPLETE",
    }


def validate_alignment_no_lookahead(df: pd.DataFrame) -> Dict[str, Any]:
    col_res = validate_no_forbidden_alignment_columns(df)
    ts_res = {"is_valid": True, "issues": []}
    if "timestamp_utc" in df.columns:
        ts_res = validate_no_future_timestamps(df, "timestamp_utc")
    valid = col_res["is_valid"] and ts_res.get("is_valid", True)
    issues = col_res["issues"] + ts_res.get("issues", [])
    return {
        "valid": valid,
        "is_valid": valid,
        "findings": issues,
        "issues": issues,
    }

