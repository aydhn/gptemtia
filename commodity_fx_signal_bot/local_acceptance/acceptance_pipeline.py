import pandas as pd
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from local_acceptance.acceptance_config import LocalAcceptanceProfile, get_local_acceptance_profile

from local_acceptance.acceptance_domain_registry import build_acceptance_domain_registry
from local_acceptance.acceptance_simulation import build_final_acceptance_simulation_checklist
from local_acceptance.reviewer_pack import build_independent_reviewer_pack
from local_acceptance.reviewer_questions import build_reviewer_question_bank
from local_acceptance.reviewer_evidence_matrix import build_reviewer_evidence_request_matrix
from local_acceptance.evidence_trail import build_audit_style_local_evidence_trail
from local_acceptance.evidence_output_trace import build_evidence_output_trace_matrix
from local_acceptance.evidence_test_trace import build_evidence_test_trace_matrix
from local_acceptance.evidence_doc_trace import build_evidence_doc_trace_matrix
from local_acceptance.evidence_safety_trace import build_evidence_safety_boundary_trace_matrix
from local_acceptance.signoff_rehearsal import build_signoff_rehearsal_checklist, build_signoff_rehearsal_binder
from local_acceptance.verification_rehearsal import build_final_verification_rehearsal_plan
from local_acceptance.verification_scenarios import build_final_verification_scenario_registry
from local_acceptance.acceptance_criteria import build_acceptance_criteria_registry
from local_acceptance.acceptance_exceptions import build_acceptance_exception_register
from local_acceptance.acceptance_no_go_safe_go import build_acceptance_no_go_register, build_acceptance_safe_go_register, build_acceptance_no_go_safe_go_summary
from local_acceptance.review_templates import build_independent_review_notes_template, build_acceptance_response_template
from local_acceptance.verification_evidence_binder import build_final_verification_evidence_binder
from local_acceptance.acceptance_gaps import build_acceptance_gap_register
from local_acceptance.acceptance_risks import build_acceptance_risk_summary
from local_acceptance.acceptance_scoring import build_acceptance_readiness_score_report
from local_acceptance.acceptance_validation import build_acceptance_validation_report
from local_acceptance.acceptance_quality import build_acceptance_quality_report

