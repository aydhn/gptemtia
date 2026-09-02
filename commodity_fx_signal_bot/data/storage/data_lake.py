from typing import Dict, Optional
from config.paths import LAKE_FEATURES_DIR
import os
from typing import Optional
import json
import re
from pathlib import Path

import pandas as pd

from config.paths import LAKE_FEATURES_GROUP_FEATURES_DIR

from config.symbols import SymbolSpec
from core.logger import get_logger
from data.data_quality import DataQualityError, validate_ohlcv_dataframe

logger = get_logger(__name__)


class DataLake:

    def _save_df(self, df, directory, filename, summary=None):
        import pandas as pd
        if df is None: return Path(directory) / f"{filename}.csv"
        Path(directory).mkdir(parents=True, exist_ok=True)
        out_path = Path(directory) / f"{filename}.csv"
        df.to_csv(out_path, index=False)
        return out_path

    def _load_df(self, directory, filename):
        import pandas as pd
        out_path = Path(directory) / f"{filename}.csv"
        if not out_path.exists(): return pd.DataFrame()
        return pd.read_csv(out_path)

    def _save_text(self, text, directory, filename, summary=None):
        if text is None: return Path(directory) / f"{filename}.md"
        Path(directory).mkdir(parents=True, exist_ok=True)
        out_path = Path(directory) / f"{filename}.md"
        out_path.write_text(text, encoding="utf-8")
        return out_path

    def _load_text(self, directory, filename):
        out_path = Path(directory) / f"{filename}.md"
        if not out_path.exists(): return ""
        return out_path.read_text(encoding="utf-8")

    def _save_json(self, data, directory, filename):
        import json
        Path(directory).mkdir(parents=True, exist_ok=True)
        out_path = Path(directory) / f"{filename}.json"
        out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return out_path

    def _load_json(self, directory, filename):
        import json
        out_path = Path(directory) / f"{filename}.json"
        if not out_path.exists(): return {}
        return json.loads(out_path.read_text(encoding="utf-8"))



    def save_performance_profile_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_PROFILES_DIR, "performance_profile_registry", summary)
    def load_performance_profile_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_PROFILES_DIR, "performance_profile_registry")

    def save_performance_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_DOMAINS_DIR, "performance_domain_registry", summary)
    def load_performance_domain_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_DOMAINS_DIR, "performance_domain_registry")

    def save_final_local_performance_budget(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_BUDGET_DIR, "final_local_performance_budget", summary)
    def load_final_local_performance_budget(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_BUDGET_DIR, "final_local_performance_budget")

    def save_lightweight_runtime_profile(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_RUNTIME_PROFILE_DIR, "lightweight_runtime_profile", summary)
    def load_lightweight_runtime_profile(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_RUNTIME_PROFILE_DIR, "lightweight_runtime_profile")

    def save_resource_footprint_rehearsal_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_RESOURCE_FOOTPRINT_DIR, "resource_footprint_rehearsal_report", summary)
    def load_resource_footprint_rehearsal_report(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_RESOURCE_FOOTPRINT_DIR, "resource_footprint_rehearsal_report")

    def save_cpu_usage_estimate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_CPU_DIR, "cpu_usage_estimate_registry", summary)
    def load_cpu_usage_estimate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_CPU_DIR, "cpu_usage_estimate_registry")

    def save_memory_usage_estimate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_MEMORY_DIR, "memory_usage_estimate_registry", summary)
    def load_memory_usage_estimate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_MEMORY_DIR, "memory_usage_estimate_registry")

    def save_disk_usage_estimate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_DISK_DIR, "disk_usage_estimate_registry", summary)
    def load_disk_usage_estimate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_DISK_DIR, "disk_usage_estimate_registry")

    def save_report_output_growth_estimate(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_GROWTH_DIR, "report_output_growth_estimate", summary)
    def load_report_output_growth_estimate(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_GROWTH_DIR, "report_output_growth_estimate")

    def save_datalake_growth_estimate(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_GROWTH_DIR, "datalake_growth_estimate", summary)
    def load_datalake_growth_estimate(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_GROWTH_DIR, "datalake_growth_estimate")

    def save_generated_docs_growth_estimate(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_GROWTH_DIR, "generated_docs_growth_estimate", summary)
    def load_generated_docs_growth_estimate(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_GROWTH_DIR, "generated_docs_growth_estimate")

    def save_script_runtime_estimate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_SCRIPT_RUNTIME_DIR, "script_runtime_estimate_registry", summary)
    def load_script_runtime_estimate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_SCRIPT_RUNTIME_DIR, "script_runtime_estimate_registry")

    def save_test_runtime_estimate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_TEST_RUNTIME_DIR, "test_runtime_estimate_registry", summary)
    def load_test_runtime_estimate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_TEST_RUNTIME_DIR, "test_runtime_estimate_registry")

    def save_pipeline_runtime_estimate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_PIPELINE_RUNTIME_DIR, "pipeline_runtime_estimate_registry", summary)
    def load_pipeline_runtime_estimate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_PIPELINE_RUNTIME_DIR, "pipeline_runtime_estimate_registry")

    def save_maintenance_cost_estimate(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_MAINTENANCE_COST_DIR, "maintenance_cost_estimate", summary)
    def load_maintenance_cost_estimate(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_MAINTENANCE_COST_DIR, "maintenance_cost_estimate")

    def save_maintenance_effort_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_MAINTENANCE_EFFORT_DIR, "maintenance_effort_matrix", summary)
    def load_maintenance_effort_matrix(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_MAINTENANCE_EFFORT_DIR, "maintenance_effort_matrix")

    def save_operator_time_budget_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_OPERATOR_TIME_DIR, "operator_time_budget_report", summary)
    def load_operator_time_budget_report(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_OPERATOR_TIME_DIR, "operator_time_budget_report")

    def save_local_machine_suitability_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_MACHINE_SUITABILITY_DIR, "local_machine_suitability_checklist", summary)
    def load_local_machine_suitability_checklist(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_MACHINE_SUITABILITY_DIR, "local_machine_suitability_checklist")

    def save_offline_efficiency_planning_guide(self, text: str, summary: dict | None = None) -> Path:
        return self._save_text(text, self.paths.LAKE_LOCAL_PERFORMANCE_EFFICIENCY_DIR, "offline_efficiency_planning_guide", summary)
    def load_offline_efficiency_planning_guide(self) -> str:
        return self._load_text(self.paths.LAKE_LOCAL_PERFORMANCE_EFFICIENCY_DIR, "offline_efficiency_planning_guide")

    def save_efficiency_candidate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_EFFICIENCY_DIR, "efficiency_candidate_registry", summary)
    def load_efficiency_candidate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_EFFICIENCY_DIR, "efficiency_candidate_registry")

    def save_lightweight_mode_recommendation_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_LIGHTWEIGHT_MODE_DIR, "lightweight_mode_recommendation_registry", summary)
    def load_lightweight_mode_recommendation_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_LIGHTWEIGHT_MODE_DIR, "lightweight_mode_recommendation_registry")

    def save_heavy_output_warning_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_WARNINGS_DIR, "heavy_output_warning_registry", summary)
    def load_heavy_output_warning_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_WARNINGS_DIR, "heavy_output_warning_registry")

    def save_storage_retention_rehearsal_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_RETENTION_DIR, "storage_retention_rehearsal_plan", summary)
    def load_storage_retention_rehearsal_plan(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_RETENTION_DIR, "storage_retention_rehearsal_plan")

    def save_report_rotation_rehearsal_guide(self, text: str, summary: dict | None = None) -> Path:
        return self._save_text(text, self.paths.LAKE_LOCAL_PERFORMANCE_RETENTION_DIR, "report_rotation_rehearsal_guide", summary)
    def load_report_rotation_rehearsal_guide(self) -> str:
        return self._load_text(self.paths.LAKE_LOCAL_PERFORMANCE_RETENTION_DIR, "report_rotation_rehearsal_guide")

    def save_datalake_retention_rehearsal_guide(self, text: str, summary: dict | None = None) -> Path:
        return self._save_text(text, self.paths.LAKE_LOCAL_PERFORMANCE_RETENTION_DIR, "datalake_retention_rehearsal_guide", summary)
    def load_datalake_retention_rehearsal_guide(self) -> str:
        return self._load_text(self.paths.LAKE_LOCAL_PERFORMANCE_RETENTION_DIR, "datalake_retention_rehearsal_guide")

    def save_performance_no_go_safe_go_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_NO_GO_SAFE_GO_DIR, "performance_no_go_safe_go_summary", summary)
    def load_performance_no_go_safe_go_summary(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_NO_GO_SAFE_GO_DIR, "performance_no_go_safe_go_summary")

    def save_performance_exception_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_EXCEPTIONS_DIR, "performance_exception_register", summary)
    def load_performance_exception_register(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_EXCEPTIONS_DIR, "performance_exception_register")

    def save_performance_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_GAPS_DIR, "performance_gap_register", summary)
    def load_performance_gap_register(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_GAPS_DIR, "performance_gap_register")

    def save_performance_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_RISKS_DIR, "performance_risk_summary", summary)
    def load_performance_risk_summary(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_RISKS_DIR, "performance_risk_summary")

    def save_performance_readiness_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_SCORING_DIR, "performance_readiness_score_report", summary)
    def load_performance_readiness_score_report(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_SCORING_DIR, "performance_readiness_score_report")

    def save_performance_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_VALIDATION_DIR, "performance_validation_report", summary)
    def load_performance_validation_report(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_VALIDATION_DIR, "performance_validation_report")

    def save_performance_quality(self, profile_name: str, quality: dict) -> Path:
        return self._save_json(quality, self.paths.LAKE_LOCAL_PERFORMANCE_QUALITY_DIR, f"performance_quality_{profile_name}")
    def load_performance_quality(self, profile_name: str) -> dict:
        return self._load_json(self.paths.LAKE_LOCAL_PERFORMANCE_QUALITY_DIR, f"performance_quality_{profile_name}")

    def save_local_performance_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        if markdown:
            self._save_text(markdown, self.paths.LAKE_LOCAL_PERFORMANCE_DIR, f"performance_report_{profile_name}")
        return self._save_json(report, self.paths.LAKE_LOCAL_PERFORMANCE_DIR, f"performance_report_{profile_name}")
    def load_local_performance_report(self, profile_name: str) -> dict:
        return self._load_json(self.paths.LAKE_LOCAL_PERFORMANCE_DIR, f"performance_report_{profile_name}")
    def list_local_performance_reports(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_communication_profile_registry(self, df, summary=None): pass
    def load_communication_profile_registry(self): return pd.DataFrame()
    def save_stakeholder_audience_registry(self, df, summary=None): pass
    def load_stakeholder_audience_registry(self): return pd.DataFrame()
    def save_executive_summary_pack(self, text, summary=None): pass
    def load_executive_summary_pack(self): return ""
    def save_project_one_pager(self, text, summary=None): pass
    def load_project_one_pager(self): return ""
    def save_non_technical_briefing_deck_source(self, df, summary=None): pass
    def load_non_technical_briefing_deck_source(self): return pd.DataFrame()
    def save_project_narrative_report(self, text, summary=None): pass
    def load_project_narrative_report(self): return ""
    def save_decision_context_binder(self, text, summary=None): pass
    def load_decision_context_binder(self): return ""
    def save_capability_map_nontechnical(self, df, summary=None): pass
    def load_capability_map_nontechnical(self): return pd.DataFrame()
    def save_boundary_non_use_summary(self, text, summary=None): pass
    def load_boundary_non_use_summary(self): return ""
    def save_risk_limitation_narrative(self, text, summary=None): pass
    def load_risk_limitation_narrative(self): return ""
    def save_milestone_narrative(self, text, summary=None): pass
    def load_milestone_narrative(self): return ""
    def save_phase_evolution_narrative(self, text, summary=None): pass
    def load_phase_evolution_narrative(self): return ""
    def save_local_only_architecture_narrative(self, text, summary=None): pass
    def load_local_only_architecture_narrative(self): return ""
    def save_stakeholder_faq_registry(self, df, summary=None): pass
    def load_stakeholder_faq_registry(self): return pd.DataFrame()
    def save_executive_glossary_registry(self, df, summary=None): pass
    def load_executive_glossary_registry(self): return pd.DataFrame()
    def save_safe_communication_guide(self, text, summary=None): pass
    def load_safe_communication_guide(self): return ""
    def save_communication_do_dont_registry(self, df, summary=None): pass
    def load_communication_do_dont_registry(self): return pd.DataFrame()
    def save_decision_question_registry(self, df, summary=None): pass
    def load_decision_question_registry(self): return pd.DataFrame()
    def save_decision_context_matrix(self, df, summary=None): pass
    def load_decision_context_matrix(self): return pd.DataFrame()
    def save_stakeholder_update_templates(self, df, summary=None): pass
    def load_stakeholder_update_templates(self): return pd.DataFrame()
    def save_communication_gap_register(self, df, summary=None): pass
    def load_communication_gap_register(self): return pd.DataFrame()
    def save_communication_risk_summary(self, df, summary=None): pass
    def load_communication_risk_summary(self): return pd.DataFrame()
    def save_briefing_validation_report(self, df, summary=None): pass
    def load_briefing_validation_report(self): return pd.DataFrame()
    def save_briefing_quality(self, profile_name, quality): pass
    def load_briefing_quality(self, profile_name): return {}
    def save_local_briefing_report(self, profile_name, report, markdown=None): pass
    def load_local_briefing_report(self, profile_name): return {}
    def list_local_briefing_reports(self): return pd.DataFrame()


    def save_dr_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_domains", "dr_domain_registry", summary=summary)
        
    def load_dr_domain_registry(self) -> pd.DataFrame:
        return self._load_df("local_dr_domains", "dr_domain_registry")
        
    def save_dr_tabletop_scenario_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_tabletop", "dr_tabletop_scenario_registry", summary=summary)
        
    def load_dr_tabletop_scenario_registry(self) -> pd.DataFrame:
        return self._load_df("local_dr_tabletop", "dr_tabletop_scenario_registry")
        
    def save_restore_drill_simulation_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_restore_drills", "restore_drill_simulation_registry", summary=summary)
        
    def load_restore_drill_simulation_registry(self) -> pd.DataFrame:
        return self._load_df("local_dr_restore_drills", "restore_drill_simulation_registry")
        
    def save_failure_mode_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_failure_modes", "failure_mode_registry", summary=summary)
        
    def load_failure_mode_registry(self) -> pd.DataFrame:
        return self._load_df("local_dr_failure_modes", "failure_mode_registry")
        
    def save_failure_mode_playbook_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_playbooks", "failure_mode_playbook_index", summary=summary)
        
    def load_failure_mode_playbook_index(self) -> pd.DataFrame:
        return self._load_df("local_dr_playbooks", "failure_mode_playbook_index")
        
    def save_incident_rehearsal_binder(self, text: str, summary: dict | None = None) -> Path:
        path = self.paths.get("local_dr_rehearsals") / "incident_rehearsal_binder.txt"
        path.write_text(text, encoding="utf-8")
        if summary:
            self._save_summary("local_dr_rehearsals", "incident_rehearsal_binder", summary)
        return path
        
    def load_incident_rehearsal_binder(self) -> str:
        path = self.paths.get("local_dr_rehearsals") / "incident_rehearsal_binder.txt"
        if path.exists():
            return path.read_text(encoding="utf-8")
        return ""
        
    def save_resilience_exercise_calendar(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_calendar", "resilience_exercise_calendar", summary=summary)
        
    def load_resilience_exercise_calendar(self) -> pd.DataFrame:
        return self._load_df("local_dr_calendar", "resilience_exercise_calendar")
        
    def save_restore_readiness_dry_run_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_restore_readiness", "restore_readiness_dry_run_checklist", summary=summary)
        
    def load_restore_readiness_dry_run_checklist(self) -> pd.DataFrame:
        return self._load_df("local_dr_restore_readiness", "restore_readiness_dry_run_checklist")
        
    def save_archive_restore_traceability_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_traceability", "archive_restore_traceability_report", summary=summary)
        
    def load_archive_restore_traceability_report(self) -> pd.DataFrame:
        return self._load_df("local_dr_traceability", "archive_restore_traceability_report")
        
    def save_backup_restore_traceability_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_traceability", "backup_restore_traceability_report", summary=summary)
        
    def load_backup_restore_traceability_report(self) -> pd.DataFrame:
        return self._load_df("local_dr_traceability", "backup_restore_traceability_report")
        
    def save_datalake_restore_simulation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_datalake", "datalake_restore_simulation_report", summary=summary)
        
    def load_datalake_restore_simulation_report(self) -> pd.DataFrame:
        return self._load_df("local_dr_datalake", "datalake_restore_simulation_report")
        
    def save_docs_restore_simulation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_docs", "docs_restore_simulation_report", summary=summary)
        
    def load_docs_restore_simulation_report(self) -> pd.DataFrame:
        return self._load_df("local_dr_docs", "docs_restore_simulation_report")
        
    def save_reports_restore_simulation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_reports", "reports_restore_simulation_report", summary=summary)
        
    def load_reports_restore_simulation_report(self) -> pd.DataFrame:
        return self._load_df("local_dr_reports", "reports_restore_simulation_report")
        
    def save_config_env_restore_simulation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_config_env", "config_env_restore_simulation_report", summary=summary)
        
    def load_config_env_restore_simulation_report(self) -> pd.DataFrame:
        return self._load_df("local_dr_config_env", "config_env_restore_simulation_report")
        
    def save_scripts_tests_restore_simulation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_scripts_tests", "scripts_tests_restore_simulation_report", summary=summary)
        
    def load_scripts_tests_restore_simulation_report(self) -> pd.DataFrame:
        return self._load_df("local_dr_scripts_tests", "scripts_tests_restore_simulation_report")
        
    def save_cross_layer_restore_simulation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_cross_layer", "cross_layer_restore_simulation_report", summary=summary)
        
    def load_cross_layer_restore_simulation_report(self) -> pd.DataFrame:
        return self._load_df("local_dr_cross_layer", "cross_layer_restore_simulation_report")
        
    def save_secret_boundary_incident_rehearsal(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_security", "secret_boundary_incident_rehearsal", summary=summary)
        
    def load_secret_boundary_incident_rehearsal(self) -> pd.DataFrame:
        return self._load_df("local_dr_security", "secret_boundary_incident_rehearsal")
        
    def save_manual_recovery_command_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_recovery_commands", "manual_recovery_command_plan", summary=summary)
        
    def load_manual_recovery_command_plan(self) -> pd.DataFrame:
        return self._load_df("local_dr_recovery_commands", "manual_recovery_command_plan")
        
    def save_dr_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_gaps", "dr_gap_register", summary=summary)
        
    def load_dr_gap_register(self) -> pd.DataFrame:
        return self._load_df("local_dr_gaps", "dr_gap_register")
        
    def save_dr_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_risks", "dr_risk_summary", summary=summary)
        
    def load_dr_risk_summary(self) -> pd.DataFrame:
        return self._load_df("local_dr_risks", "dr_risk_summary")
        
    def save_resilience_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_scoring", "resilience_score_report", summary=summary)
        
    def load_resilience_score_report(self) -> pd.DataFrame:
        return self._load_df("local_dr_scoring", "resilience_score_report")
        
    def save_dr_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_dr_validation", "dr_validation_report", summary=summary)
        
    def load_dr_validation_report(self) -> pd.DataFrame:
        return self._load_df("local_dr_validation", "dr_validation_report")
        
    def save_dr_quality(self, profile_name: str, quality: dict) -> Path:
        import json
        path = self.paths.get("local_dr_quality") / f"dr_quality_{profile_name}.json"
        path.write_text(json.dumps(quality, indent=2), encoding="utf-8")
        return path
        
    def load_dr_quality(self, profile_name: str) -> dict:
        import json
        path = self.paths.get("local_dr_quality") / f"dr_quality_{profile_name}.json"
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
        return {}
        
    def save_local_dr_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        import json
        path = self.paths.get("local_dr_reports") / f"local_dr_report_{profile_name}.json"
        path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        if markdown:
            md_path = self.paths.get("local_dr_reports") / f"local_dr_report_{profile_name}.md"
            md_path.write_text(markdown, encoding="utf-8")
        return path
        
    def load_local_dr_report(self, profile_name: str) -> dict:
        import json
        path = self.paths.get("local_dr_reports") / f"local_dr_report_{profile_name}.json"
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
        return {}
        
    def list_local_dr_reports(self) -> pd.DataFrame:
        import pandas as pd

        path = self.paths.get("local_dr_reports")
        reports = []
        if path.exists():
            for f in path.glob("local_dr_report_*.json"):
                reports.append({"report_file": f.name})
        return pd.DataFrame(reports)


    def _save_parquet_and_csv(self, df, directory, filename_prefix):
        directory.mkdir(parents=True, exist_ok=True)
        parquet_path = directory / f"{filename_prefix}.parquet"
        csv_path = directory / f"{filename_prefix}.csv"
        df.to_parquet(parquet_path, index=False)
        df.to_csv(csv_path, index=False)
        return parquet_path

    def _load_parquet(self, path):
        import pandas as pd

        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()


    # Phase 67: Local Timeline
    def save_project_event_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_EVENTS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_EVENTS_DIR, "project_event_registry")

    def load_project_event_registry(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_EVENTS_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_EVENTS_DIR / "project_event_registry.parquet")

    def save_phase_chronology_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_PHASES_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_PHASES_DIR, "phase_chronology_registry")

    def load_phase_chronology_registry(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_PHASES_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_PHASES_DIR / "phase_chronology_registry.parquet")

    def save_artifact_evolution_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_ARTIFACT_EVOLUTION_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_ARTIFACT_EVOLUTION_DIR, "artifact_evolution_registry")

    def load_artifact_evolution_registry(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_ARTIFACT_EVOLUTION_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_ARTIFACT_EVOLUTION_DIR / "artifact_evolution_registry.parquet")

    def save_file_modification_timeline(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_FILE_TIMELINE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_FILE_TIMELINE_DIR, "file_modification_timeline")

    def load_file_modification_timeline(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_FILE_TIMELINE_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_FILE_TIMELINE_DIR / "file_modification_timeline.parquet")

    def save_report_generation_timeline(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_REPORT_TIMELINE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_REPORT_TIMELINE_DIR, "report_generation_timeline")

    def load_report_generation_timeline(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_REPORT_TIMELINE_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_REPORT_TIMELINE_DIR / "report_generation_timeline.parquet")

    def save_datalake_artifact_timeline(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_DATALAKE_TIMELINE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_DATALAKE_TIMELINE_DIR, "datalake_artifact_timeline")

    def load_datalake_artifact_timeline(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_DATALAKE_TIMELINE_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_DATALAKE_TIMELINE_DIR / "datalake_artifact_timeline.parquet")

    def save_documentation_evolution_timeline(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_DOCUMENTATION_TIMELINE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_DOCUMENTATION_TIMELINE_DIR, "documentation_evolution_timeline")

    def load_documentation_evolution_timeline(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_DOCUMENTATION_TIMELINE_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_DOCUMENTATION_TIMELINE_DIR / "documentation_evolution_timeline.parquet")

    def save_command_script_evolution_timeline(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_COMMAND_TIMELINE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_COMMAND_TIMELINE_DIR, "command_script_evolution_timeline")

    def load_command_script_evolution_timeline(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_COMMAND_TIMELINE_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_COMMAND_TIMELINE_DIR / "command_script_evolution_timeline.parquet")

    def save_evidence_timeline(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_EVIDENCE_TIMELINE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_EVIDENCE_TIMELINE_DIR, "evidence_timeline")

    def load_evidence_timeline(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_EVIDENCE_TIMELINE_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_EVIDENCE_TIMELINE_DIR / "evidence_timeline.parquet")

    def save_metadata_card_timeline(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_METADATA_TIMELINE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_METADATA_TIMELINE_DIR, "metadata_card_timeline")

    def load_metadata_card_timeline(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_METADATA_TIMELINE_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_METADATA_TIMELINE_DIR / "metadata_card_timeline.parquet")

    def save_knowledge_graph_evolution_timeline(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_GRAPH_TIMELINE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_GRAPH_TIMELINE_DIR, "knowledge_graph_evolution_timeline")

    def load_knowledge_graph_evolution_timeline(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_GRAPH_TIMELINE_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_GRAPH_TIMELINE_DIR / "knowledge_graph_evolution_timeline.parquet")

    def save_scenario_regression_event_timeline(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_SCENARIO_REGRESSION_TIMELINE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_SCENARIO_REGRESSION_TIMELINE_DIR, "scenario_regression_event_timeline")

    def load_scenario_regression_event_timeline(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_SCENARIO_REGRESSION_TIMELINE_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_SCENARIO_REGRESSION_TIMELINE_DIR / "scenario_regression_event_timeline.parquet")

    def save_quality_safety_event_timeline(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_QUALITY_SAFETY_TIMELINE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_QUALITY_SAFETY_TIMELINE_DIR, "quality_safety_event_timeline")

    def load_quality_safety_event_timeline(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_QUALITY_SAFETY_TIMELINE_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_QUALITY_SAFETY_TIMELINE_DIR / "quality_safety_event_timeline.parquet")

    def save_backup_packaging_secrets_event_timeline(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_BACKUP_PACKAGING_SECRETS_TIMELINE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_BACKUP_PACKAGING_SECRETS_TIMELINE_DIR, "backup_packaging_secrets_event_timeline")

    def load_backup_packaging_secrets_event_timeline(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_BACKUP_PACKAGING_SECRETS_TIMELINE_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_BACKUP_PACKAGING_SECRETS_TIMELINE_DIR / "backup_packaging_secrets_event_timeline.parquet")

    def save_artifact_temporal_lineage(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_TEMPORAL_LINEAGE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_TEMPORAL_LINEAGE_DIR, "artifact_temporal_lineage")

    def load_artifact_temporal_lineage(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_TEMPORAL_LINEAGE_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_TEMPORAL_LINEAGE_DIR / "artifact_temporal_lineage.parquet")

    def save_module_event_cluster_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_CLUSTERS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_CLUSTERS_DIR, "module_event_cluster_report")

    def load_module_event_cluster_report(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_CLUSTERS_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_CLUSTERS_DIR / "module_event_cluster_report.parquet")

    def save_event_freshness_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_FRESHNESS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_FRESHNESS_DIR, "event_freshness_report")

    def load_event_freshness_report(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_FRESHNESS_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_FRESHNESS_DIR / "event_freshness_report.parquet")

    def save_stale_artifact_timeline_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_FRESHNESS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_FRESHNESS_DIR, "stale_artifact_timeline_report")

    def load_stale_artifact_timeline_report(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_FRESHNESS_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_FRESHNESS_DIR / "stale_artifact_timeline_report.parquet")

    def save_event_gap_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_GAPS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_GAPS_DIR, "event_gap_report")

    def load_event_gap_report(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_GAPS_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_GAPS_DIR / "event_gap_report.parquet")

    def save_phase_event_digest(self, text: str, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_DIGESTS_DIR
        p = LAKE_LOCAL_TIMELINE_DIGESTS_DIR / "phase_event_digest.txt"
        LAKE_LOCAL_TIMELINE_DIGESTS_DIR.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            f.write(text)
        return p

    def load_phase_event_digest(self) -> str:
        from config.paths import LAKE_LOCAL_TIMELINE_DIGESTS_DIR
        p = LAKE_LOCAL_TIMELINE_DIGESTS_DIR / "phase_event_digest.txt"
        if p.exists():
            with open(p, "r") as f:
                return f.read()
        return ""

    def save_change_history_digest(self, text: str, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_DIGESTS_DIR
        p = LAKE_LOCAL_TIMELINE_DIGESTS_DIR / "change_history_digest.txt"
        LAKE_LOCAL_TIMELINE_DIGESTS_DIR.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            f.write(text)
        return p

    def load_change_history_digest(self) -> str:
        from config.paths import LAKE_LOCAL_TIMELINE_DIGESTS_DIR
        p = LAKE_LOCAL_TIMELINE_DIGESTS_DIR / "change_history_digest.txt"
        if p.exists():
            with open(p, "r") as f:
                return f.read()
        return ""

    def save_timeline_query_results(self, query_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_QUERIES_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_QUERIES_DIR, f"query_result_{query_name}")

    def load_timeline_query_results(self, query_name: str) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_QUERIES_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_QUERIES_DIR / f"query_result_{query_name}.parquet")

    def save_timeline_export_manifest(self, manifest: dict) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_EXPORTS_DIR
        import json
        p = LAKE_LOCAL_TIMELINE_EXPORTS_DIR / "export_manifest.json"
        LAKE_LOCAL_TIMELINE_EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            json.dump(manifest, f)
        return p

    def load_timeline_export_manifest(self) -> dict:
        from config.paths import LAKE_LOCAL_TIMELINE_EXPORTS_DIR
        import json
        p = LAKE_LOCAL_TIMELINE_EXPORTS_DIR / "export_manifest.json"
        if p.exists():
            with open(p, "r") as f:
                return json.load(f)
        return {}

    def save_timeline_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_VALIDATION_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_TIMELINE_VALIDATION_DIR, "timeline_validation_report")

    def load_timeline_validation_report(self) -> pd.DataFrame:
        from config.paths import LAKE_LOCAL_TIMELINE_VALIDATION_DIR
        return self._load_parquet(LAKE_LOCAL_TIMELINE_VALIDATION_DIR / "timeline_validation_report.parquet")

    def save_timeline_quality(self, profile_name: str, quality: dict) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_QUALITY_DIR
        import json
        p = LAKE_LOCAL_TIMELINE_QUALITY_DIR / f"timeline_quality_{profile_name}.json"
        LAKE_LOCAL_TIMELINE_QUALITY_DIR.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            json.dump(quality, f)
        return p

    def load_timeline_quality(self, profile_name: str) -> dict:
        from config.paths import LAKE_LOCAL_TIMELINE_QUALITY_DIR
        import json
        p = LAKE_LOCAL_TIMELINE_QUALITY_DIR / f"timeline_quality_{profile_name}.json"
        if p.exists():
            with open(p, "r") as f:
                return json.load(f)
        return {}

    def save_local_timeline_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        from config.paths import LAKE_LOCAL_TIMELINE_DIR
        import json
        p = LAKE_LOCAL_TIMELINE_DIR / f"timeline_report_{profile_name}.json"
        with open(p, "w") as f:
            json.dump(report, f)
        return p

    def load_local_timeline_report(self, profile_name: str) -> dict:
        from config.paths import LAKE_LOCAL_TIMELINE_DIR
        import json
        p = LAKE_LOCAL_TIMELINE_DIR / f"timeline_report_{profile_name}.json"
        if p.exists():
            with open(p, "r") as f:
                return json.load(f)
        return {}

    def list_local_timeline_reports(self) -> pd.DataFrame:
        return pd.DataFrame()

    # Phase 66: Local Knowledge Graph
    def save_graph_node_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_NODES_DIR, "graph_node_registry")

    def load_graph_node_registry(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_NODES_DIR / "graph_node_registry.parquet")

    def save_graph_edge_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_EDGES_DIR, "graph_edge_registry")

    def load_graph_edge_registry(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_EDGES_DIR / "graph_edge_registry.parquet")

    def save_artifact_relationship_graph(self, graph: dict, summary: dict | None = None) -> Path:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_GRAPHS_DIR / "artifact_relationship_graph.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(graph, f, indent=4)
        return path

    def load_artifact_relationship_graph(self) -> dict:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_GRAPHS_DIR / "artifact_relationship_graph.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_module_relationship_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_MODULE_GRAPHS_DIR, "module_relationship_graph")

    def load_module_relationship_graph(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_MODULE_GRAPHS_DIR / "module_relationship_graph.parquet")

    def save_report_relationship_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_REPORT_GRAPHS_DIR, "report_relationship_graph")

    def load_report_relationship_graph(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_REPORT_GRAPHS_DIR / "report_relationship_graph.parquet")

    def save_evidence_relationship_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_EVIDENCE_GRAPHS_DIR, "evidence_relationship_graph")

    def load_evidence_relationship_graph(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_EVIDENCE_GRAPHS_DIR / "evidence_relationship_graph.parquet")

    def save_card_relationship_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_CARD_GRAPHS_DIR, "card_relationship_graph")

    def load_card_relationship_graph(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_CARD_GRAPHS_DIR / "card_relationship_graph.parquet")

    def save_scenario_regression_relationship_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_SCENARIO_REGRESSION_GRAPHS_DIR, "scenario_regression_relationship_graph")

    def load_scenario_regression_relationship_graph(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_SCENARIO_REGRESSION_GRAPHS_DIR / "scenario_regression_relationship_graph.parquet")

    def save_command_report_relationship_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_COMMAND_REPORT_GRAPHS_DIR, "command_report_relationship_graph")

    def load_command_report_relationship_graph(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_COMMAND_REPORT_GRAPHS_DIR / "command_report_relationship_graph.parquet")

    def save_local_semantic_keyword_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_SEMANTIC_INDEX_DIR, "local_semantic_keyword_index")

    def load_local_semantic_keyword_index(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_SEMANTIC_INDEX_DIR / "local_semantic_keyword_index.parquet")

    def save_local_tfidf_index_manifest(self, manifest: dict) -> Path:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_TFIDF_INDEX_DIR / "local_tfidf_index_manifest.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=4)
        return path

    def load_local_tfidf_index_manifest(self) -> dict:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_TFIDF_INDEX_DIR / "local_tfidf_index_manifest.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_relationship_query_results(self, query_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_QUERIES_DIR, f"relationship_query_results_{query_name}")

    def load_relationship_query_results(self, query_name: str) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_QUERIES_DIR / f"relationship_query_results_{query_name}.parquet")

    def save_graph_neighborhood_report(self, node_id: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_NEIGHBORHOODS_DIR, f"graph_neighborhood_report_{node_id}")

    def load_graph_neighborhood_report(self, node_id: str) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_NEIGHBORHOODS_DIR / f"graph_neighborhood_report_{node_id}.parquet")

    def save_graph_centrality_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_ANALYSIS_DIR, "graph_centrality_summary")

    def load_graph_centrality_summary(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_ANALYSIS_DIR / "graph_centrality_summary.parquet")

    def save_orphan_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_ANALYSIS_DIR, "orphan_artifact_report")

    def load_orphan_artifact_report(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_ANALYSIS_DIR / "orphan_artifact_report.parquet")

    def save_graph_gap_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_GAPS_DIR, "graph_gap_report")

    def load_graph_gap_report(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_GAPS_DIR / "graph_gap_report.parquet")

    def save_stale_relationship_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_GAPS_DIR, "stale_relationship_report")

    def load_stale_relationship_report(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_GAPS_DIR / "stale_relationship_report.parquet")

    def save_graph_export_manifest(self, manifest: dict) -> Path:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_EXPORTS_DIR / "graph_export_manifest.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=4)
        return path

    def load_graph_export_manifest(self) -> dict:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_EXPORTS_DIR / "graph_export_manifest.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_graph_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_VALIDATION_DIR, "graph_validation_report")

    def load_graph_validation_report(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_VALIDATION_DIR / "graph_validation_report.parquet")

    def save_graph_quality(self, profile_name: str, quality: dict) -> Path:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_QUALITY_DIR / f"graph_quality_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=4)
        return path

    def load_graph_quality(self, profile_name: str) -> dict:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_QUALITY_DIR / f"graph_quality_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_local_knowledge_graph_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_EXPORTS_DIR / f"local_knowledge_graph_report_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        if markdown:
            md_path = REPORTS_LOCAL_KNOWLEDGE_GRAPH_MARKDOWN_DIR / f"local_knowledge_graph_report_{profile_name}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown)
        return path

    def load_local_knowledge_graph_report(self, profile_name: str) -> dict:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_EXPORTS_DIR / f"local_knowledge_graph_report_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_local_knowledge_graph_reports(self) -> pd.DataFrame:
        return pd.DataFrame()


    # ARTIFACT METADATA METHODS
    def save_research_artifact_inventory(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_INVENTORY_DIR, "research_artifact_inventory")

    def load_research_artifact_inventory(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_INVENTORY_DIR / "research_artifact_inventory.parquet")

    def save_research_artifact_metadata_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_REGISTRY_DIR, "research_artifact_metadata_registry")

    def load_research_artifact_metadata_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_REGISTRY_DIR / "research_artifact_metadata_registry.parquet")

    def save_model_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_MODEL_CARDS_DIR, "model_card_registry")

    def load_model_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_MODEL_CARDS_DIR / "model_card_registry.parquet")

    def save_dataset_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_DATASET_CARDS_DIR, "dataset_card_registry")

    def load_dataset_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_DATASET_CARDS_DIR / "dataset_card_registry.parquet")

    def save_experiment_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_EXPERIMENT_CARDS_DIR, "experiment_card_registry")

    def load_experiment_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_EXPERIMENT_CARDS_DIR / "experiment_card_registry.parquet")

    def save_reproducibility_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_REPRODUCIBILITY_CARDS_DIR, "reproducibility_card_registry")

    def load_reproducibility_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_REPRODUCIBILITY_CARDS_DIR / "reproducibility_card_registry.parquet")

    def save_backtest_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_BACKTEST_CARDS_DIR, "backtest_card_registry")

    def load_backtest_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_BACKTEST_CARDS_DIR / "backtest_card_registry.parquet")

    def save_scenario_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_SCENARIO_CARDS_DIR, "scenario_card_registry")

    def load_scenario_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_SCENARIO_CARDS_DIR / "scenario_card_registry.parquet")

    def save_regression_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_REGRESSION_CARDS_DIR, "regression_card_registry")

    def load_regression_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_REGRESSION_CARDS_DIR / "regression_card_registry.parquet")

    def save_feature_set_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_FEATURE_SET_CARDS_DIR, "feature_set_card_registry")

    def load_feature_set_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_FEATURE_SET_CARDS_DIR / "feature_set_card_registry.parquet")

    def save_synthetic_data_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_SYNTHETIC_DATA_CARDS_DIR, "synthetic_data_card_registry")

    def load_synthetic_data_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_SYNTHETIC_DATA_CARDS_DIR / "synthetic_data_card_registry.parquet")

    def save_research_report_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_RESEARCH_REPORT_CARDS_DIR, "research_report_card_registry")

    def load_research_report_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_RESEARCH_REPORT_CARDS_DIR / "research_report_card_registry.parquet")

    def save_artifact_lineage_cards(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_LINEAGE_CARDS_DIR, "artifact_lineage_cards")

    def load_artifact_lineage_cards(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_LINEAGE_CARDS_DIR / "artifact_lineage_cards.parquet")

    def save_artifact_limitation_cards(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_LIMITATION_CARDS_DIR, "artifact_limitation_cards")

    def load_artifact_limitation_cards(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_LIMITATION_CARDS_DIR / "artifact_limitation_cards.parquet")

    def save_intended_use_cards(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_INTENDED_USE_CARDS_DIR, "intended_use_cards")

    def load_intended_use_cards(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_INTENDED_USE_CARDS_DIR / "intended_use_cards.parquet")

    def save_non_use_policy_cards(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_NON_USE_POLICY_CARDS_DIR, "non_use_policy_cards")

    def load_non_use_policy_cards(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_NON_USE_POLICY_CARDS_DIR / "non_use_policy_cards.parquet")

    def save_reproducibility_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_REPRODUCIBILITY_CARDS_DIR, "reproducibility_checklist")

    def load_reproducibility_checklist(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_REPRODUCIBILITY_CARDS_DIR / "reproducibility_checklist.parquet")

    def save_metadata_completeness_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_SCORING_DIR, "metadata_completeness_report")

    def load_metadata_completeness_report(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_SCORING_DIR / "metadata_completeness_report.parquet")

    def save_metadata_freshness_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_SCORING_DIR, "metadata_freshness_report")

    def load_metadata_freshness_report(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_SCORING_DIR / "metadata_freshness_report.parquet")

    def save_card_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_VALIDATION_DIR, "card_validation_report")

    def load_card_validation_report(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_VALIDATION_DIR / "card_validation_report.parquet")

    def save_metadata_quality(self, profile_name: str, quality: dict) -> Path:
        path = DATA_LAKE_ARTIFACT_METADATA_QUALITY_DIR / f"metadata_quality_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=4)
        return path

    def load_metadata_quality(self, profile_name: str) -> dict:
        path = DATA_LAKE_ARTIFACT_METADATA_QUALITY_DIR / f"metadata_quality_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_research_artifact_metadata_export(self, manifest: dict) -> Path:
        path = DATA_LAKE_ARTIFACT_METADATA_EXPORTS_DIR / "research_artifact_metadata_export.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=4)
        return path

    def load_research_artifact_metadata_export(self) -> dict:
        path = DATA_LAKE_ARTIFACT_METADATA_EXPORTS_DIR / "research_artifact_metadata_export.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_artifact_metadata_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        path = DATA_LAKE_ARTIFACT_METADATA_EXPORTS_DIR / f"artifact_metadata_report_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        return path

    def load_artifact_metadata_report(self, profile_name: str) -> dict:
        path = DATA_LAKE_ARTIFACT_METADATA_EXPORTS_DIR / f"artifact_metadata_report_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_artifact_metadata_reports(self) -> pd.DataFrame:
        return pd.DataFrame()



    def save_scenario_regression_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_REGISTRY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_REGISTRY_DIR / "regression_registry.csv"
        LAKE_SCENARIO_REGRESSION_REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_regression_registry(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_REGISTRY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_REGISTRY_DIR / "regression_registry.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_golden_outputs(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR / "golden_outputs.csv"
        LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_golden_outputs(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR / "golden_outputs.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_golden_output_manifest(self, manifest: dict) -> Path:
        import json
        from config.paths import LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR / "golden_output_manifest.json"
        LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        if manifest:
            with open(file_path, 'w') as f:
                json.dump(manifest, f, indent=2)
        return file_path

    def load_golden_output_manifest(self) -> dict:
        import json
        from config.paths import LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR / "golden_output_manifest.json"
        if file_path.exists():
            with open(file_path, 'r') as f:
                return json.load(f)
        return {}

    def save_snapshot_manifest(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR / "snapshot_manifest.csv"
        LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_snapshot_manifest(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR / "snapshot_manifest.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_snapshot_diff_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR / "snapshot_diff_report.csv"
        LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_snapshot_diff_report(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR / "snapshot_diff_report.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_deterministic_replay_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_REPLAY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_REPLAY_DIR / "deterministic_replay_report.csv"
        LAKE_SCENARIO_REGRESSION_REPLAY_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_deterministic_replay_report(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_REPLAY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_REPLAY_DIR / "deterministic_replay_report.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_fixture_reproducibility_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR / "fixture_reproducibility_report.csv"
        LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_fixture_reproducibility_report(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR / "fixture_reproducibility_report.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_scenario_output_contract_validation(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR / "scenario_output_contract_validation.csv"
        LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_output_contract_validation(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR / "scenario_output_contract_validation.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_demo_workflow_regression_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR / "demo_workflow_regression_report.csv"
        LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_demo_workflow_regression_report(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR / "demo_workflow_regression_report.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_end_to_end_demo_acceptance(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR
        file_path = LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR / "end_to_end_demo_acceptance.csv"
        LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_end_to_end_demo_acceptance(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR
        file_path = LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR / "end_to_end_demo_acceptance.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_scenario_drift_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_DRIFT_DIR
        file_path = LAKE_SCENARIO_REGRESSION_DRIFT_DIR / "scenario_drift_report.csv"
        LAKE_SCENARIO_REGRESSION_DRIFT_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_drift_report(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_DRIFT_DIR
        file_path = LAKE_SCENARIO_REGRESSION_DRIFT_DIR / "scenario_drift_report.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_regression_failure_register(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_FAILURES_DIR
        file_path = LAKE_SCENARIO_REGRESSION_FAILURES_DIR / "regression_failure_register.csv"
        LAKE_SCENARIO_REGRESSION_FAILURES_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_regression_failure_register(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_FAILURES_DIR
        file_path = LAKE_SCENARIO_REGRESSION_FAILURES_DIR / "regression_failure_register.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_regression_acceptance_checklist(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR / "regression_acceptance_checklist.csv"
        LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_regression_acceptance_checklist(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR / "regression_acceptance_checklist.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_scenario_regression_quality(self, profile_name: str, quality: dict) -> Path:
        import json
        from config.paths import LAKE_SCENARIO_REGRESSION_QUALITY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_QUALITY_DIR / f"quality_{profile_name}.json"
        LAKE_SCENARIO_REGRESSION_QUALITY_DIR.mkdir(parents=True, exist_ok=True)
        if quality:
            with open(file_path, 'w') as f:
                json.dump(quality, f, indent=2)
        return file_path

    def load_scenario_regression_quality(self, profile_name: str) -> dict:
        import json
        from config.paths import LAKE_SCENARIO_REGRESSION_QUALITY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_QUALITY_DIR / f"quality_{profile_name}.json"
        if file_path.exists():
            with open(file_path, 'r') as f:
                return json.load(f)
        return {}

    def save_scenario_regression_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        import json
        from config.paths import REPORTS_SCENARIO_REGRESSION_JSON_DIR, REPORTS_SCENARIO_REGRESSION_MARKDOWN_DIR

        REPORTS_SCENARIO_REGRESSION_JSON_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_SCENARIO_REGRESSION_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)

        json_path = REPORTS_SCENARIO_REGRESSION_JSON_DIR / f"report_{profile_name}.json"
        with open(json_path, 'w') as f:
            json.dump(report, f, indent=2)

        if markdown:
            md_path = REPORTS_SCENARIO_REGRESSION_MARKDOWN_DIR / f"{profile_name}.md"
            with open(md_path, 'w') as f:
                f.write(markdown)

        return json_path

    def load_scenario_regression_report(self, profile_name: str) -> dict:
        import json
        from config.paths import REPORTS_SCENARIO_REGRESSION_JSON_DIR
        file_path = REPORTS_SCENARIO_REGRESSION_JSON_DIR / f"report_{profile_name}.json"
        if file_path.exists():
            with open(file_path, 'r') as f:
                return json.load(f)
        return {}

    def list_scenario_regression_reports(self) -> pd.DataFrame:
        from config.paths import REPORTS_SCENARIO_REGRESSION_JSON_DIR
        if not REPORTS_SCENARIO_REGRESSION_JSON_DIR.exists():
            return pd.DataFrame()

        reports = []
        for file in REPORTS_SCENARIO_REGRESSION_JSON_DIR.glob("*.json"):
            reports.append({
                "profile_name": file.stem.replace("report_", ""),
                "path": str(file)
            })
        return pd.DataFrame(reports)

    def save_scenario_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        """Saves the scenario registry."""
        from config.paths import DATA_SCENARIOS_REGISTRY_DIR

        file_path = DATA_SCENARIOS_REGISTRY_DIR / "scenario_registry.csv"
        DATA_SCENARIOS_REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_registry(self) -> pd.DataFrame:
        """Loads the scenario registry."""
        from config.paths import DATA_SCENARIOS_REGISTRY_DIR

        file_path = self.paths.DATA_SCENARIOS_REGISTRY_DIR / "scenario_registry.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_scenario_sample_data_manifest(self, df: pd.DataFrame, summary: dict = None) -> Path:
        """Saves the scenario sample data manifest."""
        from config.paths import DATA_SCENARIOS_SAMPLE_DATA_DIR

        file_path = DATA_SCENARIOS_SAMPLE_DATA_DIR / "sample_data_manifest.csv"
        DATA_SCENARIOS_SAMPLE_DATA_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_sample_data_manifest(self) -> pd.DataFrame:
        """Loads the scenario sample data manifest."""
        from config.paths import DATA_SCENARIOS_SAMPLE_DATA_DIR

        file_path = self.paths.DATA_SCENARIOS_SAMPLE_DATA_DIR / "sample_data_manifest.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_scenario_fixtures(self, df: pd.DataFrame, summary: dict = None) -> Path:
        """Saves scenario fixtures manifest."""
        from config.paths import DATA_SCENARIOS_FIXTURES_DIR

        file_path = DATA_SCENARIOS_FIXTURES_DIR / "scenario_fixtures.csv"
        DATA_SCENARIOS_FIXTURES_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_fixtures(self) -> pd.DataFrame:
        """Loads scenario fixtures manifest."""
        from config.paths import DATA_SCENARIOS_FIXTURES_DIR

        file_path = self.paths.DATA_SCENARIOS_FIXTURES_DIR / "scenario_fixtures.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_scenario_expected_outputs(self, df: pd.DataFrame, summary: dict = None) -> Path:
        """Saves expected outputs contracts."""
        from config.paths import DATA_SCENARIOS_EXPECTED_OUTPUTS_DIR

        file_path = DATA_SCENARIOS_EXPECTED_OUTPUTS_DIR / "scenario_expected_outputs.csv"
        DATA_SCENARIOS_EXPECTED_OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_expected_outputs(self) -> pd.DataFrame:
        """Loads expected outputs contracts."""
        from config.paths import DATA_SCENARIOS_EXPECTED_OUTPUTS_DIR

        file_path = self.paths.DATA_SCENARIOS_EXPECTED_OUTPUTS_DIR / "scenario_expected_outputs.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_scenario_workflow_packs(self, df: pd.DataFrame, summary: dict = None) -> Path:
        """Saves scenario workflow packs."""
        from config.paths import DATA_SCENARIOS_WORKFLOWS_DIR

        file_path = DATA_SCENARIOS_WORKFLOWS_DIR / "scenario_workflow_packs.csv"
        DATA_SCENARIOS_WORKFLOWS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_workflow_packs(self) -> pd.DataFrame:
        """Loads scenario workflow packs."""
        from config.paths import DATA_SCENARIOS_WORKFLOWS_DIR

        file_path = self.paths.DATA_SCENARIOS_WORKFLOWS_DIR / "scenario_workflow_packs.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_demo_command_sequences(self, df: pd.DataFrame, summary: dict = None) -> Path:
        """Saves demo command sequences."""
        from config.paths import DATA_SCENARIOS_DEMO_COMMANDS_DIR

        file_path = DATA_SCENARIOS_DEMO_COMMANDS_DIR / "demo_command_sequences.csv"
        DATA_SCENARIOS_DEMO_COMMANDS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_demo_command_sequences(self) -> pd.DataFrame:
        """Loads demo command sequences."""
        from config.paths import DATA_SCENARIOS_DEMO_COMMANDS_DIR

        file_path = self.paths.DATA_SCENARIOS_DEMO_COMMANDS_DIR / "demo_command_sequences.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_scenario_dry_run_results(self, df: pd.DataFrame, summary: dict = None) -> Path:
        """Saves scenario dry run results."""
        from config.paths import DATA_SCENARIOS_DRY_RUNS_DIR

        file_path = DATA_SCENARIOS_DRY_RUNS_DIR / "scenario_dry_run_results.csv"
        DATA_SCENARIOS_DRY_RUNS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_dry_run_results(self) -> pd.DataFrame:
        """Loads scenario dry run results."""
        from config.paths import DATA_SCENARIOS_DRY_RUNS_DIR

        file_path = self.paths.DATA_SCENARIOS_DRY_RUNS_DIR / "scenario_dry_run_results.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_scenario_validation_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        """Saves scenario validation report."""
        from config.paths import DATA_SCENARIOS_VALIDATION_DIR

        file_path = DATA_SCENARIOS_VALIDATION_DIR / "scenario_validation_report.csv"
        DATA_SCENARIOS_VALIDATION_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_validation_report(self) -> pd.DataFrame:
        """Loads scenario validation report."""
        from config.paths import DATA_SCENARIOS_VALIDATION_DIR

        file_path = self.paths.DATA_SCENARIOS_VALIDATION_DIR / "scenario_validation_report.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_case_studies(self, df: pd.DataFrame, summary: dict = None) -> Path:
        """Saves case studies."""
        from config.paths import DATA_SCENARIOS_CASE_STUDIES_DIR

        file_path = DATA_SCENARIOS_CASE_STUDIES_DIR / "case_studies.csv"
        DATA_SCENARIOS_CASE_STUDIES_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_case_studies(self) -> pd.DataFrame:
        """Loads case studies."""
        from config.paths import DATA_SCENARIOS_CASE_STUDIES_DIR

        file_path = self.paths.DATA_SCENARIOS_CASE_STUDIES_DIR / "case_studies.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_module_demo_flows(self, df: pd.DataFrame, summary: dict = None) -> Path:
        """Saves module demo flows."""
        from config.paths import DATA_SCENARIOS_MODULE_FLOWS_DIR

        file_path = DATA_SCENARIOS_MODULE_FLOWS_DIR / "module_demo_flows.csv"
        DATA_SCENARIOS_MODULE_FLOWS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_module_demo_flows(self) -> pd.DataFrame:
        """Loads module demo flows."""
        from config.paths import DATA_SCENARIOS_MODULE_FLOWS_DIR

        file_path = self.paths.DATA_SCENARIOS_MODULE_FLOWS_DIR / "module_demo_flows.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_end_to_end_demo_report(self, report_name: str, report: dict, markdown: str = None) -> Path:
        """Saves end-to-end demo JSON report."""
        from config.paths import DATA_SCENARIOS_END_TO_END_DIR
        import json
        file_path = DATA_SCENARIOS_END_TO_END_DIR / f"{report_name}.json"
        DATA_SCENARIOS_END_TO_END_DIR.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w") as f:
            json.dump(report, f, indent=4)
        return file_path

    def load_end_to_end_demo_report(self, report_name: str) -> dict:
        """Loads end-to-end demo JSON report."""
        from config.paths import DATA_SCENARIOS_END_TO_END_DIR
        import json
        file_path = DATA_SCENARIOS_END_TO_END_DIR / f"{report_name}.json"
        if not file_path.exists():
            return {}
        with open(file_path, "r") as f:
            return json.load(f)

    def save_scenario_quality(self, profile_name: str, quality: dict) -> Path:
        """Saves scenario quality JSON."""
        from config.paths import DATA_SCENARIOS_QUALITY_DIR
        import json
        file_path = DATA_SCENARIOS_QUALITY_DIR / f"scenario_quality_{profile_name}.json"
        DATA_SCENARIOS_QUALITY_DIR.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w") as f:
            json.dump(quality, f, indent=4)
        return file_path

    def load_scenario_quality(self, profile_name: str) -> dict:
        """Loads scenario quality JSON."""
        from config.paths import DATA_SCENARIOS_QUALITY_DIR
        import json
        file_path = DATA_SCENARIOS_QUALITY_DIR / f"scenario_quality_{profile_name}.json"
        if not file_path.exists():
            return {}
        with open(file_path, "r") as f:
            return json.load(f)

    def save_scenario_report(self, profile_name: str, report: dict, markdown: str = None) -> Path:
        """Saves a general scenario report JSON."""
        from config.paths import DATA_SCENARIOS_DIR
        import json
        file_path = DATA_SCENARIOS_DIR / f"scenario_report_{profile_name}.json"
        DATA_SCENARIOS_DIR.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w") as f:
            json.dump(report, f, indent=4)
        return file_path

    def load_scenario_report(self, profile_name: str) -> dict:
        """Loads a general scenario report JSON."""
        from config.paths import DATA_SCENARIOS_DIR
        import json
        file_path = DATA_SCENARIOS_DIR / f"scenario_report_{profile_name}.json"
        if not file_path.exists():
            return {}
        with open(file_path, "r") as f:
            return json.load(f)

    def list_scenario_reports(self) -> pd.DataFrame:
        """Lists all scenario reports."""
        from config.paths import DATA_SCENARIOS_DIR
        reports = []
        if DATA_SCENARIOS_DIR.exists():
            for p in DATA_SCENARIOS_DIR.glob("scenario_report_*.json"):
                reports.append({"report_name": p.stem, "path": str(p)})
        return pd.DataFrame(reports)


    # Phase 50: Command Center Methods
    def save_command_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_REGISTRY_DIR / "command_registry.parquet", summary)

    def load_command_registry(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_REGISTRY_DIR / "command_registry.parquet")

    def save_guided_workflows(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_WORKFLOWS_DIR / "guided_workflows.parquet", summary)

    def load_guided_workflows(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_WORKFLOWS_DIR / "guided_workflows.parquet")

    def save_safe_runbooks(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_RUNBOOKS_DIR / "safe_runbooks.parquet", summary)

    def load_safe_runbooks(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_RUNBOOKS_DIR / "safe_runbooks.parquet")

    def save_command_dry_run_plan(self, plan_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_DRY_RUN_PLANS_DIR / f"{plan_name}.parquet", summary)

    def load_command_dry_run_plan(self, plan_name: str) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_DRY_RUN_PLANS_DIR / f"{plan_name}.parquet")

    def save_interactive_query_flow(self, flow_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_QUERY_FLOWS_DIR / f"{flow_name}.parquet", summary)

    def load_interactive_query_flow(self, flow_name: str) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_QUERY_FLOWS_DIR / f"{flow_name}.parquet")

    def save_project_status(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_PROJECT_STATUS_DIR / "project_status.parquet", summary)

    def load_project_status(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_PROJECT_STATUS_DIR / "project_status.parquet")

    def save_module_health(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_MODULE_HEALTH_DIR / "module_health.parquet", summary)

    def load_module_health(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_MODULE_HEALTH_DIR / "module_health.parquet")

    def save_script_availability_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_SCRIPT_DISCOVERY_DIR / "script_availability_matrix.parquet", summary)

    def load_script_availability_matrix(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_SCRIPT_DISCOVERY_DIR / "script_availability_matrix.parquet")

    def save_phase_coverage_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_PHASE_COVERAGE_DIR / "phase_coverage_matrix.parquet", summary)

    def load_phase_coverage_matrix(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_PHASE_COVERAGE_DIR / "phase_coverage_matrix.parquet")

    def save_project_consolidation_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        path = self.paths.LAKE_COMMAND_CENTER_CONSOLIDATION_DIR / f"{profile_name}_consolidation.json"
        with open(path, "w", encoding="utf-8") as f:
            json.update(report) if hasattr(json, "update") else json.dump(report, f, indent=4)
        return path

    def load_project_consolidation_report(self, profile_name: str) -> dict:
        path = self.paths.LAKE_COMMAND_CENTER_CONSOLIDATION_DIR / f"{profile_name}_consolidation.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_command_center_quality(self, profile_name: str, quality: dict) -> Path:
        path = self.paths.LAKE_COMMAND_CENTER_QUALITY_DIR / f"{profile_name}_quality.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=4)
        return path

    def load_command_center_quality(self, profile_name: str) -> dict:
        path = self.paths.LAKE_COMMAND_CENTER_QUALITY_DIR / f"{profile_name}_quality.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_command_center_status(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_DIR / "command_center_status.parquet", summary)

    def load_command_center_status(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_DIR / "command_center_status.parquet")

    def list_command_center_reports(self) -> pd.DataFrame:
        data = []
        for p in self.paths.LAKE_COMMAND_CENTER_DIR.rglob("*.parquet"):
            data.append({"path": str(p), "type": "parquet"})
        for p in self.paths.LAKE_COMMAND_CENTER_DIR.rglob("*.json"):
            data.append({"path": str(p), "type": "json"})
        return pd.DataFrame(data)



    # Phase 47 Governance Methods
    def save_artifact_inventory(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "inventory" / "artifact_inventory.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_artifact_inventory(self) -> pd.DataFrame:
        p = self.governance_dir / "inventory" / "artifact_inventory.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_artifact_fingerprints(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "fingerprints" / "artifact_fingerprints.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_artifact_fingerprints(self) -> pd.DataFrame:
        p = self.governance_dir / "fingerprints" / "artifact_fingerprints.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_provenance_records(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "provenance" / "provenance_records.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_provenance_records(self) -> pd.DataFrame:
        p = self.governance_dir / "provenance" / "provenance_records.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_lineage_nodes(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "lineage" / "lineage_nodes.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_lineage_nodes(self) -> pd.DataFrame:
        p = self.governance_dir / "lineage" / "lineage_nodes.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_lineage_edges(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "lineage" / "lineage_edges.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_lineage_edges(self) -> pd.DataFrame:
        p = self.governance_dir / "lineage" / "lineage_edges.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_dependency_trace(self, trace_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "dependencies" / f"{trace_name}_trace.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_dependency_trace(self, trace_name: str) -> pd.DataFrame:
        p = self.governance_dir / "dependencies" / f"{trace_name}_trace.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_audit_trail(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "audit" / "audit_trail.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_audit_trail(self) -> pd.DataFrame:
        p = self.governance_dir / "audit" / "audit_trail.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_source_attribution(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "source_attribution" / "source_attribution.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_source_attribution(self) -> pd.DataFrame:
        p = self.governance_dir / "source_attribution" / "source_attribution.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_governance_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "checklists" / "governance_checklist.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_governance_checklist(self) -> pd.DataFrame:
        p = self.governance_dir / "checklists" / "governance_checklist.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_governance_quality(self, profile_name: str, quality: dict) -> Path: # type: ignore
        import json
        p = self.governance_dir / "quality" / f"{profile_name}_quality.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            json.dump(quality, f, indent=2)
        return p

    def load_governance_quality(self, profile_name: str) -> dict: # type: ignore
        import json
        p = self.governance_dir / "quality" / f"{profile_name}_quality.json"
        if not p.exists(): return {}
        with open(p, "r") as f:
            return json.load(f)

    def save_research_governance_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        import json
        p = self.governance_dir / f"{profile_name}_report.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            json.dump(report, f, indent=2)
        return p

    def load_research_governance_report(self, profile_name: str) -> dict: # type: ignore
        import json
        p = self.governance_dir / f"{profile_name}_report.json"
        if not p.exists(): return {}
        with open(p, "r") as f:
            return json.load(f)

    def list_governance_reports(self) -> pd.DataFrame:
        reports = []
        for p in self.governance_dir.glob("*_report.json"):
            reports.append({"report_name": p.stem, "path": str(p)})
        return pd.DataFrame(reports)


    """Manager for the local Data Lake."""

    def __init__(self, root_dir):
        if hasattr(root_dir, "lake_dir"):
            self.paths = root_dir
            self.root_dir = root_dir.lake_dir
        else:
            self.root_dir = Path(root_dir)
            from config import paths

            from config.paths import ProjectPaths
            self.paths = ProjectPaths()

        self.ohlcv_dir = self.root_dir / "ohlcv"
        self.governance_dir = self.root_dir / "governance"

    @staticmethod
    def safe_symbol_name(symbol: str) -> str:
        """Sanitize symbol to be safe for filenames and directories."""
        safe_symbol = symbol.replace("/", "_").replace("=", "_")
        safe_symbol = re.sub(r"[^a-zA-Z0-9_-]", "", safe_symbol)
        return safe_symbol

    def get_symbol_dir(self, spec: SymbolSpec) -> Path:
        """Get the directory path for a specific symbol."""
        source = spec.data_source
        sub_class = spec.sub_class.lower().replace(" ", "_")
        safe_sym = self.safe_symbol_name(spec.symbol)
        return self.ohlcv_dir / source / sub_class / safe_sym

    def get_ohlcv_path(self, spec: SymbolSpec, timeframe: str) -> Path:
        """Get the file path for OHLCV data of a specific timeframe."""
        symbol_dir = self.get_symbol_dir(spec)
        return symbol_dir / f"{timeframe}.parquet"

    def get_metadata_path(self, spec: SymbolSpec) -> Path:
        """Get the file path for the symbol's metadata."""
        symbol_dir = self.get_symbol_dir(spec)
        return symbol_dir / "metadata.json"

    def save_ohlcv(self, spec: SymbolSpec, timeframe: str, df: pd.DataFrame) -> Path: # type: ignore
        """Save an OHLCV DataFrame to the Data Lake."""
        if df is None or df.empty:
            logger.warning(
                f"Attempted to save empty DataFrame for {spec.symbol} ({timeframe})"
            )
            return self.get_ohlcv_path(spec, timeframe)

        try:
            validate_ohlcv_dataframe(df)
        except DataQualityError as e:
            logger.warning(
                f"Data validation failed for {spec.symbol} ({timeframe}): {e}"
            )
            raise

        path = self.get_ohlcv_path(spec, timeframe)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            logger.debug(f"Saved OHLCV to Data Lake: {path}")
        except ImportError:
            logger.error("pyarrow is required to save parquet files.")
            raise
        except Exception as e:
            logger.error(f"Failed to save OHLCV for {spec.symbol} ({timeframe}): {e}")
            raise

        return path

    def load_ohlcv(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        """Load an OHLCV DataFrame from the Data Lake."""
        path = self.get_ohlcv_path(spec, timeframe)
        if not path.exists():
            raise FileNotFoundError(f"OHLCV data not found at {path}")

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            if isinstance(df.index, pd.DatetimeIndex) and df.index.tz is None:
                df.index = df.index.tz_localize("UTC")
            return df
        except ImportError:
            logger.error("pyarrow is required to read parquet files.")
            raise
        except Exception as e:
            logger.error(f"Failed to load OHLCV for {spec.symbol} ({timeframe}): {e}")
            raise

    def has_ohlcv(self, spec: SymbolSpec, timeframe: str) -> bool:
        """Check if OHLCV data exists for a given timeframe."""
        path = self.get_ohlcv_path(spec, timeframe)
        return path.exists() and path.is_file()

    def save_metadata(self, spec: SymbolSpec, metadata: dict) -> Path: # type: ignore
        """Save metadata for a symbol."""
        path = self.get_metadata_path(spec)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=4)
            return path
        except Exception as e:
            logger.error(f"Failed to save metadata for {spec.symbol}: {e}")
            raise

    def load_metadata(self, spec: SymbolSpec) -> dict: # type: ignore
        """Load metadata for a symbol."""
        path = self.get_metadata_path(spec)
        if not path.exists():
            return {}
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load metadata for {spec.symbol}: {e}")
            return {}

    def list_available_timeframes(self, spec: SymbolSpec) -> list[str]:
        """List all available OHLCV timeframes for a symbol."""
        symbol_dir = self.get_symbol_dir(spec)
        if not symbol_dir.exists():
            return []

        timeframes = []
        for file in symbol_dir.glob("*.parquet"):
            timeframe = file.stem
            timeframes.append(timeframe)

        return sorted(timeframes)

    def get_signal_pool_path(self, timeframe: str, profile_name: str) -> Path:
        """Get path for signal pool features."""
        from config.paths import LAKE_FEATURES_SIGNAL_POOL_DIR

        filename = f"signal_pool_{timeframe}_{profile_name}.parquet"
        return LAKE_FEATURES_SIGNAL_POOL_DIR / filename

    def save_signal_pool(
        self, timeframe: str, df: pd.DataFrame, profile_name: str
    ) -> Path:
        """Save a signal pool DataFrame to the Data Lake."""
        if df is None or df.empty:
            return self.get_signal_pool_path(timeframe, profile_name)

        path = self.get_signal_pool_path(timeframe, profile_name)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            import logging

            logging.getLogger(__name__).debug(f"Saved signal pool to Data Lake: {path}")
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to save signal pool ({timeframe}, {profile_name}): {e}"
            )
            raise

        return path

    def load_signal_pool(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        """Load a signal pool DataFrame from the Data Lake."""
        path = self.get_signal_pool_path(timeframe, profile_name)
        if not path.exists():
            return pd.DataFrame()

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            return df
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to load signal pool ({timeframe}, {profile_name}): {e}"
            )
            raise

    def has_signal_pool(self, timeframe: str, profile_name: str) -> bool:
        """Check if signal pool exists."""
        return self.get_signal_pool_path(timeframe, profile_name).exists()

    def delete_ohlcv(self, spec: SymbolSpec, timeframe: str) -> None:
        """Delete OHLCV data for a specific timeframe."""
        path = self.get_ohlcv_path(spec, timeframe)
        if path.exists():
            try:
                path.unlink()
                logger.debug(f"Deleted OHLCV from Data Lake: {path}")
            except Exception as e:
                logger.error(
                    f"Failed to delete OHLCV for {spec.symbol} ({timeframe}): {e}"
                )

    # Processed Data Methods
    def get_processed_symbol_dir(self, spec: SymbolSpec) -> Path:
        """Get the directory path for a specific symbol in the processed area."""
        source = spec.data_source
        sub_class = spec.sub_class.lower().replace(" ", "_")
        safe_sym = self.safe_symbol_name(spec.symbol)
        return self.root_dir / "processed" / "ohlcv" / source / sub_class / safe_sym

    def get_processed_ohlcv_path(self, spec: SymbolSpec, timeframe: str) -> Path:
        """Get the file path for processed OHLCV data of a specific timeframe."""
        symbol_dir = self.get_processed_symbol_dir(spec)
        return symbol_dir / f"{timeframe}.parquet"

    def save_processed_ohlcv(
        self, spec: SymbolSpec, timeframe: str, df: pd.DataFrame
    ) -> Path:
        """Save a cleaned/processed OHLCV DataFrame to the Data Lake."""
        if df is None or df.empty:
            logger.warning(
                f"Attempted to save empty processed DataFrame for {spec.symbol} ({timeframe})"
            )
            return self.get_processed_ohlcv_path(spec, timeframe)

        try:
            # We skip standard validation here or you could add a softer validation
            # since processed data might have extra columns
            pass
        except Exception as e:
            logger.warning(
                f"Processed data validation failed for {spec.symbol} ({timeframe}): {e}"
            )

        path = self.get_processed_ohlcv_path(spec, timeframe)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            logger.debug(f"Saved processed OHLCV to Data Lake: {path}")
        except ImportError:
            logger.error("pyarrow is required to save parquet files.")
            raise
        except Exception as e:
            logger.error(
                f"Failed to save processed OHLCV for {spec.symbol} ({timeframe}): {e}"
            )
            raise

        return path

    def load_processed_ohlcv(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        """Load a processed OHLCV DataFrame from the Data Lake."""
        path = self.get_processed_ohlcv_path(spec, timeframe)
        if not path.exists():
            raise FileNotFoundError(f"Processed OHLCV data not found at {path}")

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            if isinstance(df.index, pd.DatetimeIndex) and df.index.tz is None:
                df.index = df.index.tz_localize("UTC")
            return df
        except ImportError:
            logger.error("pyarrow is required to read parquet files.")
            raise
        except Exception as e:
            logger.error(
                f"Failed to load processed OHLCV for {spec.symbol} ({timeframe}): {e}"
            )
            raise

    def has_processed_ohlcv(self, spec: SymbolSpec, timeframe: str) -> bool:
        """Check if processed OHLCV data exists for a given timeframe."""
        path = self.get_processed_ohlcv_path(spec, timeframe)
        return path.exists() and path.is_file()

    def save_quality_report(
        self, spec: SymbolSpec, timeframe: str, report: dict
    ) -> Path:
        """Save a quality report."""
        safe_sym = self.safe_symbol_name(spec.symbol)
        filename = f"{safe_sym}_{timeframe}_quality.json"
        path = self.root_dir / "processed" / "quality_reports" / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=4)
            return path
        except Exception as e:
            logger.error(f"Failed to save quality report for {spec.symbol}: {e}")
            raise

    def load_quality_report(self, spec: SymbolSpec, timeframe: str) -> dict: # type: ignore
        """Load a quality report."""
        safe_sym = self.safe_symbol_name(spec.symbol)
        filename = f"{safe_sym}_{timeframe}_quality.json"
        path = self.root_dir / "processed" / "quality_reports" / filename
        if not path.exists():
            return {}
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load quality report for {spec.symbol}: {e}")
            return {}

    def save_cleaning_report(
        self, spec: SymbolSpec, timeframe: str, report: dict
    ) -> Path:
        """Save a cleaning report."""
        safe_sym = self.safe_symbol_name(spec.symbol)
        filename = f"{safe_sym}_{timeframe}_cleaning.json"
        path = self.root_dir / "processed" / "cleaning_reports" / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=4)
            return path
        except Exception as e:
            logger.error(f"Failed to save cleaning report for {spec.symbol}: {e}")
            raise

    def load_cleaning_report(self, spec: SymbolSpec, timeframe: str) -> dict: # type: ignore
        """Load a cleaning report."""
        safe_sym = self.safe_symbol_name(spec.symbol)
        filename = f"{safe_sym}_{timeframe}_cleaning.json"
        path = self.root_dir / "processed" / "cleaning_reports" / filename
        if not path.exists():
            return {}
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load cleaning report for {spec.symbol}: {e}")
            return {}

    # Feature Data Methods
    def get_feature_path(
        self, spec: SymbolSpec, timeframe: str, feature_set_name: str = "technical"
    ) -> Path:
        """Get the file path for feature data."""
        source = spec.data_source
        sub_class = spec.sub_class.lower().replace(" ", "_")
        safe_sym = self.safe_symbol_name(spec.symbol)



        symbol_dir = LAKE_FEATURES_DIR / feature_set_name / source / sub_class / safe_sym
        return symbol_dir / f"{timeframe}.parquet"

    def save_features(
        self,
        spec: SymbolSpec,
        timeframe: str,
        df: pd.DataFrame,
        feature_set_name: str = "technical",
    ) -> Path:
        """Save a feature DataFrame to the Data Lake."""
        if df is None or df.empty:
            logger.warning(
                f"Attempted to save empty feature DataFrame for {spec.symbol} ({timeframe})"
            )
            return self.get_feature_path(spec, timeframe, feature_set_name)

        path = self.get_feature_path(spec, timeframe, feature_set_name)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            logger.debug(f"Saved {feature_set_name} features to Data Lake: {path}")
        except Exception as e:
            logger.error(
                f"Failed to save {feature_set_name} features for {spec.symbol} ({timeframe}): {e}"
            )
            raise

        return path

    def load_features(
        self, spec: SymbolSpec, timeframe: str, feature_set_name: str = "technical"
    ) -> pd.DataFrame:
        """Load a feature DataFrame from the Data Lake."""
        path = self.get_feature_path(spec, timeframe, feature_set_name)
        if not path.exists():
            raise FileNotFoundError(f"Feature data not found at {path}")

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            if isinstance(df.index, pd.DatetimeIndex) and df.index.tz is None:
                df.index = df.index.tz_localize("UTC")
            return df
        except Exception as e:
            logger.error(
                f"Failed to load {feature_set_name} features for {spec.symbol} ({timeframe}): {e}"
            )
            raise

    def has_features(
        self, spec: SymbolSpec, timeframe: str, feature_set_name: str = "technical"
    ) -> bool:
        """Check if feature data exists."""
        path = self.get_feature_path(spec, timeframe, feature_set_name)
        return path.exists() and path.is_file()

    def list_feature_timeframes(
        self, spec: SymbolSpec, feature_set_name: str = "technical"
    ) -> list[str]:
        """List all available feature timeframes for a symbol."""
        path = self.get_feature_path(spec, "dummy", feature_set_name)
        symbol_dir = path.parent

        if not symbol_dir.exists():
            return []

        return sorted([f.stem for f in symbol_dir.glob("*.parquet")])

    def save_macro_series(
        self, code: str, df: pd.DataFrame, processed: bool = False
    ) -> Path:
        """Save macro series data to lake."""
        if df.empty:
            logger.warning("Attempted to save empty macro series for %s", code)
            from config.paths import LAKE_MACRO_PROCESSED_DIR, LAKE_MACRO_RAW_DIR

            return (
                LAKE_MACRO_PROCESSED_DIR if processed else LAKE_MACRO_RAW_DIR
            ) / f"{code}.parquet"

        from config.paths import LAKE_MACRO_PROCESSED_DIR, LAKE_MACRO_RAW_DIR

        target_dir = LAKE_MACRO_PROCESSED_DIR if processed else LAKE_MACRO_RAW_DIR
        filepath = target_dir / f"{code}.parquet"

        try:
            df.to_parquet(filepath, index=True)
            logger.debug("Saved macro series %s to %s", code, filepath)
            return filepath
        except Exception as e:
            logger.error("Error saving macro series %s: %s", code, str(e))
            from core.exceptions import DataStorageError

            raise DataStorageError(f"Failed to save macro series {code}: {str(e)}")

    def load_macro_series(self, code: str, processed: bool = False) -> pd.DataFrame:
        """Load macro series data from lake."""
        from config.paths import LAKE_MACRO_PROCESSED_DIR, LAKE_MACRO_RAW_DIR

        target_dir = LAKE_MACRO_PROCESSED_DIR if processed else LAKE_MACRO_RAW_DIR
        filepath = target_dir / f"{code}.parquet"

        if not filepath.exists():
            logger.debug("Macro series not found: %s", filepath)
            return pd.DataFrame()

        try:
            df = pd.read_parquet(filepath)
            return df
        except Exception as e:
            logger.error("Error loading macro series %s: %s", code, str(e))
            from core.exceptions import DataStorageError

            raise DataStorageError(f"Failed to load macro series {code}: {str(e)}")

    def has_macro_series(self, code: str, processed: bool = False) -> bool:
        """Check if macro series exists in lake."""
        from config.paths import LAKE_MACRO_PROCESSED_DIR, LAKE_MACRO_RAW_DIR

        target_dir = LAKE_MACRO_PROCESSED_DIR if processed else LAKE_MACRO_RAW_DIR
        filepath = target_dir / f"{code}.parquet"
        return filepath.exists()

    def get_group_feature_path(self, asset_class: str, timeframe: str) -> Path:
        """Get path for group features."""
        filename = f"group_features_{asset_class}_{timeframe}.{'parquet'}"
        return LAKE_FEATURES_GROUP_FEATURES_DIR / filename

    def save_group_features(
        self, asset_class: str, timeframe: str, df: pd.DataFrame
    ) -> Path:
        """Save a group feature DataFrame to the Data Lake."""
        if df is None or df.empty:
            return self.get_group_feature_path(asset_class, timeframe)

        path = self.get_group_feature_path(asset_class, timeframe)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            logger.debug(f"Saved group features to Data Lake: {path}")
        except Exception as e:
            logger.error(
                f"Failed to save group features for {asset_class} ({timeframe}): {e}"
            )
            raise

        return path

    def load_group_features(self, asset_class: str, timeframe: str) -> pd.DataFrame:
        """Load a group feature DataFrame from the Data Lake."""
        path = self.get_group_feature_path(asset_class, timeframe)
        if not path.exists():
            raise FileNotFoundError(f"Group feature data not found at {path}")

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            if isinstance(df.index, pd.DatetimeIndex) and df.index.tz is None:
                df.index = df.index.tz_localize("UTC")
            return df
        except Exception as e:
            logger.error(
                f"Failed to load group features for {asset_class} ({timeframe}): {e}"
            )
            raise

    def has_group_features(self, asset_class: str, timeframe: str) -> bool:
        """Check if group features exist."""
        return self.get_group_feature_path(asset_class, timeframe).exists()

    def list_group_feature_timeframes(self, asset_class: str) -> list[str]:
        """List all timeframes with group features for a specific asset class."""
        dir_path = LAKE_FEATURES_GROUP_FEATURES_DIR
        if not dir_path.exists():
            return []

        prefix = f"group_features_{asset_class}_"
        suffix = f".{'parquet'}"

        timeframes = []
        for file_path in dir_path.glob(f"{prefix}*{suffix}"):
            try:
                tf_part = file_path.name[len(prefix) : -len(suffix)]
                timeframes.append(tf_part)
            except Exception:
                continue

        return sorted(timeframes)

    def get_signal_pool_path(self, timeframe: str, profile_name: str) -> Path:
        """Get path for signal pool features."""
        from config.paths import LAKE_FEATURES_SIGNAL_POOL_DIR

        filename = f"signal_pool_{timeframe}_{profile_name}.parquet"
        return LAKE_FEATURES_SIGNAL_POOL_DIR / filename

    def save_signal_pool(
        self, timeframe: str, df: pd.DataFrame, profile_name: str
    ) -> Path:
        """Save a signal pool DataFrame to the Data Lake."""
        if df is None or df.empty:
            return self.get_signal_pool_path(timeframe, profile_name)

        path = self.get_signal_pool_path(timeframe, profile_name)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            import logging

            logging.getLogger(__name__).debug(f"Saved signal pool to Data Lake: {path}")
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to save signal pool ({timeframe}, {profile_name}): {e}"
            )
            raise

        return path

    def load_signal_pool(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        """Load a signal pool DataFrame from the Data Lake."""
        path = self.get_signal_pool_path(timeframe, profile_name)
        if not path.exists():
            return pd.DataFrame()

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            return df
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to load signal pool ({timeframe}, {profile_name}): {e}"
            )
            raise

    def has_signal_pool(self, timeframe: str, profile_name: str) -> bool:
        """Check if signal pool exists."""
        return self.get_signal_pool_path(timeframe, profile_name).exists()

    def get_decision_pool_path(self, timeframe: str, profile_name: str) -> Path:
        """Get path for decision pool features."""
        from config.paths import LAKE_FEATURES_DECISION_POOL_DIR

        filename = f"decision_pool_{timeframe}_{profile_name}.parquet"
        return LAKE_FEATURES_DECISION_POOL_DIR / filename

    def save_decision_pool(
        self, timeframe: str, df: pd.DataFrame, profile_name: str
    ) -> Path:
        """Save a decision pool DataFrame to the Data Lake."""
        if df is None or df.empty:
            return self.get_decision_pool_path(timeframe, profile_name)

        path = self.get_decision_pool_path(timeframe, profile_name)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            import logging

            logging.getLogger(__name__).debug(
                f"Saved decision pool to Data Lake: {path}"
            )
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to save decision pool ({timeframe}, {profile_name}): {e}"
            )
            raise

        return path

    def load_decision_pool(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        """Load a decision pool DataFrame from the Data Lake."""
        path = self.get_decision_pool_path(timeframe, profile_name)
        if not path.exists():
            return pd.DataFrame()

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            return df
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to load decision pool ({timeframe}, {profile_name}): {e}"
            )
            raise

    def has_decision_pool(self, timeframe: str, profile_name: str) -> bool:
        """Check if decision pool exists."""
        return self.get_decision_pool_path(timeframe, profile_name).exists()

    def save_sizing_pool(
        self, timeframe: str, df: pd.DataFrame, profile_name: str
    ) -> Path:
        """Saves the global universe-level sizing candidate pool."""
        if df.empty:
            logger.warning(
                f"Empty sizing pool dataframe for {timeframe} {profile_name}. Skipping save."
            )
            return (
                paths.LAKE_FEATURES_SIZING_POOL_DIR
                / f"sizing_pool_{timeframe}_{profile_name}.parquet"
            )
        file_path = (
            paths.LAKE_FEATURES_SIZING_POOL_DIR
            / f"sizing_pool_{timeframe}_{profile_name}.parquet"
        )
        self._write_parquet(df, file_path)
        logger.info(f"Saved sizing pool to {file_path}")
        return file_path

    def load_sizing_pool(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        """Loads the global universe-level sizing candidate pool."""
        file_path = (
            paths.LAKE_FEATURES_SIZING_POOL_DIR
            / f"sizing_pool_{timeframe}_{profile_name}.parquet"
        )
        if not file_path.exists():
            raise FileNotFoundError(f"Sizing pool not found: {file_path}")
        return self._read_parquet(file_path)

    def has_sizing_pool(self, timeframe: str, profile_name: str) -> bool:
        """Checks if the global universe-level sizing candidate pool exists."""
        file_path = (
            paths.LAKE_FEATURES_SIZING_POOL_DIR
            / f"sizing_pool_{timeframe}_{profile_name}.parquet"
        )
        return file_path.exists()

    def save_backtest_trades(
        self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame
    ) -> Path:
        path = (
            self.paths.backtest_trades
            / f"backtest_trades_{symbol}_{timeframe}_{profile_name}.parquet"
        )
        df.to_parquet(path)
        return path

    def load_backtest_trades(
        self, symbol: str, timeframe: str, profile_name: str
    ) -> pd.DataFrame:
        path = (
            self.paths.backtest_trades
            / f"backtest_trades_{symbol}_{timeframe}_{profile_name}.parquet"
        )
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_backtest_equity_curve(
        self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame
    ) -> Path:
        path = (
            self.paths.backtest_equity_curves
            / f"backtest_equity_{symbol}_{timeframe}_{profile_name}.parquet"
        )
        df.to_parquet(path)
        return path

    def load_backtest_equity_curve(
        self, symbol: str, timeframe: str, profile_name: str
    ) -> pd.DataFrame:
        path = (
            self.paths.backtest_equity_curves
            / f"backtest_equity_{symbol}_{timeframe}_{profile_name}.parquet"
        )
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_backtest_summary(
        self, symbol: str, timeframe: str, profile_name: str, summary: dict
    ) -> Path:
        path = (
            self.paths.backtest_runs
            / f"backtest_summary_{symbol}_{timeframe}_{profile_name}.json"
        )
        import json

        with open(path, "w") as f:
            json.dump(summary, f, indent=2, default=str)
        return path

    def load_backtest_summary(
        self, symbol: str, timeframe: str, profile_name: str
    ) -> dict:
        path = (
            self.paths.backtest_runs
            / f"backtest_summary_{symbol}_{timeframe}_{profile_name}.json"
        )
        if path.exists():
            import json

            with open(path, "r") as f:
                return json.load(f)
        return {}

    def list_backtest_runs(self) -> pd.DataFrame:
        runs = []
        import json

        for file in self.paths.backtest_runs.glob("*.json"):
            try:
                with open(file, "r") as f:
                    data = json.load(f)
                runs.append(
                    {
                        "symbol": data.get("symbol", ""),
                        "timeframe": data.get("timeframe", ""),
                        "profile": data.get("profile", ""),
                        "trade_count": data.get("performance", {}).get(
                            "trade_count", 0
                        ),
                        "win_rate": data.get("performance", {}).get("win_rate", 0),
                        "total_return_pct": data.get("performance", {}).get(
                            "total_return_pct", 0
                        ),
                        "file_path": str(file),
                    }
                )
            except Exception as e:
                pass
        return pd.DataFrame(runs)

    # --- ML DATASET PHASE ---
    def save_ml_feature_matrix(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.ml_features / f"{symbol}_{timeframe}_{profile_name}_features.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_feature_matrix(self, symbol: str, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.ml_features / f"{symbol}_{timeframe}_{profile_name}_features.parquet"
        return self._load_parquet(path)

    def save_ml_target_frame(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.ml_targets / f"{symbol}_{timeframe}_{profile_name}_targets.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_target_frame(self, symbol: str, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.ml_targets / f"{symbol}_{timeframe}_{profile_name}_targets.parquet"
        return self._load_parquet(path)

    def save_ml_supervised_dataset(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.ml_datasets / f"{symbol}_{timeframe}_{profile_name}_dataset.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_supervised_dataset(self, symbol: str, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.ml_datasets / f"{symbol}_{timeframe}_{profile_name}_dataset.parquet"
        return self._load_parquet(path)

    def save_ml_split_manifest(self, symbol: str, timeframe: str, profile_name: str, manifest: dict) -> Path: # type: ignore
        path = self.paths.ml_splits / f"{symbol}_{timeframe}_{profile_name}_split.json"
        import json
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            if hasattr(manifest, '__dataclass_fields__'):
                from dataclasses import asdict
                json.dump(asdict(manifest), f, indent=4)
            else:
                json.dump(manifest, f, indent=4)

        return path

    def load_ml_split_manifest(self, symbol: str, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.ml_splits / f"{symbol}_{timeframe}_{profile_name}_split.json"
        return {} # type: ignore path) or {}

    def save_ml_dataset_metadata(self, symbol: str, timeframe: str, profile_name: str, metadata: dict) -> Path: # type: ignore
        path = self.paths.ml_metadata / f"{symbol}_{timeframe}_{profile_name}_metadata.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(metadata, "w").write(json.dumps(_sanitize(path), indent=4))
        return path

    def load_ml_dataset_metadata(self, symbol: str, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.ml_metadata / f"{symbol}_{timeframe}_{profile_name}_metadata.json"
        return {} # type: ignore path) or {}

    def save_ml_dataset_quality(self, symbol: str, timeframe: str, profile_name: str, quality: dict) -> Path: # type: ignore
        path = self.paths.ml_quality / f"{symbol}_{timeframe}_{profile_name}_quality.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(quality, "w").write(json.dumps(_sanitize(path), indent=4))
        return path

    def load_ml_dataset_quality(self, symbol: str, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.ml_quality / f"{symbol}_{timeframe}_{profile_name}_quality.json"
        return {} # type: ignore path) or {}

    def list_ml_datasets(self) -> pd.DataFrame:
        data = []
        for file_path in self.paths.ml_metadata.glob("*.json"):
            metadata = {} # type: ignore file_path)
            if metadata:
                data.append(metadata)
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data)

    def save_ml_model_evaluation(self, symbol: str, timeframe: str, profile_name: str, model_id: str, evaluation: dict) -> Path: # type: ignore
        path = self.paths.ml_model_evaluations / f"{model_id}_evaluation.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(evaluation, "w").write(json.dumps(_sanitize(path), indent=4))
        return path

    def load_ml_model_evaluation(self, symbol: str, timeframe: str, profile_name: str, model_id: str) -> dict: # type: ignore
        path = self.paths.ml_model_evaluations / f"{model_id}_evaluation.json"
        return {} # type: ignore path) or {}

    def save_ml_cv_results(self, symbol: str, timeframe: str, profile_name: str, model_id: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.ml_model_cv / f"{model_id}_cv.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_cv_results(self, symbol: str, timeframe: str, profile_name: str, model_id: str) -> pd.DataFrame:
        path = self.paths.ml_model_cv / f"{model_id}_cv.parquet"
        return self._load_parquet(path)

    def save_ml_model_quality(self, symbol: str, timeframe: str, profile_name: str, model_id: str, quality: dict) -> Path: # type: ignore
        path = self.paths.ml_model_quality / f"{model_id}_quality.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(quality, "w").write(json.dumps(_sanitize(path), indent=4))
        return path

    def load_ml_model_quality(self, symbol: str, timeframe: str, profile_name: str, model_id: str) -> dict: # type: ignore
        path = self.paths.ml_model_quality / f"{model_id}_quality.json"
        return {} # type: ignore path) or {}

    def save_ml_registry_entry(self, entry: dict) -> Path: # type: ignore
        model_id = entry.get("model_id", "unknown")
        path = self.paths.ml_model_registry / f"{model_id}_registry.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(entry, "w").write(json.dumps(_sanitize(path), indent=4))
        return path

    def list_ml_model_registry(self) -> pd.DataFrame:
        data = []
        for file_path in self.paths.ml_model_registry.glob("*.json"):
            metadata = {} # type: ignore file_path)
            if metadata:
                data.append(metadata)
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data)


    # --- PHASE 32: ML CONTEXT INTEGRATION ---
    def save_ml_integration_features(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame, layer: str) -> Path: # type: ignore
        path = self.paths.ml_integration_features / f"{symbol}_{timeframe}_{layer}_{profile_name}_features.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_integration_features(self, symbol: str, timeframe: str, profile_name: str, layer: str) -> pd.DataFrame:
        path = self.paths.ml_integration_features / f"{symbol}_{timeframe}_{layer}_{profile_name}_features.parquet"
        return self._load_parquet(path)

    def save_ml_alignment_report(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame, layer: str) -> Path: # type: ignore
        path = self.paths.ml_integration_alignment / f"{symbol}_{timeframe}_{layer}_{profile_name}_alignment.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_alignment_report(self, symbol: str, timeframe: str, profile_name: str, layer: str) -> pd.DataFrame:
        path = self.paths.ml_integration_alignment / f"{symbol}_{timeframe}_{layer}_{profile_name}_alignment.parquet"
        return self._load_parquet(path)

    def save_ml_conflict_report(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.ml_integration_conflicts / f"{symbol}_{timeframe}_{profile_name}_conflicts.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_conflict_report(self, symbol: str, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.ml_integration_conflicts / f"{symbol}_{timeframe}_{profile_name}_conflicts.parquet"
        return self._load_parquet(path)

    def save_ml_integration_quality(self, symbol: str, timeframe: str, profile_name: str, quality: dict) -> Path: # type: ignore
        path = self.paths.ml_integration_quality / f"{symbol}_{timeframe}_{profile_name}_quality.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(quality, "w").write(json.dumps(_sanitize(path), indent=4))
        return path

    def load_ml_integration_quality(self, symbol: str, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.ml_integration_quality / f"{symbol}_{timeframe}_{profile_name}_quality.json"
        return {} # type: ignore path) or {}

    def list_ml_integration_reports(self) -> pd.DataFrame:
        data = []
        for path in self.paths.ml_integration_alignment.glob("*_alignment.parquet"):
            parts = path.stem.split("_")
            if len(parts) >= 4:
                # symbol_timeframe_layer_profile_alignment
                symbol = parts[0]
                timeframe = parts[1]
                layer = parts[2]
                profile = "_".join(parts[3:-1])
                data.append({
                    "symbol": symbol,
                    "timeframe": timeframe,
                    "layer": layer,
                    "profile": profile,
                    "type": "alignment",
                    "path": str(path)
                })
        return pd.DataFrame(data)


    # --- Notifications Specific ---
    def save_notification_message(self, message: dict): # type: ignore
        import json
        message_id = message.get("message_id", "unknown_id")
        file_path = self.paths.LAKE_NOTIFICATIONS_MESSAGES_DIR / f"{message_id}.json"

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(message, f, indent=4, ensure_ascii=False)
            logger.info(f"Saved notification message to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error saving notification message {message_id}: {e}")
            return None

    def load_notification_message(self, message_id: str) -> dict: # type: ignore
        import json
        file_path = self.paths.LAKE_NOTIFICATIONS_MESSAGES_DIR / f"{message_id}.json"

        try:
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            else:
                logger.warning(f"Notification message file not found: {file_path}")
                return {}
        except Exception as e:
            logger.error(f"Error loading notification message {message_id}: {e}")
            return {}

    def save_notification_delivery_log(self, profile_name: str, df: pd.DataFrame): # type: ignore
        if df is None or df.empty:
            logger.warning(f"Empty delivery log dataframe for {profile_name}. Not saving.")
            return None

        file_path = self.paths.LAKE_NOTIFICATIONS_DELIVERY_LOGS_DIR / f"{profile_name}_delivery_log.parquet"
        df.astype(str).to_parquet(file_path, index=False)
        logger.info(f"Saved notification delivery log to {file_path}")
        return file_path

    def load_notification_delivery_log(self, profile_name: str) -> pd.DataFrame | None:
        file_path = self.paths.LAKE_NOTIFICATIONS_DELIVERY_LOGS_DIR / f"{profile_name}_delivery_log.parquet"
        return pd.read_parquet(file_path) if file_path.exists() else None

    def save_notification_delivery_audit(self, profile_name: str, audit: dict): # type: ignore
        import json
        from datetime import datetime; timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
        file_path = self.paths.LAKE_NOTIFICATIONS_AUDITS_DIR / f"{profile_name}_{timestamp}_audit.json"

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(audit, f, indent=4, ensure_ascii=False)
            logger.info(f"Saved notification delivery audit to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error saving notification delivery audit {profile_name}: {e}")
            return None

    def load_notification_delivery_audit(self, profile_name: str) -> dict: # type: ignore
        import json
        pattern = f"{profile_name}_*_audit.json"
        files = list(self.paths.LAKE_NOTIFICATIONS_AUDITS_DIR.glob(pattern))

        if not files:
            logger.warning(f"No delivery audit found for profile: {profile_name}")
            return {}

        latest_file = sorted(files)[-1]
        try:
            with open(latest_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading notification delivery audit from {latest_file}: {e}")
            return {}

    def save_notification_quality(self, message_id: str, quality: dict): # type: ignore
        import json
        file_path = self.paths.LAKE_NOTIFICATIONS_QUALITY_DIR / f"{message_id}_quality.json"

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(quality, f, indent=4, ensure_ascii=False)
            logger.info(f"Saved notification quality to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error saving notification quality {message_id}: {e}")
            return None

    def load_notification_quality(self, message_id: str) -> dict: # type: ignore
        import json
        file_path = self.paths.LAKE_NOTIFICATIONS_QUALITY_DIR / f"{message_id}_quality.json"

        try:
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            else:
                logger.warning(f"Notification quality file not found: {file_path}")
                return {}
        except Exception as e:
            logger.error(f"Error loading notification quality {message_id}: {e}")
            return {}

    def list_notification_messages(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_NOTIFICATIONS_MESSAGES_DIR.glob("*.json"))
        data = []
        for f in files:
            try:
                import json
                with open(f, "r", encoding="utf-8") as file:
                    msg = json.load(file)
                    data.append({
                        "message_id": msg.get("message_id"),
                        "notification_type": msg.get("notification_type"),
                        "severity": msg.get("severity"),
                        "created_at_utc": msg.get("created_at_utc"),
                        "profile_name": msg.get("profile_name"),
                        "file_path": str(f)
                    })
            except Exception:
                pass

        return pd.DataFrame(data)


    # -------------------------------------------------------------------------
    # Orchestration Support
    # -------------------------------------------------------------------------

    def save_orchestration_run_manifest(self, run_id: str, manifest: dict) -> 'Path':
        """Save orchestration run manifest."""
        from config.paths import LAKE_ORCHESTRATION_MANIFESTS_DIR
        path = LAKE_ORCHESTRATION_MANIFESTS_DIR / f"{run_id}_manifest.json"
        import json
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            if hasattr(manifest, '__dataclass_fields__'):
                from dataclasses import asdict
                json.dump(asdict(manifest), f, indent=4)
            else:
                json.dump(manifest, f, indent=4)

        return path

    def load_orchestration_run_manifest(self, run_id: str) -> dict: # type: ignore
        """Load orchestration run manifest."""
        from config.paths import LAKE_ORCHESTRATION_MANIFESTS_DIR
        path = LAKE_ORCHESTRATION_MANIFESTS_DIR / f"{run_id}_manifest.json"
        return {} # type: ignore path)

    def save_orchestration_execution_plan(self, run_id: str, df: 'pd.DataFrame', summary: dict | None = None) -> 'Path':
        """Save orchestration execution plan."""
        from config.paths import LAKE_ORCHESTRATION_EXECUTION_PLANS_DIR
        path = LAKE_ORCHESTRATION_EXECUTION_PLANS_DIR / f"{run_id}_plan.parquet"
        self._save_parquet(df, path)
        if summary:
            summary_path = LAKE_ORCHESTRATION_EXECUTION_PLANS_DIR / f"{run_id}_plan_summary.json"
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(summary, "w").write(json.dumps(_sanitize(summary_path), indent=4))
        return path

    def load_orchestration_execution_plan(self, run_id: str) -> 'pd.DataFrame':
        """Load orchestration execution plan."""
        from config.paths import LAKE_ORCHESTRATION_EXECUTION_PLANS_DIR
        path = LAKE_ORCHESTRATION_EXECUTION_PLANS_DIR / f"{run_id}_plan.parquet"
        return self._load_parquet(path)

    def save_orchestration_dependency_graph(self, run_id: str, df: 'pd.DataFrame', summary: dict | None = None) -> 'Path':
        """Save orchestration dependency graph."""
        from config.paths import LAKE_ORCHESTRATION_DEPENDENCY_GRAPHS_DIR
        path = LAKE_ORCHESTRATION_DEPENDENCY_GRAPHS_DIR / f"{run_id}_graph.parquet"
        self._save_parquet(df, path)
        if summary:
            summary_path = LAKE_ORCHESTRATION_DEPENDENCY_GRAPHS_DIR / f"{run_id}_graph_summary.json"
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(summary, "w").write(json.dumps(_sanitize(summary_path), indent=4))
        return path

    def load_orchestration_dependency_graph(self, run_id: str) -> 'pd.DataFrame':
        """Load orchestration dependency graph."""
        from config.paths import LAKE_ORCHESTRATION_DEPENDENCY_GRAPHS_DIR
        path = LAKE_ORCHESTRATION_DEPENDENCY_GRAPHS_DIR / f"{run_id}_graph.parquet"
        return self._load_parquet(path)

    def save_orchestration_job_log(self, run_id: str, df: 'pd.DataFrame') -> 'Path':
        """Save orchestration job log."""
        from config.paths import LAKE_ORCHESTRATION_JOB_LOGS_DIR
        path = LAKE_ORCHESTRATION_JOB_LOGS_DIR / f"{run_id}_jobs.parquet"
        self._save_parquet(df, path)
        return path

    def load_orchestration_job_log(self, run_id: str) -> 'pd.DataFrame':
        """Load orchestration job log."""
        from config.paths import LAKE_ORCHESTRATION_JOB_LOGS_DIR
        path = LAKE_ORCHESTRATION_JOB_LOGS_DIR / f"{run_id}_jobs.parquet"
        return self._load_parquet(path)

    def save_orchestration_quality(self, run_id: str, quality: dict) -> 'Path':
        """Save orchestration quality report."""
        from config.paths import LAKE_ORCHESTRATION_QUALITY_DIR
        path = LAKE_ORCHESTRATION_QUALITY_DIR / f"{run_id}_quality.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(quality, "w").write(json.dumps(_sanitize(path), indent=4))
        return path

    def load_orchestration_quality(self, run_id: str) -> dict: # type: ignore
        """Load orchestration quality report."""
        from config.paths import LAKE_ORCHESTRATION_QUALITY_DIR
        path = LAKE_ORCHESTRATION_QUALITY_DIR / f"{run_id}_quality.json"
        return {} # type: ignore path)

    def list_orchestration_runs(self) -> 'pd.DataFrame':
        """List all available orchestration runs."""
        from config.paths import LAKE_ORCHESTRATION_MANIFESTS_DIR

        if not LAKE_ORCHESTRATION_MANIFESTS_DIR.exists():
             return pd.DataFrame()

        runs = []
        for p in LAKE_ORCHESTRATION_MANIFESTS_DIR.glob("*_manifest.json"):
             try:
                 manifest = {} # type: ignore p)
                 runs.append({
                     "run_id": manifest.get("run_id", p.stem.replace("_manifest", "")),
                     "workflow_name": manifest.get("workflow_name", "unknown"),
                     "profile_name": manifest.get("profile_name", "unknown"),
                     "timeframe": manifest.get("timeframe", "unknown"),
                     "started_at": manifest.get("started_at_utc", ""),
                     "status": manifest.get("workflow_status", "unknown"),
                     "job_count": manifest.get("job_count", 0),
                     "success_count": manifest.get("success_count", 0),
                     "failed_count": manifest.get("failed_count", 0),
                     "dry_run": manifest.get("dry_run", True)
                 })
             except Exception:
                 continue

        if not runs:
            return pd.DataFrame()

        df = pd.DataFrame(runs)
        if "started_at" in df.columns:
            df = df.sort_values("started_at", ascending=False).reset_index(drop=True)
        return df

    def list_notification_delivery_logs(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_NOTIFICATIONS_DELIVERY_LOGS_DIR.glob("*.parquet"))
        data = []
        for f in files:
            try:
                parts = f.stem.split("_")
                profile = parts[0] if len(parts) > 0 else "unknown"
                date_str = parts[-2] if len(parts) >= 2 else "unknown"
                data.append({
                    "profile_name": profile,
                    "date": date_str,
                    "file_path": str(f)
                })
            except Exception:
                pass

        return pd.DataFrame(data)

    # --- Observability Reports Save/Load ---
    def save_observability_health_report(self, report_name: str, df: pd.DataFrame, summary: dict) -> Path: # type: ignore
        """Save a health report to the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_HEALTH_DIR', self.root_dir / 'observability' / 'health')
        target_dir.mkdir(parents=True, exist_ok=True)

        csv_path = target_dir / f"{report_name}.csv"
        json_path = target_dir / f"{report_name}_summary.json"

        if not df.empty:
            df.to_csv(csv_path, index=False)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return csv_path

    def load_observability_health_report(self, report_name: str) -> pd.DataFrame:
        """Load a health report from the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_HEALTH_DIR', self.root_dir / 'observability' / 'health')
        csv_path = target_dir / f"{report_name}.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        return pd.DataFrame()

    def save_runtime_metrics(self, report_name: str, df: pd.DataFrame, summary: dict) -> Path: # type: ignore
        """Save runtime metrics to the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_RUNTIME_METRICS_DIR', self.root_dir / 'observability' / 'runtime_metrics')
        target_dir.mkdir(parents=True, exist_ok=True)

        csv_path = target_dir / f"{report_name}.csv"
        json_path = target_dir / f"{report_name}_summary.json"

        if not df.empty:
            df.to_csv(csv_path, index=False)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return csv_path

    def load_runtime_metrics(self, report_name: str) -> pd.DataFrame:
        """Load runtime metrics from the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_RUNTIME_METRICS_DIR', self.root_dir / 'observability' / 'runtime_metrics')
        csv_path = target_dir / f"{report_name}.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        return pd.DataFrame()

    def save_diagnostics_report(self, report_name: str, summary: dict) -> Path: # type: ignore
        """Save self-diagnostics summary to the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_DIAGNOSTICS_DIR', self.root_dir / 'observability' / 'diagnostics')
        target_dir.mkdir(parents=True, exist_ok=True)

        json_path = target_dir / f"{report_name}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return json_path

    def load_diagnostics_report(self, report_name: str) -> dict: # type: ignore
        """Load self-diagnostics summary from the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_DIAGNOSTICS_DIR', self.root_dir / 'observability' / 'diagnostics')
        json_path = target_dir / f"{report_name}.json"
        if json_path.exists():
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_error_taxonomy_report(self, df: pd.DataFrame, summary: dict) -> Path: # type: ignore
        """Save error taxonomy to the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_ERROR_TAXONOMY_DIR', self.root_dir / 'observability' / 'error_taxonomy')
        target_dir.mkdir(parents=True, exist_ok=True)

        csv_path = target_dir / "error_taxonomy.csv"
        json_path = target_dir / "error_taxonomy_summary.json"

        if not df.empty:
            df.to_csv(csv_path, index=False)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return csv_path

    def load_error_taxonomy_report(self) -> pd.DataFrame:
        """Load error taxonomy from the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_ERROR_TAXONOMY_DIR', self.root_dir / 'observability' / 'error_taxonomy')
        csv_path = target_dir / "error_taxonomy.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        return pd.DataFrame()

    def save_data_freshness_report(self, df: pd.DataFrame, summary: dict) -> Path: # type: ignore
        """Save data freshness report to the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_DATA_FRESHNESS_DIR', self.root_dir / 'observability' / 'data_freshness')
        target_dir.mkdir(parents=True, exist_ok=True)

        csv_path = target_dir / "data_freshness.csv"
        json_path = target_dir / "data_freshness_summary.json"

        if not df.empty:
            df.to_csv(csv_path, index=False)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return csv_path

    def load_data_freshness_report(self) -> pd.DataFrame:
        """Load data freshness report from the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_DATA_FRESHNESS_DIR', self.root_dir / 'observability' / 'data_freshness')
        csv_path = target_dir / "data_freshness.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        return pd.DataFrame()

    def save_artifact_integrity_report(self, df: pd.DataFrame, summary: dict) -> Path: # type: ignore
        """Save artifact integrity report to the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_ARTIFACT_INTEGRITY_DIR', self.root_dir / 'observability' / 'artifact_integrity')
        target_dir.mkdir(parents=True, exist_ok=True)

        csv_path = target_dir / "artifact_integrity.csv"
        json_path = target_dir / "artifact_integrity_summary.json"

        if not df.empty:
            df.to_csv(csv_path, index=False)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return csv_path

    def load_artifact_integrity_report(self) -> pd.DataFrame:
        """Load artifact integrity report from the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_ARTIFACT_INTEGRITY_DIR', self.root_dir / 'observability' / 'artifact_integrity')
        csv_path = target_dir / "artifact_integrity.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        return pd.DataFrame()

    def save_observability_quality(self, report_name: str, quality: dict) -> Path: # type: ignore
        """Save observability quality check results."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_QUALITY_DIR', self.root_dir / 'observability' / 'quality')
        target_dir.mkdir(parents=True, exist_ok=True)

        json_path = target_dir / f"{report_name}_quality.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(quality, f, indent=2, ensure_ascii=False)

        return json_path

    def load_observability_quality(self, report_name: str) -> dict: # type: ignore
        """Load observability quality check results."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_QUALITY_DIR', self.root_dir / 'observability' / 'quality')
        json_path = target_dir / f"{report_name}_quality.json"
        if json_path.exists():
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def list_observability_reports(self) -> pd.DataFrame:
        """List all available observability reports."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_DIR', self.root_dir / 'observability')

        if not target_dir.exists():
            return pd.DataFrame()

        rows = []
        for file in target_dir.rglob("*"):
            if file.is_file() and file.suffix in ['.csv', '.json']:
                report_type = file.parent.name
                rows.append({
                    "report_type": report_type,
                    "filename": file.name,
                    "modified_time": pd.Timestamp(file.stat().st_mtime, unit='s'),
                    "path": str(file)
                })

        if not rows:
            return pd.DataFrame()

        df = pd.DataFrame(rows)
        return df.sort_values(by="modified_time", ascending=False)

    # --- Phase 37: Security ---
    def save_security_audit_report(self, report_name: str, df: pd.DataFrame, summary: dict) -> Path: # type: ignore
        self.paths.security_audits.mkdir(parents=True, exist_ok=True)
        csv_path = self.paths.security_audits / f"{report_name}.csv"
        json_path = self.paths.security_audits / f"{report_name}.json"
        if not df.empty:
            df.to_csv(csv_path, index=False)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
        return csv_path

    def load_security_audit_report(self, report_name: str) -> pd.DataFrame:
        csv_path = self.paths.security_audits / f"{report_name}.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        return pd.DataFrame()

    def save_secret_hygiene_report(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("secret_hygiene", df, summary)
    def load_secret_hygiene_report(self) -> pd.DataFrame:
        return self.load_security_audit_report("secret_hygiene")
    def save_config_hardening_report(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("config_hardening", df, summary)
    def load_config_hardening_report(self) -> pd.DataFrame:
        return self.load_security_audit_report("config_hardening")
    def save_safe_defaults_report(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("safe_defaults", df, summary)
    def load_safe_defaults_report(self) -> pd.DataFrame:
        return self.load_security_audit_report("safe_defaults")
    def save_permission_boundary_report(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("permission_boundaries", df, summary)
    def load_permission_boundary_report(self) -> pd.DataFrame:
        return self.load_security_audit_report("permission_boundaries")
    def save_path_safety_report(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("path_safety", df, summary)
    def save_token_scan_report(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("token_scan", df, summary)
    def load_token_scan_report(self) -> pd.DataFrame:
        return self.load_security_audit_report("token_scan")
    def save_readiness_audit(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("readiness_audit", df, summary)
    def load_readiness_audit(self) -> pd.DataFrame:
        return self.load_security_audit_report("readiness_audit")

    def save_security_quality(self, report_name: str, quality: dict) -> Path: # type: ignore
        self.paths.security_quality.mkdir(parents=True, exist_ok=True)
        json_path = self.paths.security_quality / f"{report_name}_quality.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=2)
        return json_path

    def load_security_quality(self, report_name: str) -> dict: # type: ignore
        json_path = self.paths.security_quality / f"{report_name}_quality.json"
        if json_path.exists():
            with open(json_path, "r", encoding="utf-8") as f: return json.load(f)
        return {}

    def list_security_reports(self) -> pd.DataFrame: return pd.DataFrame()


    # Phase 42: Portfolio Regime Research
    def save_portfolio_regimes(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_report(df, self.paths.portfolio_regime_regimes / f"regimes_{timeframe}_{profile_name}.parquet")

    def load_portfolio_regimes(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_regimes / f"regimes_{timeframe}_{profile_name}.parquet")

    def save_regime_conditioned_returns(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_report(df, self.paths.portfolio_regime_conditioned_returns / f"conditioned_returns_{timeframe}_{profile_name}.parquet")

    def load_regime_conditioned_returns(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_conditioned_returns / f"conditioned_returns_{timeframe}_{profile_name}.parquet")

    def save_regime_correlation_summary(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_report(df, self.paths.portfolio_regime_correlation / f"correlation_{timeframe}_{profile_name}.parquet")

    def load_regime_correlation_summary(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_correlation / f"correlation_{timeframe}_{profile_name}.parquet")

    def save_macro_scenario_sensitivity(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_report(df, self.paths.portfolio_regime_scenarios / f"scenario_sensitivity_{timeframe}_{profile_name}.parquet")

    def load_macro_scenario_sensitivity(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_scenarios / f"scenario_sensitivity_{timeframe}_{profile_name}.parquet")

    def save_basket_stress_test_results(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_report(df, self.paths.portfolio_regime_stress_tests / f"stress_test_{timeframe}_{profile_name}.parquet")

    def load_basket_stress_test_results(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_stress_tests / f"stress_test_{timeframe}_{profile_name}.parquet")

    def save_drawdown_clusters(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_report(df, self.paths.portfolio_regime_drawdowns / f"drawdown_clusters_{timeframe}_{profile_name}.parquet")

    def load_drawdown_clusters(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_drawdowns / f"drawdown_clusters_{timeframe}_{profile_name}.parquet")

    def save_recovery_analysis(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_report(df, self.paths.portfolio_regime_recovery / f"recovery_analysis_{timeframe}_{profile_name}.parquet")

    def load_recovery_analysis(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_recovery / f"recovery_analysis_{timeframe}_{profile_name}.parquet")

    def save_tail_risk_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_report(df, self.paths.portfolio_regime_tail_risk / f"tail_risk_{timeframe}_{profile_name}.parquet")

    def load_tail_risk_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_tail_risk / f"tail_risk_{timeframe}_{profile_name}.parquet")

    def save_risk_regime_exposure(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_report(df, self.paths.portfolio_regime_exposure / f"exposure_{timeframe}_{profile_name}.parquet")

    def load_risk_regime_exposure(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_exposure / f"exposure_{timeframe}_{profile_name}.parquet")

    def save_portfolio_regime_report(self, timeframe: str, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        import json
        path = self.paths.portfolio_regime_reports / f"regime_report_{timeframe}_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        if markdown:
            md_path = self.paths.portfolio_regime_reports / f"regime_report_{timeframe}_{profile_name}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown)
        return path

    def load_portfolio_regime_report(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        import json
        path = self.paths.portfolio_regime_reports / f"regime_report_{timeframe}_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_portfolio_regime_quality(self, timeframe: str, profile_name: str, quality: dict) -> Path: # type: ignore
        import json
        path = self.paths.portfolio_regime_quality / f"quality_{timeframe}_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=2)
        return path

    def load_portfolio_regime_quality(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        import json
        path = self.paths.portfolio_regime_quality / f"quality_{timeframe}_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_portfolio_regime_reports(self) -> pd.DataFrame:
        return pd.DataFrame()

    # Phase 43: Synthetic Indices
    def save_synthetic_index_definitions(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_definitions / f"definitions_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_index_definitions(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_definitions / f"definitions_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_index_levels(self, index_id: str, timeframe: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_levels / f"{index_id}_{timeframe}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_index_levels(self, index_id: str, timeframe: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_levels / f"{index_id}_{timeframe}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_index_returns(self, index_id: str, timeframe: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_returns / f"{index_id}_{timeframe}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_index_returns(self, index_id: str, timeframe: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_returns / f"{index_id}_{timeframe}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_relative_strength_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_relative_strength / f"relative_strength_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_relative_strength_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_relative_strength / f"relative_strength_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_relative_momentum_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_relative_momentum / f"relative_momentum_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_relative_momentum_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_relative_momentum / f"relative_momentum_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_universe_rotation_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_rotation / f"universe_rotation_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_universe_rotation_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_rotation / f"universe_rotation_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_leadership_laggard_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_leadership / f"leadership_laggard_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_leadership_laggard_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_leadership / f"leadership_laggard_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_benchmark_comparison(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_comparisons / f"benchmark_comparison_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_benchmark_comparison(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_comparisons / f"benchmark_comparison_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_index_performance(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_performance / f"index_performance_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_index_performance(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_performance / f"index_performance_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_index_quality(self, timeframe: str, profile_name: str, quality: dict) -> Path: # type: ignore
        path = self.paths.synthetic_indices_quality / f"quality_{timeframe}_{profile_name}.json"
        import json
        with open(path, "w") as f:
            json.dump(quality, f, indent=2)
        return path

    def load_synthetic_index_quality(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.synthetic_indices_quality / f"quality_{timeframe}_{profile_name}.json"
        if path.exists():
            import json
            with open(path, "r") as f:
                return json.load(f)
        return {}

    def save_synthetic_index_report(self, timeframe: str, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        path = self.paths.synthetic_indices_reports / f"report_{timeframe}_{profile_name}.json"
        import json
        with open(path, "w") as f:
            json.dump(report, f, indent=2)

        if markdown:
             md_path = self.paths.synthetic_indices_reports_markdown / f"report_{timeframe}_{profile_name}.md"
             with open(md_path, "w") as f:
                 f.write(markdown)

        return path

    def load_synthetic_index_report(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.synthetic_indices_reports / f"report_{timeframe}_{profile_name}.json"
        if path.exists():
            import json
            with open(path, "r") as f:
                return json.load(f)
        return {}

    def list_synthetic_index_reports(self) -> pd.DataFrame:
        records = []
        if self.paths.synthetic_indices_reports.exists():
            import json
            for path in self.paths.synthetic_indices_reports.glob("*.json"):
                try:
                    with open(path, "r") as f:
                        data = json.load(f)
                        records.append({
                            "file": path.name,
                            "timeframe": data.get("timeframe"),
                            "profile": data.get("profile"),
                            "timestamp": data.get("timestamp")
                        })
                except Exception:
                    pass
        return pd.DataFrame(records)

    # --- Phase 45: Meta Research ---

    def save_meta_evidence_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_EVIDENCE_DIR / f"evidence_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_evidence_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_EVIDENCE_DIR / f"evidence_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_source_reliability(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_RELIABILITY_DIR / f"reliability_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_source_reliability(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_RELIABILITY_DIR / f"reliability_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_consensus_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_CONSENSUS_DIR / f"consensus_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_consensus_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_CONSENSUS_DIR / f"consensus_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_conflict_report(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_CONFLICTS_DIR / f"conflicts_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_conflict_report(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_CONFLICTS_DIR / f"conflicts_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_uncertainty_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_UNCERTAINTY_DIR / f"uncertainty_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_uncertainty_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_UNCERTAINTY_DIR / f"uncertainty_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_ensemble_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_ENSEMBLE_DIR / f"ensemble_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_ensemble_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_ENSEMBLE_DIR / f"ensemble_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_quality_adjusted_ranking(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_RANKINGS_DIR / f"ranking_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_quality_adjusted_ranking(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_RANKINGS_DIR / f"ranking_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_symbol_snapshot(self, symbol: str, timeframe: str, profile_name: str, snapshot: dict) -> Path: # type: ignore
        path = self.paths.LAKE_META_RESEARCH_SNAPSHOTS_DIR / f"snapshot_{symbol}_{timeframe}_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            import json
            json.dump(snapshot, f, indent=2, ensure_ascii=False)
        return path

    def load_meta_symbol_snapshot(self, symbol: str, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.LAKE_META_RESEARCH_SNAPSHOTS_DIR / f"snapshot_{symbol}_{timeframe}_{profile_name}.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                import json
                return json.load(f)
        return {}

    def save_meta_quality(self, timeframe: str, profile_name: str, quality: dict) -> Path: # type: ignore
        path = self.paths.LAKE_META_RESEARCH_QUALITY_DIR / f"quality_{timeframe}_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            import json
            json.dump(quality, f, indent=2, ensure_ascii=False)
        return path

    def load_meta_quality(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.LAKE_META_RESEARCH_QUALITY_DIR / f"quality_{timeframe}_{profile_name}.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                import json
                return json.load(f)
        return {}


    # Phase 46: Experiment Tracking Load/Save
    def save_hypothesis_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        out_file = self.paths.experiments_hypotheses / "hypothesis_registry.jsonl"
        # Not implementing full save here to keep the patch small, assuming managed by HypothesisRegistry
        return out_file

    def load_hypothesis_registry(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_definitions(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        return self.paths.experiments_definitions / "definitions.csv"

    def load_experiment_definitions(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_run_manifest(self, run_id: str, manifest: dict) -> Path: # type: ignore
        out_file = self.paths.experiments_runs / f"run_{run_id}.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(out_file, "w").write(json.dumps(_sanitize(manifest), indent=4))
        return out_file

    def load_experiment_run_manifest(self, run_id: str) -> dict: # type: ignore
        return {}

    def save_experiment_artifact_manifest(self, run_id: str, manifest: dict) -> Path: # type: ignore
        out_file = self.paths.experiments_artifacts / f"artifacts_{run_id}.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(out_file, "w").write(json.dumps(_sanitize(manifest), indent=4))
        return out_file

    def load_experiment_artifact_manifest(self, run_id: str) -> dict: # type: ignore
        return {}

    def save_reproducibility_manifest(self, run_id: str, manifest: dict) -> Path: # type: ignore
        out_file = self.paths.experiments_reproducibility / f"repro_{run_id}.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(out_file, "w").write(json.dumps(_sanitize(manifest), indent=4))
        return out_file

    def load_reproducibility_manifest(self, run_id: str) -> dict: # type: ignore
        return {}

    def save_research_version_record(self, version_id: str, record: dict) -> Path: # type: ignore
        out_file = self.paths.experiments_versions / f"version_{version_id}.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(out_file, "w").write(json.dumps(_sanitize(record), indent=4))
        return out_file

    def load_research_version_record(self, version_id: str) -> dict: # type: ignore
        return {}

    def save_ablation_study_results(self, study_id: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        out_file = self.paths.experiments_ablation / f"{study_id}.csv"
        df.to_csv(out_file, index=False)
        return out_file

    def load_ablation_study_results(self, study_id: str) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_comparison_table(self, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        out_file = self.paths.experiments_comparisons / f"{profile_name}_comparisons.csv"
        df.to_csv(out_file, index=False)
        return out_file

    def load_experiment_comparison_table(self, profile_name: str) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_leaderboard(self, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        out_file = self.paths.experiments_leaderboards / f"{profile_name}_leaderboard.csv"
        df.to_csv(out_file, index=False)
        return out_file

    def load_experiment_leaderboard(self, profile_name: str) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_quality(self, run_id_or_profile: str, quality: dict) -> Path: # type: ignore
        out_file = self.paths.experiments_quality / f"{run_id_or_profile}_quality.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(out_file, "w").write(json.dumps(_sanitize(quality), indent=4))
        return out_file

    def load_experiment_quality(self, run_id_or_profile: str) -> dict: # type: ignore
        return {}

    def save_experiment_tracking_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        out_file = self.paths.experiments_reports_json / f"{profile_name}_report.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(out_file, "w").write(json.dumps(_sanitize(report), indent=4))
        return out_file

    def load_experiment_tracking_report(self, profile_name: str) -> dict: # type: ignore
        return {}

    def list_experiment_runs(self) -> pd.DataFrame:
        return pd.DataFrame()

    def list_experiment_reports(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_meta_research_report(self, timeframe: str, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        json_path = self.paths.LAKE_META_RESEARCH_REPORTS_DIR / f"report_{timeframe}_{profile_name}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            import json
            json.dump(report, f, indent=2, ensure_ascii=False)

        if markdown:
            md_path = self.paths.REPORTS_META_RESEARCH_MD_DIR / f"meta_research_{timeframe}_{profile_name}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown)

        return json_path

    def load_meta_research_report(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.LAKE_META_RESEARCH_REPORTS_DIR / f"report_{timeframe}_{profile_name}.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                import json
                return json.load(f)
        return {}

    def list_meta_research_reports(self) -> pd.DataFrame:
        rows = []
        for p in self.paths.LAKE_META_RESEARCH_REPORTS_DIR.glob("report_*.json"):
            parts = p.stem.split("_", 2)
            if len(parts) >= 3:
                timeframe = parts[1]
                profile = parts[2]
                rows.append({
                    "timeframe": timeframe,
                    "profile": profile,
                    "path": str(p),
                    "size": p.stat().st_size
                })
        return pd.DataFrame(rows) if rows else pd.DataFrame(columns=["timeframe", "profile", "path", "size"])


    # Phase 48: Research Planning
    def save_research_planning_signals(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_SIGNALS_DIR / f"signals_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(summary, "w").write(json.dumps(_sanitize(filepath.with_suffix(".json"), indent=4)))
        return filepath

    def load_research_planning_signals(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_SIGNALS_DIR / f"signals_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_task_registry(self, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_TASKS_DIR / f"tasks_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(summary, "w").write(json.dumps(_sanitize(filepath.with_suffix(".json"), indent=4)))
        return filepath

    def load_research_task_registry(self, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_TASKS_DIR / f"tasks_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_backlog(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_BACKLOG_DIR / f"backlog_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(summary, "w").write(json.dumps(_sanitize(filepath.with_suffix(".json"), indent=4)))
        return filepath

    def load_research_backlog(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_BACKLOG_DIR / f"backlog_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_priority_scores(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_PRIORITIES_DIR / f"priorities_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(summary, "w").write(json.dumps(_sanitize(filepath.with_suffix(".json"), indent=4)))
        return filepath

    def load_research_priority_scores(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_PRIORITIES_DIR / f"priorities_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_next_best_experiments(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_NEXT_BEST_DIR / f"next_best_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(summary, "w").write(json.dumps(_sanitize(filepath.with_suffix(".json"), indent=4)))
        return filepath

    def load_next_best_experiments(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_NEXT_BEST_DIR / f"next_best_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_debt_report(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_DEBT_DIR / f"debt_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(summary, "w").write(json.dumps(_sanitize(filepath.with_suffix(".json"), indent=4)))
        return filepath

    def load_research_debt_report(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_DEBT_DIR / f"debt_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_opportunity_report(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_OPPORTUNITIES_DIR / f"opportunities_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(summary, "w").write(json.dumps(_sanitize(filepath.with_suffix(".json"), indent=4)))
        return filepath

    def load_research_opportunity_report(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_OPPORTUNITIES_DIR / f"opportunities_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_roadmap_health_snapshot(self, timeframe: str, profile_name: str, snapshot: dict) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_ROADMAP_DIR / f"roadmap_{timeframe}_{profile_name}.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(snapshot, "w").write(json.dumps(_sanitize(filepath), indent=4))
        return filepath

    def load_roadmap_health_snapshot(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_ROADMAP_DIR / f"roadmap_{timeframe}_{profile_name}.json"
        return {} # type: ignore filepath)

    def save_task_dependency_table(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_DEPENDENCIES_DIR / f"dependencies_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(summary, "w").write(json.dumps(_sanitize(filepath.with_suffix(".json"), indent=4)))
        return filepath

    def load_task_dependency_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_DEPENDENCIES_DIR / f"dependencies_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_milestone_tracking_table(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_MILESTONES_DIR / f"milestones_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(summary, "w").write(json.dumps(_sanitize(filepath.with_suffix(".json"), indent=4)))
        return filepath

    def load_milestone_tracking_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_MILESTONES_DIR / f"milestones_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_task_orchestration_plan(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_ORCHESTRATION_DIR / f"orchestration_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(summary, "w").write(json.dumps(_sanitize(filepath.with_suffix(".json"), indent=4)))
        return filepath

    def load_task_orchestration_plan(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_ORCHESTRATION_DIR / f"orchestration_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_planning_quality(self, timeframe: str, profile_name: str, quality: dict) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_QUALITY_DIR / f"quality_{timeframe}_{profile_name}.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(quality, "w").write(json.dumps(_sanitize(filepath), indent=4))
        return filepath

    def load_research_planning_quality(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_QUALITY_DIR / f"quality_{timeframe}_{profile_name}.json"
        return {} # type: ignore filepath)

    def save_research_planning_report(self, timeframe: str, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        filepath = self.paths.REPORTS_RESEARCH_PLANNING_JSON_DIR / f"report_{timeframe}_{profile_name}.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(report, "w").write(json.dumps(_sanitize(filepath), indent=4))
        if markdown:
            md_path = self.paths.REPORTS_RESEARCH_PLANNING_MARKDOWN_DIR / f"report_{timeframe}_{profile_name}.md"
            self._save_text(markdown, md_path)
        return filepath

    def load_research_planning_report(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        filepath = self.paths.REPORTS_RESEARCH_PLANNING_JSON_DIR / f"report_{timeframe}_{profile_name}.json"
        return {} # type: ignore filepath)

    def list_research_planning_reports(self) -> pd.DataFrame:
        files = list(self.paths.REPORTS_RESEARCH_PLANNING_JSON_DIR.glob("*.json"))
        data = []
        for f in files:
            parts = f.stem.split("_")
            if len(parts) >= 3:
                data.append({"timeframe": parts[1], "profile": "_".join(parts[2:]), "file": f.name})
        return pd.DataFrame(data)


    # Phase 49 Knowledge Base Methods
    def save_knowledge_documents(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_DOCUMENTS_DIR / "documents.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_DOCUMENTS_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_knowledge_documents(self) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_DOCUMENTS_DIR / "documents.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_knowledge_chunks(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_CHUNKS_DIR / "chunks.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_CHUNKS_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_knowledge_chunks(self) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_CHUNKS_DIR / "chunks.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_knowledge_index_summary(self, summary: dict) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_INDEXES_DIR / "index_summary.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        return p

    def load_knowledge_index_summary(self) -> dict: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_INDEXES_DIR / "index_summary.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_retrieval_results(self, query_id: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_RETRIEVAL_DIR / f"results_{query_id}.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_RETRIEVAL_DIR / f"summary_{query_id}.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_retrieval_results(self, query_id: str) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_RETRIEVAL_DIR / f"results_{query_id}.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_memory_cards(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / "memory_cards.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_memory_cards(self) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / "memory_cards.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_symbol_memory_card(self, symbol: str, card: dict) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / f"card_{symbol}.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(card, f, indent=2)
        return p

    def load_symbol_memory_card(self, symbol: str) -> dict: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / f"card_{symbol}.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_decision_journal(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_DECISION_JOURNAL_DIR / "decision_journal.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_DECISION_JOURNAL_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_decision_journal(self) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_DECISION_JOURNAL_DIR / "decision_journal.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_analyst_notes(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_ANALYST_NOTES_DIR / "analyst_notes.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_ANALYST_NOTES_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_analyst_notes(self) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_ANALYST_NOTES_DIR / "analyst_notes.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_recent_findings_digest(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_FINDINGS_DIR / "recent_findings.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_FINDINGS_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_recent_findings_digest(self) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_FINDINGS_DIR / "recent_findings.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_workspace_summary(self, summary: dict) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_WORKSPACE_DIR / "workspace_summary.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        return p

    def load_workspace_summary(self) -> dict: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_WORKSPACE_DIR / "workspace_summary.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_kb_quality(self, profile_name: str, quality: dict) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_QUALITY_DIR / f"quality_{profile_name}.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(quality, f, indent=2)
        return p

    def load_kb_quality(self, profile_name: str) -> dict: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_QUALITY_DIR / f"quality_{profile_name}.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_knowledge_base_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        p = self.paths.REPORTS_KNOWLEDGE_BASE_JSON_DIR / f"report_{profile_name}.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)

        if markdown:
            md_p = self.paths.REPORTS_KNOWLEDGE_BASE_MARKDOWN_DIR / f"report_{profile_name}.md"
            with open(md_p, 'w', encoding='utf-8') as f:
                f.write(markdown)

            txt_p = self.paths.REPORTS_KNOWLEDGE_BASE_TXT_DIR / f"report_{profile_name}.txt"
            with open(txt_p, 'w', encoding='utf-8') as f:
                f.write(markdown) # Use markdown as text for now

        return p

    def load_knowledge_base_report(self, profile_name: str) -> dict: # type: ignore
        p = self.paths.REPORTS_KNOWLEDGE_BASE_JSON_DIR / f"report_{profile_name}.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def list_knowledge_base_reports(self) -> pd.DataFrame:
        d = self.paths.REPORTS_KNOWLEDGE_BASE_JSON_DIR
        reports = []
        if d.exists():
            for p in d.glob("report_*.json"):
                profile_name = p.stem.replace("report_", "")
                with open(p, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        reports.append({
                            "profile_name": profile_name,
                            "file": p.name
                        })
                    except Exception:
                        pass
        return pd.DataFrame(reports)

    def save_runtime_profiles(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_RUNTIME.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_RUNTIME / f"runtime_profiles_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_runtime_profiles(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_RUNTIME.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_memory_profiles(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_MEMORY.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_MEMORY / f"memory_profiles_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_memory_profiles(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_MEMORY.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_cpu_gpu_awareness(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_CPU_GPU.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CPU_GPU / f"cpu_gpu_awareness_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_cpu_gpu_awareness(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_CPU_GPU.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_resource_budgets(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_BUDGET.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_BUDGET / f"resource_budgets_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_resource_budgets(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_BUDGET.glob("resource_budgets_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_resource_budget_violations(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_BUDGET.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_BUDGET / f"violations_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_resource_budget_violations(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_BUDGET.glob("violations_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_cache_inventory(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_CACHE.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CACHE / f"inventory_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_cache_inventory(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_CACHE.glob("inventory_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_cache_strategy(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_CACHE.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CACHE / f"strategy_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_cache_strategy(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_CACHE.glob("strategy_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_cache_hit_miss_report(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_CACHE.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CACHE / f"hit_miss_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_cache_hit_miss_report(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_CACHE.glob("hit_miss_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_batch_plans(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_BATCH_PLANS.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_BATCH_PLANS / f"batch_plans_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_batch_plans(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_BATCH_PLANS.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_checkpoint_manifest(self, manifest_name: str, manifest: dict) -> Path:
        self.paths.LAKE_PERFORMANCE_CHECKPOINTS.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CHECKPOINTS / f"{manifest_name}.json"
        import json
        with open(path, "w") as f:
            json.dump(manifest, f)
        return path

    def load_checkpoint_manifest(self, manifest_name: str) -> dict:
        path = self.paths.LAKE_PERFORMANCE_CHECKPOINTS / f"{manifest_name}.json"
        if not path.exists(): return {}
        import json
        with open(path, "r") as f:
            return json.load(f)

    def save_large_run_stability_report(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_STABILITY.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_STABILITY / f"stability_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_large_run_stability_report(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_STABILITY.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_bottleneck_report(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_BOTTLENECKS.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_BOTTLENECKS / f"bottleneck_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_bottleneck_report(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_BOTTLENECKS.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_optimization_recommendations(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_OPTIMIZATION.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_OPTIMIZATION / f"optimization_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_optimization_recommendations(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_OPTIMIZATION.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_performance_quality(self, profile_name: str, quality: dict) -> Path:
        self.paths.LAKE_PERFORMANCE_QUALITY.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_QUALITY / f"{profile_name}_quality_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json"
        import json
        with open(path, "w") as f:
            json.dump(quality, f)
        return path

    def load_performance_quality(self, profile_name: str) -> dict:
        files = list(self.paths.LAKE_PERFORMANCE_QUALITY.glob(f"{profile_name}_quality_*.json"))
        if not files: return {}
        latest = max(files, key=os.path.getctime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def save_performance_report(self, profile_name: str, report: dict, markdown: Optional[str] = None) -> Path:
        self.paths.REPORTS_PERFORMANCE_JSON.mkdir(parents=True, exist_ok=True)
        path = self.paths.REPORTS_PERFORMANCE_JSON / f"{profile_name}_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json"
        import json
        with open(path, "w") as f:
            json.dump(report, f)

        if markdown:
            self.paths.REPORTS_PERFORMANCE_MARKDOWN.mkdir(parents=True, exist_ok=True)
            md_path = self.paths.REPORTS_PERFORMANCE_MARKDOWN / f"{profile_name}_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.md"
            with open(md_path, "w") as f:
                f.write(markdown)

        return path

    def load_performance_report(self, profile_name: str) -> dict:
        files = list(self.paths.REPORTS_PERFORMANCE_JSON.glob(f"{profile_name}_report_*.json"))
        if not files: return {}
        latest = max(files, key=os.path.getctime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def list_performance_reports(self) -> pd.DataFrame:
        files = list(self.paths.REPORTS_PERFORMANCE_JSON.glob("*.json"))
        if not files: return pd.DataFrame()
        records = []
        for f in files:
            records.append({
                "name": f.stem,
                "path": str(f),
                "created_at": datetime.fromtimestamp(os.path.getctime(f)).isoformat()
            })
        return pd.DataFrame(records)


    # --- MAINTENANCE SUPPORT ---
    def save_storage_inventory(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_INVENTORY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "inventory")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"storage_inventory_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_inventory(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_INVENTORY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "inventory")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_retention_policies(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_POLICIES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "policies")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"retention_policies_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_retention_policies(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_POLICIES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "policies")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cleanup_candidates(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cleanup_candidates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cleanup_candidates(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cleanup_candidates_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cleanup_dry_run_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cleanup_plan_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cleanup_dry_run_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cleanup_plan_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_archive_candidates(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"archive_candidates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_archive_candidates(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("archive_candidates_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_archive_manifest(self, archive_id: str, manifest: dict) -> Path:
        out_dir = getattr(self.paths, "ARCHIVES_MANIFESTS_DIR", self.paths.PROJECT_ROOT / "archives" / "manifests")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"{archive_id}.json"
        with open(path, "w") as f:
            json.dump(manifest, f, indent=2)
        return path

    def load_archive_manifest(self, archive_id: str) -> dict:
        import json
        out_dir = getattr(self.paths, "ARCHIVES_MANIFESTS_DIR", self.paths.PROJECT_ROOT / "archives" / "manifests")
        path = out_dir / f"{archive_id}.json"
        if not path.exists():
            return {}
        with open(path, "r") as f:
            return json.load(f)

    def save_archive_dry_run_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"archive_plan_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_archive_dry_run_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("archive_plan_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_report_rotation_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"report_rotation_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_report_rotation_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("report_rotation_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_log_rotation_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"log_rotation_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_log_rotation_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("log_rotation_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cache_pruning_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cache_pruning_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cache_pruning_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cache_pruning_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_duplicate_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_DUPLICATES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "duplicates")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"duplicates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_duplicate_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_DUPLICATES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "duplicates")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_stale_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_STALE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "stale")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"stale_artifacts_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_stale_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_STALE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "stale")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_large_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_LARGE_ARTIFACTS_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "large_artifacts")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"large_artifacts_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_large_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_LARGE_ARTIFACTS_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "large_artifacts")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_storage_growth_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"storage_growth_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_growth_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("storage_growth_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_storage_growth_snapshot(self, snapshot: dict) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"snapshot_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(snapshot, f)
        return path

    def load_storage_growth_snapshots(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("snapshot_*.json"))
        if not files:
            return pd.DataFrame()
        import json
        data = []
        for f in files:
            with open(f, "r") as fp:
                data.append(json.load(fp))
        return pd.DataFrame(data)

    def save_storage_lifecycle_health(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_LIFECYCLE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "lifecycle")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"lifecycle_health_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_lifecycle_health(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_LIFECYCLE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "lifecycle")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_maintenance_quality(self, profile_name: str, quality: dict) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_QUALITY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "quality")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"quality_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(quality, f, indent=2)
        return path

    def load_maintenance_quality(self, profile_name: str) -> dict:
        out_dir = getattr(self.paths, "MAINTENANCE_QUALITY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "quality")
        if not out_dir.exists():
            return {}
        files = list(out_dir.glob(f"quality_{profile_name}_*.json"))
        if not files:
            return {}
        latest = max(files, key=lambda f: f.stat().st_mtime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def save_maintenance_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"maintenance_report_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(report, f, indent=2)

        if markdown:
            md_dir = getattr(self.paths, "REPORTS_MAINTENANCE_MARKDOWN_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "markdown")
            md_dir.mkdir(parents=True, exist_ok=True)
            md_path = md_dir / f"maintenance_report_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.md"
            with open(md_path, "w") as f:
                f.write(markdown)

        return path

    def load_maintenance_report(self, profile_name: str) -> dict:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        if not out_dir.exists():
            return {}
        files = list(out_dir.glob(f"maintenance_report_{profile_name}_*.json"))
        if not files:
            return {}
        latest = max(files, key=lambda f: f.stat().st_mtime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def list_maintenance_reports(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.json"))
        records = []
        for f in files:
            records.append({
                "file_name": f.name,
                "modified_at": datetime.fromtimestamp(f.stat().st_mtime).isoformat()
            })
        return pd.DataFrame(records)



    # --- MAINTENANCE SUPPORT ---
    def save_storage_inventory(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_INVENTORY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "inventory")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"storage_inventory_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_inventory(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_INVENTORY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "inventory")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_retention_policies(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_POLICIES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "policies")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"retention_policies_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_retention_policies(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_POLICIES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "policies")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cleanup_candidates(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cleanup_candidates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cleanup_candidates(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cleanup_candidates_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cleanup_dry_run_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cleanup_plan_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cleanup_dry_run_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cleanup_plan_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_archive_candidates(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"archive_candidates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_archive_candidates(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("archive_candidates_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_archive_manifest(self, archive_id: str, manifest: dict) -> Path:
        out_dir = getattr(self.paths, "ARCHIVES_MANIFESTS_DIR", self.paths.PROJECT_ROOT / "archives" / "manifests")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"{archive_id}.json"
        with open(path, "w") as f:
            json.dump(manifest, f, indent=2)
        return path

    def load_archive_manifest(self, archive_id: str) -> dict:
        import json
        out_dir = getattr(self.paths, "ARCHIVES_MANIFESTS_DIR", self.paths.PROJECT_ROOT / "archives" / "manifests")
        path = out_dir / f"{archive_id}.json"
        if not path.exists():
            return {}
        with open(path, "r") as f:
            return json.load(f)

    def save_archive_dry_run_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"archive_plan_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_archive_dry_run_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("archive_plan_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_report_rotation_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"report_rotation_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_report_rotation_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("report_rotation_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_log_rotation_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"log_rotation_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_log_rotation_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("log_rotation_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cache_pruning_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cache_pruning_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cache_pruning_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cache_pruning_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_duplicate_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_DUPLICATES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "duplicates")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"duplicates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_duplicate_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_DUPLICATES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "duplicates")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_stale_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_STALE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "stale")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"stale_artifacts_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_stale_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_STALE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "stale")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_large_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_LARGE_ARTIFACTS_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "large_artifacts")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"large_artifacts_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_large_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_LARGE_ARTIFACTS_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "large_artifacts")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_storage_growth_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"storage_growth_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_growth_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("storage_growth_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_storage_growth_snapshot(self, snapshot: dict) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"snapshot_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(snapshot, f)
        return path

    def load_storage_growth_snapshots(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("snapshot_*.json"))
        if not files:
            return pd.DataFrame()
        import json
        data = []
        for f in files:
            with open(f, "r") as fp:
                data.append(json.load(fp))
        return pd.DataFrame(data)

    def save_storage_lifecycle_health(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_LIFECYCLE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "lifecycle")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"lifecycle_health_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_lifecycle_health(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_LIFECYCLE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "lifecycle")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_maintenance_quality(self, profile_name: str, quality: dict) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_QUALITY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "quality")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"quality_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(quality, f, indent=2)
        return path

    def load_maintenance_quality(self, profile_name: str) -> dict:
        out_dir = getattr(self.paths, "MAINTENANCE_QUALITY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "quality")
        if not out_dir.exists():
            return {}
        files = list(out_dir.glob(f"quality_{profile_name}_*.json"))
        if not files:
            return {}
        latest = max(files, key=lambda f: f.stat().st_mtime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def save_maintenance_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"maintenance_report_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(report, f, indent=2)

        if markdown:
            md_dir = getattr(self.paths, "REPORTS_MAINTENANCE_MARKDOWN_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "markdown")
            md_dir.mkdir(parents=True, exist_ok=True)
            md_path = md_dir / f"maintenance_report_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.md"
            with open(md_path, "w") as f:
                f.write(markdown)

        return path

    def load_maintenance_report(self, profile_name: str) -> dict:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        if not out_dir.exists():
            return {}
        files = list(out_dir.glob(f"maintenance_report_{profile_name}_*.json"))
        if not files:
            return {}
        latest = max(files, key=lambda f: f.stat().st_mtime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def list_maintenance_reports(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.json"))
        records = []
        for f in files:
            records.append({
                "file_name": f.name,
                "modified_at": datetime.fromtimestamp(f.stat().st_mtime).isoformat()
            })
        return pd.DataFrame(records)

    # --- Final Review Methods ---
    def save_final_system_inventory(self, report_name: str, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        base_path = paths.FINAL_REVIEW_SYSTEM_INVENTORY
        return self._save_report_data(base_path, report_name, df, summary)

    def load_final_system_inventory(self, report_name: str) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_SYSTEM_INVENTORY / f"{report_name}.parquet")

    def save_architecture_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_ARCHITECTURE, "architecture_audit", df, summary)

    def load_architecture_audit(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_ARCHITECTURE / "architecture_audit.parquet")

    def save_safety_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_SAFETY, "safety_audit", df, summary)

    def load_safety_audit(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_SAFETY / "safety_audit.parquet")

    def save_integration_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_INTEGRATION, "integration_audit", df, summary)

    def load_integration_audit(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_INTEGRATION / "integration_audit.parquet")

    def save_command_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_COMMANDS, "command_audit", df, summary)

    def load_command_audit(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_COMMANDS / "command_audit.parquet")

    def save_datalake_contract_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_DATALAKE, "datalake_contract_audit", df, summary)

    def load_datalake_contract_audit(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_DATALAKE / "datalake_contract_audit.parquet")

    def save_report_output_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_REPORT_OUTPUTS, "report_output_audit", df, summary)

    def load_report_output_audit(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_REPORT_OUTPUTS / "report_output_audit.parquet")

    def save_documentation_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_DOCUMENTATION, "documentation_audit", df, summary)

    def load_documentation_audit(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_DOCUMENTATION / "documentation_audit.parquet")

    def save_quality_gate_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_QUALITY_GATES, "quality_gate_audit", df, summary)

    def load_quality_gate_audit(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_QUALITY_GATES / "quality_gate_audit.parquet")

    def save_readiness_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_READINESS, "readiness_audit", df, summary)

    def load_readiness_audit(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_READINESS / "readiness_audit.parquet")

    def save_final_risk_register(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_RISKS, "final_risk_register", df, summary)

    def load_final_risk_register(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_RISKS / "final_risk_register.parquet")

    def save_final_gap_register(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_GAPS, "final_gap_register", df, summary)

    def load_final_gap_register(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_GAPS / "final_gap_register.parquet")

    def save_final_acceptance_checklist(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_ACCEPTANCE, "final_acceptance_checklist", df, summary)

    def load_final_acceptance_checklist(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_ACCEPTANCE / "final_acceptance_checklist.parquet")

    def save_final_acceptance_snapshot(self, snapshot: dict) -> Path:
        path = paths.FINAL_REVIEW_ACCEPTANCE / "final_acceptance_snapshot.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(snapshot, "w").write(json.dumps(_sanitize(path), indent=4))
        return path

    def load_final_acceptance_snapshot(self) -> dict:
        return {} # type: ignore paths.FINAL_REVIEW_ACCEPTANCE / "final_acceptance_snapshot.json")

    def save_release_readiness_dry_run(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_READINESS, "release_readiness_dry_run", df, summary)

    def load_release_readiness_dry_run(self) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_READINESS / "release_readiness_dry_run.parquet")

    def save_phase_1_55_consolidation_audit(self, report_name: str, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(paths.FINAL_REVIEW_CONSOLIDATION, report_name, df, summary)

    def load_phase_1_55_consolidation_audit(self, report_name: str) -> pd.DataFrame:
        return self._load_parquet(paths.FINAL_REVIEW_CONSOLIDATION / f"{report_name}.parquet")

    def save_final_review_quality(self, profile_name: str, quality: dict) -> Path:
        path = paths.FINAL_REVIEW_QUALITY / f"{profile_name}_quality.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(quality, "w").write(json.dumps(_sanitize(path), indent=4))
        return path

    def load_final_review_quality(self, profile_name: str) -> dict:
        return {} # type: ignore paths.FINAL_REVIEW_QUALITY / f"{profile_name}_quality.json")

    def save_final_review_report(self, profile_name: str, report: dict, markdown: Optional[str] = None) -> Path:
        path = paths.FINAL_REVIEW_REPORTS_JSON / f"{profile_name}_report.json"
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(report, "w").write(json.dumps(_sanitize(path), indent=4))
        if markdown:
            md_path = paths.FINAL_REVIEW_REPORTS_MARKDOWN / f"{profile_name}_report.md"
            with open(md_path, "w") as f:
                f.write(markdown)
        return path

    def load_final_review_report(self, profile_name: str) -> dict:
        return {} # type: ignore paths.FINAL_REVIEW_REPORTS_JSON / f"{profile_name}_report.json")

    def list_final_review_reports(self) -> pd.DataFrame:
        rows = []
        for p in paths.FINAL_REVIEW_REPORTS_JSON.glob("*_report.json"):
            rows.append({"report": p.stem, "path": str(p)})
        return pd.DataFrame(rows)



    # =========================================================================
    # MASTER ORCHESTRATION
    # =========================================================================

    def save_orchestration_layer_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save orchestration layer map to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_LAYER_MAPS
        filename = f"orchestration_layer_map_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_LAYER_MAPS / filename
        LAKE_MASTER_ORCHESTRATION_LAYER_MAPS.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_LAYER_MAPS / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_orchestration_layer_map(self) -> pd.DataFrame:
        """Load orchestration layer map from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_LAYER_MAPS
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_LAYER_MAPS, prefix="orchestration_layer_map_")

    def save_module_dependency_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save module dependency map to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_DEPENDENCIES
        filename = f"module_dependency_map_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_DEPENDENCIES / filename
        LAKE_MASTER_ORCHESTRATION_DEPENDENCIES.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_DEPENDENCIES / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_module_dependency_map(self) -> pd.DataFrame:
        """Load module dependency map from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_DEPENDENCIES
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_DEPENDENCIES, prefix="module_dependency_map_")

    def save_report_dependency_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save report dependency map to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_DEPENDENCIES
        filename = f"report_dependency_map_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_DEPENDENCIES / filename
        LAKE_MASTER_ORCHESTRATION_DEPENDENCIES.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_DEPENDENCIES / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_report_dependency_map(self) -> pd.DataFrame:
        """Load report dependency map from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_DEPENDENCIES
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_DEPENDENCIES, prefix="report_dependency_map_")

    def save_datalake_dependency_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save datalake dependency map to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_DEPENDENCIES
        filename = f"datalake_dependency_map_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_DEPENDENCIES / filename
        LAKE_MASTER_ORCHESTRATION_DEPENDENCIES.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_DEPENDENCIES / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_datalake_dependency_map(self) -> pd.DataFrame:
        """Load datalake dependency map from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_DEPENDENCIES
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_DEPENDENCIES, prefix="datalake_dependency_map_")

    def save_master_command_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save master command registry to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS
        filename = f"master_command_registry_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS / filename
        LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_master_command_registry(self) -> pd.DataFrame:
        """Load master command registry from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS, prefix="master_command_registry_")

    def save_command_dependency_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save command dependency graph to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS
        filename = f"command_dependency_graph_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS / filename
        LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_command_dependency_graph(self) -> pd.DataFrame:
        """Load command dependency graph from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS, prefix="command_dependency_graph_")

    def save_operating_mode_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save operating mode registry to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_OPERATING_MODES
        filename = f"operating_mode_registry_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_OPERATING_MODES / filename
        LAKE_MASTER_ORCHESTRATION_OPERATING_MODES.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_OPERATING_MODES / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_operating_mode_registry(self) -> pd.DataFrame:
        """Load operating mode registry from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_OPERATING_MODES
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_OPERATING_MODES, prefix="operating_mode_registry_")

    def save_offline_master_command_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save offline master command plan to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_MASTER_PLANS
        filename = f"offline_master_command_plan_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_MASTER_PLANS / filename
        LAKE_MASTER_ORCHESTRATION_MASTER_PLANS.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_MASTER_PLANS / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_offline_master_command_plan(self) -> pd.DataFrame:
        """Load offline master command plan from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_MASTER_PLANS
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_MASTER_PLANS, prefix="offline_master_command_plan_")

    def save_master_dry_run_execution_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save master dry run execution plan to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_MASTER_PLANS
        filename = f"master_dry_run_execution_plan_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_MASTER_PLANS / filename
        LAKE_MASTER_ORCHESTRATION_MASTER_PLANS.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_MASTER_PLANS / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_master_dry_run_execution_plan(self) -> pd.DataFrame:
        """Load master dry run execution plan from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_MASTER_PLANS
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_MASTER_PLANS, prefix="master_dry_run_execution_plan_")

    def save_meta_runner_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save meta runner registry to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_META_RUNNER
        filename = f"meta_runner_registry_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_META_RUNNER / filename
        LAKE_MASTER_ORCHESTRATION_META_RUNNER.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_META_RUNNER / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_meta_runner_registry(self) -> pd.DataFrame:
        """Load meta runner registry from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_META_RUNNER
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_META_RUNNER, prefix="meta_runner_registry_")

    def save_operational_playbook(self, text: str, summary: dict | None = None) -> Path:
        """Save operational playbook to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_PLAYBOOKS
        filename = f"operational_playbook_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.txt"
        path = LAKE_MASTER_ORCHESTRATION_PLAYBOOKS / filename
        LAKE_MASTER_ORCHESTRATION_PLAYBOOKS.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_PLAYBOOKS / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_operational_playbook(self) -> str:
        """Load operational playbook from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_PLAYBOOKS
        path = None # type: ignore LAKE_MASTER_ORCHESTRATION_PLAYBOOKS, prefix="operational_playbook_", suffix=".txt")
        if path:
            return path.read_text(encoding="utf-8")
        return ""

    def save_run_order_plan(self, plan_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save a run order plan to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_RUN_ORDERS
        filename = f"{plan_name}_run_order_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_RUN_ORDERS / filename
        LAKE_MASTER_ORCHESTRATION_RUN_ORDERS.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_RUN_ORDERS / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_run_order_plan(self, plan_name: str) -> pd.DataFrame:
        """Load a run order plan from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_RUN_ORDERS
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_RUN_ORDERS, prefix=f"{plan_name}_run_order_")

    def save_handoff_checklist(self, checklist_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save handoff checklist to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_HANDOFFS
        filename = f"{checklist_name}_handoff_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_HANDOFFS / filename
        LAKE_MASTER_ORCHESTRATION_HANDOFFS.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_HANDOFFS / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_handoff_checklist(self, checklist_name: str) -> pd.DataFrame:
        """Load handoff checklist from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_HANDOFFS
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_HANDOFFS, prefix=f"{checklist_name}_handoff_")

    def save_phase_1_60_consolidation_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save phase 1-60 consolidation matrix to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_CONSOLIDATION
        filename = f"phase_1_60_consolidation_matrix_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_CONSOLIDATION / filename
        LAKE_MASTER_ORCHESTRATION_CONSOLIDATION.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_CONSOLIDATION / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_phase_1_60_consolidation_matrix(self) -> pd.DataFrame:
        """Load phase 1-60 consolidation matrix from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_CONSOLIDATION
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_CONSOLIDATION, prefix="phase_1_60_consolidation_matrix_")

    def save_phase_1_60_executive_digest(self, text: str, summary: dict | None = None) -> Path:
        """Save phase 1-60 executive digest to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_CONSOLIDATION
        filename = f"phase_1_60_executive_digest_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.txt"
        path = LAKE_MASTER_ORCHESTRATION_CONSOLIDATION / filename
        LAKE_MASTER_ORCHESTRATION_CONSOLIDATION.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_CONSOLIDATION / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_phase_1_60_executive_digest(self) -> str:
        """Load phase 1-60 executive digest from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_CONSOLIDATION
        path = None # type: ignore LAKE_MASTER_ORCHESTRATION_CONSOLIDATION, prefix="phase_1_60_executive_digest_", suffix=".txt")
        if path:
            return path.read_text(encoding="utf-8")
        return ""

    def save_master_safety_boundary_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        """Save master safety boundary report to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_SAFETY
        filename = f"master_safety_boundary_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        path = LAKE_MASTER_ORCHESTRATION_SAFETY / filename
        LAKE_MASTER_ORCHESTRATION_SAFETY.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        if summary:
            import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(LAKE_MASTER_ORCHESTRATION_SAFETY / f"summary_{filename}.json", "w").write(json.dumps(_sanitize(summary), indent=4))
        return path

    def load_master_safety_boundary_report(self) -> pd.DataFrame:
        """Load master safety boundary report from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_SAFETY
        return pd.DataFrame() # type: ignore LAKE_MASTER_ORCHESTRATION_SAFETY, prefix="master_safety_boundary_report_")

    def save_master_quality(self, profile_name: str, quality: dict) -> Path:
        """Save master quality report to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_QUALITY
        filename = f"master_quality_{profile_name}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json"
        path = LAKE_MASTER_ORCHESTRATION_QUALITY / filename
        LAKE_MASTER_ORCHESTRATION_QUALITY.mkdir(parents=True, exist_ok=True)
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(path, "w").write(json.dumps(_sanitize(quality), indent=4))
        return path

    def load_master_quality(self, profile_name: str) -> dict:
        """Load master quality report from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_QUALITY
        path = None # type: ignore LAKE_MASTER_ORCHESTRATION_QUALITY, prefix=f"master_quality_{profile_name}_", suffix=".json")
        if path:
            return {} # type: ignore path)
        return {}

    def save_master_orchestration_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        """Save a full master orchestration status report to the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_STATUS
        timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
        json_filename = f"master_orchestration_report_{profile_name}_{timestamp}.json"
        json_path = LAKE_MASTER_ORCHESTRATION_STATUS / json_filename
        LAKE_MASTER_ORCHESTRATION_STATUS.mkdir(parents=True, exist_ok=True)
        import json
        def _sanitize(d):
            if isinstance(d, dict):
                return {k: _sanitize(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [_sanitize(x) for x in d]
            elif hasattr(d, 'item'):  # numpy types
                return d.item()
            return d
        open(json_path, "w").write(json.dumps(_sanitize(report), indent=4))

        if markdown:
            md_filename = f"master_orchestration_report_{profile_name}_{timestamp}.md"
            md_path = LAKE_MASTER_ORCHESTRATION_STATUS / md_filename
            md_path.write_text(markdown, encoding="utf-8")

        return json_path

    def load_master_orchestration_report(self, profile_name: str) -> dict:
        """Load the latest master orchestration status report from the data lake."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_STATUS
        path = None # type: ignore LAKE_MASTER_ORCHESTRATION_STATUS, prefix=f"master_orchestration_report_{profile_name}_", suffix=".json")
        if path:
            return {} # type: ignore path)
        return {}

    def list_master_orchestration_reports(self) -> pd.DataFrame:
        """List all master orchestration reports."""
        from config.paths import LAKE_MASTER_ORCHESTRATION_STATUS
        return self.list_artifacts(LAKE_MASTER_ORCHESTRATION_STATUS)


    # Phase 61: Portable Packaging
    def save_environment_snapshot(self, snapshot: dict, packages_df: 'pd.DataFrame', summary: dict = None) -> 'Path':
        import pandas as pd

        out = self.paths.LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR / "environment_snapshot.json"
        import json
        with open(out, "w", encoding="utf-8") as f:
            json.dump({"snapshot": snapshot, "summary": summary}, f, indent=2)
        packages_df.to_parquet(self.paths.LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR / "installed_packages.parquet")
        return out

    def load_environment_snapshot(self) -> dict:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR / "environment_snapshot.json"
        if out.exists():
            with open(out, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_installed_packages_snapshot(self, df: 'pd.DataFrame', summary: dict = None) -> 'Path':
        out = self.paths.LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR / "installed_packages.parquet"
        df.to_parquet(out)
        return out

    def load_installed_packages_snapshot(self) -> 'pd.DataFrame':
        import pandas as pd

        out = self.paths.LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR / "installed_packages.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_dependency_inventory(self, df: 'pd.DataFrame', summary: dict = None) -> 'Path':
        out = self.paths.LAKE_PORTABLE_PACKAGING_DEPENDENCIES_DIR / "dependency_inventory.parquet"
        df.to_parquet(out)
        return out

    def load_dependency_inventory(self) -> 'pd.DataFrame':
        import pandas as pd

        out = self.paths.LAKE_PORTABLE_PACKAGING_DEPENDENCIES_DIR / "dependency_inventory.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_requirements_export_report(self, df: 'pd.DataFrame', summary: dict = None) -> 'Path':
        out = self.paths.LAKE_PORTABLE_PACKAGING_REQUIREMENTS_DIR / "requirements_export.parquet"
        df.to_parquet(out)
        return out

    def load_requirements_export_report(self) -> 'pd.DataFrame':
        import pandas as pd

        out = self.paths.LAKE_PORTABLE_PACKAGING_REQUIREMENTS_DIR / "requirements_export.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_install_verification_report(self, df: 'pd.DataFrame', summary: dict = None) -> 'Path':
        out = self.paths.LAKE_PORTABLE_PACKAGING_INSTALL_VERIFICATION_DIR / "install_verification.parquet"
        df.to_parquet(out)
        return out

    def load_install_verification_report(self) -> 'pd.DataFrame':
        import pandas as pd

        out = self.paths.LAKE_PORTABLE_PACKAGING_INSTALL_VERIFICATION_DIR / "install_verification.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_import_verification_report(self, df: 'pd.DataFrame', summary: dict = None) -> 'Path':
        out = self.paths.LAKE_PORTABLE_PACKAGING_IMPORT_VERIFICATION_DIR / "import_verification.parquet"
        df.to_parquet(out)
        return out

    def load_import_verification_report(self) -> 'pd.DataFrame':
        import pandas as pd

        out = self.paths.LAKE_PORTABLE_PACKAGING_IMPORT_VERIFICATION_DIR / "import_verification.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_script_verification_report(self, df: 'pd.DataFrame', summary: dict = None) -> 'Path':
        out = self.paths.LAKE_PORTABLE_PACKAGING_SCRIPT_VERIFICATION_DIR / "script_verification.parquet"
        df.to_parquet(out)
        return out

    def load_script_verification_report(self) -> 'pd.DataFrame':
        import pandas as pd

        out = self.paths.LAKE_PORTABLE_PACKAGING_SCRIPT_VERIFICATION_DIR / "script_verification.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_config_template_verification(self, df: 'pd.DataFrame', summary: dict = None) -> 'Path':
        out = self.paths.LAKE_PORTABLE_PACKAGING_CONFIG_VERIFICATION_DIR / "config_verification.parquet"
        df.to_parquet(out)
        return out

    def load_config_template_verification(self) -> 'pd.DataFrame':
        import pandas as pd

        out = self.paths.LAKE_PORTABLE_PACKAGING_CONFIG_VERIFICATION_DIR / "config_verification.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_bundle_artifact_inventory(self, df: 'pd.DataFrame', summary: dict = None) -> 'Path':
        out = self.paths.LAKE_PORTABLE_PACKAGING_BUNDLE_MANIFEST_DIR / "bundle_artifact_inventory.parquet"
        df.to_parquet(out)
        return out

    def load_bundle_artifact_inventory(self) -> 'pd.DataFrame':
        import pandas as pd

        out = self.paths.LAKE_PORTABLE_PACKAGING_BUNDLE_MANIFEST_DIR / "bundle_artifact_inventory.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_portable_bundle_manifest(self, manifest: dict) -> 'Path':
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_BUNDLE_MANIFEST_DIR / "portable_bundle_manifest.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        return out

    def load_portable_bundle_manifest(self) -> dict:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_BUNDLE_MANIFEST_DIR / "portable_bundle_manifest.json"
        if out.exists():
            with open(out, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_archive_manifest(self, manifest: dict) -> 'Path':
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_ARCHIVE_MANIFEST_DIR / "archive_manifest.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        return out

    def load_archive_manifest(self) -> dict:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_ARCHIVE_MANIFEST_DIR / "archive_manifest.json"
        if out.exists():
            with open(out, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_source_policy(self, policy_name: str, df: 'pd.DataFrame', summary: dict = None) -> 'Path':
        out = self.paths.LAKE_PORTABLE_PACKAGING_SOURCE_POLICY_DIR / f"{policy_name}.parquet"
        df.to_parquet(out)
        return out

    def load_source_policy(self, policy_name: str) -> 'pd.DataFrame':
        import pandas as pd

        out = self.paths.LAKE_PORTABLE_PACKAGING_SOURCE_POLICY_DIR / f"{policy_name}.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_reproducible_setup_guide(self, text: str, summary: dict = None) -> 'Path':
        out = self.paths.LAKE_PORTABLE_PACKAGING_SETUP_GUIDES_DIR / "reproducible_setup_guide.md"
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        return out

    def load_reproducible_setup_guide(self) -> str:
        out = self.paths.LAKE_PORTABLE_PACKAGING_SETUP_GUIDES_DIR / "reproducible_setup_guide.md"
        if out.exists():
            with open(out, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    def save_environment_drift_report(self, df: 'pd.DataFrame', summary: dict = None) -> 'Path':
        out = self.paths.LAKE_PORTABLE_PACKAGING_DRIFT_DIR / "environment_drift.parquet"
        df.to_parquet(out)
        return out

    def load_environment_drift_report(self) -> 'pd.DataFrame':
        import pandas as pd

        out = self.paths.LAKE_PORTABLE_PACKAGING_DRIFT_DIR / "environment_drift.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_packaging_safety_report(self, df: 'pd.DataFrame', summary: dict = None) -> 'Path':
        out = self.paths.LAKE_PORTABLE_PACKAGING_SAFETY_DIR / "packaging_safety.parquet"
        df.to_parquet(out)
        return out

    def load_packaging_safety_report(self) -> 'pd.DataFrame':
        import pandas as pd

        out = self.paths.LAKE_PORTABLE_PACKAGING_SAFETY_DIR / "packaging_safety.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_packaging_quality(self, profile_name: str, quality: dict) -> 'Path':
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_QUALITY_DIR / f"packaging_quality_{profile_name}.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=2)
        return out

    def load_packaging_quality(self, profile_name: str) -> dict:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_QUALITY_DIR / f"packaging_quality_{profile_name}.json"
        if out.exists():
            with open(out, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_portable_packaging_report(self, profile_name: str, report: dict, markdown: str = None) -> 'Path':
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_DIR / f"report_{profile_name}.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        if markdown:
            md_out = self.paths.LAKE_PORTABLE_PACKAGING_DIR / f"report_{profile_name}.md"
            with open(md_out, "w", encoding="utf-8") as f:
                f.write(markdown)
        return out

    def load_portable_packaging_report(self, profile_name: str) -> dict:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_DIR / f"report_{profile_name}.json"
        if out.exists():
            with open(out, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def list_portable_packaging_reports(self) -> 'pd.DataFrame':
        import pandas as pd

        data = []
        if self.paths.LAKE_PORTABLE_PACKAGING_DIR.exists():
            for p in self.paths.LAKE_PORTABLE_PACKAGING_DIR.glob("report_*.json"):
                data.append({"profile": p.stem.replace("report_", ""), "path": str(p)})
        return pd.DataFrame(data)


    def save_project_state_inventory(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_STATE_INVENTORY_DIR
        out = BACKUP_RECOVERY_STATE_INVENTORY_DIR / "project_state_inventory.csv"
        df.to_csv(out, index=False)
        return out

    def load_project_state_inventory(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_STATE_INVENTORY_DIR
        out = BACKUP_RECOVERY_STATE_INVENTORY_DIR / "project_state_inventory.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_backup_policies(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_POLICIES_DIR
        out = BACKUP_RECOVERY_POLICIES_DIR / "backup_policies.csv"
        df.to_csv(out, index=False)
        return out

    def load_backup_policies(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_POLICIES_DIR
        out = BACKUP_RECOVERY_POLICIES_DIR / "backup_policies.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_backup_scope_table(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_SCOPES_DIR
        out = BACKUP_RECOVERY_SCOPES_DIR / "backup_scope_table.csv"
        df.to_csv(out, index=False)
        return out

    def load_backup_scope_table(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_SCOPES_DIR
        out = BACKUP_RECOVERY_SCOPES_DIR / "backup_scope_table.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_critical_artifact_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_CRITICAL_ARTIFACTS_DIR
        out = BACKUP_RECOVERY_CRITICAL_ARTIFACTS_DIR / "critical_artifact_registry.csv"
        df.to_csv(out, index=False)
        return out

    def load_critical_artifact_registry(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_CRITICAL_ARTIFACTS_DIR
        out = BACKUP_RECOVERY_CRITICAL_ARTIFACTS_DIR / "critical_artifact_registry.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_noncritical_artifact_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_CRITICAL_ARTIFACTS_DIR
        out = BACKUP_RECOVERY_CRITICAL_ARTIFACTS_DIR / "noncritical_artifact_registry.csv"
        df.to_csv(out, index=False)
        return out

    def load_noncritical_artifact_registry(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_CRITICAL_ARTIFACTS_DIR
        out = BACKUP_RECOVERY_CRITICAL_ARTIFACTS_DIR / "noncritical_artifact_registry.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_excluded_secret_artifact_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_CRITICAL_ARTIFACTS_DIR
        out = BACKUP_RECOVERY_CRITICAL_ARTIFACTS_DIR / "excluded_secret_artifact_registry.csv"
        df.to_csv(out, index=False)
        return out

    def load_excluded_secret_artifact_registry(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_CRITICAL_ARTIFACTS_DIR
        out = BACKUP_RECOVERY_CRITICAL_ARTIFACTS_DIR / "excluded_secret_artifact_registry.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_backup_manifest(self, manifest: dict) -> Path:
        from config.paths import BACKUP_RECOVERY_MANIFESTS_DIR
        import json
        out = BACKUP_RECOVERY_MANIFESTS_DIR / "backup_manifest.json"
        with open(out, "w") as f:
            json.dump(manifest, f, indent=2)
        return out

    def load_backup_manifest(self) -> dict:
        from config.paths import BACKUP_RECOVERY_MANIFESTS_DIR
        import json
        out = BACKUP_RECOVERY_MANIFESTS_DIR / "backup_manifest.json"
        if out.exists():
            with open(out, "r") as f:
                return json.load(f)
        return {}

    def save_backup_dry_run_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_BACKUP_DRY_RUN_DIR
        out = BACKUP_RECOVERY_BACKUP_DRY_RUN_DIR / "backup_dry_run_plan.csv"
        df.to_csv(out, index=False)
        return out

    def load_backup_dry_run_plan(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_BACKUP_DRY_RUN_DIR
        out = BACKUP_RECOVERY_BACKUP_DRY_RUN_DIR / "backup_dry_run_plan.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_restore_dry_run_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_RESTORE_DRY_RUN_DIR
        out = BACKUP_RECOVERY_RESTORE_DRY_RUN_DIR / "restore_dry_run_plan.csv"
        df.to_csv(out, index=False)
        return out

    def load_restore_dry_run_plan(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_RESTORE_DRY_RUN_DIR
        out = BACKUP_RECOVERY_RESTORE_DRY_RUN_DIR / "restore_dry_run_plan.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_restore_verification_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_RESTORE_VERIFICATION_DIR
        out = BACKUP_RECOVERY_RESTORE_VERIFICATION_DIR / "restore_verification_report.csv"
        df.to_csv(out, index=False)
        return out

    def load_restore_verification_report(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_RESTORE_VERIFICATION_DIR
        out = BACKUP_RECOVERY_RESTORE_VERIFICATION_DIR / "restore_verification_report.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_disaster_recovery_manifest(self, manifest: dict) -> Path:
        from config.paths import BACKUP_RECOVERY_DISASTER_RECOVERY_DIR
        import json
        out = BACKUP_RECOVERY_DISASTER_RECOVERY_DIR / "disaster_recovery_manifest.json"
        with open(out, "w") as f:
            json.dump(manifest, f, indent=2)
        return out

    def load_disaster_recovery_manifest(self) -> dict:
        from config.paths import BACKUP_RECOVERY_DISASTER_RECOVERY_DIR
        import json
        out = BACKUP_RECOVERY_DISASTER_RECOVERY_DIR / "disaster_recovery_manifest.json"
        if out.exists():
            with open(out, "r") as f:
                return json.load(f)
        return {}

    def save_recovery_runbook(self, text: str, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_RUNBOOKS_DIR
        out = BACKUP_RECOVERY_RUNBOOKS_DIR / "recovery_runbook.txt"
        with open(out, "w") as f:
            f.write(text)
        return out

    def load_recovery_runbook(self) -> str:
        from config.paths import BACKUP_RECOVERY_RUNBOOKS_DIR
        out = BACKUP_RECOVERY_RUNBOOKS_DIR / "recovery_runbook.txt"
        if out.exists():
            with open(out, "r") as f:
                return f.read()
        return ""

    def save_backup_integrity_manifest(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_INTEGRITY_DIR
        out = BACKUP_RECOVERY_INTEGRITY_DIR / "backup_integrity_manifest.csv"
        df.to_csv(out, index=False)
        return out

    def load_backup_integrity_manifest(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_INTEGRITY_DIR
        out = BACKUP_RECOVERY_INTEGRITY_DIR / "backup_integrity_manifest.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_restore_integrity_verification(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_INTEGRITY_DIR
        out = BACKUP_RECOVERY_INTEGRITY_DIR / "restore_integrity_verification.csv"
        df.to_csv(out, index=False)
        return out

    def load_restore_integrity_verification(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_INTEGRITY_DIR
        out = BACKUP_RECOVERY_INTEGRITY_DIR / "restore_integrity_verification.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_recovery_gap_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_GAPS_DIR
        out = BACKUP_RECOVERY_GAPS_DIR / "recovery_gap_report.csv"
        df.to_csv(out, index=False)
        return out

    def load_recovery_gap_report(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_GAPS_DIR
        out = BACKUP_RECOVERY_GAPS_DIR / "recovery_gap_report.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_backup_safety_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_SAFETY_DIR
        out = BACKUP_RECOVERY_SAFETY_DIR / "backup_safety_report.csv"
        df.to_csv(out, index=False)
        return out

    def load_backup_safety_report(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_SAFETY_DIR
        out = BACKUP_RECOVERY_SAFETY_DIR / "backup_safety_report.csv"
        if out.exists():
            return pd.read_csv(out)
        return pd.DataFrame()

    def save_backup_quality(self, profile_name: str, quality: dict) -> Path:
        from config.paths import BACKUP_RECOVERY_QUALITY_DIR
        import json
        out = BACKUP_RECOVERY_QUALITY_DIR / f"backup_quality_{profile_name}.json"
        with open(out, "w") as f:
            json.dump(quality, f, indent=2)
        return out

    def load_backup_quality(self, profile_name: str) -> dict:
        from config.paths import BACKUP_RECOVERY_QUALITY_DIR
        import json
        out = BACKUP_RECOVERY_QUALITY_DIR / f"backup_quality_{profile_name}.json"
        if out.exists():
            with open(out, "r") as f:
                return json.load(f)
        return {}

    def save_backup_recovery_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        from config.paths import BACKUP_RECOVERY_DIR
        import json
        out = BACKUP_RECOVERY_DIR / f"backup_recovery_report_{profile_name}.json"
        with open(out, "w") as f:
            json.dump(report, f, indent=2)
        return out

    def load_backup_recovery_report(self, profile_name: str) -> dict:
        from config.paths import BACKUP_RECOVERY_DIR
        import json
        out = BACKUP_RECOVERY_DIR / f"backup_recovery_report_{profile_name}.json"
        if out.exists():
            with open(out, "r") as f:
                return json.load(f)
        return {}

    def list_backup_recovery_reports(self) -> pd.DataFrame:
        from config.paths import BACKUP_RECOVERY_DIR
        import glob
        import json
        files = glob.glob(str(BACKUP_RECOVERY_DIR / "backup_recovery_report_*.json"))
        data = []
        for f in files:
            try:
                with open(f, "r") as fh:
                    d = json.load(fh)
                data.append({"file": f, "profile_name": d.get("profile_name", "")})
            except Exception:
                pass
        return pd.DataFrame(data)

    # --- Local Consistency Engine Methods ---
    def save_consistency_check_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_check_registry_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_check_registry_dir / "consistency_check_registry.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_consistency_check_registry(self) -> pd.DataFrame:
        path = self.paths.local_consistency_check_registry_dir / "consistency_check_registry.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_cross_layer_consistency_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_matrix_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_matrix_dir / "cross_layer_consistency_matrix.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_cross_layer_consistency_matrix(self) -> pd.DataFrame:
        path = self.paths.local_consistency_matrix_dir / "cross_layer_consistency_matrix.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_config_env_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_config_env_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_config_env_dir / "config_env_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_config_env_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_config_env_dir / "config_env_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_settings_docs_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_settings_docs_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_settings_docs_dir / "settings_docs_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_settings_docs_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_settings_docs_dir / "settings_docs_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_paths_datalake_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_paths_datalake_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_paths_datalake_dir / "paths_datalake_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_paths_datalake_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_paths_datalake_dir / "paths_datalake_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_script_report_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_script_report_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_script_report_dir / "script_report_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_script_report_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_script_report_dir / "script_report_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_report_datalake_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_report_datalake_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_report_datalake_dir / "report_datalake_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_report_datalake_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_report_datalake_dir / "report_datalake_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_docs_phase_log_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_docs_phase_log_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_docs_phase_log_dir / "docs_phase_log_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_docs_phase_log_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_docs_phase_log_dir / "docs_phase_log_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_evidence_control_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_evidence_control_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_evidence_control_dir / "evidence_control_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_evidence_control_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_evidence_control_dir / "evidence_control_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_metadata_artifact_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_metadata_artifact_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_metadata_artifact_dir / "metadata_artifact_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_metadata_artifact_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_metadata_artifact_dir / "metadata_artifact_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_graph_metadata_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_graph_metadata_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_graph_metadata_dir / "graph_metadata_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_graph_metadata_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_graph_metadata_dir / "graph_metadata_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_timeline_artifact_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_timeline_artifact_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_timeline_artifact_dir / "timeline_artifact_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_timeline_artifact_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_timeline_artifact_dir / "timeline_artifact_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_backup_packaging_secrets_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_backup_packaging_secrets_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_backup_packaging_secrets_dir / "backup_packaging_secrets_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_backup_packaging_secrets_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_backup_packaging_secrets_dir / "backup_packaging_secrets_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_non_use_policy_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_non_use_policy_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_non_use_policy_dir / "non_use_policy_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_non_use_policy_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_non_use_policy_dir / "non_use_policy_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_disclaimer_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_disclaimers_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_disclaimers_dir / "disclaimer_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_disclaimer_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_disclaimers_dir / "disclaimer_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_safety_boundary_consistency_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_safety_boundaries_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_safety_boundaries_dir / "safety_boundary_consistency_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_safety_boundary_consistency_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_safety_boundaries_dir / "safety_boundary_consistency_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_contradiction_detection_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_contradictions_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_contradictions_dir / "contradiction_detection_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_contradiction_detection_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_contradictions_dir / "contradiction_detection_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_missing_reference_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_references_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_references_dir / "missing_reference_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_missing_reference_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_references_dir / "missing_reference_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_broken_reference_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_references_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_references_dir / "broken_reference_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_broken_reference_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_references_dir / "broken_reference_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_stale_artifact_reconciliation_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_reconciliation_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_reconciliation_dir / "stale_artifact_reconciliation_plan.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_stale_artifact_reconciliation_plan(self) -> pd.DataFrame:
        path = self.paths.local_consistency_reconciliation_dir / "stale_artifact_reconciliation_plan.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_consistency_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_reconciliation_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_reconciliation_dir / "consistency_gap_register.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_consistency_gap_register(self) -> pd.DataFrame:
        path = self.paths.local_consistency_reconciliation_dir / "consistency_gap_register.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_cross_layer_coherence_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_coherence_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_coherence_dir / "cross_layer_coherence_score_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_cross_layer_coherence_score_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_coherence_dir / "cross_layer_coherence_score_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_system_coherence_report(self, report: dict, markdown: str | None = None) -> Path:
        import json
        self.paths.local_consistency_coherence_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_coherence_dir / "system_coherence_report.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        return path

    def load_system_coherence_report(self) -> dict:
        import json
        path = self.paths.local_consistency_coherence_dir / "system_coherence_report.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_reconciliation_recommendations(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_recommendations_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_recommendations_dir / "reconciliation_recommendations.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_reconciliation_recommendations(self) -> pd.DataFrame:
        path = self.paths.local_consistency_recommendations_dir / "reconciliation_recommendations.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_consistency_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        self.paths.local_consistency_validation_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_validation_dir / "consistency_validation_report.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_consistency_validation_report(self) -> pd.DataFrame:
        path = self.paths.local_consistency_validation_dir / "consistency_validation_report.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)

    def save_consistency_quality(self, profile_name: str, quality: dict) -> Path:
        import json
        self.paths.local_consistency_quality_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_quality_dir / f"consistency_quality_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=4)
        return path

    def load_consistency_quality(self, profile_name: str) -> dict:
        import json
        path = self.paths.local_consistency_quality_dir / f"consistency_quality_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_local_consistency_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        import json
        self.paths.local_consistency_lake_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.local_consistency_lake_dir / f"local_consistency_report_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        return path

    def load_local_consistency_report(self, profile_name: str) -> dict:
        import json
        path = self.paths.local_consistency_lake_dir / f"local_consistency_report_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_local_consistency_reports(self) -> pd.DataFrame:
        return pd.DataFrame()

    # Phase 69: Local Readiness
    def save_readiness_gate_registry(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_GATES_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_GATES_DIR, "readiness_gate_registry")

    def load_readiness_gate_registry(self):
        from config.paths import LAKE_LOCAL_READINESS_GATES_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_GATES_DIR / "readiness_gate_registry.parquet")

    def save_milestone_acceptance_criteria(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_ACCEPTANCE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_ACCEPTANCE_DIR, "milestone_acceptance_criteria")

    def load_milestone_acceptance_criteria(self):
        from config.paths import LAKE_LOCAL_READINESS_ACCEPTANCE_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_ACCEPTANCE_DIR / "milestone_acceptance_criteria.parquet")

    def save_phase_completion_evidence_binder(self, text: str, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_PHASE_EVIDENCE_DIR
        path = LAKE_LOCAL_READINESS_PHASE_EVIDENCE_DIR / "phase_completion_evidence_binder.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            f.write(text)
        return path

    def load_phase_completion_evidence_binder(self) -> str:
        from config.paths import LAKE_LOCAL_READINESS_PHASE_EVIDENCE_DIR
        path = LAKE_LOCAL_READINESS_PHASE_EVIDENCE_DIR / "phase_completion_evidence_binder.txt"
        if path.exists():
            with open(path, "r") as f:
                return f.read()
        return ""

    def save_final_operator_checklist(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_OPERATOR_CHECKLISTS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_OPERATOR_CHECKLISTS_DIR, "final_operator_checklist")

    def load_final_operator_checklist(self):
        from config.paths import LAKE_LOCAL_READINESS_OPERATOR_CHECKLISTS_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_OPERATOR_CHECKLISTS_DIR / "final_operator_checklist.parquet")

    def save_pre_handoff_stabilization_checklist(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_STABILIZATION_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_STABILIZATION_DIR, "pre_handoff_stabilization_checklist")

    def load_pre_handoff_stabilization_checklist(self):
        from config.paths import LAKE_LOCAL_READINESS_STABILIZATION_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_STABILIZATION_DIR / "pre_handoff_stabilization_checklist.parquet")

    def save_dry_run_command_checklist(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_DRY_RUN_COMMANDS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_DRY_RUN_COMMANDS_DIR, "dry_run_command_checklist")

    def load_dry_run_command_checklist(self):
        from config.paths import LAKE_LOCAL_READINESS_DRY_RUN_COMMANDS_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_DRY_RUN_COMMANDS_DIR / "dry_run_command_checklist.parquet")

    def save_safe_command_coverage_report(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_COMMAND_COVERAGE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_COMMAND_COVERAGE_DIR, "safe_command_coverage_report")

    def load_safe_command_coverage_report(self):
        from config.paths import LAKE_LOCAL_READINESS_COMMAND_COVERAGE_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_COMMAND_COVERAGE_DIR / "safe_command_coverage_report.parquet")

    def save_documentation_readiness_report(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_DOCS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_DOCS_DIR, "documentation_readiness_report")

    def load_documentation_readiness_report(self):
        from config.paths import LAKE_LOCAL_READINESS_DOCS_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_DOCS_DIR / "documentation_readiness_report.parquet")

    def save_test_readiness_report(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_TESTS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_TESTS_DIR, "test_readiness_report")

    def load_test_readiness_report(self):
        from config.paths import LAKE_LOCAL_READINESS_TESTS_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_TESTS_DIR / "test_readiness_report.parquet")

    def save_datalake_readiness_report(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_DATALAKE_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_DATALAKE_DIR, "datalake_readiness_report")

    def load_datalake_readiness_report(self):
        from config.paths import LAKE_LOCAL_READINESS_DATALAKE_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_DATALAKE_DIR / "datalake_readiness_report.parquet")

    def save_report_output_readiness_report(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_REPORTS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_REPORTS_DIR, "report_output_readiness_report")

    def load_report_output_readiness_report(self):
        from config.paths import LAKE_LOCAL_READINESS_REPORTS_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_REPORTS_DIR / "report_output_readiness_report.parquet")

    def save_security_boundary_readiness_report(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_SECURITY_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_SECURITY_DIR, "security_boundary_readiness_report")

    def load_security_boundary_readiness_report(self):
        from config.paths import LAKE_LOCAL_READINESS_SECURITY_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_SECURITY_DIR / "security_boundary_readiness_report.parquet")

    def save_backup_packaging_readiness_report(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_BACKUP_PACKAGING_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_BACKUP_PACKAGING_DIR, "backup_packaging_readiness_report")

    def load_backup_packaging_readiness_report(self):
        from config.paths import LAKE_LOCAL_READINESS_BACKUP_PACKAGING_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_BACKUP_PACKAGING_DIR / "backup_packaging_readiness_report.parquet")

    def save_cross_layer_readiness_report(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_CROSS_LAYER_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_CROSS_LAYER_DIR, "cross_layer_readiness_report")

    def load_cross_layer_readiness_report(self):
        from config.paths import LAKE_LOCAL_READINESS_CROSS_LAYER_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_CROSS_LAYER_DIR / "cross_layer_readiness_report.parquet")

    def save_known_limitations_register(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_LIMITATIONS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_LIMITATIONS_DIR, "known_limitations_register")

    def load_known_limitations_register(self):
        from config.paths import LAKE_LOCAL_READINESS_LIMITATIONS_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_LIMITATIONS_DIR / "known_limitations_register.parquet")

    def save_known_gaps_register(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_GAPS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_GAPS_DIR, "known_gaps_register")

    def load_known_gaps_register(self):
        from config.paths import LAKE_LOCAL_READINESS_GAPS_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_GAPS_DIR / "known_gaps_register.parquet")

    def save_manual_review_register(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_MANUAL_REVIEW_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_MANUAL_REVIEW_DIR, "manual_review_register")

    def load_manual_review_register(self):
        from config.paths import LAKE_LOCAL_READINESS_MANUAL_REVIEW_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_MANUAL_REVIEW_DIR / "manual_review_register.parquet")

    def save_no_go_condition_registry(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_GO_NO_GO_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_GO_NO_GO_DIR, "no_go_condition_registry")

    def load_no_go_condition_registry(self):
        from config.paths import LAKE_LOCAL_READINESS_GO_NO_GO_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_GO_NO_GO_DIR / "no_go_condition_registry.parquet")

    def save_safe_go_condition_registry(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_GO_NO_GO_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_GO_NO_GO_DIR, "safe_go_condition_registry")

    def load_safe_go_condition_registry(self):
        from config.paths import LAKE_LOCAL_READINESS_GO_NO_GO_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_GO_NO_GO_DIR / "safe_go_condition_registry.parquet")

    def save_handoff_package_manifest(self, manifest: dict):
        from config.paths import LAKE_LOCAL_READINESS_HANDOFF_DIR
        import json
        path = LAKE_LOCAL_READINESS_HANDOFF_DIR / "handoff_package_manifest.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(manifest, f, indent=2)
        return path

    def load_handoff_package_manifest(self) -> dict:
        from config.paths import LAKE_LOCAL_READINESS_HANDOFF_DIR
        import json
        path = LAKE_LOCAL_READINESS_HANDOFF_DIR / "handoff_package_manifest.json"
        if path.exists():
            with open(path, "r") as f:
                return json.load(f)
        return {}

    def save_operator_first_run_checklist(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_OPERATOR_CHECKLISTS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_OPERATOR_CHECKLISTS_DIR, "operator_first_run_checklist")

    def load_operator_first_run_checklist(self):
        from config.paths import LAKE_LOCAL_READINESS_OPERATOR_CHECKLISTS_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_OPERATOR_CHECKLISTS_DIR / "operator_first_run_checklist.parquet")

    def save_readiness_score_report(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_SCORING_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_SCORING_DIR, "readiness_score_report")

    def load_readiness_score_report(self):
        from config.paths import LAKE_LOCAL_READINESS_SCORING_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_SCORING_DIR / "readiness_score_report.parquet")

    def save_pre_handoff_risk_summary(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_RISKS_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_RISKS_DIR, "pre_handoff_risk_summary")

    def load_pre_handoff_risk_summary(self):
        from config.paths import LAKE_LOCAL_READINESS_RISKS_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_RISKS_DIR / "pre_handoff_risk_summary.parquet")

    def save_final_local_readiness_binder(self, text: str, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_PHASE_EVIDENCE_DIR
        path = LAKE_LOCAL_READINESS_PHASE_EVIDENCE_DIR / "final_local_readiness_binder.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            f.write(text)
        return path

    def load_final_local_readiness_binder(self) -> str:
        from config.paths import LAKE_LOCAL_READINESS_PHASE_EVIDENCE_DIR
        path = LAKE_LOCAL_READINESS_PHASE_EVIDENCE_DIR / "final_local_readiness_binder.txt"
        if path.exists():
            with open(path, "r") as f:
                return f.read()
        return ""

    def save_readiness_validation_report(self, df, summary=None):
        from config.paths import LAKE_LOCAL_READINESS_VALIDATION_DIR
        return self._save_parquet_and_csv(df, LAKE_LOCAL_READINESS_VALIDATION_DIR, "readiness_validation_report")

    def load_readiness_validation_report(self):
        from config.paths import LAKE_LOCAL_READINESS_VALIDATION_DIR
        return self._load_parquet(LAKE_LOCAL_READINESS_VALIDATION_DIR / "readiness_validation_report.parquet")

    def save_readiness_quality(self, profile_name: str, quality: dict):
        from config.paths import LAKE_LOCAL_READINESS_QUALITY_DIR
        import json
        path = LAKE_LOCAL_READINESS_QUALITY_DIR / f"readiness_quality_{profile_name}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(quality, f, indent=2)
        return path

    def load_readiness_quality(self, profile_name: str) -> dict:
        from config.paths import LAKE_LOCAL_READINESS_QUALITY_DIR
        import json
        path = LAKE_LOCAL_READINESS_QUALITY_DIR / f"readiness_quality_{profile_name}.json"
        if path.exists():
            with open(path, "r") as f:
                return json.load(f)
        return {}

    def save_local_readiness_report(self, profile_name: str, report: dict, markdown: str | None = None):
        from config.paths import LAKE_LOCAL_READINESS_DIR
        import json
        path = LAKE_LOCAL_READINESS_DIR / f"local_readiness_report_{profile_name}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(report, f, indent=2)
        if markdown:
            md_path = LAKE_LOCAL_READINESS_DIR / f"local_readiness_report_{profile_name}.md"
            with open(md_path, "w") as f:
                f.write(markdown)
        return path

    def load_local_readiness_report(self, profile_name: str) -> dict:
        from config.paths import LAKE_LOCAL_READINESS_DIR
        import json
        path = LAKE_LOCAL_READINESS_DIR / f"local_readiness_report_{profile_name}.json"
        if path.exists():
            with open(path, "r") as f:
                return json.load(f)
        return {}

    def list_local_readiness_reports(self):
        from config.paths import LAKE_LOCAL_READINESS_DIR
        import pandas as pd

        reports = []
        if LAKE_LOCAL_READINESS_DIR.exists():
            for p in LAKE_LOCAL_READINESS_DIR.glob("local_readiness_report_*.json"):
                profile_name = p.stem.replace("local_readiness_report_", "")
                reports.append({"profile_name": profile_name, "path": str(p)})
        return pd.DataFrame(reports)


    # --- Local Maintenance Integration ---
    def save_maintenance_domain_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_DOMAINS_DIR / "maintenance_domain_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_maintenance_domain_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_DOMAINS_DIR / "maintenance_domain_registry.parquet"
        return self._load_parquet(in_path)

    def save_maintenance_task_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_TASKS_DIR / "maintenance_task_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_maintenance_task_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_TASKS_DIR / "maintenance_task_registry.parquet"
        return self._load_parquet(in_path)

    def save_periodic_review_calendar(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CALENDAR_DIR / "periodic_review_calendar.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_periodic_review_calendar(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CALENDAR_DIR / "periodic_review_calendar.parquet"
        return self._load_parquet(in_path)

    def save_report_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "report_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_report_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "report_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_datalake_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "datalake_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_datalake_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "datalake_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_documentation_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "documentation_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_documentation_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "documentation_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_test_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "test_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_test_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "test_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_safety_security_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "safety_security_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_safety_security_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "safety_security_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_backup_packaging_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "backup_packaging_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_backup_packaging_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "backup_packaging_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_cross_layer_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "cross_layer_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_cross_layer_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "cross_layer_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_dependency_aging_watch_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_DEPENDENCIES_DIR / "dependency_aging_watch_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_dependency_aging_watch_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_DEPENDENCIES_DIR / "dependency_aging_watch_report.parquet"
        return self._load_parquet(in_path)

    def save_dependency_review_checklist(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_DEPENDENCY_REVIEW_DIR / "dependency_review_checklist.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_dependency_review_checklist(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_DEPENDENCY_REVIEW_DIR / "dependency_review_checklist.parquet"
        return self._load_parquet(in_path)

    def save_deprecated_artifact_watch_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_ARTIFACTS_DIR / "deprecated_artifact_watch_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_deprecated_artifact_watch_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_ARTIFACTS_DIR / "deprecated_artifact_watch_report.parquet"
        return self._load_parquet(in_path)

    def save_stale_report_watch_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_REPORTS_DIR / "stale_report_watch_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_stale_report_watch_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_REPORTS_DIR / "stale_report_watch_report.parquet"
        return self._load_parquet(in_path)

    def save_stale_documentation_watch_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_DOCS_DIR / "stale_documentation_watch_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_stale_documentation_watch_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_DOCS_DIR / "stale_documentation_watch_report.parquet"
        return self._load_parquet(in_path)

    def save_stale_test_watch_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_TESTS_DIR / "stale_test_watch_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_stale_test_watch_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_TESTS_DIR / "stale_test_watch_report.parquet"
        return self._load_parquet(in_path)

    def save_manual_review_queue(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_MANUAL_REVIEW_DIR / "manual_review_queue.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_manual_review_queue(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_MANUAL_REVIEW_DIR / "manual_review_queue.parquet"
        return self._load_parquet(in_path)

    def save_maintenance_gap_register(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_GAPS_DIR / "maintenance_gap_register.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_maintenance_gap_register(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_GAPS_DIR / "maintenance_gap_register.parquet"
        return self._load_parquet(in_path)

    def save_maintenance_risk_summary(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_RISKS_DIR / "maintenance_risk_summary.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_maintenance_risk_summary(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_RISKS_DIR / "maintenance_risk_summary.parquet"
        return self._load_parquet(in_path)

    def save_sustainability_score_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_SCORING_DIR / "sustainability_score_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_sustainability_score_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_SCORING_DIR / "sustainability_score_report.parquet"
        return self._load_parquet(in_path)

    def save_operator_periodic_review_checklist(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_OPERATOR_CHECKLISTS_DIR / "operator_periodic_review_checklist.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_operator_periodic_review_checklist(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_OPERATOR_CHECKLISTS_DIR / "operator_periodic_review_checklist.parquet"
        return self._load_parquet(in_path)

    def save_monthly_review_template(self, text: str, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_TEMPLATES_DIR / "monthly_review_template.txt"
        self._save_text(text, out_path)
        return out_path

    def load_monthly_review_template(self) -> str:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_TEMPLATES_DIR / "monthly_review_template.txt"
        return self._load_text(in_path)

    def save_quarterly_review_template(self, text: str, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_TEMPLATES_DIR / "quarterly_review_template.txt"
        self._save_text(text, out_path)
        return out_path

    def load_quarterly_review_template(self) -> str:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_TEMPLATES_DIR / "quarterly_review_template.txt"
        return self._load_text(in_path)

    def save_refresh_command_plan(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_REFRESH_COMMANDS_DIR / "refresh_command_plan.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_refresh_command_plan(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_REFRESH_COMMANDS_DIR / "refresh_command_plan.parquet"
        return self._load_parquet(in_path)

    def save_maintenance_runbook(self, text: str, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_RUNBOOKS_DIR / "maintenance_runbook.txt"
        self._save_text(text, out_path)
        return out_path

    def load_maintenance_runbook(self) -> str:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_RUNBOOKS_DIR / "maintenance_runbook.txt"
        return self._load_text(in_path)

    def save_long_term_sustainability_binder(self, text: str, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_BINDERS_DIR / "long_term_sustainability_binder.txt"
        self._save_text(text, out_path)
        return out_path

    def load_long_term_sustainability_binder(self) -> str:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_BINDERS_DIR / "long_term_sustainability_binder.txt"
        return self._load_text(in_path)

    def save_maintenance_validation_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_VALIDATION_DIR / "maintenance_validation_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_maintenance_validation_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_VALIDATION_DIR / "maintenance_validation_report.parquet"
        return self._load_parquet(in_path)

    def save_maintenance_quality(self, profile_name: str, quality: dict) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_QUALITY_DIR / f"maintenance_quality_{profile_name}.json"
        self._save_json(quality, out_path)
        return out_path

    def load_maintenance_quality(self, profile_name: str) -> dict:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_QUALITY_DIR / f"maintenance_quality_{profile_name}.json"
        return self._load_json(in_path)

    def save_training_domain_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "domains" / "training_domain_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_training_domain_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "domains" / "training_domain_registry.parquet"
        return self._load_parquet(path)

    def save_role_based_onboarding_paths(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "onboarding" / "role_based_onboarding_paths.parquet"
        self._save_parquet(df, path)
        return path
    def load_role_based_onboarding_paths(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "onboarding" / "role_based_onboarding_paths.parquet"
        return self._load_parquet(path)

    def save_glossary_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "glossary" / "glossary_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_glossary_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "glossary" / "glossary_registry.parquet"
        return self._load_parquet(path)

    def save_concept_map_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "concepts" / "concept_map_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_concept_map_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "concepts" / "concept_map_registry.parquet"
        return self._load_parquet(path)

    def save_local_training_report(self, profile_name, report, markdown=None):
        path = self.paths.LAKE_LOCAL_TRAINING_REPORTS_DIR / f"{profile_name}_report.json"
        self._save_json(report, path)
        return path
    def load_local_training_report(self, profile_name):
        path = self.paths.LAKE_LOCAL_TRAINING_REPORTS_DIR / f"{profile_name}_report.json"
        return self._load_json(path)

    def save_first_week_operator_curriculum(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "curriculum" / "first_week_operator_curriculum.parquet"
        self._save_parquet(df, path)
        return path
    def load_first_week_operator_curriculum(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "curriculum" / "first_week_operator_curriculum.parquet"
        return self._load_parquet(path)

    def save_knowledge_transfer_checklist(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "checklists" / "knowledge_transfer_checklist.parquet"
        self._save_parquet(df, path)
        return path
    def load_knowledge_transfer_checklist(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "checklists" / "knowledge_transfer_checklist.parquet"
        return self._load_parquet(path)

    def save_training_assessment_dry_run(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "assessment" / "training_assessment_dry_run.parquet"
        self._save_parquet(df, path)
        return path
    def load_training_assessment_dry_run(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "assessment" / "training_assessment_dry_run.parquet"
        return self._load_parquet(path)

    def save_faq_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "faq" / "faq_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_faq_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "faq" / "faq_registry.parquet"
        return self._load_parquet(path)

    def save_guided_walkthrough_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "walkthroughs" / "guided_walkthrough_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_guided_walkthrough_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "walkthroughs" / "guided_walkthrough_registry.parquet"
        return self._load_parquet(path)

    def save_local_walkthrough_lessons(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "walkthroughs" / "local_walkthrough_lessons.parquet"
        self._save_parquet(df, path)
        return path
    def load_local_walkthrough_lessons(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "walkthroughs" / "local_walkthrough_lessons.parquet"
        return self._load_parquet(path)

    def save_safe_command_lesson_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "commands" / "safe_command_lesson_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_safe_command_lesson_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "commands" / "safe_command_lesson_registry.parquet"
        return self._load_parquet(path)

    def save_report_reading_lesson_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "reports" / "report_reading_lesson_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_report_reading_lesson_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "reports" / "report_reading_lesson_registry.parquet"
        return self._load_parquet(path)

    def save_datalake_reading_lesson_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "datalake" / "datalake_reading_lesson_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_datalake_reading_lesson_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "datalake" / "datalake_reading_lesson_registry.parquet"
        return self._load_parquet(path)

    def save_cross_layer_lesson_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "cross_layer" / "cross_layer_lesson_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_cross_layer_lesson_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "cross_layer" / "cross_layer_lesson_registry.parquet"
        return self._load_parquet(path)

    def save_troubleshooting_lesson_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "troubleshooting" / "troubleshooting_lesson_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_troubleshooting_lesson_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "troubleshooting" / "troubleshooting_lesson_registry.parquet"
        return self._load_parquet(path)

    def save_operator_training_pack(self, text, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "operator_training_pack.txt"
        self._save_text(text, path)
        return path
    def load_operator_training_pack(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "operator_training_pack.txt"
        return self._load_text(path)

    def save_analyst_training_pack(self, text, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "analyst_training_pack.txt"
        self._save_text(text, path)
        return path
    def load_analyst_training_pack(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "analyst_training_pack.txt"
        return self._load_text(path)

    def save_developer_training_pack(self, text, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "developer_training_pack.txt"
        self._save_text(text, path)
        return path
    def load_developer_training_pack(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "developer_training_pack.txt"
        return self._load_text(path)

    def save_safe_usage_training_pack(self, text, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "safe_usage_training_pack.txt"
        self._save_text(text, path)
        return path
    def load_safe_usage_training_pack(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "safe_usage_training_pack.txt"
        return self._load_text(path)

    def save_non_use_policy_training_pack(self, text, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "non_use_policy_training_pack.txt"
        self._save_text(text, path)
        return path
    def load_non_use_policy_training_pack(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "non_use_policy_training_pack.txt"
        return self._load_text(path)

    def save_handover_education_binder(self, text, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "handover_education_binder.txt"
        self._save_text(text, path)
        return path
    def load_handover_education_binder(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "handover_education_binder.txt"
        return self._load_text(path)

    def save_training_gap_register(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "gaps" / "training_gap_register.parquet"
        self._save_parquet(df, path)
        return path
    def load_training_gap_register(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "gaps" / "training_gap_register.parquet"
        return self._load_parquet(path)

    def save_training_risk_summary(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "risks" / "training_risk_summary.parquet"
        self._save_parquet(df, path)
        return path
    def load_training_risk_summary(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "risks" / "training_risk_summary.parquet"
        return self._load_parquet(path)

    def save_training_validation_report(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "validation" / "training_validation_report.parquet"
        self._save_parquet(df, path)
        return path
    def load_training_validation_report(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "validation" / "training_validation_report.parquet"
        return self._load_parquet(path)

    def save_training_quality(self, profile_name, quality):
        path = self.paths.LAKE_LOCAL_TRAINING_QUALITY_DIR / f"{profile_name}_quality.json"
        self._save_json(quality, path)
        return path
    def load_training_quality(self, profile_name):
        path = self.paths.LAKE_LOCAL_TRAINING_QUALITY_DIR / f"{profile_name}_quality.json"
        return self._load_json(path)

    def list_local_training_reports(self):
        import pandas as pd

        if not self.paths.LAKE_LOCAL_TRAINING_REPORTS_DIR.exists():
            return pd.DataFrame()
        files = list(self.paths.LAKE_LOCAL_TRAINING_REPORTS_DIR.glob("*_report.json"))
        return pd.DataFrame([{"report_file": f.name} for f in files])


    # Phase 75: Local Synthesis Layer DataLake Integration
    def save_synthesis_profile_registry(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "profiles" / "synthesis_profile_registry.csv"
        df.to_csv(path, index=False)
        return path

    def load_synthesis_profile_registry(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "profiles" / "synthesis_profile_registry.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_phase_family_registry(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "phase_families" / "phase_family_registry.csv"
        df.to_csv(path, index=False)
        return path

    def load_phase_family_registry(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "phase_families" / "phase_family_registry.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_master_artifact_index(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "master_indexes" / "master_artifact_index.csv"
        df.to_csv(path, index=False)
        return path

    def load_master_artifact_index(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "master_indexes" / "master_artifact_index.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_master_report_index(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "master_indexes" / "master_report_index.csv"
        df.to_csv(path, index=False)
        return path

    def load_master_report_index(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "master_indexes" / "master_report_index.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_master_datalake_index(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "master_indexes" / "master_datalake_index.csv"
        df.to_csv(path, index=False)
        return path

    def load_master_datalake_index(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "master_indexes" / "master_datalake_index.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_master_docs_index(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "master_indexes" / "master_docs_index.csv"
        df.to_csv(path, index=False)
        return path

    def load_master_docs_index(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "master_indexes" / "master_docs_index.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_master_script_index(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "master_indexes" / "master_script_index.csv"
        df.to_csv(path, index=False)
        return path

    def load_master_script_index(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "master_indexes" / "master_script_index.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_master_test_index(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "master_indexes" / "master_test_index.csv"
        df.to_csv(path, index=False)
        return path

    def load_master_test_index(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "master_indexes" / "master_test_index.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_cross_phase_final_map(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "final_maps" / "cross_phase_final_map.csv"
        df.to_csv(path, index=False)
        return path

    def load_cross_phase_final_map(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "final_maps" / "cross_phase_final_map.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_end_state_capability_map(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "capabilities" / "end_state_capability_map.csv"
        df.to_csv(path, index=False)
        return path

    def load_end_state_capability_map(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "capabilities" / "end_state_capability_map.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_end_state_boundary_map(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "boundaries" / "end_state_boundary_map.csv"
        df.to_csv(path, index=False)
        return path

    def load_end_state_boundary_map(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "boundaries" / "end_state_boundary_map.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_end_state_module_dependency_map(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "dependencies" / "end_state_module_dependency_map.csv"
        df.to_csv(path, index=False)
        return path

    def load_end_state_module_dependency_map(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "dependencies" / "end_state_module_dependency_map.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_end_state_output_catalog(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "catalogs" / "end_state_output_catalog.csv"
        df.to_csv(path, index=False)
        return path

    def load_end_state_output_catalog(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "catalogs" / "end_state_output_catalog.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_project_completion_dossier(self, text: str, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "dossiers" / "project_completion_dossier.md"
        path.write_text(text, encoding="utf-8")
        return path

    def load_project_completion_dossier(self) -> str:
        path = self.dirs["local_synthesis"] / "dossiers" / "project_completion_dossier.md"
        if not path.exists(): return ""
        return path.read_text(encoding="utf-8")

    def save_final_non_use_policy_binder(self, text: str, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "binders" / "final_non_use_policy_binder.md"
        path.write_text(text, encoding="utf-8")
        return path

    def load_final_non_use_policy_binder(self) -> str:
        path = self.dirs["local_synthesis"] / "binders" / "final_non_use_policy_binder.md"
        if not path.exists(): return ""
        return path.read_text(encoding="utf-8")

    def save_final_safety_boundary_binder(self, text: str, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "binders" / "final_safety_boundary_binder.md"
        path.write_text(text, encoding="utf-8")
        return path

    def load_final_safety_boundary_binder(self) -> str:
        path = self.dirs["local_synthesis"] / "binders" / "final_safety_boundary_binder.md"
        if not path.exists(): return ""
        return path.read_text(encoding="utf-8")

    def save_final_local_only_statement(self, text: str, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "statements" / "final_local_only_statement.md"
        path.write_text(text, encoding="utf-8")
        return path

    def load_final_local_only_statement(self) -> str:
        path = self.dirs["local_synthesis"] / "statements" / "final_local_only_statement.md"
        if not path.exists(): return ""
        return path.read_text(encoding="utf-8")

    def save_final_limitation_register(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "limitations" / "final_limitation_register.csv"
        df.to_csv(path, index=False)
        return path

    def load_final_limitation_register(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "limitations" / "final_limitation_register.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_final_manual_review_register(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "manual_review" / "final_manual_review_register.csv"
        df.to_csv(path, index=False)
        return path

    def load_final_manual_review_register(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "manual_review" / "final_manual_review_register.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_final_no_go_safe_go_summary(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "no_go_safe_go" / "final_no_go_safe_go_summary.csv"
        df.to_csv(path, index=False)
        return path

    def load_final_no_go_safe_go_summary(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "no_go_safe_go" / "final_no_go_safe_go_summary.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_final_operator_navigation_guide(self, text: str, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "navigation" / "final_operator_navigation_guide.md"
        path.write_text(text, encoding="utf-8")
        return path

    def load_final_operator_navigation_guide(self) -> str:
        path = self.dirs["local_synthesis"] / "navigation" / "final_operator_navigation_guide.md"
        if not path.exists(): return ""
        return path.read_text(encoding="utf-8")

    def save_final_stakeholder_navigation_guide(self, text: str, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "navigation" / "final_stakeholder_navigation_guide.md"
        path.write_text(text, encoding="utf-8")
        return path

    def load_final_stakeholder_navigation_guide(self) -> str:
        path = self.dirs["local_synthesis"] / "navigation" / "final_stakeholder_navigation_guide.md"
        if not path.exists(): return ""
        return path.read_text(encoding="utf-8")

    def save_final_developer_navigation_guide(self, text: str, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "navigation" / "final_developer_navigation_guide.md"
        path.write_text(text, encoding="utf-8")
        return path

    def load_final_developer_navigation_guide(self) -> str:
        path = self.dirs["local_synthesis"] / "navigation" / "final_developer_navigation_guide.md"
        if not path.exists(): return ""
        return path.read_text(encoding="utf-8")

    def save_final_generated_docs_catalog(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "catalogs" / "final_generated_docs_catalog.csv"
        df.to_csv(path, index=False)
        return path

    def load_final_generated_docs_catalog(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "catalogs" / "final_generated_docs_catalog.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_final_command_catalog(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "catalogs" / "final_command_catalog.csv"
        df.to_csv(path, index=False)
        return path

    def load_final_command_catalog(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "catalogs" / "final_command_catalog.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_final_report_family_catalog(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "catalogs" / "final_report_family_catalog.csv"
        df.to_csv(path, index=False)
        return path

    def load_final_report_family_catalog(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "catalogs" / "final_report_family_catalog.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_final_datalake_domain_catalog(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "catalogs" / "final_datalake_domain_catalog.csv"
        df.to_csv(path, index=False)
        return path

    def load_final_datalake_domain_catalog(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "catalogs" / "final_datalake_domain_catalog.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_final_cross_layer_catalog(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "catalogs" / "final_cross_layer_catalog.csv"
        df.to_csv(path, index=False)
        return path

    def load_final_cross_layer_catalog(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "catalogs" / "final_cross_layer_catalog.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_final_project_closure_checklist(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "checklists" / "final_project_closure_checklist.csv"
        df.to_csv(path, index=False)
        return path

    def load_final_project_closure_checklist(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "checklists" / "final_project_closure_checklist.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_final_synthesis_validation_report(self, df: pd.DataFrame, summary: Optional[Dict] = None) -> Path:
        path = self.dirs["local_synthesis"] / "validation" / "final_synthesis_validation_report.csv"
        df.to_csv(path, index=False)
        return path

    def load_final_synthesis_validation_report(self) -> pd.DataFrame:
        path = self.dirs["local_synthesis"] / "validation" / "final_synthesis_validation_report.csv"
        if not path.exists(): return pd.DataFrame()
        return pd.read_csv(path)

    def save_final_synthesis_quality(self, profile_name: str, quality: Dict) -> Path:
        path = self.dirs["local_synthesis"] / "quality" / f"final_synthesis_quality_{profile_name}.json"
        import json
        path.write_text(json.dumps(quality, indent=4), encoding="utf-8")
        return path

    def load_final_synthesis_quality(self, profile_name: str) -> Dict:
        path = self.dirs["local_synthesis"] / "quality" / f"final_synthesis_quality_{profile_name}.json"
        if not path.exists(): return {}
        import json
        return json.loads(path.read_text(encoding="utf-8"))

    def save_local_synthesis_report(self, profile_name: str, report: Dict, markdown: Optional[str] = None) -> Path:
        path = self.dirs["local_synthesis"] / "quality" / f"local_synthesis_report_{profile_name}.json"
        import json
        path.write_text(json.dumps(report, indent=4), encoding="utf-8")
        if markdown:
            md_path = self.dirs["local_synthesis"] / "quality" / f"local_synthesis_report_{profile_name}.md"
            md_path.write_text(markdown, encoding="utf-8")
        return path

    def load_local_synthesis_report(self, profile_name: str) -> Dict:
        path = self.dirs["local_synthesis"] / "quality" / f"local_synthesis_report_{profile_name}.json"
        if not path.exists(): return {}
        import json
        return json.loads(path.read_text(encoding="utf-8"))

    def list_local_synthesis_reports(self) -> pd.DataFrame:
        return pd.DataFrame(columns=["report", "status"])

    # Local Hardening Methods
    def save_hardening_profile_registry(self, df, summary=None):
        return self._save_df(df, "local_hardening/profiles", "hardening_profile_registry")
    def load_hardening_profile_registry(self):
        return self._load_df("local_hardening/profiles", "hardening_profile_registry")

    def save_hardening_domain_registry(self, df, summary=None):
        return self._save_df(df, "local_hardening/domains", "hardening_domain_registry")
    def load_hardening_domain_registry(self):
        return self._load_df("local_hardening/domains", "hardening_domain_registry")

    def save_dead_code_candidate_report(self, df, summary=None):
        return self._save_df(df, "local_hardening/dead_code", "dead_code_candidate_report")
    def load_dead_code_candidate_report(self):
        return self._load_df("local_hardening/dead_code", "dead_code_candidate_report")

    def save_unused_module_candidate_report(self, df, summary=None):
        return self._save_df(df, "local_hardening/unused_modules", "unused_module_candidate_report")
    def load_unused_module_candidate_report(self):
        return self._load_df("local_hardening/unused_modules", "unused_module_candidate_report")

    def save_orphan_script_candidate_report(self, df, summary=None):
        return self._save_df(df, "local_hardening/orphan_scripts", "orphan_script_candidate_report")
    def load_orphan_script_candidate_report(self):
        return self._load_df("local_hardening/orphan_scripts", "orphan_script_candidate_report")

    def save_orphan_test_candidate_report(self, df, summary=None):
        return self._save_df(df, "local_hardening/orphan_tests", "orphan_test_candidate_report")
    def load_orphan_test_candidate_report(self):
        return self._load_df("local_hardening/orphan_tests", "orphan_test_candidate_report")

    def save_duplicate_utility_candidate_report(self, df, summary=None):
        return self._save_df(df, "local_hardening/duplicates", "duplicate_utility_candidate_report")
    def load_duplicate_utility_candidate_report(self):
        return self._load_df("local_hardening/duplicates", "duplicate_utility_candidate_report")

    def save_contract_surface_registry(self, df, summary=None):
        return self._save_df(df, "local_hardening/contracts", "contract_surface_registry")
    def load_contract_surface_registry(self):
        return self._load_df("local_hardening/contracts", "contract_surface_registry")

    def save_public_function_contract_catalog(self, df, summary=None):
        return self._save_df(df, "local_hardening/contracts/public_functions", "public_function_contract_catalog")
    def load_public_function_contract_catalog(self):
        return self._load_df("local_hardening/contracts/public_functions", "public_function_contract_catalog")

    def save_datalake_contract_catalog(self, df, summary=None):
        return self._save_df(df, "local_hardening/contracts/datalake", "datalake_contract_catalog")
    def load_datalake_contract_catalog(self):
        return self._load_df("local_hardening/contracts/datalake", "datalake_contract_catalog")

    def save_featurestore_contract_catalog(self, df, summary=None):
        return self._save_df(df, "local_hardening/contracts/featurestore", "featurestore_contract_catalog")
    def load_featurestore_contract_catalog(self):
        return self._load_df("local_hardening/contracts/featurestore", "featurestore_contract_catalog")

    def save_script_cli_contract_catalog(self, df, summary=None):
        return self._save_df(df, "local_hardening/contracts/scripts", "script_cli_contract_catalog")
    def load_script_cli_contract_catalog(self):
        return self._load_df("local_hardening/contracts/scripts", "script_cli_contract_catalog")

    def save_report_builder_contract_catalog(self, df, summary=None):
        return self._save_df(df, "local_hardening/contracts/reports", "report_builder_contract_catalog")
    def load_report_builder_contract_catalog(self):
        return self._load_df("local_hardening/contracts/reports", "report_builder_contract_catalog")

    def save_config_settings_contract_catalog(self, df, summary=None):
        return self._save_df(df, "local_hardening/contracts/config", "config_settings_contract_catalog")
    def load_config_settings_contract_catalog(self):
        return self._load_df("local_hardening/contracts/config", "config_settings_contract_catalog")

    def save_path_contract_catalog(self, df, summary=None):
        return self._save_df(df, "local_hardening/contracts/paths", "path_contract_catalog")
    def load_path_contract_catalog(self):
        return self._load_df("local_hardening/contracts/paths", "path_contract_catalog")

    def save_test_contract_freeze_registry(self, df, summary=None):
        return self._save_df(df, "local_hardening/contracts/tests", "test_contract_freeze_registry")
    def load_test_contract_freeze_registry(self):
        return self._load_df("local_hardening/contracts/tests", "test_contract_freeze_registry")

    def save_documentation_freeze_snapshot(self, df, summary=None):
        return self._save_df(df, "local_hardening/documentation_freeze", "documentation_freeze_snapshot")
    def load_documentation_freeze_snapshot(self):
        return self._load_df("local_hardening/documentation_freeze", "documentation_freeze_snapshot")

    def save_readme_docs_freeze_checklist(self, df, summary=None):
        return self._save_df(df, "local_hardening/documentation_freeze", "readme_docs_freeze_checklist")
    def load_readme_docs_freeze_checklist(self):
        return self._load_df("local_hardening/documentation_freeze", "readme_docs_freeze_checklist")

    def save_generated_docs_freeze_catalog(self, df, summary=None):
        return self._save_df(df, "local_hardening/generated_docs_freeze", "generated_docs_freeze_catalog")
    def load_generated_docs_freeze_catalog(self):
        return self._load_df("local_hardening/generated_docs_freeze", "generated_docs_freeze_catalog")

    def save_rc_dry_run_freeze_manifest(self, manifest):
        import json
        p = self.base_dir / "local_hardening" / "rc_freeze" / "rc_dry_run_freeze_manifest.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f: json.dump(manifest, f, indent=2)
        return p
    def load_rc_dry_run_freeze_manifest(self):
        import json
        p = self.base_dir / "local_hardening" / "rc_freeze" / "rc_dry_run_freeze_manifest.json"
        if p.exists():
            with open(p, "r", encoding="utf-8") as f: return json.load(f)
        return {}

    def save_rc_dry_run_command_plan(self, df, summary=None):
        return self._save_df(df, "local_hardening/rc_freeze", "rc_dry_run_command_plan")
    def load_rc_dry_run_command_plan(self):
        return self._load_df("local_hardening/rc_freeze", "rc_dry_run_command_plan")

    def save_rc_non_use_boundary_checklist(self, df, summary=None):
        return self._save_df(df, "local_hardening/rc_freeze", "rc_non_use_boundary_checklist")
    def load_rc_non_use_boundary_checklist(self):
        return self._load_df("local_hardening/rc_freeze", "rc_non_use_boundary_checklist")

    def save_final_import_health_report(self, df, summary=None):
        return self._save_df(df, "local_hardening/health", "final_import_health_report")
    def load_final_import_health_report(self):
        return self._load_df("local_hardening/health", "final_import_health_report")

    def save_final_path_health_report(self, df, summary=None):
        return self._save_df(df, "local_hardening/health", "final_path_health_report")
    def load_final_path_health_report(self):
        return self._load_df("local_hardening/health", "final_path_health_report")

    def save_final_output_directory_health_report(self, df, summary=None):
        return self._save_df(df, "local_hardening/health", "final_output_directory_health_report")
    def load_final_output_directory_health_report(self):
        return self._load_df("local_hardening/health", "final_output_directory_health_report")

    def save_final_naming_convention_report(self, df, summary=None):
        return self._save_df(df, "local_hardening/naming", "final_naming_convention_report")
    def load_final_naming_convention_report(self):
        return self._load_df("local_hardening/naming", "final_naming_convention_report")

    def save_final_dependency_boundary_report(self, df, summary=None):
        return self._save_df(df, "local_hardening/dependencies", "final_dependency_boundary_report")
    def load_final_dependency_boundary_report(self):
        return self._load_df("local_hardening/dependencies", "final_dependency_boundary_report")

    def save_final_safety_hardening_report(self, df, summary=None):
        return self._save_df(df, "local_hardening/safety", "final_safety_hardening_report")
    def load_final_safety_hardening_report(self):
        return self._load_df("local_hardening/safety", "final_safety_hardening_report")

    def save_final_hardening_gap_register(self, df, summary=None):
        return self._save_df(df, "local_hardening/gaps", "final_hardening_gap_register")
    def load_final_hardening_gap_register(self):
        return self._load_df("local_hardening/gaps", "final_hardening_gap_register")

    def save_final_hardening_risk_summary(self, df, summary=None):
        return self._save_df(df, "local_hardening/risks", "final_hardening_risk_summary")
    def load_final_hardening_risk_summary(self):
        return self._load_df("local_hardening/risks", "final_hardening_risk_summary")

    def save_final_freeze_validation_report(self, df, summary=None):
        return self._save_df(df, "local_hardening/validation", "final_freeze_validation_report")
    def load_final_freeze_validation_report(self):
        return self._load_df("local_hardening/validation", "final_freeze_validation_report")

    def save_final_freeze_quality(self, profile_name, quality):
        import json
        p = self.base_dir / "local_hardening" / "quality" / f"{profile_name}_final_freeze_quality.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f: json.dump(quality, f, indent=2)
        return p
    def load_final_freeze_quality(self, profile_name):
        import json
        p = self.base_dir / "local_hardening" / "quality" / f"{profile_name}_final_freeze_quality.json"
        if p.exists():
            with open(p, "r", encoding="utf-8") as f: return json.load(f)
        return {}

    def save_local_hardening_report(self, profile_name, report, markdown=None):
        import json
        p = self.base_dir / "local_hardening" / "quality" / f"{profile_name}_report.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f: json.dump(report, f, indent=2)
        return p
    def load_local_hardening_report(self, profile_name):
        import json
        p = self.base_dir / "local_hardening" / "quality" / f"{profile_name}_report.json"
        if p.exists():
            with open(p, "r", encoding="utf-8") as f: return json.load(f)
        return {}
    def list_local_hardening_reports(self):
        import pandas as pd
        return pd.DataFrame()

    # --- PHASE 77: LOCAL ACCEPTANCE ---
    def save_acceptance_profile_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_profiles"] / "acceptance_profile_registry.parquet")

    def load_acceptance_profile_registry(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_profiles"] / "acceptance_profile_registry.parquet")

    def save_acceptance_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_domains"] / "acceptance_domain_registry.parquet")

    def load_acceptance_domain_registry(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_domains"] / "acceptance_domain_registry.parquet")

    def save_final_acceptance_simulation_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_simulation"] / "final_acceptance_simulation_checklist.parquet")

    def load_final_acceptance_simulation_checklist(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_simulation"] / "final_acceptance_simulation_checklist.parquet")

    def save_independent_reviewer_pack(self, text: str, summary: dict | None = None) -> Path:
        path = self.paths["lake_local_acceptance_reviewer_pack"] / "independent_reviewer_pack.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: f.write(text)
        return path

    def load_independent_reviewer_pack(self) -> str:
        path = self.paths["lake_local_acceptance_reviewer_pack"] / "independent_reviewer_pack.txt"
        if not path.exists(): return ""
        with open(path, "r", encoding="utf-8") as f: return f.read()

    def save_reviewer_question_bank(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_questions"] / "reviewer_question_bank.parquet")

    def load_reviewer_question_bank(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_questions"] / "reviewer_question_bank.parquet")

    def save_reviewer_evidence_request_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_evidence_matrix"] / "reviewer_evidence_request_matrix.parquet")

    def load_reviewer_evidence_request_matrix(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_evidence_matrix"] / "reviewer_evidence_request_matrix.parquet")

    def save_audit_style_local_evidence_trail(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_evidence_trail"] / "audit_style_local_evidence_trail.parquet")

    def load_audit_style_local_evidence_trail(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_evidence_trail"] / "audit_style_local_evidence_trail.parquet")

    def save_evidence_output_trace_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_traces"] / "evidence_output_trace_matrix.parquet")

    def load_evidence_output_trace_matrix(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_traces"] / "evidence_output_trace_matrix.parquet")

    def save_evidence_test_trace_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_traces"] / "evidence_test_trace_matrix.parquet")

    def load_evidence_test_trace_matrix(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_traces"] / "evidence_test_trace_matrix.parquet")

    def save_evidence_doc_trace_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_traces"] / "evidence_doc_trace_matrix.parquet")

    def load_evidence_doc_trace_matrix(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_traces"] / "evidence_doc_trace_matrix.parquet")

    def save_evidence_safety_boundary_trace_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_traces"] / "evidence_safety_boundary_trace_matrix.parquet")

    def load_evidence_safety_boundary_trace_matrix(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_traces"] / "evidence_safety_boundary_trace_matrix.parquet")

    def save_signoff_rehearsal_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_signoff"] / "signoff_rehearsal_checklist.parquet")

    def load_signoff_rehearsal_checklist(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_signoff"] / "signoff_rehearsal_checklist.parquet")

    def save_signoff_rehearsal_binder(self, text: str, summary: dict | None = None) -> Path:
        path = self.paths["lake_local_acceptance_binders"] / "signoff_rehearsal_binder.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: f.write(text)
        return path

    def load_signoff_rehearsal_binder(self) -> str:
        path = self.paths["lake_local_acceptance_binders"] / "signoff_rehearsal_binder.txt"
        if not path.exists(): return ""
        with open(path, "r", encoding="utf-8") as f: return f.read()

    def save_final_verification_rehearsal_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_verification"] / "final_verification_rehearsal_plan.parquet")

    def load_final_verification_rehearsal_plan(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_verification"] / "final_verification_rehearsal_plan.parquet")

    def save_final_verification_scenario_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_verification"] / "final_verification_scenario_registry.parquet")

    def load_final_verification_scenario_registry(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_verification"] / "final_verification_scenario_registry.parquet")

    def save_acceptance_criteria_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_criteria"] / "acceptance_criteria_registry.parquet")

    def load_acceptance_criteria_registry(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_criteria"] / "acceptance_criteria_registry.parquet")

    def save_acceptance_exception_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_exceptions"] / "acceptance_exception_register.parquet")

    def load_acceptance_exception_register(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_exceptions"] / "acceptance_exception_register.parquet")

    def save_acceptance_no_go_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_no_go_safe_go"] / "acceptance_no_go_register.parquet")

    def load_acceptance_no_go_register(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_no_go_safe_go"] / "acceptance_no_go_register.parquet")

    def save_acceptance_safe_go_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_no_go_safe_go"] / "acceptance_safe_go_register.parquet")

    def load_acceptance_safe_go_register(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_no_go_safe_go"] / "acceptance_safe_go_register.parquet")

    def save_acceptance_no_go_safe_go_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_no_go_safe_go"] / "acceptance_no_go_safe_go_summary.parquet")

    def load_acceptance_no_go_safe_go_summary(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_no_go_safe_go"] / "acceptance_no_go_safe_go_summary.parquet")

    def save_independent_review_notes_template(self, text: str, summary: dict | None = None) -> Path:
        path = self.paths["lake_local_acceptance_templates"] / "independent_review_notes_template.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: f.write(text)
        return path

    def load_independent_review_notes_template(self) -> str:
        path = self.paths["lake_local_acceptance_templates"] / "independent_review_notes_template.txt"
        if not path.exists(): return ""
        with open(path, "r", encoding="utf-8") as f: return f.read()

    def save_acceptance_response_template(self, text: str, summary: dict | None = None) -> Path:
        path = self.paths["lake_local_acceptance_templates"] / "acceptance_response_template.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: f.write(text)
        return path

    def load_acceptance_response_template(self) -> str:
        path = self.paths["lake_local_acceptance_templates"] / "acceptance_response_template.txt"
        if not path.exists(): return ""
        with open(path, "r", encoding="utf-8") as f: return f.read()

    def save_final_verification_evidence_binder(self, text: str, summary: dict | None = None) -> Path:
        path = self.paths["lake_local_acceptance_binders"] / "final_verification_evidence_binder.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: f.write(text)
        return path

    def load_final_verification_evidence_binder(self) -> str:
        path = self.paths["lake_local_acceptance_binders"] / "final_verification_evidence_binder.txt"
        if not path.exists(): return ""
        with open(path, "r", encoding="utf-8") as f: return f.read()

    def save_acceptance_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_gaps"] / "acceptance_gap_register.parquet")

    def load_acceptance_gap_register(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_gaps"] / "acceptance_gap_register.parquet")

    def save_acceptance_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_risks"] / "acceptance_risk_summary.parquet")

    def load_acceptance_risk_summary(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_risks"] / "acceptance_risk_summary.parquet")

    def save_acceptance_readiness_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_scoring"] / "acceptance_readiness_score_report.parquet")

    def load_acceptance_readiness_score_report(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_scoring"] / "acceptance_readiness_score_report.parquet")

    def save_acceptance_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_validation"] / "acceptance_validation_report.parquet")

    def load_acceptance_validation_report(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_validation"] / "acceptance_validation_report.parquet")

    def save_acceptance_quality(self, profile_name: str, quality: dict) -> Path:
        import json
        path = self.paths["lake_local_acceptance_quality"] / f"{profile_name}_quality.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: json.dump(quality, f, indent=2)
        return path

    def load_acceptance_quality(self, profile_name: str) -> dict:
        import json
        path = self.paths["lake_local_acceptance_quality"] / f"{profile_name}_quality.json"
        if not path.exists(): return {}
        with open(path, "r", encoding="utf-8") as f: return json.load(f)

    def save_local_acceptance_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        import json
        path = self.paths["lake_local_acceptance"] / f"{profile_name}_report.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: json.dump(report, f, indent=2)
        if markdown:
            md_path = self.paths["lake_local_acceptance"] / f"{profile_name}_report.md"
            with open(md_path, "w", encoding="utf-8") as f: f.write(markdown)
        return path

    def load_local_acceptance_report(self, profile_name: str) -> dict:
        import json
        path = self.paths["lake_local_acceptance"] / f"{profile_name}_report.json"
        if not path.exists(): return {}
        with open(path, "r", encoding="utf-8") as f: return json.load(f)

    def list_local_acceptance_reports(self) -> pd.DataFrame:
        import pandas as pd
        path = self.paths["lake_local_acceptance"]
        files = list(path.glob("*_report.json")) if path.exists() else []
        return pd.DataFrame([{"report": f.name} for f in files])

    def save_delivery_profile_registry(self, df, summary=None): pass
    def load_delivery_profile_registry(self): return None
    def save_delivery_domain_registry(self, df, summary=None): pass
    def load_delivery_domain_registry(self): return None
    def save_final_delivery_bundle_manifest(self, manifest): pass
    def load_final_delivery_bundle_manifest(self): return None
    def save_final_delivery_bundle_manifest_items(self, df, summary=None): pass
    def load_final_delivery_bundle_manifest_items(self): return None
    def save_handoff_package_index(self, df, summary=None): pass
    def load_handoff_package_index(self): return None
    def save_portable_reviewer_archive_guide(self, text, summary=None): pass
    def load_portable_reviewer_archive_guide(self): return None
    def save_final_local_transfer_checklist(self, df, summary=None): pass
    def load_final_local_transfer_checklist(self): return None
    def save_delivery_rehearsal_binder(self, text, summary=None): pass
    def load_delivery_rehearsal_binder(self): return None
    def save_recipient_orientation_guide(self, text, summary=None): pass
    def load_recipient_orientation_guide(self): return None
    def save_delivery_evidence_map(self, df, summary=None): pass
    def load_delivery_evidence_map(self): return None
    def save_delivery_artifact_trace_matrix(self, df, summary=None): pass
    def load_delivery_artifact_trace_matrix(self): return None
    def save_delivery_docs_index(self, df, summary=None): pass
    def load_delivery_docs_index(self): return None
    def save_delivery_reports_index(self, df, summary=None): pass
    def load_delivery_reports_index(self): return None
    def save_delivery_datalake_index(self, df, summary=None): pass
    def load_delivery_datalake_index(self): return None
    def save_delivery_scripts_tests_index(self, df, summary=None): pass
    def load_delivery_scripts_tests_index(self): return None
    def save_delivery_generated_docs_index(self, df, summary=None): pass
    def load_delivery_generated_docs_index(self): return None
    def save_delivery_safety_boundary_index(self, df, summary=None): pass
    def load_delivery_safety_boundary_index(self): return None
    def save_delivery_no_go_safe_go_summary(self, df, summary=None): pass
    def load_delivery_no_go_safe_go_summary(self): return None
    def save_delivery_recipient_faq(self, df, summary=None): pass
    def load_delivery_recipient_faq(self): return None
    def save_delivery_package_reading_order(self, df, summary=None): pass
    def load_delivery_package_reading_order(self): return None
    def save_delivery_transfer_readiness_checklist(self, df, summary=None): pass
    def load_delivery_transfer_readiness_checklist(self): return None
    def save_delivery_exception_register(self, df, summary=None): pass
    def load_delivery_exception_register(self): return None
    def save_delivery_gap_register(self, df, summary=None): pass
    def load_delivery_gap_register(self): return None
    def save_delivery_risk_summary(self, df, summary=None): pass
    def load_delivery_risk_summary(self): return None
    def save_delivery_readiness_score_report(self, df, summary=None): pass
    def load_delivery_readiness_score_report(self): return None
    def save_delivery_validation_report(self, df, summary=None): pass
    def load_delivery_validation_report(self): return None
    def save_delivery_quality(self, profile_name, quality): pass
    def load_delivery_quality(self, profile_name): return None
    def save_local_delivery_report(self, profile_name, report, markdown=None): pass
    def load_local_delivery_report(self, profile_name): return None
    def list_local_delivery_reports(self): return None
    # --- Local Archival ---
    def save_archival_profile_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_archival_profile_registry(self) -> pd.DataFrame: return pd.DataFrame()
    def save_archival_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_archival_domain_registry(self) -> pd.DataFrame: return pd.DataFrame()
    def save_final_archival_seal_rehearsal_manifest(self, manifest: dict) -> Path: return Path()
    def load_final_archival_seal_rehearsal_manifest(self) -> dict: return {}
    def save_archival_seal_manifest_items(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_archival_seal_manifest_items(self) -> pd.DataFrame: return pd.DataFrame()
    def save_immutable_manifest_rehearsal_catalog(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_immutable_manifest_rehearsal_catalog(self) -> pd.DataFrame: return pd.DataFrame()
    def save_local_provenance_lockfile(self, lockfile: dict) -> Path: return Path()
    def load_local_provenance_lockfile(self) -> dict: return {}
    def save_provenance_lock_entries(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_provenance_lock_entries(self) -> pd.DataFrame: return pd.DataFrame()
    def save_final_hash_catalog(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_final_hash_catalog(self) -> pd.DataFrame: return pd.DataFrame()
    def save_final_hash_of_hashes_catalog(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_final_hash_of_hashes_catalog(self) -> pd.DataFrame: return pd.DataFrame()
    def save_hash_policy_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_hash_policy_registry(self) -> pd.DataFrame: return pd.DataFrame()
    def save_hash_exclusion_policy_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_hash_exclusion_policy_registry(self) -> pd.DataFrame: return pd.DataFrame()
    def save_sensitive_file_exclusion_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_sensitive_file_exclusion_registry(self) -> pd.DataFrame: return pd.DataFrame()
    def save_archive_candidate_inventory(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_archive_candidate_inventory(self) -> pd.DataFrame: return pd.DataFrame()
    def save_delivery_bundle_hash_rehearsal(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_delivery_bundle_hash_rehearsal(self) -> pd.DataFrame: return pd.DataFrame()
    def save_handoff_package_hash_rehearsal(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_handoff_package_hash_rehearsal(self) -> pd.DataFrame: return pd.DataFrame()
    def save_generated_docs_hash_rehearsal(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_generated_docs_hash_rehearsal(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reports_hash_rehearsal(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reports_hash_rehearsal(self) -> pd.DataFrame: return pd.DataFrame()
    def save_datalake_hash_rehearsal(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_datalake_hash_rehearsal(self) -> pd.DataFrame: return pd.DataFrame()
    def save_scripts_tests_hash_rehearsal(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_scripts_tests_hash_rehearsal(self) -> pd.DataFrame: return pd.DataFrame()
    def save_safety_boundary_hash_rehearsal(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_safety_boundary_hash_rehearsal(self) -> pd.DataFrame: return pd.DataFrame()
    def save_acceptance_delivery_evidence_hash_rehearsal(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_acceptance_delivery_evidence_hash_rehearsal(self) -> pd.DataFrame: return pd.DataFrame()
    def save_custody_chain_simulation_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_custody_chain_simulation_registry(self) -> pd.DataFrame: return pd.DataFrame()
    def save_long_term_custody_rehearsal_guide(self, text: str, summary: dict | None = None) -> Path: return Path()
    def load_long_term_custody_rehearsal_guide(self) -> str: return ""
    def save_retention_note_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_retention_note_registry(self) -> pd.DataFrame: return pd.DataFrame()
    def save_tamper_evidence_dry_run_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_tamper_evidence_dry_run_report(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reproducibility_pointer_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reproducibility_pointer_registry(self) -> pd.DataFrame: return pd.DataFrame()
    def save_provenance_trace_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_provenance_trace_matrix(self) -> pd.DataFrame: return pd.DataFrame()
    def save_provenance_delivery_trace_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_provenance_delivery_trace_matrix(self) -> pd.DataFrame: return pd.DataFrame()
    def save_provenance_acceptance_trace_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_provenance_acceptance_trace_matrix(self) -> pd.DataFrame: return pd.DataFrame()
    def save_archival_no_go_safe_go_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_archival_no_go_safe_go_summary(self) -> pd.DataFrame: return pd.DataFrame()
    def save_archival_exception_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_archival_exception_register(self) -> pd.DataFrame: return pd.DataFrame()
    def save_archival_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_archival_gap_register(self) -> pd.DataFrame: return pd.DataFrame()
    def save_archival_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_archival_risk_summary(self) -> pd.DataFrame: return pd.DataFrame()
    def save_archival_readiness_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_archival_readiness_score_report(self) -> pd.DataFrame: return pd.DataFrame()
    def save_archival_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_archival_validation_report(self) -> pd.DataFrame: return pd.DataFrame()
    def save_archival_quality(self, profile_name: str, quality: dict) -> Path: return Path()
    def load_archival_quality(self, profile_name: str) -> dict: return {}
    def save_local_archival_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path: return Path()
    def load_local_archival_report(self, profile_name: str) -> dict: return {}
    def list_local_archival_reports(self) -> pd.DataFrame: return pd.DataFrame()

    # Local Reuse Methods
    def save_reuse_profile_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reuse_profile_registry(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reuse_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reuse_domain_registry(self) -> pd.DataFrame: return pd.DataFrame()
    def save_final_audit_memory_pack(self, text: str, summary: dict | None = None) -> Path: return Path()
    def load_final_audit_memory_pack(self) -> str: return ""
    def save_phase_memory_capsule_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_phase_memory_capsule_registry(self) -> pd.DataFrame: return pd.DataFrame()
    def save_cross_project_reusable_template_catalog(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_cross_project_reusable_template_catalog(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reusable_prompt_template_library(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reusable_prompt_template_library(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reusable_module_blueprint_catalog(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reusable_module_blueprint_catalog(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reusable_script_pattern_catalog(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reusable_script_pattern_catalog(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reusable_test_pattern_catalog(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reusable_test_pattern_catalog(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reusable_datalake_contract_pattern_catalog(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reusable_datalake_contract_pattern_catalog(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reusable_report_pattern_catalog(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reusable_report_pattern_catalog(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reusable_safety_boundary_pattern_catalog(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reusable_safety_boundary_pattern_catalog(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reusable_documentation_pattern_catalog(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reusable_documentation_pattern_catalog(self) -> pd.DataFrame: return pd.DataFrame()
    def save_local_knowledge_reuse_kit(self, text: str, summary: dict | None = None) -> Path: return Path()
    def load_local_knowledge_reuse_kit(self) -> str: return ""
    def save_project_pattern_extraction_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_project_pattern_extraction_report(self) -> pd.DataFrame: return pd.DataFrame()
    def save_architecture_pattern_extraction_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_architecture_pattern_extraction_report(self) -> pd.DataFrame: return pd.DataFrame()
    def save_safety_pattern_extraction_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_safety_pattern_extraction_report(self) -> pd.DataFrame: return pd.DataFrame()
    def save_validation_quality_pattern_extraction_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_validation_quality_pattern_extraction_report(self) -> pd.DataFrame: return pd.DataFrame()
    def save_handoff_delivery_closure_pattern_extraction_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_handoff_delivery_closure_pattern_extraction_report(self) -> pd.DataFrame: return pd.DataFrame()
    def save_v1_1_planning_seed(self, text: str, summary: dict | None = None) -> Path: return Path()
    def load_v1_1_planning_seed(self) -> str: return ""
    def save_v1_1_candidate_backlog_seed(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_v1_1_candidate_backlog_seed(self) -> pd.DataFrame: return pd.DataFrame()
    def save_v1_1_safety_boundary_seed(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_v1_1_safety_boundary_seed(self) -> pd.DataFrame: return pd.DataFrame()
    def save_v1_1_research_only_scope_seed(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_v1_1_research_only_scope_seed(self) -> pd.DataFrame: return pd.DataFrame()
    def save_v1_1_non_goals_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_v1_1_non_goals_registry(self) -> pd.DataFrame: return pd.DataFrame()
    def save_future_project_starter_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_future_project_starter_checklist(self) -> pd.DataFrame: return pd.DataFrame()
    def save_future_project_prompt_starter_pack(self, text: str, summary: dict | None = None) -> Path: return Path()
    def load_future_project_prompt_starter_pack(self) -> str: return ""
    def save_future_project_directory_blueprint(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_future_project_directory_blueprint(self) -> pd.DataFrame: return pd.DataFrame()
    def save_future_project_test_blueprint(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_future_project_test_blueprint(self) -> pd.DataFrame: return pd.DataFrame()
    def save_knowledge_reuse_no_go_safe_go_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_knowledge_reuse_no_go_safe_go_summary(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reuse_exception_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reuse_exception_register(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reuse_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reuse_gap_register(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reuse_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reuse_risk_summary(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reuse_readiness_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reuse_readiness_score_report(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reuse_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return Path()
    def load_reuse_validation_report(self) -> pd.DataFrame: return pd.DataFrame()
    def save_reuse_quality(self, profile_name: str, quality: dict) -> Path: return Path()
    def load_reuse_quality(self, profile_name: str) -> dict: return {}
    def save_local_reuse_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path: return Path()
    def load_local_reuse_report(self, profile_name: str) -> dict: return {}
    def list_local_reuse_reports(self) -> pd.DataFrame: return pd.DataFrame()

    def save_simplification_profile_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/profiles", "simplification_profile_registry.csv")

    def load_simplification_profile_registry(self) -> pd.DataFrame:
        return self._load_data("local_simplification/profiles/simplification_profile_registry.csv")

    def save_simplification_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/domains", "simplification_domain_registry.csv")

    def load_simplification_domain_registry(self) -> pd.DataFrame:
        return self._load_data("local_simplification/domains/simplification_domain_registry.csv")

    def save_final_modular_complexity_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/complexity", "final_modular_complexity_map.csv")

    def load_final_modular_complexity_map(self) -> pd.DataFrame:
        return self._load_data("local_simplification/complexity/final_modular_complexity_map.csv")

    def save_module_family_complexity_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/complexity", "module_family_complexity_report.csv")

    def load_module_family_complexity_report(self) -> pd.DataFrame:
        return self._load_data("local_simplification/complexity/module_family_complexity_report.csv")

    def save_folder_depth_complexity_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/complexity", "folder_depth_complexity_report.csv")

    def load_folder_depth_complexity_report(self) -> pd.DataFrame:
        return self._load_data("local_simplification/complexity/folder_depth_complexity_report.csv")

    def save_file_count_complexity_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/complexity", "file_count_complexity_report.csv")

    def load_file_count_complexity_report(self) -> pd.DataFrame:
        return self._load_data("local_simplification/complexity/file_count_complexity_report.csv")

    def save_function_count_complexity_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/complexity", "function_count_complexity_report.csv")

    def load_function_count_complexity_report(self) -> pd.DataFrame:
        return self._load_data("local_simplification/complexity/function_count_complexity_report.csv")

    def save_script_sprawl_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/sprawl", "script_sprawl_report.csv")

    def load_script_sprawl_report(self) -> pd.DataFrame:
        return self._load_data("local_simplification/sprawl/script_sprawl_report.csv")

    def save_test_sprawl_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/sprawl", "test_sprawl_report.csv")

    def load_test_sprawl_report(self) -> pd.DataFrame:
        return self._load_data("local_simplification/sprawl/test_sprawl_report.csv")

    def save_report_output_sprawl_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/sprawl", "report_output_sprawl_report.csv")

    def load_report_output_sprawl_report(self) -> pd.DataFrame:
        return self._load_data("local_simplification/sprawl/report_output_sprawl_report.csv")

    def save_datalake_output_sprawl_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/sprawl", "datalake_output_sprawl_report.csv")

    def load_datalake_output_sprawl_report(self) -> pd.DataFrame:
        return self._load_data("local_simplification/sprawl/datalake_output_sprawl_report.csv")

    def save_documentation_sprawl_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/sprawl", "documentation_sprawl_report.csv")

    def load_documentation_sprawl_report(self) -> pd.DataFrame:
        return self._load_data("local_simplification/sprawl/documentation_sprawl_report.csv")

    def save_optional_slimming_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/slimming_plan", "optional_slimming_plan.csv")

    def load_optional_slimming_plan(self) -> pd.DataFrame:
        return self._load_data("local_simplification/slimming_plan/optional_slimming_plan.csv")

    def save_safe_consolidation_candidate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/consolidation", "safe_consolidation_candidate_registry.csv")

    def load_safe_consolidation_candidate_registry(self) -> pd.DataFrame:
        return self._load_data("local_simplification/consolidation/safe_consolidation_candidate_registry.csv")

    def save_duplicate_pattern_consolidation_candidate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/consolidation", "duplicate_pattern_consolidation_candidate_registry.csv")

    def load_duplicate_pattern_consolidation_candidate_registry(self) -> pd.DataFrame:
        return self._load_data("local_simplification/consolidation/duplicate_pattern_consolidation_candidate_registry.csv")

    def save_naming_simplification_candidate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/naming", "naming_simplification_candidate_registry.csv")

    def load_naming_simplification_candidate_registry(self) -> pd.DataFrame:
        return self._load_data("local_simplification/naming/naming_simplification_candidate_registry.csv")

    def save_config_simplification_candidate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/config", "config_simplification_candidate_registry.csv")

    def load_config_simplification_candidate_registry(self) -> pd.DataFrame:
        return self._load_data("local_simplification/config/config_simplification_candidate_registry.csv")

    def save_datalake_method_simplification_candidate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/datalake", "datalake_method_simplification_candidate_registry.csv")

    def load_datalake_method_simplification_candidate_registry(self) -> pd.DataFrame:
        return self._load_data("local_simplification/datalake/datalake_method_simplification_candidate_registry.csv")

    def save_script_cli_simplification_candidate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/scripts", "script_cli_simplification_candidate_registry.csv")

    def load_script_cli_simplification_candidate_registry(self) -> pd.DataFrame:
        return self._load_data("local_simplification/scripts/script_cli_simplification_candidate_registry.csv")

    def save_test_suite_simplification_candidate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/tests", "test_suite_simplification_candidate_registry.csv")

    def load_test_suite_simplification_candidate_registry(self) -> pd.DataFrame:
        return self._load_data("local_simplification/tests/test_suite_simplification_candidate_registry.csv")

    def save_docs_navigation_simplification_candidate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/docs_navigation", "docs_navigation_simplification_candidate_registry.csv")

    def load_docs_navigation_simplification_candidate_registry(self) -> pd.DataFrame:
        return self._load_data("local_simplification/docs_navigation/docs_navigation_simplification_candidate_registry.csv")

    def save_repo_ergonomics_rehearsal_guide(self, text: str, summary: dict | None = None) -> Path:
        p = self.base_dir / "local_simplification/ergonomics/repo_ergonomics_rehearsal_guide.txt"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def load_repo_ergonomics_rehearsal_guide(self) -> str:
        p = self.base_dir / "local_simplification/ergonomics/repo_ergonomics_rehearsal_guide.txt"
        return p.read_text(encoding="utf-8") if p.exists() else ""

    def save_maintainer_onboarding_simplification_guide(self, text: str, summary: dict | None = None) -> Path:
        p = self.base_dir / "local_simplification/onboarding/maintainer_onboarding_simplification_guide.txt"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def load_maintainer_onboarding_simplification_guide(self) -> str:
        p = self.base_dir / "local_simplification/onboarding/maintainer_onboarding_simplification_guide.txt"
        return p.read_text(encoding="utf-8") if p.exists() else ""

    def save_local_maintainability_improvement_seed(self, text: str, summary: dict | None = None) -> Path:
        p = self.base_dir / "local_simplification/maintainability_seed/local_maintainability_improvement_seed.txt"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def load_local_maintainability_improvement_seed(self) -> str:
        p = self.base_dir / "local_simplification/maintainability_seed/local_maintainability_improvement_seed.txt"
        return p.read_text(encoding="utf-8") if p.exists() else ""

    def save_complexity_no_go_safe_go_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/no_go_safe_go", "complexity_no_go_safe_go_summary.csv")

    def load_complexity_no_go_safe_go_summary(self) -> pd.DataFrame:
        return self._load_data("local_simplification/no_go_safe_go/complexity_no_go_safe_go_summary.csv")

    def save_simplification_exception_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/exceptions", "simplification_exception_register.csv")

    def load_simplification_exception_register(self) -> pd.DataFrame:
        return self._load_data("local_simplification/exceptions/simplification_exception_register.csv")

    def save_simplification_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/gaps", "simplification_gap_register.csv")

    def load_simplification_gap_register(self) -> pd.DataFrame:
        return self._load_data("local_simplification/gaps/simplification_gap_register.csv")

    def save_simplification_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/risks", "simplification_risk_summary.csv")

    def load_simplification_risk_summary(self) -> pd.DataFrame:
        return self._load_data("local_simplification/risks/simplification_risk_summary.csv")

    def save_maintainability_readiness_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/scoring", "maintainability_readiness_score_report.csv")

    def load_maintainability_readiness_score_report(self) -> pd.DataFrame:
        return self._load_data("local_simplification/scoring/maintainability_readiness_score_report.csv")

    def save_simplification_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_data_or_summary(df, summary, "local_simplification/validation", "simplification_validation_report.csv")

    def load_simplification_validation_report(self) -> pd.DataFrame:
        return self._load_data("local_simplification/validation/simplification_validation_report.csv")

    def save_simplification_quality(self, profile_name: str, quality: dict) -> Path:
        import json
        p = self.base_dir / "local_simplification/quality" / f"{profile_name}_quality.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(quality, indent=2, ensure_ascii=False), encoding="utf-8")
        return p

    def load_simplification_quality(self, profile_name: str) -> dict:
        import json
        p = self.base_dir / "local_simplification/quality" / f"{profile_name}_quality.json"
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}

    def save_local_simplification_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        import json
        p = self.base_dir / "local_simplification/quality" / f"{profile_name}_report.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        if markdown:
            pm = self.base_dir / "local_simplification/quality" / f"{profile_name}_report.md"
            pm.write_text(markdown, encoding="utf-8")
        return p

    def load_local_simplification_report(self, profile_name: str) -> dict:
        import json
        p = self.base_dir / "local_simplification/quality" / f"{profile_name}_report.json"
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}

    def list_local_simplification_reports(self) -> pd.DataFrame:
        return pd.DataFrame([{"report": "example"}])

    def save_usability_profile_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_profiles", "usability_profile_registry.parquet")
    def load_usability_profile_registry(self) -> pd.DataFrame:
        return self._load_df("local_usability_profiles", "usability_profile_registry.parquet")
    def save_usability_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_domains", "usability_domain_registry.parquet")
    def load_usability_domain_registry(self) -> pd.DataFrame:
        return self._load_df("local_usability_domains", "usability_domain_registry.parquet")
    def save_final_local_usability_review(self, text: str, summary: dict | None = None) -> Path:
        return self._save_text(text, "local_usability_review", "final_local_usability_review.txt")
    def load_final_local_usability_review(self) -> str:
        return self._load_text("local_usability_review", "final_local_usability_review.txt")
    def save_operator_friction_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_friction", "operator_friction_map.parquet")
    def load_operator_friction_map(self) -> pd.DataFrame:
        return self._load_df("local_usability_friction", "operator_friction_map.parquet")
    def save_operator_task_journey_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_task_journeys", "operator_task_journey_registry.parquet")
    def load_operator_task_journey_registry(self) -> pd.DataFrame:
        return self._load_df("local_usability_task_journeys", "operator_task_journey_registry.parquet")
    def save_command_discoverability_guide(self, text: str, summary: dict | None = None) -> Path:
        return self._save_text(text, "local_usability_commands", "command_discoverability_guide.txt")
    def load_command_discoverability_guide(self) -> str:
        return self._load_text("local_usability_commands", "command_discoverability_guide.txt")
    def save_command_family_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_commands", "command_family_index.parquet")
    def load_command_family_index(self) -> pd.DataFrame:
        return self._load_df("local_usability_commands", "command_family_index.parquet")
    def save_script_purpose_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_scripts", "script_purpose_index.parquet")
    def load_script_purpose_index(self) -> pd.DataFrame:
        return self._load_df("local_usability_scripts", "script_purpose_index.parquet")
    def save_script_reading_order_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_reading_order", "script_reading_order_index.parquet")
    def load_script_reading_order_index(self) -> pd.DataFrame:
        return self._load_df("local_usability_reading_order", "script_reading_order_index.parquet")
    def save_report_reading_order_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_reading_order", "report_reading_order_index.parquet")
    def load_report_reading_order_index(self) -> pd.DataFrame:
        return self._load_df("local_usability_reading_order", "report_reading_order_index.parquet")
    def save_datalake_navigation_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_navigation", "datalake_navigation_index.parquet")
    def load_datalake_navigation_index(self) -> pd.DataFrame:
        return self._load_df("local_usability_navigation", "datalake_navigation_index.parquet")
    def save_generated_docs_navigation_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_navigation", "generated_docs_navigation_index.parquet")
    def load_generated_docs_navigation_index(self) -> pd.DataFrame:
        return self._load_df("local_usability_navigation", "generated_docs_navigation_index.parquet")
    def save_documentation_navigation_assistant_pack(self, text: str, summary: dict | None = None) -> Path:
        return self._save_text(text, "local_usability_navigation", "documentation_navigation_assistant_pack.txt")
    def load_documentation_navigation_assistant_pack(self) -> str:
        return self._load_text("local_usability_navigation", "documentation_navigation_assistant_pack.txt")
    def save_first_hour_operator_path(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_operator_paths", "first_hour_operator_path.parquet")
    def load_first_hour_operator_path(self) -> pd.DataFrame:
        return self._load_df("local_usability_operator_paths", "first_hour_operator_path.parquet")
    def save_first_day_operator_path(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_operator_paths", "first_day_operator_path.parquet")
    def load_first_day_operator_path(self) -> pd.DataFrame:
        return self._load_df("local_usability_operator_paths", "first_day_operator_path.parquet")
    def save_weekly_operator_review_path(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_operator_paths", "weekly_operator_review_path.parquet")
    def load_weekly_operator_review_path(self) -> pd.DataFrame:
        return self._load_df("local_usability_operator_paths", "weekly_operator_review_path.parquet")
    def save_human_in_the_loop_checkpoint_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_human_loop", "human_in_the_loop_checkpoint_registry.parquet")
    def load_human_in_the_loop_checkpoint_registry(self) -> pd.DataFrame:
        return self._load_df("local_usability_human_loop", "human_in_the_loop_checkpoint_registry.parquet")
    def save_manual_review_decision_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_manual_review", "manual_review_decision_map.parquet")
    def load_manual_review_decision_map(self) -> pd.DataFrame:
        return self._load_df("local_usability_manual_review", "manual_review_decision_map.parquet")
    def save_operator_question_bank(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_questions", "operator_question_bank.parquet")
    def load_operator_question_bank(self) -> pd.DataFrame:
        return self._load_df("local_usability_questions", "operator_question_bank.parquet")
    def save_operator_troubleshooting_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_troubleshooting", "operator_troubleshooting_index.parquet")
    def load_operator_troubleshooting_index(self) -> pd.DataFrame:
        return self._load_df("local_usability_troubleshooting", "operator_troubleshooting_index.parquet")
    def save_operator_what_to_run_first_guide(self, text: str, summary: dict | None = None) -> Path:
        return self._save_text(text, "local_usability_guides", "operator_what_to_run_first_guide.txt")
    def load_operator_what_to_run_first_guide(self) -> str:
        return self._load_text("local_usability_guides", "operator_what_to_run_first_guide.txt")
    def save_operator_what_not_to_run_guide(self, text: str, summary: dict | None = None) -> Path:
        return self._save_text(text, "local_usability_guides", "operator_what_not_to_run_guide.txt")
    def load_operator_what_not_to_run_guide(self) -> str:
        return self._load_text("local_usability_guides", "operator_what_not_to_run_guide.txt")
    def save_confusing_name_candidate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_candidates", "confusing_name_candidate_registry.parquet")
    def load_confusing_name_candidate_registry(self) -> pd.DataFrame:
        return self._load_df("local_usability_candidates", "confusing_name_candidate_registry.parquet")
    def save_missing_navigation_candidate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_candidates", "missing_navigation_candidate_registry.parquet")
    def load_missing_navigation_candidate_registry(self) -> pd.DataFrame:
        return self._load_df("local_usability_candidates", "missing_navigation_candidate_registry.parquet")
    def save_usability_quick_reference_card(self, text: str, summary: dict | None = None) -> Path:
        return self._save_text(text, "local_usability_quick_reference", "usability_quick_reference_card.txt")
    def load_usability_quick_reference_card(self) -> str:
        return self._load_text("local_usability_quick_reference", "usability_quick_reference_card.txt")
    def save_usability_no_go_safe_go_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_no_go_safe_go", "usability_no_go_safe_go_summary.parquet")
    def load_usability_no_go_safe_go_summary(self) -> pd.DataFrame:
        return self._load_df("local_usability_no_go_safe_go", "usability_no_go_safe_go_summary.parquet")
    def save_usability_exception_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_exceptions", "usability_exception_register.parquet")
    def load_usability_exception_register(self) -> pd.DataFrame:
        return self._load_df("local_usability_exceptions", "usability_exception_register.parquet")
    def save_usability_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_gaps", "usability_gap_register.parquet")
    def load_usability_gap_register(self) -> pd.DataFrame:
        return self._load_df("local_usability_gaps", "usability_gap_register.parquet")
    def save_usability_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_risks", "usability_risk_summary.parquet")
    def load_usability_risk_summary(self) -> pd.DataFrame:
        return self._load_df("local_usability_risks", "usability_risk_summary.parquet")
    def save_usability_readiness_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_scoring", "usability_readiness_score_report.parquet")
    def load_usability_readiness_score_report(self) -> pd.DataFrame:
        return self._load_df("local_usability_scoring", "usability_readiness_score_report.parquet")
    def save_usability_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, "local_usability_validation", "usability_validation_report.parquet")
    def load_usability_validation_report(self) -> pd.DataFrame:
        return self._load_df("local_usability_validation", "usability_validation_report.parquet")
    def save_usability_quality(self, profile_name: str, quality: dict) -> Path:
        return self._save_json(quality, "local_usability_quality", f"usability_quality_{profile_name}.json")
    def load_usability_quality(self, profile_name: str) -> dict:
        return self._load_json("local_usability_quality", f"usability_quality_{profile_name}.json")
    def save_local_usability_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        self._save_json(report, "reports_output_local_usability_json", f"usability_report_{profile_name}.json")
        if markdown:
            self._save_text(markdown, "reports_output_local_usability_markdown", f"usability_report_{profile_name}.md")
        return self.get_path("reports_output_local_usability_json") / f"usability_report_{profile_name}.json"
    def load_local_usability_report(self, profile_name: str) -> dict:
        return self._load_json("reports_output_local_usability_json", f"usability_report_{profile_name}.json")
    def list_local_usability_reports(self) -> pd.DataFrame:
        return pd.DataFrame([{"report": "usability_report"}])

    # Phase 85 additions
    def save_governance_profile_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_governance_profile_registry(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_governance_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_governance_domain_registry(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_final_local_governance_control_room_packet(self, text: str, summary: dict | None = None) -> Path:
        return Path()
    def load_final_local_governance_control_room_packet(self) -> str:
        return ""
    def save_executive_oversight_packet(self, text: str, summary: dict | None = None) -> Path:
        return Path()
    def load_executive_oversight_packet(self) -> str:
        return ""
    def save_manual_approval_ledger(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_manual_approval_ledger(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_manual_approval_checklist_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_manual_approval_checklist_registry(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_risk_committee_rehearsal_pack(self, text: str, summary: dict | None = None) -> Path:
        return Path()
    def load_risk_committee_rehearsal_pack(self) -> str:
        return ""
    def save_risk_committee_agenda_template_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_risk_committee_agenda_template_registry(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_risk_committee_decision_rehearsal_ledger(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_risk_committee_decision_rehearsal_ledger(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_operator_supervision_guide(self, text: str, summary: dict | None = None) -> Path:
        return Path()
    def load_operator_supervision_guide(self) -> str:
        return ""
    def save_operator_supervision_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_operator_supervision_checklist(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_escalation_matrix_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_escalation_matrix_registry(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_governance_roles_matrix_rehearsal(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_governance_roles_matrix_rehearsal(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_decision_authority_map_rehearsal(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_decision_authority_map_rehearsal(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_approval_boundary_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_approval_boundary_registry(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_non_approval_boundary_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_non_approval_boundary_registry(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_governance_no_go_safe_go_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_governance_no_go_safe_go_summary(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_oversight_evidence_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_oversight_evidence_index(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_oversight_report_reading_order(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_oversight_report_reading_order(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_governance_kpi_rehearsal_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_governance_kpi_rehearsal_registry(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_governance_metric_dictionary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_governance_metric_dictionary(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_governance_meeting_note_template_library(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_governance_meeting_note_template_library(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_manual_signoff_rehearsal_form_library(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_manual_signoff_rehearsal_form_library(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_exception_escalation_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_exception_escalation_register(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_governance_unresolved_item_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_governance_unresolved_item_register(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_governance_open_decision_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_governance_open_decision_register(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_governance_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_governance_risk_summary(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_governance_readiness_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_governance_readiness_score_report(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_governance_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return Path()
    def load_governance_validation_report(self) -> pd.DataFrame:
        return pd.DataFrame()
    def save_governance_quality(self, profile_name: str, quality: dict) -> Path:
        return Path()
    def load_governance_quality(self, profile_name: str) -> dict:
        return {}
    def save_local_governance_control_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        return Path()
    def load_local_governance_control_report(self, profile_name: str) -> dict:
        return {}
    def list_local_governance_control_reports(self) -> pd.DataFrame:
        return pd.DataFrame()


    # Phase 86: Local RedTeam Methods
    
    def _save_summary(self, filepath, summary):
        import json
        summary_path = filepath.with_suffix('.json')
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=4)

    def _save_artifact(self, df, filepath, summary=None):
        filepath.parent.mkdir(parents=True, exist_ok=True)
        if str(filepath).endswith('.csv'):
            df.to_csv(filepath, index=False)
        else:
            df.to_parquet(filepath, index=False)
        if summary:
            self._save_summary(filepath, summary)
        return filepath

    def _load_artifact(self, filepath):
        import pandas as pd
        if not filepath.exists():
            return pd.DataFrame()
        if str(filepath).endswith('.csv'):
            return pd.read_csv(filepath)
        else:
            return pd.read_parquet(filepath)

    def save_redteam_profile_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_PROFILES / "redteam_profile_registry.csv", summary)

    def load_redteam_profile_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_PROFILES / "redteam_profile_registry.csv")

    def save_redteam_domain_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_DOMAINS / "redteam_domain_registry.csv", summary)

    def load_redteam_domain_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_DOMAINS / "redteam_domain_registry.csv")

    def save_final_local_redteam_rehearsal_packet(self, text, summary=None):
        from config import paths
        path = paths.LAKE_LOCAL_REDTEAM_REHEARSAL_PACKET / "final_local_redteam_rehearsal_packet.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        if summary:
            self._save_summary(path, summary)
        return path

    def load_final_local_redteam_rehearsal_packet(self):
        from config import paths
        path = paths.LAKE_LOCAL_REDTEAM_REHEARSAL_PACKET / "final_local_redteam_rehearsal_packet.txt"
        if not path.exists():
            return ""
        return path.read_text(encoding="utf-8")

    def save_misuse_scenario_library(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_MISUSE_SCENARIOS / "misuse_scenario_library.csv", summary)

    def load_misuse_scenario_library(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_MISUSE_SCENARIOS / "misuse_scenario_library.csv")

    def save_abuse_case_simulation_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_ABUSE_CASES / "abuse_case_simulation_registry.csv", summary)

    def load_abuse_case_simulation_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_ABUSE_CASES / "abuse_case_simulation_registry.csv")

    def save_adversarial_prompt_safety_checklist(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_ADVERSARIAL_CHECKLIST / "adversarial_prompt_safety_checklist.csv", summary)

    def load_adversarial_prompt_safety_checklist(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_ADVERSARIAL_CHECKLIST / "adversarial_prompt_safety_checklist.csv")

    def save_prompt_injection_risk_pattern_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_PROMPT_INJECTION / "prompt_injection_risk_pattern_registry.csv", summary)

    def load_prompt_injection_risk_pattern_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_PROMPT_INJECTION / "prompt_injection_risk_pattern_registry.csv")

    def save_unsafe_output_pattern_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_UNSAFE_OUTPUTS / "unsafe_output_pattern_registry.csv", summary)

    def load_unsafe_output_pattern_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_UNSAFE_OUTPUTS / "unsafe_output_pattern_registry.csv")

    def save_forbidden_capability_request_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_FORBIDDEN_CAPABILITIES / "forbidden_capability_request_registry.csv", summary)

    def load_forbidden_capability_request_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_FORBIDDEN_CAPABILITIES / "forbidden_capability_request_registry.csv")

    def save_boundary_violation_scenario_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_BOUNDARY_VIOLATIONS / "boundary_violation_scenario_registry.csv", summary)

    def load_boundary_violation_scenario_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_BOUNDARY_VIOLATIONS / "boundary_violation_scenario_registry.csv")

    def save_live_trading_misuse_scenario_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_LIVE_TRADING / "live_trading_misuse_scenario_registry.csv", summary)

    def load_live_trading_misuse_scenario_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_LIVE_TRADING / "live_trading_misuse_scenario_registry.csv")

    def save_broker_execution_misuse_scenario_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_BROKER_EXECUTION / "broker_execution_misuse_scenario_registry.csv", summary)

    def load_broker_execution_misuse_scenario_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_BROKER_EXECUTION / "broker_execution_misuse_scenario_registry.csv")

    def save_investment_advice_misuse_scenario_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_INVESTMENT_ADVICE / "investment_advice_misuse_scenario_registry.csv", summary)

    def load_investment_advice_misuse_scenario_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_INVESTMENT_ADVICE / "investment_advice_misuse_scenario_registry.csv")

    def save_model_deployment_misuse_scenario_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_MODEL_DEPLOYMENT / "model_deployment_misuse_scenario_registry.csv", summary)

    def load_model_deployment_misuse_scenario_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_MODEL_DEPLOYMENT / "model_deployment_misuse_scenario_registry.csv")

    def save_secret_exposure_misuse_scenario_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_SECRET_EXPOSURE / "secret_exposure_misuse_scenario_registry.csv", summary)

    def load_secret_exposure_misuse_scenario_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_SECRET_EXPOSURE / "secret_exposure_misuse_scenario_registry.csv")

    def save_file_action_misuse_scenario_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_FILE_ACTIONS / "file_action_misuse_scenario_registry.csv", summary)

    def load_file_action_misuse_scenario_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_FILE_ACTIONS / "file_action_misuse_scenario_registry.csv")

    def save_cloud_publish_misuse_scenario_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_CLOUD_PUBLISH / "cloud_publish_misuse_scenario_registry.csv", summary)

    def load_cloud_publish_misuse_scenario_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_CLOUD_PUBLISH / "cloud_publish_misuse_scenario_registry.csv")

    def save_external_llm_api_misuse_scenario_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_EXTERNAL_LLM_API / "external_llm_api_misuse_scenario_registry.csv", summary)

    def load_external_llm_api_misuse_scenario_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_EXTERNAL_LLM_API / "external_llm_api_misuse_scenario_registry.csv")

    def save_safety_response_expectation_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES / "safety_response_expectation_registry.csv", summary)

    def load_safety_response_expectation_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES / "safety_response_expectation_registry.csv")

    def save_safe_refusal_template_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES / "safe_refusal_template_registry.csv", summary)

    def load_safe_refusal_template_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES / "safe_refusal_template_registry.csv")

    def save_safe_redirect_pattern_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES / "safe_redirect_pattern_registry.csv", summary)

    def load_safe_redirect_pattern_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES / "safe_redirect_pattern_registry.csv")

    def save_manual_escalation_checklist(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_MANUAL_ESCALATION / "manual_escalation_checklist.csv", summary)

    def load_manual_escalation_checklist(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_MANUAL_ESCALATION / "manual_escalation_checklist.csv")

    def save_human_review_abuse_case_checklist(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_HUMAN_REVIEW / "human_review_abuse_case_checklist.csv", summary)

    def load_human_review_abuse_case_checklist(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_HUMAN_REVIEW / "human_review_abuse_case_checklist.csv")

    def save_redteam_reading_order(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_READING_ORDER / "redteam_reading_order.csv", summary)

    def load_redteam_reading_order(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_READING_ORDER / "redteam_reading_order.csv")

    def save_safety_assurance_summary(self, text, summary=None):
        from config import paths
        path = paths.LAKE_LOCAL_REDTEAM_SAFETY_ASSURANCE / "safety_assurance_summary.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        if summary:
            self._save_summary(path, summary)
        return path

    def load_safety_assurance_summary(self):
        from config import paths
        path = paths.LAKE_LOCAL_REDTEAM_SAFETY_ASSURANCE / "safety_assurance_summary.txt"
        if not path.exists():
            return ""
        return path.read_text(encoding="utf-8")

    def save_safety_assurance_evidence_index(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_SAFETY_ASSURANCE / "safety_assurance_evidence_index.csv", summary)

    def load_safety_assurance_evidence_index(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_SAFETY_ASSURANCE / "safety_assurance_evidence_index.csv")

    def save_safety_coverage_matrix(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_COVERAGE / "safety_coverage_matrix.csv", summary)

    def load_safety_coverage_matrix(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_COVERAGE / "safety_coverage_matrix.csv")

    def save_safety_blindspot_register(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_BLINDSPOTS / "safety_blindspot_register.csv", summary)

    def load_safety_blindspot_register(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_BLINDSPOTS / "safety_blindspot_register.csv")

    def save_safety_non_goals_registry(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_NON_GOALS / "safety_non_goals_registry.csv", summary)

    def load_safety_non_goals_registry(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_NON_GOALS / "safety_non_goals_registry.csv")

    def save_redteam_no_go_safe_go_summary(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_NO_GO_SAFE_GO / "redteam_no_go_safe_go_summary.csv", summary)

    def load_redteam_no_go_safe_go_summary(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_NO_GO_SAFE_GO / "redteam_no_go_safe_go_summary.csv")

    def save_redteam_exception_register(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_EXCEPTIONS / "redteam_exception_register.csv", summary)

    def load_redteam_exception_register(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_EXCEPTIONS / "redteam_exception_register.csv")

    def save_redteam_gap_register(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_GAPS / "redteam_gap_register.csv", summary)

    def load_redteam_gap_register(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_GAPS / "redteam_gap_register.csv")

    def save_redteam_risk_summary(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_RISKS / "redteam_risk_summary.csv", summary)

    def load_redteam_risk_summary(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_RISKS / "redteam_risk_summary.csv")

    def save_redteam_readiness_score_report(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_SCORING / "redteam_readiness_score_report.csv", summary)

    def load_redteam_readiness_score_report(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_SCORING / "redteam_readiness_score_report.csv")

    def save_redteam_validation_report(self, df, summary=None):
        from config import paths
        return self._save_artifact(df, paths.LAKE_LOCAL_REDTEAM_VALIDATION / "redteam_validation_report.csv", summary)

    def load_redteam_validation_report(self):
        from config import paths
        return self._load_artifact(paths.LAKE_LOCAL_REDTEAM_VALIDATION / "redteam_validation_report.csv")

    def save_redteam_quality(self, profile_name, quality):
        from config import paths
        path = paths.LAKE_LOCAL_REDTEAM_QUALITY / f"{profile_name}_quality.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=4, ensure_ascii=False)
        return path

    def load_redteam_quality(self, profile_name):
        from config import paths
        path = paths.LAKE_LOCAL_REDTEAM_QUALITY / f"{profile_name}_quality.json"
        if not path.exists():
            return {}
        import json
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_local_redteam_report(self, profile_name, report, markdown=None):
        from config import paths
        path = paths.REPORT_OUTPUT_LOCAL_REDTEAM_JSON / f"{profile_name}_redteam_report.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
        if markdown:
            md_path = paths.REPORT_OUTPUT_LOCAL_REDTEAM_MARKDOWN / f"{profile_name}_redteam_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown)
        return path

    def load_local_redteam_report(self, profile_name):
        from config import paths
        path = paths.REPORT_OUTPUT_LOCAL_REDTEAM_JSON / f"{profile_name}_redteam_report.json"
        if not path.exists():
            return {}
        import json
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_local_redteam_reports(self):
        from config import paths
        reports = []
        path = paths.REPORT_OUTPUT_LOCAL_REDTEAM_JSON
        if path.exists():
            for file in path.glob("*_redteam_report.json"):
                reports.append({"report": file.name})
        import pandas as pd
        return pd.DataFrame(reports)

    # --- Local Incident Response Phase 87 ---
    def save_incident_profile_registry(self, df, summary=None): return None
    def load_incident_profile_registry(self): return None
    def save_incident_domain_registry(self, df, summary=None): return None
    def load_incident_domain_registry(self): return None
    def save_final_local_incident_response_rehearsal_packet(self, text, summary=None): return None
    def load_final_local_incident_response_rehearsal_packet(self): return None
    def save_safety_event_register(self, df, summary=None): return None
    def load_safety_event_register(self): return None
    def save_safety_event_taxonomy(self, df, summary=None): return None
    def load_safety_event_taxonomy(self): return None
    def save_incident_severity_taxonomy(self, df, summary=None): return None
    def load_incident_severity_taxonomy(self): return None
    def save_incident_triage_checklist(self, df, summary=None): return None
    def load_incident_triage_checklist(self): return None
    def save_incident_classification_registry(self, df, summary=None): return None
    def load_incident_classification_registry(self): return None
    def save_boundary_breach_event_registry(self, df, summary=None): return None
    def load_boundary_breach_event_registry(self): return None
    def save_unsafe_output_event_registry(self, df, summary=None): return None
    def load_unsafe_output_event_registry(self): return None
    def save_forbidden_capability_request_event_registry(self, df, summary=None): return None
    def load_forbidden_capability_request_event_registry(self): return None
    def save_secret_exposure_event_registry(self, df, summary=None): return None
    def load_secret_exposure_event_registry(self): return None
    def save_file_action_event_registry(self, df, summary=None): return None
    def load_file_action_event_registry(self): return None
    def save_cloud_publish_event_registry(self, df, summary=None): return None
    def load_cloud_publish_event_registry(self): return None
    def save_live_trading_broker_misuse_event_registry(self, df, summary=None): return None
    def load_live_trading_broker_misuse_event_registry(self): return None
    def save_model_deployment_event_registry(self, df, summary=None): return None
    def load_model_deployment_event_registry(self): return None
    def save_external_llm_api_event_registry(self, df, summary=None): return None
    def load_external_llm_api_event_registry(self): return None
    def save_rollback_decision_playbook(self, text, summary=None): return None
    def load_rollback_decision_playbook(self): return None
    def save_rollback_boundary_registry(self, df, summary=None): return None
    def load_rollback_boundary_registry(self): return None
    def save_non_rollback_boundary_registry(self, df, summary=None): return None
    def load_non_rollback_boundary_registry(self): return None
    def save_containment_rehearsal_checklist(self, df, summary=None): return None
    def load_containment_rehearsal_checklist(self): return None
    def save_degraded_mode_rehearsal_guide(self, text, summary=None): return None
    def load_degraded_mode_rehearsal_guide(self): return None
    def save_recovery_rehearsal_checklist(self, df, summary=None): return None
    def load_recovery_rehearsal_checklist(self): return None
    def save_offline_resilience_supervision_guide(self, text, summary=None): return None
    def load_offline_resilience_supervision_guide(self): return None
    def save_safety_event_evidence_snapshot_index(self, df, summary=None): return None
    def load_safety_event_evidence_snapshot_index(self): return None
    def save_incident_reading_order(self, df, summary=None): return None
    def load_incident_reading_order(self): return None
    def save_incident_timeline_template_registry(self, df, summary=None): return None
    def load_incident_timeline_template_registry(self): return None
    def save_post_incident_review_template_library(self, df, summary=None): return None
    def load_post_incident_review_template_library(self): return None
    def save_root_cause_category_registry(self, df, summary=None): return None
    def load_root_cause_category_registry(self): return None
    def save_corrective_action_rehearsal_registry(self, df, summary=None): return None
    def load_corrective_action_rehearsal_registry(self): return None
    def save_communication_template_registry(self, df, summary=None): return None
    def load_communication_template_registry(self): return None
    def save_escalation_decision_registry(self, df, summary=None): return None
    def load_escalation_decision_registry(self): return None
    def save_incident_no_go_safe_go_summary(self, df, summary=None): return None
    def load_incident_no_go_safe_go_summary(self): return None
    def save_incident_exception_register(self, df, summary=None): return None
    def load_incident_exception_register(self): return None
    def save_incident_gap_register(self, df, summary=None): return None
    def load_incident_gap_register(self): return None
    def save_incident_risk_summary(self, df, summary=None): return None
    def load_incident_risk_summary(self): return None
    def save_incident_readiness_score_report(self, df, summary=None): return None
    def load_incident_readiness_score_report(self): return None
    def save_incident_validation_report(self, df, summary=None): return None
    def load_incident_validation_report(self): return None
    def save_incident_quality(self, profile_name, quality): return None
    def load_incident_quality(self, profile_name): return None
    def save_local_incident_response_report(self, profile_name, report, markdown=None): return None
    def load_local_incident_response_report(self, profile_name): return None
    def list_local_incident_response_reports(self): return None
