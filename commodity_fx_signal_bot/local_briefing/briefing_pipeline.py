import pandas as pd
from pathlib import Path
from .briefing_config import LocalBriefingProfile, get_default_local_briefing_profile, get_local_briefing_profile
from .audience_registry import build_stakeholder_audience_registry
from .executive_summary import build_executive_summary_pack
from .project_one_pager import build_project_one_pager
from .deck_source import build_non_technical_briefing_deck_source, export_deck_source_to_markdown, export_deck_source_to_json
from .project_narrative import build_project_narrative_report
from .decision_context import build_decision_question_registry, build_decision_context_matrix, build_decision_context_binder
from .capability_map import build_capability_map_nontechnical
from .boundary_summary import build_boundary_non_use_summary
from .risk_limitation_narrative import build_risk_limitation_narrative
from .milestone_narrative import build_milestone_narrative
from .phase_evolution_narrative import build_phase_evolution_narrative
from .architecture_narrative import build_local_only_architecture_narrative
from .stakeholder_faq import build_stakeholder_faq_registry
from .executive_glossary import build_executive_glossary_registry
from .safe_communication import build_safe_communication_guide
from .communication_do_dont import build_communication_do_dont_registry
from .stakeholder_templates import build_stakeholder_update_templates
from .communication_gaps import build_communication_gap_register
from .communication_risks import build_communication_risk_summary
from .briefing_validation import build_briefing_validation_report
from .briefing_quality import build_briefing_quality_report
from .briefing_report_builder import *

