import logging
from pathlib import Path
from typing import Dict, Tuple, Optional, List
from datetime import datetime, timezone
import pandas as pd
from config.settings import Settings
from data.storage.data_lake import DataLake
from report_exports.export_config import ReportExportProfile, get_default_report_export_profile
from report_exports.export_models import ReportExportArtifact, ReportArchiveRecord, build_export_artifact_id, build_archive_id
from report_exports.html_renderer import render_markdown_report_to_html, save_html_report
from report_exports.pdf_renderer import render_markdown_to_pdf, build_pdf_export_summary
from report_exports.report_archive import ReportArchive
from report_exports.report_manifest import build_report_export_manifest
from report_exports.report_comparison import compare_archive_records, build_report_comparison_table
from report_exports.report_tracking import build_symbol_tracking_table, build_universe_tracking_table, build_periodic_tracking_report
from report_exports.report_packager import ReportPackager
from report_exports.export_quality import build_report_export_quality_report
from config.paths import REPORTS_REPORT_EXPORTS_HTML_DIR, REPORTS_REPORT_EXPORTS_PDF_DIR, REPORTS_REPORT_EXPORTS_PACKAGES_DIR, LAKE_REPORT_EXPORTS_ARCHIVE_DIR

logger = logging.getLogger(__name__)

