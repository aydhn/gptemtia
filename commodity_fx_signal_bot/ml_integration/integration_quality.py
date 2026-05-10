"""
Integration Quality

Checks integration reports and outputs to verify rules, check coverage, and ensure no forbidden live trading terms exist.
"""

import pandas as pd
from typing import Dict, Optional, List


FORBIDDEN_LIVE_TERMS = [
    "LIVE_SIGNAL",
    "BUY",
    "SELL",
    "OPEN_LONG",
    "OPEN_SHORT",
    "LIVE_ORDER",
    "BROKER_ORDER",
    "SEND_ORDER",
    "EXECUTE_TRADE",
    "REAL_POSITION",
    "LIVE_POSITION",
    "DEPLOYED_LIVE_MODEL",
]


def check_ml_context_coverage(
    ml_context_df: pd.DataFrame, candidate_df: Optional[pd.DataFrame] = None
) -> dict:
    """Check how much of the candidates timeframe is covered by ML context."""
    if candidate_df is None or candidate_df.empty:
        return {"coverage_ratio": 0.0, "status": "no_candidates"}

    if ml_context_df is None or ml_context_df.empty:
        return {"coverage_ratio": 0.0, "status": "no_context"}

    # How many candidate indices exist in ML context bounds
    try:
        # In test we pass df1, df2. We want to know how much of df2 is in df1.
        min_ml, max_ml = ml_context_df.index.min(), ml_context_df.index.max()
        covered = candidate_df.index[(candidate_df.index >= min_ml) & (candidate_df.index <= max_ml)]
        ratio = len(covered) / len(candidate_df) if len(candidate_df) > 0 else 0.0
    except Exception:
        ratio = 0.0

    return {
        "coverage_ratio": float(ratio),
        "status": "ok" if ratio > 0.5 else "low_coverage"
    }


def check_alignment_frame_quality(alignment_df: pd.DataFrame) -> dict:
    """Check alignment frame score ranges and completeness."""
    if alignment_df is None or alignment_df.empty:
        return {"alignment_rows": 0, "invalid_score_count": 0}

    invalid_scores = 0

    score_cols = [
        "ml_support_score",
        "ml_conflict_score",
        "ml_uncertainty_penalty",
        "model_signal_alignment_score",
        "model_decision_alignment_score",
        "model_strategy_alignment_score"
    ]

    for col in score_cols:
        if col in alignment_df.columns:
            invalid = alignment_df[(alignment_df[col] < 0.0) | (alignment_df[col] > 1.0)]
            invalid_scores += len(invalid)

    return {
        "alignment_rows": len(alignment_df),
        "invalid_score_count": invalid_scores,
    }


def check_model_aware_score_ranges(df: pd.DataFrame) -> dict:
    """Check model-aware score ranges to ensure clamping works."""
    if df is None or df.empty:
        return {"invalid_adjusted_scores": 0}

    invalid = 0
    if "model_aware_candidate_score" in df.columns:
        out_of_bounds = df[(df["model_aware_candidate_score"] < 0.0) | (df["model_aware_candidate_score"] > 1.0)]
        invalid += len(out_of_bounds)

    return {"invalid_adjusted_scores": invalid}


def check_ml_conflict_filter_quality(conflict_df: pd.DataFrame) -> dict:
    """Count high conflicts in the conflict filter frame."""
    if conflict_df is None or conflict_df.empty:
        return {"high_conflict_count": 0}

    count = 0
    if "conflict_label" in conflict_df.columns:
        from .integration_labels import MODEL_CONFLICTS_WITH_CANDIDATE
        count = len(conflict_df[conflict_df["conflict_label"] == MODEL_CONFLICTS_WITH_CANDIDATE])

    return {"high_conflict_count": count}


def check_for_forbidden_live_terms_in_ml_integration(
    df: Optional[pd.DataFrame] = None, summary: Optional[dict] = None
) -> dict:
    """Ensure no live execution terms leak into ML context outputs."""
    found_terms = set()

    def search_text(text: str):
        text_upper = text.upper()
        for term in FORBIDDEN_LIVE_TERMS:
            if term in text_upper:
                found_terms.add(term)

    if summary:
        # Recursive search in dict
        def traverse_dict(d):
            if isinstance(d, dict):
                for k, v in d.items():
                    search_text(str(k))
                    traverse_dict(v)
            elif isinstance(d, list):
                for v in d:
                    traverse_dict(v)
            else:
                search_text(str(d))
        traverse_dict(summary)

    if df is not None and not df.empty:
        # Search in string columns and index names
        search_text(str(df.index.name))
        for col in df.columns:
            search_text(str(col))
            # Just search all string columns directly
            sample = df[col].dropna().astype(str).tolist()[:1000]
            for val in sample:
                search_text(val)

    return {
        "forbidden_live_terms_found": list(found_terms),
        "passed_forbidden_check": len(found_terms) == 0
    }


def build_ml_integration_quality_report(
    summary: dict,
    alignment_df: Optional[pd.DataFrame] = None,
    adjusted_df: Optional[pd.DataFrame] = None
) -> dict:
    """Build the overall ML integration quality report."""

    forbidden_check = check_for_forbidden_live_terms_in_ml_integration(alignment_df, summary)
    if adjusted_df is not None:
        forbidden_check2 = check_for_forbidden_live_terms_in_ml_integration(adjusted_df, None)
        forbidden_check["forbidden_live_terms_found"].extend(forbidden_check2["forbidden_live_terms_found"])
        forbidden_check["forbidden_live_terms_found"] = list(set(forbidden_check["forbidden_live_terms_found"]))
        forbidden_check["passed_forbidden_check"] = len(forbidden_check["forbidden_live_terms_found"]) == 0

    alignment_check = check_alignment_frame_quality(alignment_df)
    score_check = check_model_aware_score_ranges(adjusted_df)

    warnings = []
    passed = True

    if not forbidden_check["passed_forbidden_check"]:
        passed = False
        warnings.append(f"Forbidden terms found: {forbidden_check['forbidden_live_terms_found']}")

    if alignment_check["invalid_score_count"] > 0:
        passed = False
        warnings.append("Invalid scores outside [0,1] range in alignment frame")

    if score_check["invalid_adjusted_scores"] > 0:
        passed = False
        warnings.append("Invalid adjusted scores outside [0,1] range")

    return {
        "ml_context_coverage_ratio": summary.get("coverage_ratio", 0.0),
        "alignment_rows": alignment_check["alignment_rows"],
        "invalid_score_count": alignment_check["invalid_score_count"] + score_check["invalid_adjusted_scores"],
        "high_conflict_count": summary.get("conflict_count", 0),
        "high_uncertainty_count": summary.get("high_uncertainty_count", 0),
        "forbidden_live_terms_found": forbidden_check["forbidden_live_terms_found"],
        "warning_count": len(warnings),
        "passed": passed,
        "warnings": warnings,
    }
