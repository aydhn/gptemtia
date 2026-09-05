from collections import Counter
from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


DUPLICATE_DETECTION_POLICIES = [
    {
        "check_name": "name_duplicate_check",
        "description": "Grid feature isimlerinde birebir aynı stringlerin bulunmasını tespit eder.",
        "action": "flag_for_manual_review",
        "auto_delete": False,
    },
    {
        "check_name": "column_series_identical_check",
        "description": "DataFrame içinde tamamen özdeş değerlere sahip farklı isimli kolonları tespit eder.",
        "action": "flag_for_manual_review",
        "auto_delete": False,
    },
]


def detect_duplicate_feature_names(feature_names: List[str]) -> Dict[str, Any]:
    counts = Counter(feature_names)
    duplicates = {name: cnt for name, cnt in counts.items() if cnt > 1}

    return {
        "has_duplicates": len(duplicates) > 0,
        "duplicate_count": len(duplicates),
        "duplicates": duplicates,
        "manual_review_required": len(duplicates) > 0,
    }


def detect_duplicate_feature_columns(df: pd.DataFrame, feature_columns: List[str]) -> Dict[str, Any]:
    duplicates = []
    # Check if identical series exist
    for i in range(len(feature_columns)):
        col_a = feature_columns[i]
        if col_a not in df.columns:
            continue
        for j in range(i + 1, len(feature_columns)):
            col_b = feature_columns[j]
            if col_b not in df.columns:
                continue
            # Compare non-NaN values
            s_a = df[col_a].dropna()
            s_b = df[col_b].dropna()
            if len(s_a) == len(s_b) and (s_a == s_b).all():
                duplicates.append({"col_a": col_a, "col_b": col_b, "reason": "identical_values"})

    return {
        "has_duplicates": len(duplicates) > 0,
        "duplicate_pairs_count": len(duplicates),
        "duplicate_pairs": duplicates,
        "manual_review_required": len(duplicates) > 0,
    }


def build_feature_grid_duplicate_detection_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    df = pd.DataFrame(DUPLICATE_DETECTION_POLICIES)
    summary = summarize_feature_grid_duplicate_detection(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_feature_grid_duplicate_detection(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_checks": 0, "status": "EMPTY"}

    return {
        "total_checks": len(df),
        "auto_delete_allowed": False,
        "action": "flag_for_manual_review",
        "status": "ACTIVE",
    }
