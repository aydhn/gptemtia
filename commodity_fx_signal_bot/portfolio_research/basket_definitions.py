from datetime import datetime, timezone
import pandas as pd
from portfolio_research.portfolio_models import VirtualBasketDefinition, build_virtual_basket_id, normalize_weights
from portfolio_research.portfolio_config import PortfolioResearchProfile
from portfolio_research.exposure_analysis import calculate_asset_class_exposure

def enforce_weight_limits(weights: dict[str, float], profile: PortfolioResearchProfile, metadata_df: pd.DataFrame | None = None) -> tuple[dict[str, float], dict]:
    warnings = []
    if not weights:
        return {}, {"warnings": warnings}

    w = normalize_weights(weights)

    capped = False
    for sym in w:
        if w[sym] > profile.max_single_symbol_weight:
            w[sym] = profile.max_single_symbol_weight
            capped = True

    if capped:
        w = normalize_weights(w)

    if metadata_df is not None and not metadata_df.empty:
        ac_exp = calculate_asset_class_exposure(w, metadata_df)
        if not ac_exp.empty:
            for _, row in ac_exp.iterrows():
                if row['exposure_weight'] > profile.max_asset_class_weight:
                    ac = row['asset_class']
                    ac_symbols = [s for s, wt in w.items() if metadata_df.loc[s, 'asset_class'] == ac]
                    scale_factor = profile.max_asset_class_weight / row['exposure_weight']
                    for s in ac_symbols:
                        w[s] *= scale_factor
                    warnings.append(f"Scaled down asset class {ac} to meet max weight limit.")

        w = normalize_weights(w)

    return w, {"warnings": warnings}


def build_equal_weight_basket(symbols: list[str], timeframe: str, profile: PortfolioResearchProfile) -> VirtualBasketDefinition:
    if not symbols:
        return VirtualBasketDefinition(basket_id="", basket_name="", basket_type="equal_weight_basket", timeframe=timeframe, symbols=[], weights={}, created_at_utc=datetime.now(timezone.utc).isoformat(), methodology="Empty", warnings=["No symbols provided."])

    n = min(len(symbols), profile.max_basket_symbols)
    selected = symbols[:n]
    w = 1.0 / n
    weights = {sym: w for sym in selected}

    weights, limits_info = enforce_weight_limits(weights, profile)

    basket_id = build_virtual_basket_id("equal_weight_basket", timeframe, selected)

    return VirtualBasketDefinition(
        basket_id=basket_id,
        basket_name=f"EW_{timeframe}_{n}Assets",
        basket_type="equal_weight_basket",
        timeframe=timeframe,
        symbols=selected,
        weights=weights,
        created_at_utc=datetime.now(timezone.utc).isoformat(),
        methodology="Equal Weight",
        warnings=limits_info.get("warnings", [])
    )

def build_research_score_weighted_basket(ranking_df: pd.DataFrame, timeframe: str, profile: PortfolioResearchProfile) -> VirtualBasketDefinition:
    if ranking_df is None or ranking_df.empty or 'research_score' not in ranking_df.columns:
        return build_equal_weight_basket([], timeframe, profile)

    df = ranking_df.sort_values(by='research_score', ascending=False)
    selected = df.head(profile.max_basket_symbols)['symbol'].tolist()
    scores = df.head(profile.max_basket_symbols)['research_score'].tolist()

    if sum(scores) == 0:
        weights = {sym: 1.0/len(selected) for sym in selected}
    else:
        weights = {sym: score/sum(scores) for sym, score in zip(selected, scores)}

    weights, limits_info = enforce_weight_limits(weights, profile)
    basket_id = build_virtual_basket_id("research_score_weighted_basket", timeframe, selected)

    return VirtualBasketDefinition(
        basket_id=basket_id,
        basket_name=f"RSW_{timeframe}_{len(selected)}Assets",
        basket_type="research_score_weighted_basket",
        timeframe=timeframe,
        symbols=selected,
        weights=weights,
        created_at_utc=datetime.now(timezone.utc).isoformat(),
        methodology="Research Score Weighted",
        warnings=limits_info.get("warnings", [])
    )

