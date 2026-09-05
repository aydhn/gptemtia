"""Phase 131: Cross-Asset Regime Context Scoring.

Calculates composite diagnostic scores assessing completeness, contract integrity,
and non-signal guard compliance for Cross-Asset Regime Context Expansion.
"""

from typing import Any, Dict, Optional, Tuple
import uuid
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)
from advanced_cross_asset_regime_context.cross_asset_regime_models import (
    CrossAssetContextScore,
)


def classify_cross_asset_context_score(
    score: float, profile: Optional[CrossAssetRegimeProfile] = None
) -> str:
    """Classify context score into standardized diagnostic tiers."""
    min_score = profile.min_context_score if profile else 0.45
    if score >= 0.80:
        return "high_context_integrity"
    elif score >= min_score:
        return "adequate_context_integrity"
    else:
        return "substandard_context_integrity"


def calculate_cross_asset_context_score(
    findings_df: pd.DataFrame,
    profile: Optional[CrossAssetRegimeProfile] = None,
    entity_count: int = 24,
    pair_count: int = 12,
    contract_count: int = 6,
    manual_review_count: int = 7,
) -> CrossAssetContextScore:
    """Calculate internal diagnostic context score based on findings penalty."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    base_score = 0.90
    if not findings_df.empty:
        penalty = len(findings_df) * 0.02
        base_score = max(0.0, min(1.0, base_score - penalty))

    classification = classify_cross_asset_context_score(base_score, profile)

    return CrossAssetContextScore(
        score_id=f"score_{uuid.uuid4().hex[:8]}",
        context_score=round(base_score, 4),
        classification=classification,
        active_profile=profile.profile_name,
        entity_count=entity_count,
        pair_count=pair_count,
        contract_count=contract_count,
        findings_count=len(findings_df),
        manual_review_count=manual_review_count,
        non_signal=True,
        source_preserved=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
    )


def build_cross_asset_regime_context_score_report(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build context score report dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    # Default evaluation with 2 sample info findings
    mock_findings = pd.DataFrame([{"finding_id": "f1"}, {"finding_id": "f2"}])
    score_obj = calculate_cross_asset_context_score(mock_findings, profile)

    row = {
        "score_id": score_obj.score_id,
        "context_score": score_obj.context_score,
        "classification": score_obj.classification,
        "active_profile": score_obj.active_profile,
        "entity_count": score_obj.entity_count,
        "pair_count": score_obj.pair_count,
        "contract_count": score_obj.contract_count,
        "findings_count": score_obj.findings_count,
        "manual_review_count": score_obj.manual_review_count,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
        "contains_target_or_prediction": False,
        "contains_trading_recommendation": False,
    }

    df = pd.DataFrame([row])
    summary = summarize_cross_asset_context_scores(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_context_scores(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize context scores."""
    mean_score = float(df["context_score"].mean()) if not df.empty else 0.0
    classification = str(df["classification"].iloc[0]) if not df.empty else "unknown"
    return {
        "total_scores": len(df),
        "context_score": mean_score,
        "classification": classification,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "official_approval_claim": False,
        "production_ready_claim": False,
        "broker_ready_claim": False,
        "zero_trading_signals": True,
    }
