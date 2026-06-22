import pandas as pd
from typing import Tuple, Dict, Any, Optional
from pathlib import Path

from local_maintenance.maintenance_config import LocalMaintenanceProfile, get_default_local_maintenance_profile
from local_maintenance.domain_registry import build_maintenance_domain_registry
from local_maintenance.task_registry import build_maintenance_task_registry
from local_maintenance.review_calendar import build_periodic_review_calendar, build_monthly_review_calendar, build_quarterly_review_calendar
from local_maintenance.refresh_cadence import (
    build_report_refresh_cadence_registry,
    build_datalake_refresh_cadence_registry,
    build_documentation_refresh_cadence_registry,
    build_test_refresh_cadence_registry,
    build_safety_security_refresh_cadence_registry,
    build_backup_packaging_refresh_cadence_registry,
    build_cross_layer_refresh_cadence_registry
)
from local_maintenance.dependency_aging import build_dependency_aging_watch_report
from local_maintenance.dependency_review import build_dependency_review_checklist
from local_maintenance.stale_artifact_watch import build_deprecated_artifact_watch_report
from local_maintenance.stale_report_watch import build_stale_report_watch_report
from local_maintenance.stale_documentation_watch import build_stale_documentation_watch_report
from local_maintenance.stale_test_watch import build_stale_test_watch_report
from local_maintenance.manual_review_queue import build_manual_review_queue
from local_maintenance.maintenance_gaps import build_maintenance_gap_register
from local_maintenance.maintenance_risks import build_maintenance_risk_summary
from local_maintenance.sustainability_scoring import build_sustainability_score_report
from local_maintenance.operator_review_checklist import build_operator_periodic_review_checklist
from local_maintenance.review_templates import build_monthly_review_template, build_quarterly_review_template
from local_maintenance.refresh_command_plan import build_refresh_command_plan
from local_maintenance.maintenance_runbook import build_maintenance_runbook
from local_maintenance.sustainability_binder import build_long_term_sustainability_binder
from local_maintenance.maintenance_validation import build_maintenance_validation_report
from local_maintenance.maintenance_quality import build_maintenance_quality_report

