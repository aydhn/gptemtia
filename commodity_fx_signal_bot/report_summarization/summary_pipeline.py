from pathlib import Path
import pandas as pd
from typing import Tuple

from config.settings import Settings
from data.storage.data_lake import DataLake
from report_summarization.summary_config import ReportSummaryProfile, get_default_report_summary_profile
from report_summarization.report_inventory import discover_summary_source_reports, build_report_inventory_summary
from report_summarization.finding_extractor import summarize_findings
from report_summarization.warning_extractor import summarize_warnings
from report_summarization.risk_gap_extractor import summarize_risks_and_gaps
from report_summarization.module_summaries import summarize_module_briefs
from report_summarization.digest_cards import summarize_digest_cards
from report_summarization.executive_summary import build_executive_summary
from report_summarization.analyst_brief import build_analyst_brief
from report_summarization.weekly_review_pack import build_weekly_offline_review_pack
from report_summarization.summary_quality import build_summary_quality_report
from report_summarization.summary_report_builder import (
    build_report_summary_registry_markdown_report,
    build_executive_summary_markdown_report,
    build_analyst_brief_markdown_report,
    build_weekly_review_pack_markdown_report,
    build_research_digest_markdown_report,
    build_summary_quality_markdown_report,
    build_briefing_status_markdown_report
)

class ReportSummarizationPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: ReportSummaryProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_report_summary_profile()

    def _get_dummy_dfs(self):
        inventory_df = discover_summary_source_reports(self.project_root, self.profile)
        summaries_df = pd.DataFrame()
        findings_df = pd.DataFrame()
        warnings_df = pd.DataFrame()
        risk_gap_df = pd.DataFrame()
        return inventory_df, summaries_df, findings_df, warnings_df, risk_gap_df

    def build_report_summary_registry(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        inventory_df, summaries_df, findings_df, warnings_df, risk_gap_df = self._get_dummy_dfs()

        summary = {
            "inventory": build_report_inventory_summary(inventory_df),
            "findings": summarize_findings(findings_df),
            "warnings": summarize_warnings(warnings_df),
            "risks_gaps": summarize_risks_and_gaps(risk_gap_df)
        }

        tables = {
            "inventory": inventory_df,
            "summaries": summaries_df,
            "findings": findings_df,
            "warnings": warnings_df,
            "risks_gaps": risk_gap_df
        }

        return tables, summary

    def build_executive_summary_report(self, save: bool = True) -> tuple[str, dict]:
        _, summaries_df, findings_df, warnings_df, risk_gap_df = self._get_dummy_dfs()
        text, meta = build_executive_summary(summaries_df, findings_df, warnings_df, risk_gap_df, self.profile)
        return text, meta

    def build_analyst_brief_report(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        _, summaries_df, findings_df, warnings_df, risk_gap_df = self._get_dummy_dfs()
        text, meta = build_analyst_brief(summaries_df, findings_df, warnings_df, risk_gap_df, self.profile)
        return {"focus_areas": pd.DataFrame(), "safe_tasks": pd.DataFrame()}, meta

    def build_weekly_offline_review_pack(self, save: bool = True) -> tuple[str, dict]:
        _, summaries_df, findings_df, warnings_df, risk_gap_df = self._get_dummy_dfs()
        text, meta = build_weekly_offline_review_pack(summaries_df, findings_df, warnings_df, risk_gap_df, self.profile)
        return text, meta

    def build_research_digest_report(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        return {"digest_cards": pd.DataFrame(), "symbol_cards": pd.DataFrame()}, {"total_cards": 0}

    def build_summary_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        quality = build_summary_quality_report({"status": "ok"})
        return quality, {"passed": quality.get("passed", True)}

    def build_briefing_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        return pd.DataFrame(), {"status": "ok"}