class ReportExportPipeline:
    def __init__(self, data_lake: DataLake, settings: Settings, profile: Optional[ReportExportProfile] = None):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_report_export_profile()
        self.archive = ReportArchive(LAKE_REPORT_EXPORTS_ARCHIVE_DIR)
        self.packager = ReportPackager(REPORTS_REPORT_EXPORTS_PACKAGES_DIR)

    def _get_markdown_report(self, report_id: str, report_type: str, symbol: Optional[str] = None) -> Optional[str]:
        try:
            return self.data_lake.load_research_report_markdown(report_id, report_type, symbol)
        except Exception:
            return None

    def _export_report_internal(self, report_id: str, report_type: str, symbol: Optional[str], timeframe: str, markdown_text: str, research_score: Optional[float] = None, save: bool = True) -> Tuple[Dict, Dict]:
        artifacts = []
        created_at = datetime.now(timezone.utc).isoformat()
        html_path = None
        html_status = "skipped"
        html_warnings = []
        if self.profile.include_html:
            try:
                html_text, _ = render_markdown_report_to_html(markdown_text, f"{report_type} Report", self.profile)
                if save:
                    safe_sym = symbol or "universe"
                    p = REPORTS_REPORT_EXPORTS_HTML_DIR / f"{report_type}_{safe_sym}_{timeframe}.html"
                    save_html_report(html_text, p)
                    html_path = str(p)
                html_status = "success"
            except Exception as e:
                html_status = "failed"
                html_warnings.append(str(e))
        artifacts.append(ReportExportArtifact(
            artifact_id=build_export_artifact_id(report_id, "html_export"),
            report_id=report_id, export_type="html_export", status=html_status, path=html_path, created_at_utc=created_at, file_size_bytes=Path(html_path).stat().st_size if html_path and save else None, warnings=html_warnings
        ))
        pdf_path = None
        pdf_status = "skipped"
        pdf_warnings = []
        if self.profile.include_pdf:
            safe_sym = symbol or "universe"
            p = REPORTS_REPORT_EXPORTS_PDF_DIR / f"{report_type}_{safe_sym}_{timeframe}.pdf" if save else Path(f"dummy.pdf")
            rendered_path, pdf_summary = render_markdown_to_pdf(markdown_text, p, self.profile)
            pdf_status = pdf_summary.get("status", "failed")
            if pdf_status == "success" and save:
                pdf_path = str(rendered_path)
            if pdf_summary.get("error"):
                pdf_warnings.append(pdf_summary["error"])
        artifacts.append(ReportExportArtifact(
            artifact_id=build_export_artifact_id(report_id, "pdf_export"),
            report_id=report_id, export_type="pdf_export", status=pdf_status, path=pdf_path, created_at_utc=created_at, file_size_bytes=Path(pdf_path).stat().st_size if pdf_path and save else None, warnings=pdf_warnings
        ))
        manifest = build_report_export_manifest(report_id, report_type, symbol, timeframe, self.profile.name, artifacts)
        if save and self.profile.archive_enabled:
            self.data_lake.save_report_export_manifest(report_id, manifest)
        package_dir = None
        if save and self.profile.include_csv_bundle:
            package_dir, _ = self.packager.build_package(manifest, artifacts)
        archive_record = None
        comparison_res = None
        tracking_df = pd.DataFrame()
        if self.profile.archive_enabled:
            record = ReportArchiveRecord(
                archive_id=build_archive_id(report_id, created_at), report_id=report_id, report_type=report_type, symbol=symbol, timeframe=timeframe, profile_name=self.profile.name, created_at_utc=created_at, research_score=research_score, warning_count=len(manifest.get("warnings", [])), missing_sources_count=0, markdown_path=None, html_path=html_path, pdf_path=pdf_path, csv_paths=[], quality_passed=True, metadata={}
            )
            if save:
                self.archive.add_record(record)
                self.data_lake.save_report_archive_record(record.__dict__)
            archive_record = record
            if self.profile.comparison_enabled:
                prev_record = self.archive.find_previous_report(report_type, symbol, timeframe, self.profile.name, created_at)
                comparison_res = compare_archive_records(record.__dict__, prev_record)
                if save:
                    self.data_lake.save_report_comparison(comparison_res.comparison_id, comparison_res.__dict__)
            if self.profile.periodic_tracking_enabled:
                archive_df = self.archive.load_records()
                if not archive_df.empty:
                    if symbol:
                        tracking_df = build_symbol_tracking_table(archive_df, symbol, timeframe)
                    elif report_type == "universe":
                        tracking_df = build_universe_tracking_table(archive_df, timeframe)
                    if save and not tracking_df.empty:
                        self.data_lake.save_periodic_tracking_table(timeframe, self.profile.name, tracking_df)
        quality = build_report_export_quality_report(artifacts, manifest, archive_record, comparison_res)
        if save and self.profile.enabled:
            self.data_lake.save_report_export_quality(report_id, quality)
        summary = {
            "report_id": report_id, "html_status": html_status, "pdf_status": pdf_status, "package_dir": str(package_dir) if package_dir else None, "archive_id": archive_record.archive_id if archive_record else None, "comparison_label": comparison_res.comparison_label if comparison_res else None, "quality_passed": quality["passed"]
        }
        return manifest, summary

    def export_symbol_report(self, symbol: str, timeframe: str = "1d", research_profile_name: str = "balanced_research_report", export_profile: Optional[ReportExportProfile] = None, save: bool = True) -> Tuple[Dict, Dict]:
        self.profile = export_profile or self.profile
        report_id = f"res_sym_{symbol}_{timeframe}"
        md = self._get_markdown_report(report_id, "symbol", symbol)
        if not md:
            return {}, {"status": "missing_report", "warnings": ["Research report missing."]}
        return self._export_report_internal(report_id, "symbol", symbol, timeframe, md, 0.60, save)

    def export_universe_report(self, timeframe: str = "1d", research_profile_name: str = "balanced_research_report", export_profile: Optional[ReportExportProfile] = None, save: bool = True) -> Tuple[Dict, Dict]:
        self.profile = export_profile or self.profile
        report_id = f"res_univ_{timeframe}"
        md = self._get_markdown_report(report_id, "universe")
        if not md:
            return {}, {"status": "missing_report", "warnings": ["Research report missing."]}
        return self._export_report_internal(report_id, "universe", None, timeframe, md, 0.50, save)

    def export_daily_digest(self, timeframe: str = "1d", research_profile_name: str = "balanced_research_report", export_profile: Optional[ReportExportProfile] = None, save: bool = True) -> Tuple[Dict, Dict]:
        self.profile = export_profile or self.profile
        report_id = f"res_digest_{timeframe}"
        md = self._get_markdown_report(report_id, "daily_digest")
        if not md:
            return {}, {"status": "missing_report", "warnings": ["Research report missing."]}
        return self._export_report_internal(report_id, "daily_digest", None, timeframe, md, 0.50, save)

    def build_report_comparison(self, report_type: str, symbol: Optional[str] = None, timeframe: str = "1d", profile_name: str = "balanced_research_report", save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        archive_df = self.archive.load_records()
        if archive_df.empty:
            return pd.DataFrame(), {"status": "empty_archive"}
        mask = (archive_df["report_type"] == report_type) & (archive_df["timeframe"] == timeframe)
        if symbol:
            mask = mask & (archive_df["symbol"] == symbol)
        filtered = archive_df[mask].sort_values("created_at_utc", ascending=False)
        if len(filtered) < 2:
            return pd.DataFrame(), {"status": "insufficient_history"}
        curr = filtered.iloc[0].to_dict()
        prev = filtered.iloc[1].to_dict()
        comp = compare_archive_records(curr, prev)
        df = build_report_comparison_table([comp])
        if save:
            self.data_lake.save_report_comparison_table(timeframe, profile_name, df)
        return df, {"status": "success", "comparison_label": comp.comparison_label}

    def build_periodic_tracking(self, symbols: Optional[List[str]] = None, timeframe: str = "1d", save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        archive_df = self.archive.load_records()
        df, summary = build_periodic_tracking_report(archive_df, symbols, timeframe)
        if save and not df.empty:
            self.data_lake.save_periodic_tracking_table(timeframe, self.profile.name, df)
        return df, summary
