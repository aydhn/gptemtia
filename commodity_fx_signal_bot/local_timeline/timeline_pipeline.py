"""
Local timeline pipeline orchestrator.
"""

from pathlib import Path
import pandas as pd

from data.storage.data_lake import DataLake
from config.settings import Settings
from local_timeline.timeline_config import LocalTimelineProfile, get_default_local_timeline_profile
from local_timeline.event_registry import build_project_event_registry
from local_timeline.phase_chronology import infer_phase_titles_from_phase_log, map_events_to_phases, build_phase_chronology_registry, build_phase_event_digest
from local_timeline.artifact_evolution import build_artifact_evolution_registry
from local_timeline.file_timeline import build_file_modification_timeline, summarize_file_timeline
from local_timeline.report_timeline import build_report_generation_timeline, summarize_report_generation_timeline
from local_timeline.datalake_timeline import build_datalake_artifact_timeline, summarize_datalake_timeline
from local_timeline.documentation_timeline import build_documentation_evolution_timeline, summarize_documentation_timeline
from local_timeline.command_timeline import build_command_script_evolution_timeline, summarize_command_script_timeline
from local_timeline.evidence_timeline import build_evidence_timeline, summarize_evidence_timeline
from local_timeline.metadata_timeline import build_metadata_card_timeline, summarize_metadata_timeline
from local_timeline.graph_timeline import build_knowledge_graph_evolution_timeline, summarize_graph_timeline
from local_timeline.scenario_regression_timeline import build_scenario_regression_event_timeline, summarize_scenario_regression_timeline
from local_timeline.quality_safety_timeline import build_quality_safety_event_timeline, summarize_quality_safety_timeline
from local_timeline.backup_packaging_secrets_timeline import build_backup_packaging_secrets_event_timeline, summarize_backup_packaging_secrets_timeline
from local_timeline.temporal_lineage import build_artifact_temporal_lineage
from local_timeline.event_clustering import build_module_event_cluster_report
from local_timeline.freshness_analysis import build_event_freshness_report, build_stale_artifact_timeline_report
from local_timeline.event_gap_detection import build_event_gap_report
from local_timeline.change_digest import build_change_history_digest
from local_timeline.timeline_query import parse_timeline_query, execute_timeline_query
from local_timeline.timeline_validation import build_timeline_validation_report
from local_timeline.timeline_quality import build_timeline_quality_report
from local_timeline.timeline_export import build_timeline_export_manifest, export_timeline_to_json, export_timeline_to_csv
from local_timeline.timeline_report_builder import (
    build_project_event_registry_markdown_report,
    build_phase_chronology_markdown_report,
    build_artifact_evolution_markdown_report,
    build_change_history_digest_markdown_report,
    build_timeline_query_markdown_report,
    build_timeline_quality_markdown_report,
    build_timeline_status_markdown_report
)

class LocalTimelinePipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: LocalTimelineProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_local_timeline_profile()

    def build_project_event_registry(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        event_df, summary = build_project_event_registry(self.project_root, self.profile)
        if save:
            self.data_lake.save_project_event_registry(event_df, summary)

            md_text = build_project_event_registry_markdown_report(summary, event_df)
            from config.paths import REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR, REPORTS_LOCAL_TIMELINE_TXT_DIR
            REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
            REPORTS_LOCAL_TIMELINE_TXT_DIR.mkdir(parents=True, exist_ok=True)
            with open(REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR / "project_event_registry_report.md", "w") as f:
                f.write(md_text)
            with open(REPORTS_LOCAL_TIMELINE_TXT_DIR / "project_event_registry_report.txt", "w") as f:
                f.write(md_text)

        return event_df, summary

    def build_phase_chronology_report(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        event_df, _ = build_project_event_registry(self.project_root, self.profile)
        phase_log_df = infer_phase_titles_from_phase_log(self.project_root)
        mapped_df = map_events_to_phases(event_df, phase_log_df)
        phase_df, summary = build_phase_chronology_registry(mapped_df, self.profile)
        digest_txt, digest_sum = build_phase_event_digest(mapped_df, phase_df, self.profile)

        tables = {
            "phase_chronology_registry": phase_df,
            "phase_event_map": mapped_df
        }

        if save:
            self.data_lake.save_phase_chronology_registry(phase_df, summary)
            self.data_lake.save_phase_event_digest(digest_txt, digest_sum)

            md_text = build_phase_chronology_markdown_report(summary, phase_df)
            from config.paths import REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR, REPORTS_LOCAL_TIMELINE_TXT_DIR, REPORTS_LOCAL_TIMELINE_CSV_DIR
            REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
            REPORTS_LOCAL_TIMELINE_TXT_DIR.mkdir(parents=True, exist_ok=True)
            REPORTS_LOCAL_TIMELINE_CSV_DIR.mkdir(parents=True, exist_ok=True)

            mapped_df.to_csv(REPORTS_LOCAL_TIMELINE_CSV_DIR / "phase_event_map.csv", index=False)

            with open(REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR / "phase_chronology_report.md", "w") as f:
                f.write(md_text)
            with open(REPORTS_LOCAL_TIMELINE_TXT_DIR / "phase_event_digest.txt", "w") as f:
                f.write(digest_txt)
            with open(REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR / "phase_event_digest.md", "w") as f:
                f.write(digest_txt)

        return tables, summary

    def build_artifact_evolution_timeline(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        event_df, _ = build_project_event_registry(self.project_root, self.profile)
        evo_df, summary = build_artifact_evolution_registry(event_df, self.profile)

        # Sub timelines
        file_df, _ = build_file_modification_timeline(self.project_root, self.profile)
        rep_df, _ = build_report_generation_timeline(self.project_root, self.profile)
        lake_df, _ = build_datalake_artifact_timeline(self.project_root, self.profile)
        doc_df, _ = build_documentation_evolution_timeline(self.project_root, self.profile)
        cmd_df, _ = build_command_script_evolution_timeline(self.project_root, self.profile)
        evd_df, _ = build_evidence_timeline(self.project_root, self.profile)
        meta_df, _ = build_metadata_card_timeline(self.project_root, self.profile)
        graph_df, _ = build_knowledge_graph_evolution_timeline(self.project_root, self.profile)
        scen_df, _ = build_scenario_regression_event_timeline(self.project_root, self.profile)
        qs_df, _ = build_quality_safety_event_timeline(self.project_root, self.profile)
        sec_df, _ = build_backup_packaging_secrets_event_timeline(self.project_root, self.profile)

        lin_df, _ = build_artifact_temporal_lineage(event_df, evo_df, self.profile)
        fresh_df, _ = build_event_freshness_report(event_df, self.profile)
        stale_df, _ = build_stale_artifact_timeline_report(evo_df, self.profile)

        tables = {
            "artifact_evolution_registry": evo_df,
            "file_modification_timeline": file_df,
            "report_generation_timeline": rep_df,
            "datalake_artifact_timeline": lake_df,
            "documentation_evolution_timeline": doc_df,
            "command_script_evolution_timeline": cmd_df,
            "evidence_timeline": evd_df,
            "metadata_card_timeline": meta_df,
            "knowledge_graph_evolution_timeline": graph_df,
            "scenario_regression_event_timeline": scen_df,
            "quality_safety_event_timeline": qs_df,
            "backup_packaging_secrets_event_timeline": sec_df,
            "artifact_temporal_lineage": lin_df,
            "event_freshness_report": fresh_df,
            "stale_artifact_timeline_report": stale_df
        }

        if save:
            self.data_lake.save_artifact_evolution_registry(evo_df)
            self.data_lake.save_file_modification_timeline(file_df)
            self.data_lake.save_report_generation_timeline(rep_df)
            self.data_lake.save_datalake_artifact_timeline(lake_df)
            self.data_lake.save_documentation_evolution_timeline(doc_df)
            self.data_lake.save_command_script_evolution_timeline(cmd_df)
            self.data_lake.save_evidence_timeline(evd_df)
            self.data_lake.save_metadata_card_timeline(meta_df)
            self.data_lake.save_knowledge_graph_evolution_timeline(graph_df)
            self.data_lake.save_scenario_regression_event_timeline(scen_df)
            self.data_lake.save_quality_safety_event_timeline(qs_df)
            self.data_lake.save_backup_packaging_secrets_event_timeline(sec_df)
            self.data_lake.save_artifact_temporal_lineage(lin_df)
            self.data_lake.save_event_freshness_report(fresh_df)
            self.data_lake.save_stale_artifact_timeline_report(stale_df)

            md_text = build_artifact_evolution_markdown_report(summary, evo_df)
            from config.paths import REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR, REPORTS_LOCAL_TIMELINE_TXT_DIR
            REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
            REPORTS_LOCAL_TIMELINE_TXT_DIR.mkdir(parents=True, exist_ok=True)
            with open(REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR / "artifact_evolution_timeline_report.md", "w") as f:
                f.write(md_text)
            with open(REPORTS_LOCAL_TIMELINE_TXT_DIR / "artifact_evolution_timeline_report.txt", "w") as f:
                f.write(md_text)

        return tables, summary

    def build_change_history_digest(self, save: bool = True) -> tuple[str, dict]:
        event_df, _ = build_project_event_registry(self.project_root, self.profile)
        evo_df, _ = build_artifact_evolution_registry(event_df, self.profile)
        phase_log_df = infer_phase_titles_from_phase_log(self.project_root)
        phase_df, _ = build_phase_chronology_registry(event_df, self.profile)
        gap_df, _ = build_event_gap_report(event_df, phase_df, evo_df, self.profile)
        cluster_df, _ = build_module_event_cluster_report(event_df, self.profile)

        digest_txt, summary = build_change_history_digest(event_df, evo_df, gap_df, self.profile)

        if save:
            self.data_lake.save_change_history_digest(digest_txt, summary)
            self.data_lake.save_event_gap_report(gap_df)
            self.data_lake.save_module_event_cluster_report(cluster_df)

            md_text = build_change_history_digest_markdown_report(summary, digest_txt)
            from config.paths import REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR, REPORTS_LOCAL_TIMELINE_TXT_DIR, DOCS_LOCAL_TIMELINE_DIR
            REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
            REPORTS_LOCAL_TIMELINE_TXT_DIR.mkdir(parents=True, exist_ok=True)
            DOCS_LOCAL_TIMELINE_DIR.mkdir(parents=True, exist_ok=True)

            with open(REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR / "change_history_digest.md", "w") as f:
                f.write(md_text)
            with open(REPORTS_LOCAL_TIMELINE_TXT_DIR / "change_history_digest.txt", "w") as f:
                f.write(md_text)
            with open(DOCS_LOCAL_TIMELINE_DIR / "CHANGE_HISTORY_DIGEST.md", "w") as f:
                f.write(md_text)

        return digest_txt, summary

    def build_timeline_query_report(self, query_text: str, save: bool = True) -> tuple[pd.DataFrame, dict]:
        event_df, _ = build_project_event_registry(self.project_root, self.profile)
        phase_df, _ = build_phase_chronology_registry(event_df, self.profile)
        evo_df, _ = build_artifact_evolution_registry(event_df, self.profile)

        query = parse_timeline_query(query_text, self.profile)
        results_df, summary = execute_timeline_query(query, event_df, phase_df, evo_df, self.profile)

        if save:
            self.data_lake.save_timeline_query_results("latest_query", results_df, summary)

            md_text = build_timeline_query_markdown_report(summary, results_df)
            from config.paths import REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR, REPORTS_LOCAL_TIMELINE_TXT_DIR, REPORTS_LOCAL_TIMELINE_JSON_DIR
            REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
            REPORTS_LOCAL_TIMELINE_TXT_DIR.mkdir(parents=True, exist_ok=True)
            REPORTS_LOCAL_TIMELINE_JSON_DIR.mkdir(parents=True, exist_ok=True)

            with open(REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR / "timeline_query_report.md", "w") as f:
                f.write(md_text)
            with open(REPORTS_LOCAL_TIMELINE_TXT_DIR / "timeline_query_report.txt", "w") as f:
                f.write(md_text)

            # Save to JSON
            results_df.to_json(REPORTS_LOCAL_TIMELINE_JSON_DIR / "timeline_query_results.json", orient='records', force_ascii=False, indent=4)

        return results_df, summary

    def build_timeline_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        event_df, _ = build_project_event_registry(self.project_root, self.profile)
        phase_df, _ = build_phase_chronology_registry(event_df, self.profile)
        evo_df, _ = build_artifact_evolution_registry(event_df, self.profile)
        gap_df, _ = build_event_gap_report(event_df, phase_df, evo_df, self.profile)

        tables = {
            "event_registry": event_df,
            "phase_chronology": phase_df,
            "artifact_evolution": evo_df
        }

        val_df, val_summary = build_timeline_validation_report(tables, self.profile)
        quality = build_timeline_quality_report(val_summary, event_df, phase_df, evo_df, gap_df)

        manifest = build_timeline_export_manifest(event_df, phase_df, evo_df, self.profile)

        if save:
            self.data_lake.save_timeline_validation_report(val_df, val_summary)
            self.data_lake.save_timeline_quality(self.profile.name, quality)
            self.data_lake.save_timeline_export_manifest(manifest)

            from config.paths import REPORTS_LOCAL_TIMELINE_JSON_DIR, REPORTS_LOCAL_TIMELINE_CSV_DIR, REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR, REPORTS_LOCAL_TIMELINE_TXT_DIR
            REPORTS_LOCAL_TIMELINE_JSON_DIR.mkdir(parents=True, exist_ok=True)
            REPORTS_LOCAL_TIMELINE_CSV_DIR.mkdir(parents=True, exist_ok=True)
            REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
            REPORTS_LOCAL_TIMELINE_TXT_DIR.mkdir(parents=True, exist_ok=True)

            with open(REPORTS_LOCAL_TIMELINE_JSON_DIR / "timeline_quality_report.json", "w") as f:
                import json
                json.dump(quality, f, indent=4)
            with open(REPORTS_LOCAL_TIMELINE_JSON_DIR / "timeline_export_manifest.json", "w") as f:
                json.dump(manifest, f, indent=4)

            export_timeline_to_json(event_df, phase_df, evo_df, REPORTS_LOCAL_TIMELINE_JSON_DIR / "project_timeline_export.json")
            export_timeline_to_csv(event_df, phase_df, evo_df, REPORTS_LOCAL_TIMELINE_CSV_DIR)

            md_text = build_timeline_quality_markdown_report(val_summary, quality)
            with open(REPORTS_LOCAL_TIMELINE_MARKDOWN_DIR / "timeline_quality_report.md", "w") as f:
                f.write(md_text)
            with open(REPORTS_LOCAL_TIMELINE_TXT_DIR / "timeline_quality_report.txt", "w") as f:
                f.write(md_text)

        return quality, manifest

    def build_timeline_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        status_data = []
        from config.paths import LAKE_DIR, REPORTS_DIR
        for d in [LAKE_DIR / "local_timeline", REPORTS_DIR / "output" / "local_timeline"]:
            if d.exists():
                for root, _, files in os.walk(d):
                    for f in files:
                        status_data.append({"directory": str(d.name), "file": f})

        df = pd.DataFrame(status_data)
        summary = {"total_files": len(status_data)}

        if save:
            from config.paths import REPORTS_LOCAL_TIMELINE_CSV_DIR, REPORTS_LOCAL_TIMELINE_TXT_DIR
            REPORTS_LOCAL_TIMELINE_CSV_DIR.mkdir(parents=True, exist_ok=True)
            REPORTS_LOCAL_TIMELINE_TXT_DIR.mkdir(parents=True, exist_ok=True)
            if not df.empty:
                df.to_csv(REPORTS_LOCAL_TIMELINE_CSV_DIR / "timeline_status.csv", index=False)

            md_text = build_timeline_status_markdown_report(summary, df)
            with open(REPORTS_LOCAL_TIMELINE_TXT_DIR / "timeline_status_report.txt", "w") as f:
                f.write(md_text)

        return df, summary
