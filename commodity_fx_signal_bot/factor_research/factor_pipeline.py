import pandas as pd
from datetime import datetime
import logging
from config.settings import Settings
from data.storage.data_lake import DataLake
from config.symbols import SymbolSpec
from .factor_config import FactorResearchProfile, get_default_factor_research_profile
from .factor_universe import build_factor_universe, build_factor_metadata_table
from .factor_data_adapter import FactorDataAdapter
from .factor_definitions import build_default_factor_definitions, factor_definitions_to_dataframe
from .trend_factor import build_trend_factor_scores
from .momentum_factor import build_momentum_factor_scores
from .volatility_factor import build_volatility_factor_scores
from .carry_proxy_factor import build_carry_proxy_factor_scores
from .value_proxy_factor import build_value_proxy_factor_scores
from .macro_sensitivity_factors import build_macro_sensitivity_factor_scores
from .factor_scoring import build_factor_score_table
from .factor_ranking import build_factor_rank_table, build_composite_factor_ranking, summarize_factor_ranking
from .factor_backtest import calculate_forward_returns, build_factor_bucket_forward_returns, calculate_top_bottom_spread, build_factor_backtest_results, summarize_factor_backtest
from .factor_ic import calculate_factor_ic_proxy, calculate_factor_ic_summary, build_factor_ic_report
from .factor_stability import build_factor_stability_report
from .factor_exposure import build_factor_exposure_table, summarize_factor_exposure
from .factor_neutralization import build_factor_neutral_basket
from .factor_quality import build_factor_quality_report
from .factor_report_builder import build_factor_research_markdown_report

logger = logging.getLogger(__name__)

class FactorResearchPipeline:
    def __init__(self, data_lake: DataLake, settings: Settings, profile: FactorResearchProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_factor_research_profile()
        self.data_adapter = FactorDataAdapter(data_lake)

    def _prepare_data(self, specs: list[SymbolSpec], timeframe: str):
        valid_specs, uni_summary = build_factor_universe(specs, self.profile.min_symbols)
        metadata_df = build_factor_metadata_table(valid_specs)
        close_df, close_summary = self.data_adapter.load_close_prices(valid_specs, timeframe)
        returns_df, ret_summary = self.data_adapter.build_returns_matrix(close_df, self.profile.return_method)
        synthetic_indices, syn_summary = self.data_adapter.load_synthetic_indices(timeframe)
        return valid_specs, metadata_df, close_df, returns_df, synthetic_indices

    def build_factor_research_report(self, specs: list[SymbolSpec], timeframe: str = "1d", profile: FactorResearchProfile | None = None, limit: int | None = None, save: bool = True) -> tuple[dict, dict]:
        prof = profile or self.profile
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        valid_specs, metadata_df, close_df, returns_df, synthetic_indices = self._prepare_data(specs, timeframe)

        if len(valid_specs) < prof.min_symbols:
            return {}, {"warnings": ["Insufficient symbols for factor research"]}

        defs = build_default_factor_definitions(prof)
        defs_df = factor_definitions_to_dataframe(defs)

        scores = {}
        trend_s, _ = build_trend_factor_scores(close_df, prof)
        mom_s, _ = build_momentum_factor_scores(returns_df, prof)
        vol_s, _ = build_volatility_factor_scores(returns_df, prof)
        carry_s, _ = build_carry_proxy_factor_scores(metadata_df, close_df, returns_df, prof)
        val_s, _ = build_value_proxy_factor_scores(close_df, synthetic_indices, prof)
        macro_s, _ = build_macro_sensitivity_factor_scores(returns_df, prof)

        scores.update(trend_s)
        scores.update(mom_s)
        scores.update(vol_s)
        scores.update(carry_s)
        scores.update(val_s)
        scores.update(macro_s)

        score_df = build_factor_score_table(scores, timeframe, timestamp, defs, prof)
        rank_df = build_factor_rank_table(score_df, prof)
        comp_rank_df = build_composite_factor_ranking(score_df, prof)

        fwd_returns = calculate_forward_returns(returns_df, prof.forward_return_horizon)
        bucket_returns = build_factor_bucket_forward_returns(score_df, fwd_returns, prof)
        spread_df = calculate_top_bottom_spread(bucket_returns)
        backtest_df = build_factor_backtest_results(bucket_returns, spread_df, prof)

        # Proxies
        ic_df = pd.DataFrame() # calculate_factor_ic_proxy(score_df, fwd_returns)
        exp_df = build_factor_exposure_table(score_df)
        neutral_basket = build_factor_neutral_basket(score_df, timeframe, prof)

        summary = {
            "timeframe": timeframe,
            "timestamp": timestamp,
            "profile": prof.name,
            "universe_coverage": {"valid_symbols": len(valid_specs)},
            "ranking_summary": summarize_factor_ranking(comp_rank_df),
            "backtest_summary": summarize_factor_backtest(backtest_df)
        }

        quality = build_factor_quality_report(summary, defs, score_df, rank_df, backtest_df)

        tables = {
            "composite_ranking": comp_rank_df,
            "backtest_results": backtest_df
        }

        md_report = build_factor_research_markdown_report(summary, tables, prof)

        if save and self.settings.factor_research_save_reports:
             self.data_lake.save_factor_definitions(timeframe, prof.name, defs_df)
             self.data_lake.save_factor_score_table(timeframe, prof.name, score_df)
             self.data_lake.save_factor_rank_table(timeframe, prof.name, rank_df)
             self.data_lake.save_factor_bucket_returns(timeframe, prof.name, bucket_returns)
             self.data_lake.save_factor_backtest_results(timeframe, prof.name, backtest_df)
             self.data_lake.save_factor_exposure_table(timeframe, prof.name, exp_df)
             from .factor_models import factor_neutral_basket_to_dict
             self.data_lake.save_factor_neutral_basket(timeframe, prof.name, factor_neutral_basket_to_dict(neutral_basket))
             self.data_lake.save_factor_quality(timeframe, prof.name, quality)
             self.data_lake.save_factor_research_report(timeframe, prof.name, summary, md_report)

        return summary, {"warnings": quality["warnings"]}

    def build_factor_score_report(self, specs: list[SymbolSpec], timeframe: str = "1d", profile: FactorResearchProfile | None = None, limit: int | None = None, save: bool = True) -> tuple[pd.DataFrame, dict]:
        return pd.DataFrame(), {"warnings": []}

    def build_factor_backtest_report(self, specs: list[SymbolSpec], timeframe: str = "1d", profile: FactorResearchProfile | None = None, limit: int | None = None, save: bool = True) -> tuple[pd.DataFrame, dict]:
        return pd.DataFrame(), {"warnings": []}

    def build_factor_exposure_report(self, specs: list[SymbolSpec], timeframe: str = "1d", profile: FactorResearchProfile | None = None, limit: int | None = None, save: bool = True) -> tuple[pd.DataFrame, dict]:
        return pd.DataFrame(), {"warnings": []}

    def build_factor_neutral_report(self, specs: list[SymbolSpec], timeframe: str = "1d", profile: FactorResearchProfile | None = None, limit: int | None = None, save: bool = True) -> tuple[dict, dict]:
        return {}, {"warnings": []}
