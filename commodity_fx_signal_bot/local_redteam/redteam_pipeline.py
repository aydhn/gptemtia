from pathlib import Path
import pandas as pd

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_redteam.redteam_config import LocalRedTeamProfile
from local_redteam.redteam_domain_registry import build_redteam_domain_registry
from local_redteam.redteam_rehearsal_packet import build_final_local_redteam_rehearsal_packet
from local_redteam.misuse_scenarios import build_misuse_scenario_library
from local_redteam.adversarial_prompt_checklist import build_adversarial_prompt_safety_checklist
from local_redteam.safety_assurance import build_safety_assurance_summary
from local_redteam.redteam_quality import build_redteam_quality_report
from local_redteam.redteam_report_builder import (
    build_redteam_domain_registry_markdown_report,
    build_redteam_rehearsal_packet_markdown_report,
    build_misuse_scenario_library_markdown_report,
    build_adversarial_prompt_checklist_markdown_report,
    build_safety_assurance_markdown_report,
    build_redteam_quality_markdown_report,
    build_redteam_status_markdown_report
)

class LocalRedTeamPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: LocalRedTeamProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile

    def build_redteam_domain_registry(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        if not self.profile: return {}, {}
        df, summary = build_redteam_domain_registry(self.profile)
        if save:
            self.data_lake.save_redteam_domain_registry(df, summary)
            md = build_redteam_domain_registry_markdown_report(summary, df)
            self.data_lake.save_local_redteam_report(self.profile.name, summary, md)
        return {"redteam_domain_registry": df}, summary

    def build_final_local_redteam_rehearsal(self, save: bool = True) -> tuple[str, dict]:
        if not self.profile: return "", {}
        text, summary = build_final_local_redteam_rehearsal_packet(self.project_root, self.profile)
        if save:
            self.data_lake.save_final_local_redteam_rehearsal_packet(text, summary)
            md = build_redteam_rehearsal_packet_markdown_report(summary, text)
            self.data_lake.save_local_redteam_report(self.profile.name, summary, md)
        return text, summary

    def build_misuse_scenario_library(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        if not self.profile: return {}, {}
        df, summary = build_misuse_scenario_library(self.profile)
        if save:
            self.data_lake.save_misuse_scenario_library(df, summary)
            md = build_misuse_scenario_library_markdown_report(summary, df)
            self.data_lake.save_local_redteam_report(self.profile.name, summary, md)
        return {"misuse_scenario_library": df}, summary

    def build_adversarial_prompt_safety_checklist(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        if not self.profile: return {}, {}
        df, summary = build_adversarial_prompt_safety_checklist(self.profile)
        if save:
            self.data_lake.save_adversarial_prompt_safety_checklist(df, summary)
            md = build_adversarial_prompt_checklist_markdown_report(summary, df)
            self.data_lake.save_local_redteam_report(self.profile.name, summary, md)
        return {"adversarial_prompt_safety_checklist": df}, summary

    def build_safety_assurance_summary(self, save: bool = True) -> tuple[str, dict]:
        if not self.profile: return "", {}
        text, summary = build_safety_assurance_summary(self.project_root, self.profile)
        if save:
            self.data_lake.save_safety_assurance_summary(text, summary)
            md = build_safety_assurance_markdown_report(summary, text)
            self.data_lake.save_local_redteam_report(self.profile.name, summary, md)
        return text, summary

    def build_redteam_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        if not self.profile: return {}, {}
        quality = build_redteam_quality_report({"note": "Quality build"})
        if save:
            self.data_lake.save_redteam_quality(self.profile.name, quality)
            md = build_redteam_quality_markdown_report({"note": "Quality report generated"}, quality)
            self.data_lake.save_local_redteam_report(self.profile.name, {"quality": quality}, md)
        return quality, {"note": "Quality report done"}

    def build_redteam_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        if not self.profile: return pd.DataFrame(), {}
        df = pd.DataFrame([{"status": "ok"}])
        summary = {"total": len(df)}
        if save:
            md = build_redteam_status_markdown_report(summary, df)
            self.data_lake.save_local_redteam_report(self.profile.name, summary, md)
        return df, summary