class LocalMaintenancePipeline:
    def __init__(
        self,
        data_lake: Any,  # Inject DataLake here
        settings: Any,   # Inject Settings here
        project_root: Path,
        profile: Optional[LocalMaintenanceProfile] = None
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_local_maintenance_profile()

    def build_maintenance_domain_registry(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        domain_df, d_sum = build_maintenance_domain_registry(self.profile)
        task_df, t_sum = build_maintenance_task_registry(domain_df, self.profile)

        tables = {"domains": domain_df, "tasks": task_df}
        summary = {"domains": d_sum, "tasks": t_sum}

        if save and self.data_lake:
            self.data_lake.save_maintenance_domain_registry(domain_df, d_sum)
            self.data_lake.save_maintenance_task_registry(task_df, t_sum)

        return tables, summary

    def build_periodic_review_calendar(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        _, t_sum = self.build_maintenance_domain_registry(save=False)
        # Re-build for simplicity
        domain_df, _ = build_maintenance_domain_registry(self.profile)
        task_df, _ = build_maintenance_task_registry(domain_df, self.profile)

        cal_df, cal_sum = build_periodic_review_calendar(task_df, self.profile)
        monthly_df = build_monthly_review_calendar(task_df, self.profile)
        quarterly_df = build_quarterly_review_calendar(task_df, self.profile)
        op_df, op_sum = build_operator_periodic_review_checklist(self.profile)

        tables = {
            "calendar": cal_df,
            "monthly_calendar": monthly_df,
            "quarterly_calendar": quarterly_df,
            "operator_checklist": op_df
        }

        summary = {"calendar": cal_sum, "operator": op_sum}

        if save and self.data_lake:
            self.data_lake.save_periodic_review_calendar(cal_df, cal_sum)
            self.data_lake.save_operator_periodic_review_checklist(op_df, op_sum)

        return tables, summary

    def build_refresh_cadence_report(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        rep_df, rep_sum = build_report_refresh_cadence_registry(self.profile)
        dl_df, dl_sum = build_datalake_refresh_cadence_registry(self.profile)
        doc_df, doc_sum = build_documentation_refresh_cadence_registry(self.profile)
        test_df, test_sum = build_test_refresh_cadence_registry(self.profile)
        sec_df, sec_sum = build_safety_security_refresh_cadence_registry(self.profile)
        bak_df, bak_sum = build_backup_packaging_refresh_cadence_registry(self.profile)
        cross_df, cross_sum = build_cross_layer_refresh_cadence_registry(self.profile)
        cmd_df, cmd_sum = build_refresh_command_plan(self.profile)

        tables = {
            "report_cadence": rep_df,
            "datalake_cadence": dl_df,
            "documentation_cadence": doc_df,
            "test_cadence": test_df,
            "safety_cadence": sec_df,
            "backup_cadence": bak_df,
            "cross_layer_cadence": cross_df,
            "command_plan": cmd_df
        }

        summary = {"commands": cmd_sum}

        if save and self.data_lake:
            self.data_lake.save_report_refresh_cadence_registry(rep_df, rep_sum)
            self.data_lake.save_datalake_refresh_cadence_registry(dl_df, dl_sum)
            self.data_lake.save_documentation_refresh_cadence_registry(doc_df, doc_sum)
            self.data_lake.save_test_refresh_cadence_registry(test_df, test_sum)
            self.data_lake.save_safety_security_refresh_cadence_registry(sec_df, sec_sum)
            self.data_lake.save_backup_packaging_refresh_cadence_registry(bak_df, bak_sum)
            self.data_lake.save_cross_layer_refresh_cadence_registry(cross_df, cross_sum)
            self.data_lake.save_refresh_command_plan(cmd_df, cmd_sum)

        return tables, summary

    def build_dependency_aging_watch(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        age_df, age_sum = build_dependency_aging_watch_report(self.project_root, self.profile)
        rev_df, rev_sum = build_dependency_review_checklist(age_df, self.profile)

        tables = {"aging": age_df, "review": rev_df}
        summary = {"aging": age_sum, "review": rev_sum}

        if save and self.data_lake:
            self.data_lake.save_dependency_aging_watch_report(age_df, age_sum)
            self.data_lake.save_dependency_review_checklist(rev_df, rev_sum)

        return tables, summary

    def build_maintenance_sustainability_report(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        # Get necessary inputs
        domain_df, _ = build_maintenance_domain_registry(self.profile)
        task_df, _ = build_maintenance_task_registry(domain_df, self.profile)
        cal_df, _ = build_periodic_review_calendar(task_df, self.profile)
        cmd_df, _ = build_refresh_command_plan(self.profile)

        dep_tables, _ = self.build_dependency_aging_watch(save=False)
        dep_df = dep_tables["aging"]

        cadence_tables, _ = self.build_refresh_cadence_report(save=False)

        stale_art_df, _ = build_deprecated_artifact_watch_report(self.project_root, self.profile)
        stale_rep_df, _ = build_stale_report_watch_report(self.project_root, self.profile)
        stale_doc_df, _ = build_stale_documentation_watch_report(self.project_root, self.profile)
        stale_test_df, _ = build_stale_test_watch_report(self.project_root, self.profile)

        gap_df, gap_sum = build_maintenance_gap_register(self.project_root, task_df, cadence_tables, self.profile)
        queue_df, queue_sum = build_manual_review_queue(dep_df, stale_rep_df, stale_doc_df, stale_test_df, gap_df, self.profile)
        risk_df, risk_sum = build_maintenance_risk_summary(gap_df, queue_df, dep_df, self.profile)
        score_df, score_sum = build_sustainability_score_report(task_df, gap_df, risk_df, self.profile)

        m_temp, _ = build_monthly_review_template(self.profile)
        q_temp, _ = build_quarterly_review_template(self.profile)
        runbook, _ = build_maintenance_runbook(task_df, cal_df, cmd_df, queue_df, self.profile)
        binder, _ = build_long_term_sustainability_binder(domain_df, task_df, cal_df, score_df, risk_df, self.profile)

        tables = {
            "deprecated_artifacts": stale_art_df,
            "stale_reports": stale_rep_df,
            "stale_docs": stale_doc_df,
            "stale_tests": stale_test_df,
            "manual_review_queue": queue_df,
            "gaps": gap_df,
            "risks": risk_df,
            "score": score_df
        }

        summary = {"score": score_sum, "risks": risk_sum}

        if save and self.data_lake:
            self.data_lake.save_deprecated_artifact_watch_report(stale_art_df)
            self.data_lake.save_stale_report_watch_report(stale_rep_df)
            self.data_lake.save_stale_documentation_watch_report(stale_doc_df)
            self.data_lake.save_stale_test_watch_report(stale_test_df)
            self.data_lake.save_manual_review_queue(queue_df, queue_sum)
            self.data_lake.save_maintenance_gap_register(gap_df, gap_sum)
            self.data_lake.save_maintenance_risk_summary(risk_df, risk_sum)
            self.data_lake.save_sustainability_score_report(score_df, score_sum)

            self.data_lake.save_monthly_review_template(m_temp)
            self.data_lake.save_quarterly_review_template(q_temp)
            self.data_lake.save_maintenance_runbook(runbook)
            self.data_lake.save_long_term_sustainability_binder(binder)

        return tables, summary

    def build_maintenance_quality_report(self, save: bool = True) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        domain_df, _ = build_maintenance_domain_registry(self.profile)
        task_df, _ = build_maintenance_task_registry(domain_df, self.profile)
        cmd_df, _ = build_refresh_command_plan(self.profile)

        val_df, val_sum = build_maintenance_validation_report(
            {"domains": domain_df, "tasks": task_df, "commands": cmd_df}, self.profile
        )

        quality = build_maintenance_quality_report(val_sum, domain_df, task_df, None, self.profile)

        if save and self.data_lake:
            self.data_lake.save_maintenance_validation_report(val_df, val_sum)
            self.data_lake.save_maintenance_quality(self.profile.name, quality)

        return {"validation": val_df}, quality

    def build_maintenance_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        # Dummy implementation for status checking
        data = [{"file": "status_check", "status": "ok"}]
        df = pd.DataFrame(data)
        summary = {"total_files": len(df)}
        return df, summary