class LocalAcceptancePipeline:
    def __init__(self, data_lake: DataLake, settings: Settings, project_root: Path, profile: LocalAcceptanceProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_local_acceptance_profile(settings.default_local_acceptance_profile)

    def build_acceptance_domain_registry(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, s = build_acceptance_domain_registry(self.profile)
        c_df, c_s = build_acceptance_criteria_registry(self.profile)
        ng_df, ng_s = build_acceptance_no_go_register(self.project_root, self.profile)
        sg_df, sg_s = build_acceptance_safe_go_register(self.project_root, self.profile)
        
        dfs = {"domain": df, "criteria": c_df, "no_go": ng_df, "safe_go": sg_df}
        summary = {"domain": s, "criteria": c_s, "no_go": ng_s, "safe_go": sg_s}
        
        if save:
            self.data_lake.save_acceptance_domain_registry(df, s)
            self.data_lake.save_acceptance_criteria_registry(c_df, c_s)
            self.data_lake.save_acceptance_no_go_register(ng_df, ng_s)
            self.data_lake.save_acceptance_safe_go_register(sg_df, sg_s)
        return dfs, summary

    def build_final_acceptance_simulation(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, s = build_final_acceptance_simulation_checklist(self.project_root, self.profile)
        e_df, e_s = build_acceptance_exception_register(df, pd.DataFrame(), self.profile)
        sc_df, sc_s = build_acceptance_readiness_score_report(df, pd.DataFrame(), pd.DataFrame(), self.profile)
        
        dfs = {"checklist": df, "exceptions": e_df, "score": sc_df}
        summary = {"checklist": s, "exceptions": e_s, "score": sc_s}
        
        if save:
            self.data_lake.save_final_acceptance_simulation_checklist(df, s)
            self.data_lake.save_acceptance_exception_register(e_df, e_s)
            self.data_lake.save_acceptance_readiness_score_report(sc_df, sc_s)
        return dfs, summary

    def build_independent_reviewer_pack(self, save: bool = True) -> tuple[str, dict]:
        q_df, q_s = build_reviewer_question_bank(self.profile)
        m_df, m_s = build_reviewer_evidence_request_matrix(q_df, self.project_root, self.profile)
        
        text, s = build_independent_reviewer_pack(pd.DataFrame(), q_df, pd.DataFrame(), self.profile)
        nt, ns = build_independent_review_notes_template(self.profile)
        rt, rs = build_acceptance_response_template(self.profile)
        
        if save:
            self.data_lake.save_reviewer_question_bank(q_df, q_s)
            self.data_lake.save_reviewer_evidence_request_matrix(m_df, m_s)
            self.data_lake.save_independent_reviewer_pack(text, s)
            self.data_lake.save_independent_review_notes_template(nt, ns)
            self.data_lake.save_acceptance_response_template(rt, rs)
        return text, s

    def build_acceptance_evidence_trail(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, s = build_audit_style_local_evidence_trail(self.project_root, self.profile)
        o_df, o_s = build_evidence_output_trace_matrix(df, self.project_root, self.profile)
        t_df, t_s = build_evidence_test_trace_matrix(df, self.project_root, self.profile)
        d_df, d_s = build_evidence_doc_trace_matrix(df, self.project_root, self.profile)
        sa_df, sa_s = build_evidence_safety_boundary_trace_matrix(df, self.project_root, self.profile)
        
        bt, bs = build_final_verification_evidence_binder(df, o_df, t_df, d_df, sa_df, self.profile)
        
        dfs = {"evidence": df, "output_trace": o_df, "test_trace": t_df, "doc_trace": d_df, "safety_trace": sa_df}
        summary = {"evidence": s, "output_trace": o_s, "test_trace": t_s, "doc_trace": d_s, "safety_trace": sa_s, "binder": bs}
        
        if save:
            self.data_lake.save_audit_style_local_evidence_trail(df, s)
            self.data_lake.save_evidence_output_trace_matrix(o_df, o_s)
            self.data_lake.save_evidence_test_trace_matrix(t_df, t_s)
            self.data_lake.save_evidence_doc_trace_matrix(d_df, d_s)
            self.data_lake.save_evidence_safety_boundary_trace_matrix(sa_df, sa_s)
            self.data_lake.save_final_verification_evidence_binder(bt, bs)
        return dfs, summary

    def build_signoff_rehearsal(self, save: bool = True) -> tuple[str, dict]:
        c_df, c_s = build_signoff_rehearsal_checklist(self.profile)
        sc_df, sc_s = build_final_verification_scenario_registry(self.profile)
        p_df, p_s = build_final_verification_rehearsal_plan(self.project_root, self.profile)
        
        text, s = build_signoff_rehearsal_binder(c_df, pd.DataFrame(), pd.DataFrame(), self.profile)
        
        g_df, g_s = build_acceptance_gap_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), self.profile)
        r_df, r_s = build_acceptance_risk_summary(g_df, pd.DataFrame(), pd.DataFrame(), self.profile)
        
        if save:
            self.data_lake.save_signoff_rehearsal_checklist(c_df, c_s)
            self.data_lake.save_final_verification_scenario_registry(sc_df, sc_s)
            self.data_lake.save_final_verification_rehearsal_plan(p_df, p_s)
            self.data_lake.save_signoff_rehearsal_binder(text, s)
            self.data_lake.save_acceptance_gap_register(g_df, g_s)
            self.data_lake.save_acceptance_risk_summary(r_df, r_s)
        return text, s

    def build_acceptance_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        v_df, v_s = build_acceptance_validation_report({}, self.profile)
        q = build_acceptance_quality_report({"dummy": "dummy"}, pd.DataFrame(), pd.DataFrame(), pd.DataFrame())
        
        if save:
            self.data_lake.save_acceptance_validation_report(v_df, v_s)
            self.data_lake.save_acceptance_quality(self.profile.name, q)
        return q, {"status": "generated"}

    def build_acceptance_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "ok"}])
        s = {"status": "ok"}
        return df, s
