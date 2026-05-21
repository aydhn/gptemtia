import pandas as pd
from typing import List, Optional
from portfolio_regime.regime_config import PortfolioRegimeProfile
from portfolio_regime.regime_models import MacroScenarioDefinition, build_scenario_id

def build_default_macro_scenarios(profile: PortfolioRegimeProfile) -> List[MacroScenarioDefinition]:
    """Builds default macro scenario definitions."""
    scenarios = []

    # USDTRY Up
    scenarios.append(MacroScenarioDefinition(
        scenario_id=build_scenario_id("usdtry_up_scenario", profile.scenario_shock_large),
        scenario_label="usdtry_up_scenario",
        description="USDTRY experiences a large positive shock.",
        shocked_factor="USDTRY=X",
        shock_direction="up",
        shock_size=profile.scenario_shock_large,
        affected_symbols=["USDTRY=X", "EURTRY=X", "GBPTRY=X", "GC=F"],
        methodology="historical_proxy",
        warnings=["Macro senaryo tahmini gerçek piyasa tahmini değildir."]
    ))

    # Gold Down
    scenarios.append(MacroScenarioDefinition(
        scenario_id=build_scenario_id("gold_down_scenario", profile.scenario_shock_medium),
        scenario_label="gold_down_scenario",
        description="Gold experiences a medium negative shock.",
        shocked_factor="GC=F",
        shock_direction="down",
        shock_size=profile.scenario_shock_medium,
        affected_symbols=["GC=F", "SI=F"],
        methodology="historical_proxy",
        warnings=["Macro senaryo tahmini gerçek piyasa tahmini değildir."]
    ))

    # Broad risk off
    scenarios.append(MacroScenarioDefinition(
        scenario_id=build_scenario_id("broad_risk_off_scenario", profile.scenario_shock_large),
        scenario_label="broad_risk_off_scenario",
        description="Broad risk-off sentiment in markets.",
        shocked_factor="market",
        shock_direction="down",
        shock_size=profile.scenario_shock_large,
        affected_symbols=["all"],
        methodology="beta_proxy",
        warnings=["Macro senaryo tahmini gerçek piyasa tahmini değildir."]
    ))

    return scenarios

def infer_symbol_scenario_exposure(symbol: str, asset_class: Optional[str], scenario: MacroScenarioDefinition) -> float:
    """Infers exposure of a symbol to a scenario."""
    if "all" in scenario.affected_symbols:
        return 1.0 if scenario.shock_direction == "up" else -1.0

    if symbol in scenario.affected_symbols:
        return 1.0 if scenario.shock_direction == "up" else -1.0

    return 0.0

def build_scenario_exposure_matrix(symbols: List[str], metadata_df: pd.DataFrame, scenarios: List[MacroScenarioDefinition]) -> pd.DataFrame:
    """Builds a matrix of symbol exposures to scenarios."""
    results = []
    for symbol in symbols:
        row = {"symbol": symbol}
        # In a real impl, fetch asset_class from metadata_df
        asset_class = None
        for scenario in scenarios:
            exposure = infer_symbol_scenario_exposure(symbol, asset_class, scenario)
            row[scenario.scenario_id] = exposure
        results.append(row)

    return pd.DataFrame(results).set_index("symbol")

def macro_scenarios_to_dataframe(scenarios: List[MacroScenarioDefinition]) -> pd.DataFrame:
    """Converts scenarios to a dataframe."""
    from portfolio_regime.regime_models import macro_scenario_definition_to_dict
    return pd.DataFrame([macro_scenario_definition_to_dict(s) for s in scenarios])
