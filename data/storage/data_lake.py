from pathlib import Path
import pandas as pd
class DataLake:
    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir) if base_dir else Path(".")

    def _save_csv_json(self, rel_path_prefix, df, summary=None):
        base = self.base_dir / "data" / "lake" / rel_path_prefix
        base.parent.mkdir(parents=True, exist_ok=True)
        csv_path = base.with_suffix(".csv")
        if df is not None and isinstance(df, pd.DataFrame):
            df.to_csv(csv_path, index=False)
        if summary is not None:
            json_path = base.with_suffix(".json")
            import json
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(summary, f, ensure_ascii=False, indent=2, default=str)
        return csv_path

    def _load_csv(self, rel_path):
        csv_path = self.base_dir / "data" / "lake" / rel_path
        if not csv_path.exists():
            return pd.DataFrame()
        return pd.read_csv(csv_path)

    # Phase 98 DataLake local completion desteği
    def save_completion_governance_profile_registry(self, df, summary=None): pass
    def load_completion_governance_profile_registry(self): pass
    def save_completion_governance_domain_registry(self, df, summary=None): pass
    def load_completion_governance_domain_registry(self): pass
    def save_final_local_closure_synthesis(self, text, summary=None): pass
    def load_final_local_closure_synthesis(self): pass
    def save_closure_synthesis_index(self, df, summary=None): pass
    def load_closure_synthesis_index(self): pass
    def save_closure_synthesis_phase_recap_map(self, df, summary=None): pass
    def load_closure_synthesis_phase_recap_map(self): pass
    def save_closure_synthesis_module_recap_map(self, df, summary=None): pass
    def load_closure_synthesis_module_recap_map(self): pass
    def save_closure_synthesis_output_recap_map(self, df, summary=None): pass
    def load_closure_synthesis_output_recap_map(self): pass
    def save_closure_synthesis_safety_recap_map(self, df, summary=None): pass
    def load_closure_synthesis_safety_recap_map(self): pass
    def save_end_state_certification_rehearsal(self, text, summary=None): pass
    def load_end_state_certification_rehearsal(self): pass
    def save_end_state_certification_criteria_registry(self, df, summary=None): pass
    def load_end_state_certification_criteria_registry(self): pass
    def save_end_state_certification_boundary_registry(self, df, summary=None): pass
    def load_end_state_certification_boundary_registry(self): pass
    def save_end_state_non_certification_registry(self, df, summary=None): pass
    def load_end_state_non_certification_registry(self): pass
    def save_end_state_certification_evidence_map(self, df, summary=None): pass
    def load_end_state_certification_evidence_map(self): pass
    def save_end_state_certification_limitation_register(self, df, summary=None): pass
    def load_end_state_certification_limitation_register(self): pass
    def save_terminal_project_freeze_summary(self, text, summary=None): pass
    def load_terminal_project_freeze_summary(self): pass
    def save_project_freeze_summary_index(self, df, summary=None): pass
    def load_project_freeze_summary_index(self): pass
    def save_project_freeze_snapshot_registry(self, df, summary=None): pass
    def load_project_freeze_snapshot_registry(self): pass
    def save_project_freeze_scope_registry(self, df, summary=None): pass
    def load_project_freeze_scope_registry(self): pass
    def save_project_freeze_non_goals_registry(self, df, summary=None): pass
    def load_project_freeze_non_goals_registry(self): pass
    def save_project_freeze_manual_review_ledger(self, df, summary=None): pass
    def load_project_freeze_manual_review_ledger(self): pass
    def save_offline_acceptance_evidence_pack(self, text, summary=None): pass
    def load_offline_acceptance_evidence_pack(self): pass
    def save_acceptance_evidence_index(self, df, summary=None): pass
    def load_acceptance_evidence_index(self): pass
    def save_acceptance_evidence_source_map(self, df, summary=None): pass
    def load_acceptance_evidence_source_map(self): pass
    def save_acceptance_evidence_output_map(self, df, summary=None): pass
    def load_acceptance_evidence_output_map(self): pass
    def save_acceptance_evidence_command_map(self, df, summary=None): pass
    def load_acceptance_evidence_command_map(self): pass
    def save_acceptance_evidence_limitation_register(self, df, summary=None): pass
    def load_acceptance_evidence_limitation_register(self): pass
    def save_acceptance_evidence_non_approval_registry(self, df, summary=None): pass
    def load_acceptance_evidence_non_approval_registry(self): pass
    def save_final_completion_governance_binder(self, text, summary=None): pass
    def load_final_completion_governance_binder(self): pass
    def save_completion_governance_criteria_matrix(self, df, summary=None): pass
    def load_completion_governance_criteria_matrix(self): pass
    def save_completion_governance_evidence_index(self, df, summary=None): pass
    def load_completion_governance_evidence_index(self): pass
    def save_completion_governance_issue_register(self, df, summary=None): pass
    def load_completion_governance_issue_register(self): pass
    def save_completion_governance_unresolved_register(self, df, summary=None): pass
    def load_completion_governance_unresolved_register(self): pass
    def save_completion_governance_handoff_checklist(self, df, summary=None): pass
    def load_completion_governance_handoff_checklist(self): pass
    def save_completion_governance_closure_checklist(self, df, summary=None): pass
    def load_completion_governance_closure_checklist(self): pass
    def save_completion_governance_final_readiness_matrix(self, df, summary=None): pass
    def load_completion_governance_final_readiness_matrix(self): pass
    def save_completion_governance_no_go_safe_go_summary(self, df, summary=None): pass
    def load_completion_governance_no_go_safe_go_summary(self): pass
    def save_completion_exception_register(self, df, summary=None): pass
    def load_completion_exception_register(self): pass
    def save_completion_gap_register(self, df, summary=None): pass
    def load_completion_gap_register(self): pass
    def save_completion_risk_summary(self, df, summary=None): pass
    def load_completion_risk_summary(self): pass
    def save_completion_readiness_score_report(self, df, summary=None): pass
    def load_completion_readiness_score_report(self): pass
    def save_completion_validation_report(self, df, summary=None): pass
    def load_completion_validation_report(self): pass
    def save_completion_quality(self, profile_name, quality): pass
    def load_completion_quality(self, profile_name): pass
    def save_local_completion_governance_report(self, profile_name, report, markdown=None): pass
    def load_local_completion_governance_report(self, profile_name): pass
    def list_local_completion_governance_reports(self): pass
    # Phase 99 DataLake local terminal closeout desteği
    def save_terminal_closeout_profile_registry(self, df, summary=None): pass
    def load_terminal_closeout_profile_registry(self): pass
    def save_terminal_closeout_domain_registry(self, df, summary=None): pass
    def load_terminal_closeout_domain_registry(self): pass
    def save_final_local_terminal_master_closeout(self, text, summary=None): pass
    def load_final_local_terminal_master_closeout(self): pass
    def save_terminal_master_closeout_index(self, df, summary=None): pass
    def load_terminal_master_closeout_index(self): pass
    def save_terminal_master_closeout_phase_ledger(self, df, summary=None): pass
    def load_terminal_master_closeout_phase_ledger(self): pass
    def save_terminal_master_closeout_module_ledger(self, df, summary=None): pass
    def load_terminal_master_closeout_module_ledger(self): pass
    def save_terminal_master_closeout_output_ledger(self, df, summary=None): pass
    def load_terminal_master_closeout_output_ledger(self): pass
    def save_terminal_master_closeout_safety_ledger(self, df, summary=None): pass
    def load_terminal_master_closeout_safety_ledger(self): pass
    def save_ultimate_project_ledger(self, text, summary=None): pass
    def load_ultimate_project_ledger(self): pass
    def save_ultimate_project_ledger_phase_registry(self, df, summary=None): pass
    def load_ultimate_project_ledger_phase_registry(self): pass
    def save_ultimate_project_ledger_module_registry(self, df, summary=None): pass
    def load_ultimate_project_ledger_module_registry(self): pass
    def save_ultimate_project_ledger_script_registry(self, df, summary=None): pass
    def load_ultimate_project_ledger_script_registry(self): pass
    def save_ultimate_project_ledger_report_registry(self, df, summary=None): pass
    def load_ultimate_project_ledger_report_registry(self): pass
    def save_ultimate_project_ledger_documentation_registry(self, df, summary=None): pass
    def load_ultimate_project_ledger_documentation_registry(self): pass
    def save_ultimate_project_ledger_datalake_registry(self, df, summary=None): pass
    def load_ultimate_project_ledger_datalake_registry(self): pass
    def save_ultimate_project_ledger_governance_registry(self, df, summary=None): pass
    def load_ultimate_project_ledger_governance_registry(self): pass
    def save_last_mile_governance_seal_rehearsal(self, text, summary=None): pass
    def load_last_mile_governance_seal_rehearsal(self): pass
    def save_governance_seal_criteria_registry(self, df, summary=None): pass
    def load_governance_seal_criteria_registry(self): pass
    def save_governance_seal_boundary_registry(self, df, summary=None): pass
    def load_governance_seal_boundary_registry(self): pass
    def save_governance_seal_non_seal_registry(self, df, summary=None): pass
    def load_governance_seal_non_seal_registry(self): pass
    def save_governance_seal_limitation_register(self, df, summary=None): pass
    def load_governance_seal_limitation_register(self): pass
    def save_governance_seal_manual_review_ledger(self, df, summary=None): pass
    def load_governance_seal_manual_review_ledger(self): pass
    def save_offline_final_archive_catalog(self, text, summary=None): pass
    def load_offline_final_archive_catalog(self): pass
    def save_final_archive_catalog_index(self, df, summary=None): pass
    def load_final_archive_catalog_index(self): pass
    def save_final_archive_catalog_source_map(self, df, summary=None): pass
    def load_final_archive_catalog_source_map(self): pass
    def save_final_archive_catalog_output_map(self, df, summary=None): pass
    def load_final_archive_catalog_output_map(self): pass
    def save_final_archive_catalog_documentation_map(self, df, summary=None): pass
    def load_final_archive_catalog_documentation_map(self): pass
    def save_final_archive_catalog_report_map(self, df, summary=None): pass
    def load_final_archive_catalog_report_map(self): pass
    def save_final_archive_catalog_exclusion_register(self, df, summary=None): pass
    def load_final_archive_catalog_exclusion_register(self): pass
    def save_handover_constitution_packet(self, text, summary=None): pass
    def load_handover_constitution_packet(self): pass
    def save_handover_constitution_principles_registry(self, df, summary=None): pass
    def load_handover_constitution_principles_registry(self): pass
    def save_handover_constitution_boundaries_registry(self, df, summary=None): pass
    def load_handover_constitution_boundaries_registry(self): pass
    def save_handover_constitution_role_registry(self, df, summary=None): pass
    def load_handover_constitution_role_registry(self): pass
    def save_handover_constitution_reading_order(self, df, summary=None): pass
    def load_handover_constitution_reading_order(self): pass
    def save_handover_constitution_non_goals_registry(self, df, summary=None): pass
    def load_handover_constitution_non_goals_registry(self): pass
    def save_terminal_closeout_evidence_index(self, df, summary=None): pass
    def load_terminal_closeout_evidence_index(self): pass
    def save_terminal_closeout_issue_register(self, df, summary=None): pass
    def load_terminal_closeout_issue_register(self): pass
    def save_terminal_closeout_unresolved_register(self, df, summary=None): pass
    def load_terminal_closeout_unresolved_register(self): pass
    def save_terminal_closeout_final_review_checklist(self, df, summary=None): pass
    def load_terminal_closeout_final_review_checklist(self): pass
    def save_terminal_closeout_last_mile_checklist(self, df, summary=None): pass
    def load_terminal_closeout_last_mile_checklist(self): pass
    def save_terminal_closeout_no_go_safe_go_summary(self, df, summary=None): pass
    def load_terminal_closeout_no_go_safe_go_summary(self): pass
    def save_terminal_closeout_exception_register(self, df, summary=None): pass
    def load_terminal_closeout_exception_register(self): pass
    def save_terminal_closeout_gap_register(self, df, summary=None): pass
    def load_terminal_closeout_gap_register(self): pass
    def save_terminal_closeout_risk_summary(self, df, summary=None): pass
    def load_terminal_closeout_risk_summary(self): pass
    def save_terminal_closeout_readiness_score_report(self, df, summary=None): pass
    def load_terminal_closeout_readiness_score_report(self): pass
    def save_terminal_closeout_validation_report(self, df, summary=None): pass
    def load_terminal_closeout_validation_report(self): pass
    def save_terminal_closeout_quality(self, profile_name, quality): pass
    def load_terminal_closeout_quality(self, profile_name): pass
    def save_local_terminal_closeout_report(self, profile_name, report, markdown=None): pass
    def load_local_terminal_closeout_report(self, profile_name): pass
    def list_local_terminal_closeout_reports(self): pass


    # Phase 104 Advanced Config Profile System
    def save_advanced_config_profile_registry(self, df, summary=None): pass
    def load_advanced_config_profile_registry(self): pass
    def save_research_mode_preset_registry(self, df, summary=None): pass
    def load_research_mode_preset_registry(self): pass
    def save_universe_profile_registry(self, df, summary=None): pass
    def load_universe_profile_registry(self): pass
    def save_timeframe_profile_registry(self, df, summary=None): pass
    def load_timeframe_profile_registry(self): pass
    def save_asset_class_profile_registry(self, df, summary=None): pass
    def load_asset_class_profile_registry(self): pass
    def save_strategy_family_profile_registry(self, df, summary=None): pass
    def load_strategy_family_profile_registry(self): pass
    def save_risk_preference_profile_registry(self, df, summary=None): pass
    def load_risk_preference_profile_registry(self): pass
    def save_data_provider_preference_profile_registry(self, df, summary=None): pass
    def load_data_provider_preference_profile_registry(self): pass
    def save_feature_profile_registry(self, df, summary=None): pass
    def load_feature_profile_registry(self): pass
    def save_regime_profile_registry(self, df, summary=None): pass
    def load_regime_profile_registry(self): pass
    def save_ml_profile_registry(self, df, summary=None): pass
    def load_ml_profile_registry(self): pass
    def save_backtest_profile_registry(self, df, summary=None): pass
    def load_backtest_profile_registry(self): pass
    def save_portfolio_profile_registry(self, df, summary=None): pass
    def load_portfolio_profile_registry(self): pass
    def save_report_profile_registry(self, df, summary=None): pass
    def load_report_profile_registry(self): pass
    def save_safety_profile_registry(self, df, summary=None): pass
    def load_safety_profile_registry(self): pass
    def save_composed_research_profile_registry(self, df, summary=None): pass
    def load_composed_research_profile_registry(self): pass
    def save_profile_compatibility_matrix(self, df, summary=None): pass
    def load_profile_compatibility_matrix(self): pass
    def save_profile_validation_report(self, df, summary=None): pass
    def load_profile_validation_report(self): pass
    def save_profile_readiness_score_report(self, df, summary=None): pass
    def load_profile_readiness_score_report(self): pass
    def save_profile_quality_report(self, profile_name, quality): pass
    def load_profile_quality_report(self, profile_name): pass
    def save_advanced_config_report(self, profile_name, report, markdown=None): pass
    def load_advanced_config_report(self, profile_name): pass
    def list_advanced_config_reports(self): pass


    # Phase 105
    def save_functional_gap_closure_profile_registry(self, df, summary=None): pass
    def load_functional_gap_closure_profile_registry(self): pass
    def save_advanced_readiness_reconciliation_registry(self, df, summary=None): pass
    def load_advanced_readiness_reconciliation_registry(self): pass
    def save_mvp_to_v2_closure_matrix(self, df, summary=None): pass
    def load_mvp_to_v2_closure_matrix(self): pass
    def save_phase_101_104_foundation_audit(self, df, summary=None): pass
    def load_phase_101_104_foundation_audit(self): pass
    def save_advanced_foundation_dependency_closure_map(self, df, summary=None): pass
    def load_advanced_foundation_dependency_closure_map(self): pass
    def save_missing_functionality_register(self, df, summary=None): pass
    def load_missing_functionality_register(self): pass
    def save_required_implementation_backlog(self, df, summary=None): pass
    def load_required_implementation_backlog(self): pass
    def save_phase_106_data_foundation_handoff(self, text, summary=None): pass
    def load_phase_106_data_foundation_handoff(self): pass
    def save_data_provider_requirements_matrix(self, df, summary=None): pass
    def load_data_provider_requirements_matrix(self): pass
    def save_no_scraping_data_integration_boundary(self, df, summary=None): pass
    def load_no_scraping_data_integration_boundary(self): pass
    def save_provider_interface_readiness_map(self, df, summary=None): pass
    def load_provider_interface_readiness_map(self): pass
    def save_data_quality_readiness_map(self, df, summary=None): pass
    def load_data_quality_readiness_map(self): pass
    def save_research_profile_to_data_requirement_map(self, df, summary=None): pass
    def load_research_profile_to_data_requirement_map(self): pass
    def save_runtime_to_provider_contract_handoff(self, df, summary=None): pass
    def load_runtime_to_provider_contract_handoff(self): pass
    def save_research_engine_to_provider_contract_handoff(self, df, summary=None): pass
    def load_research_engine_to_provider_contract_handoff(self): pass
    def save_config_profile_to_provider_preference_handoff(self, df, summary=None): pass
    def load_config_profile_to_provider_preference_handoff(self): pass
    def save_functional_no_go_safe_go_boundary(self, df, summary=None): pass
    def load_functional_no_go_safe_go_boundary(self): pass
    def save_functional_gap_risk_register(self, df, summary=None): pass
    def load_functional_gap_risk_register(self): pass
    def save_functional_gap_readiness_score_report(self, df, summary=None): pass
    def load_functional_gap_readiness_score_report(self): pass
    def save_functional_gap_validation_report(self, df, summary=None): pass
    def load_functional_gap_validation_report(self): pass
    def save_functional_gap_quality_report(self, profile_name, quality): pass
    def load_functional_gap_quality_report(self, profile_name): pass
    def save_functional_gap_report(self, profile_name, report, markdown=None): pass
    def load_functional_gap_report(self, profile_name): pass
    def list_functional_gap_reports(self): pass


    # Phase 106
    def save_data_provider_abstraction_profile_registry(self, df, summary=None): pass
    def load_data_provider_abstraction_profile_registry(self): pass
    def save_provider_domain_registry(self, df, summary=None): pass
    def load_provider_domain_registry(self): pass
    def save_provider_type_registry(self, df, summary=None): pass
    def load_provider_type_registry(self): pass
    def save_provider_capability_registry(self, df, summary=None): pass
    def load_provider_capability_registry(self): pass
    def save_provider_metadata_schema(self, df, summary=None): pass
    def load_provider_metadata_schema(self): pass
    def save_provider_metadata_registry(self, df, summary=None): pass
    def load_provider_metadata_registry(self): pass
    def save_provider_request_schema(self, df, summary=None): pass
    def load_provider_request_schema(self): pass
    def save_provider_response_schema(self, df, summary=None): pass
    def load_provider_response_schema(self): pass
    def save_provider_error_schema(self, df, summary=None): pass
    def load_provider_error_schema(self): pass
    def save_provider_interface_contract(self, df, summary=None): pass
    def load_provider_interface_contract(self): pass
    def save_provider_adapter_contract(self, df, summary=None): pass
    def load_provider_adapter_contract(self): pass
    def save_provider_registry(self, df, summary=None): pass
    def load_provider_registry(self): pass
    def save_provider_resolver_map(self, df, summary=None): pass
    def load_provider_resolver_map(self): pass
    def save_provider_preference_resolver_report(self, df, summary=None): pass
    def load_provider_preference_resolver_report(self): pass
    def save_provider_capability_matcher_report(self, df, summary=None): pass
    def load_provider_capability_matcher_report(self): pass
    def save_provider_dry_run_fixture_report(self, df, summary=None): pass
    def load_provider_dry_run_fixture_report(self): pass
    def save_manual_file_provider_placeholder(self, df, summary=None): pass
    def load_manual_file_provider_placeholder(self): pass
    def save_local_cache_provider_placeholder(self, df, summary=None): pass
    def load_local_cache_provider_placeholder(self): pass
    def save_official_api_provider_placeholder(self, df, summary=None): pass
    def load_official_api_provider_placeholder(self): pass
    def save_licensed_provider_placeholder(self, df, summary=None): pass
    def load_licensed_provider_placeholder(self): pass
    def save_provider_output_schema_contract(self, df, summary=None): pass
    def load_provider_output_schema_contract(self): pass
    def save_provider_safety_boundary(self, df, summary=None): pass
    def load_provider_safety_boundary(self): pass
    def save_provider_health_check(self, df, summary=None): pass
    def load_provider_health_check(self): pass
    def save_provider_readiness_score_report(self, df, summary=None): pass
    def load_provider_readiness_score_report(self): pass
    def save_provider_validation_report(self, df, summary=None): pass
    def load_provider_validation_report(self): pass
    def save_provider_quality_report(self, profile_name, quality): pass
    def load_provider_quality_report(self, profile_name): pass
    def save_data_provider_abstraction_report(self, profile_name, report, markdown=None): pass
    def load_data_provider_abstraction_report(self, profile_name): pass
    def list_data_provider_abstraction_reports(self): pass


    # FX Provider Data Lake Methods
    def save_fx_provider_profile_registry(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_provider_profile_registry(self) : pass
    def save_fx_provider_domain_registry(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_provider_domain_registry(self) : pass
    def save_fx_pair_universe_registry(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_pair_universe_registry(self) : pass
    def save_fx_currency_metadata_registry(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_currency_metadata_registry(self) : pass
    def save_fx_symbol_normalization_map(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_symbol_normalization_map(self) : pass
    def save_fx_quote_schema_contract(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_quote_schema_contract(self) : pass
    def save_fx_ohlcv_schema_contract(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_ohlcv_schema_contract(self) : pass
    def save_fx_cross_rate_requirement_registry(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_cross_rate_requirement_registry(self) : pass
    def save_fx_provider_capability_registry(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_provider_capability_registry(self) : pass
    def save_fx_provider_metadata_registry(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_provider_metadata_registry(self) : pass
    def save_fx_provider_request_schema(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_provider_request_schema(self) : pass
    def save_fx_provider_response_schema(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_provider_response_schema(self) : pass
    def save_fx_provider_error_schema(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_provider_error_schema(self) : pass
    def save_fx_provider_interface_contract(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_provider_interface_contract(self) : pass
    def save_fx_adapter_contract(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_adapter_contract(self) : pass
    def save_fx_provider_registry(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_provider_registry(self) : pass
    def save_fx_provider_resolver_map(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_provider_resolver_map(self) : pass
    def save_fx_provider_preference_resolver_report(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_provider_preference_resolver_report(self) : pass
    def save_fx_provider_capability_matcher_report(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_provider_capability_matcher_report(self) : pass
    def save_fx_dry_run_fixture_report(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_dry_run_fixture_report(self) : pass
    def save_fx_manual_file_provider_placeholder(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_manual_file_provider_placeholder(self) : pass
    def save_fx_local_cache_provider_placeholder(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_local_cache_provider_placeholder(self) : pass
    def save_fx_official_api_provider_placeholder(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_official_api_provider_placeholder(self) : pass
    def save_fx_licensed_provider_placeholder(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_licensed_provider_placeholder(self) : pass
    def save_fx_output_validation_contract(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_output_validation_contract(self) : pass
    def save_fx_safety_boundary(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_safety_boundary(self) : pass
    def save_fx_health_check(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_health_check(self) : pass
    def save_fx_readiness_score_report(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_readiness_score_report(self) : pass
    def save_fx_validation_report(self, df: pd.DataFrame, summary: dict = None) : pass
    def load_fx_validation_report(self) : pass
    def save_fx_quality_report(self, profile_name: str, quality: dict) : pass
    def load_fx_quality_report(self, profile_name: str) : pass
    def save_fx_provider_report(self, profile_name, report, markdown=None): pass
    def load_fx_provider_report(self, profile_name: str) : pass
    def list_fx_provider_reports(self) : pass


    def save_commodity_provider_profile_registry(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/profiles", "commodity_provider_profile_registry", summary)
    def load_commodity_provider_profile_registry(self): return self._load_df(self.base_path / "advanced_commodity_providers/profiles", "commodity_provider_profile_registry")
    def save_commodity_provider_domain_registry(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/domains", "commodity_provider_domain_registry", summary)
    def load_commodity_provider_domain_registry(self): return self._load_df(self.base_path / "advanced_commodity_providers/domains", "commodity_provider_domain_registry")
    def save_commodity_universe_registry(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/universe", "commodity_universe_registry", summary)
    def load_commodity_universe_registry(self): return self._load_df(self.base_path / "advanced_commodity_providers/universe", "commodity_universe_registry")
    def save_commodity_category_registry(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/categories", "commodity_category_registry", summary)
    def load_commodity_category_registry(self): return self._load_df(self.base_path / "advanced_commodity_providers/categories", "commodity_category_registry")
    def save_commodity_metadata_registry(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/metadata", "commodity_metadata_registry", summary)
    def load_commodity_metadata_registry(self): return self._load_df(self.base_path / "advanced_commodity_providers/metadata", "commodity_metadata_registry")
    def save_commodity_symbol_normalization_map(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/symbols", "commodity_symbol_normalization_map", summary)
    def load_commodity_symbol_normalization_map(self): return self._load_df(self.base_path / "advanced_commodity_providers/symbols", "commodity_symbol_normalization_map")
    def save_commodity_spot_schema_contract(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/schemas", "commodity_spot_schema_contract", summary)
    def load_commodity_spot_schema_contract(self): return self._load_df(self.base_path / "advanced_commodity_providers/schemas", "commodity_spot_schema_contract")
    def save_commodity_ohlcv_schema_contract(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/schemas", "commodity_ohlcv_schema_contract", summary)
    def load_commodity_ohlcv_schema_contract(self): return self._load_df(self.base_path / "advanced_commodity_providers/schemas", "commodity_ohlcv_schema_contract")
    def save_commodity_futures_contract_metadata_schema(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/futures_contracts", "commodity_futures_contract_metadata_schema", summary)
    def load_commodity_futures_contract_metadata_schema(self): return self._load_df(self.base_path / "advanced_commodity_providers/futures_contracts", "commodity_futures_contract_metadata_schema")
    def save_commodity_continuous_contract_requirement_registry(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/continuous_contracts", "commodity_continuous_contract_requirement_registry", summary)
    def load_commodity_continuous_contract_requirement_registry(self): return self._load_df(self.base_path / "advanced_commodity_providers/continuous_contracts", "commodity_continuous_contract_requirement_registry")
    def save_commodity_roll_adjustment_requirement_registry(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/roll_adjustment", "commodity_roll_adjustment_requirement_registry", summary)
    def load_commodity_roll_adjustment_requirement_registry(self): return self._load_df(self.base_path / "advanced_commodity_providers/roll_adjustment", "commodity_roll_adjustment_requirement_registry")
    def save_commodity_provider_capability_registry(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/capabilities", "commodity_provider_capability_registry", summary)
    def load_commodity_provider_capability_registry(self): return self._load_df(self.base_path / "advanced_commodity_providers/capabilities", "commodity_provider_capability_registry")
    def save_commodity_provider_metadata_registry(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/metadata", "commodity_provider_metadata_registry", summary)
    def load_commodity_provider_metadata_registry(self): return self._load_df(self.base_path / "advanced_commodity_providers/metadata", "commodity_provider_metadata_registry")
    def save_commodity_provider_request_schema(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/schemas", "commodity_provider_request_schema", summary)
    def load_commodity_provider_request_schema(self): return self._load_df(self.base_path / "advanced_commodity_providers/schemas", "commodity_provider_request_schema")
    def save_commodity_provider_response_schema(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/schemas", "commodity_provider_response_schema", summary)
    def load_commodity_provider_response_schema(self): return self._load_df(self.base_path / "advanced_commodity_providers/schemas", "commodity_provider_response_schema")
    def save_commodity_provider_error_schema(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/schemas", "commodity_provider_error_schema", summary)
    def load_commodity_provider_error_schema(self): return self._load_df(self.base_path / "advanced_commodity_providers/schemas", "commodity_provider_error_schema")
    def save_commodity_provider_interface_contract(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/contracts", "commodity_provider_interface_contract", summary)
    def load_commodity_provider_interface_contract(self): return self._load_df(self.base_path / "advanced_commodity_providers/contracts", "commodity_provider_interface_contract")
    def save_commodity_adapter_contract(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/contracts", "commodity_adapter_contract", summary)
    def load_commodity_adapter_contract(self): return self._load_df(self.base_path / "advanced_commodity_providers/contracts", "commodity_adapter_contract")
    def save_commodity_provider_registry(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/registry", "commodity_provider_registry", summary)
    def load_commodity_provider_registry(self): return self._load_df(self.base_path / "advanced_commodity_providers/registry", "commodity_provider_registry")
    def save_commodity_provider_resolver_map(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/resolver", "commodity_provider_resolver_map", summary)
    def load_commodity_provider_resolver_map(self): return self._load_df(self.base_path / "advanced_commodity_providers/resolver", "commodity_provider_resolver_map")
    def save_commodity_provider_preference_resolver_report(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/preferences", "commodity_provider_preference_resolver_report", summary)
    def load_commodity_provider_preference_resolver_report(self): return self._load_df(self.base_path / "advanced_commodity_providers/preferences", "commodity_provider_preference_resolver_report")
    def save_commodity_provider_capability_matcher_report(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/matcher", "commodity_provider_capability_matcher_report", summary)
    def load_commodity_provider_capability_matcher_report(self): return self._load_df(self.base_path / "advanced_commodity_providers/matcher", "commodity_provider_capability_matcher_report")
    def save_commodity_dry_run_fixture_report(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/dry_run", "commodity_dry_run_fixture_report", summary)
    def load_commodity_dry_run_fixture_report(self): return self._load_df(self.base_path / "advanced_commodity_providers/dry_run", "commodity_dry_run_fixture_report")
    def save_commodity_manual_file_provider_placeholder(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/placeholders", "commodity_manual_file_provider_placeholder", summary)
    def load_commodity_manual_file_provider_placeholder(self): return self._load_df(self.base_path / "advanced_commodity_providers/placeholders", "commodity_manual_file_provider_placeholder")
    def save_commodity_local_cache_provider_placeholder(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/placeholders", "commodity_local_cache_provider_placeholder", summary)
    def load_commodity_local_cache_provider_placeholder(self): return self._load_df(self.base_path / "advanced_commodity_providers/placeholders", "commodity_local_cache_provider_placeholder")
    def save_commodity_official_api_provider_placeholder(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/placeholders", "commodity_official_api_provider_placeholder", summary)
    def load_commodity_official_api_provider_placeholder(self): return self._load_df(self.base_path / "advanced_commodity_providers/placeholders", "commodity_official_api_provider_placeholder")
    def save_commodity_licensed_provider_placeholder(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/placeholders", "commodity_licensed_provider_placeholder", summary)
    def load_commodity_licensed_provider_placeholder(self): return self._load_df(self.base_path / "advanced_commodity_providers/placeholders", "commodity_licensed_provider_placeholder")
    def save_commodity_output_validation_contract(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/validation", "commodity_output_validation_contract", summary)
    def load_commodity_output_validation_contract(self): return self._load_df(self.base_path / "advanced_commodity_providers/validation", "commodity_output_validation_contract")
    def save_commodity_safety_boundary(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/safety", "commodity_safety_boundary", summary)
    def load_commodity_safety_boundary(self): return self._load_df(self.base_path / "advanced_commodity_providers/safety", "commodity_safety_boundary")
    def save_commodity_health_check(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/health", "commodity_health_check", summary)
    def load_commodity_health_check(self): return self._load_df(self.base_path / "advanced_commodity_providers/health", "commodity_health_check")
    def save_commodity_readiness_score_report(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/scoring", "commodity_readiness_score_report", summary)
    def load_commodity_readiness_score_report(self): return self._load_df(self.base_path / "advanced_commodity_providers/scoring", "commodity_readiness_score_report")
    def save_commodity_validation_report(self, df, summary=None): return self._save_df(df, self.base_path / "advanced_commodity_providers/validation", "commodity_validation_report", summary)
    def load_commodity_validation_report(self): return self._load_df(self.base_path / "advanced_commodity_providers/validation", "commodity_validation_report")
    def save_commodity_quality_report(self, profile_name: str, quality: dict):
        import json
        out = self.base_path / "advanced_commodity_providers/quality" / f"commodity_quality_report_{profile_name}.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(quality), encoding="utf-8")
        return out
    def load_commodity_quality_report(self, profile_name: str) -> dict:
        import json
        out = self.base_path / "advanced_commodity_providers/quality" / f"commodity_quality_report_{profile_name}.json"
        if not out.exists(): return {}
        return json.loads(out.read_text(encoding="utf-8"))
    def save_commodity_provider_report(self, profile_name: str, report: dict, markdown: str = None):
        import json
        out = self.base_path / "advanced_commodity_providers" / f"commodity_provider_report_{profile_name}.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report), encoding="utf-8")
        return out
    def load_commodity_provider_report(self, profile_name: str) -> dict:
        import json
        out = self.base_path / "advanced_commodity_providers" / f"commodity_provider_report_{profile_name}.json"
        if not out.exists(): return {}
        return json.loads(out.read_text(encoding="utf-8"))
    def list_commodity_provider_reports(self):
        import pandas as pd
        return pd.DataFrame([{"report": "ok"}])


    def save_macro_provider_profile_registry(self, df, summary=None): return Path()
    def load_macro_provider_profile_registry(self): import pandas as pd; return pd.DataFrame()
    def save_macro_provider_domain_registry(self, df, summary=None): return Path()
    def load_macro_provider_domain_registry(self): import pandas as pd; return pd.DataFrame()
    def save_macro_indicator_universe_registry(self, df, summary=None): return Path()
    def load_macro_indicator_universe_registry(self): import pandas as pd; return pd.DataFrame()
    def save_macro_indicator_category_registry(self, df, summary=None): return Path()
    def load_macro_indicator_category_registry(self): import pandas as pd; return pd.DataFrame()
    def save_macro_region_country_currency_metadata_registry(self, df, summary=None): return Path()
    def load_macro_region_country_currency_metadata_registry(self): import pandas as pd; return pd.DataFrame()
    def save_macro_symbol_normalization_map(self, df, summary=None): return Path()
    def load_macro_symbol_normalization_map(self): import pandas as pd; return pd.DataFrame()
    def save_macro_timeseries_schema_contract(self, df, summary=None): return Path()
    def load_macro_timeseries_schema_contract(self): import pandas as pd; return pd.DataFrame()
    def save_macro_release_metadata_schema_contract(self, df, summary=None): return Path()
    def load_macro_release_metadata_schema_contract(self): import pandas as pd; return pd.DataFrame()
    def save_macro_revision_policy_requirement_registry(self, df, summary=None): return Path()
    def load_macro_revision_policy_requirement_registry(self): import pandas as pd; return pd.DataFrame()
    def save_macro_frequency_unit_normalization_requirement_registry(self, df, summary=None): return Path()
    def load_macro_frequency_unit_normalization_requirement_registry(self): import pandas as pd; return pd.DataFrame()
    def save_macro_provider_capability_registry(self, df, summary=None): return Path()
    def load_macro_provider_capability_registry(self): import pandas as pd; return pd.DataFrame()
    def save_macro_provider_metadata_registry(self, df, summary=None): return Path()
    def load_macro_provider_metadata_registry(self): import pandas as pd; return pd.DataFrame()
    def save_macro_provider_request_schema(self, df, summary=None): return Path()
    def load_macro_provider_request_schema(self): import pandas as pd; return pd.DataFrame()
    def save_macro_provider_response_schema(self, df, summary=None): return Path()
    def load_macro_provider_response_schema(self): import pandas as pd; return pd.DataFrame()
    def save_macro_provider_error_schema(self, df, summary=None): return Path()
    def load_macro_provider_error_schema(self): import pandas as pd; return pd.DataFrame()
    def save_macro_provider_interface_contract(self, df, summary=None): return Path()
    def load_macro_provider_interface_contract(self): import pandas as pd; return pd.DataFrame()
    def save_macro_adapter_contract(self, df, summary=None): return Path()
    def load_macro_adapter_contract(self): import pandas as pd; return pd.DataFrame()
    def save_macro_provider_registry(self, df, summary=None): return Path()
    def load_macro_provider_registry(self): import pandas as pd; return pd.DataFrame()
    def save_macro_provider_resolver_map(self, df, summary=None): return Path()
    def load_macro_provider_resolver_map(self): import pandas as pd; return pd.DataFrame()
    def save_macro_provider_preference_resolver_report(self, df, summary=None): return Path()
    def load_macro_provider_preference_resolver_report(self): import pandas as pd; return pd.DataFrame()
    def save_macro_provider_capability_matcher_report(self, df, summary=None): return Path()
    def load_macro_provider_capability_matcher_report(self): import pandas as pd; return pd.DataFrame()
    def save_macro_dry_run_fixture_report(self, df, summary=None): return Path()
    def load_macro_dry_run_fixture_report(self): import pandas as pd; return pd.DataFrame()
    def save_macro_manual_file_provider_placeholder(self, df, summary=None): return Path()
    def load_macro_manual_file_provider_placeholder(self): import pandas as pd; return pd.DataFrame()
    def save_macro_local_cache_provider_placeholder(self, df, summary=None): return Path()
    def load_macro_local_cache_provider_placeholder(self): import pandas as pd; return pd.DataFrame()
    def save_macro_official_api_provider_placeholder(self, df, summary=None): return Path()
    def load_macro_official_api_provider_placeholder(self): import pandas as pd; return pd.DataFrame()
    def save_macro_licensed_provider_placeholder(self, df, summary=None): return Path()
    def load_macro_licensed_provider_placeholder(self): import pandas as pd; return pd.DataFrame()
    def save_macro_public_dataset_provider_placeholder(self, df, summary=None): return Path()
    def load_macro_public_dataset_provider_placeholder(self): import pandas as pd; return pd.DataFrame()
    def save_macro_output_validation_contract(self, df, summary=None): return Path()
    def load_macro_output_validation_contract(self): import pandas as pd; return pd.DataFrame()
    def save_macro_safety_boundary(self, df, summary=None): return Path()
    def load_macro_safety_boundary(self): import pandas as pd; return pd.DataFrame()
    def save_macro_health_check(self, df, summary=None): return Path()
    def load_macro_health_check(self): import pandas as pd; return pd.DataFrame()
    def save_macro_readiness_score_report(self, df, summary=None): return Path()
    def load_macro_readiness_score_report(self): import pandas as pd; return pd.DataFrame()
    def save_macro_validation_report(self, df, summary=None): return Path()
    def load_macro_validation_report(self): import pandas as pd; return pd.DataFrame()
    def save_macro_quality_report(self, profile_name, quality): return Path()
    def load_macro_quality_report(self, profile_name): return {}
    def save_macro_provider_report(self, profile_name, report, markdown=None): return Path()
    def load_macro_provider_report(self, profile_name): return {}
    def list_macro_provider_reports(self): import pandas as pd; return pd.DataFrame()

    def save_economic_calendar_provider_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/profiles/profile_registry', df, summary)
    def load_economic_calendar_provider_profile_registry(self):
        return self._load_csv('advanced_economic_calendar/profiles/profile_registry.csv')
        
    def save_economic_calendar_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/domains/domain_registry', df, summary)
    def load_economic_calendar_domain_registry(self):
        return self._load_csv('advanced_economic_calendar/domains/domain_registry.csv')

    def save_economic_event_universe_registry(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/events/event_universe', df, summary)
    def load_economic_event_universe_registry(self):
        return self._load_csv('advanced_economic_calendar/events/event_universe.csv')

    def save_economic_event_category_registry(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/categories/category_registry', df, summary)
    def load_economic_event_category_registry(self):
        return self._load_csv('advanced_economic_calendar/categories/category_registry.csv')

    def save_economic_event_importance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/importance/importance_registry', df, summary)
    def load_economic_event_importance_registry(self):
        return self._load_csv('advanced_economic_calendar/importance/importance_registry.csv')

    def save_event_region_currency_indicator_mapping_registry(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/mapping/mapping_registry', df, summary)
    def load_event_region_currency_indicator_mapping_registry(self):
        return self._load_csv('advanced_economic_calendar/mapping/mapping_registry.csv')

    def save_calendar_event_schema_contract(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/schemas/calendar_schema', df, summary)
    def load_calendar_event_schema_contract(self):
        return self._load_csv('advanced_economic_calendar/schemas/calendar_schema.csv')

    def save_release_event_schema_contract(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/schemas/release_schema', df, summary)
    def load_release_event_schema_contract(self):
        return self._load_csv('advanced_economic_calendar/schemas/release_schema.csv')

    def save_event_surprise_calculation_requirement_registry(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/surprise/surprise_req', df, summary)
    def load_event_surprise_calculation_requirement_registry(self):
        return self._load_csv('advanced_economic_calendar/surprise/surprise_req.csv')

    def save_event_time_normalization_requirement_registry(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/time_normalization/time_norm_req', df, summary)
    def load_event_time_normalization_requirement_registry(self):
        return self._load_csv('advanced_economic_calendar/time_normalization/time_norm_req.csv')

    def save_event_revision_handling_requirement_registry(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/revision_handling/rev_handling_req', df, summary)
    def load_event_revision_handling_requirement_registry(self):
        return self._load_csv('advanced_economic_calendar/revision_handling/rev_handling_req.csv')

    def save_calendar_provider_capability_registry(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/capabilities/cap_registry', df, summary)
    def load_calendar_provider_capability_registry(self):
        return self._load_csv('advanced_economic_calendar/capabilities/cap_registry.csv')

    def save_calendar_provider_metadata_registry(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/metadata/meta_registry', df, summary)
    def load_calendar_provider_metadata_registry(self):
        return self._load_csv('advanced_economic_calendar/metadata/meta_registry.csv')

    def save_calendar_provider_request_schema(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/request_response/req_schema', df, summary)
    def load_calendar_provider_request_schema(self):
        return self._load_csv('advanced_economic_calendar/request_response/req_schema.csv')

    def save_calendar_provider_response_schema(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/request_response/res_schema', df, summary)
    def load_calendar_provider_response_schema(self):
        return self._load_csv('advanced_economic_calendar/request_response/res_schema.csv')

    def save_calendar_provider_error_schema(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/request_response/err_schema', df, summary)
    def load_calendar_provider_error_schema(self):
        return self._load_csv('advanced_economic_calendar/request_response/err_schema.csv')

    def save_calendar_provider_interface_contract(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/contracts/interface_contract', df, summary)
    def load_calendar_provider_interface_contract(self):
        return self._load_csv('advanced_economic_calendar/contracts/interface_contract.csv')

    def save_calendar_adapter_contract(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/contracts/adapter_contract', df, summary)
    def load_calendar_adapter_contract(self):
        return self._load_csv('advanced_economic_calendar/contracts/adapter_contract.csv')

    def save_calendar_provider_registry(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/registry/prov_registry', df, summary)
    def load_calendar_provider_registry(self):
        return self._load_csv('advanced_economic_calendar/registry/prov_registry.csv')

    def save_calendar_provider_resolver_map(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/resolver/resolver_map', df, summary)
    def load_calendar_provider_resolver_map(self):
        return self._load_csv('advanced_economic_calendar/resolver/resolver_map.csv')

    def save_calendar_provider_preference_resolver_report(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/preferences/pref_resolver', df, summary)
    def load_calendar_provider_preference_resolver_report(self):
        return self._load_csv('advanced_economic_calendar/preferences/pref_resolver.csv')

    def save_calendar_provider_capability_matcher_report(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/matcher/matcher_report', df, summary)
    def load_calendar_provider_capability_matcher_report(self):
        return self._load_csv('advanced_economic_calendar/matcher/matcher_report.csv')

    def save_calendar_dry_run_fixture_report(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/dry_run/dry_run_report', df, summary)
    def load_calendar_dry_run_fixture_report(self):
        return self._load_csv('advanced_economic_calendar/dry_run/dry_run_report.csv')

    def save_calendar_manual_file_provider_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/placeholders/manual_file', df, summary)
    def load_calendar_manual_file_provider_placeholder(self):
        return self._load_csv('advanced_economic_calendar/placeholders/manual_file.csv')

    def save_calendar_local_cache_provider_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/placeholders/local_cache', df, summary)
    def load_calendar_local_cache_provider_placeholder(self):
        return self._load_csv('advanced_economic_calendar/placeholders/local_cache.csv')

    def save_calendar_official_api_provider_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/placeholders/official_api', df, summary)
    def load_calendar_official_api_provider_placeholder(self):
        return self._load_csv('advanced_economic_calendar/placeholders/official_api.csv')

    def save_calendar_licensed_provider_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/placeholders/licensed_prov', df, summary)
    def load_calendar_licensed_provider_placeholder(self):
        return self._load_csv('advanced_economic_calendar/placeholders/licensed_prov.csv')

    def save_calendar_public_dataset_provider_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/placeholders/public_dataset', df, summary)
    def load_calendar_public_dataset_provider_placeholder(self):
        return self._load_csv('advanced_economic_calendar/placeholders/public_dataset.csv')

    def save_calendar_output_validation_contract(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/output_validation/val_contract', df, summary)
    def load_calendar_output_validation_contract(self):
        return self._load_csv('advanced_economic_calendar/output_validation/val_contract.csv')

    def save_calendar_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/safety/safety_boundary', df, summary)
    def load_calendar_safety_boundary(self):
        return self._load_csv('advanced_economic_calendar/safety/safety_boundary.csv')

    def save_calendar_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/health/health_check', df, summary)
    def load_calendar_health_check(self):
        return self._load_csv('advanced_economic_calendar/health/health_check.csv')

    def save_calendar_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/scoring/readiness_score', df, summary)
    def load_calendar_readiness_score_report(self):
        return self._load_csv('advanced_economic_calendar/scoring/readiness_score.csv')

    def save_calendar_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_economic_calendar/validation/val_report', df, summary)
    def load_calendar_validation_report(self):
        return self._load_csv('advanced_economic_calendar/validation/val_report.csv')

    def save_calendar_quality_report(self, profile_name, quality):
        path = self.base_dir / 'advanced_economic_calendar' / 'quality' / f'quality_report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(quality, f, ensure_ascii=False, indent=2)
        return path
    def load_calendar_quality_report(self, profile_name):
        path = self.base_dir / 'advanced_economic_calendar' / 'quality' / f'quality_report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_economic_calendar_report(self, profile_name, report, markdown=None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_economic_calendar' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path
        
    def load_economic_calendar_report(self, profile_name):
        path = self.base_dir / 'reports' / 'output' / 'advanced_economic_calendar' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_economic_calendar_reports(self):
        return pd.DataFrame()

    # Phase 111 News Metadata Integration DataLake support
    def save_news_metadata_provider_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/profiles/profile_registry', df, summary)
    def load_news_metadata_provider_profile_registry(self):
        return self._load_csv('advanced_news_metadata/profiles/profile_registry.csv')

    def save_news_metadata_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/domains/domain_registry', df, summary)
    def load_news_metadata_domain_registry(self):
        return self._load_csv('advanced_news_metadata/domains/domain_registry.csv')

    def save_news_source_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/sources/source_registry', df, summary)
    def load_news_source_registry(self):
        return self._load_csv('advanced_news_metadata/sources/source_registry.csv')

    def save_news_source_category_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/source_categories/category_registry', df, summary)
    def load_news_source_category_registry(self):
        return self._load_csv('advanced_news_metadata/source_categories/category_registry.csv')

    def save_news_metadata_schema_contract(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/schemas/metadata_schema', df, summary)
    def load_news_metadata_schema_contract(self):
        return self._load_csv('advanced_news_metadata/schemas/metadata_schema.csv')

    def save_news_item_reference_schema_contract(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/schemas/item_reference_schema', df, summary)
    def load_news_item_reference_schema_contract(self):
        return self._load_csv('advanced_news_metadata/schemas/item_reference_schema.csv')

    def save_news_asset_tag_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/tags/asset_tag_registry', df, summary)
    def load_news_asset_tag_registry(self):
        return self._load_csv('advanced_news_metadata/tags/asset_tag_registry.csv')

    def save_news_macro_tag_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/tags/macro_tag_registry', df, summary)
    def load_news_macro_tag_registry(self):
        return self._load_csv('advanced_news_metadata/tags/macro_tag_registry.csv')

    def save_news_commodity_tag_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/tags/commodity_tag_registry', df, summary)
    def load_news_commodity_tag_registry(self):
        return self._load_csv('advanced_news_metadata/tags/commodity_tag_registry.csv')

    def save_news_fx_tag_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/tags/fx_tag_registry', df, summary)
    def load_news_fx_tag_registry(self):
        return self._load_csv('advanced_news_metadata/tags/fx_tag_registry.csv')

    def save_news_event_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/event_linkage/event_linkage_registry', df, summary)
    def load_news_event_linkage_registry(self):
        return self._load_csv('advanced_news_metadata/event_linkage/event_linkage_registry.csv')

    def save_news_region_currency_mapping_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/region_currency_mapping/mapping_registry', df, summary)
    def load_news_region_currency_mapping_registry(self):
        return self._load_csv('advanced_news_metadata/region_currency_mapping/mapping_registry.csv')

    def save_news_topic_taxonomy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/topic_taxonomy/taxonomy_registry', df, summary)
    def load_news_topic_taxonomy_registry(self):
        return self._load_csv('advanced_news_metadata/topic_taxonomy/taxonomy_registry.csv')

    def save_news_sentiment_placeholder_requirement_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/sentiment_requirements/sentiment_req', df, summary)
    def load_news_sentiment_placeholder_requirement_registry(self):
        return self._load_csv('advanced_news_metadata/sentiment_requirements/sentiment_req.csv')

    def save_news_impact_placeholder_requirement_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/impact_requirements/impact_req', df, summary)
    def load_news_impact_placeholder_requirement_registry(self):
        return self._load_csv('advanced_news_metadata/impact_requirements/impact_req.csv')

    def save_news_freshness_staleness_requirement_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/freshness_requirements/freshness_req', df, summary)
    def load_news_freshness_staleness_requirement_registry(self):
        return self._load_csv('advanced_news_metadata/freshness_requirements/freshness_req.csv')

    def save_news_deduplication_requirement_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/deduplication_requirements/dedup_req', df, summary)
    def load_news_deduplication_requirement_registry(self):
        return self._load_csv('advanced_news_metadata/deduplication_requirements/dedup_req.csv')

    def save_news_provider_capability_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/capabilities/cap_registry', df, summary)
    def load_news_provider_capability_registry(self):
        return self._load_csv('advanced_news_metadata/capabilities/cap_registry.csv')

    def save_news_provider_metadata_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/metadata/meta_registry', df, summary)
    def load_news_provider_metadata_registry(self):
        return self._load_csv('advanced_news_metadata/metadata/meta_registry.csv')

    def save_news_provider_request_schema(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/request_response/req_schema', df, summary)
    def load_news_provider_request_schema(self):
        return self._load_csv('advanced_news_metadata/request_response/req_schema.csv')

    def save_news_provider_response_schema(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/request_response/res_schema', df, summary)
    def load_news_provider_response_schema(self):
        return self._load_csv('advanced_news_metadata/request_response/res_schema.csv')

    def save_news_provider_error_schema(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/request_response/err_schema', df, summary)
    def load_news_provider_error_schema(self):
        return self._load_csv('advanced_news_metadata/request_response/err_schema.csv')

    def save_news_provider_interface_contract(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/contracts/interface_contract', df, summary)
    def load_news_provider_interface_contract(self):
        return self._load_csv('advanced_news_metadata/contracts/interface_contract.csv')

    def save_news_adapter_contract(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/contracts/adapter_contract', df, summary)
    def load_news_adapter_contract(self):
        return self._load_csv('advanced_news_metadata/contracts/adapter_contract.csv')

    def save_news_provider_registry(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/registry/prov_registry', df, summary)
    def load_news_provider_registry(self):
        return self._load_csv('advanced_news_metadata/registry/prov_registry.csv')

    def save_news_provider_resolver_map(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/resolver/resolver_map', df, summary)
    def load_news_provider_resolver_map(self):
        return self._load_csv('advanced_news_metadata/resolver/resolver_map.csv')

    def save_news_provider_preference_resolver_report(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/preferences/pref_resolver', df, summary)
    def load_news_provider_preference_resolver_report(self):
        return self._load_csv('advanced_news_metadata/preferences/pref_resolver.csv')

    def save_news_provider_capability_matcher_report(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/matcher/matcher_report', df, summary)
    def load_news_provider_capability_matcher_report(self):
        return self._load_csv('advanced_news_metadata/matcher/matcher_report.csv')

    def save_news_dry_run_fixture_report(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/dry_run/dry_run_report', df, summary)
    def load_news_dry_run_fixture_report(self):
        return self._load_csv('advanced_news_metadata/dry_run/dry_run_report.csv')

    def save_news_manual_file_provider_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/placeholders/manual_file', df, summary)
    def load_news_manual_file_provider_placeholder(self):
        return self._load_csv('advanced_news_metadata/placeholders/manual_file.csv')

    def save_news_local_cache_provider_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/placeholders/local_cache', df, summary)
    def load_news_local_cache_provider_placeholder(self):
        return self._load_csv('advanced_news_metadata/placeholders/local_cache.csv')

    def save_news_official_api_provider_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/placeholders/official_api', df, summary)
    def load_news_official_api_provider_placeholder(self):
        return self._load_csv('advanced_news_metadata/placeholders/official_api.csv')

    def save_news_licensed_provider_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/placeholders/licensed_prov', df, summary)
    def load_news_licensed_provider_placeholder(self):
        return self._load_csv('advanced_news_metadata/placeholders/licensed_prov.csv')

    def save_news_public_dataset_provider_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/placeholders/public_dataset', df, summary)
    def load_news_public_dataset_provider_placeholder(self):
        return self._load_csv('advanced_news_metadata/placeholders/public_dataset.csv')

    def save_news_output_validation_contract(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/output_validation/val_contract', df, summary)
    def load_news_output_validation_contract(self):
        return self._load_csv('advanced_news_metadata/output_validation/val_contract.csv')

    def save_news_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/safety/safety_boundary', df, summary)
    def load_news_safety_boundary(self):
        return self._load_csv('advanced_news_metadata/safety/safety_boundary.csv')

    def save_news_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/health/health_check', df, summary)
    def load_news_health_check(self):
        return self._load_csv('advanced_news_metadata/health/health_check.csv')

    def save_news_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/scoring/readiness_score', df, summary)
    def load_news_readiness_score_report(self):
        return self._load_csv('advanced_news_metadata/scoring/readiness_score.csv')

    def save_news_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_news_metadata/validation/val_report', df, summary)
    def load_news_validation_report(self):
        return self._load_csv('advanced_news_metadata/validation/val_report.csv')

    def save_news_quality_report(self, profile_name, quality):
        path = self.base_dir / 'advanced_news_metadata' / 'quality' / f'quality_report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(quality, f, ensure_ascii=False, indent=2)
        return path
    def load_news_quality_report(self, profile_name):
        path = self.base_dir / 'advanced_news_metadata' / 'quality' / f'quality_report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_news_metadata_report(self, profile_name, report, markdown=None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_news_metadata' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path
        
    def load_news_metadata_report(self, profile_name):
        path = self.base_dir / 'reports' / 'output' / 'advanced_news_metadata' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_news_metadata_reports(self):
        return pd.DataFrame()

    # Phase 112 Data Quality Engine DataLake Integration
    def save_data_quality_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/profiles/profile_registry', df, summary)
    def load_data_quality_profile_registry(self):
        return self._load_csv('advanced_data_quality/profiles/profile_registry.csv')

    def save_data_quality_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/domains/domain_registry', df, summary)
    def load_data_quality_domain_registry(self):
        return self._load_csv('advanced_data_quality/domains/domain_registry.csv')

    def save_quality_severity_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/severity/severity_registry', df, summary)
    def load_quality_severity_registry(self):
        return self._load_csv('advanced_data_quality/severity/severity_registry.csv')

    def save_quality_rule_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/rules/rule_registry', df, summary)
    def load_quality_rule_registry(self):
        return self._load_csv('advanced_data_quality/rules/rule_registry.csv')

    def save_schema_compliance_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/schema_compliance/rule_set', df, summary)
    def load_schema_compliance_rule_set(self):
        return self._load_csv('advanced_data_quality/schema_compliance/rule_set.csv')

    def save_missing_data_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/missing/rule_set', df, summary)
    def load_missing_data_rule_set(self):
        return self._load_csv('advanced_data_quality/missing/rule_set.csv')

    def save_stale_data_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/stale/rule_set', df, summary)
    def load_stale_data_rule_set(self):
        return self._load_csv('advanced_data_quality/stale/rule_set.csv')

    def save_duplicate_data_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/duplicates/rule_set', df, summary)
    def load_duplicate_data_rule_set(self):
        return self._load_csv('advanced_data_quality/duplicates/rule_set.csv')

    def save_outlier_placeholder_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/outliers/rule_set', df, summary)
    def load_outlier_placeholder_rule_set(self):
        return self._load_csv('advanced_data_quality/outliers/rule_set.csv')

    def save_timestamp_integrity_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/timestamps/rule_set', df, summary)
    def load_timestamp_integrity_rule_set(self):
        return self._load_csv('advanced_data_quality/timestamps/rule_set.csv')

    def save_frequency_unit_consistency_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/frequency_unit/rule_set', df, summary)
    def load_frequency_unit_consistency_rule_set(self):
        return self._load_csv('advanced_data_quality/frequency_unit/rule_set.csv')

    def save_fx_quality_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/fx/rule_set', df, summary)
    def load_fx_quality_rule_set(self):
        return self._load_csv('advanced_data_quality/fx/rule_set.csv')

    def save_commodity_quality_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/commodity/rule_set', df, summary)
    def load_commodity_quality_rule_set(self):
        return self._load_csv('advanced_data_quality/commodity/rule_set.csv')

    def save_macro_quality_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/macro/rule_set', df, summary)
    def load_macro_quality_rule_set(self):
        return self._load_csv('advanced_data_quality/macro/rule_set.csv')

    def save_calendar_quality_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/calendar/rule_set', df, summary)
    def load_calendar_quality_rule_set(self):
        return self._load_csv('advanced_data_quality/calendar/rule_set.csv')

    def save_news_metadata_quality_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/news/rule_set', df, summary)
    def load_news_metadata_quality_rule_set(self):
        return self._load_csv('advanced_data_quality/news/rule_set.csv')

    def save_provider_metadata_quality_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/provider_metadata/rule_set', df, summary)
    def load_provider_metadata_quality_rule_set(self):
        return self._load_csv('advanced_data_quality/provider_metadata/rule_set.csv')

    def save_ohlc_consistency_rule_contract(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/consistency/ohlc_contract', df, summary)
    def load_ohlc_consistency_rule_contract(self):
        return self._load_csv('advanced_data_quality/consistency/ohlc_contract.csv')

    def save_quote_consistency_rule_contract(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/consistency/quote_contract', df, summary)
    def load_quote_consistency_rule_contract(self):
        return self._load_csv('advanced_data_quality/consistency/quote_contract.csv')

    def save_event_release_consistency_rule_contract(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/consistency/event_contract', df, summary)
    def load_event_release_consistency_rule_contract(self):
        return self._load_csv('advanced_data_quality/consistency/event_contract.csv')

    def save_news_metadata_copyright_quality_rule_set(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/news/copyright_rule_set', df, summary)
    def load_news_metadata_copyright_quality_rule_set(self):
        return self._load_csv('advanced_data_quality/news/copyright_rule_set.csv')

    def save_quality_finding_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/findings/finding_registry', df, summary)
    def load_quality_finding_registry(self):
        return self._load_csv('advanced_data_quality/findings/finding_registry.csv')

    def save_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/manual_review/review_queue', df, summary)
    def load_manual_review_queue(self):
        return self._load_csv('advanced_data_quality/manual_review/review_queue.csv')

    def save_provider_quality_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/scoring/provider_scores', df, summary)
    def load_provider_quality_score_report(self):
        return self._load_csv('advanced_data_quality/scoring/provider_scores.csv')

    def save_dataset_quality_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/scoring/dataset_scores', df, summary)
    def load_dataset_quality_score_report(self):
        return self._load_csv('advanced_data_quality/scoring/dataset_scores.csv')

    def save_cross_provider_quality_comparison_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/cross_provider/comparison', df, summary)
    def load_cross_provider_quality_comparison_placeholder(self):
        return self._load_csv('advanced_data_quality/cross_provider/comparison.csv')

    def save_data_quality_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/health/health_check', df, summary)
    def load_data_quality_health_check(self):
        return self._load_csv('advanced_data_quality/health/health_check.csv')

    def save_data_quality_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/validation/validation_report', df, summary)
    def load_data_quality_validation_report(self):
        return self._load_csv('advanced_data_quality/validation/validation_report.csv')

    def save_data_quality_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/safety/safety_boundary', df, summary)
    def load_data_quality_safety_boundary(self):
        return self._load_csv('advanced_data_quality/safety/safety_boundary.csv')

    def save_phase_113_normalization_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_quality/handoff/phase_113_handoff', df, summary)
    def load_phase_113_normalization_handoff_report(self):
        return self._load_csv('advanced_data_quality/handoff/phase_113_handoff.csv')

    def save_data_quality_report(self, profile_name, report, markdown=None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_data_quality' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_data_quality_report(self, profile_name):
        path = self.base_dir / 'reports' / 'output' / 'advanced_data_quality' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_data_quality_reports(self):
        return pd.DataFrame()

    # Phase 113 Data Normalization Layer
    def save_data_normalization_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/profiles/profile_registry', df, summary)
    def load_data_normalization_profile_registry(self):
        return self._load_csv('advanced_data_normalization/profiles/profile_registry.csv')

    def save_data_normalization_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/domains/domain_registry', df, summary)
    def load_data_normalization_domain_registry(self):
        return self._load_csv('advanced_data_normalization/domains/domain_registry.csv')

    def save_normalization_status_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/status/status_registry', df, summary)
    def load_normalization_status_registry(self):
        return self._load_csv('advanced_data_normalization/status/status_registry.csv')

    def save_normalization_rule_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/rules/rule_registry', df, summary)
    def load_normalization_rule_registry(self):
        return self._load_csv('advanced_data_normalization/rules/rule_registry.csv')

    def save_canonical_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/canonical_schema/canonical_schema_registry', df, summary)
    def load_canonical_schema_registry(self):
        return self._load_csv('advanced_data_normalization/canonical_schema/canonical_schema_registry.csv')

    def save_canonical_field_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/canonical_fields/canonical_field_registry', df, summary)
    def load_canonical_field_registry(self):
        return self._load_csv('advanced_data_normalization/canonical_fields/canonical_field_registry.csv')

    def save_schema_version_normalization_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/schema_version/schema_version_registry', df, summary)
    def load_schema_version_normalization_registry(self):
        return self._load_csv('advanced_data_normalization/schema_version/schema_version_registry.csv')

    def save_provider_name_normalization_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/provider_names/provider_name_registry', df, summary)
    def load_provider_name_normalization_registry(self):
        return self._load_csv('advanced_data_normalization/provider_names/provider_name_registry.csv')

    def save_fx_symbol_normalization_enforcement_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/symbols/fx_symbol_report', df, summary)
    def load_fx_symbol_normalization_enforcement_report(self):
        return self._load_csv('advanced_data_normalization/symbols/fx_symbol_report.csv')

    def save_commodity_symbol_normalization_enforcement_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/symbols/commodity_symbol_report', df, summary)
    def load_commodity_symbol_normalization_enforcement_report(self):
        return self._load_csv('advanced_data_normalization/symbols/commodity_symbol_report.csv')

    def save_macro_indicator_normalization_enforcement_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/symbols/macro_indicator_report', df, summary)
    def load_macro_indicator_normalization_enforcement_report(self):
        return self._load_csv('advanced_data_normalization/symbols/macro_indicator_report.csv')

    def save_calendar_event_normalization_enforcement_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/symbols/calendar_event_report', df, summary)
    def load_calendar_event_normalization_enforcement_report(self):
        return self._load_csv('advanced_data_normalization/symbols/calendar_event_report.csv')

    def save_news_topic_tag_normalization_enforcement_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/symbols/news_topic_tag_report', df, summary)
    def load_news_topic_tag_normalization_enforcement_report(self):
        return self._load_csv('advanced_data_normalization/symbols/news_topic_tag_report.csv')

    def save_region_country_currency_normalization_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/regions/region_currency_registry', df, summary)
    def load_region_country_currency_normalization_registry(self):
        return self._load_csv('advanced_data_normalization/regions/region_currency_registry.csv')

    def save_timestamp_timezone_normalization_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/timestamps/timestamp_timezone_registry', df, summary)
    def load_timestamp_timezone_normalization_registry(self):
        return self._load_csv('advanced_data_normalization/timestamps/timestamp_timezone_registry.csv')

    def save_session_alignment_requirement_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/sessions/session_alignment_registry', df, summary)
    def load_session_alignment_requirement_registry(self):
        return self._load_csv('advanced_data_normalization/sessions/session_alignment_registry.csv')

    def save_frequency_normalization_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/frequency/frequency_registry', df, summary)
    def load_frequency_normalization_registry(self):
        return self._load_csv('advanced_data_normalization/frequency/frequency_registry.csv')

    def save_unit_normalization_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/units/unit_registry', df, summary)
    def load_unit_normalization_registry(self):
        return self._load_csv('advanced_data_normalization/units/unit_registry.csv')

    def save_numeric_type_normalization_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/numeric_types/numeric_type_registry', df, summary)
    def load_numeric_type_normalization_registry(self):
        return self._load_csv('advanced_data_normalization/numeric_types/numeric_type_registry.csv')

    def save_string_case_slug_normalization_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/string_slug/string_slug_registry', df, summary)
    def load_string_case_slug_normalization_registry(self):
        return self._load_csv('advanced_data_normalization/string_slug/string_slug_registry.csv')

    def save_duplicate_key_normalization_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/duplicate_keys/duplicate_key_registry', df, summary)
    def load_duplicate_key_normalization_registry(self):
        return self._load_csv('advanced_data_normalization/duplicate_keys/duplicate_key_registry.csv')

    def save_normalized_view_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/normalized_views/normalized_view_registry', df, summary)
    def load_normalized_view_registry(self):
        return self._load_csv('advanced_data_normalization/normalized_views/normalized_view_registry.csv')

    def save_normalization_finding_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/findings/finding_registry', df, summary)
    def load_normalization_finding_registry(self):
        return self._load_csv('advanced_data_normalization/findings/finding_registry.csv')

    def save_normalization_decision_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/decisions/decision_registry', df, summary)
    def load_normalization_decision_registry(self):
        return self._load_csv('advanced_data_normalization/decisions/decision_registry.csv')

    def save_manual_review_normalization_queue(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/manual_review/review_queue', df, summary)
    def load_manual_review_normalization_queue(self):
        return self._load_csv('advanced_data_normalization/manual_review/review_queue.csv')

    def save_normalized_output_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/output_manifest/output_manifest', df, summary)
    def load_normalized_output_manifest(self):
        return self._load_csv('advanced_data_normalization/output_manifest/output_manifest.csv')

    def save_normalization_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/scoring/normalization_scores', df, summary)
    def load_normalization_score_report(self):
        return self._load_csv('advanced_data_normalization/scoring/normalization_scores.csv')

    def save_cross_domain_normalized_mapping_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/cross_domain/cross_domain_mapping', df, summary)
    def load_cross_domain_normalized_mapping_report(self):
        return self._load_csv('advanced_data_normalization/cross_domain/cross_domain_mapping.csv')

    def save_data_normalization_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/health/health_check', df, summary)
    def load_data_normalization_health_check(self):
        return self._load_csv('advanced_data_normalization/health/health_check.csv')

    def save_data_normalization_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/validation/validation_report', df, summary)
    def load_data_normalization_validation_report(self):
        return self._load_csv('advanced_data_normalization/validation/validation_report.csv')

    def save_data_normalization_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/safety/safety_boundary', df, summary)
    def load_data_normalization_safety_boundary(self):
        return self._load_csv('advanced_data_normalization/safety/safety_boundary.csv')

    def save_phase_114_lineage_provenance_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_normalization/handoff/phase_114_handoff', df, summary)
    def load_phase_114_lineage_provenance_handoff_report(self):
        return self._load_csv('advanced_data_normalization/handoff/phase_114_handoff.csv')

    def save_data_normalization_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_data_normalization' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_data_normalization_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_data_normalization' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_data_normalization_reports(self):
        return pd.DataFrame()

    # Phase 114 Data Lineage and Provenance methods
    def save_data_lineage_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/profiles/profile_registry', df, summary)
    def load_data_lineage_profile_registry(self):
        return self._load_csv('advanced_data_lineage/profiles/profile_registry.csv')

    def save_data_lineage_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/domains/domain_registry', df, summary)
    def load_data_lineage_domain_registry(self):
        return self._load_csv('advanced_data_lineage/domains/domain_registry.csv')

    def save_provenance_source_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/sources/source_registry', df, summary)
    def load_provenance_source_registry(self):
        return self._load_csv('advanced_data_lineage/sources/source_registry.csv')

    def save_source_reference_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/source_references/source_reference_registry', df, summary)
    def load_source_reference_registry(self):
        return self._load_csv('advanced_data_lineage/source_references/source_reference_registry.csv')

    def save_provider_provenance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/provider_provenance/provider_provenance_registry', df, summary)
    def load_provider_provenance_registry(self):
        return self._load_csv('advanced_data_lineage/provider_provenance/provider_provenance_registry.csv')

    def save_dataset_provenance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/dataset_provenance/dataset_provenance_registry', df, summary)
    def load_dataset_provenance_registry(self):
        return self._load_csv('advanced_data_lineage/dataset_provenance/dataset_provenance_registry.csv')

    def save_schema_provenance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/schema_provenance/schema_provenance_registry', df, summary)
    def load_schema_provenance_registry(self):
        return self._load_csv('advanced_data_lineage/schema_provenance/schema_provenance_registry.csv')

    def save_transformation_provenance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/transformation_provenance/transformation_provenance_registry', df, summary)
    def load_transformation_provenance_registry(self):
        return self._load_csv('advanced_data_lineage/transformation_provenance/transformation_provenance_registry.csv')

    def save_normalization_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/normalization_lineage/normalization_lineage_registry', df, summary)
    def load_normalization_lineage_registry(self):
        return self._load_csv('advanced_data_lineage/normalization_lineage/normalization_lineage_registry.csv')

    def save_quality_finding_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/quality_lineage/quality_finding_lineage_registry', df, summary)
    def load_quality_finding_lineage_registry(self):
        return self._load_csv('advanced_data_lineage/quality_lineage/quality_finding_lineage_registry.csv')

    def save_manual_review_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/manual_review_lineage/manual_review_lineage_registry', df, summary)
    def load_manual_review_lineage_registry(self):
        return self._load_csv('advanced_data_lineage/manual_review_lineage/manual_review_lineage_registry.csv')

    def save_normalized_output_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/normalized_output_lineage/normalized_output_lineage_registry', df, summary)
    def load_normalized_output_lineage_registry(self):
        return self._load_csv('advanced_data_lineage/normalized_output_lineage/normalized_output_lineage_registry.csv')

    def save_fx_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/domain_lineage/fx_lineage_registry', df, summary)
    def load_fx_lineage_registry(self):
        return self._load_csv('advanced_data_lineage/domain_lineage/fx_lineage_registry.csv')

    def save_commodity_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/domain_lineage/commodity_lineage_registry', df, summary)
    def load_commodity_lineage_registry(self):
        return self._load_csv('advanced_data_lineage/domain_lineage/commodity_lineage_registry.csv')

    def save_macro_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/domain_lineage/macro_lineage_registry', df, summary)
    def load_macro_lineage_registry(self):
        return self._load_csv('advanced_data_lineage/domain_lineage/macro_lineage_registry.csv')

    def save_calendar_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/domain_lineage/calendar_lineage_registry', df, summary)
    def load_calendar_lineage_registry(self):
        return self._load_csv('advanced_data_lineage/domain_lineage/calendar_lineage_registry.csv')

    def save_news_metadata_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/domain_lineage/news_metadata_lineage_registry', df, summary)
    def load_news_metadata_lineage_registry(self):
        return self._load_csv('advanced_data_lineage/domain_lineage/news_metadata_lineage_registry.csv')

    def save_license_provenance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/license_provenance/license_provenance_registry', df, summary)
    def load_license_provenance_registry(self):
        return self._load_csv('advanced_data_lineage/license_provenance/license_provenance_registry.csv')

    def save_copyright_boundary_provenance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/copyright_boundary/copyright_boundary_registry', df, summary)
    def load_copyright_boundary_provenance_registry(self):
        return self._load_csv('advanced_data_lineage/copyright_boundary/copyright_boundary_registry.csv')

    def save_metadata_only_provenance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/metadata_only/metadata_only_registry', df, summary)
    def load_metadata_only_provenance_registry(self):
        return self._load_csv('advanced_data_lineage/metadata_only/metadata_only_registry.csv')

    def save_data_usage_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/usage_boundary/usage_boundary_registry', df, summary)
    def load_data_usage_boundary_registry(self):
        return self._load_csv('advanced_data_lineage/usage_boundary/usage_boundary_registry.csv')

    def save_audit_trail_event_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/audit_trail/audit_trail_event_registry', df, summary)
    def load_audit_trail_event_registry(self):
        return self._load_csv('advanced_data_lineage/audit_trail/audit_trail_event_registry.csv')

    def save_transformation_audit_trail_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/audit_trail/transformation_audit_trail_registry', df, summary)
    def load_transformation_audit_trail_registry(self):
        return self._load_csv('advanced_data_lineage/audit_trail/transformation_audit_trail_registry.csv')

    def save_lineage_finding_registry(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/findings/lineage_finding_registry', df, summary)
    def load_lineage_finding_registry(self):
        return self._load_csv('advanced_data_lineage/findings/lineage_finding_registry.csv')

    def save_provenance_confidence_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/scoring/provenance_confidence_scores', df, summary)
    def load_provenance_confidence_score_report(self):
        return self._load_csv('advanced_data_lineage/scoring/provenance_confidence_scores.csv')

    def save_dataset_traceability_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/scoring/dataset_traceability_scores', df, summary)
    def load_dataset_traceability_score_report(self):
        return self._load_csv('advanced_data_lineage/scoring/dataset_traceability_scores.csv')

    def save_provider_traceability_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/scoring/provider_traceability_scores', df, summary)
    def load_provider_traceability_score_report(self):
        return self._load_csv('advanced_data_lineage/scoring/provider_traceability_scores.csv')

    def save_lineage_graph_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/lineage_graph/lineage_graph_placeholder', df, summary)
    def load_lineage_graph_placeholder(self):
        return self._load_csv('advanced_data_lineage/lineage_graph/lineage_graph_placeholder.csv')

    def save_cross_domain_provenance_map(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/cross_domain/cross_domain_provenance_map', df, summary)
    def load_cross_domain_provenance_map(self):
        return self._load_csv('advanced_data_lineage/cross_domain/cross_domain_provenance_map.csv')

    def save_data_lineage_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/health/health_check', df, summary)
    def load_data_lineage_health_check(self):
        return self._load_csv('advanced_data_lineage/health/health_check.csv')

    def save_data_lineage_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/validation/validation_report', df, summary)
    def load_data_lineage_validation_report(self):
        return self._load_csv('advanced_data_lineage/validation/validation_report.csv')

    def save_data_lineage_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/safety/safety_boundary', df, summary)
    def load_data_lineage_safety_boundary(self):
        return self._load_csv('advanced_data_lineage/safety/safety_boundary.csv')

    def save_phase_115_provider_benchmark_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_data_lineage/handoff/phase_115_handoff', df, summary)
    def load_phase_115_provider_benchmark_handoff_report(self):
        return self._load_csv('advanced_data_lineage/handoff/phase_115_handoff.csv')

    def save_data_lineage_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_data_lineage' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_data_lineage_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_data_lineage' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_data_lineage_reports(self):
        return pd.DataFrame()

    # Phase 115 Data Provider Benchmark Report DataLake Support
    def save_provider_benchmark_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/profiles/profile_registry', df, summary)
    def load_provider_benchmark_profile_registry(self):
        return self._load_csv('advanced_provider_benchmark/profiles/profile_registry.csv')

    def save_provider_benchmark_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/domains/domain_registry', df, summary)
    def load_provider_benchmark_domain_registry(self):
        return self._load_csv('advanced_provider_benchmark/domains/domain_registry.csv')

    def save_provider_benchmark_metric_registry(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/metrics/metric_registry', df, summary)
    def load_provider_benchmark_metric_registry(self):
        return self._load_csv('advanced_provider_benchmark/metrics/metric_registry.csv')

    def save_provider_benchmark_weight_registry(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/weights/weight_registry', df, summary)
    def load_provider_benchmark_weight_registry(self):
        return self._load_csv('advanced_provider_benchmark/weights/weight_registry.csv')

    def save_provider_coverage_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/coverage/coverage_report', df, summary)
    def load_provider_coverage_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/coverage/coverage_report.csv')

    def save_provider_capability_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/capability/capability_report', df, summary)
    def load_provider_capability_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/capability/capability_report.csv')

    def save_provider_quality_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/quality/quality_report', df, summary)
    def load_provider_quality_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/quality/quality_report.csv')

    def save_provider_normalization_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/normalization/normalization_report', df, summary)
    def load_provider_normalization_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/normalization/normalization_report.csv')

    def save_provider_traceability_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/traceability/traceability_report', df, summary)
    def load_provider_traceability_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/traceability/traceability_report.csv')

    def save_provider_license_provenance_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/license_provenance/license_report', df, summary)
    def load_provider_license_provenance_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/license_provenance/license_report.csv')

    def save_provider_no_scraping_compliance_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/no_scraping/no_scraping_report', df, summary)
    def load_provider_no_scraping_compliance_report(self):
        return self._load_csv('advanced_provider_benchmark/no_scraping/no_scraping_report.csv')

    def save_provider_metadata_only_compliance_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/metadata_only/metadata_only_report', df, summary)
    def load_provider_metadata_only_compliance_report(self):
        return self._load_csv('advanced_provider_benchmark/metadata_only/metadata_only_report.csv')

    def save_provider_manual_review_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/manual_review/manual_review_report', df, summary)
    def load_provider_manual_review_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/manual_review/manual_review_report.csv')

    def save_fx_provider_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/domain_benchmarks/fx_benchmark_report', df, summary)
    def load_fx_provider_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/domain_benchmarks/fx_benchmark_report.csv')

    def save_commodity_provider_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/domain_benchmarks/commodity_benchmark_report', df, summary)
    def load_commodity_provider_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/domain_benchmarks/commodity_benchmark_report.csv')

    def save_macro_provider_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/domain_benchmarks/macro_benchmark_report', df, summary)
    def load_macro_provider_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/domain_benchmarks/macro_benchmark_report.csv')

    def save_calendar_provider_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/domain_benchmarks/calendar_benchmark_report', df, summary)
    def load_calendar_provider_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/domain_benchmarks/calendar_benchmark_report.csv')

    def save_news_metadata_provider_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/domain_benchmarks/news_metadata_benchmark_report', df, summary)
    def load_news_metadata_provider_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/domain_benchmarks/news_metadata_benchmark_report.csv')

    def save_cross_domain_provider_benchmark_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/cross_domain/cross_domain_report', df, summary)
    def load_cross_domain_provider_benchmark_report(self):
        return self._load_csv('advanced_provider_benchmark/cross_domain/cross_domain_report.csv')

    def save_provider_benchmark_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/scoring/score_report', df, summary)
    def load_provider_benchmark_score_report(self):
        return self._load_csv('advanced_provider_benchmark/scoring/score_report.csv')

    def save_provider_ranking_research_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/ranking/ranking_report', df, summary)
    def load_provider_ranking_research_report(self):
        return self._load_csv('advanced_provider_benchmark/ranking/ranking_report.csv')

    def save_provider_benchmark_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/findings/findings_registry', df, summary)
    def load_provider_benchmark_findings_registry(self):
        return self._load_csv('advanced_provider_benchmark/findings/findings_registry.csv')

    def save_provider_benchmark_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/manual_review_queue/manual_review_queue', df, summary)
    def load_provider_benchmark_manual_review_queue(self):
        return self._load_csv('advanced_provider_benchmark/manual_review_queue/manual_review_queue.csv')

    def save_provider_benchmark_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/health/health_check', df, summary)
    def load_provider_benchmark_health_check(self):
        return self._load_csv('advanced_provider_benchmark/health/health_check.csv')

    def save_provider_benchmark_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/validation/validation_report', df, summary)
    def load_provider_benchmark_validation_report(self):
        return self._load_csv('advanced_provider_benchmark/validation/validation_report.csv')

    def save_provider_benchmark_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/safety/safety_boundary', df, summary)
    def load_provider_benchmark_safety_boundary(self):
        return self._load_csv('advanced_provider_benchmark/safety/safety_boundary.csv')

    def save_phase_116_indicator_feature_factor_engine_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_provider_benchmark/handoff/phase_116_handoff', df, summary)
    def load_phase_116_indicator_feature_factor_engine_handoff_report(self):
        return self._load_csv('advanced_provider_benchmark/handoff/phase_116_handoff.csv')

    def save_provider_benchmark_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_provider_benchmark' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_provider_benchmark_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_provider_benchmark' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_provider_benchmark_reports(self):
        return pd.DataFrame()

    # Phase 116 Advanced Indicator/Feature/Factor Engine Foundation DataLake support
    def save_feature_engine_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/profiles/feature_engine_profile_registry', df, summary)
    def load_feature_engine_profile_registry(self):
        return self._load_csv('advanced_feature_engine/profiles/feature_engine_profile_registry.csv')

    def save_feature_engine_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/domains/feature_engine_domain_registry', df, summary)
    def load_feature_engine_domain_registry(self):
        return self._load_csv('advanced_feature_engine/domains/feature_engine_domain_registry.csv')

    def save_feature_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/input_contracts/feature_input_contract_registry', df, summary)
    def load_feature_input_contract_registry(self):
        return self._load_csv('advanced_feature_engine/input_contracts/feature_input_contract_registry.csv')

    def save_feature_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/schemas/feature_schema_registry', df, summary)
    def load_feature_schema_registry(self):
        return self._load_csv('advanced_feature_engine/schemas/feature_schema_registry.csv')

    def save_factor_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/factors/factor_schema_registry', df, summary)
    def load_factor_schema_registry(self):
        return self._load_csv('advanced_feature_engine/factors/factor_schema_registry.csv')

    def save_indicator_catalog_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/catalogs/indicator_catalog_registry', df, summary)
    def load_indicator_catalog_registry(self):
        return self._load_csv('advanced_feature_engine/catalogs/indicator_catalog_registry.csv')

    def save_price_indicator_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/price/price_indicator_catalog', df, summary)
    def load_price_indicator_catalog(self):
        return self._load_csv('advanced_feature_engine/price/price_indicator_catalog.csv')

    def save_trend_indicator_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/trend/trend_indicator_catalog', df, summary)
    def load_trend_indicator_catalog(self):
        return self._load_csv('advanced_feature_engine/trend/trend_indicator_catalog.csv')

    def save_momentum_indicator_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/momentum/momentum_indicator_catalog', df, summary)
    def load_momentum_indicator_catalog(self):
        return self._load_csv('advanced_feature_engine/momentum/momentum_indicator_catalog.csv')

    def save_volatility_indicator_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/volatility/volatility_indicator_catalog', df, summary)
    def load_volatility_indicator_catalog(self):
        return self._load_csv('advanced_feature_engine/volatility/volatility_indicator_catalog.csv')

    def save_mean_reversion_indicator_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/mean_reversion/mean_reversion_indicator_catalog', df, summary)
    def load_mean_reversion_indicator_catalog(self):
        return self._load_csv('advanced_feature_engine/mean_reversion/mean_reversion_indicator_catalog.csv')

    def save_quote_feature_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/quote/quote_feature_catalog', df, summary)
    def load_quote_feature_catalog(self):
        return self._load_csv('advanced_feature_engine/quote/quote_feature_catalog.csv')

    def save_volume_liquidity_feature_placeholder_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/volume_liquidity/volume_liquidity_placeholder_catalog', df, summary)
    def load_volume_liquidity_feature_placeholder_catalog(self):
        return self._load_csv('advanced_feature_engine/volume_liquidity/volume_liquidity_placeholder_catalog.csv')

    def save_macro_feature_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/macro/macro_feature_catalog', df, summary)
    def load_macro_feature_catalog(self):
        return self._load_csv('advanced_feature_engine/macro/macro_feature_catalog.csv')

    def save_calendar_event_feature_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/calendar/calendar_event_feature_catalog', df, summary)
    def load_calendar_event_feature_catalog(self):
        return self._load_csv('advanced_feature_engine/calendar/calendar_event_feature_catalog.csv')

    def save_news_metadata_feature_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/news/news_metadata_feature_catalog', df, summary)
    def load_news_metadata_feature_catalog(self):
        return self._load_csv('advanced_feature_engine/news/news_metadata_feature_catalog.csv')

    def save_feature_metadata_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/metadata/feature_metadata_registry', df, summary)
    def load_feature_metadata_registry(self):
        return self._load_csv('advanced_feature_engine/metadata/feature_metadata_registry.csv')

    def save_factor_metadata_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/metadata/factor_metadata_registry', df, summary)
    def load_factor_metadata_registry(self):
        return self._load_csv('advanced_feature_engine/metadata/factor_metadata_registry.csv')

    def save_rolling_window_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/rolling_windows/rolling_window_contract_registry', df, summary)
    def load_rolling_window_contract_registry(self):
        return self._load_csv('advanced_feature_engine/rolling_windows/rolling_window_contract_registry.csv')

    def save_feature_computation_interface_contract(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/computation/feature_computation_contract', df, summary)
    def load_feature_computation_interface_contract(self):
        return self._load_csv('advanced_feature_engine/computation/feature_computation_contract.csv')

    def save_feature_dependency_graph_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/dependencies/feature_dependency_graph', df, summary)
    def load_feature_dependency_graph_placeholder(self):
        return self._load_csv('advanced_feature_engine/dependencies/feature_dependency_graph.csv')

    def save_feature_validation_rule_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/validation/feature_validation_rule_registry', df, summary)
    def load_feature_validation_rule_registry(self):
        return self._load_csv('advanced_feature_engine/validation/feature_validation_rule_registry.csv')

    def save_feature_quality_handoff_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/quality_handoff/feature_quality_handoff_registry', df, summary)
    def load_feature_quality_handoff_registry(self):
        return self._load_csv('advanced_feature_engine/quality_handoff/feature_quality_handoff_registry.csv')

    def save_feature_engine_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/health/health_check', df, summary)
    def load_feature_engine_health_check(self):
        return self._load_csv('advanced_feature_engine/health/health_check.csv')

    def save_feature_engine_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/validation/validation_report', df, summary)
    def load_feature_engine_validation_report(self):
        return self._load_csv('advanced_feature_engine/validation/validation_report.csv')

    def save_feature_engine_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/safety/safety_boundary', df, summary)
    def load_feature_engine_safety_boundary(self):
        return self._load_csv('advanced_feature_engine/safety/safety_boundary.csv')

    def save_phase_117_technical_indicator_expansion_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_engine/handoff/phase_117_handoff_report', df, summary)
    def load_phase_117_technical_indicator_expansion_handoff_report(self):
        return self._load_csv('advanced_feature_engine/handoff/phase_117_handoff_report.csv')

    def save_feature_engine_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_engine' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_feature_engine_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_engine' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_feature_engine_reports(self):
        return pd.DataFrame()

    # Phase 117 Technical Indicator Expansion DataLake Support
    def save_technical_indicator_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/profiles/profile_registry', df, summary)
    def load_technical_indicator_profile_registry(self):
        return self._load_csv('advanced_technical_indicators/profiles/profile_registry.csv')

    def save_technical_indicator_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/domains/domain_registry', df, summary)
    def load_technical_indicator_domain_registry(self):
        return self._load_csv('advanced_technical_indicators/domains/domain_registry.csv')

    def save_technical_indicator_catalog_expansion(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/catalogs/catalog_expansion', df, summary)
    def load_technical_indicator_catalog_expansion(self):
        return self._load_csv('advanced_technical_indicators/catalogs/catalog_expansion.csv')

    def save_price_action_indicator_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/price_action/price_action_registry', df, summary)
    def load_price_action_indicator_registry(self):
        return self._load_csv('advanced_technical_indicators/price_action/price_action_registry.csv')

    def save_return_indicator_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/returns/return_registry', df, summary)
    def load_return_indicator_registry(self):
        return self._load_csv('advanced_technical_indicators/returns/return_registry.csv')

    def save_moving_average_indicator_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/moving_averages/moving_average_registry', df, summary)
    def load_moving_average_indicator_registry(self):
        return self._load_csv('advanced_technical_indicators/moving_averages/moving_average_registry.csv')

    def save_trend_indicator_expansion_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/trend/trend_registry', df, summary)
    def load_trend_indicator_expansion_registry(self):
        return self._load_csv('advanced_technical_indicators/trend/trend_registry.csv')

    def save_momentum_indicator_expansion_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/momentum/momentum_registry', df, summary)
    def load_momentum_indicator_expansion_registry(self):
        return self._load_csv('advanced_technical_indicators/momentum/momentum_registry.csv')

    def save_oscillator_indicator_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/oscillators/oscillator_registry', df, summary)
    def load_oscillator_indicator_registry(self):
        return self._load_csv('advanced_technical_indicators/oscillators/oscillator_registry.csv')

    def save_volatility_indicator_expansion_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/volatility/volatility_registry', df, summary)
    def load_volatility_indicator_expansion_registry(self):
        return self._load_csv('advanced_technical_indicators/volatility/volatility_registry.csv')

    def save_range_indicator_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/range/range_registry', df, summary)
    def load_range_indicator_registry(self):
        return self._load_csv('advanced_technical_indicators/range/range_registry.csv')

    def save_channel_indicator_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/channels/channel_registry', df, summary)
    def load_channel_indicator_registry(self):
        return self._load_csv('advanced_technical_indicators/channels/channel_registry.csv')

    def save_candle_anatomy_feature_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/candles/candle_registry', df, summary)
    def load_candle_anatomy_feature_registry(self):
        return self._load_csv('advanced_technical_indicators/candles/candle_registry.csv')

    def save_quote_microstructure_feature_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/quote_microstructure/quote_registry', df, summary)
    def load_quote_microstructure_feature_registry(self):
        return self._load_csv('advanced_technical_indicators/quote_microstructure/quote_registry.csv')

    def save_mean_reversion_indicator_expansion_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/mean_reversion/mean_reversion_registry', df, summary)
    def load_mean_reversion_indicator_expansion_registry(self):
        return self._load_csv('advanced_technical_indicators/mean_reversion/mean_reversion_registry.csv')

    def save_indicator_parameter_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/parameters/parameter_registry', df, summary)
    def load_indicator_parameter_contract_registry(self):
        return self._load_csv('advanced_technical_indicators/parameters/parameter_registry.csv')

    def save_indicator_output_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/output_schema/output_schema_registry', df, summary)
    def load_indicator_output_schema_registry(self):
        return self._load_csv('advanced_technical_indicators/output_schema/output_schema_registry.csv')

    def save_indicator_warmup_nan_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/warmup_nan/warmup_nan_registry', df, summary)
    def load_indicator_warmup_nan_policy_registry(self):
        return self._load_csv('advanced_technical_indicators/warmup_nan/warmup_nan_registry.csv')

    def save_no_lookahead_indicator_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/no_lookahead/no_lookahead_registry', df, summary)
    def load_no_lookahead_indicator_guard_registry(self):
        return self._load_csv('advanced_technical_indicators/no_lookahead/no_lookahead_registry.csv')

    def save_indicator_computation_interface_contract(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/computation/computation_interface_contract', df, summary)
    def load_indicator_computation_interface_contract(self):
        return self._load_csv('advanced_technical_indicators/computation/computation_interface_contract.csv')

    def save_indicator_computation_rehearsal_report(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/computation/rehearsal_report', df, summary)
    def load_indicator_computation_rehearsal_report(self):
        return self._load_csv('advanced_technical_indicators/computation/rehearsal_report.csv')

    def save_indicator_validation_rule_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/validation/validation_rule_registry', df, summary)
    def load_indicator_validation_rule_registry(self):
        return self._load_csv('advanced_technical_indicators/validation/validation_rule_registry.csv')

    def save_indicator_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/dependencies/dependency_registry', df, summary)
    def load_indicator_dependency_registry(self):
        return self._load_csv('advanced_technical_indicators/dependencies/dependency_registry.csv')

    def save_indicator_quality_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/quality_handoff/quality_handoff_report', df, summary)
    def load_indicator_quality_handoff_report(self):
        return self._load_csv('advanced_technical_indicators/quality_handoff/quality_handoff_report.csv')

    def save_technical_indicator_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/health/health_check', df, summary)
    def load_technical_indicator_health_check(self):
        return self._load_csv('advanced_technical_indicators/health/health_check.csv')

    def save_technical_indicator_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/validation/validation_report', df, summary)
    def load_technical_indicator_validation_report(self):
        return self._load_csv('advanced_technical_indicators/validation/validation_report.csv')

    def save_technical_indicator_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/safety/safety_boundary', df, summary)
    def load_technical_indicator_safety_boundary(self):
        return self._load_csv('advanced_technical_indicators/safety/safety_boundary.csv')

    def save_phase_118_multi_window_feature_grid_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_technical_indicators/handoff/phase_118_handoff_report', df, summary)
    def load_phase_118_multi_window_feature_grid_handoff_report(self):
        return self._load_csv('advanced_technical_indicators/handoff/phase_118_handoff_report.csv')

    def save_technical_indicator_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_technical_indicators' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_technical_indicator_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_technical_indicators' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_technical_indicator_reports(self):
        return pd.DataFrame()

    # Phase 118 Multi-Window Feature Grid Methods
    def save_feature_grid_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/profiles/profile_registry', df, summary)
    def load_feature_grid_profile_registry(self):
        return self._load_csv('advanced_feature_grid/profiles/profile_registry.csv')

    def save_feature_grid_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/domains/domain_registry', df, summary)
    def load_feature_grid_domain_registry(self):
        return self._load_csv('advanced_feature_grid/domains/domain_registry.csv')

    def save_window_grid_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/window_contracts/window_grid_contract_registry', df, summary)
    def load_window_grid_contract_registry(self):
        return self._load_csv('advanced_feature_grid/window_contracts/window_grid_contract_registry.csv')

    def save_indicator_parameter_grid_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/parameter_grids/parameter_grid_registry', df, summary)
    def load_indicator_parameter_grid_registry(self):
        return self._load_csv('advanced_feature_grid/parameter_grids/parameter_grid_registry.csv')

    def save_feature_grid_naming_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/naming/naming_registry', df, summary)
    def load_feature_grid_naming_registry(self):
        return self._load_csv('advanced_feature_grid/naming/naming_registry.csv')

    def save_feature_grid_output_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/output_schema/output_schema_registry', df, summary)
    def load_feature_grid_output_schema_registry(self):
        return self._load_csv('advanced_feature_grid/output_schema/output_schema_registry.csv')

    def save_feature_grid_warmup_nan_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/warmup_nan/warmup_nan_registry', df, summary)
    def load_feature_grid_warmup_nan_policy_registry(self):
        return self._load_csv('advanced_feature_grid/warmup_nan/warmup_nan_registry.csv')

    def save_feature_grid_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/no_lookahead/no_lookahead_registry', df, summary)
    def load_feature_grid_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_feature_grid/no_lookahead/no_lookahead_registry.csv')

    def save_feature_grid_duplicate_detection_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/duplicates/duplicate_registry', df, summary)
    def load_feature_grid_duplicate_detection_registry(self):
        return self._load_csv('advanced_feature_grid/duplicates/duplicate_registry.csv')

    def save_moving_average_window_grid_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/moving_average/moving_average_grid_registry', df, summary)
    def load_moving_average_window_grid_registry(self):
        return self._load_csv('advanced_feature_grid/moving_average/moving_average_grid_registry.csv')

    def save_momentum_window_grid_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/momentum/momentum_grid_registry', df, summary)
    def load_momentum_window_grid_registry(self):
        return self._load_csv('advanced_feature_grid/momentum/momentum_grid_registry.csv')

    def save_volatility_window_grid_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/volatility/volatility_grid_registry', df, summary)
    def load_volatility_window_grid_registry(self):
        return self._load_csv('advanced_feature_grid/volatility/volatility_grid_registry.csv')

    def save_range_channel_window_grid_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/range_channel/range_channel_grid_registry', df, summary)
    def load_range_channel_window_grid_registry(self):
        return self._load_csv('advanced_feature_grid/range_channel/range_channel_grid_registry.csv')

    def save_mean_reversion_window_grid_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/mean_reversion/mean_reversion_grid_registry', df, summary)
    def load_mean_reversion_window_grid_registry(self):
        return self._load_csv('advanced_feature_grid/mean_reversion/mean_reversion_grid_registry.csv')

    def save_return_window_grid_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/returns/return_grid_registry', df, summary)
    def load_return_window_grid_registry(self):
        return self._load_csv('advanced_feature_grid/returns/return_grid_registry.csv')

    def save_quote_feature_grid_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/quote/quote_placeholder_registry', df, summary)
    def load_quote_feature_grid_placeholder_registry(self):
        return self._load_csv('advanced_feature_grid/quote/quote_placeholder_registry.csv')

    def save_macro_feature_grid_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/macro/macro_placeholder_registry', df, summary)
    def load_macro_feature_grid_placeholder_registry(self):
        return self._load_csv('advanced_feature_grid/macro/macro_placeholder_registry.csv')

    def save_calendar_feature_grid_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/calendar/calendar_placeholder_registry', df, summary)
    def load_calendar_feature_grid_placeholder_registry(self):
        return self._load_csv('advanced_feature_grid/calendar/calendar_placeholder_registry.csv')

    def save_news_metadata_feature_grid_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/news/news_placeholder_registry', df, summary)
    def load_news_metadata_feature_grid_placeholder_registry(self):
        return self._load_csv('advanced_feature_grid/news/news_placeholder_registry.csv')

    def save_feature_grid_computation_interface_contract(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/computation/computation_interface_contract', df, summary)
    def load_feature_grid_computation_interface_contract(self):
        return self._load_csv('advanced_feature_grid/computation/computation_interface_contract.csv')

    def save_feature_grid_computation_rehearsal_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/rehearsal/rehearsal_report', df, summary)
    def load_feature_grid_computation_rehearsal_report(self):
        return self._load_csv('advanced_feature_grid/rehearsal/rehearsal_report.csv')

    def save_feature_grid_metadata_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/metadata/metadata_registry', df, summary)
    def load_feature_grid_metadata_registry(self):
        return self._load_csv('advanced_feature_grid/metadata/metadata_registry.csv')

    def save_feature_grid_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/dependencies/dependency_registry', df, summary)
    def load_feature_grid_dependency_registry(self):
        return self._load_csv('advanced_feature_grid/dependencies/dependency_registry.csv')

    def save_feature_grid_validation_rule_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/validation/validation_rule_registry', df, summary)
    def load_feature_grid_validation_rule_registry(self):
        return self._load_csv('advanced_feature_grid/validation/validation_rule_registry.csv')

    def save_feature_grid_quality_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/quality_handoff/quality_handoff_report', df, summary)
    def load_feature_grid_quality_handoff_report(self):
        return self._load_csv('advanced_feature_grid/quality_handoff/quality_handoff_report.csv')

    def save_multi_window_feature_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/health/health_check', df, summary)
    def load_multi_window_feature_health_check(self):
        return self._load_csv('advanced_feature_grid/health/health_check.csv')

    def save_multi_window_feature_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/validation/validation_report', df, summary)
    def load_multi_window_feature_validation_report(self):
        return self._load_csv('advanced_feature_grid/validation/validation_report.csv')

    def save_multi_window_feature_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/safety/safety_boundary', df, summary)
    def load_multi_window_feature_safety_boundary(self):
        return self._load_csv('advanced_feature_grid/safety/safety_boundary.csv')

    def save_phase_119_cross_asset_feature_alignment_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_grid/handoff/phase_119_handoff_report', df, summary)
    def load_phase_119_cross_asset_feature_alignment_handoff_report(self):
        return self._load_csv('advanced_feature_grid/handoff/phase_119_handoff_report.csv')

    def save_feature_grid_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_grid' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_feature_grid_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_grid' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_feature_grid_reports(self):
        return pd.DataFrame()

    # Phase 119 Cross-Asset Feature Alignment Data Lake Support
    def save_cross_asset_alignment_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/profiles/profile_registry', df, summary)
    def load_cross_asset_alignment_profile_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/profiles/profile_registry.csv')

    def save_cross_asset_alignment_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/domains/domain_registry', df, summary)
    def load_cross_asset_alignment_domain_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/domains/domain_registry.csv')

    def save_asset_universe_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/universes/universe_registry', df, summary)
    def load_asset_universe_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/universes/universe_registry.csv')

    def save_asset_symbol_mapping_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/symbols/symbol_mapping_registry', df, summary)
    def load_asset_symbol_mapping_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/symbols/symbol_mapping_registry.csv')

    def save_feature_namespace_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/namespaces/namespace_registry', df, summary)
    def load_feature_namespace_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/namespaces/namespace_registry.csv')

    def save_timestamp_alignment_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/timestamps/timestamp_contract_registry', df, summary)
    def load_timestamp_alignment_contract_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/timestamps/timestamp_contract_registry.csv')

    def save_session_calendar_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/sessions/session_calendar_registry', df, summary)
    def load_session_calendar_alignment_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/sessions/session_calendar_registry.csv')

    def save_feature_matrix_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/matrix_contracts/matrix_contract_registry', df, summary)
    def load_feature_matrix_contract_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/matrix_contracts/matrix_contract_registry.csv')

    def save_feature_matrix_join_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/join_policies/join_policy_registry', df, summary)
    def load_feature_matrix_join_policy_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/join_policies/join_policy_registry.csv')

    def save_fx_commodity_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/domain_alignments/fx_commodity_registry', df, summary)
    def load_fx_commodity_alignment_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/domain_alignments/fx_commodity_registry.csv')

    def save_fx_macro_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/domain_alignments/fx_macro_registry', df, summary)
    def load_fx_macro_alignment_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/domain_alignments/fx_macro_registry.csv')

    def save_fx_calendar_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/domain_alignments/fx_calendar_registry', df, summary)
    def load_fx_calendar_alignment_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/domain_alignments/fx_calendar_registry.csv')

    def save_fx_news_metadata_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/domain_alignments/fx_news_metadata_registry', df, summary)
    def load_fx_news_metadata_alignment_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/domain_alignments/fx_news_metadata_registry.csv')

    def save_commodity_macro_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/domain_alignments/commodity_macro_registry', df, summary)
    def load_commodity_macro_alignment_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/domain_alignments/commodity_macro_registry.csv')

    def save_commodity_calendar_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/domain_alignments/commodity_calendar_registry', df, summary)
    def load_commodity_calendar_alignment_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/domain_alignments/commodity_calendar_registry.csv')

    def save_commodity_news_metadata_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/domain_alignments/commodity_news_metadata_registry', df, summary)
    def load_commodity_news_metadata_alignment_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/domain_alignments/commodity_news_metadata_registry.csv')

    def save_macro_calendar_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/domain_alignments/macro_calendar_registry', df, summary)
    def load_macro_calendar_alignment_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/domain_alignments/macro_calendar_registry.csv')

    def save_calendar_news_metadata_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/domain_alignments/calendar_news_metadata_registry', df, summary)
    def load_calendar_news_metadata_alignment_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/domain_alignments/calendar_news_metadata_registry.csv')

    def save_cross_domain_feature_matrix(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/matrices/cross_domain_feature_matrix', df, summary)
    def load_cross_domain_feature_matrix(self):
        return self._load_csv('advanced_cross_asset_alignment/matrices/cross_domain_feature_matrix.csv')

    def save_aligned_feature_matrix_manifest_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/manifests/aligned_manifest_registry', df, summary)
    def load_aligned_feature_matrix_manifest_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/manifests/aligned_manifest_registry.csv')

    def save_cross_asset_feature_metadata_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/metadata/cross_asset_metadata_registry', df, summary)
    def load_cross_asset_feature_metadata_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/metadata/cross_asset_metadata_registry.csv')

    def save_cross_asset_alignment_validation_rule_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/validation/validation_rule_registry', df, summary)
    def load_cross_asset_alignment_validation_rule_registry(self):
        return self._load_csv('advanced_cross_asset_alignment/validation/validation_rule_registry.csv')

    def save_cross_asset_alignment_quality_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/quality_handoff/quality_handoff_report', df, summary)
    def load_cross_asset_alignment_quality_handoff_report(self):
        return self._load_csv('advanced_cross_asset_alignment/quality_handoff/quality_handoff_report.csv')

    def save_cross_asset_alignment_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/health/health_check', df, summary)
    def load_cross_asset_alignment_health_check(self):
        return self._load_csv('advanced_cross_asset_alignment/health/health_check.csv')

    def save_cross_asset_alignment_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/validation/validation_report', df, summary)
    def load_cross_asset_alignment_validation_report(self):
        return self._load_csv('advanced_cross_asset_alignment/validation/validation_report.csv')

    def save_cross_asset_alignment_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/safety/safety_boundary', df, summary)
    def load_cross_asset_alignment_safety_boundary(self):
        return self._load_csv('advanced_cross_asset_alignment/safety/safety_boundary.csv')

    def save_phase_120_cross_asset_feature_fusion_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_alignment/handoff/phase_120_handoff_report', df, summary)
    def load_phase_120_cross_asset_feature_fusion_handoff_report(self):
        return self._load_csv('advanced_cross_asset_alignment/handoff/phase_120_handoff_report.csv')

    def save_cross_asset_alignment_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_cross_asset_alignment' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_cross_asset_alignment_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_cross_asset_alignment' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_cross_asset_alignment_reports(self):
        return pd.DataFrame()

    # Phase 120 Macro/Calendar/News Feature Fusion methods
    def save_fusion_feature_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/profiles/fusion_feature_profile_registry', df, summary)
    def load_fusion_feature_profile_registry(self):
        return self._load_csv('advanced_feature_fusion/profiles/fusion_feature_profile_registry.csv')

    def save_fusion_feature_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/domains/fusion_feature_domain_registry', df, summary)
    def load_fusion_feature_domain_registry(self):
        return self._load_csv('advanced_feature_fusion/domains/fusion_feature_domain_registry.csv')

    def save_macro_feature_fusion_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/macro_contracts/macro_feature_fusion_contract_registry', df, summary)
    def load_macro_feature_fusion_contract_registry(self):
        return self._load_csv('advanced_feature_fusion/macro_contracts/macro_feature_fusion_contract_registry.csv')

    def save_calendar_event_fusion_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/calendar_contracts/calendar_event_fusion_contract_registry', df, summary)
    def load_calendar_event_fusion_contract_registry(self):
        return self._load_csv('advanced_feature_fusion/calendar_contracts/calendar_event_fusion_contract_registry.csv')

    def save_release_event_fusion_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/release_contracts/release_event_fusion_contract_registry', df, summary)
    def load_release_event_fusion_contract_registry(self):
        return self._load_csv('advanced_feature_fusion/release_contracts/release_event_fusion_contract_registry.csv')

    def save_news_metadata_fusion_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/news_contracts/news_metadata_fusion_contract_registry', df, summary)
    def load_news_metadata_fusion_contract_registry(self):
        return self._load_csv('advanced_feature_fusion/news_contracts/news_metadata_fusion_contract_registry.csv')

    def save_macro_release_lag_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/macro_lag/macro_release_lag_policy_registry', df, summary)
    def load_macro_release_lag_policy_registry(self):
        return self._load_csv('advanced_feature_fusion/macro_lag/macro_release_lag_policy_registry.csv')

    def save_calendar_event_window_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/event_windows/calendar_event_window_policy_registry', df, summary)
    def load_calendar_event_window_policy_registry(self):
        return self._load_csv('advanced_feature_fusion/event_windows/calendar_event_window_policy_registry.csv')

    def save_news_metadata_only_fusion_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/news_metadata_only/news_metadata_only_fusion_policy_registry', df, summary)
    def load_news_metadata_only_fusion_policy_registry(self):
        return self._load_csv('advanced_feature_fusion/news_metadata_only/news_metadata_only_fusion_policy_registry.csv')

    def save_fusion_timestamp_alignment_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/timestamp_alignment/fusion_timestamp_alignment_policy_registry', df, summary)
    def load_fusion_timestamp_alignment_policy_registry(self):
        return self._load_csv('advanced_feature_fusion/timestamp_alignment/fusion_timestamp_alignment_policy_registry.csv')

    def save_fusion_asof_join_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/asof_join/fusion_asof_join_policy_registry', df, summary)
    def load_fusion_asof_join_policy_registry(self):
        return self._load_csv('advanced_feature_fusion/asof_join/fusion_asof_join_policy_registry.csv')

    def save_no_lookahead_fusion_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/no_lookahead/no_lookahead_fusion_guard_registry', df, summary)
    def load_no_lookahead_fusion_guard_registry(self):
        return self._load_csv('advanced_feature_fusion/no_lookahead/no_lookahead_fusion_guard_registry.csv')

    def save_macro_feature_fusion_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/macro/macro_feature_fusion_registry', df, summary)
    def load_macro_feature_fusion_registry(self):
        return self._load_csv('advanced_feature_fusion/macro/macro_feature_fusion_registry.csv')

    def save_macro_surprise_feature_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/macro_surprise/macro_surprise_feature_placeholder_registry', df, summary)
    def load_macro_surprise_feature_placeholder_registry(self):
        return self._load_csv('advanced_feature_fusion/macro_surprise/macro_surprise_feature_placeholder_registry.csv')

    def save_macro_revision_feature_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/macro_revision/macro_revision_feature_placeholder_registry', df, summary)
    def load_macro_revision_feature_placeholder_registry(self):
        return self._load_csv('advanced_feature_fusion/macro_revision/macro_revision_feature_placeholder_registry.csv')

    def save_calendar_event_window_feature_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/calendar/calendar_event_window_feature_registry', df, summary)
    def load_calendar_event_window_feature_registry(self):
        return self._load_csv('advanced_feature_fusion/calendar/calendar_event_window_feature_registry.csv')

    def save_release_event_feature_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/release_events/release_event_feature_registry', df, summary)
    def load_release_event_feature_registry(self):
        return self._load_csv('advanced_feature_fusion/release_events/release_event_feature_registry.csv')

    def save_event_importance_feature_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/event_importance/event_importance_feature_placeholder_registry', df, summary)
    def load_event_importance_feature_placeholder_registry(self):
        return self._load_csv('advanced_feature_fusion/event_importance/event_importance_feature_placeholder_registry.csv')

    def save_news_topic_feature_fusion_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/news_topics/news_topic_feature_fusion_registry', df, summary)
    def load_news_topic_feature_fusion_registry(self):
        return self._load_csv('advanced_feature_fusion/news_topics/news_topic_feature_fusion_registry.csv')

    def save_news_asset_tag_feature_fusion_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/news_asset_tags/news_asset_tag_feature_fusion_registry', df, summary)
    def load_news_asset_tag_feature_fusion_registry(self):
        return self._load_csv('advanced_feature_fusion/news_asset_tags/news_asset_tag_feature_fusion_registry.csv')

    def save_news_event_linkage_feature_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/news_event_linkage/news_event_linkage_feature_registry', df, summary)
    def load_news_event_linkage_feature_registry(self):
        return self._load_csv('advanced_feature_fusion/news_event_linkage/news_event_linkage_feature_registry.csv')

    def save_news_freshness_feature_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/news_freshness/news_freshness_feature_placeholder_registry', df, summary)
    def load_news_freshness_feature_placeholder_registry(self):
        return self._load_csv('advanced_feature_fusion/news_freshness/news_freshness_feature_placeholder_registry.csv')

    def save_macro_calendar_fusion_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/macro_calendar/macro_calendar_fusion_registry', df, summary)
    def load_macro_calendar_fusion_registry(self):
        return self._load_csv('advanced_feature_fusion/macro_calendar/macro_calendar_fusion_registry.csv')

    def save_macro_news_fusion_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/macro_news/macro_news_fusion_registry', df, summary)
    def load_macro_news_fusion_registry(self):
        return self._load_csv('advanced_feature_fusion/macro_news/macro_news_fusion_registry.csv')

    def save_calendar_news_fusion_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/calendar_news/calendar_news_fusion_registry', df, summary)
    def load_calendar_news_fusion_registry(self):
        return self._load_csv('advanced_feature_fusion/calendar_news/calendar_news_fusion_registry.csv')

    def save_cross_domain_context_fusion_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/cross_domain_context/cross_domain_context_fusion_registry', df, summary)
    def load_cross_domain_context_fusion_registry(self):
        return self._load_csv('advanced_feature_fusion/cross_domain_context/cross_domain_context_fusion_registry.csv')

    def save_fusion_feature_matrix_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/matrix_contracts/fusion_feature_matrix_contract_registry', df, summary)
    def load_fusion_feature_matrix_contract_registry(self):
        return self._load_csv('advanced_feature_fusion/matrix_contracts/fusion_feature_matrix_contract_registry.csv')

    def save_fusion_feature_matrix_placeholder(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/matrix/fusion_feature_matrix_placeholder', df, summary)
    def load_fusion_feature_matrix_placeholder(self):
        return self._load_csv('advanced_feature_fusion/matrix/fusion_feature_matrix_placeholder.csv')

    def save_fusion_feature_metadata_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/metadata/fusion_feature_metadata_registry', df, summary)
    def load_fusion_feature_metadata_registry(self):
        return self._load_csv('advanced_feature_fusion/metadata/fusion_feature_metadata_registry.csv')

    def save_fusion_feature_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/dependencies/fusion_feature_dependency_registry', df, summary)
    def load_fusion_feature_dependency_registry(self):
        return self._load_csv('advanced_feature_fusion/dependencies/fusion_feature_dependency_registry.csv')

    def save_fusion_feature_validation_rule_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/validation/fusion_feature_validation_rule_registry', df, summary)
    def load_fusion_feature_validation_rule_registry(self):
        return self._load_csv('advanced_feature_fusion/validation/fusion_feature_validation_rule_registry.csv')

    def save_fusion_quality_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/quality_handoff/fusion_quality_handoff_report', df, summary)
    def load_fusion_quality_handoff_report(self):
        return self._load_csv('advanced_feature_fusion/quality_handoff/fusion_quality_handoff_report.csv')

    def save_fusion_feature_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/health/fusion_feature_health_check', df, summary)
    def load_fusion_feature_health_check(self):
        return self._load_csv('advanced_feature_fusion/health/fusion_feature_health_check.csv')

    def save_fusion_feature_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/validation/fusion_feature_validation_report', df, summary)
    def load_fusion_feature_validation_report(self):
        return self._load_csv('advanced_feature_fusion/validation/fusion_feature_validation_report.csv')

    def save_fusion_feature_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/safety/fusion_feature_safety_boundary', df, summary)
    def load_fusion_feature_safety_boundary(self):
        return self._load_csv('advanced_feature_fusion/safety/fusion_feature_safety_boundary.csv')

    def save_phase_121_feature_validation_no_lookahead_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/handoff/phase_121_handoff_report', df, summary)
    def load_phase_121_feature_validation_no_lookahead_handoff_report(self):
        return self._load_csv('advanced_feature_fusion/handoff/phase_121_handoff_report.csv')

    def save_fusion_feature_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_fusion' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_fusion_feature_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_fusion' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_fusion_feature_reports(self):
        return pd.DataFrame()

    def save_macro_feature_fusion_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/contracts/macro_feature_fusion_contract_registry', df if isinstance(df, pd.DataFrame) else pd.DataFrame(df), summary)
    def save_calendar_event_fusion_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/contracts/calendar_event_fusion_contract_registry', df if isinstance(df, pd.DataFrame) else pd.DataFrame(df), summary)
    def save_release_event_fusion_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/contracts/release_event_fusion_contract_registry', df if isinstance(df, pd.DataFrame) else pd.DataFrame(df), summary)
    def save_news_metadata_fusion_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/contracts/news_metadata_fusion_contract_registry', df if isinstance(df, pd.DataFrame) else pd.DataFrame(df), summary)
    def save_macro_release_lag_policies(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/policies/macro_release_lag_policy_registry', df if isinstance(df, pd.DataFrame) else pd.DataFrame(df), summary)
    def save_calendar_event_window_policies(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/policies/calendar_event_window_policy_registry', df if isinstance(df, pd.DataFrame) else pd.DataFrame(df), summary)
    def save_news_metadata_only_fusion_policies(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/policies/news_metadata_only_policy_registry', df if isinstance(df, pd.DataFrame) else pd.DataFrame(df), summary)
    def save_fusion_timestamp_alignment_policies(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/policies/fusion_timestamp_alignment_policy_registry', df if isinstance(df, pd.DataFrame) else pd.DataFrame(df), summary)
    def save_fusion_asof_join_policies(self, df, summary=None):
        return self._save_csv_json('advanced_feature_fusion/policies/fusion_asof_join_policy_registry', df if isinstance(df, pd.DataFrame) else pd.DataFrame(df), summary)
    def save_macro_calendar_news_fusion_registries(self, summary):
        return self._save_csv_json('advanced_feature_fusion/cross_fusion/macro_calendar_news_fusion_registries', None, summary)
    def save_fusion_feature_matrix_manifest(self, summary):
        return self._save_csv_json('advanced_feature_fusion/matrix/fusion_feature_matrix_manifest', None, summary)
    def save_fusion_quality_handoff(self, summary):
        return self._save_csv_json('advanced_feature_fusion/quality_handoff/fusion_quality_handoff', None, summary)
    def save_fusion_feature_report_markdown(self, markdown_text: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_fusion' / 'fusion_feature_report.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(markdown_text)
        return path
    def save_fusion_feature_report_text(self, text_content: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_fusion' / 'fusion_feature_report.txt'
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text_content)
        return path

    # Phase 121 Feature Validation and No-Lookahead Guard DataLake Support
    def save_feature_validation_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/profiles/profile_registry', df, summary)
    def load_feature_validation_profile_registry(self):
        return self._load_csv('advanced_feature_validation/profiles/profile_registry.csv')

    def save_feature_validation_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/domains/domain_registry', df, summary)
    def load_feature_validation_domain_registry(self):
        return self._load_csv('advanced_feature_validation/domains/domain_registry.csv')

    def save_feature_validation_rule_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/rules/rule_registry', df, summary)
    def load_feature_validation_rule_registry(self):
        return self._load_csv('advanced_feature_validation/rules/rule_registry.csv')

    def save_forbidden_feature_column_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/forbidden_columns/forbidden_column_registry', df, summary)
    def load_forbidden_feature_column_registry(self):
        return self._load_csv('advanced_feature_validation/forbidden_columns/forbidden_column_registry.csv')

    def save_no_lookahead_rule_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/no_lookahead/no_lookahead_rule_registry', df, summary)
    def load_no_lookahead_rule_registry(self):
        return self._load_csv('advanced_feature_validation/no_lookahead/no_lookahead_rule_registry.csv')

    def save_timestamp_order_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/timestamp_order/timestamp_order_validation_registry', df, summary)
    def load_timestamp_order_validation_registry(self):
        return self._load_csv('advanced_feature_validation/timestamp_order/timestamp_order_validation_registry.csv')

    def save_asof_join_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/asof_join/asof_join_validation_registry', df, summary)
    def load_asof_join_validation_registry(self):
        return self._load_csv('advanced_feature_validation/asof_join/asof_join_validation_registry.csv')

    def save_macro_release_lag_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/macro_lag/macro_release_lag_validation_registry', df, summary)
    def load_macro_release_lag_validation_registry(self):
        return self._load_csv('advanced_feature_validation/macro_lag/macro_release_lag_validation_registry.csv')

    def save_event_window_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/event_window/event_window_validation_registry', df, summary)
    def load_event_window_validation_registry(self):
        return self._load_csv('advanced_feature_validation/event_window/event_window_validation_registry.csv')

    def save_news_metadata_only_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/news_metadata_only/news_metadata_only_validation_registry', df, summary)
    def load_news_metadata_only_validation_registry(self):
        return self._load_csv('advanced_feature_validation/news_metadata_only/news_metadata_only_validation_registry.csv')

    def save_warmup_nan_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/warmup_nan/warmup_nan_validation_registry', df, summary)
    def load_warmup_nan_validation_registry(self):
        return self._load_csv('advanced_feature_validation/warmup_nan/warmup_nan_validation_registry.csv')

    def save_duplicate_feature_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/duplicate_features/duplicate_feature_validation_registry', df, summary)
    def load_duplicate_feature_validation_registry(self):
        return self._load_csv('advanced_feature_validation/duplicate_features/duplicate_feature_validation_registry.csv')

    def save_namespace_collision_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/namespace_collision/namespace_collision_validation_registry', df, summary)
    def load_namespace_collision_validation_registry(self):
        return self._load_csv('advanced_feature_validation/namespace_collision/namespace_collision_validation_registry.csv')

    def save_feature_numeric_sanity_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/numeric_sanity/feature_numeric_sanity_validation_registry', df, summary)
    def load_feature_numeric_sanity_validation_registry(self):
        return self._load_csv('advanced_feature_validation/numeric_sanity/feature_numeric_sanity_validation_registry.csv')

    def save_feature_missingness_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/missingness/feature_missingness_validation_registry', df, summary)
    def load_feature_missingness_validation_registry(self):
        return self._load_csv('advanced_feature_validation/missingness/feature_missingness_validation_registry.csv')

    def save_feature_infinite_value_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/infinite_values/feature_infinite_value_validation_registry', df, summary)
    def load_feature_infinite_value_validation_registry(self):
        return self._load_csv('advanced_feature_validation/infinite_values/feature_infinite_value_validation_registry.csv')

    def save_feature_matrix_integrity_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/matrix_contracts/feature_matrix_integrity_contracts', df, summary)
    def load_feature_matrix_integrity_contracts(self):
        return self._load_csv('advanced_feature_validation/matrix_contracts/feature_matrix_integrity_contracts.csv')

    def save_feature_matrix_integrity_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/matrix_manifest/feature_matrix_integrity_manifest', df, summary)
    def load_feature_matrix_integrity_manifest(self):
        return self._load_csv('advanced_feature_validation/matrix_manifest/feature_matrix_integrity_manifest.csv')

    def save_feature_validation_finding_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/findings/finding_registry', df, summary)
    def load_feature_validation_finding_registry(self):
        return self._load_csv('advanced_feature_validation/findings/finding_registry.csv')

    def save_feature_validation_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/manual_review/review_queue', df, summary)
    def load_feature_validation_manual_review_queue(self):
        return self._load_csv('advanced_feature_validation/manual_review/review_queue.csv')

    def save_feature_validation_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/scoring/score_report', df, summary)
    def load_feature_validation_score_report(self):
        return self._load_csv('advanced_feature_validation/scoring/score_report.csv')

    def save_indicator_output_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/indicator_outputs/indicator_output_validation_registry', df, summary)
    def load_indicator_output_validation_registry(self):
        return self._load_csv('advanced_feature_validation/indicator_outputs/indicator_output_validation_registry.csv')

    def save_feature_grid_output_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/grid_outputs/feature_grid_output_validation_registry', df, summary)
    def load_feature_grid_output_validation_registry(self):
        return self._load_csv('advanced_feature_validation/grid_outputs/feature_grid_output_validation_registry.csv')

    def save_cross_asset_alignment_output_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/alignment_outputs/cross_asset_alignment_output_validation_registry', df, summary)
    def load_cross_asset_alignment_output_validation_registry(self):
        return self._load_csv('advanced_feature_validation/alignment_outputs/cross_asset_alignment_output_validation_registry.csv')

    def save_fusion_feature_output_validation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/fusion_outputs/fusion_feature_output_validation_registry', df, summary)
    def load_fusion_feature_output_validation_registry(self):
        return self._load_csv('advanced_feature_validation/fusion_outputs/fusion_feature_output_validation_registry.csv')

    def save_no_leakage_guard_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/leakage_guard/no_leakage_guard_report', df, summary)
    def load_no_leakage_guard_report(self):
        return self._load_csv('advanced_feature_validation/leakage_guard/no_leakage_guard_report.csv')

    def save_non_signal_feature_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/non_signal/non_signal_feature_validation_report', df, summary)
    def load_non_signal_feature_validation_report(self):
        return self._load_csv('advanced_feature_validation/non_signal/non_signal_feature_validation_report.csv')

    def save_feature_validation_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/health/health_check', df, summary)
    def load_feature_validation_health_check(self):
        return self._load_csv('advanced_feature_validation/health/health_check.csv')

    def save_feature_validation_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/validation/validation_report', df, summary)
    def load_feature_validation_validation_report(self):
        return self._load_csv('advanced_feature_validation/validation/validation_report.csv')

    def save_feature_validation_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/safety/safety_boundary', df, summary)
    def load_feature_validation_safety_boundary(self):
        return self._load_csv('advanced_feature_validation/safety/safety_boundary.csv')

    def save_phase_122_selection_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_validation/handoff/phase_122_handoff_report', df, summary)
    def load_phase_122_selection_handoff_report(self):
        return self._load_csv('advanced_feature_validation/handoff/phase_122_handoff_report.csv')

    def save_feature_validation_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_validation' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_feature_validation_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_validation' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_feature_validation_reports(self):
        return pd.DataFrame()

    def save_feature_validation_report_markdown(self, markdown_text: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_validation' / 'feature_validation_report.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(markdown_text)
        return path

    def save_feature_validation_report_text(self, text_content: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_validation' / 'feature_validation_report.txt'
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text_content)
        return path

    # Phase 122 Factor Metadata and Factor Families DataLake methods
    def save_factor_metadata_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/profiles/factor_metadata_profile_registry', df, summary)
    def load_factor_metadata_profile_registry(self):
        return self._load_csv('advanced_factor_metadata/profiles/factor_metadata_profile_registry.csv')

    def save_factor_metadata_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/domains/factor_metadata_domain_registry', df, summary)
    def load_factor_metadata_domain_registry(self):
        return self._load_csv('advanced_factor_metadata/domains/factor_metadata_domain_registry.csv')

    def save_factor_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/families/factor_family_registry', df, summary)
    def load_factor_family_registry(self):
        return self._load_csv('advanced_factor_metadata/families/factor_family_registry.csv')

    def save_factor_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/contracts/factor_contract_registry', df, summary)
    def load_factor_contract_registry(self):
        return self._load_csv('advanced_factor_metadata/contracts/factor_contract_registry.csv')

    def save_factor_input_feature_set_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/input_feature_sets/factor_input_feature_set_registry', df, summary)
    def load_factor_input_feature_set_registry(self):
        return self._load_csv('advanced_factor_metadata/input_feature_sets/factor_input_feature_set_registry.csv')

    def save_factor_namespace_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/namespace/factor_namespace_registry', df, summary)
    def load_factor_namespace_registry(self):
        return self._load_csv('advanced_factor_metadata/namespace/factor_namespace_registry.csv')

    def save_factor_output_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/output_schema/factor_output_schema_registry', df, summary)
    def load_factor_output_schema_registry(self):
        return self._load_csv('advanced_factor_metadata/output_schema/factor_output_schema_registry.csv')

    def save_factor_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/dependencies/factor_dependency_registry', df, summary)
    def load_factor_dependency_registry(self):
        return self._load_csv('advanced_factor_metadata/dependencies/factor_dependency_registry.csv')

    def save_factor_validation_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/validation_dependencies/factor_validation_dependency_registry', df, summary)
    def load_factor_validation_dependency_registry(self):
        return self._load_csv('advanced_factor_metadata/validation_dependencies/factor_validation_dependency_registry.csv')

    def save_factor_quality_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/quality_dependencies/factor_quality_dependency_registry', df, summary)
    def load_factor_quality_dependency_registry(self):
        return self._load_csv('advanced_factor_metadata/quality_dependencies/factor_quality_dependency_registry.csv')

    def save_technical_factor_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/technical/technical_factor_family_registry', df, summary)
    def load_technical_factor_family_registry(self):
        return self._load_csv('advanced_factor_metadata/technical/technical_factor_family_registry.csv')

    def save_trend_factor_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/trend/trend_factor_family_registry', df, summary)
    def load_trend_factor_family_registry(self):
        return self._load_csv('advanced_factor_metadata/trend/trend_factor_family_registry.csv')

    def save_momentum_factor_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/momentum/momentum_factor_family_registry', df, summary)
    def load_momentum_factor_family_registry(self):
        return self._load_csv('advanced_factor_metadata/momentum/momentum_factor_family_registry.csv')

    def save_volatility_factor_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/volatility/volatility_factor_family_registry', df, summary)
    def load_volatility_factor_family_registry(self):
        return self._load_csv('advanced_factor_metadata/volatility/volatility_factor_family_registry.csv')

    def save_mean_reversion_factor_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/mean_reversion/mean_reversion_factor_family_registry', df, summary)
    def load_mean_reversion_factor_family_registry(self):
        return self._load_csv('advanced_factor_metadata/mean_reversion/mean_reversion_factor_family_registry.csv')

    def save_return_factor_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/returns/return_factor_family_registry', df, summary)
    def load_return_factor_family_registry(self):
        return self._load_csv('advanced_factor_metadata/returns/return_factor_family_registry.csv')

    def save_quote_microstructure_factor_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/quote_microstructure/quote_microstructure_factor_placeholder_registry', df, summary)
    def load_quote_microstructure_factor_placeholder_registry(self):
        return self._load_csv('advanced_factor_metadata/quote_microstructure/quote_microstructure_factor_placeholder_registry.csv')

    def save_macro_context_factor_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/macro_context/macro_context_factor_family_registry', df, summary)
    def load_macro_context_factor_family_registry(self):
        return self._load_csv('advanced_factor_metadata/macro_context/macro_context_factor_family_registry.csv')

    def save_calendar_event_factor_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/calendar_event/calendar_event_factor_family_registry', df, summary)
    def load_calendar_event_factor_family_registry(self):
        return self._load_csv('advanced_factor_metadata/calendar_event/calendar_event_factor_family_registry.csv')

    def save_news_attention_factor_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/news_attention/news_attention_factor_family_registry', df, summary)
    def load_news_attention_factor_family_registry(self):
        return self._load_csv('advanced_factor_metadata/news_attention/news_attention_factor_family_registry.csv')

    def save_cross_asset_context_factor_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/cross_asset_context/cross_asset_context_factor_family_registry', df, summary)
    def load_cross_asset_context_factor_family_registry(self):
        return self._load_csv('advanced_factor_metadata/cross_asset_context/cross_asset_context_factor_family_registry.csv')

    def save_regime_prep_factor_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/regime_prep/regime_prep_factor_placeholder_registry', df, summary)
    def load_regime_prep_factor_placeholder_registry(self):
        return self._load_csv('advanced_factor_metadata/regime_prep/regime_prep_factor_placeholder_registry.csv')

    def save_composite_factor_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/composite/composite_factor_placeholder_registry', df, summary)
    def load_composite_factor_placeholder_registry(self):
        return self._load_csv('advanced_factor_metadata/composite/composite_factor_placeholder_registry.csv')

    def save_factor_metadata_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/manifest/factor_metadata_manifest', df, summary)
    def load_factor_metadata_manifest(self):
        return self._load_csv('advanced_factor_metadata/manifest/factor_metadata_manifest.csv')

    def save_factor_manual_review_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/manual_review/factor_manual_review_registry', df, summary)
    def load_factor_manual_review_registry(self):
        return self._load_csv('advanced_factor_metadata/manual_review/factor_manual_review_registry.csv')

    def save_factor_non_signal_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/non_signal/factor_non_signal_policy_registry', df, summary)
    def load_factor_non_signal_policy_registry(self):
        return self._load_csv('advanced_factor_metadata/non_signal/factor_non_signal_policy_registry.csv')

    def save_factor_forbidden_claim_registry(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/forbidden_claims/factor_forbidden_claim_registry', df, summary)
    def load_factor_forbidden_claim_registry(self):
        return self._load_csv('advanced_factor_metadata/forbidden_claims/factor_forbidden_claim_registry.csv')

    def save_factor_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/health/factor_health_check', df, summary)
    def load_factor_health_check(self):
        return self._load_csv('advanced_factor_metadata/health/factor_health_check.csv')

    def save_factor_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/validation/factor_validation_report', df, summary)
    def load_factor_validation_report(self):
        return self._load_csv('advanced_factor_metadata/validation/factor_validation_report.csv')

    def save_factor_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/safety/factor_safety_boundary', df, summary)
    def load_factor_safety_boundary(self):
        return self._load_csv('advanced_factor_metadata/safety/factor_safety_boundary.csv')

    def save_phase_123_feature_quality_drift_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_factor_metadata/handoff/phase_123_feature_quality_drift_handoff_report', df, summary)
    def load_phase_123_feature_quality_drift_handoff_report(self):
        return self._load_csv('advanced_factor_metadata/handoff/phase_123_feature_quality_drift_handoff_report.csv')

    def save_factor_metadata_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_factor_metadata' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_factor_metadata_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_factor_metadata' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_factor_metadata_reports(self):
        return pd.DataFrame()

    # Phase 123 Feature Quality and Drift Diagnostics DataLake Support
    def save_feature_quality_drift_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/profiles/feature_quality_drift_profile_registry', df, summary)
    def load_feature_quality_drift_profile_registry(self):
        return self._load_csv('advanced_feature_quality_drift/profiles/feature_quality_drift_profile_registry.csv')

    def save_feature_quality_drift_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/domains/feature_quality_drift_domain_registry', df, summary)
    def load_feature_quality_drift_domain_registry(self):
        return self._load_csv('advanced_feature_quality_drift/domains/feature_quality_drift_domain_registry.csv')

    def save_feature_quality_metric_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/metrics/feature_quality_metric_registry', df, summary)
    def load_feature_quality_metric_registry(self):
        return self._load_csv('advanced_feature_quality_drift/metrics/feature_quality_metric_registry.csv')

    def save_feature_drift_metric_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/metrics/feature_drift_metric_registry', df, summary)
    def load_feature_drift_metric_registry(self):
        return self._load_csv('advanced_feature_quality_drift/metrics/feature_drift_metric_registry.csv')

    def save_feature_quality_threshold_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/thresholds/feature_quality_threshold_registry', df, summary)
    def load_feature_quality_threshold_registry(self):
        return self._load_csv('advanced_feature_quality_drift/thresholds/feature_quality_threshold_registry.csv')

    def save_feature_drift_threshold_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/thresholds/feature_drift_threshold_registry', df, summary)
    def load_feature_drift_threshold_registry(self):
        return self._load_csv('advanced_feature_quality_drift/thresholds/feature_drift_threshold_registry.csv')

    def save_feature_quality_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/contracts/feature_quality_input_contract_registry', df, summary)
    def load_feature_quality_input_contract_registry(self):
        return self._load_csv('advanced_feature_quality_drift/contracts/feature_quality_input_contract_registry.csv')

    def save_feature_drift_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/contracts/feature_drift_input_contract_registry', df, summary)
    def load_feature_drift_input_contract_registry(self):
        return self._load_csv('advanced_feature_quality_drift/contracts/feature_drift_input_contract_registry.csv')

    def save_feature_missingness_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/missingness/feature_missingness_diagnostics_report', df, summary)
    def load_feature_missingness_diagnostics_report(self):
        return self._load_csv('advanced_feature_quality_drift/missingness/feature_missingness_diagnostics_report.csv')

    def save_feature_infinite_value_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/infinite_values/feature_infinite_value_diagnostics_report', df, summary)
    def load_feature_infinite_value_diagnostics_report(self):
        return self._load_csv('advanced_feature_quality_drift/infinite_values/feature_infinite_value_diagnostics_report.csv')

    def save_feature_all_nan_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/all_nan/feature_all_nan_diagnostics_report', df, summary)
    def load_feature_all_nan_diagnostics_report(self):
        return self._load_csv('advanced_feature_quality_drift/all_nan/feature_all_nan_diagnostics_report.csv')

    def save_feature_zero_variance_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/zero_variance/feature_zero_variance_diagnostics_report', df, summary)
    def load_feature_zero_variance_diagnostics_report(self):
        return self._load_csv('advanced_feature_quality_drift/zero_variance/feature_zero_variance_diagnostics_report.csv')

    def save_feature_duplicate_value_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/duplicates/feature_duplicate_value_diagnostics_report', df, summary)
    def load_feature_duplicate_value_diagnostics_report(self):
        return self._load_csv('advanced_feature_quality_drift/duplicates/feature_duplicate_value_diagnostics_report.csv')

    def save_feature_distribution_summary_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/distribution/feature_distribution_summary_report', df, summary)
    def load_feature_distribution_summary_report(self):
        return self._load_csv('advanced_feature_quality_drift/distribution/feature_distribution_summary_report.csv')

    def save_feature_distribution_drift_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/drift/feature_distribution_drift_report', df, summary)
    def load_feature_distribution_drift_report(self):
        return self._load_csv('advanced_feature_quality_drift/drift/feature_distribution_drift_report.csv')

    def save_feature_rolling_stability_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/stability/feature_rolling_stability_report', df, summary)
    def load_feature_rolling_stability_report(self):
        return self._load_csv('advanced_feature_quality_drift/stability/feature_rolling_stability_report.csv')

    def save_feature_staleness_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/staleness/feature_staleness_diagnostics_report', df, summary)
    def load_feature_staleness_diagnostics_report(self):
        return self._load_csv('advanced_feature_quality_drift/staleness/feature_staleness_diagnostics_report.csv')

    def save_feature_namespace_quality_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/namespace/feature_namespace_quality_report', df, summary)
    def load_feature_namespace_quality_report(self):
        return self._load_csv('advanced_feature_quality_drift/namespace/feature_namespace_quality_report.csv')

    def save_factor_family_quality_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/factor_quality/factor_family_quality_report', df, summary)
    def load_factor_family_quality_report(self):
        return self._load_csv('advanced_feature_quality_drift/factor_quality/factor_family_quality_report.csv')

    def save_factor_family_drift_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/factor_drift/factor_family_drift_report', df, summary)
    def load_factor_family_drift_report(self):
        return self._load_csv('advanced_feature_quality_drift/factor_drift/factor_family_drift_report.csv')

    def save_factor_availability_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/factor_availability/factor_availability_report', df, summary)
    def load_factor_availability_report(self):
        return self._load_csv('advanced_feature_quality_drift/factor_availability/factor_availability_report.csv')

    def save_factor_dependency_quality_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/factor_quality/factor_dependency_quality_report', df, summary)
    def load_factor_dependency_quality_report(self):
        return self._load_csv('advanced_feature_quality_drift/factor_quality/factor_dependency_quality_report.csv')

    def save_macro_calendar_news_quality_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/macro_calendar_news/macro_calendar_news_quality_report', df, summary)
    def load_macro_calendar_news_quality_report(self):
        return self._load_csv('advanced_feature_quality_drift/macro_calendar_news/macro_calendar_news_quality_report.csv')

    def save_cross_asset_feature_quality_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/cross_asset/cross_asset_feature_quality_report', df, summary)
    def load_cross_asset_feature_quality_report(self):
        return self._load_csv('advanced_feature_quality_drift/cross_asset/cross_asset_feature_quality_report.csv')

    def save_feature_quality_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/findings/feature_quality_findings_registry', df, summary)
    def load_feature_quality_findings_registry(self):
        return self._load_csv('advanced_feature_quality_drift/findings/feature_quality_findings_registry.csv')

    def save_feature_drift_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/findings/feature_drift_findings_registry', df, summary)
    def load_feature_drift_findings_registry(self):
        return self._load_csv('advanced_feature_quality_drift/findings/feature_drift_findings_registry.csv')

    def save_feature_quality_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/manual_review/feature_quality_manual_review_queue', df, summary)
    def load_feature_quality_manual_review_queue(self):
        return self._load_csv('advanced_feature_quality_drift/manual_review/feature_quality_manual_review_queue.csv')

    def save_feature_drift_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/manual_review/feature_drift_manual_review_queue', df, summary)
    def load_feature_drift_manual_review_queue(self):
        return self._load_csv('advanced_feature_quality_drift/manual_review/feature_drift_manual_review_queue.csv')

    def save_feature_quality_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/scoring/feature_quality_score_report', df, summary)
    def load_feature_quality_score_report(self):
        return self._load_csv('advanced_feature_quality_drift/scoring/feature_quality_score_report.csv')

    def save_feature_drift_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/scoring/feature_drift_score_report', df, summary)
    def load_feature_drift_score_report(self):
        return self._load_csv('advanced_feature_quality_drift/scoring/feature_drift_score_report.csv')

    def save_feature_quality_drift_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/manifest/feature_quality_drift_manifest', df, summary)
    def load_feature_quality_drift_manifest(self):
        return self._load_csv('advanced_feature_quality_drift/manifest/feature_quality_drift_manifest.csv')

    def save_feature_quality_drift_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/health/feature_quality_drift_health_check', df, summary)
    def load_feature_quality_drift_health_check(self):
        return self._load_csv('advanced_feature_quality_drift/health/feature_quality_drift_health_check.csv')

    def save_feature_quality_drift_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/validation/feature_quality_drift_validation_report', df, summary)
    def load_feature_quality_drift_validation_report(self):
        return self._load_csv('advanced_feature_quality_drift/validation/feature_quality_drift_validation_report.csv')

    def save_feature_quality_drift_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/safety/feature_quality_drift_safety_boundary', df, summary)
    def load_feature_quality_drift_safety_boundary(self):
        return self._load_csv('advanced_feature_quality_drift/safety/feature_quality_drift_safety_boundary.csv')

    def save_phase_124_feature_store_integration_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_quality_drift/handoff/phase_124_feature_store_integration_handoff_report', df, summary)
    def load_phase_124_feature_store_integration_handoff_report(self):
        return self._load_csv('advanced_feature_quality_drift/handoff/phase_124_feature_store_integration_handoff_report.csv')

    def save_feature_quality_drift_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_quality_drift' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_feature_quality_drift_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_quality_drift' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_feature_quality_drift_reports(self):
        return pd.DataFrame()

    # Phase 124 Feature Store Integration Expansion DataLake Support
    def save_feature_store_integration_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/profiles/profile_registry', df, summary)
    def load_feature_store_integration_profile_registry(self):
        return self._load_csv('advanced_feature_store_integration/profiles/profile_registry.csv')

    def save_feature_store_integration_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/domains/domain_registry', df, summary)
    def load_feature_store_integration_domain_registry(self):
        return self._load_csv('advanced_feature_store_integration/domains/domain_registry.csv')

    def save_feature_store_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/contracts/contract_registry', df, summary)
    def load_feature_store_contract_registry(self):
        return self._load_csv('advanced_feature_store_integration/contracts/contract_registry.csv')

    def save_feature_store_entity_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/entities/entity_registry', df, summary)
    def load_feature_store_entity_registry(self):
        return self._load_csv('advanced_feature_store_integration/entities/entity_registry.csv')

    def save_feature_store_feature_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/features/feature_registry', df, summary)
    def load_feature_store_feature_registry(self):
        return self._load_csv('advanced_feature_store_integration/features/feature_registry.csv')

    def save_feature_store_factor_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/factors/factor_registry', df, summary)
    def load_feature_store_factor_registry(self):
        return self._load_csv('advanced_feature_store_integration/factors/factor_registry.csv')

    def save_feature_store_namespace_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/namespace/namespace_registry', df, summary)
    def load_feature_store_namespace_registry(self):
        return self._load_csv('advanced_feature_store_integration/namespace/namespace_registry.csv')

    def save_feature_store_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/schema/schema_registry', df, summary)
    def load_feature_store_schema_registry(self):
        return self._load_csv('advanced_feature_store_integration/schema/schema_registry.csv')

    def save_feature_store_version_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/version_policy/version_policy_registry', df, summary)
    def load_feature_store_version_policy_registry(self):
        return self._load_csv('advanced_feature_store_integration/version_policy/version_policy_registry.csv')

    def save_feature_store_partition_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/partition_policy/partition_policy_registry', df, summary)
    def load_feature_store_partition_policy_registry(self):
        return self._load_csv('advanced_feature_store_integration/partition_policy/partition_policy_registry.csv')

    def save_feature_store_lineage_reference_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/lineage/lineage_reference_registry', df, summary)
    def load_feature_store_lineage_reference_registry(self):
        return self._load_csv('advanced_feature_store_integration/lineage/lineage_reference_registry.csv')

    def save_feature_store_validation_status_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/validation_status/validation_status_registry', df, summary)
    def load_feature_store_validation_status_registry(self):
        return self._load_csv('advanced_feature_store_integration/validation_status/validation_status_registry.csv')

    def save_feature_store_quality_score_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/quality_scores/quality_score_registry', df, summary)
    def load_feature_store_quality_score_registry(self):
        return self._load_csv('advanced_feature_store_integration/quality_scores/quality_score_registry.csv')

    def save_feature_store_drift_score_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/drift_scores/drift_score_registry', df, summary)
    def load_feature_store_drift_score_registry(self):
        return self._load_csv('advanced_feature_store_integration/drift_scores/drift_score_registry.csv')

    def save_feature_store_manual_review_blocker_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/manual_review/manual_review_blocker_registry', df, summary)
    def load_feature_store_manual_review_blocker_registry(self):
        return self._load_csv('advanced_feature_store_integration/manual_review/manual_review_blocker_registry.csv')

    def save_feature_store_metadata_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/manifest/feature_store_metadata_manifest', df, summary)
    def load_feature_store_metadata_manifest(self):
        return self._load_csv('advanced_feature_store_integration/manifest/feature_store_metadata_manifest.csv')

    def save_feature_store_read_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/read_contracts/read_contract_registry', df, summary)
    def load_feature_store_read_contract_registry(self):
        return self._load_csv('advanced_feature_store_integration/read_contracts/read_contract_registry.csv')

    def save_feature_store_write_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/write_contracts/write_contract_registry', df, summary)
    def load_feature_store_write_contract_registry(self):
        return self._load_csv('advanced_feature_store_integration/write_contracts/write_contract_registry.csv')

    def save_feature_store_query_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/query_contracts/query_contract_registry', df, summary)
    def load_feature_store_query_contract_registry(self):
        return self._load_csv('advanced_feature_store_integration/query_contracts/query_contract_registry.csv')

    def save_feature_store_non_signal_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/non_signal/non_signal_policy_registry', df, summary)
    def load_feature_store_non_signal_policy_registry(self):
        return self._load_csv('advanced_feature_store_integration/non_signal/non_signal_policy_registry.csv')

    def save_feature_store_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/forbidden_columns/forbidden_column_policy_registry', df, summary)
    def load_feature_store_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_feature_store_integration/forbidden_columns/forbidden_column_policy_registry.csv')

    def save_feature_store_source_preservation_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/source_preservation/source_preservation_policy_registry', df, summary)
    def load_feature_store_source_preservation_policy_registry(self):
        return self._load_csv('advanced_feature_store_integration/source_preservation/source_preservation_policy_registry.csv')

    def save_feature_store_feature_catalog_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/catalogs/feature_catalog_report', df, summary)
    def load_feature_store_feature_catalog_report(self):
        return self._load_csv('advanced_feature_store_integration/catalogs/feature_catalog_report.csv')

    def save_feature_store_factor_catalog_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/catalogs/factor_catalog_report', df, summary)
    def load_feature_store_factor_catalog_report(self):
        return self._load_csv('advanced_feature_store_integration/catalogs/factor_catalog_report.csv')

    def save_feature_store_quality_drift_catalog_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/catalogs/quality_drift_catalog_report', df, summary)
    def load_feature_store_quality_drift_catalog_report(self):
        return self._load_csv('advanced_feature_store_integration/catalogs/quality_drift_catalog_report.csv')

    def save_feature_store_validation_catalog_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/catalogs/validation_catalog_report', df, summary)
    def load_feature_store_validation_catalog_report(self):
        return self._load_csv('advanced_feature_store_integration/catalogs/validation_catalog_report.csv')

    def save_feature_store_integration_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/health/feature_store_integration_health_check', df, summary)
    def load_feature_store_integration_health_check(self):
        return self._load_csv('advanced_feature_store_integration/health/feature_store_integration_health_check.csv')

    def save_feature_store_integration_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/validation/feature_store_integration_validation_report', df, summary)
    def load_feature_store_integration_validation_report(self):
        return self._load_csv('advanced_feature_store_integration/validation/feature_store_integration_validation_report.csv')

    def save_feature_store_integration_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/safety/feature_store_integration_safety_boundary', df, summary)
    def load_feature_store_integration_safety_boundary(self):
        return self._load_csv('advanced_feature_store_integration/safety/feature_store_integration_safety_boundary.csv')

    def save_phase_125_feature_factor_engine_acceptance_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_store_integration/handoff/phase_125_feature_factor_engine_acceptance_handoff_report', df, summary)
    def load_phase_125_feature_factor_engine_acceptance_handoff_report(self):
        return self._load_csv('advanced_feature_store_integration/handoff/phase_125_feature_factor_engine_acceptance_handoff_report.csv')

    def save_feature_store_integration_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_store_integration' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_feature_store_integration_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_store_integration' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_feature_store_integration_reports(self):
        return pd.DataFrame()

    # Phase 125 Feature/Factor Acceptance DataLake Support
    def save_feature_factor_acceptance_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/profiles/profile_registry', df, summary)
    def load_feature_factor_acceptance_profile_registry(self):
        return self._load_csv('advanced_feature_factor_acceptance/profiles/profile_registry.csv')

    def save_feature_factor_acceptance_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/domains/domain_registry', df, summary)
    def load_feature_factor_acceptance_domain_registry(self):
        return self._load_csv('advanced_feature_factor_acceptance/domains/domain_registry.csv')

    def save_feature_engine_block_inventory_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/inventory/inventory_report', df, summary)
    def load_feature_engine_block_inventory_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/inventory/inventory_report.csv')

    def save_feature_engine_block_dependency_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/dependencies/dependency_report', df, summary)
    def load_feature_engine_block_dependency_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/dependencies/dependency_report.csv')

    def save_feature_engine_block_acceptance_gate_registry(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/gates/acceptance_gate_registry', df, summary)
    def load_feature_engine_block_acceptance_gate_registry(self):
        return self._load_csv('advanced_feature_factor_acceptance/gates/acceptance_gate_registry.csv')

    def save_feature_engine_block_acceptance_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/scoring/acceptance_score_report', df, summary)
    def load_feature_engine_block_acceptance_score_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/scoring/acceptance_score_report.csv')

    def save_feature_engine_block_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/manual_review/manual_review_queue', df, summary)
    def load_feature_engine_block_manual_review_queue(self):
        return self._load_csv('advanced_feature_factor_acceptance/manual_review/manual_review_queue.csv')

    def save_feature_engine_block_safety_boundary_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/safety/safety_boundary_report', df, summary)
    def load_feature_engine_block_safety_boundary_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/safety/safety_boundary_report.csv')

    def save_feature_engine_block_non_signal_compliance_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/compliance/non_signal_compliance_report', df, summary)
    def load_feature_engine_block_non_signal_compliance_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/compliance/non_signal_compliance_report.csv')

    def save_feature_engine_block_no_lookahead_compliance_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/compliance/no_lookahead_compliance_report', df, summary)
    def load_feature_engine_block_no_lookahead_compliance_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/compliance/no_lookahead_compliance_report.csv')

    def save_feature_engine_block_forbidden_column_compliance_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/compliance/forbidden_column_compliance_report', df, summary)
    def load_feature_engine_block_forbidden_column_compliance_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/compliance/forbidden_column_compliance_report.csv')

    def save_feature_engine_block_news_metadata_only_compliance_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/compliance/news_metadata_only_compliance_report', df, summary)
    def load_feature_engine_block_news_metadata_only_compliance_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/compliance/news_metadata_only_compliance_report.csv')

    def save_feature_engine_block_source_preservation_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/compliance/source_preservation_report', df, summary)
    def load_feature_engine_block_source_preservation_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/compliance/source_preservation_report.csv')

    def save_feature_engine_block_feature_store_readiness_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/compliance/feature_store_readiness_report', df, summary)
    def load_feature_engine_block_feature_store_readiness_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/compliance/feature_store_readiness_report.csv')

    def save_feature_engine_block_documentation_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/documentation/documentation_report', df, summary)
    def load_feature_engine_block_documentation_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/documentation/documentation_report.csv')

    def save_feature_engine_block_script_contract_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/scripts/script_contract_report', df, summary)
    def load_feature_engine_block_script_contract_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/scripts/script_contract_report.csv')

    def save_feature_engine_block_test_contract_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/tests/test_contract_report', df, summary)
    def load_feature_engine_block_test_contract_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/tests/test_contract_report.csv')

    def save_feature_engine_block_status_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/status/block_status_report', df, summary)
    def load_feature_engine_block_status_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/status/block_status_report.csv')

    def save_phase_116_125_acceptance_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/manifest/phase_116_125_acceptance_manifest', df, summary)
    def load_phase_116_125_acceptance_manifest(self):
        return self._load_csv('advanced_feature_factor_acceptance/manifest/phase_116_125_acceptance_manifest.csv')

    def save_feature_factor_acceptance_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/health/health_check', df, summary)
    def load_feature_factor_acceptance_health_check(self):
        return self._load_csv('advanced_feature_factor_acceptance/health/health_check.csv')

    def save_feature_factor_acceptance_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/validation/validation_report', df, summary)
    def load_feature_factor_acceptance_validation_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/validation/validation_report.csv')

    def save_phase_126_regime_classification_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_feature_factor_acceptance/handoff/phase_126_regime_classification_handoff_report', df, summary)
    def load_phase_126_regime_classification_handoff_report(self):
        return self._load_csv('advanced_feature_factor_acceptance/handoff/phase_126_regime_classification_handoff_report.csv')

    def save_feature_factor_acceptance_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_factor_acceptance' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_feature_factor_acceptance_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_feature_factor_acceptance' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_feature_factor_acceptance_reports(self):
        return pd.DataFrame()

    # Phase 126 Regime Classification and Market Behavior Foundation DataLake Support
    def save_regime_foundation_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/profiles/profile_registry', df, summary)
    def load_regime_foundation_profile_registry(self):
        return self._load_csv('advanced_regime_foundation/profiles/profile_registry.csv')

    def save_regime_foundation_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/domains/domain_registry', df, summary)
    def load_regime_foundation_domain_registry(self):
        return self._load_csv('advanced_regime_foundation/domains/domain_registry.csv')

    def save_market_behavior_taxonomy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/market_behavior_taxonomy/behavior_taxonomy', df, summary)
    def load_market_behavior_taxonomy_registry(self):
        return self._load_csv('advanced_regime_foundation/market_behavior_taxonomy/behavior_taxonomy.csv')

    def save_regime_state_taxonomy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/regime_state_taxonomy/state_taxonomy', df, summary)
    def load_regime_state_taxonomy_registry(self):
        return self._load_csv('advanced_regime_foundation/regime_state_taxonomy/state_taxonomy.csv')

    def save_regime_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/regime_families/family_registry', df, summary)
    def load_regime_family_registry(self):
        return self._load_csv('advanced_regime_foundation/regime_families/family_registry.csv')

    def save_volatility_regime_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/volatility/volatility_regimes', df, summary)
    def load_volatility_regime_family_registry(self):
        return self._load_csv('advanced_regime_foundation/volatility/volatility_regimes.csv')

    def save_trend_regime_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/trend/trend_regimes', df, summary)
    def load_trend_regime_family_registry(self):
        return self._load_csv('advanced_regime_foundation/trend/trend_regimes.csv')

    def save_range_regime_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/range/range_regimes', df, summary)
    def load_range_regime_family_registry(self):
        return self._load_csv('advanced_regime_foundation/range/range_regimes.csv')

    def save_liquidity_regime_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/liquidity/liquidity_placeholders', df, summary)
    def load_liquidity_regime_placeholder_registry(self):
        return self._load_csv('advanced_regime_foundation/liquidity/liquidity_placeholders.csv')

    def save_macro_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/macro_context/macro_contexts', df, summary)
    def load_macro_regime_context_registry(self):
        return self._load_csv('advanced_regime_foundation/macro_context/macro_contexts.csv')

    def save_event_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/event_context/event_contexts', df, summary)
    def load_event_regime_context_registry(self):
        return self._load_csv('advanced_regime_foundation/event_context/event_contexts.csv')

    def save_news_metadata_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/news_metadata_context/news_metadata_contexts', df, summary)
    def load_news_metadata_regime_context_registry(self):
        return self._load_csv('advanced_regime_foundation/news_metadata_context/news_metadata_contexts.csv')

    def save_cross_asset_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/cross_asset_context/cross_asset_contexts', df, summary)
    def load_cross_asset_regime_context_registry(self):
        return self._load_csv('advanced_regime_foundation/cross_asset_context/cross_asset_contexts.csv')

    def save_regime_input_feature_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/contracts/input_contracts', df, summary)
    def load_regime_input_feature_contract_registry(self):
        return self._load_csv('advanced_regime_foundation/contracts/input_contracts.csv')

    def save_regime_factor_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/dependencies/factor_dependencies', df, summary)
    def load_regime_factor_dependency_registry(self):
        return self._load_csv('advanced_regime_foundation/dependencies/factor_dependencies.csv')

    def save_regime_validation_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/dependencies/validation_dependencies', df, summary)
    def load_regime_validation_dependency_registry(self):
        return self._load_csv('advanced_regime_foundation/dependencies/validation_dependencies.csv')

    def save_regime_quality_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/dependencies/quality_dependencies', df, summary)
    def load_regime_quality_dependency_registry(self):
        return self._load_csv('advanced_regime_foundation/dependencies/quality_dependencies.csv')

    def save_regime_state_output_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/output_schema/output_schema', df, summary)
    def load_regime_state_output_schema_registry(self):
        return self._load_csv('advanced_regime_foundation/output_schema/output_schema.csv')

    def save_regime_namespace_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/namespace/namespace_registry', df, summary)
    def load_regime_namespace_registry(self):
        return self._load_csv('advanced_regime_foundation/namespace/namespace_registry.csv')

    def save_regime_non_signal_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/non_signal/non_signal_policies', df, summary)
    def load_regime_non_signal_policy_registry(self):
        return self._load_csv('advanced_regime_foundation/non_signal/non_signal_policies.csv')

    def save_regime_forbidden_claim_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/forbidden_claims/forbidden_claims', df, summary)
    def load_regime_forbidden_claim_registry(self):
        return self._load_csv('advanced_regime_foundation/forbidden_claims/forbidden_claims.csv')

    def save_regime_foundation_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/manifest/foundation_manifest', df, summary)
    def load_regime_foundation_manifest(self):
        return self._load_csv('advanced_regime_foundation/manifest/foundation_manifest.csv')

    def save_regime_foundation_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/health/health_check', df, summary)
    def load_regime_foundation_health_check(self):
        return self._load_csv('advanced_regime_foundation/health/health_check.csv')

    def save_regime_foundation_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/validation/validation_report', df, summary)
    def load_regime_foundation_validation_report(self):
        return self._load_csv('advanced_regime_foundation/validation/validation_report.csv')

    def save_regime_foundation_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/safety/safety_boundary', df, summary)
    def load_regime_foundation_safety_boundary(self):
        return self._load_csv('advanced_regime_foundation/safety/safety_boundary.csv')

    def save_phase_127_regime_feature_matrix_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_foundation/handoff/phase_127_regime_feature_matrix_handoff_report', df, summary)
    def load_phase_127_regime_feature_matrix_handoff_report(self):
        return self._load_csv('advanced_regime_foundation/handoff/phase_127_regime_feature_matrix_handoff_report.csv')

    def save_regime_foundation_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_foundation' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_regime_foundation_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_foundation' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_regime_foundation_reports(self):
        return pd.DataFrame()

    # Phase 127 Regime Feature Matrix and State Dataset Contracts Support
    def save_regime_matrix_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/profiles/profile_registry', df, summary)
    def load_regime_matrix_profile_registry(self):
        return self._load_csv('advanced_regime_matrix/profiles/profile_registry.csv')

    def save_regime_matrix_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/domains/domain_registry', df, summary)
    def load_regime_matrix_domain_registry(self):
        return self._load_csv('advanced_regime_matrix/domains/domain_registry.csv')

    def save_regime_feature_matrix_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/feature_matrix_contracts/feature_matrix_contracts', df, summary)
    def load_regime_feature_matrix_contract_registry(self):
        return self._load_csv('advanced_regime_matrix/feature_matrix_contracts/feature_matrix_contracts.csv')

    def save_regime_state_dataset_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/state_dataset_contracts/state_dataset_contracts', df, summary)
    def load_regime_state_dataset_contract_registry(self):
        return self._load_csv('advanced_regime_matrix/state_dataset_contracts/state_dataset_contracts.csv')

    def save_regime_matrix_entity_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/entities/entity_registry', df, summary)
    def load_regime_matrix_entity_registry(self):
        return self._load_csv('advanced_regime_matrix/entities/entity_registry.csv')

    def save_regime_matrix_namespace_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/namespace/namespace_registry', df, summary)
    def load_regime_matrix_namespace_registry(self):
        return self._load_csv('advanced_regime_matrix/namespace/namespace_registry.csv')

    def save_regime_matrix_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/schema/schema_registry', df, summary)
    def load_regime_matrix_schema_registry(self):
        return self._load_csv('advanced_regime_matrix/schema/schema_registry.csv')

    def save_regime_matrix_input_feature_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/input_features/input_feature_registry', df, summary)
    def load_regime_matrix_input_feature_registry(self):
        return self._load_csv('advanced_regime_matrix/input_features/input_feature_registry.csv')

    def save_regime_matrix_factor_input_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/factor_inputs/factor_input_registry', df, summary)
    def load_regime_matrix_factor_input_registry(self):
        return self._load_csv('advanced_regime_matrix/factor_inputs/factor_input_registry.csv')

    def save_regime_matrix_context_input_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/context_inputs/context_input_registry', df, summary)
    def load_regime_matrix_context_input_registry(self):
        return self._load_csv('advanced_regime_matrix/context_inputs/context_input_registry.csv')

    def save_regime_matrix_quality_input_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/quality_inputs/quality_input_registry', df, summary)
    def load_regime_matrix_quality_input_registry(self):
        return self._load_csv('advanced_regime_matrix/quality_inputs/quality_input_registry.csv')

    def save_regime_matrix_timestamp_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/timestamp_alignment/timestamp_alignment_registry', df, summary)
    def load_regime_matrix_timestamp_alignment_registry(self):
        return self._load_csv('advanced_regime_matrix/timestamp_alignment/timestamp_alignment_registry.csv')

    def save_regime_matrix_asof_join_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/asof_join/asof_join_policy_registry', df, summary)
    def load_regime_matrix_asof_join_policy_registry(self):
        return self._load_csv('advanced_regime_matrix/asof_join/asof_join_policy_registry.csv')

    def save_regime_matrix_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/no_lookahead/no_lookahead_guard_registry', df, summary)
    def load_regime_matrix_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_regime_matrix/no_lookahead/no_lookahead_guard_registry.csv')

    def save_regime_state_dataset_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/state_dataset_schema/state_dataset_schema', df, summary)
    def load_regime_state_dataset_schema_registry(self):
        return self._load_csv('advanced_regime_matrix/state_dataset_schema/state_dataset_schema.csv')

    def save_regime_state_dataset_metadata_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/state_dataset_metadata/state_dataset_metadata', df, summary)
    def load_regime_state_dataset_metadata_registry(self):
        return self._load_csv('advanced_regime_matrix/state_dataset_metadata/state_dataset_metadata.csv')

    def save_regime_state_candidate_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/candidate_context/candidate_context_registry', df, summary)
    def load_regime_state_candidate_context_registry(self):
        return self._load_csv('advanced_regime_matrix/candidate_context/candidate_context_registry.csv')

    def save_regime_matrix_integrity_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/integrity/integrity_contracts', df, summary)
    def load_regime_matrix_integrity_contract_registry(self):
        return self._load_csv('advanced_regime_matrix/integrity/integrity_contracts.csv')

    def save_regime_matrix_integrity_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/integrity/integrity_manifest', df, summary)
    def load_regime_matrix_integrity_manifest(self):
        return self._load_csv('advanced_regime_matrix/integrity/integrity_manifest.csv')

    def save_regime_matrix_source_phase_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/source_phases/source_phase_registry', df, summary)
    def load_regime_matrix_source_phase_registry(self):
        return self._load_csv('advanced_regime_matrix/source_phases/source_phase_registry.csv')

    def save_regime_matrix_validation_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/validation_dependencies/validation_dependencies', df, summary)
    def load_regime_matrix_validation_dependency_registry(self):
        return self._load_csv('advanced_regime_matrix/validation_dependencies/validation_dependencies.csv')

    def save_regime_matrix_quality_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/quality_dependencies/quality_dependencies', df, summary)
    def load_regime_matrix_quality_dependency_registry(self):
        return self._load_csv('advanced_regime_matrix/quality_dependencies/quality_dependencies.csv')

    def save_regime_matrix_non_signal_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/non_signal/non_signal_policies', df, summary)
    def load_regime_matrix_non_signal_policy_registry(self):
        return self._load_csv('advanced_regime_matrix/non_signal/non_signal_policies.csv')

    def save_regime_matrix_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/forbidden_columns/forbidden_column_policies', df, summary)
    def load_regime_matrix_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_regime_matrix/forbidden_columns/forbidden_column_policies.csv')

    def save_regime_matrix_source_preservation_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/source_preservation/source_preservation_policies', df, summary)
    def load_regime_matrix_source_preservation_policy_registry(self):
        return self._load_csv('advanced_regime_matrix/source_preservation/source_preservation_policies.csv')

    def save_regime_matrix_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/manual_review/manual_review_queue', df, summary)
    def load_regime_matrix_manual_review_queue(self):
        return self._load_csv('advanced_regime_matrix/manual_review/manual_review_queue.csv')

    def save_regime_matrix_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/health/health_check', df, summary)
    def load_regime_matrix_health_check(self):
        return self._load_csv('advanced_regime_matrix/health/health_check.csv')

    def save_regime_matrix_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/validation/validation_report', df, summary)
    def load_regime_matrix_validation_report(self):
        return self._load_csv('advanced_regime_matrix/validation/validation_report.csv')

    def save_regime_matrix_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/safety/safety_boundary', df, summary)
    def load_regime_matrix_safety_boundary(self):
        return self._load_csv('advanced_regime_matrix/safety/safety_boundary.csv')

    def save_phase_128_rule_free_labeling_unsupervised_prep_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_matrix/handoff/phase_128_handoff', df, summary)
    def load_phase_128_rule_free_labeling_unsupervised_prep_handoff_report(self):
        return self._load_csv('advanced_regime_matrix/handoff/phase_128_handoff.csv')

    def save_regime_matrix_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_matrix' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_regime_matrix_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_matrix' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_regime_matrix_reports(self):
        return pd.DataFrame()

    # Phase 127 Aliases for script compatibility
    save_regime_feature_matrix_contracts = save_regime_feature_matrix_contract_registry
    load_regime_feature_matrix_contracts = load_regime_feature_matrix_contract_registry
    save_regime_state_dataset_contracts = save_regime_state_dataset_contract_registry
    load_regime_state_dataset_contracts = load_regime_state_dataset_contract_registry
    save_regime_matrix_entities_registry = save_regime_matrix_entity_registry
    load_regime_matrix_entities_registry = load_regime_matrix_entity_registry
    save_regime_matrix_input_features_registry = save_regime_matrix_input_feature_registry
    load_regime_matrix_input_features_registry = load_regime_matrix_input_feature_registry
    save_regime_matrix_factor_inputs_registry = save_regime_matrix_factor_input_registry
    load_regime_matrix_factor_inputs_registry = load_regime_matrix_factor_input_registry
    save_regime_matrix_context_inputs_registry = save_regime_matrix_context_input_registry
    load_regime_matrix_context_inputs_registry = load_regime_matrix_context_input_registry
    save_regime_matrix_quality_inputs_registry = save_regime_matrix_quality_input_registry
    load_regime_matrix_quality_inputs_registry = load_regime_matrix_quality_input_registry
    save_regime_matrix_asof_join_policies = save_regime_matrix_asof_join_policy_registry
    load_regime_matrix_asof_join_policies = load_regime_matrix_asof_join_policy_registry
    save_regime_matrix_integrity_contracts = save_regime_matrix_integrity_contract_registry
    load_regime_matrix_integrity_contracts = load_regime_matrix_integrity_contract_registry
    save_phase_128_handoff_registry = save_phase_128_rule_free_labeling_unsupervised_prep_handoff_report
    load_phase_128_handoff_registry = load_phase_128_rule_free_labeling_unsupervised_prep_handoff_report
    save_regime_matrix_source_phases_registry = save_regime_matrix_source_phase_registry
    load_regime_matrix_source_phases_registry = load_regime_matrix_source_phase_registry
    save_regime_matrix_validation_dependencies = save_regime_matrix_validation_dependency_registry
    load_regime_matrix_validation_dependencies = load_regime_matrix_validation_dependency_registry
    save_regime_matrix_quality_dependencies = save_regime_matrix_quality_dependency_registry
    load_regime_matrix_quality_dependencies = load_regime_matrix_quality_dependency_registry
    save_regime_matrix_non_signal_policies = save_regime_matrix_non_signal_policy_registry
    load_regime_matrix_non_signal_policies = load_regime_matrix_non_signal_policy_registry
    save_regime_matrix_forbidden_column_policies = save_regime_matrix_forbidden_column_policy_registry
    load_regime_matrix_forbidden_column_policies = load_regime_matrix_forbidden_column_policy_registry
    save_regime_matrix_source_preservation_policies = save_regime_matrix_source_preservation_policy_registry
    load_regime_matrix_source_preservation_policies = load_regime_matrix_source_preservation_policy_registry

    # Additional script aliases
    save_regime_matrix_schema = save_regime_matrix_schema_registry
    load_regime_matrix_schema = load_regime_matrix_schema_registry
    save_regime_state_dataset_schema = save_regime_state_dataset_schema_registry
    load_regime_state_dataset_schema = load_regime_state_dataset_schema_registry
    save_regime_state_dataset_metadata = save_regime_state_dataset_metadata_registry
    load_regime_state_dataset_metadata = load_regime_state_dataset_metadata_registry
    save_regime_state_candidate_contexts = save_regime_state_candidate_context_registry
    load_regime_state_candidate_contexts = load_regime_state_candidate_context_registry
    save_regime_matrix_health = save_regime_matrix_health_check
    load_regime_matrix_health = load_regime_matrix_health_check
    save_regime_matrix_validation = save_regime_matrix_validation_report
    load_regime_matrix_validation = load_regime_matrix_validation_report
    save_regime_matrix_safety = save_regime_matrix_safety_boundary
    load_regime_matrix_safety = load_regime_matrix_safety_boundary
    save_phase_128_handoff = save_phase_128_rule_free_labeling_unsupervised_prep_handoff_report
    load_phase_128_handoff = load_phase_128_rule_free_labeling_unsupervised_prep_handoff_report
    save_regime_matrix_timestamp_alignment = save_regime_matrix_timestamp_alignment_registry
    load_regime_matrix_timestamp_alignment = load_regime_matrix_timestamp_alignment_registry
    save_regime_matrix_source_phases = save_regime_matrix_source_phase_registry
    load_regime_matrix_source_phases = load_regime_matrix_source_phase_registry
    save_regime_matrix_input_features = save_regime_matrix_input_feature_registry
    load_regime_matrix_input_features = load_regime_matrix_input_feature_registry
    save_regime_matrix_factor_inputs = save_regime_matrix_factor_input_registry
    load_regime_matrix_factor_inputs = load_regime_matrix_factor_input_registry
    save_regime_matrix_context_inputs = save_regime_matrix_context_input_registry
    load_regime_matrix_context_inputs = load_regime_matrix_context_input_registry
    save_regime_matrix_quality_inputs = save_regime_matrix_quality_input_registry
    load_regime_matrix_quality_inputs = load_regime_matrix_quality_input_registry

    # Phase 128 Regime Rule-Free Labeling Contracts and Unsupervised Prep Support
    def save_regime_rule_free_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/profiles/profile_registry', df, summary)
    def load_regime_rule_free_profile_registry(self):
        return self._load_csv('advanced_regime_rule_free/profiles/profile_registry.csv')

    def save_regime_rule_free_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/domains/domain_registry', df, summary)
    def load_regime_rule_free_domain_registry(self):
        return self._load_csv('advanced_regime_rule_free/domains/domain_registry.csv')

    def save_rule_free_labeling_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/labeling_contracts/labeling_contracts', df, summary)
    def load_rule_free_labeling_contract_registry(self):
        return self._load_csv('advanced_regime_rule_free/labeling_contracts/labeling_contracts.csv')

    def save_candidate_state_assignment_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/assignment_policies/assignment_policies', df, summary)
    def load_candidate_state_assignment_policy_registry(self):
        return self._load_csv('advanced_regime_rule_free/assignment_policies/assignment_policies.csv')

    def save_candidate_state_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/candidate_state_schema/candidate_state_schema', df, summary)
    def load_candidate_state_schema_registry(self):
        return self._load_csv('advanced_regime_rule_free/candidate_state_schema/candidate_state_schema.csv')

    def save_pseudo_state_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/pseudo_state_schema/pseudo_state_schema', df, summary)
    def load_pseudo_state_schema_registry(self):
        return self._load_csv('advanced_regime_rule_free/pseudo_state_schema/pseudo_state_schema.csv')

    def save_unsupervised_prep_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/unsupervised_prep/unsupervised_prep_contracts', df, summary)
    def load_unsupervised_prep_contract_registry(self):
        return self._load_csv('advanced_regime_rule_free/unsupervised_prep/unsupervised_prep_contracts.csv')

    def save_clustering_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/clustering_inputs/clustering_input_contracts', df, summary)
    def load_clustering_input_contract_registry(self):
        return self._load_csv('advanced_regime_rule_free/clustering_inputs/clustering_input_contracts.csv')

    def save_clustering_algorithm_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/algorithm_placeholders/clustering_algorithm_placeholders', df, summary)
    def load_clustering_algorithm_placeholder_registry(self):
        return self._load_csv('advanced_regime_rule_free/algorithm_placeholders/clustering_algorithm_placeholders.csv')

    def save_distance_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/distance_metrics/distance_metric_placeholders', df, summary)
    def load_distance_metric_placeholder_registry(self):
        return self._load_csv('advanced_regime_rule_free/distance_metrics/distance_metric_placeholders.csv')

    def save_normalization_prep_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/normalization/normalization_prep_contracts', df, summary)
    def load_normalization_prep_contract_registry(self):
        return self._load_csv('advanced_regime_rule_free/normalization/normalization_prep_contracts.csv')

    def save_scaling_prep_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/scaling/scaling_prep_contracts', df, summary)
    def load_scaling_prep_contract_registry(self):
        return self._load_csv('advanced_regime_rule_free/scaling/scaling_prep_contracts.csv')

    def save_dimensionality_reduction_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/dimensionality_reduction/dimensionality_reduction_placeholders', df, summary)
    def load_dimensionality_reduction_placeholder_registry(self):
        return self._load_csv('advanced_regime_rule_free/dimensionality_reduction/dimensionality_reduction_placeholders.csv')

    def save_regime_candidate_feature_set_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/candidate_feature_sets/candidate_feature_sets', df, summary)
    def load_regime_candidate_feature_set_registry(self):
        return self._load_csv('advanced_regime_rule_free/candidate_feature_sets/candidate_feature_sets.csv')

    def save_regime_candidate_state_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/candidate_context/candidate_context', df, summary)
    def load_regime_candidate_state_context_registry(self):
        return self._load_csv('advanced_regime_rule_free/candidate_context/candidate_context.csv')

    def save_regime_candidate_state_metadata_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/candidate_metadata/candidate_metadata', df, summary)
    def load_regime_candidate_state_metadata_registry(self):
        return self._load_csv('advanced_regime_rule_free/candidate_metadata/candidate_metadata.csv')

    def save_regime_candidate_state_namespace_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/namespace/namespace_registry', df, summary)
    def load_regime_candidate_state_namespace_registry(self):
        return self._load_csv('advanced_regime_rule_free/namespace/namespace_registry.csv')

    def save_regime_candidate_state_integrity_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/integrity/integrity_contracts', df, summary)
    def load_regime_candidate_state_integrity_contract_registry(self):
        return self._load_csv('advanced_regime_rule_free/integrity/integrity_contracts.csv')

    def save_regime_candidate_state_integrity_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/integrity/integrity_manifest', df, summary)
    def load_regime_candidate_state_integrity_manifest(self):
        return self._load_csv('advanced_regime_rule_free/integrity/integrity_manifest.csv')

    def save_regime_candidate_state_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/no_lookahead/no_lookahead_guards', df, summary)
    def load_regime_candidate_state_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_regime_rule_free/no_lookahead/no_lookahead_guards.csv')

    def save_regime_candidate_state_timestamp_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/timestamp_policy/timestamp_policies', df, summary)
    def load_regime_candidate_state_timestamp_policy_registry(self):
        return self._load_csv('advanced_regime_rule_free/timestamp_policy/timestamp_policies.csv')

    def save_regime_candidate_state_quality_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/quality_dependencies/quality_dependencies', df, summary)
    def load_regime_candidate_state_quality_dependency_registry(self):
        return self._load_csv('advanced_regime_rule_free/quality_dependencies/quality_dependencies.csv')

    def save_regime_candidate_state_validation_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/validation_dependencies/validation_dependencies', df, summary)
    def load_regime_candidate_state_validation_dependency_registry(self):
        return self._load_csv('advanced_regime_rule_free/validation_dependencies/validation_dependencies.csv')

    def save_regime_candidate_state_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/manual_review/manual_review_queue', df, summary)
    def load_regime_candidate_state_manual_review_queue(self):
        return self._load_csv('advanced_regime_rule_free/manual_review/manual_review_queue.csv')

    def save_regime_rule_free_non_signal_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/non_signal/non_signal_policies', df, summary)
    def load_regime_rule_free_non_signal_policy_registry(self):
        return self._load_csv('advanced_regime_rule_free/non_signal/non_signal_policies.csv')

    def save_regime_rule_free_forbidden_claim_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/forbidden_claims/forbidden_claims', df, summary)
    def load_regime_rule_free_forbidden_claim_registry(self):
        return self._load_csv('advanced_regime_rule_free/forbidden_claims/forbidden_claims.csv')

    def save_regime_rule_free_source_preservation_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/source_preservation/source_preservation_policies', df, summary)
    def load_regime_rule_free_source_preservation_policy_registry(self):
        return self._load_csv('advanced_regime_rule_free/source_preservation/source_preservation_policies.csv')

    def save_regime_rule_free_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/health/health_check', df, summary)
    def load_regime_rule_free_health_check(self):
        return self._load_csv('advanced_regime_rule_free/health/health_check.csv')

    def save_regime_rule_free_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/validation/validation_report', df, summary)
    def load_regime_rule_free_validation_report(self):
        return self._load_csv('advanced_regime_rule_free/validation/validation_report.csv')

    def save_regime_rule_free_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/safety/safety_boundary', df, summary)
    def load_regime_rule_free_safety_boundary(self):
        return self._load_csv('advanced_regime_rule_free/safety/safety_boundary.csv')

    def save_phase_129_market_behavior_diagnostics_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_rule_free/handoff/phase_129_handoff', df, summary)
    def load_phase_129_market_behavior_diagnostics_handoff_report(self):
        return self._load_csv('advanced_regime_rule_free/handoff/phase_129_handoff.csv')

    def save_regime_rule_free_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_rule_free' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_regime_rule_free_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_rule_free' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_regime_rule_free_reports(self):
        return pd.DataFrame()

    # Phase 128 Aliases for script compatibility
    save_rule_free_labeling_contracts = save_rule_free_labeling_contract_registry
    load_rule_free_labeling_contracts = load_rule_free_labeling_contract_registry
    save_candidate_state_assignment_policies = save_candidate_state_assignment_policy_registry
    load_candidate_state_assignment_policies = load_candidate_state_assignment_policy_registry
    save_candidate_state_schema = save_candidate_state_schema_registry
    load_candidate_state_schema = load_candidate_state_schema_registry
    save_pseudo_state_schema = save_pseudo_state_schema_registry
    load_pseudo_state_schema = load_pseudo_state_schema_registry
    save_unsupervised_prep_contracts = save_unsupervised_prep_contract_registry
    load_unsupervised_prep_contracts = load_unsupervised_prep_contract_registry
    save_clustering_input_contracts = save_clustering_input_contract_registry
    load_clustering_input_contracts = load_clustering_input_contract_registry
    save_clustering_algorithm_placeholders = save_clustering_algorithm_placeholder_registry
    load_clustering_algorithm_placeholders = load_clustering_algorithm_placeholder_registry
    save_distance_metric_placeholders = save_distance_metric_placeholder_registry
    load_distance_metric_placeholders = load_distance_metric_placeholder_registry
    save_normalization_prep_contracts = save_normalization_prep_contract_registry
    load_normalization_prep_contracts = load_normalization_prep_contract_registry
    save_scaling_prep_contracts = save_scaling_prep_contract_registry
    load_scaling_prep_contracts = load_scaling_prep_contract_registry
    save_dimensionality_reduction_placeholders = save_dimensionality_reduction_placeholder_registry
    load_dimensionality_reduction_placeholders = load_dimensionality_reduction_placeholder_registry
    save_regime_candidate_feature_sets = save_regime_candidate_feature_set_registry
    load_regime_candidate_feature_sets = load_regime_candidate_feature_set_registry
    save_regime_candidate_state_context = save_regime_candidate_state_context_registry
    load_regime_candidate_state_context = load_regime_candidate_state_context_registry
    save_regime_candidate_state_metadata = save_regime_candidate_state_metadata_registry
    load_regime_candidate_state_metadata = load_regime_candidate_state_metadata_registry
    save_regime_candidate_state_namespace = save_regime_candidate_state_namespace_registry
    load_regime_candidate_state_namespace = load_regime_candidate_state_namespace_registry
    save_regime_candidate_state_integrity_contracts = save_regime_candidate_state_integrity_contract_registry
    load_regime_candidate_state_integrity_contracts = load_regime_candidate_state_integrity_contract_registry
    save_regime_candidate_state_no_lookahead_guard = save_regime_candidate_state_no_lookahead_guard_registry
    load_regime_candidate_state_no_lookahead_guard = load_regime_candidate_state_no_lookahead_guard_registry
    save_regime_candidate_state_timestamp_policies = save_regime_candidate_state_timestamp_policy_registry
    load_regime_candidate_state_timestamp_policies = load_regime_candidate_state_timestamp_policy_registry
    save_regime_candidate_state_quality_dependencies = save_regime_candidate_state_quality_dependency_registry
    load_regime_candidate_state_quality_dependencies = load_regime_candidate_state_quality_dependency_registry
    save_regime_candidate_state_validation_dependencies = save_regime_candidate_state_validation_dependency_registry
    load_regime_candidate_state_validation_dependencies = load_regime_candidate_state_validation_dependency_registry
    save_regime_candidate_state_manual_review = save_regime_candidate_state_manual_review_queue
    load_regime_candidate_state_manual_review = load_regime_candidate_state_manual_review_queue
    save_regime_rule_free_non_signal_policies = save_regime_rule_free_non_signal_policy_registry
    load_regime_rule_free_non_signal_policies = load_regime_rule_free_non_signal_policy_registry
    save_regime_rule_free_forbidden_claims = save_regime_rule_free_forbidden_claim_registry
    load_regime_rule_free_forbidden_claims = load_regime_rule_free_forbidden_claim_registry
    save_regime_rule_free_source_preservation_policies = save_regime_rule_free_source_preservation_policy_registry
    load_regime_rule_free_source_preservation_policies = load_regime_rule_free_source_preservation_policy_registry
    save_regime_rule_free_health = save_regime_rule_free_health_check
    load_regime_rule_free_health = load_regime_rule_free_health_check
    save_regime_rule_free_validation = save_regime_rule_free_validation_report
    load_regime_rule_free_validation = load_regime_rule_free_validation_report
    save_regime_rule_free_safety = save_regime_rule_free_safety_boundary
    load_regime_rule_free_safety = load_regime_rule_free_safety_boundary
    save_phase_129_handoff = save_phase_129_market_behavior_diagnostics_handoff_report
    load_phase_129_handoff = load_phase_129_market_behavior_diagnostics_handoff_report

    # =========================================================================
    # Phase 129: Advanced Market Behavior Diagnostics & Regime Quality
    # =========================================================================

    def save_market_behavior_diagnostics_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/profiles/profile_registry', df, summary)
    def load_market_behavior_diagnostics_profile_registry(self):
        return self._load_csv('advanced_market_behavior_diagnostics/profiles/profile_registry.csv')

    def save_market_behavior_diagnostics_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/domains/domain_registry', df, summary)
    def load_market_behavior_diagnostics_domain_registry(self):
        return self._load_csv('advanced_market_behavior_diagnostics/domains/domain_registry.csv')

    def save_behavior_quality_metric_registry(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/metrics/quality_metric_registry', df, summary)
    def load_behavior_quality_metric_registry(self):
        return self._load_csv('advanced_market_behavior_diagnostics/metrics/quality_metric_registry.csv')

    def save_behavior_diagnostics_metric_registry(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/metrics/diagnostics_metric_registry', df, summary)
    def load_behavior_diagnostics_metric_registry(self):
        return self._load_csv('advanced_market_behavior_diagnostics/metrics/diagnostics_metric_registry.csv')

    def save_behavior_quality_threshold_registry(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/thresholds/threshold_registry', df, summary)
    def load_behavior_quality_threshold_registry(self):
        return self._load_csv('advanced_market_behavior_diagnostics/thresholds/threshold_registry.csv')

    def save_candidate_state_quality_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/candidate_quality/candidate_state_quality', df, summary)
    def load_candidate_state_quality_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/candidate_quality/candidate_state_quality.csv')

    def save_pseudo_state_quality_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/pseudo_state_quality/pseudo_state_quality', df, summary)
    def load_pseudo_state_quality_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/pseudo_state_quality/pseudo_state_quality.csv')

    def save_candidate_state_coverage_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/coverage/candidate_state_coverage', df, summary)
    def load_candidate_state_coverage_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/coverage/candidate_state_coverage.csv')

    def save_candidate_state_consistency_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/consistency/candidate_state_consistency', df, summary)
    def load_candidate_state_consistency_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/consistency/candidate_state_consistency.csv')

    def save_candidate_state_ambiguity_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/ambiguity/candidate_state_ambiguity', df, summary)
    def load_candidate_state_ambiguity_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/ambiguity/candidate_state_ambiguity.csv')

    def save_candidate_state_stability_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/stability/candidate_state_stability', df, summary)
    def load_candidate_state_stability_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/stability/candidate_state_stability.csv')

    def save_candidate_state_missingness_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/missingness/candidate_state_missingness', df, summary)
    def load_candidate_state_missingness_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/missingness/candidate_state_missingness.csv')

    def save_candidate_state_namespace_quality_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/namespace/candidate_state_namespace_quality', df, summary)
    def load_candidate_state_namespace_quality_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/namespace/candidate_state_namespace_quality.csv')

    def save_regime_family_quality_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/regime_family_quality/regime_family_quality', df, summary)
    def load_regime_family_quality_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/regime_family_quality/regime_family_quality.csv')

    def save_regime_family_coverage_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/regime_family_coverage/regime_family_coverage', df, summary)
    def load_regime_family_coverage_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/regime_family_coverage/regime_family_coverage.csv')

    def save_regime_family_consistency_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/regime_family_consistency/regime_family_consistency', df, summary)
    def load_regime_family_consistency_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/regime_family_consistency/regime_family_consistency.csv')

    def save_volatility_behavior_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/volatility_behavior/volatility_behavior', df, summary)
    def load_volatility_behavior_diagnostics_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/volatility_behavior/volatility_behavior.csv')

    def save_trend_behavior_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/trend_behavior/trend_behavior', df, summary)
    def load_trend_behavior_diagnostics_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/trend_behavior/trend_behavior.csv')

    def save_range_behavior_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/range_behavior/range_behavior', df, summary)
    def load_range_behavior_diagnostics_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/range_behavior/range_behavior.csv')

    def save_macro_event_behavior_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/macro_event_behavior/macro_event_behavior', df, summary)
    def load_macro_event_behavior_diagnostics_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/macro_event_behavior/macro_event_behavior.csv')

    def save_news_metadata_behavior_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/news_metadata_behavior/news_metadata_behavior', df, summary)
    def load_news_metadata_behavior_diagnostics_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/news_metadata_behavior/news_metadata_behavior.csv')

    def save_cross_asset_behavior_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/cross_asset_behavior/cross_asset_behavior', df, summary)
    def load_cross_asset_behavior_diagnostics_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/cross_asset_behavior/cross_asset_behavior.csv')

    def save_behavior_transition_readiness_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/transition_readiness/transition_readiness', df, summary)
    def load_behavior_transition_readiness_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/transition_readiness/transition_readiness.csv')

    def save_behavior_stability_readiness_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/stability_readiness/stability_readiness', df, summary)
    def load_behavior_stability_readiness_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/stability_readiness/stability_readiness.csv')

    def save_regime_quality_dependency_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/dependencies/quality_dependencies', df, summary)
    def load_regime_quality_dependency_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/dependencies/quality_dependencies.csv')

    def save_behavior_quality_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/findings/findings_registry', df, summary)
    def load_behavior_quality_findings_registry(self):
        return self._load_csv('advanced_market_behavior_diagnostics/findings/findings_registry.csv')

    def save_behavior_quality_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/manual_review/manual_review_queue', df, summary)
    def load_behavior_quality_manual_review_queue(self):
        return self._load_csv('advanced_market_behavior_diagnostics/manual_review/manual_review_queue.csv')

    def save_behavior_quality_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/scoring/quality_scores', df, summary)
    def load_behavior_quality_score_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/scoring/quality_scores.csv')

    def save_behavior_diagnostics_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/manifest/behavior_diagnostics_manifest', df, summary)
    def load_behavior_diagnostics_manifest(self):
        return self._load_csv('advanced_market_behavior_diagnostics/manifest/behavior_diagnostics_manifest.csv')

    def save_market_behavior_diagnostics_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/health/health_check', df, summary)
    def load_market_behavior_diagnostics_health_check(self):
        return self._load_csv('advanced_market_behavior_diagnostics/health/health_check.csv')

    def save_market_behavior_diagnostics_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/validation/validation_report', df, summary)
    def load_market_behavior_diagnostics_validation_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/validation/validation_report.csv')

    def save_market_behavior_diagnostics_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/safety/safety_boundary', df, summary)
    def load_market_behavior_diagnostics_safety_boundary(self):
        return self._load_csv('advanced_market_behavior_diagnostics/safety/safety_boundary.csv')

    def save_phase_130_regime_transition_stability_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_market_behavior_diagnostics/handoff/phase_130_handoff', df, summary)
    def load_phase_130_regime_transition_stability_handoff_report(self):
        return self._load_csv('advanced_market_behavior_diagnostics/handoff/phase_130_handoff.csv')

    def save_market_behavior_diagnostics_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_market_behavior_diagnostics' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_market_behavior_diagnostics_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_market_behavior_diagnostics' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_market_behavior_diagnostics_reports(self):
        return pd.DataFrame()

    # Phase 129 Aliases for script and test compatibility
    save_candidate_state_quality = save_candidate_state_quality_report
    load_candidate_state_quality = load_candidate_state_quality_report
    save_pseudo_state_quality = save_pseudo_state_quality_report
    load_pseudo_state_quality = load_pseudo_state_quality_report
    save_candidate_state_coverage = save_candidate_state_coverage_report
    load_candidate_state_coverage = load_candidate_state_coverage_report
    save_candidate_state_consistency = save_candidate_state_consistency_report
    load_candidate_state_consistency = load_candidate_state_consistency_report
    save_candidate_state_ambiguity = save_candidate_state_ambiguity_report
    load_candidate_state_ambiguity = load_candidate_state_ambiguity_report
    save_candidate_state_stability = save_candidate_state_stability_report
    load_candidate_state_stability = load_candidate_state_stability_report
    save_candidate_state_missingness = save_candidate_state_missingness_report
    load_candidate_state_missingness = load_candidate_state_missingness_report
    save_candidate_state_namespace_quality = save_candidate_state_namespace_quality_report
    load_candidate_state_namespace_quality = load_candidate_state_namespace_quality_report
    save_regime_family_quality = save_regime_family_quality_report
    load_regime_family_quality = load_regime_family_quality_report
    save_regime_family_coverage = save_regime_family_coverage_report
    load_regime_family_coverage = load_regime_family_coverage_report
    save_regime_family_consistency = save_regime_family_consistency_report
    load_regime_family_consistency = load_regime_family_consistency_report
    save_volatility_behavior_diagnostics = save_volatility_behavior_diagnostics_report
    load_volatility_behavior_diagnostics = load_volatility_behavior_diagnostics_report
    save_trend_behavior_diagnostics = save_trend_behavior_diagnostics_report
    load_trend_behavior_diagnostics = load_trend_behavior_diagnostics_report
    save_range_behavior_diagnostics = save_range_behavior_diagnostics_report
    load_range_behavior_diagnostics = load_range_behavior_diagnostics_report
    save_macro_event_behavior_diagnostics = save_macro_event_behavior_diagnostics_report
    load_macro_event_behavior_diagnostics = load_macro_event_behavior_diagnostics_report
    save_news_metadata_behavior_diagnostics = save_news_metadata_behavior_diagnostics_report
    load_news_metadata_behavior_diagnostics = load_news_metadata_behavior_diagnostics_report
    save_cross_asset_behavior_diagnostics = save_cross_asset_behavior_diagnostics_report
    load_cross_asset_behavior_diagnostics = load_cross_asset_behavior_diagnostics_report
    save_behavior_transition_readiness = save_behavior_transition_readiness_report
    load_behavior_transition_readiness = load_behavior_transition_readiness_report
    save_behavior_stability_readiness = save_behavior_stability_readiness_report
    load_behavior_stability_readiness = load_behavior_stability_readiness_report
    save_regime_quality_dependencies = save_regime_quality_dependency_report
    load_regime_quality_dependencies = load_regime_quality_dependency_report
    save_behavior_quality_findings = save_behavior_quality_findings_registry
    load_behavior_quality_findings = load_behavior_quality_findings_registry
    save_behavior_quality_manual_review = save_behavior_quality_manual_review_queue
    load_behavior_quality_manual_review = load_behavior_quality_manual_review_queue
    save_behavior_quality_scores = save_behavior_quality_score_report
    load_behavior_quality_scores = load_behavior_quality_score_report
    save_market_behavior_diagnostics_health = save_market_behavior_diagnostics_health_check
    load_market_behavior_diagnostics_health = load_market_behavior_diagnostics_health_check
    save_market_behavior_diagnostics_validation = save_market_behavior_diagnostics_validation_report
    load_market_behavior_diagnostics_validation = load_market_behavior_diagnostics_validation_report
    save_market_behavior_diagnostics_safety = save_market_behavior_diagnostics_safety_boundary
    load_market_behavior_diagnostics_safety = load_market_behavior_diagnostics_safety_boundary
    save_phase_130_handoff = save_phase_130_regime_transition_stability_handoff_report
    load_phase_130_handoff = load_phase_130_regime_transition_stability_handoff_report

    # =========================================================================
    # Phase 130: Advanced Regime Transition & Stability Analysis
    # =========================================================================

    def save_regime_transition_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/profiles/profile_registry', df, summary)
    def load_regime_transition_profile_registry(self):
        return self._load_csv('advanced_regime_transition/profiles/profile_registry.csv')

    def save_regime_transition_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/domains/domain_registry', df, summary)
    def load_regime_transition_domain_registry(self):
        return self._load_csv('advanced_regime_transition/domains/domain_registry.csv')

    def save_regime_state_sequence_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/sequence_contracts/sequence_contract_registry', df, summary)
    def load_regime_state_sequence_contract_registry(self):
        return self._load_csv('advanced_regime_transition/sequence_contracts/sequence_contract_registry.csv')

    def save_candidate_state_sequence_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/sequence_schema/candidate_sequence_schema', df, summary)
    def load_candidate_state_sequence_schema_registry(self):
        return self._load_csv('advanced_regime_transition/sequence_schema/candidate_sequence_schema.csv')

    def save_pseudo_state_sequence_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/sequence_schema/pseudo_sequence_schema', df, summary)
    def load_pseudo_state_sequence_schema_registry(self):
        return self._load_csv('advanced_regime_transition/sequence_schema/pseudo_sequence_schema.csv')

    def save_regime_transition_metric_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/metrics/transition_metric_registry', df, summary)
    def load_regime_transition_metric_registry(self):
        return self._load_csv('advanced_regime_transition/metrics/transition_metric_registry.csv')

    def save_regime_stability_metric_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/metrics/stability_metric_registry', df, summary)
    def load_regime_stability_metric_registry(self):
        return self._load_csv('advanced_regime_transition/metrics/stability_metric_registry.csv')

    def save_regime_transition_threshold_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/thresholds/threshold_registry', df, summary)
    def load_regime_transition_threshold_registry(self):
        return self._load_csv('advanced_regime_transition/thresholds/threshold_registry.csv')

    def save_regime_transition_timestamp_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/timestamp_policies/timestamp_policy_registry', df, summary)
    def load_regime_transition_timestamp_policy_registry(self):
        return self._load_csv('advanced_regime_transition/timestamp_policies/timestamp_policy_registry.csv')

    def save_regime_transition_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/no_lookahead/no_lookahead_registry', df, summary)
    def load_regime_transition_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_regime_transition/no_lookahead/no_lookahead_registry.csv')

    def save_regime_transition_source_phase_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/source_phases/source_phase_registry', df, summary)
    def load_regime_transition_source_phase_registry(self):
        return self._load_csv('advanced_regime_transition/source_phases/source_phase_registry.csv')

    def save_state_persistence_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/persistence/state_persistence_diagnostics', df, summary)
    def load_state_persistence_diagnostics_report(self):
        return self._load_csv('advanced_regime_transition/persistence/state_persistence_diagnostics.csv')

    def save_state_transition_frequency_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/frequency/state_transition_frequency', df, summary)
    def load_state_transition_frequency_report(self):
        return self._load_csv('advanced_regime_transition/frequency/state_transition_frequency.csv')

    def save_state_transition_matrix_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/transition_matrix/matrix_placeholder_registry', df, summary)
    def load_state_transition_matrix_placeholder_registry(self):
        return self._load_csv('advanced_regime_transition/transition_matrix/matrix_placeholder_registry.csv')

    def save_state_transition_ambiguity_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/ambiguity/state_transition_ambiguity', df, summary)
    def load_state_transition_ambiguity_report(self):
        return self._load_csv('advanced_regime_transition/ambiguity/state_transition_ambiguity.csv')

    def save_state_transition_continuity_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/continuity/state_transition_continuity', df, summary)
    def load_state_transition_continuity_report(self):
        return self._load_csv('advanced_regime_transition/continuity/state_transition_continuity.csv')

    def save_state_transition_stability_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/stability/state_transition_stability', df, summary)
    def load_state_transition_stability_report(self):
        return self._load_csv('advanced_regime_transition/stability/state_transition_stability.csv')

    def save_volatility_transition_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/volatility_transition/volatility_transition_diagnostics', df, summary)
    def load_volatility_transition_diagnostics_report(self):
        return self._load_csv('advanced_regime_transition/volatility_transition/volatility_transition_diagnostics.csv')

    def save_trend_transition_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/trend_transition/trend_transition_diagnostics', df, summary)
    def load_trend_transition_diagnostics_report(self):
        return self._load_csv('advanced_regime_transition/trend_transition/trend_transition_diagnostics.csv')

    def save_range_transition_diagnostics_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/range_transition/range_transition_diagnostics', df, summary)
    def load_range_transition_diagnostics_report(self):
        return self._load_csv('advanced_regime_transition/range_transition/range_transition_diagnostics.csv')

    def save_macro_event_transition_context_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/macro_event_context/macro_event_transition_context', df, summary)
    def load_macro_event_transition_context_report(self):
        return self._load_csv('advanced_regime_transition/macro_event_context/macro_event_transition_context.csv')

    def save_news_metadata_transition_context_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/news_metadata_context/news_metadata_transition_context', df, summary)
    def load_news_metadata_transition_context_report(self):
        return self._load_csv('advanced_regime_transition/news_metadata_context/news_metadata_transition_context.csv')

    def save_cross_asset_transition_prep_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/cross_asset_prep/cross_asset_transition_prep', df, summary)
    def load_cross_asset_transition_prep_report(self):
        return self._load_csv('advanced_regime_transition/cross_asset_prep/cross_asset_transition_prep.csv')

    def save_transition_quality_dependency_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/quality_dependencies/quality_dependencies', df, summary)
    def load_transition_quality_dependency_report(self):
        return self._load_csv('advanced_regime_transition/quality_dependencies/quality_dependencies.csv')

    def save_transition_validation_dependency_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/validation_dependencies/validation_dependencies', df, summary)
    def load_transition_validation_dependency_report(self):
        return self._load_csv('advanced_regime_transition/validation_dependencies/validation_dependencies.csv')

    def save_transition_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/manual_review/manual_review_queue', df, summary)
    def load_transition_manual_review_queue(self):
        return self._load_csv('advanced_regime_transition/manual_review/manual_review_queue.csv')

    def save_transition_quality_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/findings/findings_registry', df, summary)
    def load_transition_quality_findings_registry(self):
        return self._load_csv('advanced_regime_transition/findings/findings_registry.csv')

    def save_transition_stability_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/scoring/stability_scores', df, summary)
    def load_transition_stability_score_report(self):
        return self._load_csv('advanced_regime_transition/scoring/stability_scores.csv')

    def save_transition_diagnostics_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/manifest/transition_diagnostics_manifest', df, summary)
    def load_transition_diagnostics_manifest(self):
        return self._load_csv('advanced_regime_transition/manifest/transition_diagnostics_manifest.csv')

    def save_regime_transition_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/health/health_check', df, summary)
    def load_regime_transition_health_check(self):
        return self._load_csv('advanced_regime_transition/health/health_check.csv')

    def save_regime_transition_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/validation/validation_report', df, summary)
    def load_regime_transition_validation_report(self):
        return self._load_csv('advanced_regime_transition/validation/validation_report.csv')

    def save_regime_transition_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/safety/safety_boundary', df, summary)
    def load_regime_transition_safety_boundary(self):
        return self._load_csv('advanced_regime_transition/safety/safety_boundary.csv')

    def save_phase_131_cross_asset_regime_context_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_transition/handoff/phase_131_handoff', df, summary)
    def load_phase_131_cross_asset_regime_context_handoff_report(self):
        return self._load_csv('advanced_regime_transition/handoff/phase_131_handoff.csv')

    def save_regime_transition_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_transition' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_regime_transition_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_transition' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_regime_transition_reports(self):
        return pd.DataFrame()

    # Phase 130 Aliases for script and test compatibility
    save_state_persistence_diagnostics = save_state_persistence_diagnostics_report
    load_state_persistence_diagnostics = load_state_persistence_diagnostics_report
    save_state_transition_frequency = save_state_transition_frequency_report
    load_state_transition_frequency = load_state_transition_frequency_report
    save_state_transition_ambiguity = save_state_transition_ambiguity_report
    load_state_transition_ambiguity = load_state_transition_ambiguity_report
    save_state_transition_continuity = save_state_transition_continuity_report
    load_state_transition_continuity = load_state_transition_continuity_report
    save_state_transition_stability = save_state_transition_stability_report
    load_state_transition_stability = load_state_transition_stability_report
    save_volatility_transition_diagnostics = save_volatility_transition_diagnostics_report
    load_volatility_transition_diagnostics = load_volatility_transition_diagnostics_report
    save_trend_transition_diagnostics = save_trend_transition_diagnostics_report
    load_trend_transition_diagnostics = load_trend_transition_diagnostics_report
    save_range_transition_diagnostics = save_range_transition_diagnostics_report
    load_range_transition_diagnostics = load_range_transition_diagnostics_report
    save_macro_event_transition_context = save_macro_event_transition_context_report
    load_macro_event_transition_context = load_macro_event_transition_context_report
    save_news_metadata_transition_context = save_news_metadata_transition_context_report
    load_news_metadata_transition_context = load_news_metadata_transition_context_report
    save_cross_asset_transition_prep = save_cross_asset_transition_prep_report
    load_cross_asset_transition_prep = load_cross_asset_transition_prep_report
    save_transition_quality_dependencies = save_transition_quality_dependency_report
    load_transition_quality_dependencies = load_transition_quality_dependency_report
    save_transition_validation_dependencies = save_transition_validation_dependency_report
    load_transition_validation_dependencies = load_transition_validation_dependency_report
    save_transition_quality_findings = save_transition_quality_findings_registry
    load_transition_quality_findings = load_transition_quality_findings_registry
    save_transition_stability_scores = save_transition_stability_score_report
    load_transition_stability_scores = load_transition_stability_score_report
    save_regime_transition_health = save_regime_transition_health_check
    load_regime_transition_health = load_regime_transition_health_check
    save_regime_transition_validation = save_regime_transition_validation_report
    load_regime_transition_validation = load_regime_transition_validation_report
    save_regime_transition_safety = save_regime_transition_safety_boundary
    load_regime_transition_safety = load_regime_transition_safety_boundary
    save_phase_131_handoff = save_phase_131_cross_asset_regime_context_handoff_report
    load_phase_131_handoff = load_phase_131_cross_asset_regime_context_handoff_report

    # Phase 131 Cross-Asset Regime Context Expansion Methods
    def save_cross_asset_regime_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/profiles/profile_registry', df, summary)
    def load_cross_asset_regime_profile_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/profiles/profile_registry.csv')

    def save_cross_asset_regime_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/domains/domain_registry', df, summary)
    def load_cross_asset_regime_domain_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/domains/domain_registry.csv')

    def save_cross_asset_regime_entity_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/entities/entity_registry', df, summary)
    def load_cross_asset_regime_entity_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/entities/entity_registry.csv')

    def save_cross_asset_regime_pair_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/pairs/pair_registry', df, summary)
    def load_cross_asset_regime_pair_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/pairs/pair_registry.csv')

    def save_cross_asset_regime_relationship_taxonomy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/relationship_taxonomy/taxonomy_registry', df, summary)
    def load_cross_asset_regime_relationship_taxonomy_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/relationship_taxonomy/taxonomy_registry.csv')

    def save_fx_commodity_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/fx_commodity/fx_commodity_registry', df, summary)
    def load_fx_commodity_regime_context_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/fx_commodity/fx_commodity_registry.csv')

    def save_fx_macro_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/fx_macro/fx_macro_registry', df, summary)
    def load_fx_macro_regime_context_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/fx_macro/fx_macro_registry.csv')

    def save_commodity_macro_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/commodity_macro/commodity_macro_registry', df, summary)
    def load_commodity_macro_regime_context_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/commodity_macro/commodity_macro_registry.csv')

    def save_macro_calendar_cross_asset_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/macro_calendar/macro_calendar_registry', df, summary)
    def load_macro_calendar_cross_asset_context_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/macro_calendar/macro_calendar_registry.csv')

    def save_calendar_news_cross_asset_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/calendar_news/calendar_news_registry', df, summary)
    def load_calendar_news_cross_asset_context_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/calendar_news/calendar_news_registry.csv')

    def save_cross_asset_transition_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/transition_alignment/transition_alignment_registry', df, summary)
    def load_cross_asset_transition_alignment_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/transition_alignment/transition_alignment_registry.csv')

    def save_cross_asset_volatility_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/volatility_linkage/volatility_linkage_registry', df, summary)
    def load_cross_asset_volatility_linkage_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/volatility_linkage/volatility_linkage_registry.csv')

    def save_cross_asset_trend_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/trend_linkage/trend_linkage_registry', df, summary)
    def load_cross_asset_trend_linkage_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/trend_linkage/trend_linkage_registry.csv')

    def save_cross_asset_range_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/range_linkage/range_linkage_registry', df, summary)
    def load_cross_asset_range_linkage_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/range_linkage/range_linkage_registry.csv')

    def save_cross_asset_divergence_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/divergence/divergence_registry', df, summary)
    def load_cross_asset_divergence_context_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/divergence/divergence_registry.csv')

    def save_cross_asset_convergence_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/convergence/convergence_registry', df, summary)
    def load_cross_asset_convergence_context_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/convergence/convergence_registry.csv')

    def save_cross_asset_correlation_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/correlation/correlation_registry', df, summary)
    def load_cross_asset_correlation_placeholder_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/correlation/correlation_registry.csv')

    def save_cross_asset_lead_lag_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/lead_lag/lead_lag_registry', df, summary)
    def load_cross_asset_lead_lag_placeholder_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/lead_lag/lead_lag_registry.csv')

    def save_cross_asset_regime_context_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/contracts/contract_registry', df, summary)
    def load_cross_asset_regime_context_contract_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/contracts/contract_registry.csv')

    def save_cross_asset_regime_timestamp_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/timestamp_policies/timestamp_policy_registry', df, summary)
    def load_cross_asset_regime_timestamp_policy_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/timestamp_policies/timestamp_policy_registry.csv')

    def save_cross_asset_regime_asof_join_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/asof_join/asof_join_policy_registry', df, summary)
    def load_cross_asset_regime_asof_join_policy_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/asof_join/asof_join_policy_registry.csv')

    def save_cross_asset_regime_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/no_lookahead/no_lookahead_guard_registry', df, summary)
    def load_cross_asset_regime_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/no_lookahead/no_lookahead_guard_registry.csv')

    def save_cross_asset_regime_validation_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/validation_dependencies/validation_dependency_registry', df, summary)
    def load_cross_asset_regime_validation_dependency_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/validation_dependencies/validation_dependency_registry.csv')

    def save_cross_asset_regime_quality_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/quality_dependencies/quality_dependency_registry', df, summary)
    def load_cross_asset_regime_quality_dependency_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/quality_dependencies/quality_dependency_registry.csv')

    def save_cross_asset_regime_source_phase_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/source_phases/source_phase_registry', df, summary)
    def load_cross_asset_regime_source_phase_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/source_phases/source_phase_registry.csv')

    def save_cross_asset_regime_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/manual_review/manual_review_queue', df, summary)
    def load_cross_asset_regime_manual_review_queue(self):
        return self._load_csv('advanced_cross_asset_regime_context/manual_review/manual_review_queue.csv')

    def save_cross_asset_regime_context_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/findings/findings_registry', df, summary)
    def load_cross_asset_regime_context_findings_registry(self):
        return self._load_csv('advanced_cross_asset_regime_context/findings/findings_registry.csv')

    def save_cross_asset_regime_context_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/scoring/context_score_report', df, summary)
    def load_cross_asset_regime_context_score_report(self):
        return self._load_csv('advanced_cross_asset_regime_context/scoring/context_score_report.csv')

    def save_cross_asset_regime_context_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/manifest/context_manifest', df, summary)
    def load_cross_asset_regime_context_manifest(self):
        return self._load_csv('advanced_cross_asset_regime_context/manifest/context_manifest.csv')

    def save_cross_asset_regime_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/health/health_check', df, summary)
    def load_cross_asset_regime_health_check(self):
        return self._load_csv('advanced_cross_asset_regime_context/health/health_check.csv')

    def save_cross_asset_regime_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/validation/validation_report', df, summary)
    def load_cross_asset_regime_validation_report(self):
        return self._load_csv('advanced_cross_asset_regime_context/validation/validation_report.csv')

    def save_cross_asset_regime_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/safety/safety_boundary', df, summary)
    def load_cross_asset_regime_safety_boundary(self):
        return self._load_csv('advanced_cross_asset_regime_context/safety/safety_boundary.csv')

    def save_phase_132_macro_event_news_regime_context_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_cross_asset_regime_context/handoff/phase_132_handoff', df, summary)
    def load_phase_132_macro_event_news_regime_context_handoff_report(self):
        return self._load_csv('advanced_cross_asset_regime_context/handoff/phase_132_handoff.csv')

    def save_cross_asset_regime_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_cross_asset_regime_context' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_cross_asset_regime_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_cross_asset_regime_context' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_cross_asset_regime_reports(self):
        return pd.DataFrame()

    # Phase 131 Aliases
    save_cross_asset_regime_health = save_cross_asset_regime_health_check
    load_cross_asset_regime_health = load_cross_asset_regime_health_check
    save_cross_asset_regime_validation = save_cross_asset_regime_validation_report
    load_cross_asset_regime_validation = load_cross_asset_regime_validation_report
    save_cross_asset_regime_safety = save_cross_asset_regime_safety_boundary
    load_cross_asset_regime_safety = load_cross_asset_regime_safety_boundary
    save_phase_132_handoff = save_phase_132_macro_event_news_regime_context_handoff_report
    load_phase_132_handoff = load_phase_132_macro_event_news_regime_context_handoff_report
    save_cross_asset_regime_findings = save_cross_asset_regime_context_findings_registry
    load_cross_asset_regime_findings = load_cross_asset_regime_context_findings_registry
    save_cross_asset_regime_score = save_cross_asset_regime_context_score_report
    load_cross_asset_regime_score = load_cross_asset_regime_context_score_report
    save_cross_asset_regime_manifest = save_cross_asset_regime_context_manifest
    load_cross_asset_regime_manifest = load_cross_asset_regime_context_manifest