def build_risk_adjusted_basket(ranking_df: pd.DataFrame, timeframe: str, profile: PortfolioResearchProfile) -> VirtualBasketDefinition:
    if ranking_df is None or ranking_df.empty or 'risk_score' not in ranking_df.columns:
        return build_equal_weight_basket([], timeframe, profile)

    df = ranking_df.sort_values(by='risk_score', ascending=True)
    selected = df.head(profile.max_basket_symbols)['symbol'].tolist()

    safe_scores = [max(0.01, rs) for rs in df.head(profile.max_basket_symbols)['risk_score'].tolist()]
    inv_scores = [1.0/rs for rs in safe_scores]

    weights = {sym: inv/sum(inv_scores) for sym, inv in zip(selected, inv_scores)}
    weights, limits_info = enforce_weight_limits(weights, profile)

    basket_id = build_virtual_basket_id("risk_adjusted_basket", timeframe, selected)

    return VirtualBasketDefinition(
        basket_id=basket_id,
        basket_name=f"RA_{timeframe}_{len(selected)}Assets",
        basket_type="risk_adjusted_basket",
        timeframe=timeframe,
        symbols=selected,
        weights=weights,
        created_at_utc=datetime.now(timezone.utc).isoformat(),
        methodology="Risk Adjusted (Inverse Risk Score)",
        warnings=limits_info.get("warnings", [])
    )

def build_paper_performance_weighted_basket(ranking_df: pd.DataFrame, timeframe: str, profile: PortfolioResearchProfile) -> VirtualBasketDefinition:
    if ranking_df is None or ranking_df.empty or 'paper_score' not in ranking_df.columns:
        return build_equal_weight_basket([], timeframe, profile)

    df = ranking_df.sort_values(by='paper_score', ascending=False)
    df = df[df['paper_score'] > 0]

    if df.empty:
        return build_equal_weight_basket([], timeframe, profile)

    selected = df.head(profile.max_basket_symbols)['symbol'].tolist()
    scores = df.head(profile.max_basket_symbols)['paper_score'].tolist()

    weights = {sym: score/sum(scores) for sym, score in zip(selected, scores)}
    weights, limits_info = enforce_weight_limits(weights, profile)

    basket_id = build_virtual_basket_id("paper_performance_weighted_basket", timeframe, selected)

    return VirtualBasketDefinition(
        basket_id=basket_id,
        basket_name=f"PPW_{timeframe}_{len(selected)}Assets",
        basket_type="paper_performance_weighted_basket",
        timeframe=timeframe,
        symbols=selected,
        weights=weights,
        created_at_utc=datetime.now(timezone.utc).isoformat(),
        methodology="Paper Performance Weighted",
        warnings=limits_info.get("warnings", [])
    )

def build_default_virtual_baskets(symbols: list[str], ranking_df: pd.DataFrame | None, timeframe: str, profile: PortfolioResearchProfile) -> tuple[list[VirtualBasketDefinition], dict]:
    baskets = []
    warnings = []

    if profile.equal_weight_enabled:
        baskets.append(build_equal_weight_basket(symbols, timeframe, profile))

    if ranking_df is not None and not ranking_df.empty:
        if profile.score_weight_enabled:
            baskets.append(build_research_score_weighted_basket(ranking_df, timeframe, profile))
        if profile.risk_weight_enabled:
            baskets.append(build_risk_adjusted_basket(ranking_df, timeframe, profile))
        if profile.paper_weight_enabled:
            baskets.append(build_paper_performance_weighted_basket(ranking_df, timeframe, profile))
    else:
        warnings.append("Ranking DF is missing, skipping score/risk/paper weighted baskets.")

    baskets = [b for b in baskets if b.symbols]

    return baskets, {"warnings": warnings}
