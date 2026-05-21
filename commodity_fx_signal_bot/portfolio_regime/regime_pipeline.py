import pandas as pd
from typing import List, Tuple, Optional, Dict
from config.symbols import SymbolSpec
from config.settings import Settings
from data.storage.data_lake import DataLake
from core.logger import get_logger

from portfolio_regime.regime_config import PortfolioRegimeProfile, get_portfolio_regime_profile, get_default_portfolio_regime_profile
from portfolio_regime.regime_data_adapter import PortfolioRegimeDataAdapter
from portfolio_regime.regime_classifier import classify_portfolio_regimes
from portfolio_regime.regime_conditioned_returns import build_regime_conditioned_returns_report
from portfolio_regime.regime_correlation import build_regime_correlation_report
from portfolio_regime.macro_scenarios import build_default_macro_scenarios
from portfolio_regime.scenario_sensitivity import build_scenario_sensitivity_report
from portfolio_regime.stress_windows import identify_historical_stress_windows
from portfolio_regime.basket_stress_test import build_basket_stress_test_report
from portfolio_regime.drawdown_clustering import build_drawdown_cluster_report
from portfolio_regime.recovery_analysis import build_recovery_analysis_report
from portfolio_regime.tail_risk import build_tail_risk_table, summarize_tail_risk
from portfolio_regime.risk_regime_exposure import build_risk_regime_exposure_table, summarize_risk_regime_exposure
from portfolio_regime.regime_quality import build_regime_quality_report
from portfolio_regime.regime_report_builder import (
    build_regime_portfolio_markdown_report,
    build_macro_scenario_markdown_report,
    build_stress_test_markdown_report,
    build_drawdown_cluster_markdown_report,
    build_risk_regime_exposure_markdown_report
)

logger = get_logger(__name__)

class PortfolioRegimePipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: Optional[PortfolioRegimeProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_portfolio_regime_profile()
        self.adapter = PortfolioRegimeDataAdapter(self.data_lake)

    def _get_symbols(self, specs: List[SymbolSpec]) -> List[str]:
        return [s.name for s in specs if s.enabled]

    def build_regime_portfolio_report(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[PortfolioRegimeProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Tuple[dict, dict]:
        logger.info(f"Building portfolio regime report for {len(specs)} specs")
        profile_to_use = profile or self.profile
        symbols = self._get_symbols(specs)

        returns_df, ret_summary = self.adapter.load_universe_returns(timeframe)
        if len(returns_df) < profile_to_use.min_observations:
            logger.warning(f"Insufficient observations. Need {profile_to_use.min_observations}, got {len(returns_df)}")

        regime_df, _ = classify_portfolio_regimes(returns_df, profile_to_use)

        basket_returns_df, _ = self.adapter.load_virtual_basket_performance(timeframe)
        basket_returns = {c: basket_returns_df[c] for c in basket_returns_df.columns} if not basket_returns_df.empty else None

        ret_tables, _ = build_regime_conditioned_returns_report(returns_df, regime_df, basket_returns)
        corr_tables, _ = build_regime_correlation_report(returns_df, regime_df)

        summary = {"status": "success", "profile": profile_to_use.name}

        quality = build_regime_quality_report(summary, regime_df)

        if save:
            if hasattr(self.data_lake, 'save_portfolio_regimes') and not regime_df.empty:
                self.data_lake.save_portfolio_regimes(timeframe, profile_to_use.name, regime_df)

            # Additional saving logic would go here
            pass

        return summary, quality

    def build_macro_scenario_sensitivity_report(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[PortfolioRegimeProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        profile_to_use = profile or self.profile
        scenarios = build_default_macro_scenarios(profile_to_use)
        returns_df, _ = self.adapter.load_universe_returns(timeframe)

        baskets_df = pd.DataFrame() # Placeholder
        metadata_df = pd.DataFrame() # Placeholder

        df, summary = build_scenario_sensitivity_report(returns_df, baskets_df, metadata_df, scenarios)
        return df, summary

    def build_basket_stress_test_report(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[PortfolioRegimeProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], dict]:
        profile_to_use = profile or self.profile

        # Stubs for now
        baskets = []
        basket_returns = {}
        scenarios = build_default_macro_scenarios(profile_to_use)
        scenario_exposure_df = pd.DataFrame()
        stress_windows_df = pd.DataFrame()

        tables, summary = build_basket_stress_test_report(
            baskets, basket_returns, scenarios, scenario_exposure_df, stress_windows_df
        )
        return tables, summary

    def build_drawdown_cluster_report(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[PortfolioRegimeProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        profile_to_use = profile or self.profile
        curves, _ = self.adapter.load_basket_equity_curves(timeframe)
        df, summary = build_drawdown_cluster_report(curves, profile_to_use)
        return df, summary

    def build_risk_regime_exposure_report(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[PortfolioRegimeProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        profile_to_use = profile or self.profile

        returns_df, _ = self.adapter.load_universe_returns(timeframe)
        regime_df, _ = classify_portfolio_regimes(returns_df, profile_to_use)

        basket_returns_df, _ = self.adapter.load_virtual_basket_performance(timeframe)

        df = build_risk_regime_exposure_table(basket_returns_df, regime_df)
        summary = summarize_risk_regime_exposure(df)

        return df, summary
