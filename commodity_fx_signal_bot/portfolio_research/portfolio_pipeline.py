import logging
from datetime import datetime, timezone
import pandas as pd
from data.storage.data_lake import DataLake
from config.settings import Settings
from config.symbols import SymbolSpec

from portfolio_research.portfolio_config import PortfolioResearchProfile, get_default_portfolio_research_profile
from portfolio_research.portfolio_models import PortfolioResearchReport, build_portfolio_report_id, virtual_basket_definition_to_dict, virtual_basket_performance_to_dict
from portfolio_research.universe_returns import UniverseReturnsBuilder
from portfolio_research.correlation_analysis import build_correlation_report
from portfolio_research.diversification import build_diversification_table
from portfolio_research.exposure_analysis import build_cross_asset_exposure_report
from portfolio_research.basket_definitions import build_default_virtual_baskets
from portfolio_research.basket_performance import build_basket_performance_table
from portfolio_research.basket_tracking import build_basket_tracking_report
from portfolio_research.allocation_research import build_allocation_research_report
from portfolio_research.portfolio_quality import build_portfolio_quality_report
from portfolio_research.portfolio_report_builder import build_portfolio_markdown_report

logger = logging.getLogger(__name__)

class PortfolioResearchPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: PortfolioResearchProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_portfolio_research_profile()

    def build_portfolio_research(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: PortfolioResearchProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> tuple[PortfolioResearchReport, dict]:
        p = profile or self.profile
        logger.info(f"Starting portfolio research pipeline for {len(specs)} symbols. Profile: {p.name}")

        warnings = []

        builder = UniverseReturnsBuilder(self.data_lake)
        close_df, info = builder.load_close_prices(specs, timeframe)
        if close_df.empty:
            logger.warning("No close prices found.")
            return PortfolioResearchReport("", p.name, timeframe, [], "", {}, {}, "", ["No close prices found"]), {"warnings": ["No close prices found"], "quality": {"passed": False}}

        returns_df, ret_info = builder.build_returns_matrix(close_df, method=p.return_method)
        aligned_df, align_info = builder.align_universe_returns(returns_df, min_observations=p.min_observations)

        warnings.extend(info.get("warnings", []))
        warnings.extend(ret_info.get("warnings", []))
        warnings.extend(align_info.get("warnings", []))

        if len(aligned_df.columns) < p.min_symbols:
            msg = f"Insufficient symbols after alignment ({len(aligned_df.columns)} < {p.min_symbols})"
            logger.warning(msg)
            warnings.append(msg)
            return PortfolioResearchReport("", p.name, timeframe, [], "", {}, {}, "", warnings), {"warnings": warnings, "quality": {"passed": False}}

        symbols = list(aligned_df.columns)

        corr_tables, corr_summary = build_correlation_report(aligned_df, p)

        ranking_df = pd.DataFrame()

        baskets, basket_info = build_default_virtual_baskets(symbols, ranking_df, timeframe, p)
        warnings.extend(basket_info.get("warnings", []))

        perf_df = build_basket_performance_table(baskets, aligned_df, corr_tables.get("correlation_matrix"))

        alloc_df, alloc_summary = build_allocation_research_report(baskets, corr_tables.get("correlation_matrix"), specs, p)
        div_df = build_diversification_table(baskets, corr_tables.get("correlation_matrix"))

        summary = {
            "timeframe": timeframe,
            "symbol_count": len(symbols),
            "basket_count": len(baskets),
            "created_at_utc": datetime.now(timezone.utc).isoformat(),
            "warnings": warnings,
            "correlation_summary": corr_summary,
            "allocation_summary": alloc_summary
        }

        quality = build_portfolio_quality_report(summary, aligned_df, corr_tables.get("correlation_matrix"), baskets, perf_df)

        tables = {
            "correlation_matrix": corr_tables.get("correlation_matrix"),
            "pairwise_correlation": corr_tables.get("pairwise_correlation"),
            "virtual_baskets": pd.DataFrame([virtual_basket_definition_to_dict(b) for b in baskets]),
            "basket_performance": perf_df,
            "allocation": alloc_df,
            "diversification": div_df
        }

        report_id = build_portfolio_report_id(p.name, timeframe, symbols)
        md = build_portfolio_markdown_report(summary, tables, p)

        report = PortfolioResearchReport(
            report_id=report_id,
            profile_name=p.name,
            timeframe=timeframe,
            symbols=symbols,
            created_at_utc=summary["created_at_utc"],
            portfolio_summary=summary,
            tables=tables,
            markdown=md,
            warnings=warnings
        )

        if save and self.settings.portfolio_research_save_reports:
            if hasattr(self.data_lake, 'save_portfolio_research_report'):
                self.data_lake.save_portfolio_research_report(timeframe, p.name, {
                    "report_id": report.report_id,
                    "summary": summary
                }, md)

            if hasattr(self.data_lake, 'save_correlation_matrix') and tables["correlation_matrix"] is not None:
                self.data_lake.save_correlation_matrix(timeframe, p.name, tables["correlation_matrix"])

            if hasattr(self.data_lake, 'save_virtual_basket_performance') and not tables["basket_performance"].empty:
                self.data_lake.save_virtual_basket_performance(timeframe, p.name, tables["basket_performance"])

        return report, {"quality": quality, "warnings": warnings}

    def build_correlation_report(self, specs, timeframe="1d", profile=None, limit=None, save=True):
        return {}, {"warnings": ["Not implemented directly in this snippet, run build_portfolio_research"]}

    def build_virtual_basket_report(self, specs, timeframe="1d", profile=None, limit=None, save=True):
         return {}, {"warnings": ["Not implemented directly in this snippet, run build_portfolio_research"]}

    def build_basket_tracking_report(self, specs, timeframe="1d", profile=None, limit=None, save=True):
         return pd.DataFrame(), {"warnings": ["Not implemented directly in this snippet"]}
