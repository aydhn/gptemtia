import pandas as pd
from typing import List, Dict, Tuple, Optional
from portfolio_regime.regime_models import MacroScenarioDefinition, BasketStressTestResult
from core.logger import get_logger

logger = get_logger(__name__)

# Mock definition class for typing
class VirtualBasketDefinition:
    def __init__(self, basket_id: str, weights: Dict[str, float]):
        self.basket_id = basket_id
        self.weights = weights

def run_scenario_stress_test_for_basket(
    basket: VirtualBasketDefinition,
    scenarios: List[MacroScenarioDefinition],
    scenario_exposure_df: pd.DataFrame
) -> pd.DataFrame:
    """Runs scenario stress tests for a basket."""
    from portfolio_regime.scenario_sensitivity import calculate_basket_scenario_sensitivity

    if scenario_exposure_df.empty:
        return pd.DataFrame()

    sensitivity = calculate_basket_scenario_sensitivity(basket.weights, scenario_exposure_df)

    results = []
    for _, row in sensitivity.iterrows():
        results.append({
            'basket_id': basket.basket_id,
            'scenario_id': row['scenario_id'],
            'timeframe': '1d',
            'estimated_return_impact': row['estimated_directional_impact'],
            'estimated_drawdown_impact': None,
            'estimated_volatility_impact': None,
            'stress_severity': 'moderate_stress',
            'methodology': 'beta_proxy',
            'warnings': ['Offline simülasyon']
        })

    return pd.DataFrame(results)

def run_historical_stress_test_for_basket(basket_returns: pd.Series, stress_windows_df: pd.DataFrame) -> pd.DataFrame:
    """Runs historical stress tests for a basket."""
    if basket_returns.empty or stress_windows_df.empty:
        return pd.DataFrame()

    results = []
    for _, window in stress_windows_df.iterrows():
        results.append({
            'basket_id': 'unknown',
            'stress_window_id': window['stress_window_id'],
            'realized_return': 0.0, # Placeholder
            'stress_severity': window['stress_severity']
        })

    return pd.DataFrame(results)

def build_basket_stress_test_summary(scenario_stress_df: pd.DataFrame, historical_stress_df: Optional[pd.DataFrame] = None) -> dict:
    """Summarizes stress test results."""
    summary = {
        "status": "success",
        "scenario_tests_run": len(scenario_stress_df) if not scenario_stress_df.empty else 0,
        "historical_tests_run": len(historical_stress_df) if historical_stress_df is not None and not historical_stress_df.empty else 0
    }
    return summary

def build_basket_stress_test_report(
    baskets: List[VirtualBasketDefinition],
    basket_returns: Dict[str, pd.Series],
    scenarios: List[MacroScenarioDefinition],
    scenario_exposure_df: pd.DataFrame,
    stress_windows_df: Optional[pd.DataFrame] = None
) -> Tuple[Dict[str, pd.DataFrame], dict]:
    """Builds the full basket stress test report."""
    logger.info("Building basket stress test report")

    scenario_results = []
    for basket in baskets:
        df = run_scenario_stress_test_for_basket(basket, scenarios, scenario_exposure_df)
        if not df.empty:
            scenario_results.append(df)

    scenario_df = pd.concat(scenario_results, ignore_index=True) if scenario_results else pd.DataFrame()

    historical_df = pd.DataFrame()
    if stress_windows_df is not None and not stress_windows_df.empty:
        hist_results = []
        for basket_id, returns in basket_returns.items():
            df = run_historical_stress_test_for_basket(returns, stress_windows_df)
            if not df.empty:
                df['basket_id'] = basket_id
                hist_results.append(df)
        historical_df = pd.concat(hist_results, ignore_index=True) if hist_results else pd.DataFrame()

    summary = build_basket_stress_test_summary(scenario_df, historical_df)

    tables = {
        "scenario_stress": scenario_df,
        "historical_stress": historical_df
    }

    return tables, summary
