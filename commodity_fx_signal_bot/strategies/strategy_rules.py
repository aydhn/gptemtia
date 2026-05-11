import pandas as pd

from strategies.strategy_config import StrategySelectionProfile
from strategies.strategy_family import get_strategy_family_spec


def calculate_regime_fit(
    family: str, context_snapshot: dict
) -> tuple[float, list[str]]:
    spec = get_strategy_family_spec(family)
    reasons = []

    if "regime_events" not in context_snapshot and "regime" not in context_snapshot:
        reasons.append("Missing regime context")
        return 0.5, reasons

    current_regime = "unknown"
    regime_data = context_snapshot.get(
        "regime_events", context_snapshot.get("regime", {})
    )

    if "regime_label" in regime_data:
        current_regime = regime_data["regime_label"]
    elif "current_regime" in regime_data:
        current_regime = regime_data["current_regime"]

    if current_regime == "unknown":
        reasons.append("Regime unknown")
        return 0.5, reasons

    if current_regime in spec.avoided_regimes:
        reasons.append(f"Avoided regime ({current_regime})")
        return 0.1, reasons

    if current_regime in spec.preferred_regimes:
        return 0.9, reasons

    return 0.5, reasons


def calculate_mtf_fit(family: str, context_snapshot: dict) -> tuple[float, list[str]]:
    reasons = []

    if "mtf_events" not in context_snapshot and "mtf" not in context_snapshot:
        reasons.append("Missing MTF context")
        return 0.5, reasons

    mtf_data = context_snapshot.get("mtf_events", context_snapshot.get("mtf", {}))

    is_trend = family in ("trend_following", "momentum_continuation", "pullback")
    mtf_aligned = mtf_data.get("mtf_trend_alignment_bullish", False) or mtf_data.get(
        "mtf_trend_alignment_bearish", False
    )

    if is_trend:
        if mtf_aligned:
            return 0.9, reasons
        else:
            reasons.append("MTF trend not aligned")
            return 0.3, reasons

    if family == "mean_reversion":
        if mtf_aligned:
            reasons.append("MTF strong trend limits mean reversion")
            return 0.3, reasons
        return 0.7, reasons

    return 0.5, reasons


def calculate_asset_profile_fit(
    family: str, context_snapshot: dict
) -> tuple[float, list[str]]:
    spec = get_strategy_family_spec(family)
    reasons = []

    if "asset_profiles" not in context_snapshot:
        reasons.append("Missing asset profile context")
        return 0.5, reasons

    profile_data = context_snapshot.get("asset_profiles", {})
    profile_label = profile_data.get("behavioral_profile", "unknown")

    if profile_label in spec.preferred_asset_profiles:
        return 0.9, reasons

    return 0.5, reasons


def calculate_macro_fit(family: str, context_snapshot: dict) -> tuple[float, list[str]]:
    reasons = []
    if "macro_events" not in context_snapshot:
        reasons.append("Missing macro context")
        return 0.5, reasons
    return 0.5, reasons


def calculate_decision_fit(family: str, decision_row: pd.Series) -> float:
    return float(decision_row.get("decision_score", 0.5))


def calculate_conflict_penalty(
    family: str, decision_row: pd.Series, context_snapshot: dict
) -> float:
    return float(decision_row.get("conflict_score", 0.0))


def calculate_strategy_selection_score(
    components: dict[str, float], profile: StrategySelectionProfile
) -> float:
    weights = profile.component_weights
    total_score = 0.0
    weight_sum = 0.0

    for key, weight in weights.items():
        if key == "conflict_penalty":
            penalty = components.get(key, 0.0)
            total_score -= penalty * weight
            weight_sum += weight
        else:
            val = components.get(key, 0.5)
            total_score += val * weight
            weight_sum += weight

    if weight_sum > 0:
        score = total_score / weight_sum
        return max(0.0, min(1.0, score))
    return 0.0


