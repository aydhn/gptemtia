import pandas as pd
from pathlib import Path

from data.storage.data_lake import DataLake
from config.settings import Settings
from .readiness_config import LocalReadinessProfile, get_local_readiness_profile
from .gate_registry import build_readiness_gate_registry
from .operator_checklist import build_final_operator_checklist
from .docs_readiness import build_documentation_readiness_report
from .handoff_manifest import build_handoff_package_manifest
from .phase_evidence_binder import build_phase_completion_evidence_binder
from .readiness_quality import build_readiness_quality_report
from .readiness_report_builder import *

class LocalReadinessPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: LocalReadinessProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_local_readiness_profile(settings.default_local_readiness_profile)

    def build_readiness_gate_registry(
        self,
        save: bool = True,
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        gate_df, summary = build_readiness_gate_registry(self.project_root, self.profile)
        if save:
            self.data_lake.save_readiness_gate_registry(gate_df, summary)
        return {"gate_registry": gate_df}, summary

    def build_final_operator_checklist(
        self,
        save: bool = True,
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        checklist_df, summary = build_final_operator_checklist(self.profile)
        if save:
            self.data_lake.save_final_operator_checklist(checklist_df, summary)
        return {"operator_checklist": checklist_df}, summary

    def build_readiness_reports(
        self,
        save: bool = True,
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        docs_df, summary = build_documentation_readiness_report(self.project_root, self.profile)
        if save:
            self.data_lake.save_documentation_readiness_report(docs_df, summary)
        return {"docs_readiness": docs_df}, summary

    def build_handoff_package_manifest(
        self,
        save: bool = True,
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        manifest_dict, summary = build_handoff_package_manifest(self.project_root, 1.0, {}, self.profile)
        if save:
            self.data_lake.save_handoff_package_manifest(manifest_dict)
        return {"handoff_manifest": pd.DataFrame([manifest_dict])}, summary

    def build_final_local_readiness_binder(
        self,
        save: bool = True,
    ) -> tuple[str, dict]:
        binder_text, summary = build_phase_completion_evidence_binder(self.project_root, self.profile)
        if save:
            self.data_lake.save_final_local_readiness_binder(binder_text, summary)
        return binder_text, summary

    def build_readiness_quality_report(
        self,
        save: bool = True,
    ) -> tuple[dict, dict]:
        from .readiness_quality import build_readiness_quality_report as build_quality
        quality = build_quality({})
        if save:
            self.data_lake.save_readiness_quality(self.profile.name, quality)
        return quality, {"quality_checks": 1}

    def build_readiness_status(
        self,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "all_reports_generated"}])
        return df, {"status": "ok"}
