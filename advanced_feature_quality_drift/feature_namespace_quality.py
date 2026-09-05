"""Phase 123 Feature Namespace Quality.

Audits feature column naming for collisions, invalid casing, and forbidden forward-looking
or signal tokens (e.g. target, label, future, forward, predict, buy, sell).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)

FORBIDDEN_NAME_TOKENS = [
    "target", "label", "future", "forward", "predict", "next_return",
    "shift_minus", "signal", "buy", "sell", "order", "prediction",
]


def validate_feature_namespace_quality(
    feature_columns: List[str],
) -> pd.DataFrame:
    """Audit feature names for forbidden tokens, duplicates, and style conventions."""
    seen_names = set()
    records = []

    for col in feature_columns:
        col_lower = col.lower()
        has_forbidden = False
        forbidden_found = []

        for tok in FORBIDDEN_NAME_TOKENS:
            if tok in col_lower:
                has_forbidden = True
                forbidden_found.append(tok)

        is_duplicate = col_lower in seen_names
        seen_names.add(col_lower)

        has_standard_prefix = col_lower.startswith(("feat_", "factor_", "ind_", "macro_", "event_", "news_", "quote_"))

        if has_forbidden:
            status = "diagnostic_fail"
            sev = "quality_critical"
            issue = f"Forbidden tokens detected: {', '.join(forbidden_found)}"
            review = True
        elif is_duplicate:
            status = "diagnostic_fail"
            sev = "quality_high"
            issue = "Case-insensitive namespace collision / duplicate name"
            review = True
        elif not has_standard_prefix:
            status = "diagnostic_pass_with_warnings"
            sev = "quality_medium"
            issue = "Non-standard prefix naming convention"
            review = False
        else:
            status = "diagnostic_pass"
            sev = "quality_info"
            issue = "Compliant namespace"
            review = False

        records.append({
            "feature_column": col,
            "has_forbidden_token": has_forbidden,
            "forbidden_tokens": ",".join(forbidden_found),
            "is_duplicate": is_duplicate,
            "has_standard_prefix": has_standard_prefix,
            "issue_description": issue,
            "status": status,
            "severity": sev,
            "manual_review_required": review,
        })

    return pd.DataFrame(records)


def summarize_feature_namespace_quality(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from namespace quality DataFrame."""
    if df.empty:
        return {
            "total_features_checked": 0,
            "forbidden_name_count": 0,
            "namespace_collision_count": 0,
            "non_standard_prefix_count": 0,
            "status": "diagnostic_pass",
            "manual_review_required": False,
        }

    total_features = len(df)
    forbid_count = int(df["has_forbidden_token"].sum()) if "has_forbidden_token" in df.columns else 0
    coll_count = int(df["is_duplicate"].sum()) if "is_duplicate" in df.columns else 0
    non_std = int((~df["has_standard_prefix"]).sum()) if "has_standard_prefix" in df.columns else 0

    if forbid_count > 0 or coll_count > 0:
        overall_status = "diagnostic_fail"
    elif non_std > 0:
        overall_status = "diagnostic_pass_with_warnings"
    else:
        overall_status = "diagnostic_pass"

    return {
        "total_features_checked": total_features,
        "forbidden_name_count": forbid_count,
        "namespace_collision_count": coll_count,
        "non_standard_prefix_count": non_std,
        "status": overall_status,
        "manual_review_required": (forbid_count + coll_count) > 0,
    }


def build_feature_namespace_quality_report(
    profile: FeatureQualityDriftProfile | None = None,
    feature_columns: List[str] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build namespace quality report and metadata summary."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    cols = feature_columns or [
        "feat_rsi_14", "feat_macd_line", "feat_bb_upper_20",
        "feat_atr_14", "feat_volatility_parkinson_20", "feat_macro_cpi_surprise"
    ]

    res_df = validate_feature_namespace_quality(cols)
    summary = summarize_feature_namespace_quality(res_df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return res_df, summary