def calculate_strategy_family_fit(
    family: str,
    decision_row: pd.Series,
    context_snapshot: dict,
    profile: StrategySelectionProfile,
) -> dict:

    regime_fit, regime_reasons = calculate_regime_fit(family, context_snapshot)
    mtf_fit, mtf_reasons = calculate_mtf_fit(family, context_snapshot)
    asset_profile_fit, asset_reasons = calculate_asset_profile_fit(
        family, context_snapshot
    )
    macro_fit, macro_reasons = calculate_macro_fit(family, context_snapshot)

    decision_fit = calculate_decision_fit(family, decision_row)
    conflict_penalty = calculate_conflict_penalty(
        family, decision_row, context_snapshot
    )

    decision_confidence = decision_row.get("confidence", 0.5)
    decision_quality = decision_row.get("quality_score", 0.5)

    components = {
        "decision_score": decision_fit,
        "decision_confidence": decision_confidence,
        "decision_quality": decision_quality,
        "regime_fit": regime_fit,
        "mtf_fit": mtf_fit,
        "asset_profile_fit": asset_profile_fit,
        "macro_fit": macro_fit,
        "conflict_penalty": conflict_penalty,
    }

    selection_score = calculate_strategy_selection_score(components, profile)

    fit_score_components = {
        "regime_fit": regime_fit,
        "mtf_fit": mtf_fit,
        "asset_profile_fit": asset_profile_fit,
        "macro_fit": macro_fit,
    }
    fit_score = sum(fit_score_components.values()) / max(1, len(fit_score_components))

    block_reasons = []
    block_reasons.extend(regime_reasons)
    block_reasons.extend(mtf_reasons)

    if selection_score < profile.min_selection_score:
        block_reasons.append("Low selection score")
    if fit_score < profile.min_fit_score:
        block_reasons.append("Low fit score")
    if conflict_penalty > profile.max_conflict_score:
        block_reasons.append("High conflict penalty")

    return {
        "family": family,
        "decision_fit": float(decision_fit),
        "regime_fit": float(regime_fit),
        "mtf_fit": float(mtf_fit),
        "asset_profile_fit": float(asset_profile_fit),
        "macro_fit": float(macro_fit),
        "conflict_penalty": float(conflict_penalty),
        "selection_score": float(selection_score),
        "fit_score": float(fit_score),
        "block_reasons": list(set(block_reasons)),
        "warnings": [],
    }


def calculate_ml_strategy_fit(family: str, context_snapshot: dict) -> float:
    """
    Optionally evaluate strategy fit based on ML context.
    Returns 0.5 (neutral) if unavailable.
    """
    ml_context = context_snapshot.get("ml_prediction_context")
    if ml_context is None or ml_context.empty:
        ml_context = context_snapshot.get("ml_integration_strategy")
        if ml_context is None or ml_context.empty:
            return 0.5

    # Assuming snapshot is already for the current timestamp
    if isinstance(ml_context, pd.DataFrame):
        if not ml_context.empty:
            ml_row = ml_context.iloc[-1]
        else:
            return 0.5
    else:
        ml_row = ml_context

    if "model_strategy_alignment_score" in ml_row:
        return float(ml_row["model_strategy_alignment_score"])

    prediction = str(ml_row.get("predicted_direction", "flat")).lower()
    confidence = float(ml_row.get("confidence_score", 0.0))
    uncertainty = float(ml_row.get("uncertainty_score", 0.0))

    if family == "trend_following":
        if prediction in ["up", "down"]:
            return min(1.0, 0.5 + (confidence * 0.5) - (uncertainty * 0.2))
        else:
            return 0.4
    elif family == "mean_reversion":
        if prediction == "flat":
            return min(1.0, 0.5 + (confidence * 0.5))
        elif uncertainty > 0.5:
            # High uncertainty might mean ranging/mean reversion is okay
            return 0.6
        else:
            return 0.3

    return 0.5
