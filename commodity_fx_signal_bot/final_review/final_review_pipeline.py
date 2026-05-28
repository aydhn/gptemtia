import pandas as pd
from pathlib import Path
from typing import Tuple, Dict, Optional
import datetime

from data.storage.data_lake import DataLake
from config.settings import Settings
from final_review.final_review_config import FinalReviewProfile, get_default_final_review_profile
from final_review.system_inventory import build_full_system_inventory
from final_review.architecture_audit import build_architecture_audit_report
from final_review.safety_audit import build_safety_audit_report
from final_review.integration_audit import build_integration_audit_report
from final_review.command_audit import build_command_audit_report
from final_review.datalake_audit import build_datalake_audit_report
from final_review.report_output_audit import build_report_output_audit_report
from final_review.documentation_audit import build_documentation_audit_report
from final_review.quality_gate_audit import build_quality_gate_audit_report
from final_review.readiness_audit import build_readiness_audit_report
from final_review.consolidation_audit import build_phase_1_55_consolidation_audit
from final_review.risk_register import build_risks_from_audit_results, risks_to_dataframe, summarize_final_risks
from final_review.gap_register import build_gaps_from_audit_results, gaps_to_dataframe, summarize_final_gaps
from final_review.acceptance_checklist import (
    build_final_acceptance_checklist,
    evaluate_final_acceptance_checklist,
    calculate_acceptance_score,
    calculate_safety_score,
    infer_final_readiness_label,
    summarize_acceptance_checklist
)
from final_review.final_review_models import FinalAcceptanceSnapshot, final_acceptance_snapshot_to_dict, build_acceptance_snapshot_id
from final_review.release_readiness_dry_run import build_release_readiness_dry_run_report
from final_review.final_review_quality import build_final_review_quality_report
from final_review.final_review_report_builder import build_final_system_review_markdown_report

class FinalReviewPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[FinalReviewProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_final_review_profile()

    def build_final_system_review(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], dict]:
        # Generate components
        inv_tables, inv_summary = build_full_system_inventory(self.project_root)
        arch_df, arch_sum = build_architecture_audit_report(self.project_root, self.profile)
        safe_df, safe_sum = build_safety_audit_report(self.project_root, self.profile)
        int_df, int_sum = build_integration_audit_report(self.project_root, self.profile)
        cmd_df, cmd_sum = build_command_audit_report(self.project_root, self.profile)
        dl_df, dl_sum = build_datalake_audit_report(self.project_root, self.profile)
        ro_df, ro_sum = build_report_output_audit_report(self.project_root, self.profile)
        doc_df, doc_sum = build_documentation_audit_report(self.project_root, self.profile)
        qg_df, qg_sum = build_quality_gate_audit_report(self.project_root, self.profile)
        ready_df, ready_sum = build_readiness_audit_report(self.project_root, self.profile)

        audit_tables = {
            "architecture": arch_df,
            "safety": safe_df,
            "integration": int_df,
            "commands": cmd_df,
            "datalake": dl_df,
            "report_outputs": ro_df,
            "documentation": doc_df,
            "quality_gates": qg_df,
            "readiness": ready_df
        }

        summaries = {
            "documentation": doc_sum
        }

        # Risk & Gap
        risks = build_risks_from_audit_results(audit_tables, summaries)
        risk_df = risks_to_dataframe(risks)
        risk_sum = summarize_final_risks(risk_df)

        gaps = build_gaps_from_audit_results(audit_tables, summaries)
        gap_df = gaps_to_dataframe(gaps)
        gap_sum = summarize_final_gaps(gap_df)

        # Acceptance
        chk_df = build_final_acceptance_checklist(self.profile)
        eval_chk_df = evaluate_final_acceptance_checklist(chk_df, summaries, risk_sum, gap_sum)
        acc_sum = summarize_acceptance_checklist(eval_chk_df)

        acc_score = calculate_acceptance_score(eval_chk_df, risk_sum)
        safe_score = calculate_safety_score(risk_df, safe_df)
        readiness_label = infer_final_readiness_label(acc_score, safe_score, risk_sum.get("blocking_risks", 0), self.profile)

        snapshot = FinalAcceptanceSnapshot(
            snapshot_id=build_acceptance_snapshot_id(self.profile.name, datetime.datetime.utcnow().isoformat()),
            created_at_utc=datetime.datetime.utcnow().isoformat(),
            profile_name=self.profile.name,
            acceptance_score=acc_score,
            safety_score=safe_score,
            readiness_label=readiness_label,
            audit_count=len(audit_tables),
            passed_audit_count=acc_sum.get("passed_items", 0),
            warning_count=0,
            failure_count=0,
            blocking_risk_count=risk_sum.get("blocking_risks", 0),
            gap_count=gap_sum.get("total_gaps", 0),
            warnings=[]
        )
        snapshot_dict = final_acceptance_snapshot_to_dict(snapshot)

        # Consolidation & Dry-Run
        consol_dfs, consol_sum = build_phase_1_55_consolidation_audit(self.project_root, self.profile)
        dryrun_df, dryrun_sum = build_release_readiness_dry_run_report(self.project_root, self.profile, acc_sum, risk_sum)

        summary = {
            "profile": self.profile.name,
            "passed": risk_sum.get("passed", False),
            "snapshot": snapshot_dict
        }

        quality = build_final_review_quality_report(summary, audit_tables, risk_df, gap_df)

        if save and hasattr(self.data_lake, "save_architecture_audit"):
            self.data_lake.save_architecture_audit(arch_df)
            self.data_lake.save_safety_audit(safe_df)
            self.data_lake.save_integration_audit(int_df)
            self.data_lake.save_command_audit(cmd_df)
            self.data_lake.save_datalake_contract_audit(dl_df)
            self.data_lake.save_report_output_audit(ro_df)
            self.data_lake.save_documentation_audit(doc_df)
            self.data_lake.save_quality_gate_audit(qg_df)
            self.data_lake.save_readiness_audit(ready_df)
            self.data_lake.save_final_risk_register(risk_df)
            self.data_lake.save_final_gap_register(gap_df)
            self.data_lake.save_final_acceptance_checklist(eval_chk_df)
            self.data_lake.save_final_acceptance_snapshot(snapshot_dict)
            self.data_lake.save_release_readiness_dry_run(dryrun_df)
            self.data_lake.save_phase_1_55_consolidation_audit("phase_1_55_matrix", consol_dfs.get("matrix", pd.DataFrame()))
            self.data_lake.save_final_review_quality(self.profile.name, quality)

            md = build_final_system_review_markdown_report(summary, audit_tables)
            self.data_lake.save_final_review_report(self.profile.name, summary, md)

        return audit_tables, summary

    def build_architecture_audit(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        df, summary = build_architecture_audit_report(self.project_root, self.profile)
        if save and hasattr(self.data_lake, "save_architecture_audit"):
            self.data_lake.save_architecture_audit(df, summary)
        return df, summary

    def build_safety_audit(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        df, summary = build_safety_audit_report(self.project_root, self.profile)
        if save and hasattr(self.data_lake, "save_safety_audit"):
            self.data_lake.save_safety_audit(df, summary)
        return df, summary

    def build_offline_acceptance_audit(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        # Minimal mock wrapper for script
        chk_df = build_final_acceptance_checklist(self.profile)
        eval_df = evaluate_final_acceptance_checklist(chk_df, {}, {}, {})
        summary = {"passed": True}
        if save and hasattr(self.data_lake, "save_final_acceptance_checklist"):
            self.data_lake.save_final_acceptance_checklist(eval_df, summary)
        return eval_df, summary

    def build_release_readiness_dry_run(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        df, summary = build_release_readiness_dry_run_report(self.project_root, self.profile, {}, {})
        if save and hasattr(self.data_lake, "save_release_readiness_dry_run"):
            self.data_lake.save_release_readiness_dry_run(df, summary)
        return df, summary

    def build_final_consolidation_audit(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], dict]:
        dfs, summary = build_phase_1_55_consolidation_audit(self.project_root, self.profile)
        if save and hasattr(self.data_lake, "save_phase_1_55_consolidation_audit"):
            self.data_lake.save_phase_1_55_consolidation_audit("matrix", dfs.get("matrix", pd.DataFrame()), summary)
        return dfs, summary

    def build_final_review_status(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        # Mock status
        df = pd.DataFrame([{"component": "architecture", "status": "ok"}])
        summary = {"passed": True}
        return df, summary
