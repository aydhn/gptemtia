
from pathlib import Path
import pandas as pd
from typing import Optional
from config.settings import Settings
from data.storage.data_lake import DataLake
from local_closure.closure_config import LocalClosureProfile, get_local_closure_profile, get_default_local_closure_profile
from local_closure.closure_domain_registry import build_closure_domain_registry
from local_closure.meta_review import build_final_project_meta_review_report
from local_closure.lessons_learned import build_lessons_learned_compendium
from local_closure.roadmap_backlog import build_future_roadmap_backlog
from local_closure.closure_dossier import build_v1_local_closure_dossier
from local_closure.closure_quality import build_closure_quality_report
from local_closure.closure_recaps import build_closure_executive_recap, build_closure_technical_recap
from local_closure.closure_exceptions import build_closure_exception_register
from local_closure.closure_gaps import build_closure_gap_register
from local_closure.closure_risks import build_closure_risk_summary
from local_closure.closure_scoring import build_closure_readiness_score_report
from local_closure.unresolved_items import build_closure_unresolved_items_register

class LocalClosurePipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[LocalClosureProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_local_closure_profile()

    def build_closure_domain_registry(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, summary = build_closure_domain_registry(self.profile)
        if save and self.settings.local_closure_save_reports:
            self.data_lake.save_closure_domain_registry(df, summary)
        return {"domain_registry": df}, summary

    def build_final_meta_review(self, save: bool = True) -> tuple[str, dict]:
        text, summary = build_final_project_meta_review_report(self.project_root, self.profile)
        if save and self.settings.local_closure_save_reports:
            self.data_lake.save_final_project_meta_review_report(text, summary)
        return text, summary

    def build_lessons_learned_compendium(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, summary = build_lessons_learned_compendium(self.project_root, self.profile)
        if save and self.settings.local_closure_save_reports:
            self.data_lake.save_lessons_learned_compendium(df, summary)
        return {"lessons_learned": df}, summary

    def build_future_roadmap_backlog(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, summary = build_future_roadmap_backlog(self.project_root, self.profile)
        if save and self.settings.local_closure_save_reports:
            self.data_lake.save_future_roadmap_backlog(df, summary)
        return {"roadmap_backlog": df}, summary

    def build_v1_local_closure_dossier(self, save: bool = True) -> tuple[str, dict]:
        meta_text, _ = build_final_project_meta_review_report(self.project_root, self.profile)
        lessons_df, _ = build_lessons_learned_compendium(self.project_root, self.profile)
        roadmap_df, _ = build_future_roadmap_backlog(self.project_root, self.profile)
        ex_recap, _ = build_closure_executive_recap(self.project_root, self.profile)
        tech_recap, _ = build_closure_technical_recap(self.project_root, self.profile)
        
        recap_texts = {
            "executive": ex_recap,
            "technical": tech_recap
        }
        text, summary = build_v1_local_closure_dossier(
            meta_text, lessons_df, roadmap_df, recap_texts, self.profile
        )
        if save and self.settings.local_closure_save_reports:
            self.data_lake.save_v1_local_closure_dossier(text, summary)
        return text, summary

    def build_closure_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        domain_df, _ = build_closure_domain_registry(self.profile)
        roadmap_df, _ = build_future_roadmap_backlog(self.project_root, self.profile)
        quality = build_closure_quality_report({"status": "generated"}, domain_df, roadmap_df, None)
        if save and self.settings.local_closure_save_reports:
            self.data_lake.save_closure_quality(self.profile.name, quality)
        return quality, {"total_checks": len(quality)}

    def build_closure_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "ok", "message": "all generated"}])
        return df, {"total": len(df)}
