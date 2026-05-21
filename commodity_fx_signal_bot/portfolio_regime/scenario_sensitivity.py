import pandas as pd
from typing import Tuple, List, Dict
from portfolio_regime.regime_models import MacroScenarioDefinition
from core.logger import get_logger

logger = get_logger(__name__)

def calculate_symbol_scenario_sensitivity(returns_df: pd.DataFrame, scenario_exposure_df: pd.DataFrame) -> pd.DataFrame:
    """Calculates symbol sensitivity to scenarios."""
    if returns_df.empty or scenario_exposure_df.empty:
        return pd.DataFrame()

    results = []
    for scenario_id in scenario_exposure_df.columns:
        for symbol in scenario_exposure_df.index:
            exposure = scenario_exposure_df.loc[symbol, scenario_id]
            # Simple placeholder for estimated impact
            # Assume 1.0 exposure = 1% impact
            estimated_impact = exposure * 0.01

            results.append({
                'symbol': symbol,
                'scenario_id': scenario_id,
                'exposure_score': exposure,
                'estimated_directional_impact': estimated_impact,
                'sensitivity_score': abs(exposure),
                'warning_label': 'high_sensitivity' if abs(exposure) > 0.8 else 'normal'
            })

    return pd.DataFrame(results)

def calculate_basket_scenario_sensitivity(weights: Dict[str, float], scenario_exposure_df: pd.DataFrame) -> pd.DataFrame:
    """Calculates basket sensitivity to scenarios based on weights."""
    if not weights or scenario_exposure_df.empty:
        return pd.DataFrame()

    results = []
    for scenario_id in scenario_exposure_df.columns:
        basket_exposure = 0.0
        for symbol, weight in weights.items():
            if symbol in scenario_exposure_df.index:
                basket_exposure += weight * scenario_exposure_df.loc[symbol, scenario_id]

        estimated_impact = basket_exposure * 0.01

        results.append({
            'scenario_id': scenario_id,
            'exposure_score': basket_exposure,
            'estimated_directional_impact': estimated_impact,
            'sensitivity_score': abs(basket_exposure),
            'warning_label': 'high_sensitivity' if abs(basket_exposure) > 0.8 else 'normal'
        })

    return pd.DataFrame(results)

def build_basket_scenario_sensitivity_table(baskets_df: pd.DataFrame, scenario_exposure_df: pd.DataFrame) -> pd.DataFrame:
    """Builds table of all baskets' sensitivities."""
    # Placeholder
    return pd.DataFrame()

def summarize_scenario_sensitivity(sensitivity_df: pd.DataFrame) -> dict:
    """Summarizes scenario sensitivity."""
    if sensitivity_df.empty:
        return {"status": "empty"}

    return {
        "status": "success",
        "scenarios_analyzed": len(sensitivity_df['scenario_id'].unique()),
        "high_sensitivity_count": len(sensitivity_df[sensitivity_df['warning_label'] == 'high_sensitivity'])
    }

def build_scenario_sensitivity_report(
    returns_df: pd.DataFrame,
    baskets_df: pd.DataFrame,
    metadata_df: pd.DataFrame,
    scenarios: List[MacroScenarioDefinition]
) -> Tuple[pd.DataFrame, dict]:
    """Builds full scenario sensitivity report."""
    logger.info("Building scenario sensitivity report")
    summary = {"warnings": []}

    from portfolio_regime.macro_scenarios import build_scenario_exposure_matrix

    if returns_df.empty:
        return pd.DataFrame(), summary

    exposure_df = build_scenario_exposure_matrix(returns_df.columns.tolist(), metadata_df, scenarios)
    sensitivity_df = calculate_symbol_scenario_sensitivity(returns_df, exposure_df)

    summary = summarize_scenario_sensitivity(sensitivity_df)

    return sensitivity_df, summary