class LocalBriefingPipeline:
    def __init__(self, data_lake, settings, project_root: Path, profile: LocalBriefingProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_local_briefing_profile()

    def build_briefing_profile_registry(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        aud_df, aud_sum = build_stakeholder_audience_registry(self.profile)
        gl_df, gl_sum = build_executive_glossary_registry(self.profile)
        do_df, do_sum = build_communication_do_dont_registry(self.profile)
        
        prof_df = pd.DataFrame([vars(self.profile)])
        
        if save:
            if hasattr(self.data_lake, 'save_communication_profile_registry'):
                self.data_lake.save_communication_profile_registry(prof_df)
                self.data_lake.save_stakeholder_audience_registry(aud_df)
                self.data_lake.save_executive_glossary_registry(gl_df)
                self.data_lake.save_communication_do_dont_registry(do_df)
        
        return {"profile": prof_df, "audience": aud_df, "glossary": gl_df, "do_dont": do_df}, {"status": "ok"}

    def build_executive_summary_pack(self, save: bool = True) -> tuple[str, dict]:
        ex_text, ex_sum = build_executive_summary_pack(self.project_root, self.profile)
        op_text, op_sum = build_project_one_pager(self.project_root, self.profile)
        cm_df, cm_sum = build_capability_map_nontechnical(self.project_root, self.profile)
        bn_text, bn_sum = build_boundary_non_use_summary(self.project_root, self.profile)
        
        if save:
            if hasattr(self.data_lake, 'save_executive_summary_pack'):
                self.data_lake.save_executive_summary_pack(ex_text)
                self.data_lake.save_project_one_pager(op_text)
                self.data_lake.save_capability_map_nontechnical(cm_df)
                self.data_lake.save_boundary_non_use_summary(bn_text)
                
            docs_dir = self.project_root / "docs" / "generated" / "local_briefing"
            docs_dir.mkdir(parents=True, exist_ok=True)
            (docs_dir / "EXECUTIVE_SUMMARY_PACK.md").write_text(ex_text)
            (docs_dir / "PROJECT_ONE_PAGER.md").write_text(op_text)
        
        return ex_text, {"status": "ok"}

    def build_briefing_deck_source(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        ds_df, ds_sum = build_non_technical_briefing_deck_source(self.project_root, self.profile)
        pn_text, pn_sum = build_project_narrative_report(self.project_root, self.profile)
        rl_text, rl_sum = build_risk_limitation_narrative(self.project_root, self.profile)
        
        if save:
            if hasattr(self.data_lake, 'save_non_technical_briefing_deck_source'):
                self.data_lake.save_non_technical_briefing_deck_source(ds_df)
                self.data_lake.save_project_narrative_report(pn_text)
                self.data_lake.save_risk_limitation_narrative(rl_text)
                
            docs_dir = self.project_root / "docs" / "generated" / "local_briefing"
            docs_dir.mkdir(parents=True, exist_ok=True)
            (docs_dir / "NON_TECHNICAL_BRIEFING_DECK_SOURCE.md").write_text(export_deck_source_to_markdown(ds_df))
            (docs_dir / "PROJECT_NARRATIVE_REPORT.md").write_text(pn_text)
        
        return {"deck_source": ds_df}, {"status": "ok"}

    def build_decision_context_binder(self, save: bool = True) -> tuple[str, dict]:
        dq_df, dq_sum = build_decision_question_registry(self.profile)
        dm_df, dm_sum = build_decision_context_matrix(dq_df, self.profile)
        dc_text, dc_sum = build_decision_context_binder(self.project_root, self.profile)
        mn_text, mn_sum = build_milestone_narrative(self.project_root, self.profile)
        pe_text, pe_sum = build_phase_evolution_narrative(self.project_root, self.profile)
        an_text, an_sum = build_local_only_architecture_narrative(self.project_root, self.profile)
        
        if save:
            if hasattr(self.data_lake, 'save_decision_question_registry'):
                self.data_lake.save_decision_question_registry(dq_df)
                self.data_lake.save_decision_context_matrix(dm_df)
                self.data_lake.save_decision_context_binder(dc_text)
                self.data_lake.save_milestone_narrative(mn_text)
                self.data_lake.save_phase_evolution_narrative(pe_text)
                self.data_lake.save_local_only_architecture_narrative(an_text)
                
            docs_dir = self.project_root / "docs" / "generated" / "local_briefing"
            docs_dir.mkdir(parents=True, exist_ok=True)
            (docs_dir / "DECISION_CONTEXT_BINDER.md").write_text(dc_text)
        
        return dc_text, {"status": "ok"}

    def build_stakeholder_communication_kit(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        faq_df, faq_sum = build_stakeholder_faq_registry(self.profile)
        sc_text, sc_sum = build_safe_communication_guide(self.profile)
        st_df, st_sum = build_stakeholder_update_templates(self.profile)
        
        aud_df, _ = build_stakeholder_audience_registry(self.profile)
        gap_df, gap_sum = build_communication_gap_register(aud_df, pd.DataFrame(), faq_df, st_df, self.profile)
        risk_df, risk_sum = build_communication_risk_summary(gap_df, pd.DataFrame(), st_df, self.profile)
        
        if save:
            if hasattr(self.data_lake, 'save_stakeholder_faq_registry'):
                self.data_lake.save_stakeholder_faq_registry(faq_df)
                self.data_lake.save_safe_communication_guide(sc_text)
                self.data_lake.save_stakeholder_update_templates(st_df)
                self.data_lake.save_communication_gap_register(gap_df)
                self.data_lake.save_communication_risk_summary(risk_df)
                
            docs_dir = self.project_root / "docs" / "generated" / "local_briefing"
            docs_dir.mkdir(parents=True, exist_ok=True)
            (docs_dir / "SAFE_COMMUNICATION_GUIDE.md").write_text(sc_text)
        
        return {"faq": faq_df, "templates": st_df, "gaps": gap_df, "risks": risk_df}, {"status": "ok"}

    def build_briefing_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        val_df, val_sum = build_briefing_validation_report({}, self.profile)
        qual = build_briefing_quality_report({"test": 1})
        
        if save:
            if hasattr(self.data_lake, 'save_briefing_validation_report'):
                self.data_lake.save_briefing_validation_report(val_df)
                self.data_lake.save_briefing_quality(self.profile.name, qual)
                
        return qual, {"status": "ok"}

    def build_briefing_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "ok"}])
        return df, {"status": "ok"}
