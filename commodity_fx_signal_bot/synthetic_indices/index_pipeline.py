import logging
import datetime
import pandas as pd
from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from synthetic_indices.index_config import SyntheticIndexProfile, get_default_synthetic_index_profile, get_synthetic_index_profile
from synthetic_indices.composite_index_builder import CompositeIndexBuilder
from synthetic_indices.benchmark_definitions import build_default_synthetic_benchmark_definitions, build_commodity_composite_definition
from synthetic_indices.index_performance import build_index_performance_table, summarize_index_performance
from synthetic_indices.relative_strength import build_relative_strength_report
from synthetic_indices.relative_momentum import build_relative_momentum_report
from synthetic_indices.rotation_research import build_universe_rotation_report
from synthetic_indices.leadership_laggard import build_leadership_laggard_report
from synthetic_indices.benchmark_comparison import build_benchmark_comparison_report
from synthetic_indices.index_quality import build_synthetic_index_quality_report
from synthetic_indices.index_report_builder import (
    build_synthetic_benchmark_markdown_report,
    build_composite_index_markdown_report,
    build_relative_strength_markdown_report,
    build_universe_rotation_markdown_report,
    build_leadership_laggard_markdown_report
)

logger = logging.getLogger(__name__)

class SyntheticIndexPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: SyntheticIndexProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_synthetic_index_profile()
        self.builder = CompositeIndexBuilder(self.data_lake)

    def _prepare_data(self, specs: list[SymbolSpec], timeframe: str) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
        summary = {"warnings": []}

        close_df, close_summary = self.builder.load_close_prices(specs, timeframe)
        if close_summary.get("warnings"):
            summary["warnings"].extend(close_summary["warnings"])

        if close_df.empty:
            summary["warnings"].append("No close prices loaded.")
            return pd.DataFrame(), pd.DataFrame(), summary

        returns_df, ret_summary = self.builder.build_returns_matrix(close_df, method=self.profile.return_method)
        if ret_summary.get("warnings"):
            summary["warnings"].extend(ret_summary["warnings"])

        return close_df, returns_df, summary

    def build_synthetic_benchmark_report(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: SyntheticIndexProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> tuple[dict, dict]:

        prof = profile or self.profile
        summary = {
            "timeframe": timeframe,
            "profile": prof.name,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "warnings": []
        }

        _, returns_df, prep_summary = self._prepare_data(specs, timeframe)
        if prep_summary.get("warnings"):
            summary["warnings"].extend(prep_summary["warnings"])

        if returns_df.empty:
            summary["warnings"].append("Insufficient data.")
            return summary, {}

        if limit:
             returns_df = returns_df.iloc[-limit:]

        definitions, def_summary = build_default_synthetic_benchmark_definitions(specs, timeframe, prof)
        if def_summary.get("warnings"):
             summary["warnings"].extend(def_summary["warnings"])

        series_map, series_summary = self.builder.build_index_series_for_definitions(definitions, returns_df)
        if series_summary.get("warnings"):
             summary["warnings"].extend(series_summary["warnings"])

        comparison_df, comp_summary = build_benchmark_comparison_report(returns_df, series_map, prof)
        if comp_summary.get("warnings"):
             summary["warnings"].extend(comp_summary["warnings"])

        # Definition to DF
        from synthetic_indices.index_models import synthetic_index_definition_to_dict
        def_df = pd.DataFrame([synthetic_index_definition_to_dict(d) for d in definitions])

        quality = build_synthetic_index_quality_report(summary=summary, definitions=definitions, index_series_map=series_map, profile=prof)
        summary["quality_passed"] = quality["passed"]

        tables = {"Benchmark Definitions": def_df, "Benchmark Comparison": comparison_df}

        if save and self.settings.synthetic_indices_enabled:
            self.data_lake.save_synthetic_index_definitions(timeframe, prof.name, def_df)
            self.data_lake.save_synthetic_benchmark_comparison(timeframe, prof.name, comparison_df)
            for s_id, s_series in series_map.items():
                self.data_lake.save_synthetic_index_levels(s_id, timeframe, s_series.level_series.to_frame(name="level"))
                self.data_lake.save_synthetic_index_returns(s_id, timeframe, s_series.return_series.to_frame(name="return"))

            md_report = build_synthetic_benchmark_markdown_report(summary, tables, prof)
            self.data_lake.save_synthetic_index_report(timeframe, prof.name, summary, md_report)
            self.data_lake.save_synthetic_index_quality(timeframe, prof.name, quality)

            # Save CSV and TXT in reports output
            if not def_df.empty:
                csv_path = self.data_lake.paths.synthetic_indices_reports_csv / f"synthetic_benchmark_definitions_{timeframe}_{prof.name}.csv"
                def_df.to_csv(csv_path, index=False)

            txt_path = self.data_lake.paths.synthetic_indices_reports_txt / f"synthetic_benchmark_{timeframe}_{prof.name}.txt"
            from reports.report_builder import build_synthetic_benchmark_text_report
            txt_content = build_synthetic_benchmark_text_report(summary, def_df)
            with open(txt_path, "w") as f:
                 f.write(txt_content)

        return summary, tables

    def build_composite_index_report(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: SyntheticIndexProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> tuple[dict, dict]:

        prof = profile or self.profile
        summary = {
            "timeframe": timeframe,
            "profile": prof.name,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "warnings": []
        }

        _, returns_df, prep_summary = self._prepare_data(specs, timeframe)
        if prep_summary.get("warnings"):
            summary["warnings"].extend(prep_summary["warnings"])

        if returns_df.empty:
            summary["warnings"].append("Insufficient data.")
            return summary, {}

        if limit:
             returns_df = returns_df.iloc[-limit:]

        definitions, _ = build_default_synthetic_benchmark_definitions(specs, timeframe, prof)
        series_map, _ = self.builder.build_index_series_for_definitions(definitions, returns_df)

        perf_df = build_index_performance_table(series_map)
        perf_summary = summarize_index_performance(perf_df)
        summary.update(perf_summary)

        quality = build_synthetic_index_quality_report(summary=summary, index_series_map=series_map, profile=prof)
        summary["quality_passed"] = quality["passed"]

        tables = {"Performance": perf_df}

        if save and self.settings.synthetic_indices_enabled:
            self.data_lake.save_synthetic_index_performance(timeframe, prof.name, perf_df)

            md_report = build_composite_index_markdown_report(summary, perf_df, prof)
            self.data_lake.save_synthetic_index_report(timeframe, f"{prof.name}_composite", summary, md_report)

            if not perf_df.empty:
                csv_path = self.data_lake.paths.synthetic_indices_reports_csv / f"composite_index_performance_{timeframe}_{prof.name}.csv"
                perf_df.to_csv(csv_path, index=False)

            txt_path = self.data_lake.paths.synthetic_indices_reports_txt / f"composite_index_report_{timeframe}_{prof.name}.txt"
            from reports.report_builder import build_composite_index_text_report
            txt_content = build_composite_index_text_report(summary, perf_df)
            with open(txt_path, "w") as f:
                 f.write(txt_content)

        return summary, tables

    def build_relative_strength_report(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: SyntheticIndexProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        prof = profile or self.profile
        summary = {
            "timeframe": timeframe,
            "profile": prof.name,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "warnings": []
        }

        _, returns_df, prep_summary = self._prepare_data(specs, timeframe)
        if prep_summary.get("warnings"):
            summary["warnings"].extend(prep_summary["warnings"])

        if returns_df.empty:
            summary["warnings"].append("Insufficient data.")
            return pd.DataFrame(), summary

        if limit:
             returns_df = returns_df.iloc[-limit:]

        # Need a benchmark for RS. We'll build a commodity composite dynamically.
        bench_def = build_commodity_composite_definition(specs, timeframe, prof)
        bench_series, bench_summary = self.builder.build_index_series(bench_def, returns_df)
        if bench_summary.get("warnings"):
             summary["warnings"].extend(bench_summary["warnings"])

        rs_df, rs_summary = build_relative_strength_report(returns_df, bench_series.return_series, prof)
        if rs_summary.get("warnings"):
             summary["warnings"].extend(rs_summary["warnings"])

        summary["symbols_processed"] = rs_summary.get("symbols_processed", 0)

        quality = build_synthetic_index_quality_report(summary=summary, rs_df=rs_df, profile=prof)
        summary["quality_passed"] = quality["passed"]

        if save and self.settings.synthetic_indices_enabled:
            self.data_lake.save_relative_strength_table(timeframe, prof.name, rs_df)

            md_report = build_relative_strength_markdown_report(summary, rs_df, prof)
            self.data_lake.save_synthetic_index_report(timeframe, f"{prof.name}_relative_strength", summary, md_report)

            if not rs_df.empty:
                csv_path = self.data_lake.paths.synthetic_indices_reports_csv / f"relative_strength_{timeframe}_{prof.name}.csv"
                rs_df.to_csv(csv_path, index=False)

            txt_path = self.data_lake.paths.synthetic_indices_reports_txt / f"relative_strength_report_{timeframe}_{prof.name}.txt"
            from reports.report_builder import build_relative_strength_text_report
            txt_content = build_relative_strength_text_report(summary, rs_df)
            with open(txt_path, "w") as f:
                 f.write(txt_content)

        return rs_df, summary

    def build_universe_rotation_report(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: SyntheticIndexProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        prof = profile or self.profile
        summary = {
            "timeframe": timeframe,
            "profile": prof.name,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "warnings": []
        }

        _, returns_df, prep_summary = self._prepare_data(specs, timeframe)
        if prep_summary.get("warnings"):
            summary["warnings"].extend(prep_summary["warnings"])

        if returns_df.empty:
            summary["warnings"].append("Insufficient data.")
            return pd.DataFrame(), summary

        if limit:
             returns_df = returns_df.iloc[-limit:]

        prev_df = None # Load from lake if we want rank delta
        try:
             prev_df = self.data_lake.load_universe_rotation_table(timeframe, prof.name)
        except Exception:
             pass

        rot_df, rot_summary = build_universe_rotation_report(returns_df, prev_df, timeframe, prof)
        if rot_summary.get("warnings"):
             summary["warnings"].extend(rot_summary["warnings"])

        for k in ["stability_score", "avg_rank_delta", "turnover_proxy", "symbols_processed"]:
             if k in rot_summary:
                  summary[k] = rot_summary[k]

        quality = build_synthetic_index_quality_report(summary=summary, rotation_df=rot_df, profile=prof)
        summary["quality_passed"] = quality["passed"]

        if save and self.settings.synthetic_indices_enabled:
            self.data_lake.save_universe_rotation_table(timeframe, prof.name, rot_df)

            md_report = build_universe_rotation_markdown_report(summary, rot_df, prof)
            self.data_lake.save_synthetic_index_report(timeframe, f"{prof.name}_rotation", summary, md_report)

            if not rot_df.empty:
                csv_path = self.data_lake.paths.synthetic_indices_reports_csv / f"universe_rotation_{timeframe}_{prof.name}.csv"
                rot_df.to_csv(csv_path, index=False)

            txt_path = self.data_lake.paths.synthetic_indices_reports_txt / f"universe_rotation_report_{timeframe}_{prof.name}.txt"
            from reports.report_builder import build_universe_rotation_text_report
            txt_content = build_universe_rotation_text_report(summary, rot_df)
            with open(txt_path, "w") as f:
                 f.write(txt_content)

        return rot_df, summary

    def build_leadership_laggard_report(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: SyntheticIndexProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        prof = profile or self.profile
        summary = {
            "timeframe": timeframe,
            "profile": prof.name,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "warnings": []
        }

        _, returns_df, prep_summary = self._prepare_data(specs, timeframe)
        if prep_summary.get("warnings"):
            summary["warnings"].extend(prep_summary["warnings"])

        if returns_df.empty:
            summary["warnings"].append("Insufficient data.")
            return pd.DataFrame(), summary

        if limit:
             returns_df = returns_df.iloc[-limit:]

        bench_def = build_commodity_composite_definition(specs, timeframe, prof)
        bench_series, _ = self.builder.build_index_series(bench_def, returns_df)

        rs_df, _ = build_relative_strength_report(returns_df, bench_series.return_series, prof)
        mom_df, _ = build_relative_momentum_report(returns_df, prof)

        rot_df = None
        try:
             rot_df = self.data_lake.load_universe_rotation_table(timeframe, prof.name)
        except Exception:
             pass

        leader_df, lead_summary = build_leadership_laggard_report(rs_df, mom_df, rot_df, prof)
        if lead_summary.get("warnings"):
             summary["warnings"].extend(lead_summary["warnings"])

        for k in ["total_symbols", "leaders", "laggards"]:
             if k in lead_summary:
                  summary[k] = lead_summary[k]

        quality = build_synthetic_index_quality_report(summary=summary, rs_df=rs_df, rotation_df=rot_df, profile=prof)
        summary["quality_passed"] = quality["passed"]

        if save and self.settings.synthetic_indices_enabled:
            self.data_lake.save_leadership_laggard_table(timeframe, prof.name, leader_df)

            md_report = build_leadership_laggard_markdown_report(summary, leader_df, prof)
            self.data_lake.save_synthetic_index_report(timeframe, f"{prof.name}_leadership", summary, md_report)

            if not leader_df.empty:
                csv_path = self.data_lake.paths.synthetic_indices_reports_csv / f"leadership_laggard_{timeframe}_{prof.name}.csv"
                leader_df.to_csv(csv_path, index=False)

            txt_path = self.data_lake.paths.synthetic_indices_reports_txt / f"leadership_laggard_report_{timeframe}_{prof.name}.txt"
            from reports.report_builder import build_leadership_laggard_text_report
            txt_content = build_leadership_laggard_text_report(summary, leader_df)
            with open(txt_path, "w") as f:
                 f.write(txt_content)

        return leader_df, summary
