import pandas as pd
from datetime import datetime, timezone
from pathlib import Path
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from config.settings import Settings
from research_reports.research_config import ResearchReportProfile, get_default_research_report_profile
from research_reports.data_collector import ResearchDataCollector
from research_reports.symbol_summary import build_symbol_research_snapshot
from research_reports.narrative_builder import build_symbol_narrative, build_universe_narrative
from research_reports.ranking_builder import build_ranking_summary
from research_reports.ranking_builder import build_symbol_ranking_table
from research_reports.markdown_renderer import render_symbol_report_markdown, render_universe_report_markdown, render_daily_digest_markdown
from research_reports.research_models import ResearchReport, build_research_report_id, symbol_research_snapshot_to_dict
from research_reports.report_quality import build_research_quality_report
from research_reports.csv_exporter import export_ranking_table, export_symbol_summary_table
from config.paths import (
    REPORTS_RESEARCH_REPORTS_MARKDOWN_DIR,
    REPORTS_RESEARCH_REPORTS_CSV_DIR,
    REPORTS_RESEARCH_REPORTS_TXT_DIR
)

class ResearchReportPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: ResearchReportProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_research_report_profile()
        self.collector = ResearchDataCollector(data_lake)

    def build_symbol_report(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: ResearchReportProfile | None = None,
        save: bool = True,
    ) -> tuple[ResearchReport, dict]:

        prof = profile or self.profile
        inputs, metadata = self.collector.collect_symbol_inputs(spec, timeframe)
        snapshot = build_symbol_research_snapshot(spec, timeframe, inputs, metadata, prof)
        narrative = build_symbol_narrative(snapshot, prof)

        # We don't have complex tables implemented yet, so pass empty dict
        tables = {}

        markdown = render_symbol_report_markdown(snapshot, narrative, tables)

        report_id = build_research_report_id("symbol_research", prof.name, timeframe, [spec.symbol])

        report = ResearchReport(
            report_id=report_id,
            report_type="symbol_research",
            title=f"{spec.symbol} Research Report",
            profile_name=prof.name,
            timeframe=timeframe,
            symbols=[spec.symbol],
            created_at_utc=datetime.now(timezone.utc).isoformat(),
            markdown=markdown,
            tables=tables,
            summary=symbol_research_snapshot_to_dict(snapshot),
            warnings=snapshot.warnings
        )

        quality = build_research_quality_report(report, snapshots=[snapshot])

        if save:
            self.data_lake.save_symbol_research_report(spec.symbol, timeframe, prof.name, report.summary, markdown)
            self.data_lake.save_research_quality(report_id, quality)

            # Save markdown
            md_path = REPORTS_RESEARCH_REPORTS_MARKDOWN_DIR / f"symbol_research_{spec.symbol}_{timeframe}_{prof.name}.md"
            md_path.write_text(markdown, encoding='utf-8')

            # Save txt
            txt_path = REPORTS_RESEARCH_REPORTS_TXT_DIR / f"symbol_research_{spec.symbol}_{timeframe}_{prof.name}.txt"
            txt_path.write_text(markdown, encoding='utf-8') # Just saving md as txt for simplicity

        return report, quality

    def build_universe_report(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: ResearchReportProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> tuple[ResearchReport, dict]:

        prof = profile or self.profile
        universe_inputs, metadata = self.collector.collect_universe_inputs(specs, timeframe, limit)

        snapshots = []
        for sym, data in universe_inputs.items():
            spec = next((s for s in specs if s.symbol == sym), None)
            if spec:
                snapshots.append(build_symbol_research_snapshot(spec, timeframe, data['inputs'], data['metadata'], prof))

        ranking_df = build_symbol_ranking_table(snapshots, prof)
        ranking_summary = build_ranking_summary(ranking_df)
        narrative = build_universe_narrative(ranking_summary)

        markdown = render_universe_report_markdown(ranking_df, narrative, prof)

        symbols = [s.symbol for s in snapshots]
        report_id = build_research_report_id("universe_research", prof.name, timeframe, symbols)

        tables = {"ranking": ranking_df}

        report = ResearchReport(
            report_id=report_id,
            report_type="universe_research",
            title="Universe Research Report",
            profile_name=prof.name,
            timeframe=timeframe,
            symbols=symbols,
            created_at_utc=datetime.now(timezone.utc).isoformat(),
            markdown=markdown,
            tables=tables,
            summary=ranking_summary,
            warnings=metadata.get('warnings', [])
        )

        quality = build_research_quality_report(report, snapshots=snapshots, ranking_df=ranking_df)

        if save:
            self.data_lake.save_universe_research_report(timeframe, prof.name, report.summary, markdown)
            self.data_lake.save_research_ranking_table(timeframe, prof.name, ranking_df)
            self.data_lake.save_research_quality(report_id, quality)

            md_path = REPORTS_RESEARCH_REPORTS_MARKDOWN_DIR / f"universe_research_{timeframe}_{prof.name}.md"
            md_path.write_text(markdown, encoding='utf-8')

            csv_path = REPORTS_RESEARCH_REPORTS_CSV_DIR / f"universe_ranking_{timeframe}_{prof.name}.csv"
            export_ranking_table(ranking_df, csv_path)

        return report, quality

    def build_daily_digest(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: ResearchReportProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> tuple[ResearchReport, dict]:

        prof = profile or self.profile
        universe_inputs, metadata = self.collector.collect_universe_inputs(specs, timeframe, limit)

        snapshots = []
        for sym, data in universe_inputs.items():
            spec = next((s for s in specs if s.symbol == sym), None)
            if spec:
                snapshots.append(build_symbol_research_snapshot(spec, timeframe, data['inputs'], data['metadata'], prof))

        ranking_df = build_symbol_ranking_table(snapshots, prof)

        markdown = render_daily_digest_markdown(snapshots, ranking_df, prof)

        symbols = [s.symbol for s in snapshots]
        report_id = build_research_report_id("daily_digest", prof.name, timeframe, symbols)

        report = ResearchReport(
            report_id=report_id,
            report_type="daily_digest",
            title="Daily Research Digest",
            profile_name=prof.name,
            timeframe=timeframe,
            symbols=symbols,
            created_at_utc=datetime.now(timezone.utc).isoformat(),
            markdown=markdown,
            tables={"ranking": ranking_df},
            summary={"processed_count": len(snapshots)},
            warnings=metadata.get('warnings', [])
        )

        quality = build_research_quality_report(report, snapshots=snapshots, ranking_df=ranking_df)

        if save:
            self.data_lake.save_daily_research_digest(timeframe, prof.name, report.summary, markdown)
            self.data_lake.save_research_quality(report_id, quality)

            md_path = REPORTS_RESEARCH_REPORTS_MARKDOWN_DIR / f"daily_research_digest_{timeframe}_{prof.name}.md"
            md_path.write_text(markdown, encoding='utf-8')

            txt_path = REPORTS_RESEARCH_REPORTS_TXT_DIR / f"daily_research_digest_{timeframe}_{prof.name}.txt"
            txt_path.write_text(markdown, encoding='utf-8')

        return report, quality
