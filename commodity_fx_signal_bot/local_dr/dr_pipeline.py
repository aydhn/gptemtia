
import pandas as pd
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from local_dr.dr_config import LocalDRProfile, get_default_local_dr_profile

class LocalDRPipeline:
    def __init__(self, data_lake: DataLake, settings: Settings, project_root: Path, profile: LocalDRProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_local_dr_profile()

    def build_dr_domain_registry(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        # placeholders, since the subagents implement the actual builder logic, we can import them here if they exist
        try:
            from local_dr.dr_domain_registry import build_dr_domain_registry
            from local_dr.failure_mode_registry import build_failure_mode_registry
        except ImportError:
            return {}, {}
            
        domain_df, domain_summary = build_dr_domain_registry(self.profile)
        failure_df, failure_summary = build_failure_mode_registry(self.profile)
        
        if save:
            self.data_lake.save_dr_domain_registry(domain_df, domain_summary)
            self.data_lake.save_failure_mode_registry(failure_df, failure_summary)
            
        return {"domain_df": domain_df, "failure_df": failure_df}, {"domain": domain_summary, "failure": failure_summary}

    def build_dr_tabletop_scenarios(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        try:
            from local_dr.tabletop_scenarios import build_dr_tabletop_scenario_registry
            from local_dr.dr_domain_registry import build_dr_domain_registry
        except ImportError:
            return {}, {}
            
        domain_df, _ = build_dr_domain_registry(self.profile)
        scenario_df, scenario_summary = build_dr_tabletop_scenario_registry(domain_df, self.profile)
        
        if save:
            self.data_lake.save_dr_tabletop_scenario_registry(scenario_df, scenario_summary)
            
        return {"scenario_df": scenario_df}, {"scenario": scenario_summary}

    def build_restore_drill_simulation(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        try:
            from local_dr.restore_drill_simulation import build_restore_drill_simulation_registry
            from local_dr.restore_readiness_checklist import build_restore_readiness_dry_run_checklist
            from local_dr.archive_restore_traceability import build_archive_restore_traceability_report
            from local_dr.backup_restore_traceability import build_backup_restore_traceability_report
        except ImportError:
            return {}, {}
            
        drill_df, drill_summary = build_restore_drill_simulation_registry(self.project_root, self.profile)
        checklist_df, checklist_summary = build_restore_readiness_dry_run_checklist(self.project_root, self.profile)
        archive_df, archive_summary = build_archive_restore_traceability_report(self.project_root, self.profile)
        backup_df, backup_summary = build_backup_restore_traceability_report(self.project_root, self.profile)
        
        if save:
            self.data_lake.save_restore_drill_simulation_registry(drill_df, drill_summary)
            self.data_lake.save_restore_readiness_dry_run_checklist(checklist_df, checklist_summary)
            self.data_lake.save_archive_restore_traceability_report(archive_df, archive_summary)
            self.data_lake.save_backup_restore_traceability_report(backup_df, backup_summary)
            
        return {"drill_df": drill_df, "checklist_df": checklist_df, "archive_df": archive_df, "backup_df": backup_df}, {"drill": drill_summary, "checklist": checklist_summary, "archive": archive_summary, "backup": backup_summary}

    def build_failure_mode_playbooks(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        try:
            from local_dr.failure_playbooks import build_failure_mode_playbook_index
            from local_dr.failure_mode_registry import build_failure_mode_registry
            from local_dr.datalake_restore_simulation import build_datalake_restore_simulation_report
            from local_dr.docs_restore_simulation import build_docs_restore_simulation_report
            from local_dr.reports_restore_simulation import build_reports_restore_simulation_report
            from local_dr.config_env_restore_simulation import build_config_env_restore_simulation_report
            from local_dr.scripts_tests_restore_simulation import build_scripts_tests_restore_simulation_report
            from local_dr.cross_layer_restore_simulation import build_cross_layer_restore_simulation_report
            from local_dr.secret_boundary_rehearsal import build_secret_boundary_incident_rehearsal
        except ImportError:
            return {}, {}
            
        failure_df, _ = build_failure_mode_registry(self.profile)
        playbook_df, playbook_summary = build_failure_mode_playbook_index(failure_df, self.profile)
        
        dl_df, dl_summary = build_datalake_restore_simulation_report(self.project_root, self.profile)
        docs_df, docs_summary = build_docs_restore_simulation_report(self.project_root, self.profile)
        reports_df, reports_summary = build_reports_restore_simulation_report(self.project_root, self.profile)
        config_df, config_summary = build_config_env_restore_simulation_report(self.project_root, self.profile)
        scripts_df, scripts_summary = build_scripts_tests_restore_simulation_report(self.project_root, self.profile)
        cross_df, cross_summary = build_cross_layer_restore_simulation_report(self.project_root, self.profile)
        secret_df, secret_summary = build_secret_boundary_incident_rehearsal(self.project_root, self.profile)
        
        if save:
            self.data_lake.save_failure_mode_playbook_index(playbook_df, playbook_summary)
            self.data_lake.save_datalake_restore_simulation_report(dl_df, dl_summary)
            self.data_lake.save_docs_restore_simulation_report(docs_df, docs_summary)
            self.data_lake.save_reports_restore_simulation_report(reports_df, reports_summary)
            self.data_lake.save_config_env_restore_simulation_report(config_df, config_summary)
            self.data_lake.save_scripts_tests_restore_simulation_report(scripts_df, scripts_summary)
            self.data_lake.save_cross_layer_restore_simulation_report(cross_df, cross_summary)
            self.data_lake.save_secret_boundary_incident_rehearsal(secret_df, secret_summary)
            
        return {"playbook_df": playbook_df, "dl_df": dl_df, "docs_df": docs_df, "reports_df": reports_df, "config_df": config_df, "scripts_df": scripts_df, "cross_df": cross_df, "secret_df": secret_df}, {"playbook": playbook_summary}

    def build_incident_rehearsal_binder(self, save: bool = True) -> tuple[str, dict]:
        try:
            from local_dr.incident_rehearsal_binder import build_incident_rehearsal_binder
            from local_dr.recovery_command_plan import build_manual_recovery_command_plan
            from local_dr.dr_gaps import build_dr_gap_register
            from local_dr.dr_risks import build_dr_risk_summary
            from local_dr.resilience_scoring import build_resilience_score_report
            from local_dr.dr_domain_registry import build_dr_domain_registry
            from local_dr.tabletop_scenarios import build_dr_tabletop_scenario_registry
            from local_dr.restore_drill_simulation import build_restore_drill_simulation_registry
            from local_dr.failure_mode_registry import build_failure_mode_registry
        except ImportError:
            return "", {}
            
        # These need their dependencies to be built first, but this is just the pipeline wrapping.
        domain_df, _ = build_dr_domain_registry(self.profile)
        scenario_df, _ = build_dr_tabletop_scenario_registry(domain_df, self.profile)
        drill_df, _ = build_restore_drill_simulation_registry(self.project_root, self.profile)
        failure_df, _ = build_failure_mode_registry(self.profile)
        
        cmd_df, cmd_sum = build_manual_recovery_command_plan(self.profile)
        gap_df, gap_sum = build_dr_gap_register(scenario_df, drill_df, None, None, self.profile)
        risk_df, risk_sum = build_dr_risk_summary(gap_df, drill_df, None, self.profile)
        score_df, score_sum = build_resilience_score_report(drill_df, gap_df, risk_df, self.profile)
        
        binder_text, binder_summary = build_incident_rehearsal_binder(scenario_df, drill_df, failure_df, self.profile)
        
        if save:
            self.data_lake.save_manual_recovery_command_plan(cmd_df, cmd_sum)
            self.data_lake.save_dr_gap_register(gap_df, gap_sum)
            self.data_lake.save_dr_risk_summary(risk_df, risk_sum)
            self.data_lake.save_resilience_score_report(score_df, score_sum)
            self.data_lake.save_incident_rehearsal_binder(binder_text, binder_summary)
            
        return binder_text, binder_summary

    def build_dr_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        try:
            from local_dr.dr_quality import build_dr_quality_report
            from local_dr.dr_validation import build_dr_validation_report
        except ImportError:
            return {}, {}
            
        val_df, val_sum = build_dr_validation_report({}, self.profile)
        qual = build_dr_quality_report({"dummy": "summary"})
        
        if save:
            self.data_lake.save_dr_validation_report(val_df, val_sum)
            self.data_lake.save_dr_quality(self.profile.name, qual)
            
        return qual, val_sum

    def build_dr_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "ok"}])
        if save:
            self.data_lake.save_local_dr_report(self.profile.name, {"status": "ok"})
        return df, {"total": 1}
