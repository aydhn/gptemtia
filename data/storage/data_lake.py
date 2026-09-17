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

    # Phase 132 Macro/Event/News Regime Context Expansion methods
    def save_macro_event_news_regime_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/profiles/profile_registry', df, summary)
    def load_macro_event_news_regime_profile_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/profiles/profile_registry.csv')

    def save_macro_event_news_regime_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/domains/domain_registry', df, summary)
    def load_macro_event_news_regime_domain_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/domains/domain_registry.csv')

    def save_macro_regime_entity_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/entities/macro_entity_registry', df, summary)
    def load_macro_regime_entity_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/entities/macro_entity_registry.csv')

    def save_event_regime_entity_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/entities/event_entity_registry', df, summary)
    def load_event_regime_entity_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/entities/event_entity_registry.csv')

    def save_news_metadata_regime_entity_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/entities/news_metadata_entity_registry', df, summary)
    def load_news_metadata_regime_entity_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/entities/news_metadata_entity_registry.csv')

    def save_macro_regime_context_taxonomy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/context_taxonomy/macro_taxonomy_registry', df, summary)
    def load_macro_regime_context_taxonomy_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/context_taxonomy/macro_taxonomy_registry.csv')

    def save_event_regime_context_taxonomy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/context_taxonomy/event_taxonomy_registry', df, summary)
    def load_event_regime_context_taxonomy_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/context_taxonomy/event_taxonomy_registry.csv')

    def save_news_metadata_regime_context_taxonomy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/context_taxonomy/news_metadata_taxonomy_registry', df, summary)
    def load_news_metadata_regime_context_taxonomy_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/context_taxonomy/news_metadata_taxonomy_registry.csv')

    def save_macro_indicator_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/macro_indicator_context/indicator_context_registry', df, summary)
    def load_macro_indicator_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/macro_indicator_context/indicator_context_registry.csv')

    def save_macro_release_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/macro_release_context/release_context_registry', df, summary)
    def load_macro_release_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/macro_release_context/release_context_registry.csv')

    def save_macro_revision_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/macro_revision_context/revision_context_registry', df, summary)
    def load_macro_revision_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/macro_revision_context/revision_context_registry.csv')

    def save_macro_surprise_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/macro_surprise/surprise_placeholder_registry', df, summary)
    def load_macro_surprise_placeholder_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/macro_surprise/surprise_placeholder_registry.csv')

    def save_calendar_event_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/calendar_event_context/calendar_event_registry', df, summary)
    def load_calendar_event_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/calendar_event_context/calendar_event_registry.csv')

    def save_event_window_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/event_window_context/event_window_registry', df, summary)
    def load_event_window_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/event_window_context/event_window_registry.csv')

    def save_pre_event_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/pre_event_context/pre_event_registry', df, summary)
    def load_pre_event_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/pre_event_context/pre_event_registry.csv')

    def save_post_event_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/post_event_context/post_event_registry', df, summary)
    def load_post_event_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/post_event_context/post_event_registry.csv')

    def save_event_importance_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/event_importance_context/event_importance_registry', df, summary)
    def load_event_importance_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/event_importance_context/event_importance_registry.csv')

    def save_release_lag_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/release_lag_context/release_lag_registry', df, summary)
    def load_release_lag_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/release_lag_context/release_lag_registry.csv')

    def save_scheduled_actual_release_alignment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/release_alignment/release_alignment_registry', df, summary)
    def load_scheduled_actual_release_alignment_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/release_alignment/release_alignment_registry.csv')

    def save_news_topic_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/news_topic_context/news_topic_registry', df, summary)
    def load_news_topic_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/news_topic_context/news_topic_registry.csv')

    def save_news_asset_tag_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/news_asset_tag_context/news_asset_tag_registry', df, summary)
    def load_news_asset_tag_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/news_asset_tag_context/news_asset_tag_registry.csv')

    def save_news_macro_tag_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/news_macro_tag_context/news_macro_tag_registry', df, summary)
    def load_news_macro_tag_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/news_macro_tag_context/news_macro_tag_registry.csv')

    def save_news_event_linkage_regime_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/news_event_linkage_context/news_event_linkage_registry', df, summary)
    def load_news_event_linkage_regime_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/news_event_linkage_context/news_event_linkage_registry.csv')

    def save_news_freshness_regime_context_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/news_freshness_context/news_freshness_registry', df, summary)
    def load_news_freshness_regime_context_placeholder_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/news_freshness_context/news_freshness_registry.csv')

    def save_metadata_only_news_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/metadata_only_boundary/boundary_registry', df, summary)
    def load_metadata_only_news_boundary_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/metadata_only_boundary/boundary_registry.csv')

    def save_macro_event_news_cross_asset_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/cross_asset_context/cross_asset_registry', df, summary)
    def load_macro_event_news_cross_asset_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/cross_asset_context/cross_asset_registry.csv')

    def save_macro_event_news_transition_context_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/transition_context/transition_registry', df, summary)
    def load_macro_event_news_transition_context_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/transition_context/transition_registry.csv')

    def save_macro_event_news_regime_context_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/contracts/contract_registry', df, summary)
    def load_macro_event_news_regime_context_contract_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/contracts/contract_registry.csv')

    def save_macro_event_news_timestamp_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/timestamp_policies/timestamp_policy_registry', df, summary)
    def load_macro_event_news_timestamp_policy_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/timestamp_policies/timestamp_policy_registry.csv')

    def save_macro_event_news_asof_join_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/asof_join/asof_join_policy_registry', df, summary)
    def load_macro_event_news_asof_join_policy_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/asof_join/asof_join_policy_registry.csv')

    def save_macro_event_news_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/no_lookahead/no_lookahead_guard_registry', df, summary)
    def load_macro_event_news_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/no_lookahead/no_lookahead_guard_registry.csv')

    def save_macro_event_news_validation_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/validation_dependencies/validation_dependency_registry', df, summary)
    def load_macro_event_news_validation_dependency_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/validation_dependencies/validation_dependency_registry.csv')

    def save_macro_event_news_quality_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/quality_dependencies/quality_dependency_registry', df, summary)
    def load_macro_event_news_quality_dependency_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/quality_dependencies/quality_dependency_registry.csv')

    def save_macro_event_news_source_phase_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/source_phases/source_phase_registry', df, summary)
    def load_macro_event_news_source_phase_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/source_phases/source_phase_registry.csv')

    def save_macro_event_news_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/manual_review/manual_review_queue', df, summary)
    def load_macro_event_news_manual_review_queue(self):
        return self._load_csv('advanced_macro_event_news_regime/manual_review/manual_review_queue.csv')

    def save_macro_event_news_context_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/findings/findings_registry', df, summary)
    def load_macro_event_news_context_findings_registry(self):
        return self._load_csv('advanced_macro_event_news_regime/findings/findings_registry.csv')

    def save_macro_event_news_context_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/scoring/context_score_report', df, summary)
    def load_macro_event_news_context_score_report(self):
        return self._load_csv('advanced_macro_event_news_regime/scoring/context_score_report.csv')

    def save_macro_event_news_regime_context_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/manifest/context_manifest', df, summary)
    def load_macro_event_news_regime_context_manifest(self):
        return self._load_csv('advanced_macro_event_news_regime/manifest/context_manifest.csv')

    def save_macro_event_news_regime_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/health/health_check', df, summary)
    def load_macro_event_news_regime_health_check(self):
        return self._load_csv('advanced_macro_event_news_regime/health/health_check.csv')

    def save_macro_event_news_regime_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/validation/validation_report', df, summary)
    def load_macro_event_news_regime_validation_report(self):
        return self._load_csv('advanced_macro_event_news_regime/validation/validation_report.csv')

    def save_macro_event_news_regime_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/safety/safety_boundary', df, summary)
    def load_macro_event_news_regime_safety_boundary(self):
        return self._load_csv('advanced_macro_event_news_regime/safety/safety_boundary.csv')

    def save_phase_133_regime_validation_no_lookahead_acceptance_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_macro_event_news_regime/handoff/phase_133_handoff', df, summary)
    def load_phase_133_regime_validation_no_lookahead_acceptance_handoff_report(self):
        return self._load_csv('advanced_macro_event_news_regime/handoff/phase_133_handoff.csv')

    def save_macro_event_news_regime_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_macro_event_news_regime' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_macro_event_news_regime_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_macro_event_news_regime' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_macro_event_news_regime_reports(self):
        return pd.DataFrame()

    # Phase 132 Aliases
    save_macro_event_news_regime_health = save_macro_event_news_regime_health_check
    load_macro_event_news_regime_health = load_macro_event_news_regime_health_check
    save_macro_event_news_regime_validation = save_macro_event_news_regime_validation_report
    load_macro_event_news_regime_validation = load_macro_event_news_regime_validation_report
    save_macro_event_news_regime_safety = save_macro_event_news_regime_safety_boundary
    load_macro_event_news_regime_safety = load_macro_event_news_regime_safety_boundary
    save_phase_133_handoff = save_phase_133_regime_validation_no_lookahead_acceptance_handoff_report
    load_phase_133_handoff = load_phase_133_regime_validation_no_lookahead_acceptance_handoff_report
    save_macro_event_news_regime_findings = save_macro_event_news_context_findings_registry
    load_macro_event_news_regime_findings = load_macro_event_news_context_findings_registry
    save_macro_event_news_regime_score = save_macro_event_news_context_score_report
    load_macro_event_news_regime_score = load_macro_event_news_context_score_report
    save_macro_event_news_regime_manifest = save_macro_event_news_regime_context_manifest
    load_macro_event_news_regime_manifest = load_macro_event_news_regime_context_manifest

    # =========================================================================
    # Phase 133: Advanced Regime Validation & No-Lookahead Acceptance DataLake API
    # =========================================================================

    def save_regime_validation_acceptance_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/profiles/profile_registry', df, summary)
    def load_regime_validation_acceptance_profile_registry(self):
        return self._load_csv('advanced_regime_validation_acceptance/profiles/profile_registry.csv')

    def save_regime_validation_acceptance_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/domains/domain_registry', df, summary)
    def load_regime_validation_acceptance_domain_registry(self):
        return self._load_csv('advanced_regime_validation_acceptance/domains/domain_registry.csv')

    def save_regime_validation_gate_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/gates/gate_registry', df, summary)
    def load_regime_validation_gate_registry(self):
        return self._load_csv('advanced_regime_validation_acceptance/gates/gate_registry.csv')

    def save_regime_no_lookahead_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/no_lookahead/no_lookahead_report', df, summary)
    def load_regime_no_lookahead_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/no_lookahead/no_lookahead_report.csv')

    def save_regime_timestamp_order_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/timestamp_order/timestamp_order_report', df, summary)
    def load_regime_timestamp_order_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/timestamp_order/timestamp_order_report.csv')

    def save_regime_backward_asof_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/backward_asof/backward_asof_report', df, summary)
    def load_regime_backward_asof_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/backward_asof/backward_asof_report.csv')

    def save_regime_forbidden_column_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/forbidden_columns/forbidden_columns_report', df, summary)
    def load_regime_forbidden_column_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/forbidden_columns/forbidden_columns_report.csv')

    def save_regime_metadata_only_news_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/metadata_only_news/metadata_only_news_report', df, summary)
    def load_regime_metadata_only_news_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/metadata_only_news/metadata_only_news_report.csv')

    def save_regime_source_preservation_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/source_preservation/source_preservation_report', df, summary)
    def load_regime_source_preservation_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/source_preservation/source_preservation_report.csv')

    def save_regime_non_signal_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/non_signal/non_signal_report', df, summary)
    def load_regime_non_signal_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/non_signal/non_signal_report.csv')

    def save_regime_target_label_prediction_absence_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/target_label_prediction_absence/target_label_absence_report', df, summary)
    def load_regime_target_label_prediction_absence_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/target_label_prediction_absence/target_label_absence_report.csv')

    def save_regime_model_execution_absence_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/model_execution_absence/model_execution_absence_report', df, summary)
    def load_regime_model_execution_absence_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/model_execution_absence/model_execution_absence_report.csv')

    def save_regime_matrix_validation_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/matrix_acceptance/matrix_acceptance_report', df, summary)
    def load_regime_matrix_validation_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/matrix_acceptance/matrix_acceptance_report.csv')

    def save_candidate_state_validation_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/candidate_state_acceptance/candidate_state_acceptance_report', df, summary)
    def load_candidate_state_validation_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/candidate_state_acceptance/candidate_state_acceptance_report.csv')

    def save_pseudo_state_validation_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/pseudo_state_acceptance/pseudo_state_acceptance_report', df, summary)
    def load_pseudo_state_validation_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/pseudo_state_acceptance/pseudo_state_acceptance_report.csv')

    def save_transition_validation_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/transition_acceptance/transition_acceptance_report', df, summary)
    def load_transition_validation_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/transition_acceptance/transition_acceptance_report.csv')

    def save_cross_asset_regime_validation_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/cross_asset_acceptance/cross_asset_acceptance_report', df, summary)
    def load_cross_asset_regime_validation_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/cross_asset_acceptance/cross_asset_acceptance_report.csv')

    def save_macro_event_news_validation_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/macro_event_news_acceptance/macro_event_news_acceptance_report', df, summary)
    def load_macro_event_news_validation_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/macro_event_news_acceptance/macro_event_news_acceptance_report.csv')

    def save_regime_validation_dependency_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/validation_dependencies/validation_dependencies_report', df, summary)
    def load_regime_validation_dependency_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/validation_dependencies/validation_dependencies_report.csv')

    def save_regime_quality_dependency_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/quality_dependencies/quality_dependencies_report', df, summary)
    def load_regime_quality_dependency_acceptance_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/quality_dependencies/quality_dependencies_report.csv')

    def save_regime_manual_review_acceptance_queue(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/manual_review/manual_review_queue', df, summary)
    def load_regime_manual_review_acceptance_queue(self):
        return self._load_csv('advanced_regime_validation_acceptance/manual_review/manual_review_queue.csv')

    def save_regime_validation_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/findings/findings_registry', df, summary)
    def load_regime_validation_findings_registry(self):
        return self._load_csv('advanced_regime_validation_acceptance/findings/findings_registry.csv')

    def save_regime_acceptance_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/scoring/acceptance_score_report', df, summary)
    def load_regime_acceptance_score_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/scoring/acceptance_score_report.csv')

    def save_regime_validation_acceptance_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/manifest/acceptance_manifest', df, summary)
    def load_regime_validation_acceptance_manifest(self):
        return self._load_csv('advanced_regime_validation_acceptance/manifest/acceptance_manifest.csv')

    def save_regime_validation_acceptance_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/health/health_check', df, summary)
    def load_regime_validation_acceptance_health_check(self):
        return self._load_csv('advanced_regime_validation_acceptance/health/health_check.csv')

    def save_regime_validation_acceptance_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/validation/validation_report', df, summary)
    def load_regime_validation_acceptance_validation_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/validation/validation_report.csv')

    def save_regime_validation_acceptance_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/safety/safety_boundary', df, summary)
    def load_regime_validation_acceptance_safety_boundary(self):
        return self._load_csv('advanced_regime_validation_acceptance/safety/safety_boundary.csv')

    def save_phase_134_regime_featurestore_integration_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_validation_acceptance/handoff/phase_134_handoff', df, summary)
    def load_phase_134_regime_featurestore_integration_handoff_report(self):
        return self._load_csv('advanced_regime_validation_acceptance/handoff/phase_134_handoff.csv')

    def save_regime_validation_acceptance_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_validation_acceptance' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_regime_validation_acceptance_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_validation_acceptance' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_regime_validation_acceptance_reports(self):
        return pd.DataFrame()

    # Phase 133 Aliases
    save_regime_validation_acceptance_health = save_regime_validation_acceptance_health_check
    load_regime_validation_acceptance_health = load_regime_validation_acceptance_health_check
    save_regime_validation_acceptance_validation = save_regime_validation_acceptance_validation_report
    load_regime_validation_acceptance_validation = load_regime_validation_acceptance_validation_report
    save_regime_validation_acceptance_safety = save_regime_validation_acceptance_safety_boundary
    load_regime_validation_acceptance_safety = load_regime_validation_acceptance_safety_boundary
    save_phase_134_handoff = save_phase_134_regime_featurestore_integration_handoff_report
    load_phase_134_handoff = load_phase_134_regime_featurestore_integration_handoff_report
    save_regime_validation_findings = save_regime_validation_findings_registry
    load_regime_validation_findings = load_regime_validation_findings_registry
    save_regime_acceptance_score = save_regime_acceptance_score_report
    load_regime_acceptance_score = load_regime_acceptance_score_report
    save_regime_validation_manifest = save_regime_validation_acceptance_manifest
    load_regime_validation_manifest = load_regime_validation_acceptance_manifest

    # Phase 134 Regime FeatureStore Integration DataLake Support
    def save_regime_featurestore_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/profiles/profile_registry', df, summary)
    def load_regime_featurestore_profile_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/profiles/profile_registry.csv')

    def save_regime_featurestore_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/domains/domain_registry', df, summary)
    def load_regime_featurestore_domain_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/domains/domain_registry.csv')

    def save_regime_featurestore_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/contracts/contract_registry', df, summary)
    def load_regime_featurestore_contract_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/contracts/contract_registry.csv')

    def save_regime_featurestore_entity_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/entities/entity_registry', df, summary)
    def load_regime_featurestore_entity_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/entities/entity_registry.csv')

    def save_regime_featurestore_namespace_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/namespace/namespace_registry', df, summary)
    def load_regime_featurestore_namespace_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/namespace/namespace_registry.csv')

    def save_regime_featurestore_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/schema/schema_registry', df, summary)
    def load_regime_featurestore_schema_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/schema/schema_registry.csv')

    def save_regime_featurestore_version_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/version_policy/version_policy_registry', df, summary)
    def load_regime_featurestore_version_policy_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/version_policy/version_policy_registry.csv')

    def save_regime_featurestore_partition_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/partition_policy/partition_policy_registry', df, summary)
    def load_regime_featurestore_partition_policy_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/partition_policy/partition_policy_registry.csv')

    def save_regime_taxonomy_store_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/taxonomy_catalog/taxonomy_store_catalog', df, summary)
    def load_regime_taxonomy_store_catalog(self):
        return self._load_csv('advanced_regime_featurestore_integration/taxonomy_catalog/taxonomy_store_catalog.csv')

    def save_regime_matrix_store_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/matrix_catalog/matrix_store_catalog', df, summary)
    def load_regime_matrix_store_catalog(self):
        return self._load_csv('advanced_regime_featurestore_integration/matrix_catalog/matrix_store_catalog.csv')

    def save_candidate_state_store_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/candidate_state_catalog/candidate_state_store_catalog', df, summary)
    def load_candidate_state_store_catalog(self):
        return self._load_csv('advanced_regime_featurestore_integration/candidate_state_catalog/candidate_state_store_catalog.csv')

    def save_pseudo_state_store_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/pseudo_state_catalog/pseudo_state_store_catalog', df, summary)
    def load_pseudo_state_store_catalog(self):
        return self._load_csv('advanced_regime_featurestore_integration/pseudo_state_catalog/pseudo_state_store_catalog.csv')

    def save_transition_store_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/transition_catalog/transition_store_catalog', df, summary)
    def load_transition_store_catalog(self):
        return self._load_csv('advanced_regime_featurestore_integration/transition_catalog/transition_store_catalog.csv')

    def save_cross_asset_regime_store_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/cross_asset_catalog/cross_asset_regime_store_catalog', df, summary)
    def load_cross_asset_regime_store_catalog(self):
        return self._load_csv('advanced_regime_featurestore_integration/cross_asset_catalog/cross_asset_regime_store_catalog.csv')

    def save_macro_event_news_regime_store_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/macro_event_news_catalog/macro_event_news_regime_store_catalog', df, summary)
    def load_macro_event_news_regime_store_catalog(self):
        return self._load_csv('advanced_regime_featurestore_integration/macro_event_news_catalog/macro_event_news_regime_store_catalog.csv')

    def save_regime_validation_acceptance_store_catalog(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/validation_acceptance_catalog/validation_acceptance_store_catalog', df, summary)
    def load_regime_validation_acceptance_store_catalog(self):
        return self._load_csv('advanced_regime_featurestore_integration/validation_acceptance_catalog/validation_acceptance_store_catalog.csv')

    def save_regime_no_lookahead_accepted_reference_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/accepted_references/no_lookahead_accepted_references', df, summary)
    def load_regime_no_lookahead_accepted_reference_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/accepted_references/no_lookahead_accepted_references.csv')

    def save_regime_metadata_only_news_accepted_reference_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/accepted_references/metadata_only_news_accepted_references', df, summary)
    def load_regime_metadata_only_news_accepted_reference_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/accepted_references/metadata_only_news_accepted_references.csv')

    def save_regime_source_preservation_accepted_reference_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/accepted_references/source_preservation_accepted_references', df, summary)
    def load_regime_source_preservation_accepted_reference_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/accepted_references/source_preservation_accepted_references.csv')

    def save_regime_non_signal_accepted_reference_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/accepted_references/non_signal_accepted_references', df, summary)
    def load_regime_non_signal_accepted_reference_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/accepted_references/non_signal_accepted_references.csv')

    def save_regime_quality_dependency_store_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/quality_dependencies/quality_dependencies', df, summary)
    def load_regime_quality_dependency_store_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/quality_dependencies/quality_dependencies.csv')

    def save_regime_validation_dependency_store_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/validation_dependencies/validation_dependencies', df, summary)
    def load_regime_validation_dependency_store_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/validation_dependencies/validation_dependencies.csv')

    def save_regime_lineage_reference_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/lineage/lineage_references', df, summary)
    def load_regime_lineage_reference_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/lineage/lineage_references.csv')

    def save_regime_manual_review_blocker_store_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/manual_review/manual_review_blockers', df, summary)
    def load_regime_manual_review_blocker_store_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/manual_review/manual_review_blockers.csv')

    def save_regime_featurestore_metadata_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/manifest/metadata_manifest', df, summary)
    def load_regime_featurestore_metadata_manifest(self):
        return self._load_csv('advanced_regime_featurestore_integration/manifest/metadata_manifest.csv')

    def save_regime_featurestore_read_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/read_contracts/read_contracts', df, summary)
    def load_regime_featurestore_read_contract_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/read_contracts/read_contracts.csv')

    def save_regime_featurestore_write_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/write_contracts/write_contracts', df, summary)
    def load_regime_featurestore_write_contract_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/write_contracts/write_contracts.csv')

    def save_regime_featurestore_query_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/query_contracts/query_contracts', df, summary)
    def load_regime_featurestore_query_contract_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/query_contracts/query_contracts.csv')

    def save_regime_featurestore_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/forbidden_columns/forbidden_column_policies', df, summary)
    def load_regime_featurestore_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/forbidden_columns/forbidden_column_policies.csv')

    def save_regime_featurestore_non_signal_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/non_signal/non_signal_policies', df, summary)
    def load_regime_featurestore_non_signal_policy_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/non_signal/non_signal_policies.csv')

    def save_regime_featurestore_source_preservation_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/source_preservation/source_preservation_policies', df, summary)
    def load_regime_featurestore_source_preservation_policy_registry(self):
        return self._load_csv('advanced_regime_featurestore_integration/source_preservation/source_preservation_policies.csv')

    def save_regime_featurestore_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/health/health_check', df, summary)
    def load_regime_featurestore_health_check(self):
        return self._load_csv('advanced_regime_featurestore_integration/health/health_check.csv')

    def save_regime_featurestore_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/validation/validation_report', df, summary)
    def load_regime_featurestore_validation_report(self):
        return self._load_csv('advanced_regime_featurestore_integration/validation/validation_report.csv')

    def save_regime_featurestore_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/safety/safety_boundary', df, summary)
    def load_regime_featurestore_safety_boundary(self):
        return self._load_csv('advanced_regime_featurestore_integration/safety/safety_boundary.csv')

    def save_phase_135_regime_classification_acceptance_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_featurestore_integration/handoff/phase_135_handoff', df, summary)
    def load_phase_135_regime_classification_acceptance_handoff_report(self):
        return self._load_csv('advanced_regime_featurestore_integration/handoff/phase_135_handoff.csv')

    def save_regime_featurestore_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_featurestore_integration' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_regime_featurestore_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_featurestore_integration' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_regime_featurestore_reports(self):
        return pd.DataFrame()

    # Phase 134 Aliases
    save_phase_135_handoff = save_phase_135_regime_classification_acceptance_handoff_report
    load_phase_135_handoff = load_phase_135_regime_classification_acceptance_handoff_report

    # Phase 135 Regime Classification Acceptance Report DataLake Support
    def save_regime_acceptance_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/profiles/profile_registry', df, summary)
    def load_regime_acceptance_profile_registry(self):
        return self._load_csv('advanced_regime_acceptance/profiles/profile_registry.csv')

    def save_regime_acceptance_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/domains/domain_registry', df, summary)
    def load_regime_acceptance_domain_registry(self):
        return self._load_csv('advanced_regime_acceptance/domains/domain_registry.csv')

    def save_regime_block_inventory_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/inventory/inventory_report', df, summary)
    def load_regime_block_inventory_report(self):
        return self._load_csv('advanced_regime_acceptance/inventory/inventory_report.csv')

    def save_regime_block_dependency_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/dependencies/dependency_report', df, summary)
    def load_regime_block_dependency_report(self):
        return self._load_csv('advanced_regime_acceptance/dependencies/dependency_report.csv')

    def save_regime_block_acceptance_gate_registry(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/gates/acceptance_gates', df, summary)
    def load_regime_block_acceptance_gate_registry(self):
        return self._load_csv('advanced_regime_acceptance/gates/acceptance_gates.csv')

    def save_regime_block_acceptance_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/scoring/acceptance_score', df, summary)
    def load_regime_block_acceptance_score_report(self):
        return self._load_csv('advanced_regime_acceptance/scoring/acceptance_score.csv')

    def save_regime_block_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/manual_review/manual_review_queue', df, summary)
    def load_regime_block_manual_review_queue(self):
        return self._load_csv('advanced_regime_acceptance/manual_review/manual_review_queue.csv')

    def save_regime_block_safety_boundary_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/safety/safety_boundary', df, summary)
    def load_regime_block_safety_boundary_report(self):
        return self._load_csv('advanced_regime_acceptance/safety/safety_boundary.csv')

    def save_regime_block_non_signal_compliance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/compliance/non_signal_compliance', df, summary)
    def load_regime_block_non_signal_compliance_report(self):
        return self._load_csv('advanced_regime_acceptance/compliance/non_signal_compliance.csv')

    def save_regime_block_no_lookahead_compliance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/compliance/no_lookahead_compliance', df, summary)
    def load_regime_block_no_lookahead_compliance_report(self):
        return self._load_csv('advanced_regime_acceptance/compliance/no_lookahead_compliance.csv')

    def save_regime_block_metadata_only_news_compliance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/compliance/metadata_only_news_compliance', df, summary)
    def load_regime_block_metadata_only_news_compliance_report(self):
        return self._load_csv('advanced_regime_acceptance/compliance/metadata_only_news_compliance.csv')

    def save_regime_block_forbidden_column_compliance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/compliance/forbidden_column_compliance', df, summary)
    def load_regime_block_forbidden_column_compliance_report(self):
        return self._load_csv('advanced_regime_acceptance/compliance/forbidden_column_compliance.csv')

    def save_regime_block_source_preservation_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/compliance/source_preservation', df, summary)
    def load_regime_block_source_preservation_report(self):
        return self._load_csv('advanced_regime_acceptance/compliance/source_preservation.csv')

    def save_regime_block_featurestore_readiness_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/compliance/featurestore_readiness', df, summary)
    def load_regime_block_featurestore_readiness_report(self):
        return self._load_csv('advanced_regime_acceptance/compliance/featurestore_readiness.csv')

    def save_regime_block_component_acceptance_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/component_acceptance/component_acceptance', df, summary)
    def load_regime_block_component_acceptance_report(self):
        return self._load_csv('advanced_regime_acceptance/component_acceptance/component_acceptance.csv')

    def save_regime_block_documentation_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/documentation/documentation_report', df, summary)
    def load_regime_block_documentation_report(self):
        return self._load_csv('advanced_regime_acceptance/documentation/documentation_report.csv')

    def save_regime_block_script_contract_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/scripts/script_contracts', df, summary)
    def load_regime_block_script_contract_report(self):
        return self._load_csv('advanced_regime_acceptance/scripts/script_contracts.csv')

    def save_regime_block_test_contract_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/tests/test_contracts', df, summary)
    def load_regime_block_test_contract_report(self):
        return self._load_csv('advanced_regime_acceptance/tests/test_contracts.csv')

    def save_regime_block_status_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/status/block_status', df, summary)
    def load_regime_block_status_report(self):
        return self._load_csv('advanced_regime_acceptance/status/block_status.csv')

    def save_phase_126_135_acceptance_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/manifest/acceptance_manifest', df, summary)
    def load_phase_126_135_acceptance_manifest(self):
        return self._load_csv('advanced_regime_acceptance/manifest/acceptance_manifest.csv')

    def save_regime_acceptance_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/health/health_check', df, summary)
    def load_regime_acceptance_health_check(self):
        return self._load_csv('advanced_regime_acceptance/health/health_check.csv')

    def save_regime_acceptance_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/validation/validation_report', df, summary)
    def load_regime_acceptance_validation_report(self):
        return self._load_csv('advanced_regime_acceptance/validation/validation_report.csv')

    def save_phase_136_advanced_ml_gpu_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_regime_acceptance/handoff/phase_136_handoff', df, summary)
    def load_phase_136_advanced_ml_gpu_handoff_report(self):
        return self._load_csv('advanced_regime_acceptance/handoff/phase_136_handoff.csv')

    def save_regime_acceptance_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_acceptance' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_regime_acceptance_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_regime_acceptance' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_regime_acceptance_reports(self):
        return pd.DataFrame()

    # Phase 135 Aliases
    save_phase_136_handoff = save_phase_136_advanced_ml_gpu_handoff_report
    load_phase_136_handoff = load_phase_136_advanced_ml_gpu_handoff_report

    # Phase 136 GPU Acceleration and Advanced ML Runtime Foundation Support
    def save_gpu_ml_runtime_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/profiles/profile_registry', df, summary)
    def load_gpu_ml_runtime_profile_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/profiles/profile_registry.csv')

    def save_gpu_ml_runtime_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/domains/domain_registry', df, summary)
    def load_gpu_ml_runtime_domain_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/domains/domain_registry.csv')

    def save_local_hardware_discovery_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/hardware/hardware_discovery', df, summary)
    def load_local_hardware_discovery_report(self):
        return self._load_csv('advanced_gpu_ml_runtime/hardware/hardware_discovery.csv')

    def save_gpu_capability_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/gpu_capability/gpu_capability', df, summary)
    def load_gpu_capability_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/gpu_capability/gpu_capability.csv')

    def save_cpu_capability_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/cpu_capability/cpu_capability', df, summary)
    def load_cpu_capability_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/cpu_capability/cpu_capability.csv')

    def save_memory_capability_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/memory_capability/memory_capability', df, summary)
    def load_memory_capability_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/memory_capability/memory_capability.csv')

    def save_cuda_availability_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/cuda/cuda_availability', df, summary)
    def load_cuda_availability_report(self):
        return self._load_csv('advanced_gpu_ml_runtime/cuda/cuda_availability.csv')

    def save_torch_runtime_capability_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/torch/torch_runtime_capability', df, summary)
    def load_torch_runtime_capability_report(self):
        return self._load_csv('advanced_gpu_ml_runtime/torch/torch_runtime_capability.csv')

    def save_sklearn_runtime_capability_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/sklearn/sklearn_runtime_capability', df, summary)
    def load_sklearn_runtime_capability_report(self):
        return self._load_csv('advanced_gpu_ml_runtime/sklearn/sklearn_runtime_capability.csv')

    def save_numpy_pandas_runtime_capability_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/numpy_pandas/numpy_pandas_runtime_capability', df, summary)
    def load_numpy_pandas_runtime_capability_report(self):
        return self._load_csv('advanced_gpu_ml_runtime/numpy_pandas/numpy_pandas_runtime_capability.csv')

    def save_optional_ml_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/dependencies/optional_ml_dependencies', df, summary)
    def load_optional_ml_dependency_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/dependencies/optional_ml_dependencies.csv')

    def save_accelerator_backend_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/accelerators/accelerator_backends', df, summary)
    def load_accelerator_backend_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/accelerators/accelerator_backends.csv')

    def save_ml_runtime_environment_snapshot(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/environment/environment_snapshot', df, summary)
    def load_ml_runtime_environment_snapshot(self):
        return self._load_csv('advanced_gpu_ml_runtime/environment/environment_snapshot.csv')

    def save_ml_runtime_safety_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/safety_contracts/safety_contracts', df, summary)
    def load_ml_runtime_safety_contract_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/safety_contracts/safety_contracts.csv')

    def save_ml_experiment_permission_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/permission_policies/permission_policies', df, summary)
    def load_ml_experiment_permission_policy_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/permission_policies/permission_policies.csv')

    def save_ml_training_disabled_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/training_disabled/training_disabled_policies', df, summary)
    def load_ml_training_disabled_policy_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/training_disabled/training_disabled_policies.csv')

    def save_ml_inference_disabled_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/inference_disabled/inference_disabled_policies', df, summary)
    def load_ml_inference_disabled_policy_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/inference_disabled/inference_disabled_policies.csv')

    def save_ml_target_label_disabled_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/target_label_disabled/target_label_disabled_policies', df, summary)
    def load_ml_target_label_disabled_policy_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/target_label_disabled/target_label_disabled_policies.csv')

    def save_ml_artifact_governance_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/artifact_governance/artifact_governance_placeholders', df, summary)
    def load_ml_artifact_governance_placeholder_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/artifact_governance/artifact_governance_placeholders.csv')

    def save_regime_metadata_ml_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/ml_input_contracts/regime_metadata_input_contracts', df, summary)
    def load_regime_metadata_ml_input_contract_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/ml_input_contracts/regime_metadata_input_contracts.csv')

    def save_featurestore_ml_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/ml_input_contracts/featurestore_input_contracts', df, summary)
    def load_featurestore_ml_input_contract_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/ml_input_contracts/featurestore_input_contracts.csv')

    def save_no_lookahead_ml_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/no_lookahead_input_contracts/no_lookahead_input_contracts', df, summary)
    def load_no_lookahead_ml_input_contract_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/no_lookahead_input_contracts/no_lookahead_input_contracts.csv')

    def save_metadata_only_news_ml_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/metadata_only_news_input_contracts/metadata_only_news_input_contracts', df, summary)
    def load_metadata_only_news_ml_input_contract_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/metadata_only_news_input_contracts/metadata_only_news_input_contracts.csv')

    def save_source_preservation_ml_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/source_preservation_input_contracts/source_preservation_input_contracts', df, summary)
    def load_source_preservation_ml_input_contract_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/source_preservation_input_contracts/source_preservation_input_contracts.csv')

    def save_ml_runtime_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/manual_review/manual_review_queue', df, summary)
    def load_ml_runtime_manual_review_queue(self):
        return self._load_csv('advanced_gpu_ml_runtime/manual_review/manual_review_queue.csv')

    def save_ml_runtime_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/findings/findings_registry', df, summary)
    def load_ml_runtime_findings_registry(self):
        return self._load_csv('advanced_gpu_ml_runtime/findings/findings_registry.csv')

    def save_ml_runtime_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/scoring/readiness_score', df, summary)
    def load_ml_runtime_readiness_score_report(self):
        return self._load_csv('advanced_gpu_ml_runtime/scoring/readiness_score.csv')

    def save_gpu_ml_runtime_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/manifest/manifest', df, summary)
    def load_gpu_ml_runtime_manifest(self):
        return self._load_csv('advanced_gpu_ml_runtime/manifest/manifest.csv')

    def save_gpu_ml_runtime_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/health/health_check', df, summary)
    def load_gpu_ml_runtime_health_check(self):
        return self._load_csv('advanced_gpu_ml_runtime/health/health_check.csv')

    def save_gpu_ml_runtime_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/validation/validation_report', df, summary)
    def load_gpu_ml_runtime_validation_report(self):
        return self._load_csv('advanced_gpu_ml_runtime/validation/validation_report.csv')

    def save_gpu_ml_runtime_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/safety/safety_boundary', df, summary)
    def load_gpu_ml_runtime_safety_boundary(self):
        return self._load_csv('advanced_gpu_ml_runtime/safety/safety_boundary.csv')

    def save_phase_137_advanced_ml_dataset_experiment_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_ml_runtime/handoff/phase_137_handoff', df, summary)
    def load_phase_137_advanced_ml_dataset_experiment_handoff_report(self):
        return self._load_csv('advanced_gpu_ml_runtime/handoff/phase_137_handoff.csv')

    def save_gpu_ml_runtime_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_gpu_ml_runtime' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_gpu_ml_runtime_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_gpu_ml_runtime' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_gpu_ml_runtime_reports(self):
        return pd.DataFrame()

    # Phase 136 Aliases
    save_phase_137_handoff = save_phase_137_advanced_ml_dataset_experiment_handoff_report
    load_phase_137_handoff = load_phase_137_advanced_ml_dataset_experiment_handoff_report

    # Phase 137 Advanced ML Dataset Contracts and Experiment Registry Methods
    def save_advanced_ml_dataset_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/profiles/profile_registry', df, summary)
    def load_advanced_ml_dataset_profile_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/profiles/profile_registry.csv')

    def save_advanced_ml_dataset_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/domains/domain_registry', df, summary)
    def load_advanced_ml_dataset_domain_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/domains/domain_registry.csv')

    def save_ml_dataset_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/contracts/dataset_contract_registry', df, summary)
    def load_ml_dataset_contract_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/contracts/dataset_contract_registry.csv')

    def save_ml_dataset_source_catalog_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/source_catalog/source_catalog_registry', df, summary)
    def load_ml_dataset_source_catalog_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/source_catalog/source_catalog_registry.csv')

    def save_ml_dataset_schema_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/schema/dataset_schema_registry', df, summary)
    def load_ml_dataset_schema_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/schema/dataset_schema_registry.csv')

    def save_ml_dataset_feature_namespace_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/feature_namespace/feature_namespace_registry', df, summary)
    def load_ml_dataset_feature_namespace_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/feature_namespace/feature_namespace_registry.csv')

    def save_ml_dataset_version_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/version_policies/version_policy_registry', df, summary)
    def load_ml_dataset_version_policy_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/version_policies/version_policy_registry.csv')

    def save_ml_dataset_partition_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/partition_policies/partition_policy_registry', df, summary)
    def load_ml_dataset_partition_policy_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/partition_policies/partition_policy_registry.csv')

    def save_ml_dataset_time_index_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/time_index_policies/time_index_policy_registry', df, summary)
    def load_ml_dataset_time_index_policy_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/time_index_policies/time_index_policy_registry.csv')

    def save_ml_dataset_time_series_split_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/split_policies/time_series_split_policy_registry', df, summary)
    def load_ml_dataset_time_series_split_policy_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/split_policies/time_series_split_policy_registry.csv')

    def save_ml_dataset_walk_forward_split_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/walk_forward_policies/walk_forward_split_policy_registry', df, summary)
    def load_ml_dataset_walk_forward_split_policy_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/walk_forward_policies/walk_forward_split_policy_registry.csv')

    def save_ml_dataset_purged_split_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/purged_split_placeholders/purged_split_placeholder_registry', df, summary)
    def load_ml_dataset_purged_split_placeholder_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/purged_split_placeholders/purged_split_placeholder_registry.csv')

    def save_ml_dataset_leakage_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/leakage_guards/leakage_guard_registry', df, summary)
    def load_ml_dataset_leakage_guard_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/leakage_guards/leakage_guard_registry.csv')

    def save_ml_dataset_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/no_lookahead_guards/no_lookahead_guard_registry', df, summary)
    def load_ml_dataset_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/no_lookahead_guards/no_lookahead_guard_registry.csv')

    def save_ml_dataset_metadata_only_news_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/metadata_only_news_guards/metadata_only_news_guard_registry', df, summary)
    def load_ml_dataset_metadata_only_news_guard_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/metadata_only_news_guards/metadata_only_news_guard_registry.csv')

    def save_ml_dataset_source_preservation_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/source_preservation_guards/source_preservation_guard_registry', df, summary)
    def load_ml_dataset_source_preservation_guard_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/source_preservation_guards/source_preservation_guard_registry.csv')

    def save_ml_dataset_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/forbidden_columns/forbidden_column_policy_registry', df, summary)
    def load_ml_dataset_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/forbidden_columns/forbidden_column_policy_registry.csv')

    def save_ml_dataset_target_label_disabled_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/target_label_disabled/target_label_disabled_policy_registry', df, summary)
    def load_ml_dataset_target_label_disabled_policy_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/target_label_disabled/target_label_disabled_policy_registry.csv')

    def save_ml_dataset_feature_snapshot_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/feature_snapshot_contracts/feature_snapshot_contract_registry', df, summary)
    def load_ml_dataset_feature_snapshot_contract_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/feature_snapshot_contracts/feature_snapshot_contract_registry.csv')

    def save_ml_dataset_feature_snapshot_manifest_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/feature_snapshot_manifest_placeholders/feature_snapshot_manifest_placeholder_registry', df, summary)
    def load_ml_dataset_feature_snapshot_manifest_placeholder_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/feature_snapshot_manifest_placeholders/feature_snapshot_manifest_placeholder_registry.csv')

    def save_ml_dataset_quality_gate_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/quality_gates/quality_gate_registry', df, summary)
    def load_ml_dataset_quality_gate_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/quality_gates/quality_gate_registry.csv')

    def save_ml_dataset_validation_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/validation_dependencies/validation_dependency_registry', df, summary)
    def load_ml_dataset_validation_dependency_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/validation_dependencies/validation_dependency_registry.csv')

    def save_ml_dataset_quality_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/quality_dependencies/quality_dependency_registry', df, summary)
    def load_ml_dataset_quality_dependency_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/quality_dependencies/quality_dependency_registry.csv')

    def save_ml_dataset_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/lineage/lineage_registry', df, summary)
    def load_ml_dataset_lineage_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/lineage/lineage_registry.csv')

    def save_ml_experiment_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/experiment_registry/experiment_registry', df, summary)
    def load_ml_experiment_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/experiment_registry/experiment_registry.csv')

    def save_ml_experiment_template_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/experiment_templates/experiment_template_registry', df, summary)
    def load_ml_experiment_template_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/experiment_templates/experiment_template_registry.csv')

    def save_ml_experiment_permission_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/experiment_permissions/experiment_permission_registry', df, summary)
    def load_ml_experiment_permission_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/experiment_permissions/experiment_permission_registry.csv')

    def save_ml_experiment_run_plan_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/run_plan_placeholders/run_plan_placeholder_registry', df, summary)
    def load_ml_experiment_run_plan_placeholder_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/run_plan_placeholders/run_plan_placeholder_registry.csv')

    def save_ml_model_family_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/model_family_placeholders/model_family_placeholder_registry', df, summary)
    def load_ml_model_family_placeholder_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/model_family_placeholders/model_family_placeholder_registry.csv')

    def save_ml_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/metric_placeholders/metric_placeholder_registry', df, summary)
    def load_ml_metric_placeholder_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/metric_placeholders/metric_placeholder_registry.csv')

    def save_ml_training_harness_disabled_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/training_harness_disabled/training_harness_disabled_contract_registry', df, summary)
    def load_ml_training_harness_disabled_contract_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/training_harness_disabled/training_harness_disabled_contract_registry.csv')

    def save_ml_prediction_disabled_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/prediction_disabled/prediction_disabled_contract_registry', df, summary)
    def load_ml_prediction_disabled_contract_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/prediction_disabled/prediction_disabled_contract_registry.csv')

    def save_ml_artifact_disabled_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/artifact_disabled/artifact_disabled_contract_registry', df, summary)
    def load_ml_artifact_disabled_contract_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/artifact_disabled/artifact_disabled_contract_registry.csv')

    def save_ml_dataset_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/manual_review/manual_review_queue', df, summary)
    def load_ml_dataset_manual_review_queue(self):
        return self._load_csv('advanced_ml_dataset_registry/manual_review/manual_review_queue.csv')

    def save_ml_dataset_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/findings/findings_registry', df, summary)
    def load_ml_dataset_findings_registry(self):
        return self._load_csv('advanced_ml_dataset_registry/findings/findings_registry.csv')

    def save_ml_dataset_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/scoring/readiness_score', df, summary)
    def load_ml_dataset_readiness_score_report(self):
        return self._load_csv('advanced_ml_dataset_registry/scoring/readiness_score.csv')

    def save_advanced_ml_dataset_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/manifest/manifest', df, summary)
    def load_advanced_ml_dataset_manifest(self):
        return self._load_csv('advanced_ml_dataset_registry/manifest/manifest.csv')

    def save_advanced_ml_dataset_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/health/health_check', df, summary)
    def load_advanced_ml_dataset_health_check(self):
        return self._load_csv('advanced_ml_dataset_registry/health/health_check.csv')

    def save_advanced_ml_dataset_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/validation/validation_report', df, summary)
    def load_advanced_ml_dataset_validation_report(self):
        return self._load_csv('advanced_ml_dataset_registry/validation/validation_report.csv')

    def save_advanced_ml_dataset_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/safety/safety_boundary', df, summary)
    def load_advanced_ml_dataset_safety_boundary(self):
        return self._load_csv('advanced_ml_dataset_registry/safety/safety_boundary.csv')

    def save_phase_138_baseline_ml_model_contracts_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_ml_dataset_registry/handoff/phase_138_handoff', df, summary)
    def load_phase_138_baseline_ml_model_contracts_handoff_report(self):
        return self._load_csv('advanced_ml_dataset_registry/handoff/phase_138_handoff.csv')

    def save_advanced_ml_dataset_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_ml_dataset_registry' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_advanced_ml_dataset_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_ml_dataset_registry' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_advanced_ml_dataset_reports(self):
        return pd.DataFrame()

    # Phase 137 Aliases
    save_phase_138_handoff = save_phase_138_baseline_ml_model_contracts_handoff_report
    load_phase_138_handoff = load_phase_138_baseline_ml_model_contracts_handoff_report

    # Phase 138 Baseline ML Model Contracts and Dry-Run Training Harness DataLake Support
    def save_baseline_ml_model_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/profiles/profile_registry', df, summary)
    def load_baseline_ml_model_profile_registry(self):
        return self._load_csv('advanced_baseline_ml_models/profiles/profile_registry.csv')

    def save_baseline_ml_model_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/domains/domain_registry', df, summary)
    def load_baseline_ml_model_domain_registry(self):
        return self._load_csv('advanced_baseline_ml_models/domains/domain_registry.csv')

    def save_baseline_model_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/model_families/model_family_registry', df, summary)
    def load_baseline_model_family_registry(self):
        return self._load_csv('advanced_baseline_ml_models/model_families/model_family_registry.csv')

    def save_baseline_model_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/model_contracts/model_contract_registry', df, summary)
    def load_baseline_model_contract_registry(self):
        return self._load_csv('advanced_baseline_ml_models/model_contracts/model_contract_registry.csv')

    def save_baseline_model_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/input_contracts/input_contract_registry', df, summary)
    def load_baseline_model_input_contract_registry(self):
        return self._load_csv('advanced_baseline_ml_models/input_contracts/input_contract_registry.csv')

    def save_baseline_model_output_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/output_contracts/output_contract_registry', df, summary)
    def load_baseline_model_output_contract_registry(self):
        return self._load_csv('advanced_baseline_ml_models/output_contracts/output_contract_registry.csv')

    def save_baseline_model_training_plan_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/training_plans/training_plan_registry', df, summary)
    def load_baseline_model_training_plan_registry(self):
        return self._load_csv('advanced_baseline_ml_models/training_plans/training_plan_registry.csv')

    def save_dry_run_training_harness_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/dry_run_harness_contracts/harness_contract_registry', df, summary)
    def load_dry_run_training_harness_contract_registry(self):
        return self._load_csv('advanced_baseline_ml_models/dry_run_harness_contracts/harness_contract_registry.csv')

    def save_dry_run_training_harness_interface_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/dry_run_interfaces/interface_registry', df, summary)
    def load_dry_run_training_harness_interface_registry(self):
        return self._load_csv('advanced_baseline_ml_models/dry_run_interfaces/interface_registry.csv')

    def save_dry_run_trainer_stub_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/trainer_stubs/trainer_stub_registry', df, summary)
    def load_dry_run_trainer_stub_registry(self):
        return self._load_csv('advanced_baseline_ml_models/trainer_stubs/trainer_stub_registry.csv')

    def save_dry_run_training_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/dry_run_policies/policy_registry', df, summary)
    def load_dry_run_training_policy_registry(self):
        return self._load_csv('advanced_baseline_ml_models/dry_run_policies/policy_registry.csv')

    def save_no_real_training_execution_report(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/no_real_training/no_real_training_report', df, summary)
    def load_no_real_training_execution_report(self):
        return self._load_csv('advanced_baseline_ml_models/no_real_training/no_real_training_report.csv')

    def save_no_prediction_execution_report(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/no_prediction/no_prediction_report', df, summary)
    def load_no_prediction_execution_report(self):
        return self._load_csv('advanced_baseline_ml_models/no_prediction/no_prediction_report.csv')

    def save_no_target_label_generation_report(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/no_target_label/no_target_label_report', df, summary)
    def load_no_target_label_generation_report(self):
        return self._load_csv('advanced_baseline_ml_models/no_target_label/no_target_label_report.csv')

    def save_model_artifact_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/artifact_disabled/artifact_disabled_report', df, summary)
    def load_model_artifact_disabled_report(self):
        return self._load_csv('advanced_baseline_ml_models/artifact_disabled/artifact_disabled_report.csv')

    def save_model_registry_write_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/model_registry_disabled/registry_disabled_report', df, summary)
    def load_model_registry_write_disabled_report(self):
        return self._load_csv('advanced_baseline_ml_models/model_registry_disabled/registry_disabled_report.csv')

    def save_baseline_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/metric_placeholders/metric_placeholder_registry', df, summary)
    def load_baseline_metric_placeholder_registry(self):
        return self._load_csv('advanced_baseline_ml_models/metric_placeholders/metric_placeholder_registry.csv')

    def save_baseline_evaluation_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/evaluation_placeholders/evaluation_placeholder_registry', df, summary)
    def load_baseline_evaluation_placeholder_registry(self):
        return self._load_csv('advanced_baseline_ml_models/evaluation_placeholders/evaluation_placeholder_registry.csv')

    def save_baseline_model_validation_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/validation_dependencies/validation_dependency_registry', df, summary)
    def load_baseline_model_validation_dependency_registry(self):
        return self._load_csv('advanced_baseline_ml_models/validation_dependencies/validation_dependency_registry.csv')

    def save_baseline_model_quality_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/quality_dependencies/quality_dependency_registry', df, summary)
    def load_baseline_model_quality_dependency_registry(self):
        return self._load_csv('advanced_baseline_ml_models/quality_dependencies/quality_dependency_registry.csv')

    def save_baseline_model_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/lineage/lineage_registry', df, summary)
    def load_baseline_model_lineage_registry(self):
        return self._load_csv('advanced_baseline_ml_models/lineage/lineage_registry.csv')

    def save_baseline_model_featurestore_input_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/featurestore_inputs/featurestore_input_registry', df, summary)
    def load_baseline_model_featurestore_input_registry(self):
        return self._load_csv('advanced_baseline_ml_models/featurestore_inputs/featurestore_input_registry.csv')

    def save_baseline_model_regime_input_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/regime_inputs/regime_input_registry', df, summary)
    def load_baseline_model_regime_input_registry(self):
        return self._load_csv('advanced_baseline_ml_models/regime_inputs/regime_input_registry.csv')

    def save_baseline_model_no_lookahead_input_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/no_lookahead_guards/no_lookahead_guard_registry', df, summary)
    def load_baseline_model_no_lookahead_input_guard_registry(self):
        return self._load_csv('advanced_baseline_ml_models/no_lookahead_guards/no_lookahead_guard_registry.csv')

    def save_baseline_model_metadata_only_news_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/metadata_only_news_guards/metadata_only_news_guard_registry', df, summary)
    def load_baseline_model_metadata_only_news_guard_registry(self):
        return self._load_csv('advanced_baseline_ml_models/metadata_only_news_guards/metadata_only_news_guard_registry.csv')

    def save_baseline_model_source_preservation_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/source_preservation_guards/source_preservation_guard_registry', df, summary)
    def load_baseline_model_source_preservation_guard_registry(self):
        return self._load_csv('advanced_baseline_ml_models/source_preservation_guards/source_preservation_guard_registry.csv')

    def save_baseline_model_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/forbidden_columns/forbidden_column_policy_registry', df, summary)
    def load_baseline_model_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_baseline_ml_models/forbidden_columns/forbidden_column_policy_registry.csv')

    def save_baseline_model_experiment_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/experiment_linkage/experiment_linkage_registry', df, summary)
    def load_baseline_model_experiment_linkage_registry(self):
        return self._load_csv('advanced_baseline_ml_models/experiment_linkage/experiment_linkage_registry.csv')

    def save_baseline_model_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/manual_review/manual_review_queue', df, summary)
    def load_baseline_model_manual_review_queue(self):
        return self._load_csv('advanced_baseline_ml_models/manual_review/manual_review_queue.csv')

    def save_baseline_model_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/findings/findings_registry', df, summary)
    def load_baseline_model_findings_registry(self):
        return self._load_csv('advanced_baseline_ml_models/findings/findings_registry.csv')

    def save_baseline_model_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/scoring/readiness_score', df, summary)
    def load_baseline_model_readiness_score_report(self):
        return self._load_csv('advanced_baseline_ml_models/scoring/readiness_score.csv')

    def save_baseline_ml_model_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/manifest/manifest', df, summary)
    def load_baseline_ml_model_manifest(self):
        return self._load_csv('advanced_baseline_ml_models/manifest/manifest.csv')

    def save_baseline_ml_model_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/health/health_check', df, summary)
    def load_baseline_ml_model_health_check(self):
        return self._load_csv('advanced_baseline_ml_models/health/health_check.csv')

    def save_baseline_ml_model_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/validation/validation_report', df, summary)
    def load_baseline_ml_model_validation_report(self):
        return self._load_csv('advanced_baseline_ml_models/validation/validation_report.csv')

    def save_baseline_ml_model_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/safety/safety_boundary', df, summary)
    def load_baseline_ml_model_safety_boundary(self):
        return self._load_csv('advanced_baseline_ml_models/safety/safety_boundary.csv')

    def save_phase_139_gpu_training_harness_resource_governance_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_baseline_ml_models/handoff/phase_139_handoff', df, summary)
    def load_phase_139_gpu_training_harness_resource_governance_handoff_report(self):
        return self._load_csv('advanced_baseline_ml_models/handoff/phase_139_handoff.csv')

    def save_baseline_ml_model_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_baseline_ml_models' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_baseline_ml_model_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_baseline_ml_models' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_baseline_ml_model_reports(self):
        return pd.DataFrame()

    # Phase 138 Aliases
    save_phase_139_handoff = save_phase_139_gpu_training_harness_resource_governance_handoff_report
    load_phase_139_handoff = load_phase_139_gpu_training_harness_resource_governance_handoff_report

    # =========================================================================
    # Phase 139: GPU-Accelerated Training Harness & Resource Governance
    # =========================================================================

    def save_gpu_training_governance_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/profiles/profile_registry', df, summary)
    def load_gpu_training_governance_profile_registry(self):
        return self._load_csv('advanced_gpu_training_governance/profiles/profile_registry.csv')

    def save_gpu_training_governance_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/domains/domain_registry', df, summary)
    def load_gpu_training_governance_domain_registry(self):
        return self._load_csv('advanced_gpu_training_governance/domains/domain_registry.csv')

    def save_gpu_training_resource_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/resource_policies/resource_policy_registry', df, summary)
    def load_gpu_training_resource_policy_registry(self):
        return self._load_csv('advanced_gpu_training_governance/resource_policies/resource_policy_registry.csv')

    def save_gpu_device_selection_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/device_selection/device_selection_policy_registry', df, summary)
    def load_gpu_device_selection_policy_registry(self):
        return self._load_csv('advanced_gpu_training_governance/device_selection/device_selection_policy_registry.csv')

    def save_gpu_memory_budget_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/memory_budget/memory_budget_policy_registry', df, summary)
    def load_gpu_memory_budget_policy_registry(self):
        return self._load_csv('advanced_gpu_training_governance/memory_budget/memory_budget_policy_registry.csv')

    def save_cpu_fallback_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/cpu_fallback/cpu_fallback_policy_registry', df, summary)
    def load_cpu_fallback_policy_registry(self):
        return self._load_csv('advanced_gpu_training_governance/cpu_fallback/cpu_fallback_policy_registry.csv')

    def save_training_timeout_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/timeout_policy/timeout_policy_registry', df, summary)
    def load_training_timeout_policy_registry(self):
        return self._load_csv('advanced_gpu_training_governance/timeout_policy/timeout_policy_registry.csv')

    def save_batch_size_placeholder_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/batch_size_placeholders/batch_size_placeholder_policy_registry', df, summary)
    def load_batch_size_placeholder_policy_registry(self):
        return self._load_csv('advanced_gpu_training_governance/batch_size_placeholders/batch_size_placeholder_policy_registry.csv')

    def save_dataloader_placeholder_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/dataloader_placeholders/dataloader_placeholder_policy_registry', df, summary)
    def load_dataloader_placeholder_policy_registry(self):
        return self._load_csv('advanced_gpu_training_governance/dataloader_placeholders/dataloader_placeholder_policy_registry.csv')

    def save_training_loop_stub_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/training_loop_contracts/training_loop_stub_contract_registry', df, summary)
    def load_training_loop_stub_contract_registry(self):
        return self._load_csv('advanced_gpu_training_governance/training_loop_contracts/training_loop_stub_contract_registry.csv')

    def save_gpu_training_harness_interface_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/harness_interfaces/harness_interface_registry', df, summary)
    def load_gpu_training_harness_interface_registry(self):
        return self._load_csv('advanced_gpu_training_governance/harness_interfaces/harness_interface_registry.csv')

    def save_gpu_training_harness_stub_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/harness_stubs/harness_stub_registry', df, summary)
    def load_gpu_training_harness_stub_registry(self):
        return self._load_csv('advanced_gpu_training_governance/harness_stubs/harness_stub_registry.csv')

    def save_dry_run_resource_check_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/dry_run_resource_checks/resource_check_report', df, summary)
    def load_dry_run_resource_check_report(self):
        return self._load_csv('advanced_gpu_training_governance/dry_run_resource_checks/resource_check_report.csv')

    def save_dry_run_device_selection_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/dry_run_device_selection/device_selection_report', df, summary)
    def load_dry_run_device_selection_report(self):
        return self._load_csv('advanced_gpu_training_governance/dry_run_device_selection/device_selection_report.csv')

    def save_dry_run_memory_guard_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/dry_run_memory_guards/memory_guard_report', df, summary)
    def load_dry_run_memory_guard_report(self):
        return self._load_csv('advanced_gpu_training_governance/dry_run_memory_guards/memory_guard_report.csv')

    def save_dry_run_timeout_guard_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/dry_run_timeout_guards/timeout_guard_report', df, summary)
    def load_dry_run_timeout_guard_report(self):
        return self._load_csv('advanced_gpu_training_governance/dry_run_timeout_guards/timeout_guard_report.csv')

    def save_dry_run_training_execution_block_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/execution_blocks/execution_block_report', df, summary)
    def load_dry_run_training_execution_block_report(self):
        return self._load_csv('advanced_gpu_training_governance/execution_blocks/execution_block_report.csv')

    def save_gpu_training_no_real_training_execution_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/no_real_training/no_real_training_report', df, summary)
    def load_gpu_training_no_real_training_execution_report(self):
        return self._load_csv('advanced_gpu_training_governance/no_real_training/no_real_training_report.csv')

    def save_gpu_training_no_prediction_execution_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/no_prediction/no_prediction_report', df, summary)
    def load_gpu_training_no_prediction_execution_report(self):
        return self._load_csv('advanced_gpu_training_governance/no_prediction/no_prediction_report.csv')

    def save_gpu_training_no_target_label_generation_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/no_target_label/no_target_label_report', df, summary)
    def load_gpu_training_no_target_label_generation_report(self):
        return self._load_csv('advanced_gpu_training_governance/no_target_label/no_target_label_report.csv')

    def save_no_model_artifact_persistence_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/artifact_disabled/artifact_disabled_report', df, summary)
    def load_no_model_artifact_persistence_report(self):
        return self._load_csv('advanced_gpu_training_governance/artifact_disabled/artifact_disabled_report.csv')

    def save_no_model_registry_write_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/model_registry_disabled/model_registry_disabled_report', df, summary)
    def load_no_model_registry_write_report(self):
        return self._load_csv('advanced_gpu_training_governance/model_registry_disabled/model_registry_disabled_report.csv')

    def save_gpu_training_dataset_contract_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/dataset_dependencies/dataset_dependency_registry', df, summary)
    def load_gpu_training_dataset_contract_dependency_registry(self):
        return self._load_csv('advanced_gpu_training_governance/dataset_dependencies/dataset_dependency_registry.csv')

    def save_gpu_training_baseline_model_contract_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/baseline_model_dependencies/baseline_model_dependency_registry', df, summary)
    def load_gpu_training_baseline_model_contract_dependency_registry(self):
        return self._load_csv('advanced_gpu_training_governance/baseline_model_dependencies/baseline_model_dependency_registry.csv')

    def save_gpu_training_runtime_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/runtime_dependencies/runtime_dependency_registry', df, summary)
    def load_gpu_training_runtime_dependency_registry(self):
        return self._load_csv('advanced_gpu_training_governance/runtime_dependencies/runtime_dependency_registry.csv')

    def save_gpu_training_featurestore_input_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/featurestore_inputs/featurestore_input_registry', df, summary)
    def load_gpu_training_featurestore_input_dependency_registry(self):
        return self._load_csv('advanced_gpu_training_governance/featurestore_inputs/featurestore_input_registry.csv')

    def save_gpu_training_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/no_lookahead_guards/no_lookahead_guard_registry', df, summary)
    def load_gpu_training_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_gpu_training_governance/no_lookahead_guards/no_lookahead_guard_registry.csv')

    def save_gpu_training_metadata_only_news_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/metadata_only_news_guards/metadata_only_news_guard_registry', df, summary)
    def load_gpu_training_metadata_only_news_guard_registry(self):
        return self._load_csv('advanced_gpu_training_governance/metadata_only_news_guards/metadata_only_news_guard_registry.csv')

    def save_gpu_training_source_preservation_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/source_preservation_guards/source_preservation_guard_registry', df, summary)
    def load_gpu_training_source_preservation_guard_registry(self):
        return self._load_csv('advanced_gpu_training_governance/source_preservation_guards/source_preservation_guard_registry.csv')

    def save_gpu_training_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/forbidden_columns/forbidden_column_policy_registry', df, summary)
    def load_gpu_training_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_gpu_training_governance/forbidden_columns/forbidden_column_policy_registry.csv')

    def save_gpu_training_resource_audit_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/resource_audit/resource_audit_placeholder_registry', df, summary)
    def load_gpu_training_resource_audit_placeholder_registry(self):
        return self._load_csv('advanced_gpu_training_governance/resource_audit/resource_audit_placeholder_registry.csv')

    def save_gpu_training_experiment_audit_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/experiment_audit/experiment_audit_placeholder_registry', df, summary)
    def load_gpu_training_experiment_audit_placeholder_registry(self):
        return self._load_csv('advanced_gpu_training_governance/experiment_audit/experiment_audit_placeholder_registry.csv')

    def save_gpu_training_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/manual_review/manual_review_queue', df, summary)
    def load_gpu_training_manual_review_queue(self):
        return self._load_csv('advanced_gpu_training_governance/manual_review/manual_review_queue.csv')

    def save_gpu_training_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/findings/findings_registry', df, summary)
    def load_gpu_training_findings_registry(self):
        return self._load_csv('advanced_gpu_training_governance/findings/findings_registry.csv')

    def save_gpu_training_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/scoring/readiness_score', df, summary)
    def load_gpu_training_readiness_score_report(self):
        return self._load_csv('advanced_gpu_training_governance/scoring/readiness_score.csv')

    def save_gpu_training_governance_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/manifest/manifest', df, summary)
    def load_gpu_training_governance_manifest(self):
        return self._load_csv('advanced_gpu_training_governance/manifest/manifest.csv')

    def save_gpu_training_governance_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/health/health_check', df, summary)
    def load_gpu_training_governance_health_check(self):
        return self._load_csv('advanced_gpu_training_governance/health/health_check.csv')

    def save_gpu_training_governance_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/validation/validation_report', df, summary)
    def load_gpu_training_governance_validation_report(self):
        return self._load_csv('advanced_gpu_training_governance/validation/validation_report.csv')

    def save_gpu_training_governance_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/safety/safety_boundary', df, summary)
    def load_gpu_training_governance_safety_boundary(self):
        return self._load_csv('advanced_gpu_training_governance/safety/safety_boundary.csv')

    def save_phase_140_ensemble_candidate_model_registry_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_gpu_training_governance/handoff/phase_140_handoff', df, summary)
    def load_phase_140_ensemble_candidate_model_registry_handoff_report(self):
        return self._load_csv('advanced_gpu_training_governance/handoff/phase_140_handoff.csv')

    def save_gpu_training_governance_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_gpu_training_governance' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_gpu_training_governance_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_gpu_training_governance' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_gpu_training_governance_reports(self):
        return pd.DataFrame()

    save_phase_140_handoff = save_phase_140_ensemble_candidate_model_registry_handoff_report
    load_phase_140_handoff = load_phase_140_ensemble_candidate_model_registry_handoff_report

    # Phase 140 Ensemble Model Contracts & Candidate Model Registry Data Lake Methods
    def save_ensemble_model_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/profiles/profile_registry', df, summary)
    def load_ensemble_model_profile_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/profiles/profile_registry.csv')

    def save_ensemble_model_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/domains/domain_registry', df, summary)
    def load_ensemble_model_domain_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/domains/domain_registry.csv')

    def save_candidate_model_family_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/candidate_families/candidate_family_registry', df, summary)
    def load_candidate_model_family_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/candidate_families/candidate_family_registry.csv')

    def save_candidate_model_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/candidate_contracts/candidate_contract_registry', df, summary)
    def load_candidate_model_contract_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/candidate_contracts/candidate_contract_registry.csv')

    def save_candidate_model_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/input_contracts/input_contract_registry', df, summary)
    def load_candidate_model_input_contract_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/input_contracts/input_contract_registry.csv')

    def save_candidate_model_output_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/output_contracts/output_contract_registry', df, summary)
    def load_candidate_model_output_contract_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/output_contracts/output_contract_registry.csv')

    def save_candidate_model_eligibility_gate_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/eligibility_gates/eligibility_gate_registry', df, summary)
    def load_candidate_model_eligibility_gate_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/eligibility_gates/eligibility_gate_registry.csv')

    def save_candidate_model_compatibility_matrix(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/compatibility_matrix/compatibility_matrix', df, summary)
    def load_candidate_model_compatibility_matrix(self):
        return self._load_csv('advanced_ensemble_model_registry/compatibility_matrix/compatibility_matrix.csv')

    def save_ensemble_strategy_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/strategy_contracts/strategy_contract_registry', df, summary)
    def load_ensemble_strategy_contract_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/strategy_contracts/strategy_contract_registry.csv')

    def save_ensemble_voting_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/voting_placeholders/voting_placeholder_registry', df, summary)
    def load_ensemble_voting_placeholder_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/voting_placeholders/voting_placeholder_registry.csv')

    def save_ensemble_blending_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/blending_placeholders/blending_placeholder_registry', df, summary)
    def load_ensemble_blending_placeholder_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/blending_placeholders/blending_placeholder_registry.csv')

    def save_ensemble_stacking_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/stacking_placeholders/stacking_placeholder_registry', df, summary)
    def load_ensemble_stacking_placeholder_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/stacking_placeholders/stacking_placeholder_registry.csv')

    def save_ensemble_weighting_policy_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/weighting_policies/weighting_policy_registry', df, summary)
    def load_ensemble_weighting_policy_placeholder_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/weighting_policies/weighting_policy_registry.csv')

    def save_ensemble_meta_model_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/meta_models/meta_model_registry', df, summary)
    def load_ensemble_meta_model_placeholder_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/meta_models/meta_model_registry.csv')

    def save_ensemble_selection_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/selection_policies/selection_policy_registry', df, summary)
    def load_ensemble_selection_policy_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/selection_policies/selection_policy_registry.csv')

    def save_ensemble_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/ensemble_inputs/ensemble_input_registry', df, summary)
    def load_ensemble_input_contract_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/ensemble_inputs/ensemble_input_registry.csv')

    def save_ensemble_output_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/ensemble_outputs/ensemble_output_registry', df, summary)
    def load_ensemble_output_contract_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/ensemble_outputs/ensemble_output_registry.csv')

    def save_ensemble_disabled_execution_report_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/disabled_execution/disabled_execution_registry', df, summary)
    def load_ensemble_disabled_execution_report_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/disabled_execution/disabled_execution_registry.csv')

    def save_candidate_model_training_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/disabled_execution/training_disabled_report', df, summary)
    def load_candidate_model_training_disabled_report(self):
        return self._load_csv('advanced_ensemble_model_registry/disabled_execution/training_disabled_report.csv')

    def save_candidate_model_prediction_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/disabled_execution/prediction_disabled_report', df, summary)
    def load_candidate_model_prediction_disabled_report(self):
        return self._load_csv('advanced_ensemble_model_registry/disabled_execution/prediction_disabled_report.csv')

    def save_candidate_model_target_label_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/disabled_execution/target_label_disabled_report', df, summary)
    def load_candidate_model_target_label_disabled_report(self):
        return self._load_csv('advanced_ensemble_model_registry/disabled_execution/target_label_disabled_report.csv')

    def save_candidate_model_artifact_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/disabled_execution/artifact_disabled_report', df, summary)
    def load_candidate_model_artifact_disabled_report(self):
        return self._load_csv('advanced_ensemble_model_registry/disabled_execution/artifact_disabled_report.csv')

    def save_candidate_model_registry_write_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/disabled_execution/registry_write_disabled_report', df, summary)
    def load_candidate_model_registry_write_disabled_report(self):
        return self._load_csv('advanced_ensemble_model_registry/disabled_execution/registry_write_disabled_report.csv')

    def save_ensemble_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/metric_placeholders/metric_placeholder_registry', df, summary)
    def load_ensemble_metric_placeholder_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/metric_placeholders/metric_placeholder_registry.csv')

    def save_ensemble_evaluation_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/evaluation_placeholders/evaluation_placeholder_registry', df, summary)
    def load_ensemble_evaluation_placeholder_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/evaluation_placeholders/evaluation_placeholder_registry.csv')

    def save_ensemble_validation_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/validation_dependencies/validation_dependency_registry', df, summary)
    def load_ensemble_validation_dependency_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/validation_dependencies/validation_dependency_registry.csv')

    def save_ensemble_quality_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/quality_dependencies/quality_dependency_registry', df, summary)
    def load_ensemble_quality_dependency_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/quality_dependencies/quality_dependency_registry.csv')

    def save_ensemble_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/lineage/lineage_registry', df, summary)
    def load_ensemble_lineage_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/lineage/lineage_registry.csv')

    def save_ensemble_experiment_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/experiment_linkage/experiment_linkage_registry', df, summary)
    def load_ensemble_experiment_linkage_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/experiment_linkage/experiment_linkage_registry.csv')

    def save_ensemble_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/no_lookahead_guards/no_lookahead_guard_registry', df, summary)
    def load_ensemble_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/no_lookahead_guards/no_lookahead_guard_registry.csv')

    def save_ensemble_metadata_only_news_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/metadata_only_news_guards/metadata_only_news_guard_registry', df, summary)
    def load_ensemble_metadata_only_news_guard_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/metadata_only_news_guards/metadata_only_news_guard_registry.csv')

    def save_ensemble_source_preservation_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/source_preservation_guards/source_preservation_guard_registry', df, summary)
    def load_ensemble_source_preservation_guard_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/source_preservation_guards/source_preservation_guard_registry.csv')

    def save_ensemble_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/forbidden_columns/forbidden_column_policy_registry', df, summary)
    def load_ensemble_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/forbidden_columns/forbidden_column_policy_registry.csv')

    def save_ensemble_candidate_audit_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/candidate_audit/candidate_audit_placeholder_registry', df, summary)
    def load_ensemble_candidate_audit_placeholder_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/candidate_audit/candidate_audit_placeholder_registry.csv')

    def save_ensemble_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/manual_review/manual_review_queue', df, summary)
    def load_ensemble_manual_review_queue(self):
        return self._load_csv('advanced_ensemble_model_registry/manual_review/manual_review_queue.csv')

    def save_ensemble_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/findings/findings_registry', df, summary)
    def load_ensemble_findings_registry(self):
        return self._load_csv('advanced_ensemble_model_registry/findings/findings_registry.csv')

    def save_ensemble_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/scoring/readiness_score', df, summary)
    def load_ensemble_readiness_score_report(self):
        return self._load_csv('advanced_ensemble_model_registry/scoring/readiness_score.csv')

    def save_ensemble_model_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/manifest/manifest', df, summary)
    def load_ensemble_model_manifest(self):
        return self._load_csv('advanced_ensemble_model_registry/manifest/manifest.csv')

    def save_ensemble_model_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/health/health_check', df, summary)
    def load_ensemble_model_health_check(self):
        return self._load_csv('advanced_ensemble_model_registry/health/health_check.csv')

    def save_ensemble_model_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/validation/validation_report', df, summary)
    def load_ensemble_model_validation_report(self):
        return self._load_csv('advanced_ensemble_model_registry/validation/validation_report.csv')

    def save_ensemble_model_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/safety/safety_boundary', df, summary)
    def load_ensemble_model_safety_boundary(self):
        return self._load_csv('advanced_ensemble_model_registry/safety/safety_boundary.csv')

    def save_phase_141_probability_calibration_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_ensemble_model_registry/handoff/phase_141_handoff', df, summary)
    def load_phase_141_probability_calibration_handoff_report(self):
        return self._load_csv('advanced_ensemble_model_registry/handoff/phase_141_handoff.csv')

    def save_ensemble_model_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_ensemble_model_registry' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_ensemble_model_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_ensemble_model_registry' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_ensemble_model_reports(self):
        return pd.DataFrame()

    save_phase_141_handoff = save_phase_141_probability_calibration_handoff_report
    load_phase_141_handoff = load_phase_141_probability_calibration_handoff_report

    # Phase 141 Probability Calibration and Uncertainty Estimation Contracts DataLake Support
    def save_calibration_uncertainty_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/profiles/profile_registry', df, summary)
    def load_calibration_uncertainty_profile_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/profiles/profile_registry.csv')

    def save_calibration_uncertainty_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/domains/domain_registry', df, summary)
    def load_calibration_uncertainty_domain_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/domains/domain_registry.csv')

    def save_probability_calibration_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_contracts/probability_calibration_contracts', df, summary)
    def load_probability_calibration_contract_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_contracts/probability_calibration_contracts.csv')

    def save_calibration_method_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_methods/calibration_method_placeholders', df, summary)
    def load_calibration_method_placeholder_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_methods/calibration_method_placeholders.csv')

    def save_calibration_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_input_contracts/calibration_input_contracts', df, summary)
    def load_calibration_input_contract_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_input_contracts/calibration_input_contracts.csv')

    def save_calibration_output_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_output_contracts/calibration_output_contracts', df, summary)
    def load_calibration_output_contract_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_output_contracts/calibration_output_contracts.csv')

    def save_calibration_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_execution_disabled/calibration_execution_disabled', df, summary)
    def load_calibration_execution_disabled_report(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_execution_disabled/calibration_execution_disabled.csv')

    def save_calibration_fit_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_fit_disabled/calibration_fit_disabled', df, summary)
    def load_calibration_fit_disabled_report(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_fit_disabled/calibration_fit_disabled.csv')

    def save_calibration_transform_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_transform_disabled/calibration_transform_disabled', df, summary)
    def load_calibration_transform_disabled_report(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_transform_disabled/calibration_transform_disabled.csv')

    def save_probability_prediction_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/probability_prediction_disabled/probability_prediction_disabled', df, summary)
    def load_probability_prediction_disabled_report(self):
        return self._load_csv('advanced_calibration_uncertainty/probability_prediction_disabled/probability_prediction_disabled.csv')

    def save_uncertainty_estimation_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/uncertainty_contracts/uncertainty_estimation_contracts', df, summary)
    def load_uncertainty_estimation_contract_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/uncertainty_contracts/uncertainty_estimation_contracts.csv')

    def save_uncertainty_method_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/uncertainty_methods/uncertainty_method_placeholders', df, summary)
    def load_uncertainty_method_placeholder_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/uncertainty_methods/uncertainty_method_placeholders.csv')

    def save_uncertainty_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/uncertainty_input_contracts/uncertainty_input_contracts', df, summary)
    def load_uncertainty_input_contract_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/uncertainty_input_contracts/uncertainty_input_contracts.csv')

    def save_uncertainty_output_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/uncertainty_output_contracts/uncertainty_output_contracts', df, summary)
    def load_uncertainty_output_contract_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/uncertainty_output_contracts/uncertainty_output_contracts.csv')

    def save_uncertainty_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/uncertainty_execution_disabled/uncertainty_execution_disabled', df, summary)
    def load_uncertainty_execution_disabled_report(self):
        return self._load_csv('advanced_calibration_uncertainty/uncertainty_execution_disabled/uncertainty_execution_disabled.csv')

    def save_confidence_score_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/confidence_score_placeholders/confidence_score_placeholders', df, summary)
    def load_confidence_score_placeholder_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/confidence_score_placeholders/confidence_score_placeholders.csv')

    def save_confidence_interval_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/confidence_interval_placeholders/confidence_interval_placeholders', df, summary)
    def load_confidence_interval_placeholder_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/confidence_interval_placeholders/confidence_interval_placeholders.csv')

    def save_prediction_interval_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/prediction_interval_placeholders/prediction_interval_placeholders', df, summary)
    def load_prediction_interval_placeholder_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/prediction_interval_placeholders/prediction_interval_placeholders.csv')

    def save_quantile_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/quantile_placeholders/quantile_placeholders', df, summary)
    def load_quantile_placeholder_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/quantile_placeholders/quantile_placeholders.csv')

    def save_conformal_prediction_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/conformal_prediction_placeholders/conformal_prediction_placeholders', df, summary)
    def load_conformal_prediction_placeholder_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/conformal_prediction_placeholders/conformal_prediction_placeholders.csv')

    def save_calibration_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_metric_placeholders/calibration_metric_placeholders', df, summary)
    def load_calibration_metric_placeholder_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_metric_placeholders/calibration_metric_placeholders.csv')

    def save_uncertainty_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/uncertainty_metric_placeholders/uncertainty_metric_placeholders', df, summary)
    def load_uncertainty_metric_placeholder_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/uncertainty_metric_placeholders/uncertainty_metric_placeholders.csv')

    def save_calibration_evaluation_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_evaluation_placeholders/calibration_evaluation_placeholders', df, summary)
    def load_calibration_evaluation_placeholder_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_evaluation_placeholders/calibration_evaluation_placeholders.csv')

    def save_uncertainty_evaluation_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/uncertainty_evaluation_placeholders/uncertainty_evaluation_placeholders', df, summary)
    def load_uncertainty_evaluation_placeholder_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/uncertainty_evaluation_placeholders/uncertainty_evaluation_placeholders.csv')

    def save_calibration_quality_gate_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_quality_gates/calibration_quality_gates', df, summary)
    def load_calibration_quality_gate_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_quality_gates/calibration_quality_gates.csv')

    def save_uncertainty_quality_gate_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/uncertainty_quality_gates/uncertainty_quality_gates', df, summary)
    def load_uncertainty_quality_gate_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/uncertainty_quality_gates/uncertainty_quality_gates.csv')

    def save_calibration_candidate_model_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/candidate_dependencies/candidate_dependencies', df, summary)
    def load_calibration_candidate_model_dependency_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/candidate_dependencies/candidate_dependencies.csv')

    def save_calibration_ensemble_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/ensemble_dependencies/ensemble_dependencies', df, summary)
    def load_calibration_ensemble_dependency_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/ensemble_dependencies/ensemble_dependencies.csv')

    def save_calibration_dataset_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/dataset_dependencies/dataset_dependencies', df, summary)
    def load_calibration_dataset_dependency_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/dataset_dependencies/dataset_dependencies.csv')

    def save_calibration_runtime_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/runtime_dependencies/runtime_dependencies', df, summary)
    def load_calibration_runtime_dependency_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/runtime_dependencies/runtime_dependencies.csv')

    def save_calibration_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_no_lookahead_guards/calibration_no_lookahead_guards', df, summary)
    def load_calibration_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_no_lookahead_guards/calibration_no_lookahead_guards.csv')

    def save_calibration_metadata_only_news_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_metadata_only_news_guards/calibration_metadata_only_news_guards', df, summary)
    def load_calibration_metadata_only_news_guard_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_metadata_only_news_guards/calibration_metadata_only_news_guards.csv')

    def save_calibration_source_preservation_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_source_preservation_guards/calibration_source_preservation_guards', df, summary)
    def load_calibration_source_preservation_guard_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_source_preservation_guards/calibration_source_preservation_guards.csv')

    def save_calibration_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/calibration_forbidden_columns/calibration_forbidden_columns', df, summary)
    def load_calibration_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/calibration_forbidden_columns/calibration_forbidden_columns.csv')

    def save_uncertainty_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/uncertainty_no_lookahead_guards/uncertainty_no_lookahead_guards', df, summary)
    def load_uncertainty_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/uncertainty_no_lookahead_guards/uncertainty_no_lookahead_guards.csv')

    def save_uncertainty_metadata_only_news_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/uncertainty_metadata_only_news_guards/uncertainty_metadata_only_news_guards', df, summary)
    def load_uncertainty_metadata_only_news_guard_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/uncertainty_metadata_only_news_guards/uncertainty_metadata_only_news_guards.csv')

    def save_uncertainty_source_preservation_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/uncertainty_source_preservation_guards/uncertainty_source_preservation_guards', df, summary)
    def load_uncertainty_source_preservation_guard_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/uncertainty_source_preservation_guards/uncertainty_source_preservation_guards.csv')

    def save_uncertainty_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/uncertainty_forbidden_columns/uncertainty_forbidden_columns', df, summary)
    def load_uncertainty_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/uncertainty_forbidden_columns/uncertainty_forbidden_columns.csv')

    def save_calibration_uncertainty_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/lineage/lineage_registry', df, summary)
    def load_calibration_uncertainty_lineage_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/lineage/lineage_registry.csv')

    def save_calibration_uncertainty_experiment_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/experiment_linkage/experiment_linkage_registry', df, summary)
    def load_calibration_uncertainty_experiment_linkage_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/experiment_linkage/experiment_linkage_registry.csv')

    def save_calibration_uncertainty_audit_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/audit_placeholders/audit_placeholder_registry', df, summary)
    def load_calibration_uncertainty_audit_placeholder_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/audit_placeholders/audit_placeholder_registry.csv')

    def save_calibration_uncertainty_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/manual_review/manual_review_queue', df, summary)
    def load_calibration_uncertainty_manual_review_queue(self):
        return self._load_csv('advanced_calibration_uncertainty/manual_review/manual_review_queue.csv')

    def save_calibration_uncertainty_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/findings/findings_registry', df, summary)
    def load_calibration_uncertainty_findings_registry(self):
        return self._load_csv('advanced_calibration_uncertainty/findings/findings_registry.csv')

    def save_calibration_uncertainty_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/scoring/readiness_score_report', df, summary)
    def load_calibration_uncertainty_readiness_score_report(self):
        return self._load_csv('advanced_calibration_uncertainty/scoring/readiness_score_report.csv')

    def save_calibration_uncertainty_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/manifest/manifest', df, summary)
    def load_calibration_uncertainty_manifest(self):
        return self._load_csv('advanced_calibration_uncertainty/manifest/manifest.csv')

    def save_calibration_uncertainty_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/health/health_check', df, summary)
    def load_calibration_uncertainty_health_check(self):
        return self._load_csv('advanced_calibration_uncertainty/health/health_check.csv')

    def save_calibration_uncertainty_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/validation/validation_report', df, summary)
    def load_calibration_uncertainty_validation_report(self):
        return self._load_csv('advanced_calibration_uncertainty/validation/validation_report.csv')

    def save_calibration_uncertainty_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/safety/safety_boundary', df, summary)
    def load_calibration_uncertainty_safety_boundary(self):
        return self._load_csv('advanced_calibration_uncertainty/safety/safety_boundary.csv')

    def save_phase_142_model_drift_monitoring_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_calibration_uncertainty/handoff/phase_142_handoff', df, summary)
    def load_phase_142_model_drift_monitoring_handoff_report(self):
        return self._load_csv('advanced_calibration_uncertainty/handoff/phase_142_handoff.csv')

    def save_calibration_uncertainty_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_calibration_uncertainty' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_calibration_uncertainty_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_calibration_uncertainty' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_calibration_uncertainty_reports(self):
        return pd.DataFrame()

    save_phase_142_handoff = save_phase_142_model_drift_monitoring_handoff_report
    load_phase_142_handoff = load_phase_142_model_drift_monitoring_handoff_report
    save_calibration_execution_disabled_registry = save_calibration_execution_disabled_report
    load_calibration_execution_disabled_registry = load_calibration_execution_disabled_report
    save_calibration_fit_disabled_registry = save_calibration_fit_disabled_report
    load_calibration_fit_disabled_registry = load_calibration_fit_disabled_report
    save_calibration_transform_disabled_registry = save_calibration_transform_disabled_report
    load_calibration_transform_disabled_registry = load_calibration_transform_disabled_report
    save_probability_prediction_disabled_registry = save_probability_prediction_disabled_report
    load_probability_prediction_disabled_registry = load_probability_prediction_disabled_report
    save_uncertainty_execution_disabled_registry = save_uncertainty_execution_disabled_report
    # Phase 142 Model Drift Monitoring and Data/Feature Drift Linkage methods
    def save_model_drift_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/profiles/profile_registry', df, summary)
    def load_model_drift_profile_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/profiles/profile_registry.csv')

    def save_model_drift_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/domains/domain_registry', df, summary)
    def load_model_drift_domain_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/domains/domain_registry.csv')

    def save_model_drift_monitoring_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/model_drift_contracts/model_drift_contracts', df, summary)
    def load_model_drift_monitoring_contract_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/model_drift_contracts/model_drift_contracts.csv')

    def save_data_drift_monitoring_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/data_drift_contracts/data_drift_contracts', df, summary)
    def load_data_drift_monitoring_contract_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/data_drift_contracts/data_drift_contracts.csv')

    def save_feature_drift_monitoring_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/feature_drift_contracts/feature_drift_contracts', df, summary)
    def load_feature_drift_monitoring_contract_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/feature_drift_contracts/feature_drift_contracts.csv')

    def save_feature_drift_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/feature_drift_linkage/feature_drift_linkage', df, summary)
    def load_feature_drift_linkage_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/feature_drift_linkage/feature_drift_linkage.csv')

    def save_feature_quality_drift_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/feature_quality_drift_linkage/feature_quality_drift_linkage', df, summary)
    def load_feature_quality_drift_linkage_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/feature_quality_drift_linkage/feature_quality_drift_linkage.csv')

    def save_featurestore_drift_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/featurestore_drift_linkage/featurestore_drift_linkage', df, summary)
    def load_featurestore_drift_linkage_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/featurestore_drift_linkage/featurestore_drift_linkage.csv')

    def save_regime_drift_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/regime_drift_linkage/regime_drift_linkage', df, summary)
    def load_regime_drift_linkage_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/regime_drift_linkage/regime_drift_linkage.csv')

    def save_calibration_drift_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/calibration_drift_contracts/calibration_drift_contracts', df, summary)
    def load_calibration_drift_contract_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/calibration_drift_contracts/calibration_drift_contracts.csv')

    def save_uncertainty_drift_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/uncertainty_drift_contracts/uncertainty_drift_contracts', df, summary)
    def load_uncertainty_drift_contract_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/uncertainty_drift_contracts/uncertainty_drift_contracts.csv')

    def save_prediction_distribution_drift_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/prediction_drift_placeholders/prediction_drift_placeholders', df, summary)
    def load_prediction_distribution_drift_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/prediction_drift_placeholders/prediction_drift_placeholders.csv')

    def save_reference_window_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/reference_windows/reference_windows', df, summary)
    def load_reference_window_policy_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/reference_windows/reference_windows.csv')

    def save_current_window_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/current_windows/current_windows', df, summary)
    def load_current_window_policy_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/current_windows/current_windows.csv')

    def save_rolling_window_placeholder_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/rolling_windows/rolling_windows', df, summary)
    def load_rolling_window_placeholder_policy_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/rolling_windows/rolling_windows.csv')

    def save_drift_threshold_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/drift_thresholds/drift_thresholds', df, summary)
    def load_drift_threshold_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/drift_thresholds/drift_thresholds.csv')

    def save_drift_segment_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/drift_segments/drift_segments', df, summary)
    def load_drift_segment_policy_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/drift_segments/drift_segments.csv')

    def save_drift_monitoring_schedule_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/drift_schedules/drift_schedules', df, summary)
    def load_drift_monitoring_schedule_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/drift_schedules/drift_schedules.csv')

    def save_drift_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/drift_metrics/drift_metrics', df, summary)
    def load_drift_metric_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/drift_metrics/drift_metrics.csv')

    def save_psi_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/psi_metrics/psi_metrics', df, summary)
    def load_psi_metric_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/psi_metrics/psi_metrics.csv')

    def save_ks_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/ks_metrics/ks_metrics', df, summary)
    def load_ks_metric_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/ks_metrics/ks_metrics.csv')

    def save_js_divergence_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/js_divergence_metrics/js_divergence_metrics', df, summary)
    def load_js_divergence_metric_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/js_divergence_metrics/js_divergence_metrics.csv')

    def save_wasserstein_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/wasserstein_metrics/wasserstein_metrics', df, summary)
    def load_wasserstein_metric_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/wasserstein_metrics/wasserstein_metrics.csv')

    def save_correlation_drift_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/correlation_drift_metrics/correlation_drift_metrics', df, summary)
    def load_correlation_drift_metric_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/correlation_drift_metrics/correlation_drift_metrics.csv')

    def save_missingness_drift_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/missingness_drift_metrics/missingness_drift_metrics', df, summary)
    def load_missingness_drift_metric_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/missingness_drift_metrics/missingness_drift_metrics.csv')

    def save_categorical_drift_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/categorical_drift_metrics/categorical_drift_metrics', df, summary)
    def load_categorical_drift_metric_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/categorical_drift_metrics/categorical_drift_metrics.csv')

    def save_numerical_drift_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/numerical_drift_metrics/numerical_drift_metrics', df, summary)
    def load_numerical_drift_metric_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/numerical_drift_metrics/numerical_drift_metrics.csv')

    def save_calibration_drift_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/calibration_drift_metrics/calibration_drift_metrics', df, summary)
    def load_calibration_drift_metric_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/calibration_drift_metrics/calibration_drift_metrics.csv')

    def save_uncertainty_drift_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/uncertainty_drift_metrics/uncertainty_drift_metrics', df, summary)
    def load_uncertainty_drift_metric_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/uncertainty_drift_metrics/uncertainty_drift_metrics.csv')

    def save_drift_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/execution_disabled/execution_disabled', df, summary)
    def load_drift_execution_disabled_report(self):
        return self._load_csv('advanced_model_drift_monitoring/execution_disabled/execution_disabled.csv')

    def save_drift_metric_calculation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/metric_calc_disabled/metric_calc_disabled', df, summary)
    def load_drift_metric_calculation_disabled_report(self):
        return self._load_csv('advanced_model_drift_monitoring/metric_calc_disabled/metric_calc_disabled.csv')

    def save_drift_alerting_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/alerting_disabled/alerting_disabled', df, summary)
    def load_drift_alerting_disabled_report(self):
        return self._load_csv('advanced_model_drift_monitoring/alerting_disabled/alerting_disabled.csv')

    def save_drift_retraining_trigger_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/retraining_trigger_disabled/retraining_trigger_disabled', df, summary)
    def load_drift_retraining_trigger_disabled_report(self):
        return self._load_csv('advanced_model_drift_monitoring/retraining_trigger_disabled/retraining_trigger_disabled.csv')

    def save_drift_model_action_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/model_action_disabled/model_action_disabled', df, summary)
    def load_drift_model_action_disabled_report(self):
        return self._load_csv('advanced_model_drift_monitoring/model_action_disabled/model_action_disabled.csv')

    def save_drift_prediction_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/prediction_disabled/prediction_disabled', df, summary)
    def load_drift_prediction_disabled_report(self):
        return self._load_csv('advanced_model_drift_monitoring/prediction_disabled/prediction_disabled.csv')

    def save_drift_monitoring_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/input_contracts/input_contracts', df, summary)
    def load_drift_monitoring_input_contract_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/input_contracts/input_contracts.csv')

    def save_drift_monitoring_output_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/output_contracts/output_contracts', df, summary)
    def load_drift_monitoring_output_contract_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/output_contracts/output_contracts.csv')

    def save_drift_validation_dependency_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/validation_dependencies/validation_dependencies', df, summary)
    def load_drift_validation_dependency_report(self):
        return self._load_csv('advanced_model_drift_monitoring/validation_dependencies/validation_dependencies.csv')

    def save_drift_quality_dependency_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/quality_dependencies/quality_dependencies', df, summary)
    def load_drift_quality_dependency_report(self):
        return self._load_csv('advanced_model_drift_monitoring/quality_dependencies/quality_dependencies.csv')

    def save_drift_runtime_dependency_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/runtime_dependencies/runtime_dependencies', df, summary)
    def load_drift_runtime_dependency_report(self):
        return self._load_csv('advanced_model_drift_monitoring/runtime_dependencies/runtime_dependencies.csv')

    def save_drift_candidate_model_dependency_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/candidate_model_dependencies/candidate_model_dependencies', df, summary)
    def load_drift_candidate_model_dependency_report(self):
        return self._load_csv('advanced_model_drift_monitoring/candidate_model_dependencies/candidate_model_dependencies.csv')

    def save_drift_ensemble_dependency_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/ensemble_dependencies/ensemble_dependencies', df, summary)
    def load_drift_ensemble_dependency_report(self):
        return self._load_csv('advanced_model_drift_monitoring/ensemble_dependencies/ensemble_dependencies.csv')

    def save_drift_calibration_uncertainty_dependency_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/calib_uncert_dependencies/calib_uncert_dependencies', df, summary)
    def load_drift_calibration_uncertainty_dependency_report(self):
        return self._load_csv('advanced_model_drift_monitoring/calib_uncert_dependencies/calib_uncert_dependencies.csv')

    def save_drift_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/no_lookahead_guards/no_lookahead_guards', df, summary)
    def load_drift_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/no_lookahead_guards/no_lookahead_guards.csv')

    def save_drift_metadata_only_news_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/metadata_only_news_guards/metadata_only_news_guards', df, summary)
    def load_drift_metadata_only_news_guard_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/metadata_only_news_guards/metadata_only_news_guards.csv')

    def save_drift_source_preservation_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/source_preservation_guards/source_preservation_guards', df, summary)
    def load_drift_source_preservation_guard_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/source_preservation_guards/source_preservation_guards.csv')

    def save_drift_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/forbidden_columns/forbidden_columns', df, summary)
    def load_drift_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/forbidden_columns/forbidden_columns.csv')

    def save_drift_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/lineage/lineage_registry', df, summary)
    def load_drift_lineage_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/lineage/lineage_registry.csv')

    def save_drift_experiment_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/experiment_linkage/experiment_linkage_registry', df, summary)
    def load_drift_experiment_linkage_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/experiment_linkage/experiment_linkage_registry.csv')

    def save_drift_audit_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/audit_placeholders/audit_placeholder_registry', df, summary)
    def load_drift_audit_placeholder_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/audit_placeholders/audit_placeholder_registry.csv')

    def save_drift_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/manual_review/manual_review_queue', df, summary)
    def load_drift_manual_review_queue(self):
        return self._load_csv('advanced_model_drift_monitoring/manual_review/manual_review_queue.csv')

    def save_drift_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/findings/findings_registry', df, summary)
    def load_drift_findings_registry(self):
        return self._load_csv('advanced_model_drift_monitoring/findings/findings_registry.csv')

    def save_drift_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/scoring/readiness_score_report', df, summary)
    def load_drift_readiness_score_report(self):
        return self._load_csv('advanced_model_drift_monitoring/scoring/readiness_score_report.csv')

    def save_model_drift_monitoring_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/manifest/manifest', df, summary)
    def load_model_drift_monitoring_manifest(self):
        return self._load_csv('advanced_model_drift_monitoring/manifest/manifest.csv')

    def save_model_drift_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/health/health_check', df, summary)
    def load_model_drift_health_check(self):
        return self._load_csv('advanced_model_drift_monitoring/health/health_check.csv')

    def save_model_drift_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/validation/validation_report', df, summary)
    def load_model_drift_validation_report(self):
        return self._load_csv('advanced_model_drift_monitoring/validation/validation_report.csv')

    def save_model_drift_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/safety/safety_boundary', df, summary)
    def load_model_drift_safety_boundary(self):
        return self._load_csv('advanced_model_drift_monitoring/safety/safety_boundary.csv')

    def save_phase_143_explainability_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_drift_monitoring/handoff/phase_143_handoff', df, summary)
    def load_phase_143_explainability_handoff_report(self):
        return self._load_csv('advanced_model_drift_monitoring/handoff/phase_143_handoff.csv')

    def save_model_drift_monitoring_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_model_drift_monitoring' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_model_drift_monitoring_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_model_drift_monitoring' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_model_drift_monitoring_reports(self):
        return pd.DataFrame()

    save_phase_143_handoff = save_phase_143_explainability_handoff_report
    load_phase_143_handoff = load_phase_143_explainability_handoff_report
    save_drift_calculation_disabled_registry = save_drift_metric_calculation_disabled_report
    load_drift_calculation_disabled_registry = load_drift_metric_calculation_disabled_report

    # Phase 143 Explainability and Feature Attribution Reports Methods
    def save_explainability_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/profiles/profile_registry', df, summary)
    def load_explainability_profile_registry(self):
        return self._load_csv('advanced_explainability_attribution/profiles/profile_registry.csv')

    def save_explainability_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/domains/domain_registry', df, summary)
    def load_explainability_domain_registry(self):
        return self._load_csv('advanced_explainability_attribution/domains/domain_registry.csv')

    def save_explainability_report_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/report_contracts/report_contracts', df, summary)
    def load_explainability_report_contracts(self):
        return self._load_csv('advanced_explainability_attribution/report_contracts/report_contracts.csv')

    def save_feature_attribution_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/attribution_contracts/attribution_contracts', df, summary)
    def load_feature_attribution_contracts(self):
        return self._load_csv('advanced_explainability_attribution/attribution_contracts/attribution_contracts.csv')

    def save_global_explanation_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/global_explanations/global_explanations', df, summary)
    def load_global_explanation_contracts(self):
        return self._load_csv('advanced_explainability_attribution/global_explanations/global_explanations.csv')

    def save_local_explanation_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/local_explanations/local_explanations', df, summary)
    def load_local_explanation_contracts(self):
        return self._load_csv('advanced_explainability_attribution/local_explanations/local_explanations.csv')

    def save_feature_importance_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/feature_importance_placeholders/feature_importance_placeholders', df, summary)
    def load_feature_importance_placeholders(self):
        return self._load_csv('advanced_explainability_attribution/feature_importance_placeholders/feature_importance_placeholders.csv')

    def save_feature_contribution_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/feature_contribution_placeholders/feature_contribution_placeholders', df, summary)
    def load_feature_contribution_placeholders(self):
        return self._load_csv('advanced_explainability_attribution/feature_contribution_placeholders/feature_contribution_placeholders.csv')

    def save_shap_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/shap_placeholders/shap_placeholders', df, summary)
    def load_shap_placeholders(self):
        return self._load_csv('advanced_explainability_attribution/shap_placeholders/shap_placeholders.csv')

    def save_lime_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/lime_placeholders/lime_placeholders', df, summary)
    def load_lime_placeholders(self):
        return self._load_csv('advanced_explainability_attribution/lime_placeholders/lime_placeholders.csv')

    def save_permutation_importance_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/permutation_importance_placeholders/permutation_importance_placeholders', df, summary)
    def load_permutation_importance_placeholders(self):
        return self._load_csv('advanced_explainability_attribution/permutation_importance_placeholders/permutation_importance_placeholders.csv')

    def save_pdp_ice_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/pdp_placeholders/pdp_ice_placeholders', df, summary)
    def load_pdp_ice_placeholders(self):
        return self._load_csv('advanced_explainability_attribution/pdp_placeholders/pdp_ice_placeholders.csv')

    def save_surrogate_model_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/surrogate_model_placeholders/surrogate_model_placeholders', df, summary)
    def load_surrogate_model_placeholders(self):
        return self._load_csv('advanced_explainability_attribution/surrogate_model_placeholders/surrogate_model_placeholders.csv')

    def save_counterfactual_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/counterfactual_placeholders/counterfactual_placeholders', df, summary)
    def load_counterfactual_placeholders(self):
        return self._load_csv('advanced_explainability_attribution/counterfactual_placeholders/counterfactual_placeholders.csv')

    def save_reason_code_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/reason_code_placeholders/reason_code_placeholders', df, summary)
    def load_reason_code_placeholders(self):
        return self._load_csv('advanced_explainability_attribution/reason_code_placeholders/reason_code_placeholders.csv')

    def save_attribution_method_policies(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/method_policies/method_policies', df, summary)
    def load_attribution_method_policies(self):
        return self._load_csv('advanced_explainability_attribution/method_policies/method_policies.csv')

    def save_attribution_scope_policies(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/scope_policies/scope_policies', df, summary)
    def load_attribution_scope_policies(self):
        return self._load_csv('advanced_explainability_attribution/scope_policies/scope_policies.csv')

    def save_attribution_input_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/input_contracts/input_contracts', df, summary)
    def load_attribution_input_contracts(self):
        return self._load_csv('advanced_explainability_attribution/input_contracts/input_contracts.csv')

    def save_attribution_output_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/output_contracts/output_contracts', df, summary)
    def load_attribution_output_contracts(self):
        return self._load_csv('advanced_explainability_attribution/output_contracts/output_contracts.csv')

    def save_explainability_disabled_execution_report(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/execution_disabled/execution_disabled', df, summary)
    def load_explainability_disabled_execution_report(self):
        return self._load_csv('advanced_explainability_attribution/execution_disabled/execution_disabled.csv')

    def save_explainability_metric_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/metric_placeholders/metric_placeholders', df, summary)
    def load_explainability_metric_placeholders(self):
        return self._load_csv('advanced_explainability_attribution/metric_placeholders/metric_placeholders.csv')

    def save_attribution_quality_gates(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/quality_gates/quality_gates', df, summary)
    def load_attribution_quality_gates(self):
        return self._load_csv('advanced_explainability_attribution/quality_gates/quality_gates.csv')

    def save_explanation_stability_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/stability_placeholders/stability_placeholders', df, summary)
    def load_explanation_stability_placeholders(self):
        return self._load_csv('advanced_explainability_attribution/stability_placeholders/stability_placeholders.csv')

    def save_attribution_drift_linkage(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/drift_linkage/drift_linkage', df, summary)
    def load_attribution_drift_linkage(self):
        return self._load_csv('advanced_explainability_attribution/drift_linkage/drift_linkage.csv')

    def save_featurestore_explainability_linkage(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/featurestore_linkage/featurestore_linkage', df, summary)
    def load_featurestore_explainability_linkage(self):
        return self._load_csv('advanced_explainability_attribution/featurestore_linkage/featurestore_linkage.csv')

    def save_regime_explainability_linkage(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/regime_linkage/regime_linkage', df, summary)
    def load_regime_explainability_linkage(self):
        return self._load_csv('advanced_explainability_attribution/regime_linkage/regime_linkage.csv')

    def save_drift_explainability_linkage(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/drift_linkage/drift_explainability_linkage', df, summary)
    def load_drift_explainability_linkage(self):
        return self._load_csv('advanced_explainability_attribution/drift_linkage/drift_explainability_linkage.csv')

    def save_calibration_uncertainty_explainability_linkage(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/calibration_uncertainty_linkage/calibration_uncertainty_linkage', df, summary)
    def load_calibration_uncertainty_explainability_linkage(self):
        return self._load_csv('advanced_explainability_attribution/calibration_uncertainty_linkage/calibration_uncertainty_linkage.csv')

    def save_explainability_validation_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/validation_dependencies/validation_dependencies', df, summary)
    def load_explainability_validation_dependencies(self):
        return self._load_csv('advanced_explainability_attribution/validation_dependencies/validation_dependencies.csv')

    def save_explainability_quality_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/quality_dependencies/quality_dependencies', df, summary)
    def load_explainability_quality_dependencies(self):
        return self._load_csv('advanced_explainability_attribution/quality_dependencies/quality_dependencies.csv')

    def save_explainability_runtime_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/runtime_dependencies/runtime_dependencies', df, summary)
    def load_explainability_runtime_dependencies(self):
        return self._load_csv('advanced_explainability_attribution/runtime_dependencies/runtime_dependencies.csv')

    def save_explainability_candidate_model_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/candidate_dependencies/candidate_dependencies', df, summary)
    def load_explainability_candidate_model_dependencies(self):
        return self._load_csv('advanced_explainability_attribution/candidate_dependencies/candidate_dependencies.csv')

    def save_explainability_ensemble_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/ensemble_dependencies/ensemble_dependencies', df, summary)
    def load_explainability_ensemble_dependencies(self):
        return self._load_csv('advanced_explainability_attribution/ensemble_dependencies/ensemble_dependencies.csv')

    def save_explainability_no_lookahead_guards(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/no_lookahead_guards/no_lookahead_guards', df, summary)
    def load_explainability_no_lookahead_guards(self):
        return self._load_csv('advanced_explainability_attribution/no_lookahead_guards/no_lookahead_guards.csv')

    def save_explainability_metadata_only_news_guards(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/metadata_only_news_guards/metadata_only_news_guards', df, summary)
    def load_explainability_metadata_only_news_guards(self):
        return self._load_csv('advanced_explainability_attribution/metadata_only_news_guards/metadata_only_news_guards.csv')

    def save_explainability_source_preservation_guards(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/source_preservation_guards/source_preservation_guards', df, summary)
    def load_explainability_source_preservation_guards(self):
        return self._load_csv('advanced_explainability_attribution/source_preservation_guards/source_preservation_guards.csv')

    def save_explainability_forbidden_column_policies(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/forbidden_columns/forbidden_columns', df, summary)
    def load_explainability_forbidden_column_policies(self):
        return self._load_csv('advanced_explainability_attribution/forbidden_columns/forbidden_columns.csv')

    def save_explainability_lineage(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/lineage/lineage_registry', df, summary)
    def load_explainability_lineage(self):
        return self._load_csv('advanced_explainability_attribution/lineage/lineage_registry.csv')

    def save_explainability_experiment_linkage(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/experiment_linkage/experiment_linkage', df, summary)
    def load_explainability_experiment_linkage(self):
        return self._load_csv('advanced_explainability_attribution/experiment_linkage/experiment_linkage.csv')

    def save_explainability_audit_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/audit_placeholders/audit_placeholders', df, summary)
    def load_explainability_audit_placeholders(self):
        return self._load_csv('advanced_explainability_attribution/audit_placeholders/audit_placeholders.csv')

    def save_explainability_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/manual_review/manual_review_queue', df, summary)
    def load_explainability_manual_review_queue(self):
        return self._load_csv('advanced_explainability_attribution/manual_review/manual_review_queue.csv')

    def save_explainability_findings(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/findings/findings_registry', df, summary)
    def load_explainability_findings(self):
        return self._load_csv('advanced_explainability_attribution/findings/findings_registry.csv')

    def save_explainability_readiness_score(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/scoring/readiness_score_report', df, summary)
    def load_explainability_readiness_score(self):
        return self._load_csv('advanced_explainability_attribution/scoring/readiness_score_report.csv')

    def save_explainability_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/manifest/manifest', df, summary)
    def load_explainability_manifest(self):
        return self._load_csv('advanced_explainability_attribution/manifest/manifest.csv')

    def save_explainability_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/health/health_check', df, summary)
    def load_explainability_health_check(self):
        return self._load_csv('advanced_explainability_attribution/health/health_check.csv')

    def save_explainability_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/validation/validation_report', df, summary)
    def load_explainability_validation_report(self):
        return self._load_csv('advanced_explainability_attribution/validation/validation_report.csv')

    def save_explainability_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/safety/safety_boundary', df, summary)
    def load_explainability_safety_boundary(self):
        return self._load_csv('advanced_explainability_attribution/safety/safety_boundary.csv')

    def save_phase_144_model_governance_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_explainability_attribution/handoff/phase_144_handoff', df, summary)
    def load_phase_144_model_governance_handoff_report(self):
        return self._load_csv('advanced_explainability_attribution/handoff/phase_144_handoff.csv')

    def save_explainability_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_explainability_attribution' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_explainability_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_explainability_attribution' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_explainability_reports(self):
        return pd.DataFrame()

    save_phase_144_handoff = save_phase_144_model_governance_handoff_report
    load_phase_144_handoff = load_phase_144_model_governance_handoff_report

    # Phase 144 Model Governance, Model Cards and Audit Trail
    def save_model_governance_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/profiles/profile_registry', df, summary)
    def load_model_governance_profile_registry(self):
        return self._load_csv('advanced_model_governance/profiles/profile_registry.csv')

    def save_model_governance_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/domains/domain_registry', df, summary)
    def load_model_governance_domain_registry(self):
        return self._load_csv('advanced_model_governance/domains/domain_registry.csv')

    def save_model_governance_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/governance_contracts/contract_registry', df, summary)
    def load_model_governance_contract_registry(self):
        return self._load_csv('advanced_model_governance/governance_contracts/contract_registry.csv')

    def save_model_card_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/model_cards/card_contracts', df, summary)
    def load_model_card_contract_registry(self):
        return self._load_csv('advanced_model_governance/model_cards/card_contracts.csv')

    def save_model_card_template_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/model_card_templates/template_registry', df, summary)
    def load_model_card_template_registry(self):
        return self._load_csv('advanced_model_governance/model_card_templates/template_registry.csv')

    def save_model_card_section_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/model_card_sections/section_registry', df, summary)
    def load_model_card_section_registry(self):
        return self._load_csv('advanced_model_governance/model_card_sections/section_registry.csv')

    def save_model_card_limitation_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/model_card_limitations/limitation_registry', df, summary)
    def load_model_card_limitation_registry(self):
        return self._load_csv('advanced_model_governance/model_card_limitations/limitation_registry.csv')

    def save_model_card_intended_use_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/intended_use/intended_use_registry', df, summary)
    def load_model_card_intended_use_registry(self):
        return self._load_csv('advanced_model_governance/intended_use/intended_use_registry.csv')

    def save_model_card_prohibited_use_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/prohibited_use/prohibited_use_registry', df, summary)
    def load_model_card_prohibited_use_registry(self):
        return self._load_csv('advanced_model_governance/prohibited_use/prohibited_use_registry.csv')

    def save_model_card_risk_disclosure_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/risk_disclosures/risk_disclosure_registry', df, summary)
    def load_model_card_risk_disclosure_registry(self):
        return self._load_csv('advanced_model_governance/risk_disclosures/risk_disclosure_registry.csv')

    def save_model_card_validation_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/validation_evidence/validation_evidence_registry', df, summary)
    def load_model_card_validation_evidence_registry(self):
        return self._load_csv('advanced_model_governance/validation_evidence/validation_evidence_registry.csv')

    def save_model_card_data_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/data_dependencies/data_dependency_registry', df, summary)
    def load_model_card_data_dependency_registry(self):
        return self._load_csv('advanced_model_governance/data_dependencies/data_dependency_registry.csv')

    def save_model_card_feature_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/feature_dependencies/feature_dependency_registry', df, summary)
    def load_model_card_feature_dependency_registry(self):
        return self._load_csv('advanced_model_governance/feature_dependencies/feature_dependency_registry.csv')

    def save_model_card_model_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/model_dependencies/model_dependency_registry', df, summary)
    def load_model_card_model_dependency_registry(self):
        return self._load_csv('advanced_model_governance/model_dependencies/model_dependency_registry.csv')

    def save_model_card_runtime_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/runtime_dependencies/runtime_dependency_registry', df, summary)
    def load_model_card_runtime_dependency_registry(self):
        return self._load_csv('advanced_model_governance/runtime_dependencies/runtime_dependency_registry.csv')

    def save_governance_approval_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/approval_boundaries/approval_boundary_registry', df, summary)
    def load_governance_approval_boundary_registry(self):
        return self._load_csv('advanced_model_governance/approval_boundaries/approval_boundary_registry.csv')

    def save_governance_release_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/release_boundaries/release_boundary_registry', df, summary)
    def load_governance_release_boundary_registry(self):
        return self._load_csv('advanced_model_governance/release_boundaries/release_boundary_registry.csv')

    def save_governance_non_production_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/non_production_boundaries/non_production_boundary_registry', df, summary)
    def load_governance_non_production_boundary_registry(self):
        return self._load_csv('advanced_model_governance/non_production_boundaries/non_production_boundary_registry.csv')

    def save_governance_manual_review_gate_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/manual_review_gates/manual_review_gate_registry', df, summary)
    def load_governance_manual_review_gate_registry(self):
        return self._load_csv('advanced_model_governance/manual_review_gates/manual_review_gate_registry.csv')

    def save_governance_validation_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/validation_evidence/governance_validation_evidence', df, summary)
    def load_governance_validation_evidence_registry(self):
        return self._load_csv('advanced_model_governance/validation_evidence/governance_validation_evidence.csv')

    def save_governance_risk_register(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/risk_register/risk_register', df, summary)
    def load_governance_risk_register(self):
        return self._load_csv('advanced_model_governance/risk_register/risk_register.csv')

    def save_governance_control_checklist_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/control_checklists/control_checklist_registry', df, summary)
    def load_governance_control_checklist_registry(self):
        return self._load_csv('advanced_model_governance/control_checklists/control_checklist_registry.csv')

    def save_governance_compliance_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/compliance_placeholders/compliance_placeholder_registry', df, summary)
    def load_governance_compliance_placeholder_registry(self):
        return self._load_csv('advanced_model_governance/compliance_placeholders/compliance_placeholder_registry.csv')

    def save_governance_audit_trail_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/audit_trail_placeholders/audit_trail_placeholder_registry', df, summary)
    def load_governance_audit_trail_placeholder_registry(self):
        return self._load_csv('advanced_model_governance/audit_trail_placeholders/audit_trail_placeholder_registry.csv')

    def save_governance_decision_log_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/decision_log_placeholders/decision_log_placeholder_registry', df, summary)
    def load_governance_decision_log_placeholder_registry(self):
        return self._load_csv('advanced_model_governance/decision_log_placeholders/decision_log_placeholder_registry.csv')

    def save_governance_change_log_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/change_log_placeholders/change_log_placeholder_registry', df, summary)
    def load_governance_change_log_placeholder_registry(self):
        return self._load_csv('advanced_model_governance/change_log_placeholders/change_log_placeholder_registry.csv')

    def save_governance_owner_responsibility_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/owner_responsibility_placeholders/owner_responsibility_placeholder_registry', df, summary)
    def load_governance_owner_responsibility_placeholder_registry(self):
        return self._load_csv('advanced_model_governance/owner_responsibility_placeholders/owner_responsibility_placeholder_registry.csv')

    def save_governance_model_lifecycle_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/lifecycle_placeholders/model_lifecycle_placeholder_registry', df, summary)
    def load_governance_model_lifecycle_placeholder_registry(self):
        return self._load_csv('advanced_model_governance/lifecycle_placeholders/model_lifecycle_placeholder_registry.csv')

    def save_governance_model_version_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/version_placeholders/model_version_placeholder_registry', df, summary)
    def load_governance_model_version_placeholder_registry(self):
        return self._load_csv('advanced_model_governance/version_placeholders/model_version_placeholder_registry.csv')

    def save_governance_model_registry_write_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/model_registry_write_disabled/report', df, summary)
    def load_governance_model_registry_write_disabled_report(self):
        return self._load_csv('advanced_model_governance/model_registry_write_disabled/report.csv')

    def save_governance_model_artifact_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/artifact_disabled/report', df, summary)
    def load_governance_model_artifact_disabled_report(self):
        return self._load_csv('advanced_model_governance/artifact_disabled/report.csv')

    def save_governance_deployment_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/deployment_disabled/report', df, summary)
    def load_governance_deployment_disabled_report(self):
        return self._load_csv('advanced_model_governance/deployment_disabled/report.csv')

    def save_governance_production_approval_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/production_approval_disabled/report', df, summary)
    def load_governance_production_approval_disabled_report(self):
        return self._load_csv('advanced_model_governance/production_approval_disabled/report.csv')

    def save_governance_broker_ready_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/broker_ready_disabled/report', df, summary)
    def load_governance_broker_ready_disabled_report(self):
        return self._load_csv('advanced_model_governance/broker_ready_disabled/report.csv')

    def save_governance_live_trading_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/live_trading_disabled/report', df, summary)
    def load_governance_live_trading_disabled_report(self):
        return self._load_csv('advanced_model_governance/live_trading_disabled/report.csv')

    def save_governance_prediction_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/prediction_disabled/report', df, summary)
    def load_governance_prediction_disabled_report(self):
        return self._load_csv('advanced_model_governance/prediction_disabled/report.csv')

    def save_governance_training_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/training_disabled/report', df, summary)
    def load_governance_training_disabled_report(self):
        return self._load_csv('advanced_model_governance/training_disabled/report.csv')

    def save_governance_signal_generation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/signal_generation_disabled/report', df, summary)
    def load_governance_signal_generation_disabled_report(self):
        return self._load_csv('advanced_model_governance/signal_generation_disabled/report.csv')

    def save_governance_performance_claim_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/performance_claim_disabled/report', df, summary)
    def load_governance_performance_claim_disabled_report(self):
        return self._load_csv('advanced_model_governance/performance_claim_disabled/report.csv')

    def save_governance_dataset_contract_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/dataset_dependencies/dataset_dependency_registry', df, summary)
    def load_governance_dataset_contract_dependency_registry(self):
        return self._load_csv('advanced_model_governance/dataset_dependencies/dataset_dependency_registry.csv')

    def save_governance_baseline_model_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/baseline_dependencies/baseline_dependency_registry', df, summary)
    def load_governance_baseline_model_dependency_registry(self):
        return self._load_csv('advanced_model_governance/baseline_dependencies/baseline_dependency_registry.csv')

    def save_governance_gpu_training_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/gpu_training_dependencies/gpu_training_dependency_registry', df, summary)
    def load_governance_gpu_training_dependency_registry(self):
        return self._load_csv('advanced_model_governance/gpu_training_dependencies/gpu_training_dependency_registry.csv')

    def save_governance_ensemble_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/ensemble_dependencies/ensemble_dependency_registry', df, summary)
    def load_governance_ensemble_dependency_registry(self):
        return self._load_csv('advanced_model_governance/ensemble_dependencies/ensemble_dependency_registry.csv')

    def save_governance_calibration_uncertainty_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/calibration_uncertainty_dependencies/calibration_uncertainty_dependency_registry', df, summary)
    def load_governance_calibration_uncertainty_dependency_registry(self):
        return self._load_csv('advanced_model_governance/calibration_uncertainty_dependencies/calibration_uncertainty_dependency_registry.csv')

    def save_governance_drift_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/drift_dependencies/drift_dependency_registry', df, summary)
    def load_governance_drift_dependency_registry(self):
        return self._load_csv('advanced_model_governance/drift_dependencies/drift_dependency_registry.csv')

    def save_governance_explainability_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/explainability_dependencies/explainability_dependency_registry', df, summary)
    def load_governance_explainability_dependency_registry(self):
        return self._load_csv('advanced_model_governance/explainability_dependencies/explainability_dependency_registry.csv')

    def save_governance_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/no_lookahead_guards/no_lookahead_guard_registry', df, summary)
    def load_governance_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_model_governance/no_lookahead_guards/no_lookahead_guard_registry.csv')

    def save_governance_metadata_only_news_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/metadata_only_news_guards/metadata_only_news_guard_registry', df, summary)
    def load_governance_metadata_only_news_guard_registry(self):
        return self._load_csv('advanced_model_governance/metadata_only_news_guards/metadata_only_news_guard_registry.csv')

    def save_governance_source_preservation_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/source_preservation_guards/source_preservation_guard_registry', df, summary)
    def load_governance_source_preservation_guard_registry(self):
        return self._load_csv('advanced_model_governance/source_preservation_guards/source_preservation_guard_registry.csv')

    def save_governance_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/forbidden_columns/forbidden_column_policy_registry', df, summary)
    def load_governance_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_model_governance/forbidden_columns/forbidden_column_policy_registry.csv')

    def save_governance_lineage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/lineage/lineage_registry', df, summary)
    def load_governance_lineage_registry(self):
        return self._load_csv('advanced_model_governance/lineage/lineage_registry.csv')

    def save_governance_experiment_linkage_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/experiment_linkage/experiment_linkage_registry', df, summary)
    def load_governance_experiment_linkage_registry(self):
        return self._load_csv('advanced_model_governance/experiment_linkage/experiment_linkage_registry.csv')

    def save_governance_audit_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/audit_placeholders/audit_placeholder_registry', df, summary)
    def load_governance_audit_placeholder_registry(self):
        return self._load_csv('advanced_model_governance/audit_placeholders/audit_placeholder_registry.csv')

    def save_governance_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/manual_review/manual_review_queue', df, summary)
    def load_governance_manual_review_queue(self):
        return self._load_csv('advanced_model_governance/manual_review/manual_review_queue.csv')

    def save_governance_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/findings/findings_registry', df, summary)
    def load_governance_findings_registry(self):
        return self._load_csv('advanced_model_governance/findings/findings_registry.csv')

    def save_governance_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/scoring/readiness_score_report', df, summary)
    def load_governance_readiness_score_report(self):
        return self._load_csv('advanced_model_governance/scoring/readiness_score_report.csv')

    def save_model_governance_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/manifest/manifest', df, summary)
    def load_model_governance_manifest(self):
        return self._load_csv('advanced_model_governance/manifest/manifest.csv')

    def save_model_governance_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/health/health_check', df, summary)
    def load_model_governance_health_check(self):
        return self._load_csv('advanced_model_governance/health/health_check.csv')

    def save_model_governance_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/validation/validation_report', df, summary)
    def load_model_governance_validation_report(self):
        return self._load_csv('advanced_model_governance/validation/validation_report.csv')

    def save_model_governance_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/safety/safety_boundary', df, summary)
    def load_model_governance_safety_boundary(self):
        return self._load_csv('advanced_model_governance/safety/safety_boundary.csv')

    def save_phase_145_advanced_ml_acceptance_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_model_governance/handoff/phase_145_handoff', df, summary)
    def load_phase_145_advanced_ml_acceptance_handoff_report(self):
        return self._load_csv('advanced_model_governance/handoff/phase_145_handoff.csv')

    def save_model_governance_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_model_governance' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_model_governance_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_model_governance' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_model_governance_reports(self):
        return pd.DataFrame()

    save_phase_145_handoff = save_phase_145_advanced_ml_acceptance_handoff_report
    load_phase_145_handoff = load_phase_145_advanced_ml_acceptance_handoff_report

    # Phase 145 Advanced ML Acceptance Report DataLake Methods
    def save_advanced_ml_acceptance_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/profiles/profile_registry', df, summary)
    def load_advanced_ml_acceptance_profile_registry(self):
        return self._load_csv('advanced_ml_acceptance/profiles/profile_registry.csv')

    def save_advanced_ml_acceptance_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/domains/domain_registry', df, summary)
    def load_advanced_ml_acceptance_domain_registry(self):
        return self._load_csv('advanced_ml_acceptance/domains/domain_registry.csv')

    def save_advanced_ml_acceptance_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/scope/scope_registry', df, summary)
    def load_advanced_ml_acceptance_scope_registry(self):
        return self._load_csv('advanced_ml_acceptance/scope/scope_registry.csv')

    def save_advanced_ml_component_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/components/component_registry', df, summary)
    def load_advanced_ml_component_registry(self):
        return self._load_csv('advanced_ml_acceptance/components/component_registry.csv')

    def save_advanced_ml_component_acceptance_checkpoint_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/component_checkpoints/checkpoint_registry', df, summary)
    def load_advanced_ml_component_acceptance_checkpoint_registry(self):
        return self._load_csv('advanced_ml_acceptance/component_checkpoints/checkpoint_registry.csv')

    def save_phase_136_gpu_runtime_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/phase_136_gpu_runtime/phase_136_acceptance', df, summary)
    def load_phase_136_gpu_runtime_acceptance_registry(self):
        return self._load_csv('advanced_ml_acceptance/phase_136_gpu_runtime/phase_136_acceptance.csv')

    def save_phase_137_dataset_contract_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/phase_137_dataset_contracts/phase_137_acceptance', df, summary)
    def load_phase_137_dataset_contract_acceptance_registry(self):
        return self._load_csv('advanced_ml_acceptance/phase_137_dataset_contracts/phase_137_acceptance.csv')

    def save_phase_138_baseline_model_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/phase_138_baseline_models/phase_138_acceptance', df, summary)
    def load_phase_138_baseline_model_acceptance_registry(self):
        return self._load_csv('advanced_ml_acceptance/phase_138_baseline_models/phase_138_acceptance.csv')

    def save_phase_139_gpu_training_governance_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/phase_139_gpu_training_governance/phase_139_acceptance', df, summary)
    def load_phase_139_gpu_training_governance_acceptance_registry(self):
        return self._load_csv('advanced_ml_acceptance/phase_139_gpu_training_governance/phase_139_acceptance.csv')

    def save_phase_140_ensemble_candidate_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/phase_140_ensemble_candidate/phase_140_acceptance', df, summary)
    def load_phase_140_ensemble_candidate_acceptance_registry(self):
        return self._load_csv('advanced_ml_acceptance/phase_140_ensemble_candidate/phase_140_acceptance.csv')

    def save_phase_141_calibration_uncertainty_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/phase_141_calibration_uncertainty/phase_141_acceptance', df, summary)
    def load_phase_141_calibration_uncertainty_acceptance_registry(self):
        return self._load_csv('advanced_ml_acceptance/phase_141_calibration_uncertainty/phase_141_acceptance.csv')

    def save_phase_142_drift_monitoring_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/phase_142_drift_monitoring/phase_142_acceptance', df, summary)
    def load_phase_142_drift_monitoring_acceptance_registry(self):
        return self._load_csv('advanced_ml_acceptance/phase_142_drift_monitoring/phase_142_acceptance.csv')

    def save_phase_143_explainability_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/phase_143_explainability/phase_143_acceptance', df, summary)
    def load_phase_143_explainability_acceptance_registry(self):
        return self._load_csv('advanced_ml_acceptance/phase_143_explainability/phase_143_acceptance.csv')

    def save_phase_144_model_governance_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/phase_144_model_governance/phase_144_acceptance', df, summary)
    def load_phase_144_model_governance_acceptance_registry(self):
        return self._load_csv('advanced_ml_acceptance/phase_144_model_governance/phase_144_acceptance.csv')

    def save_advanced_ml_dependency_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/dependency_acceptance/dependency_registry', df, summary)
    def load_advanced_ml_dependency_acceptance_registry(self):
        return self._load_csv('advanced_ml_acceptance/dependency_acceptance/dependency_registry.csv')

    def save_advanced_ml_validation_evidence_summary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/validation_evidence/evidence_summary', df, summary)
    def load_advanced_ml_validation_evidence_summary_registry(self):
        return self._load_csv('advanced_ml_acceptance/validation_evidence/evidence_summary.csv')

    def save_advanced_ml_safety_boundary_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/safety_boundary_acceptance/safety_boundary_registry', df, summary)
    def load_advanced_ml_safety_boundary_acceptance_registry(self):
        return self._load_csv('advanced_ml_acceptance/safety_boundary_acceptance/safety_boundary_registry.csv')

    def save_advanced_ml_non_production_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/non_production_boundaries/non_production_registry', df, summary)
    def load_advanced_ml_non_production_boundary_registry(self):
        return self._load_csv('advanced_ml_acceptance/non_production_boundaries/non_production_registry.csv')

    def save_advanced_ml_manual_review_gate_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/manual_review_gates/manual_review_gate_registry', df, summary)
    def load_advanced_ml_manual_review_gate_registry(self):
        return self._load_csv('advanced_ml_acceptance/manual_review_gates/manual_review_gate_registry.csv')

    def save_advanced_ml_go_no_go_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/go_no_go_boundaries/go_no_go_registry', df, summary)
    def load_advanced_ml_go_no_go_boundary_registry(self):
        return self._load_csv('advanced_ml_acceptance/go_no_go_boundaries/go_no_go_registry.csv')

    def save_advanced_ml_blocker_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/blockers/blocker_registry', df, summary)
    def load_advanced_ml_blocker_registry(self):
        return self._load_csv('advanced_ml_acceptance/blockers/blocker_registry.csv')

    def save_advanced_ml_gap_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/gaps/gap_registry', df, summary)
    def load_advanced_ml_gap_registry(self):
        return self._load_csv('advanced_ml_acceptance/gaps/gap_registry.csv')

    def save_advanced_ml_warning_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/warnings/warning_registry', df, summary)
    def load_advanced_ml_warning_registry(self):
        return self._load_csv('advanced_ml_acceptance/warnings/warning_registry.csv')

    def save_advanced_ml_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/findings/findings_registry', df, summary)
    def load_advanced_ml_findings_registry(self):
        return self._load_csv('advanced_ml_acceptance/findings/findings_registry.csv')

    def save_advanced_ml_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/scoring/readiness_score_report', df, summary)
    def load_advanced_ml_readiness_score_report(self):
        return self._load_csv('advanced_ml_acceptance/scoring/readiness_score_report.csv')

    def save_advanced_ml_acceptance_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/manifest/manifest', df, summary)
    def load_advanced_ml_acceptance_manifest(self):
        return self._load_csv('advanced_ml_acceptance/manifest/manifest.csv')

    def save_advanced_ml_acceptance_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/health/health_check', df, summary)
    def load_advanced_ml_acceptance_health_check(self):
        return self._load_csv('advanced_ml_acceptance/health/health_check.csv')

    def save_advanced_ml_acceptance_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/validation/validation_report', df, summary)
    def load_advanced_ml_acceptance_validation_report(self):
        return self._load_csv('advanced_ml_acceptance/validation/validation_report.csv')

    def save_advanced_ml_acceptance_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/safety/safety_boundary', df, summary)
    def load_advanced_ml_acceptance_safety_boundary(self):
        return self._load_csv('advanced_ml_acceptance/safety/safety_boundary.csv')

    def save_phase_146_realistic_backtest_transaction_cost_slippage_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_ml_acceptance/handoff/phase_146_handoff', df, summary)
    def load_phase_146_realistic_backtest_transaction_cost_slippage_handoff_report(self):
        return self._load_csv('advanced_ml_acceptance/handoff/phase_146_handoff.csv')

    def save_advanced_ml_acceptance_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_ml_acceptance' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_advanced_ml_acceptance_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_ml_acceptance' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_advanced_ml_acceptance_reports(self):
        return pd.DataFrame()

    save_phase_146_handoff = save_phase_146_realistic_backtest_transaction_cost_slippage_handoff_report
    load_phase_146_handoff = load_phase_146_realistic_backtest_transaction_cost_slippage_handoff_report

    # Phase 146 Realistic Backtest, Transaction Cost and Slippage Modeling DataLake Methods
    def save_realistic_backtest_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/profiles/profile_registry', df, summary)
    def load_realistic_backtest_profile_registry(self):
        return self._load_csv('advanced_realistic_backtest/profiles/profile_registry.csv')

    def save_realistic_backtest_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/domains/domain_registry', df, summary)
    def load_realistic_backtest_domain_registry(self):
        return self._load_csv('advanced_realistic_backtest/domains/domain_registry.csv')

    def save_backtest_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/scope/scope_registry', df, summary)
    def load_backtest_scope_registry(self):
        return self._load_csv('advanced_realistic_backtest/scope/scope_registry.csv')

    def save_backtest_engine_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/engines/engine_contract_registry', df, summary)
    def load_backtest_engine_contract_registry(self):
        return self._load_csv('advanced_realistic_backtest/engines/engine_contract_registry.csv')

    def save_event_driven_backtest_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/event_driven/event_driven_registry', df, summary)
    def load_event_driven_backtest_contract_registry(self):
        return self._load_csv('advanced_realistic_backtest/event_driven/event_driven_registry.csv')

    def save_vectorized_backtest_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/vectorized/vectorized_registry', df, summary)
    def load_vectorized_backtest_contract_registry(self):
        return self._load_csv('advanced_realistic_backtest/vectorized/vectorized_registry.csv')

    def save_portfolio_backtest_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/portfolio/portfolio_registry', df, summary)
    def load_portfolio_backtest_contract_registry(self):
        return self._load_csv('advanced_realistic_backtest/portfolio/portfolio_registry.csv')

    def save_order_simulation_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/order_simulation/order_simulation_registry', df, summary)
    def load_order_simulation_contract_registry(self):
        return self._load_csv('advanced_realistic_backtest/order_simulation/order_simulation_registry.csv')

    def save_fill_model_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/fill_models/fill_model_registry', df, summary)
    def load_fill_model_contract_registry(self):
        return self._load_csv('advanced_realistic_backtest/fill_models/fill_model_registry.csv')

    def save_execution_price_model_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/execution_price/price_model_registry', df, summary)
    def load_execution_price_model_contract_registry(self):
        return self._load_csv('advanced_realistic_backtest/execution_price/price_model_registry.csv')

    def save_commission_model_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/commission_models/commission_registry', df, summary)
    def load_commission_model_contract_registry(self):
        return self._load_csv('advanced_realistic_backtest/commission_models/commission_registry.csv')

    def save_fee_model_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/fee_models/fee_registry', df, summary)
    def load_fee_model_contract_registry(self):
        return self._load_csv('advanced_realistic_backtest/fee_models/fee_registry.csv')

    def save_spread_model_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/spread_models/spread_registry', df, summary)
    def load_spread_model_contract_registry(self):
        return self._load_csv('advanced_realistic_backtest/spread_models/spread_registry.csv')

    def save_slippage_model_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/slippage_models/slippage_registry', df, summary)
    def load_slippage_model_contract_registry(self):
        return self._load_csv('advanced_realistic_backtest/slippage_models/slippage_registry.csv')

    def save_transaction_cost_model_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/cost_models/cost_model_registry', df, summary)
    def load_transaction_cost_model_registry(self):
        return self._load_csv('advanced_realistic_backtest/cost_models/cost_model_registry.csv')

    def save_transaction_cost_component_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/cost_components/component_registry', df, summary)
    def load_transaction_cost_component_registry(self):
        return self._load_csv('advanced_realistic_backtest/cost_components/component_registry.csv')

    def save_backtest_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/no_lookahead_guards/guard_registry', df, summary)
    def load_backtest_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_realistic_backtest/no_lookahead_guards/guard_registry.csv')

    def save_backtest_survivorship_bias_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/survivorship_guards/guard_registry', df, summary)
    def load_backtest_survivorship_bias_guard_registry(self):
        return self._load_csv('advanced_realistic_backtest/survivorship_guards/guard_registry.csv')

    def save_backtest_data_snooping_bias_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/data_snooping_guards/guard_registry', df, summary)
    def load_backtest_data_snooping_bias_guard_registry(self):
        return self._load_csv('advanced_realistic_backtest/data_snooping_guards/guard_registry.csv')

    def save_backtest_overfitting_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/overfitting_guards/guard_registry', df, summary)
    def load_backtest_overfitting_guard_registry(self):
        return self._load_csv('advanced_realistic_backtest/overfitting_guards/guard_registry.csv')

    def save_backtest_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/forbidden_column_policies/policy_registry', df, summary)
    def load_backtest_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_realistic_backtest/forbidden_column_policies/policy_registry.csv')

    def save_backtest_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/disabled_execution/execution_disabled', df, summary)
    def load_backtest_execution_disabled_report(self):
        return self._load_csv('advanced_realistic_backtest/disabled_execution/execution_disabled.csv')

    def save_backtest_optimizer_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/disabled_execution/optimizer_disabled', df, summary)
    def load_backtest_optimizer_disabled_report(self):
        return self._load_csv('advanced_realistic_backtest/disabled_execution/optimizer_disabled.csv')

    def save_backtest_walk_forward_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/disabled_execution/walk_forward_disabled', df, summary)
    def load_backtest_walk_forward_disabled_report(self):
        return self._load_csv('advanced_realistic_backtest/disabled_execution/walk_forward_disabled.csv')

    def save_backtest_benchmark_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/disabled_execution/benchmark_disabled', df, summary)
    def load_backtest_benchmark_disabled_report(self):
        return self._load_csv('advanced_realistic_backtest/disabled_execution/benchmark_disabled.csv')

    def save_backtest_live_trading_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/disabled_execution/live_trading_disabled', df, summary)
    def load_backtest_live_trading_disabled_report(self):
        return self._load_csv('advanced_realistic_backtest/disabled_execution/live_trading_disabled.csv')

    def save_backtest_broker_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/disabled_execution/broker_disabled', df, summary)
    def load_backtest_broker_execution_disabled_report(self):
        return self._load_csv('advanced_realistic_backtest/disabled_execution/broker_disabled.csv')

    def save_backtest_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/findings/findings_registry', df, summary)
    def load_backtest_findings_registry(self):
        return self._load_csv('advanced_realistic_backtest/findings/findings_registry.csv')

    def save_backtest_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/scoring/readiness_score_report', df, summary)
    def load_backtest_readiness_score_report(self):
        return self._load_csv('advanced_realistic_backtest/scoring/readiness_score_report.csv')

    def save_realistic_backtest_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/manifest/manifest', df, summary)
    def load_realistic_backtest_manifest(self):
        return self._load_csv('advanced_realistic_backtest/manifest/manifest.csv')

    def save_realistic_backtest_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/health/health_check', df, summary)
    def load_realistic_backtest_health_check(self):
        return self._load_csv('advanced_realistic_backtest/health/health_check.csv')

    def save_realistic_backtest_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/validation/validation_report', df, summary)
    def load_realistic_backtest_validation_report(self):
        return self._load_csv('advanced_realistic_backtest/validation/validation_report.csv')

    def save_realistic_backtest_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/safety/safety_boundary', df, summary)
    def load_realistic_backtest_safety_boundary(self):
        return self._load_csv('advanced_realistic_backtest/safety/safety_boundary.csv')

    def save_phase_147_walk_forward_oos_benchmark_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/handoff/phase_147_handoff', df, summary)
    def load_phase_147_walk_forward_oos_benchmark_handoff_report(self):
        return self._load_csv('advanced_realistic_backtest/handoff/phase_147_handoff.csv')

    def save_realistic_backtest_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_realistic_backtest' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_realistic_backtest_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_realistic_backtest' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_realistic_backtest_reports(self):
        return pd.DataFrame()

    def save_realistic_execution_assumptions(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/assumptions/assumption_registry', df, summary)
    def load_realistic_execution_assumptions(self):
        return self._load_csv('advanced_realistic_backtest/assumptions/assumption_registry.csv')

    def save_backtest_data_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/data_contracts/data_contract_registry', df, summary)
    def load_backtest_data_contracts(self):
        return self._load_csv('advanced_realistic_backtest/data_contracts/data_contract_registry.csv')

    def save_backtest_feature_input_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/feature_contracts/feature_contract_registry', df, summary)
    def load_backtest_feature_input_contracts(self):
        return self._load_csv('advanced_realistic_backtest/feature_contracts/feature_contract_registry.csv')

    def save_backtest_signal_input_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/signal_contracts/signal_contract_registry', df, summary)
    def load_backtest_signal_input_contracts(self):
        return self._load_csv('advanced_realistic_backtest/signal_contracts/signal_contract_registry.csv')

    def save_backtest_output_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/output_contracts/output_contract_registry', df, summary)
    def load_backtest_output_contracts(self):
        return self._load_csv('advanced_realistic_backtest/output_contracts/output_contract_registry.csv')

    def save_backtest_metric_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/metrics/metric_placeholder_registry', df, summary)
    def load_backtest_metric_placeholders(self):
        return self._load_csv('advanced_realistic_backtest/metrics/metric_placeholder_registry.csv')

    def save_pnl_accounting_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/accounting/pnl_accounting_registry', df, summary)
    def load_pnl_accounting_contracts(self):
        return self._load_csv('advanced_realistic_backtest/accounting/pnl_accounting_registry.csv')

    def save_cash_position_accounting_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/accounting/cash_position_registry', df, summary)
    def load_cash_position_accounting_contracts(self):
        return self._load_csv('advanced_realistic_backtest/accounting/cash_position_registry.csv')

    def save_leverage_margin_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/accounting/leverage_margin_registry', df, summary)
    def load_leverage_margin_placeholders(self):
        return self._load_csv('advanced_realistic_backtest/accounting/leverage_margin_registry.csv')

    def save_trade_lifecycle_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/lifecycle/trade_lifecycle_registry', df, summary)
    def load_trade_lifecycle_contracts(self):
        return self._load_csv('advanced_realistic_backtest/lifecycle/trade_lifecycle_registry.csv')

    def save_position_lifecycle_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/lifecycle/position_lifecycle_registry', df, summary)
    def load_position_lifecycle_contracts(self):
        return self._load_csv('advanced_realistic_backtest/lifecycle/position_lifecycle_registry.csv')

    def save_corporate_action_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/lifecycle/corporate_action_registry', df, summary)
    def load_corporate_action_placeholders(self):
        return self._load_csv('advanced_realistic_backtest/lifecycle/corporate_action_registry.csv')

    def save_currency_conversion_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/lifecycle/currency_conversion_registry', df, summary)
    def load_currency_conversion_placeholders(self):
        return self._load_csv('advanced_realistic_backtest/lifecycle/currency_conversion_registry.csv')

    def save_market_impact_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/execution_realism/market_impact_registry', df, summary)
    def load_market_impact_placeholders(self):
        return self._load_csv('advanced_realistic_backtest/execution_realism/market_impact_registry.csv')

    def save_latency_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/execution_realism/latency_registry', df, summary)
    def load_latency_placeholders(self):
        return self._load_csv('advanced_realistic_backtest/execution_realism/latency_registry.csv')

    def save_liquidity_constraint_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/execution_realism/liquidity_constraint_registry', df, summary)
    def load_liquidity_constraint_placeholders(self):
        return self._load_csv('advanced_realistic_backtest/execution_realism/liquidity_constraint_registry.csv')

    def save_partial_fill_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/execution_realism/partial_fill_registry', df, summary)
    def load_partial_fill_placeholders(self):
        return self._load_csv('advanced_realistic_backtest/execution_realism/partial_fill_registry.csv')

    def save_rejected_order_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/execution_realism/rejected_order_registry', df, summary)
    def load_rejected_order_placeholders(self):
        return self._load_csv('advanced_realistic_backtest/execution_realism/rejected_order_registry.csv')

    def save_order_book_depth_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/execution_realism/order_book_depth_registry', df, summary)
    def load_order_book_depth_placeholders(self):
        return self._load_csv('advanced_realistic_backtest/execution_realism/order_book_depth_registry.csv')

    def save_timezone_alignment_backtest_guards(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/timezone_guards/guard_registry', df, summary)
    def load_timezone_alignment_backtest_guards(self):
        return self._load_csv('advanced_realistic_backtest/timezone_guards/guard_registry.csv')

    def save_backtest_metadata_only_news_guards(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/news_guards/guard_registry', df, summary)
    def load_backtest_metadata_only_news_guards(self):
        return self._load_csv('advanced_realistic_backtest/news_guards/guard_registry.csv')

    def save_backtest_source_preservation_guards(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/source_guards/guard_registry', df, summary)
    def load_backtest_source_preservation_guards(self):
        return self._load_csv('advanced_realistic_backtest/source_guards/guard_registry.csv')

    def save_backtest_model_training_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/disabled_execution/model_training_disabled', df, summary)
    def load_backtest_model_training_disabled_report(self):
        return self._load_csv('advanced_realistic_backtest/disabled_execution/model_training_disabled.csv')

    def save_backtest_prediction_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/disabled_execution/prediction_disabled', df, summary)
    def load_backtest_prediction_disabled_report(self):
        return self._load_csv('advanced_realistic_backtest/disabled_execution/prediction_disabled.csv')

    def save_backtest_performance_claim_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/disabled_execution/performance_claim_disabled', df, summary)
    def load_backtest_performance_claim_disabled_report(self):
        return self._load_csv('advanced_realistic_backtest/disabled_execution/performance_claim_disabled.csv')

    def save_backtest_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/dependencies/dependency_registry', df, summary)
    def load_backtest_dependencies(self):
        return self._load_csv('advanced_realistic_backtest/dependencies/dependency_registry.csv')

    def save_backtest_validation_evidence(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/evidence/evidence_registry', df, summary)
    def load_backtest_validation_evidence(self):
        return self._load_csv('advanced_realistic_backtest/evidence/evidence_registry.csv')

    def save_backtest_manual_review(self, df, summary=None):
        return self._save_csv_json('advanced_realistic_backtest/review/manual_review_queue', df, summary)
    def load_backtest_manual_review(self):
        return self._load_csv('advanced_realistic_backtest/review/manual_review_queue.csv')

    save_phase_147_handoff = save_phase_147_walk_forward_oos_benchmark_handoff_report
    load_phase_147_handoff = load_phase_147_walk_forward_oos_benchmark_handoff_report

    # Phase 147 Walk-Forward Validation and Out-of-Sample Benchmarking Support
    def save_walk_forward_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/profiles/profile_registry', df, summary)
    def load_walk_forward_profile_registry(self):
        return self._load_csv('advanced_walk_forward_validation/profiles/profile_registry.csv')

    def save_walk_forward_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/domains/domain_registry', df, summary)
    def load_walk_forward_domain_registry(self):
        return self._load_csv('advanced_walk_forward_validation/domains/domain_registry.csv')

    def save_walk_forward_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/scopes/scope_registry', df, summary)
    def load_walk_forward_scope_registry(self):
        return self._load_csv('advanced_walk_forward_validation/scopes/scope_registry.csv')

    def save_walk_forward_validation_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/validation_contracts/validation_contract_registry', df, summary)
    def load_walk_forward_validation_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/validation_contracts/validation_contract_registry.csv')

    def save_rolling_window_validation_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/rolling_contracts/rolling_contract_registry', df, summary)
    def load_rolling_window_validation_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/rolling_contracts/rolling_contract_registry.csv')

    def save_expanding_window_validation_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/expanding_contracts/expanding_contract_registry', df, summary)
    def load_expanding_window_validation_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/expanding_contracts/expanding_contract_registry.csv')

    def save_anchored_window_validation_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/anchored_contracts/anchored_contract_registry', df, summary)
    def load_anchored_window_validation_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/anchored_contracts/anchored_contract_registry.csv')

    def save_purged_walk_forward_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/purged_contracts/purged_contract_registry', df, summary)
    def load_purged_walk_forward_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/purged_contracts/purged_contract_registry.csv')

    def save_embargo_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/embargo_policies/embargo_policy_registry', df, summary)
    def load_embargo_policy_registry(self):
        return self._load_csv('advanced_walk_forward_validation/embargo_policies/embargo_policy_registry.csv')

    def save_train_validation_test_split_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/train_val_test_splits/split_contract_registry', df, summary)
    def load_train_validation_test_split_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/train_val_test_splits/split_contract_registry.csv')

    def save_out_of_sample_split_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/oos_splits/oos_split_registry', df, summary)
    def load_out_of_sample_split_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/oos_splits/oos_split_registry.csv')

    def save_holdout_period_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/holdout_periods/holdout_registry', df, summary)
    def load_holdout_period_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/holdout_periods/holdout_registry.csv')

    def save_temporal_split_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/temporal_boundaries/boundary_registry', df, summary)
    def load_temporal_split_boundary_registry(self):
        return self._load_csv('advanced_walk_forward_validation/temporal_boundaries/boundary_registry.csv')

    def save_regime_aware_split_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/regime_aware_splits/regime_split_registry', df, summary)
    def load_regime_aware_split_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/regime_aware_splits/regime_split_registry.csv')

    def save_cross_asset_oos_split_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/cross_asset_splits/cross_asset_registry', df, summary)
    def load_cross_asset_oos_split_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/cross_asset_splits/cross_asset_registry.csv')

    def save_oos_benchmark_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/oos_benchmarks/benchmark_contract_registry', df, summary)
    def load_oos_benchmark_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/oos_benchmarks/benchmark_contract_registry.csv')

    def save_benchmark_universe_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/benchmark_universes/universe_registry', df, summary)
    def load_benchmark_universe_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/benchmark_universes/universe_registry.csv')

    def save_benchmark_baseline_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/benchmark_baselines/baseline_registry', df, summary)
    def load_benchmark_baseline_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/benchmark_baselines/baseline_registry.csv')

    def save_benchmark_comparison_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/benchmark_comparisons/comparison_registry', df, summary)
    def load_benchmark_comparison_contract_registry(self):
        return self._load_csv('advanced_walk_forward_validation/benchmark_comparisons/comparison_registry.csv')

    def save_benchmark_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/benchmark_metrics/metric_registry', df, summary)
    def load_benchmark_metric_placeholder_registry(self):
        return self._load_csv('advanced_walk_forward_validation/benchmark_metrics/metric_registry.csv')

    def save_oos_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/oos_metrics/metric_registry', df, summary)
    def load_oos_metric_placeholder_registry(self):
        return self._load_csv('advanced_walk_forward_validation/oos_metrics/metric_registry.csv')

    def save_validation_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/validation_metrics/metric_registry', df, summary)
    def load_validation_metric_placeholder_registry(self):
        return self._load_csv('advanced_walk_forward_validation/validation_metrics/metric_registry.csv')

    def save_validation_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/guards/no_lookahead_registry', df, summary)
    def load_validation_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_walk_forward_validation/guards/no_lookahead_registry.csv')

    def save_validation_purge_embargo_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/guards/purge_embargo_registry', df, summary)
    def load_validation_purge_embargo_guard_registry(self):
        return self._load_csv('advanced_walk_forward_validation/guards/purge_embargo_registry.csv')

    def save_validation_data_snooping_bias_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/guards/data_snooping_registry', df, summary)
    def load_validation_data_snooping_bias_guard_registry(self):
        return self._load_csv('advanced_walk_forward_validation/guards/data_snooping_registry.csv')

    def save_validation_overfitting_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/guards/overfitting_registry', df, summary)
    def load_validation_overfitting_guard_registry(self):
        return self._load_csv('advanced_walk_forward_validation/guards/overfitting_registry.csv')

    def save_validation_survivorship_bias_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/guards/survivorship_registry', df, summary)
    def load_validation_survivorship_bias_guard_registry(self):
        return self._load_csv('advanced_walk_forward_validation/guards/survivorship_registry.csv')

    def save_validation_multiple_testing_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/guards/multiple_testing_registry', df, summary)
    def load_validation_multiple_testing_guard_registry(self):
        return self._load_csv('advanced_walk_forward_validation/guards/multiple_testing_registry.csv')

    def save_validation_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/guards/forbidden_column_registry', df, summary)
    def load_validation_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_walk_forward_validation/guards/forbidden_column_registry.csv')

    def save_walk_forward_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/disabled_execution/walk_forward_disabled', df, summary)
    def load_walk_forward_execution_disabled_report(self):
        return self._load_csv('advanced_walk_forward_validation/disabled_execution/walk_forward_disabled.csv')

    def save_oos_benchmark_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/disabled_execution/oos_benchmark_disabled', df, summary)
    def load_oos_benchmark_execution_disabled_report(self):
        return self._load_csv('advanced_walk_forward_validation/disabled_execution/oos_benchmark_disabled.csv')

    def save_benchmark_metric_calculation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/disabled_execution/metric_calc_disabled', df, summary)
    def load_benchmark_metric_calculation_disabled_report(self):
        return self._load_csv('advanced_walk_forward_validation/disabled_execution/metric_calc_disabled.csv')

    def save_validation_optimizer_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/disabled_execution/optimizer_disabled', df, summary)
    def load_validation_optimizer_disabled_report(self):
        return self._load_csv('advanced_walk_forward_validation/disabled_execution/optimizer_disabled.csv')

    def save_validation_live_trading_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/disabled_execution/live_trading_disabled', df, summary)
    def load_validation_live_trading_disabled_report(self):
        return self._load_csv('advanced_walk_forward_validation/disabled_execution/live_trading_disabled.csv')

    def save_validation_broker_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/disabled_execution/broker_disabled', df, summary)
    def load_validation_broker_execution_disabled_report(self):
        return self._load_csv('advanced_walk_forward_validation/disabled_execution/broker_disabled.csv')

    def save_validation_model_training_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/disabled_execution/model_training_disabled', df, summary)
    def load_validation_model_training_disabled_report(self):
        return self._load_csv('advanced_walk_forward_validation/disabled_execution/model_training_disabled.csv')

    def save_validation_prediction_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/disabled_execution/prediction_disabled', df, summary)
    def load_validation_prediction_disabled_report(self):
        return self._load_csv('advanced_walk_forward_validation/disabled_execution/prediction_disabled.csv')

    def save_validation_performance_claim_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/disabled_execution/performance_claim_disabled', df, summary)
    def load_validation_performance_claim_disabled_report(self):
        return self._load_csv('advanced_walk_forward_validation/disabled_execution/performance_claim_disabled.csv')

    def save_validation_evidence(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/evidence/validation_evidence', df, summary)
    def load_validation_evidence(self):
        return self._load_csv('advanced_walk_forward_validation/evidence/validation_evidence.csv')
    save_validation_evidence_registry = save_validation_evidence
    load_validation_evidence_registry = load_validation_evidence

    def save_walk_forward_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/manual_review/manual_review_queue', df, summary)
    def load_walk_forward_manual_review_queue(self):
        return self._load_csv('advanced_walk_forward_validation/manual_review/manual_review_queue.csv')

    def save_walk_forward_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/findings/findings_registry', df, summary)
    def load_walk_forward_findings_registry(self):
        return self._load_csv('advanced_walk_forward_validation/findings/findings_registry.csv')

    def save_walk_forward_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/scoring/readiness_score_report', df, summary)
    def load_walk_forward_readiness_score_report(self):
        return self._load_csv('advanced_walk_forward_validation/scoring/readiness_score_report.csv')

    def save_walk_forward_validation_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/manifest/manifest', df, summary)
    def load_walk_forward_validation_manifest(self):
        return self._load_csv('advanced_walk_forward_validation/manifest/manifest.csv')
    save_walk_forward_manifest = save_walk_forward_validation_manifest
    load_walk_forward_manifest = load_walk_forward_validation_manifest

    def save_walk_forward_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/health/health_check', df, summary)
    def load_walk_forward_health_check(self):
        return self._load_csv('advanced_walk_forward_validation/health/health_check.csv')

    def save_walk_forward_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/validation/validation_report', df, summary)
    def load_walk_forward_validation_report(self):
        return self._load_csv('advanced_walk_forward_validation/validation/validation_report.csv')

    def save_walk_forward_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/safety/safety_boundary', df, summary)
    def load_walk_forward_safety_boundary(self):
        return self._load_csv('advanced_walk_forward_validation/safety/safety_boundary.csv')

    def save_phase_148_stress_testing_scenario_simulation_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_walk_forward_validation/handoff/phase_148_handoff', df, summary)
    def load_phase_148_stress_testing_scenario_simulation_handoff_report(self):
        return self._load_csv('advanced_walk_forward_validation/handoff/phase_148_handoff.csv')
    save_phase_148_handoff = save_phase_148_stress_testing_scenario_simulation_handoff_report
    load_phase_148_handoff = load_phase_148_stress_testing_scenario_simulation_handoff_report

    def save_walk_forward_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_walk_forward_validation' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_walk_forward_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_walk_forward_validation' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_walk_forward_reports(self):
        return pd.DataFrame()

    # Phase 148 Stress Testing and Scenario Simulation DataLake Support
    def save_stress_testing_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/profiles/profile_registry', df, summary)
    def load_stress_testing_profile_registry(self):
        return self._load_csv('advanced_stress_testing/profiles/profile_registry.csv')

    def save_stress_testing_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/domains/domain_registry', df, summary)
    def load_stress_testing_domain_registry(self):
        return self._load_csv('advanced_stress_testing/domains/domain_registry.csv')

    def save_stress_testing_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/scopes/scope_registry', df, summary)
    def load_stress_testing_scope_registry(self):
        return self._load_csv('advanced_stress_testing/scopes/scope_registry.csv')

    def save_stress_scenario_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/scenario_contracts/scenario_contract_registry', df, summary)
    def load_stress_scenario_contract_registry(self):
        return self._load_csv('advanced_stress_testing/scenario_contracts/scenario_contract_registry.csv')

    def save_historical_stress_scenario_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/historical_scenarios/historical_registry', df, summary)
    def load_historical_stress_scenario_contract_registry(self):
        return self._load_csv('advanced_stress_testing/historical_scenarios/historical_registry.csv')

    def save_hypothetical_stress_scenario_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/hypothetical_scenarios/hypothetical_registry', df, summary)
    def load_hypothetical_stress_scenario_contract_registry(self):
        return self._load_csv('advanced_stress_testing/hypothetical_scenarios/hypothetical_registry.csv')

    def save_regime_shock_scenario_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/regime_shocks/regime_shock_registry', df, summary)
    def load_regime_shock_scenario_contract_registry(self):
        return self._load_csv('advanced_stress_testing/regime_shocks/regime_shock_registry.csv')

    def save_volatility_shock_scenario_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/volatility_shocks/volatility_shock_registry', df, summary)
    def load_volatility_shock_scenario_contract_registry(self):
        return self._load_csv('advanced_stress_testing/volatility_shocks/volatility_shock_registry.csv')

    def save_liquidity_shock_scenario_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/liquidity_shocks/liquidity_shock_registry', df, summary)
    def load_liquidity_shock_scenario_contract_registry(self):
        return self._load_csv('advanced_stress_testing/liquidity_shocks/liquidity_shock_registry.csv')

    def save_spread_widening_scenario_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/spread_widening/spread_widening_registry', df, summary)
    def load_spread_widening_scenario_contract_registry(self):
        return self._load_csv('advanced_stress_testing/spread_widening/spread_widening_registry.csv')

    def save_gap_risk_scenario_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/shock_placeholders/gap_risk_registry', df, summary)
    def load_gap_risk_scenario_placeholder_registry(self):
        return self._load_csv('advanced_stress_testing/shock_placeholders/gap_risk_registry.csv')

    def save_correlation_breakdown_scenario_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/shock_placeholders/correlation_breakdown_registry', df, summary)
    def load_correlation_breakdown_scenario_placeholder_registry(self):
        return self._load_csv('advanced_stress_testing/shock_placeholders/correlation_breakdown_registry.csv')

    def save_macro_shock_scenario_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/shock_placeholders/macro_shock_registry', df, summary)
    def load_macro_shock_scenario_placeholder_registry(self):
        return self._load_csv('advanced_stress_testing/shock_placeholders/macro_shock_registry.csv')

    def save_cross_asset_contagion_scenario_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/shock_placeholders/cross_asset_contagion_registry', df, summary)
    def load_cross_asset_contagion_scenario_placeholder_registry(self):
        return self._load_csv('advanced_stress_testing/shock_placeholders/cross_asset_contagion_registry.csv')

    def save_transaction_cost_shock_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/cost_slippage_shocks/transaction_cost_shock_registry', df, summary)
    def load_transaction_cost_shock_contract_registry(self):
        return self._load_csv('advanced_stress_testing/cost_slippage_shocks/transaction_cost_shock_registry.csv')

    def save_slippage_shock_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/cost_slippage_shocks/slippage_shock_registry', df, summary)
    def load_slippage_shock_contract_registry(self):
        return self._load_csv('advanced_stress_testing/cost_slippage_shocks/slippage_shock_registry.csv')

    def save_stress_scenario_library_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/scenario_library/library_registry', df, summary)
    def load_stress_scenario_library_registry(self):
        return self._load_csv('advanced_stress_testing/scenario_library/library_registry.csv')

    def save_stress_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/metric_placeholders/metric_registry', df, summary)
    def load_stress_metric_placeholder_registry(self):
        return self._load_csv('advanced_stress_testing/metric_placeholders/metric_registry.csv')

    def save_scenario_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/metric_placeholders/scenario_metric_registry', df, summary)
    def load_scenario_metric_placeholder_registry(self):
        return self._load_csv('advanced_stress_testing/metric_placeholders/scenario_metric_registry.csv')

    def save_robustness_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/metric_placeholders/robustness_metric_registry', df, summary)
    def load_robustness_metric_placeholder_registry(self):
        return self._load_csv('advanced_stress_testing/metric_placeholders/robustness_metric_registry.csv')

    def save_stress_no_lookahead_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/guards/no_lookahead_registry', df, summary)
    def load_stress_no_lookahead_guard_registry(self):
        return self._load_csv('advanced_stress_testing/guards/no_lookahead_registry.csv')

    def save_stress_scenario_leakage_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/guards/scenario_leakage_registry', df, summary)
    def load_stress_scenario_leakage_guard_registry(self):
        return self._load_csv('advanced_stress_testing/guards/scenario_leakage_registry.csv')

    def save_stress_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/guards/forbidden_column_registry', df, summary)
    def load_stress_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_stress_testing/guards/forbidden_column_registry.csv')

    def save_stress_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/disabled_execution/stress_execution_disabled', df, summary)
    def load_stress_execution_disabled_report(self):
        return self._load_csv('advanced_stress_testing/disabled_execution/stress_execution_disabled.csv')

    def save_scenario_simulation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/disabled_execution/scenario_simulation_disabled', df, summary)
    def load_scenario_simulation_disabled_report(self):
        return self._load_csv('advanced_stress_testing/disabled_execution/scenario_simulation_disabled.csv')

    def save_stress_metric_calculation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/disabled_execution/metric_calc_disabled', df, summary)
    def load_stress_metric_calculation_disabled_report(self):
        return self._load_csv('advanced_stress_testing/disabled_execution/metric_calc_disabled.csv')

    def save_stress_live_trading_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/disabled_execution/live_trading_disabled', df, summary)
    def load_stress_live_trading_disabled_report(self):
        return self._load_csv('advanced_stress_testing/disabled_execution/live_trading_disabled.csv')

    def save_stress_broker_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/disabled_execution/broker_disabled', df, summary)
    def load_stress_broker_execution_disabled_report(self):
        return self._load_csv('advanced_stress_testing/disabled_execution/broker_disabled.csv')

    def save_stress_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/findings/findings_registry', df, summary)
    def load_stress_findings_registry(self):
        return self._load_csv('advanced_stress_testing/findings/findings_registry.csv')

    def save_stress_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/scoring/readiness_score_report', df, summary)
    def load_stress_readiness_score_report(self):
        return self._load_csv('advanced_stress_testing/scoring/readiness_score_report.csv')

    def save_stress_testing_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/manifest/manifest', df, summary)
    def load_stress_testing_manifest(self):
        return self._load_csv('advanced_stress_testing/manifest/manifest.csv')

    def save_stress_testing_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/health/health_check', df, summary)
    def load_stress_testing_health_check(self):
        return self._load_csv('advanced_stress_testing/health/health_check.csv')

    def save_stress_testing_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/validation/validation_report', df, summary)
    def load_stress_testing_validation_report(self):
        return self._load_csv('advanced_stress_testing/validation/validation_report.csv')

    def save_stress_testing_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/safety/safety_boundary', df, summary)
    def load_stress_testing_safety_boundary(self):
        return self._load_csv('advanced_stress_testing/safety/safety_boundary.csv')

    def save_phase_149_monte_carlo_robustness_parameter_stability_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_stress_testing/handoff/phase_149_handoff', df, summary)
    def load_phase_149_monte_carlo_robustness_parameter_stability_handoff_report(self):
        return self._load_csv('advanced_stress_testing/handoff/phase_149_handoff.csv')
    save_phase_149_handoff = save_phase_149_monte_carlo_robustness_parameter_stability_handoff_report
    load_phase_149_handoff = load_phase_149_monte_carlo_robustness_parameter_stability_handoff_report

    def save_stress_testing_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_stress_testing' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_stress_testing_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_stress_testing' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_stress_testing_reports(self):
        return pd.DataFrame()

    # ---------------------------------------------------------
    # PHASE 149: ADVANCED MONTE CARLO ROBUSTNESS CONTRACTS
    # ---------------------------------------------------------
    def save_monte_carlo_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/profiles/profile_registry', df, summary)
    def load_monte_carlo_profile_registry(self):
        return self._load_csv('advanced_monte_carlo_robustness/profiles/profile_registry.csv')

    def save_monte_carlo_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/domains/domain_registry', df, summary)
    def load_monte_carlo_domain_registry(self):
        return self._load_csv('advanced_monte_carlo_robustness/domains/domain_registry.csv')

    def save_monte_carlo_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/scopes/scope_registry', df, summary)
    def load_monte_carlo_scope_registry(self):
        return self._load_csv('advanced_monte_carlo_robustness/scopes/scope_registry.csv')

    def save_monte_carlo_robustness_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/contracts/robustness_contracts', df, summary)
    def load_monte_carlo_robustness_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/contracts/robustness_contracts.csv')

    def save_bootstrap_simulation_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/contracts/bootstrap_simulation_contracts', df, summary)
    def load_bootstrap_simulation_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/contracts/bootstrap_simulation_contracts.csv')

    def save_block_bootstrap_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/contracts/block_bootstrap_contracts', df, summary)
    def load_block_bootstrap_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/contracts/block_bootstrap_contracts.csv')

    def save_stationary_bootstrap_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/contracts/stationary_bootstrap_contracts', df, summary)
    def load_stationary_bootstrap_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/contracts/stationary_bootstrap_contracts.csv')

    def save_return_path_resampling_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/contracts/return_path_resampling_contracts', df, summary)
    def load_return_path_resampling_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/contracts/return_path_resampling_contracts.csv')

    def save_trade_sequence_reshuffling_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/contracts/trade_sequence_reshuffling_contracts', df, summary)
    def load_trade_sequence_reshuffling_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/contracts/trade_sequence_reshuffling_contracts.csv')

    def save_residual_resampling_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/resampling/residual_resampling_placeholders', df, summary)
    def load_residual_resampling_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/resampling/residual_resampling_placeholders.csv')

    def save_noise_injection_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/resampling/noise_injection_placeholders', df, summary)
    def load_noise_injection_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/resampling/noise_injection_placeholders.csv')

    def save_path_perturbation_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/resampling/path_perturbation_placeholders', df, summary)
    def load_path_perturbation_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/resampling/path_perturbation_placeholders.csv')

    def save_parameter_stability_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/parameter_stability/stability_contracts', df, summary)
    def load_parameter_stability_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/parameter_stability/stability_contracts.csv')

    def save_parameter_sensitivity_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/parameter_stability/sensitivity_contracts', df, summary)
    def load_parameter_sensitivity_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/parameter_stability/sensitivity_contracts.csv')

    def save_parameter_perturbation_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/parameter_stability/perturbation_contracts', df, summary)
    def load_parameter_perturbation_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/parameter_stability/perturbation_contracts.csv')

    def save_parameter_grid_stability_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/parameter_stability/grid_stability_placeholders', df, summary)
    def load_parameter_grid_stability_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/parameter_stability/grid_stability_placeholders.csv')

    def save_parameter_surface_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/parameter_stability/surface_placeholders', df, summary)
    def load_parameter_surface_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/parameter_stability/surface_placeholders.csv')

    def save_parameter_fragility_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/parameter_stability/fragility_placeholders', df, summary)
    def load_parameter_fragility_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/parameter_stability/fragility_placeholders.csv')

    def save_robustness_envelope_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/envelopes/envelope_placeholders', df, summary)
    def load_robustness_envelope_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/envelopes/envelope_placeholders.csv')

    def save_stability_band_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/envelopes/stability_band_placeholders', df, summary)
    def load_stability_band_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/envelopes/stability_band_placeholders.csv')

    def save_confidence_interval_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/envelopes/confidence_interval_placeholders', df, summary)
    def load_confidence_interval_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/envelopes/confidence_interval_placeholders.csv')

    def save_drawdown_distribution_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/envelopes/drawdown_distribution_placeholders', df, summary)
    def load_drawdown_distribution_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/envelopes/drawdown_distribution_placeholders.csv')

    def save_return_distribution_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/envelopes/return_distribution_placeholders', df, summary)
    def load_return_distribution_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/envelopes/return_distribution_placeholders.csv')

    def save_tail_risk_distribution_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/envelopes/tail_risk_distribution_placeholders', df, summary)
    def load_tail_risk_distribution_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/envelopes/tail_risk_distribution_placeholders.csv')

    def save_worst_case_path_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/envelopes/worst_case_path_placeholders', df, summary)
    def load_worst_case_path_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/envelopes/worst_case_path_placeholders.csv')

    def save_best_case_path_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/envelopes/best_case_path_placeholders', df, summary)
    def load_best_case_path_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/envelopes/best_case_path_placeholders.csv')

    def save_median_case_path_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/envelopes/median_case_path_placeholders', df, summary)
    def load_median_case_path_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/envelopes/median_case_path_placeholders.csv')

    def save_scenario_resampling_linkage(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/dependencies/scenario_resampling_linkage', df, summary)
    def load_scenario_resampling_linkage(self):
        return self._load_csv('advanced_monte_carlo_robustness/dependencies/scenario_resampling_linkage.csv')

    def save_stress_monte_carlo_linkage(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/dependencies/stress_monte_carlo_linkage', df, summary)
    def load_stress_monte_carlo_linkage(self):
        return self._load_csv('advanced_monte_carlo_robustness/dependencies/stress_monte_carlo_linkage.csv')

    def save_walk_forward_monte_carlo_linkage(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/dependencies/walk_forward_monte_carlo_linkage', df, summary)
    def load_walk_forward_monte_carlo_linkage(self):
        return self._load_csv('advanced_monte_carlo_robustness/dependencies/walk_forward_monte_carlo_linkage.csv')

    def save_realistic_backtest_monte_carlo_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/dependencies/backtest_dependencies', df, summary)
    def load_realistic_backtest_monte_carlo_dependencies(self):
        return self._load_csv('advanced_monte_carlo_robustness/dependencies/backtest_dependencies.csv')

    def save_transaction_cost_monte_carlo_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/dependencies/transaction_cost_dependencies', df, summary)
    def load_transaction_cost_monte_carlo_dependencies(self):
        return self._load_csv('advanced_monte_carlo_robustness/dependencies/transaction_cost_dependencies.csv')

    def save_slippage_monte_carlo_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/dependencies/slippage_dependencies', df, summary)
    def load_slippage_monte_carlo_dependencies(self):
        return self._load_csv('advanced_monte_carlo_robustness/dependencies/slippage_dependencies.csv')

    def save_regime_monte_carlo_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/dependencies/regime_dependencies', df, summary)
    def load_regime_monte_carlo_dependencies(self):
        return self._load_csv('advanced_monte_carlo_robustness/dependencies/regime_dependencies.csv')

    def save_governance_monte_carlo_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/dependencies/governance_dependencies', df, summary)
    def load_governance_monte_carlo_dependencies(self):
        return self._load_csv('advanced_monte_carlo_robustness/dependencies/governance_dependencies.csv')

    def save_monte_carlo_input_data_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/io_contracts/input_data_contracts', df, summary)
    def load_monte_carlo_input_data_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/io_contracts/input_data_contracts.csv')

    def save_monte_carlo_feature_input_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/io_contracts/feature_input_contracts', df, summary)
    def load_monte_carlo_feature_input_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/io_contracts/feature_input_contracts.csv')

    def save_monte_carlo_signal_input_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/io_contracts/signal_input_contracts', df, summary)
    def load_monte_carlo_signal_input_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/io_contracts/signal_input_contracts.csv')

    def save_monte_carlo_output_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/io_contracts/output_contracts', df, summary)
    def load_monte_carlo_output_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/io_contracts/output_contracts.csv')

    def save_robustness_output_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/io_contracts/robustness_output_contracts', df, summary)
    def load_robustness_output_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/io_contracts/robustness_output_contracts.csv')

    def save_parameter_stability_output_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/io_contracts/stability_output_contracts', df, summary)
    def load_parameter_stability_output_contracts(self):
        return self._load_csv('advanced_monte_carlo_robustness/io_contracts/stability_output_contracts.csv')

    def save_monte_carlo_metric_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/metrics/mc_metric_placeholders', df, summary)
    def load_monte_carlo_metric_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/metrics/mc_metric_placeholders.csv')

    def save_robustness_metric_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/metrics/robustness_metric_placeholders', df, summary)
    def load_robustness_metric_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/metrics/robustness_metric_placeholders.csv')

    def save_parameter_stability_metric_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/metrics/stability_metric_placeholders', df, summary)
    def load_parameter_stability_metric_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/metrics/stability_metric_placeholders.csv')

    def save_fragility_metric_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/metrics/fragility_metric_placeholders', df, summary)
    def load_fragility_metric_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/metrics/fragility_metric_placeholders.csv')

    def save_distribution_metric_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/metrics/distribution_metric_placeholders', df, summary)
    def load_distribution_metric_placeholders(self):
        return self._load_csv('advanced_monte_carlo_robustness/metrics/distribution_metric_placeholders.csv')

    def save_monte_carlo_no_lookahead_guards(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/guards/no_lookahead_guards', df, summary)
    def load_monte_carlo_no_lookahead_guards(self):
        return self._load_csv('advanced_monte_carlo_robustness/guards/no_lookahead_guards.csv')

    def save_monte_carlo_resampling_leakage_guards(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/guards/resampling_leakage_guards', df, summary)
    def load_monte_carlo_resampling_leakage_guards(self):
        return self._load_csv('advanced_monte_carlo_robustness/guards/resampling_leakage_guards.csv')

    def save_monte_carlo_data_snooping_bias_guards(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/guards/data_snooping_guards', df, summary)
    def load_monte_carlo_data_snooping_bias_guards(self):
        return self._load_csv('advanced_monte_carlo_robustness/guards/data_snooping_guards.csv')

    def save_monte_carlo_overfitting_guards(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/guards/overfitting_guards', df, summary)
    def load_monte_carlo_overfitting_guards(self):
        return self._load_csv('advanced_monte_carlo_robustness/guards/overfitting_guards.csv')

    def save_monte_carlo_survivorship_bias_guards(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/guards/survivorship_bias_guards', df, summary)
    def load_monte_carlo_survivorship_bias_guards(self):
        return self._load_csv('advanced_monte_carlo_robustness/guards/survivorship_bias_guards.csv')

    def save_monte_carlo_multiple_testing_guards(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/guards/multiple_testing_guards', df, summary)
    def load_monte_carlo_multiple_testing_guards(self):
        return self._load_csv('advanced_monte_carlo_robustness/guards/multiple_testing_guards.csv')

    def save_monte_carlo_metadata_only_news_guards(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/guards/metadata_only_news_guards', df, summary)
    def load_monte_carlo_metadata_only_news_guards(self):
        return self._load_csv('advanced_monte_carlo_robustness/guards/metadata_only_news_guards.csv')

    def save_monte_carlo_source_preservation_guards(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/guards/source_preservation_guards', df, summary)
    def load_monte_carlo_source_preservation_guards(self):
        return self._load_csv('advanced_monte_carlo_robustness/guards/source_preservation_guards.csv')

    def save_monte_carlo_forbidden_column_policies(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/guards/forbidden_column_policies', df, summary)
    def load_monte_carlo_forbidden_column_policies(self):
        return self._load_csv('advanced_monte_carlo_robustness/guards/forbidden_column_policies.csv')

    def save_monte_carlo_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/disabled_execution/mc_disabled', df, summary)
    def load_monte_carlo_execution_disabled_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/disabled_execution/mc_disabled.csv')

    def save_bootstrap_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/disabled_execution/bootstrap_disabled', df, summary)
    def load_bootstrap_execution_disabled_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/disabled_execution/bootstrap_disabled.csv')

    def save_parameter_optimization_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/disabled_execution/param_opt_disabled', df, summary)
    def load_parameter_optimization_disabled_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/disabled_execution/param_opt_disabled.csv')

    def save_parameter_sweep_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/disabled_execution/sweep_disabled', df, summary)
    def load_parameter_sweep_execution_disabled_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/disabled_execution/sweep_disabled.csv')

    def save_monte_carlo_metric_calculation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/disabled_execution/metric_calc_disabled', df, summary)
    def load_monte_carlo_metric_calculation_disabled_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/disabled_execution/metric_calc_disabled.csv')

    def save_monte_carlo_model_training_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/disabled_execution/model_train_disabled', df, summary)
    def load_monte_carlo_model_training_disabled_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/disabled_execution/model_train_disabled.csv')

    def save_monte_carlo_prediction_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/disabled_execution/prediction_disabled', df, summary)
    def load_monte_carlo_prediction_disabled_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/disabled_execution/prediction_disabled.csv')

    def save_monte_carlo_live_trading_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/disabled_execution/live_trading_disabled', df, summary)
    def load_monte_carlo_live_trading_disabled_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/disabled_execution/live_trading_disabled.csv')

    def save_monte_carlo_broker_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/disabled_execution/broker_disabled', df, summary)
    def load_monte_carlo_broker_execution_disabled_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/disabled_execution/broker_disabled.csv')

    def save_monte_carlo_performance_claim_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/disabled_execution/perf_claim_disabled', df, summary)
    def load_monte_carlo_performance_claim_disabled_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/disabled_execution/perf_claim_disabled.csv')

    def save_monte_carlo_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/findings/manual_review_queue', df, summary)
    def load_monte_carlo_manual_review_queue(self):
        return self._load_csv('advanced_monte_carlo_robustness/findings/manual_review_queue.csv')

    def save_monte_carlo_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/findings/findings_registry', df, summary)
    def load_monte_carlo_findings_registry(self):
        return self._load_csv('advanced_monte_carlo_robustness/findings/findings_registry.csv')

    def save_monte_carlo_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/scoring/readiness_score_report', df, summary)
    def load_monte_carlo_readiness_score_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/scoring/readiness_score_report.csv')

    def save_monte_carlo_robustness_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/manifest/manifest', df, summary)
    def load_monte_carlo_robustness_manifest(self):
        return self._load_csv('advanced_monte_carlo_robustness/manifest/manifest.csv')

    def save_monte_carlo_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/health/health_check', df, summary)
    def load_monte_carlo_health_check(self):
        return self._load_csv('advanced_monte_carlo_robustness/health/health_check.csv')

    def save_monte_carlo_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/validation/validation_report', df, summary)
    def load_monte_carlo_validation_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/validation/validation_report.csv')

    def save_monte_carlo_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/safety/safety_boundary', df, summary)
    def load_monte_carlo_safety_boundary(self):
        return self._load_csv('advanced_monte_carlo_robustness/safety/safety_boundary.csv')

    def save_phase_150_backtest_governance_bias_control_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_monte_carlo_robustness/handoff/phase_150_handoff', df, summary)
    def load_phase_150_backtest_governance_bias_control_handoff_report(self):
        return self._load_csv('advanced_monte_carlo_robustness/handoff/phase_150_handoff.csv')
    save_phase_150_handoff = save_phase_150_backtest_governance_bias_control_handoff_report
    load_phase_150_handoff = load_phase_150_backtest_governance_bias_control_handoff_report

    def save_monte_carlo_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_monte_carlo_robustness' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_monte_carlo_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_monte_carlo_robustness' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_monte_carlo_reports(self):
        return pd.DataFrame()

    # =========================================================================
    # Phase 150: Advanced Backtest Governance & Bias Control
    # =========================================================================
    def save_backtest_governance_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/profiles/profile_registry', df, summary)
    def load_backtest_governance_profile_registry(self):
        return self._load_csv('advanced_backtest_governance/profiles/profile_registry.csv')

    def save_backtest_governance_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/domains/domain_registry', df, summary)
    def load_backtest_governance_domain_registry(self):
        return self._load_csv('advanced_backtest_governance/domains/domain_registry.csv')

    def save_backtest_governance_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/scopes/scope_registry', df, summary)
    def load_backtest_governance_scope_registry(self):
        return self._load_csv('advanced_backtest_governance/scopes/scope_registry.csv')

    def save_backtest_governance_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/contracts/governance_contracts', df, summary)
    def load_backtest_governance_contracts(self):
        return self._load_csv('advanced_backtest_governance/contracts/governance_contracts.csv')

    def save_backtest_bias_control_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/contracts/bias_control_contracts', df, summary)
    def load_backtest_bias_control_contracts(self):
        return self._load_csv('advanced_backtest_governance/contracts/bias_control_contracts.csv')

    def save_backtest_result_reporting_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/contracts/result_reporting_contracts', df, summary)
    def load_backtest_result_reporting_contracts(self):
        return self._load_csv('advanced_backtest_governance/contracts/result_reporting_contracts.csv')

    def save_backtest_metric_claim_boundaries(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/boundaries/metric_claim_boundaries', df, summary)
    def load_backtest_metric_claim_boundaries(self):
        return self._load_csv('advanced_backtest_governance/boundaries/metric_claim_boundaries.csv')

    def save_backtest_performance_claim_boundaries(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/boundaries/performance_claim_boundaries', df, summary)
    def load_backtest_performance_claim_boundaries(self):
        return self._load_csv('advanced_backtest_governance/boundaries/performance_claim_boundaries.csv')

    def save_backtest_result_disclosure_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/placeholders/result_disclosure_placeholders', df, summary)
    def load_backtest_result_disclosure_placeholders(self):
        return self._load_csv('advanced_backtest_governance/placeholders/result_disclosure_placeholders.csv')

    def save_lookahead_bias_controls(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/bias_controls/lookahead_bias_controls', df, summary)
    def load_lookahead_bias_controls(self):
        return self._load_csv('advanced_backtest_governance/bias_controls/lookahead_bias_controls.csv')

    def save_survivorship_bias_controls(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/bias_controls/survivorship_bias_controls', df, summary)
    def load_survivorship_bias_controls(self):
        return self._load_csv('advanced_backtest_governance/bias_controls/survivorship_bias_controls.csv')

    def save_data_snooping_bias_controls(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/bias_controls/data_snooping_bias_controls', df, summary)
    def load_data_snooping_bias_controls(self):
        return self._load_csv('advanced_backtest_governance/bias_controls/data_snooping_bias_controls.csv')

    def save_overfitting_bias_controls(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/bias_controls/overfitting_bias_controls', df, summary)
    def load_overfitting_bias_controls(self):
        return self._load_csv('advanced_backtest_governance/bias_controls/overfitting_bias_controls.csv')

    def save_multiple_testing_bias_controls(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/bias_controls/multiple_testing_bias_controls', df, summary)
    def load_multiple_testing_bias_controls(self):
        return self._load_csv('advanced_backtest_governance/bias_controls/multiple_testing_bias_controls.csv')

    def save_parameter_fishing_bias_controls(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/bias_controls/parameter_fishing_bias_controls', df, summary)
    def load_parameter_fishing_bias_controls(self):
        return self._load_csv('advanced_backtest_governance/bias_controls/parameter_fishing_bias_controls.csv')

    def save_benchmark_selection_bias_controls(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/bias_controls/benchmark_selection_bias_controls', df, summary)
    def load_benchmark_selection_bias_controls(self):
        return self._load_csv('advanced_backtest_governance/bias_controls/benchmark_selection_bias_controls.csv')

    def save_regime_coverage_bias_controls(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/bias_controls/regime_coverage_bias_controls', df, summary)
    def load_regime_coverage_bias_controls(self):
        return self._load_csv('advanced_backtest_governance/bias_controls/regime_coverage_bias_controls.csv')

    def save_sample_coverage_bias_controls(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/bias_controls/sample_coverage_bias_controls', df, summary)
    def load_sample_coverage_bias_controls(self):
        return self._load_csv('advanced_backtest_governance/bias_controls/sample_coverage_bias_controls.csv')

    def save_transaction_cost_realism_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/realism/transaction_cost_realism', df, summary)
    def load_transaction_cost_realism_governance(self):
        return self._load_csv('advanced_backtest_governance/realism/transaction_cost_realism.csv')

    def save_slippage_realism_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/realism/slippage_realism', df, summary)
    def load_slippage_realism_governance(self):
        return self._load_csv('advanced_backtest_governance/realism/slippage_realism.csv')

    def save_fill_model_realism_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/realism/fill_model_realism', df, summary)
    def load_fill_model_realism_governance(self):
        return self._load_csv('advanced_backtest_governance/realism/fill_model_realism.csv')

    def save_liquidity_realism_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/realism/liquidity_realism', df, summary)
    def load_liquidity_realism_governance(self):
        return self._load_csv('advanced_backtest_governance/realism/liquidity_realism.csv')

    def save_timestamp_integrity_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/time_series/timestamp_integrity', df, summary)
    def load_timestamp_integrity_governance(self):
        return self._load_csv('advanced_backtest_governance/time_series/timestamp_integrity.csv')

    def save_split_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/splits/split_governance', df, summary)
    def load_split_governance(self):
        return self._load_csv('advanced_backtest_governance/splits/split_governance.csv')

    def save_walk_forward_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/splits/walk_forward_governance', df, summary)
    def load_walk_forward_governance(self):
        return self._load_csv('advanced_backtest_governance/splits/walk_forward_governance.csv')

    def save_oos_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/splits/oos_governance', df, summary)
    def load_oos_governance(self):
        return self._load_csv('advanced_backtest_governance/splits/oos_governance.csv')

    def save_stress_testing_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/robustness/stress_testing_governance', df, summary)
    def load_stress_testing_governance(self):
        return self._load_csv('advanced_backtest_governance/robustness/stress_testing_governance.csv')

    def save_monte_carlo_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/robustness/monte_carlo_governance', df, summary)
    def load_monte_carlo_governance(self):
        return self._load_csv('advanced_backtest_governance/robustness/monte_carlo_governance.csv')

    def save_benchmark_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/robustness/benchmark_governance', df, summary)
    def load_benchmark_governance(self):
        return self._load_csv('advanced_backtest_governance/robustness/benchmark_governance.csv')

    def save_scenario_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/robustness/scenario_governance', df, summary)
    def load_scenario_governance(self):
        return self._load_csv('advanced_backtest_governance/robustness/scenario_governance.csv')

    def save_parameter_stability_governance(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/robustness/parameter_stability_governance', df, summary)
    def load_parameter_stability_governance(self):
        return self._load_csv('advanced_backtest_governance/robustness/parameter_stability_governance.csv')

    def save_backtest_audit_policies(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/policies/audit_policies', df, summary)
    def load_backtest_audit_policies(self):
        return self._load_csv('advanced_backtest_governance/policies/audit_policies.csv')

    def save_backtest_evidence_policies(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/policies/evidence_policies', df, summary)
    def load_backtest_evidence_policies(self):
        return self._load_csv('advanced_backtest_governance/policies/evidence_policies.csv')

    def save_backtest_manual_review_gates(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/gates/manual_review_gates', df, summary)
    def load_backtest_manual_review_gates(self):
        return self._load_csv('advanced_backtest_governance/gates/manual_review_gates.csv')

    def save_backtest_go_no_go_boundaries(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/gates/go_no_go_boundaries', df, summary)
    def load_backtest_go_no_go_boundaries(self):
        return self._load_csv('advanced_backtest_governance/gates/go_no_go_boundaries.csv')

    def save_backtest_result_release_boundaries(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/boundaries/result_release_boundaries', df, summary)
    def load_backtest_result_release_boundaries(self):
        return self._load_csv('advanced_backtest_governance/boundaries/result_release_boundaries.csv')

    def save_backtest_report_disclaimers(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/policies/report_disclaimers', df, summary)
    def load_backtest_report_disclaimers(self):
        return self._load_csv('advanced_backtest_governance/policies/report_disclaimers.csv')

    def save_backtest_source_preservation_guards(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/guards/source_preservation_guards', df, summary)
    def load_backtest_source_preservation_guards(self):
        return self._load_csv('advanced_backtest_governance/guards/source_preservation_guards.csv')

    def save_backtest_metadata_only_news_guards(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/guards/metadata_only_news_guards', df, summary)
    def load_backtest_metadata_only_news_guards(self):
        return self._load_csv('advanced_backtest_governance/guards/metadata_only_news_guards.csv')

    def save_backtest_forbidden_column_policies(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/guards/forbidden_column_policies', df, summary)
    def load_backtest_forbidden_column_policies(self):
        return self._load_csv('advanced_backtest_governance/guards/forbidden_column_policies.csv')

    def save_backtest_governance_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/disabled_execution/governance_execution_disabled', df, summary)
    def load_backtest_governance_execution_disabled_report(self):
        return self._load_csv('advanced_backtest_governance/disabled_execution/governance_execution_disabled.csv')

    def save_backtest_result_claim_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/disabled_execution/result_claim_disabled', df, summary)
    def load_backtest_result_claim_disabled_report(self):
        return self._load_csv('advanced_backtest_governance/disabled_execution/result_claim_disabled.csv')

    def save_backtest_metric_calculation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/disabled_execution/metric_calc_disabled', df, summary)
    def load_backtest_metric_calculation_disabled_report(self):
        return self._load_csv('advanced_backtest_governance/disabled_execution/metric_calc_disabled.csv')

    def save_backtest_optimizer_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/disabled_execution/optimizer_disabled', df, summary)
    def load_backtest_optimizer_disabled_report(self):
        return self._load_csv('advanced_backtest_governance/disabled_execution/optimizer_disabled.csv')

    def save_backtest_model_training_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/disabled_execution/model_training_disabled', df, summary)
    def load_backtest_model_training_disabled_report(self):
        return self._load_csv('advanced_backtest_governance/disabled_execution/model_training_disabled.csv')

    def save_backtest_prediction_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/disabled_execution/prediction_disabled', df, summary)
    def load_backtest_prediction_disabled_report(self):
        return self._load_csv('advanced_backtest_governance/disabled_execution/prediction_disabled.csv')

    def save_backtest_live_trading_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/disabled_execution/live_trading_disabled', df, summary)
    def load_backtest_live_trading_disabled_report(self):
        return self._load_csv('advanced_backtest_governance/disabled_execution/live_trading_disabled.csv')

    def save_backtest_broker_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/disabled_execution/broker_execution_disabled', df, summary)
    def load_backtest_broker_execution_disabled_report(self):
        return self._load_csv('advanced_backtest_governance/disabled_execution/broker_execution_disabled.csv')

    def save_backtest_deployment_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/disabled_execution/deployment_disabled', df, summary)
    def load_backtest_deployment_disabled_report(self):
        return self._load_csv('advanced_backtest_governance/disabled_execution/deployment_disabled.csv')

    def save_backtest_governance_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/dependencies/dependencies', df, summary)
    def load_backtest_governance_dependencies(self):
        return self._load_csv('advanced_backtest_governance/dependencies/dependencies.csv')

    def save_backtest_governance_validation_evidence(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/evidence/validation_evidence', df, summary)
    def load_backtest_governance_validation_evidence(self):
        return self._load_csv('advanced_backtest_governance/evidence/validation_evidence.csv')

    def save_backtest_governance_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/findings/manual_review_queue', df, summary)
    def load_backtest_governance_manual_review_queue(self):
        return self._load_csv('advanced_backtest_governance/findings/manual_review_queue.csv')

    def save_backtest_governance_findings(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/findings/findings_registry', df, summary)
    def load_backtest_governance_findings(self):
        return self._load_csv('advanced_backtest_governance/findings/findings_registry.csv')

    def save_backtest_governance_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/scoring/readiness_score_report', df, summary)
    def load_backtest_governance_readiness_score_report(self):
        return self._load_csv('advanced_backtest_governance/scoring/readiness_score_report.csv')

    def save_backtest_governance_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/manifest/manifest', df, summary)
    def load_backtest_governance_manifest(self):
        return self._load_csv('advanced_backtest_governance/manifest/manifest.csv')

    def save_backtest_governance_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/health/health_check', df, summary)
    def load_backtest_governance_health_check(self):
        return self._load_csv('advanced_backtest_governance/health/health_check.csv')

    def save_backtest_governance_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/validation/validation_report', df, summary)
    def load_backtest_governance_validation_report(self):
        return self._load_csv('advanced_backtest_governance/validation/validation_report.csv')

    def save_backtest_governance_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/safety/safety_boundary', df, summary)
    def load_backtest_governance_safety_boundary(self):
        return self._load_csv('advanced_backtest_governance/safety/safety_boundary.csv')

    def save_phase_151_benchmark_strategy_evaluation_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_governance/handoff/phase_151_handoff', df, summary)
    def load_phase_151_benchmark_strategy_evaluation_handoff_report(self):
        return self._load_csv('advanced_backtest_governance/handoff/phase_151_handoff.csv')
    save_phase_151_handoff = save_phase_151_benchmark_strategy_evaluation_handoff_report
    load_phase_151_handoff = load_phase_151_benchmark_strategy_evaluation_handoff_report

    def save_backtest_governance_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_backtest_governance' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_backtest_governance_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_backtest_governance' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_backtest_governance_reports(self):
        return pd.DataFrame()

    # Phase 151 Advanced Benchmark Evaluation and Strategy Evaluation Reports DataLake Support
    def save_benchmark_evaluation_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/profiles/profile_registry', df, summary)
    def load_benchmark_evaluation_profile_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/profiles/profile_registry.csv')

    def save_benchmark_evaluation_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/domains/domain_registry', df, summary)
    def load_benchmark_evaluation_domain_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/domains/domain_registry.csv')

    def save_benchmark_evaluation_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/scopes/scope_registry', df, summary)
    def load_benchmark_evaluation_scope_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/scopes/scope_registry.csv')

    def save_benchmark_comparison_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/contracts/benchmark_comparison_report_contracts', df, summary)
    def load_benchmark_comparison_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/contracts/benchmark_comparison_report_contracts.csv')

    def save_strategy_evaluation_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/contracts/strategy_evaluation_report_contracts', df, summary)
    def load_strategy_evaluation_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/contracts/strategy_evaluation_report_contracts.csv')

    def save_benchmark_universe_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/universe/benchmark_universe_report_contracts', df, summary)
    def load_benchmark_universe_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/universe/benchmark_universe_report_contracts.csv')

    def save_benchmark_baseline_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/baselines/benchmark_baseline_report_contracts', df, summary)
    def load_benchmark_baseline_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/baselines/benchmark_baseline_report_contracts.csv')

    def save_strategy_vs_benchmark_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/strategy_vs_benchmark/strategy_vs_benchmark_report_contracts', df, summary)
    def load_strategy_vs_benchmark_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/strategy_vs_benchmark/strategy_vs_benchmark_report_contracts.csv')

    def save_cost_adjusted_evaluation_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/cost_adjusted/cost_adjusted_report_contracts', df, summary)
    def load_cost_adjusted_evaluation_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/cost_adjusted/cost_adjusted_report_contracts.csv')

    def save_slippage_adjusted_evaluation_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/slippage_adjusted/slippage_adjusted_report_contracts', df, summary)
    def load_slippage_adjusted_evaluation_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/slippage_adjusted/slippage_adjusted_report_contracts.csv')

    def save_regime_aware_evaluation_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/regime_aware/regime_aware_report_contracts', df, summary)
    def load_regime_aware_evaluation_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/regime_aware/regime_aware_report_contracts.csv')

    def save_walk_forward_evaluation_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/walk_forward/walk_forward_report_contracts', df, summary)
    def load_walk_forward_evaluation_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/walk_forward/walk_forward_report_contracts.csv')

    def save_oos_evaluation_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/oos/oos_report_contracts', df, summary)
    def load_oos_evaluation_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/oos/oos_report_contracts.csv')

    def save_stress_aware_evaluation_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/stress_aware/stress_aware_report_contracts', df, summary)
    def load_stress_aware_evaluation_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/stress_aware/stress_aware_report_contracts.csv')

    def save_monte_carlo_robustness_evaluation_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/monte_carlo/monte_carlo_report_contracts', df, summary)
    def load_monte_carlo_robustness_evaluation_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/monte_carlo/monte_carlo_report_contracts.csv')

    def save_parameter_stability_evaluation_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/contracts/parameter_stability_report_contracts', df, summary)
    def load_parameter_stability_evaluation_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/contracts/parameter_stability_report_contracts.csv')

    def save_governance_aware_evaluation_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/governance/governance_aware_report_contracts', df, summary)
    def load_governance_aware_evaluation_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/governance/governance_aware_report_contracts.csv')

    def save_bias_control_evaluation_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/governance/bias_control_report_contracts', df, summary)
    def load_bias_control_evaluation_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/governance/bias_control_report_contracts.csv')

    def save_result_disclosure_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/reports/result_disclosure_report_contracts', df, summary)
    def load_result_disclosure_report_contract_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/reports/result_disclosure_report_contracts.csv')

    def save_strategy_evaluation_summary_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/placeholders/strategy_evaluation_summary_placeholders', df, summary)
    def load_strategy_evaluation_summary_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/placeholders/strategy_evaluation_summary_placeholders.csv')

    def save_benchmark_comparison_summary_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/placeholders/benchmark_comparison_summary_placeholders', df, summary)
    def load_benchmark_comparison_summary_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/placeholders/benchmark_comparison_summary_placeholders.csv')

    def save_metric_summary_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/placeholders/metric_summary_placeholders', df, summary)
    def load_metric_summary_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/placeholders/metric_summary_placeholders.csv')

    def save_risk_summary_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/placeholders/risk_summary_placeholders', df, summary)
    def load_risk_summary_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/placeholders/risk_summary_placeholders.csv')

    def save_cost_impact_summary_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/placeholders/cost_impact_summary_placeholders', df, summary)
    def load_cost_impact_summary_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/placeholders/cost_impact_summary_placeholders.csv')

    def save_slippage_impact_summary_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/placeholders/slippage_impact_summary_placeholders', df, summary)
    def load_slippage_impact_summary_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/placeholders/slippage_impact_summary_placeholders.csv')

    def save_regime_performance_summary_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/placeholders/regime_performance_summary_placeholders', df, summary)
    def load_regime_performance_summary_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/placeholders/regime_performance_summary_placeholders.csv')

    def save_stress_result_summary_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/placeholders/stress_result_summary_placeholders', df, summary)
    def load_stress_result_summary_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/placeholders/stress_result_summary_placeholders.csv')

    def save_monte_carlo_result_summary_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/placeholders/monte_carlo_result_summary_placeholders', df, summary)
    def load_monte_carlo_result_summary_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/placeholders/monte_carlo_result_summary_placeholders.csv')

    def save_strategy_limitation_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/placeholders/strategy_limitation_placeholders', df, summary)
    def load_strategy_limitation_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/placeholders/strategy_limitation_placeholders.csv')

    def save_benchmark_limitation_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/placeholders/benchmark_limitation_placeholders', df, summary)
    def load_benchmark_limitation_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/placeholders/benchmark_limitation_placeholders.csv')

    def save_strategy_evaluation_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/metrics/strategy_evaluation_metric_placeholders', df, summary)
    def load_strategy_evaluation_metric_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/metrics/strategy_evaluation_metric_placeholders.csv')

    def save_benchmark_comparison_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/metrics/benchmark_comparison_metric_placeholders', df, summary)
    def load_benchmark_comparison_metric_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/metrics/benchmark_comparison_metric_placeholders.csv')

    def save_relative_performance_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/metrics/relative_performance_metric_placeholders', df, summary)
    def load_relative_performance_metric_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/metrics/relative_performance_metric_placeholders.csv')

    def save_risk_adjusted_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/metrics/risk_adjusted_metric_placeholders', df, summary)
    def load_risk_adjusted_metric_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/metrics/risk_adjusted_metric_placeholders.csv')

    def save_cost_adjusted_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/metrics/cost_adjusted_metric_placeholders', df, summary)
    def load_cost_adjusted_metric_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/metrics/cost_adjusted_metric_placeholders.csv')

    def save_robustness_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/metrics/robustness_metric_placeholders', df, summary)
    def load_robustness_metric_placeholder_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/metrics/robustness_metric_placeholders.csv')

    def save_evaluation_result_claim_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/guards/result_claim_guards', df, summary)
    def load_evaluation_result_claim_guard_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/guards/result_claim_guards.csv')

    def save_evaluation_performance_claim_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/guards/performance_claim_guards', df, summary)
    def load_evaluation_performance_claim_guard_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/guards/performance_claim_guards.csv')

    def save_evaluation_strategy_approval_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/guards/strategy_approval_guards', df, summary)
    def load_evaluation_strategy_approval_guard_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/guards/strategy_approval_guards.csv')

    def save_evaluation_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/guards/forbidden_column_policies', df, summary)
    def load_evaluation_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/guards/forbidden_column_policies.csv')

    def save_benchmark_report_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/disabled_execution/benchmark_report_execution_disabled', df, summary)
    def load_benchmark_report_execution_disabled_report(self):
        return self._load_csv('advanced_benchmark_evaluation/disabled_execution/benchmark_report_execution_disabled.csv')

    def save_strategy_evaluation_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/disabled_execution/strategy_evaluation_execution_disabled', df, summary)
    def load_strategy_evaluation_execution_disabled_report(self):
        return self._load_csv('advanced_benchmark_evaluation/disabled_execution/strategy_evaluation_execution_disabled.csv')

    def save_evaluation_metric_calculation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/disabled_execution/evaluation_metric_calculation_disabled', df, summary)
    def load_evaluation_metric_calculation_disabled_report(self):
        return self._load_csv('advanced_benchmark_evaluation/disabled_execution/evaluation_metric_calculation_disabled.csv')

    def save_evaluation_result_claim_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/disabled_execution/evaluation_result_claim_disabled', df, summary)
    def load_evaluation_result_claim_disabled_report(self):
        return self._load_csv('advanced_benchmark_evaluation/disabled_execution/evaluation_result_claim_disabled.csv')

    def save_evaluation_strategy_approval_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/disabled_execution/evaluation_strategy_approval_disabled', df, summary)
    def load_evaluation_strategy_approval_disabled_report(self):
        return self._load_csv('advanced_benchmark_evaluation/disabled_execution/evaluation_strategy_approval_disabled.csv')

    def save_evaluation_live_trading_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/disabled_execution/evaluation_live_trading_disabled', df, summary)
    def load_evaluation_live_trading_disabled_report(self):
        return self._load_csv('advanced_benchmark_evaluation/disabled_execution/evaluation_live_trading_disabled.csv')

    def save_evaluation_broker_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/disabled_execution/evaluation_broker_execution_disabled', df, summary)
    def load_evaluation_broker_execution_disabled_report(self):
        return self._load_csv('advanced_benchmark_evaluation/disabled_execution/evaluation_broker_execution_disabled.csv')

    def save_benchmark_evaluation_dependencies(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/dependencies/dependencies', df, summary)
    def load_benchmark_evaluation_dependencies(self):
        return self._load_csv('advanced_benchmark_evaluation/dependencies/dependencies.csv')

    def save_benchmark_evaluation_validation_evidence(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/evidence/validation_evidence', df, summary)
    def load_benchmark_evaluation_validation_evidence(self):
        return self._load_csv('advanced_benchmark_evaluation/evidence/validation_evidence.csv')

    def save_benchmark_evaluation_manual_review_queue(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/manual_review/manual_review_queue', df, summary)
    def load_benchmark_evaluation_manual_review_queue(self):
        return self._load_csv('advanced_benchmark_evaluation/manual_review/manual_review_queue.csv')

    def save_benchmark_evaluation_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/findings/findings_registry', df, summary)
    def load_benchmark_evaluation_findings_registry(self):
        return self._load_csv('advanced_benchmark_evaluation/findings/findings_registry.csv')

    def save_benchmark_evaluation_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/scoring/readiness_score_report', df, summary)
    def load_benchmark_evaluation_readiness_score_report(self):
        return self._load_csv('advanced_benchmark_evaluation/scoring/readiness_score_report.csv')

    def save_benchmark_evaluation_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/manifest/manifest', df, summary)
    def load_benchmark_evaluation_manifest(self):
        return self._load_csv('advanced_benchmark_evaluation/manifest/manifest.csv')

    def save_benchmark_evaluation_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/health/health_check', df, summary)
    def load_benchmark_evaluation_health_check(self):
        return self._load_csv('advanced_benchmark_evaluation/health/health_check.csv')

    def save_benchmark_evaluation_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/validation/validation_report', df, summary)
    def load_benchmark_evaluation_validation_report(self):
        return self._load_csv('advanced_benchmark_evaluation/validation/validation_report.csv')

    def save_benchmark_evaluation_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/safety/safety_boundary', df, summary)
    def load_benchmark_evaluation_safety_boundary(self):
        return self._load_csv('advanced_benchmark_evaluation/safety/safety_boundary.csv')

    def save_phase_152_backtest_acceptance_report_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_benchmark_evaluation/handoff/phase_152_handoff', df, summary)
    def load_phase_152_backtest_acceptance_report_handoff_report(self):
        return self._load_csv('advanced_benchmark_evaluation/handoff/phase_152_handoff.csv')
    save_phase_152_handoff = save_phase_152_backtest_acceptance_report_handoff_report
    load_phase_152_handoff = load_phase_152_backtest_acceptance_report_handoff_report

    def save_benchmark_evaluation_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_benchmark_evaluation' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_benchmark_evaluation_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_benchmark_evaluation' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_benchmark_evaluation_reports(self):
        return pd.DataFrame()

    # Phase 152 Backtest Acceptance Report Methods
    def save_backtest_acceptance_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/profiles/profile_registry', df, summary)
    def load_backtest_acceptance_profile_registry(self):
        return self._load_csv('advanced_backtest_acceptance/profiles/profile_registry.csv')

    def save_backtest_acceptance_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/domains/domain_registry', df, summary)
    def load_backtest_acceptance_domain_registry(self):
        return self._load_csv('advanced_backtest_acceptance/domains/domain_registry.csv')

    def save_backtest_acceptance_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/scopes/scope_registry', df, summary)
    def load_backtest_acceptance_scope_registry(self):
        return self._load_csv('advanced_backtest_acceptance/scopes/scope_registry.csv')

    def save_backtest_acceptance_component_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/components/component_registry', df, summary)
    def load_backtest_acceptance_component_registry(self):
        return self._load_csv('advanced_backtest_acceptance/components/component_registry.csv')

    def save_backtest_acceptance_component_checkpoint_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/checkpoints/checkpoint_registry', df, summary)
    def load_backtest_acceptance_component_checkpoint_registry(self):
        return self._load_csv('advanced_backtest_acceptance/checkpoints/checkpoint_registry.csv')

    def save_phase_146_realistic_backtest_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/phase_acceptance/phase_146_acceptance', df, summary)
    def load_phase_146_realistic_backtest_acceptance_registry(self):
        return self._load_csv('advanced_backtest_acceptance/phase_acceptance/phase_146_acceptance.csv')

    def save_phase_147_walk_forward_oos_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/phase_acceptance/phase_147_acceptance', df, summary)
    def load_phase_147_walk_forward_oos_acceptance_registry(self):
        return self._load_csv('advanced_backtest_acceptance/phase_acceptance/phase_147_acceptance.csv')

    def save_phase_148_stress_testing_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/phase_acceptance/phase_148_acceptance', df, summary)
    def load_phase_148_stress_testing_acceptance_registry(self):
        return self._load_csv('advanced_backtest_acceptance/phase_acceptance/phase_148_acceptance.csv')

    def save_phase_149_monte_carlo_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/phase_acceptance/phase_149_acceptance', df, summary)
    def load_phase_149_monte_carlo_acceptance_registry(self):
        return self._load_csv('advanced_backtest_acceptance/phase_acceptance/phase_149_acceptance.csv')

    def save_phase_150_backtest_governance_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/phase_acceptance/phase_150_acceptance', df, summary)
    def load_phase_150_backtest_governance_acceptance_registry(self):
        return self._load_csv('advanced_backtest_acceptance/phase_acceptance/phase_150_acceptance.csv')

    def save_phase_151_benchmark_evaluation_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/phase_acceptance/phase_151_acceptance', df, summary)
    def load_phase_151_benchmark_evaluation_acceptance_registry(self):
        return self._load_csv('advanced_backtest_acceptance/phase_acceptance/phase_151_acceptance.csv')

    def save_backtest_acceptance_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/dependencies/dependency_registry', df, summary)
    def load_backtest_acceptance_dependency_registry(self):
        return self._load_csv('advanced_backtest_acceptance/dependencies/dependency_registry.csv')

    def save_backtest_acceptance_validation_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/evidence/validation_evidence_registry', df, summary)
    def load_backtest_acceptance_validation_evidence_registry(self):
        return self._load_csv('advanced_backtest_acceptance/evidence/validation_evidence_registry.csv')

    def save_backtest_acceptance_safety_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/safety/safety_boundary_registry', df, summary)
    def load_backtest_acceptance_safety_boundary_registry(self):
        return self._load_csv('advanced_backtest_acceptance/safety/safety_boundary_registry.csv')

    def save_backtest_acceptance_non_production_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/boundaries/non_production_boundary_registry', df, summary)
    def load_backtest_acceptance_non_production_boundary_registry(self):
        return self._load_csv('advanced_backtest_acceptance/boundaries/non_production_boundary_registry.csv')

    def save_backtest_acceptance_manual_review_gate_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/manual_review/manual_review_gate_registry', df, summary)
    def load_backtest_acceptance_manual_review_gate_registry(self):
        return self._load_csv('advanced_backtest_acceptance/manual_review/manual_review_gate_registry.csv')

    def save_backtest_acceptance_go_no_go_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/boundaries/go_no_go_boundary_registry', df, summary)
    def load_backtest_acceptance_go_no_go_boundary_registry(self):
        return self._load_csv('advanced_backtest_acceptance/boundaries/go_no_go_boundary_registry.csv')

    def save_backtest_acceptance_blocker_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/blockers/blocker_registry', df, summary)
    def load_backtest_acceptance_blocker_registry(self):
        return self._load_csv('advanced_backtest_acceptance/blockers/blocker_registry.csv')

    def save_backtest_acceptance_gap_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/gaps/gap_registry', df, summary)
    def load_backtest_acceptance_gap_registry(self):
        return self._load_csv('advanced_backtest_acceptance/gaps/gap_registry.csv')

    def save_backtest_acceptance_warning_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/warnings/warning_registry', df, summary)
    def load_backtest_acceptance_warning_registry(self):
        return self._load_csv('advanced_backtest_acceptance/warnings/warning_registry.csv')

    def save_backtest_acceptance_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/findings/findings_registry', df, summary)
    def load_backtest_acceptance_findings_registry(self):
        return self._load_csv('advanced_backtest_acceptance/findings/findings_registry.csv')

    def save_backtest_acceptance_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/scoring/readiness_score_report', df, summary)
    def load_backtest_acceptance_readiness_score_report(self):
        return self._load_csv('advanced_backtest_acceptance/scoring/readiness_score_report.csv')

    def save_backtest_acceptance_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/manifest/manifest', df, summary)
    def load_backtest_acceptance_manifest(self):
        return self._load_csv('advanced_backtest_acceptance/manifest/manifest.csv')

    def save_backtest_acceptance_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/health/health_check', df, summary)
    def load_backtest_acceptance_health_check(self):
        return self._load_csv('advanced_backtest_acceptance/health/health_check.csv')

    def save_backtest_acceptance_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/validation/validation_report', df, summary)
    def load_backtest_acceptance_validation_report(self):
        return self._load_csv('advanced_backtest_acceptance/validation/validation_report.csv')

    def save_backtest_acceptance_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/safety/safety_boundary', df, summary)
    def load_backtest_acceptance_safety_boundary(self):
        return self._load_csv('advanced_backtest_acceptance/safety/safety_boundary.csv')

    def save_phase_153_portfolio_construction_position_sizing_risk_budgeting_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_backtest_acceptance/handoff/phase_153_handoff', df, summary)
    def load_phase_153_portfolio_construction_position_sizing_risk_budgeting_handoff_report(self):
        return self._load_csv('advanced_backtest_acceptance/handoff/phase_153_handoff.csv')
    save_phase_153_handoff = save_phase_153_portfolio_construction_position_sizing_risk_budgeting_handoff_report
    load_phase_153_handoff = load_phase_153_portfolio_construction_position_sizing_risk_budgeting_handoff_report

    def save_backtest_acceptance_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_backtest_acceptance' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_backtest_acceptance_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_backtest_acceptance' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_backtest_acceptance_reports(self):
        return pd.DataFrame()

    # =========================================================================
    # Phase 153: Advanced Portfolio Construction, Position Sizing, and Risk Budgeting
    # =========================================================================
    def save_portfolio_construction_table(self, table_name: str, df: pd.DataFrame, summary: dict | None = None):
        return self._save_csv_json(f'advanced_portfolio_construction/{table_name}/{table_name}', df, summary)

    def load_portfolio_construction_table(self, table_name: str):
        return self._load_csv(f'advanced_portfolio_construction/{table_name}/{table_name}.csv')

    def save_portfolio_construction_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/profiles/profile_registry', df, summary)
    def load_portfolio_construction_profile_registry(self):
        return self._load_csv('advanced_portfolio_construction/profiles/profile_registry.csv')

    def save_portfolio_construction_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/contracts/contract_registry', df, summary)
    def load_portfolio_construction_contract_registry(self):
        return self._load_csv('advanced_portfolio_construction/contracts/contract_registry.csv')

    def save_portfolio_universe_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/universe/universe_contract_registry', df, summary)
    def load_portfolio_universe_contract_registry(self):
        return self._load_csv('advanced_portfolio_construction/universe/universe_contract_registry.csv')

    def save_portfolio_asset_eligibility_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/eligibility/asset_eligibility_contract_registry', df, summary)
    def load_portfolio_asset_eligibility_contract_registry(self):
        return self._load_csv('advanced_portfolio_construction/eligibility/asset_eligibility_contract_registry.csv')

    def save_portfolio_signal_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/signals/signal_input_contract_registry', df, summary)
    def load_portfolio_signal_input_contract_registry(self):
        return self._load_csv('advanced_portfolio_construction/signals/signal_input_contract_registry.csv')

    def save_portfolio_risk_input_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/risks/risk_input_contract_registry', df, summary)
    def load_portfolio_risk_input_contract_registry(self):
        return self._load_csv('advanced_portfolio_construction/risks/risk_input_contract_registry.csv')

    def save_position_sizing_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/position_sizing/position_sizing_contract_registry', df, summary)
    def load_position_sizing_contract_registry(self):
        return self._load_csv('advanced_portfolio_construction/position_sizing/position_sizing_contract_registry.csv')

    def save_fixed_fractional_sizing_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/sizing_placeholders/fixed_fractional', df, summary)
    def load_fixed_fractional_sizing_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_construction/sizing_placeholders/fixed_fractional.csv')

    def save_volatility_targeting_sizing_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/sizing_placeholders/volatility_targeting', df, summary)
    def load_volatility_targeting_sizing_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_construction/sizing_placeholders/volatility_targeting.csv')

    def save_risk_parity_sizing_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/sizing_placeholders/risk_parity', df, summary)
    def load_risk_parity_sizing_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_construction/sizing_placeholders/risk_parity.csv')

    def save_drawdown_aware_sizing_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/sizing_placeholders/drawdown_aware', df, summary)
    def load_drawdown_aware_sizing_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_construction/sizing_placeholders/drawdown_aware.csv')

    def save_risk_budget_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/risk_budget/risk_budget_contract_registry', df, summary)
    def load_risk_budget_contract_registry(self):
        return self._load_csv('advanced_portfolio_construction/risk_budget/risk_budget_contract_registry.csv')

    def save_per_asset_risk_budget_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/risk_budget/per_asset_risk_budget', df, summary)
    def load_per_asset_risk_budget_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_construction/risk_budget/per_asset_risk_budget.csv')

    def save_per_strategy_risk_budget_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/risk_budget/per_strategy_risk_budget', df, summary)
    def load_per_strategy_risk_budget_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_construction/risk_budget/per_strategy_risk_budget.csv')

    def save_per_regime_risk_budget_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/risk_budget/per_regime_risk_budget', df, summary)
    def load_per_regime_risk_budget_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_construction/risk_budget/per_regime_risk_budget.csv')

    def save_portfolio_risk_budget_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/risk_budget/portfolio_risk_budget', df, summary)
    def load_portfolio_risk_budget_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_construction/risk_budget/portfolio_risk_budget.csv')

    def save_concentration_limit_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/limits/concentration_limit_contract_registry', df, summary)
    def load_concentration_limit_contract_registry(self):
        return self._load_csv('advanced_portfolio_construction/limits/concentration_limit_contract_registry.csv')

    def save_exposure_limit_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/limits/exposure_limit_contract_registry', df, summary)
    def load_exposure_limit_contract_registry(self):
        return self._load_csv('advanced_portfolio_construction/limits/exposure_limit_contract_registry.csv')

    def save_leverage_limit_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/limits/leverage_limit_placeholder_registry', df, summary)
    def load_leverage_limit_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_construction/limits/leverage_limit_placeholder_registry.csv')

    def save_margin_limit_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/limits/margin_limit_placeholder_registry', df, summary)
    def load_margin_limit_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_construction/limits/margin_limit_placeholder_registry.csv')

    def save_notional_limit_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/limits/notional_limit_placeholder_registry', df, summary)
    def load_notional_limit_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_construction/limits/notional_limit_placeholder_registry.csv')

    def save_portfolio_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/findings/findings_registry', df, summary)
    def load_portfolio_findings_registry(self):
        return self._load_csv('advanced_portfolio_construction/findings/findings_registry.csv')

    def save_portfolio_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/scoring/readiness_score_report', df, summary)
    def load_portfolio_readiness_score_report(self):
        return self._load_csv('advanced_portfolio_construction/scoring/readiness_score_report.csv')

    def save_portfolio_construction_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/manifest/manifest', df, summary)
    def load_portfolio_construction_manifest(self):
        return self._load_csv('advanced_portfolio_construction/manifest/manifest.csv')

    def save_portfolio_construction_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/health/health_check', df, summary)
    def load_portfolio_construction_health_check(self):
        return self._load_csv('advanced_portfolio_construction/health/health_check.csv')

    def save_portfolio_construction_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/validation/validation_report', df, summary)
    def load_portfolio_construction_validation_report(self):
        return self._load_csv('advanced_portfolio_construction/validation/validation_report.csv')

    def save_portfolio_construction_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/safety/safety_boundary', df, summary)
    def load_portfolio_construction_safety_boundary(self):
        return self._load_csv('advanced_portfolio_construction/safety/safety_boundary.csv')

    def save_phase_154_portfolio_construction_position_sizing_risk_budgeting_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_construction/handoff/phase_154_handoff', df, summary)
    def load_phase_154_portfolio_construction_position_sizing_risk_budgeting_handoff_report(self):
        return self._load_csv('advanced_portfolio_construction/handoff/phase_154_handoff.csv')
    save_phase_154_handoff = save_phase_154_portfolio_construction_position_sizing_risk_budgeting_handoff_report
    load_phase_154_handoff = load_phase_154_portfolio_construction_position_sizing_risk_budgeting_handoff_report

    def save_portfolio_construction_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_portfolio_construction' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_portfolio_construction_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_portfolio_construction' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_portfolio_construction_reports(self):
        return pd.DataFrame()

    # =========================================================================
    # Phase 154: Advanced Portfolio Optimization & Allocation Constraints
    # =========================================================================

    def save_portfolio_optimization_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/profiles/profile_registry', df, summary)
    def load_portfolio_optimization_profile_registry(self):
        return self._load_csv('advanced_portfolio_optimization/profiles/profile_registry.csv')

    def save_portfolio_optimization_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/domains/domain_registry', df, summary)
    def load_portfolio_optimization_domain_registry(self):
        return self._load_csv('advanced_portfolio_optimization/domains/domain_registry.csv')

    def save_portfolio_optimization_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/scopes/scope_registry', df, summary)
    def load_portfolio_optimization_scope_registry(self):
        return self._load_csv('advanced_portfolio_optimization/scopes/scope_registry.csv')

    def save_portfolio_optimization_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/optimization_contracts/optimization_contracts', df, summary)
    def load_portfolio_optimization_contracts(self):
        return self._load_csv('advanced_portfolio_optimization/optimization_contracts/optimization_contracts.csv')
    save_portfolio_optimization_contract_registry = save_portfolio_optimization_contracts
    load_portfolio_optimization_contract_registry = load_portfolio_optimization_contracts

    def save_optimization_objective_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/objective_contracts/objective_contracts', df, summary)
    def load_optimization_objective_contracts(self):
        return self._load_csv('advanced_portfolio_optimization/objective_contracts/objective_contracts.csv')
    save_optimization_objective_contract_registry = save_optimization_objective_contracts
    load_optimization_objective_contract_registry = load_optimization_objective_contracts

    def save_mean_variance_objective_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/objectives/mean_variance', df, summary)
    def load_mean_variance_objective_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/objectives/mean_variance.csv')

    def save_minimum_variance_objective_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/objectives/minimum_variance', df, summary)
    def load_minimum_variance_objective_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/objectives/minimum_variance.csv')

    def save_maximum_sharpe_objective_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/objectives/maximum_sharpe', df, summary)
    def load_maximum_sharpe_objective_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/objectives/maximum_sharpe.csv')

    def save_risk_parity_objective_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/objectives/risk_parity', df, summary)
    def load_risk_parity_objective_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/objectives/risk_parity.csv')

    def save_cvar_objective_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/objectives/cvar', df, summary)
    def load_cvar_objective_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/objectives/cvar.csv')

    def save_drawdown_minimization_objective_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/objectives/drawdown_minimization', df, summary)
    def load_drawdown_minimization_objective_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/objectives/drawdown_minimization.csv')

    def save_turnover_minimization_objective_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/objectives/turnover_minimization', df, summary)
    def load_turnover_minimization_objective_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/objectives/turnover_minimization.csv')

    def save_cost_aware_objective_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/objectives/cost_aware', df, summary)
    def load_cost_aware_objective_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/objectives/cost_aware.csv')

    def save_slippage_aware_objective_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/objectives/slippage_aware', df, summary)
    def load_slippage_aware_objective_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/objectives/slippage_aware.csv')

    def save_regime_aware_objective_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/objectives/regime_aware', df, summary)
    def load_regime_aware_objective_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/objectives/regime_aware.csv')

    def save_robust_optimization_objective_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/objectives/robust_optimization', df, summary)
    def load_robust_optimization_objective_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/objectives/robust_optimization.csv')

    def save_allocation_constraint_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraint_contracts/constraint_contracts', df, summary)
    def load_allocation_constraint_contracts(self):
        return self._load_csv('advanced_portfolio_optimization/constraint_contracts/constraint_contracts.csv')
    save_allocation_constraint_contract_registry = save_allocation_constraint_contracts
    load_allocation_constraint_contract_registry = load_allocation_constraint_contracts

    def save_long_only_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/long_only', df, summary)
    def load_long_only_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/long_only.csv')

    def save_max_weight_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/max_weight', df, summary)
    def load_max_weight_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/max_weight.csv')

    def save_min_weight_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/min_weight', df, summary)
    def load_min_weight_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/min_weight.csv')

    def save_group_weight_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/group_weight', df, summary)
    def load_group_weight_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/group_weight.csv')

    def save_asset_count_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/asset_count', df, summary)
    def load_asset_count_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/asset_count.csv')

    def save_concentration_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/concentration', df, summary)
    def load_concentration_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/concentration.csv')

    def save_exposure_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/exposure', df, summary)
    def load_exposure_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/exposure.csv')

    def save_gross_exposure_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/gross_exposure', df, summary)
    def load_gross_exposure_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/gross_exposure.csv')

    def save_net_exposure_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/net_exposure', df, summary)
    def load_net_exposure_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/net_exposure.csv')

    def save_currency_exposure_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/currency_exposure', df, summary)
    def load_currency_exposure_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/currency_exposure.csv')

    def save_cross_asset_exposure_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/cross_asset_exposure', df, summary)
    def load_cross_asset_exposure_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/cross_asset_exposure.csv')

    def save_correlation_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/correlation', df, summary)
    def load_correlation_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/correlation.csv')

    def save_liquidity_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/liquidity', df, summary)
    def load_liquidity_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/liquidity.csv')

    def save_turnover_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/turnover', df, summary)
    def load_turnover_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/turnover.csv')

    def save_transaction_cost_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/transaction_cost', df, summary)
    def load_transaction_cost_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/transaction_cost.csv')

    def save_slippage_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/slippage', df, summary)
    def load_slippage_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/slippage.csv')

    def save_risk_budget_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/risk_budget', df, summary)
    def load_risk_budget_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/risk_budget.csv')

    def save_volatility_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/volatility', df, summary)
    def load_volatility_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/volatility.csv')

    def save_drawdown_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/drawdown', df, summary)
    def load_drawdown_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/drawdown.csv')

    def save_leverage_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/leverage', df, summary)
    def load_leverage_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/leverage.csv')

    def save_margin_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/margin', df, summary)
    def load_margin_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/margin.csv')

    def save_rebalance_constraint_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/constraints/rebalance', df, summary)
    def load_rebalance_constraint_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/constraints/rebalance.csv')

    def save_optimization_solver_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/solvers/solver_contracts', df, summary)
    def load_optimization_solver_contracts(self):
        return self._load_csv('advanced_portfolio_optimization/solvers/solver_contracts.csv')
    save_optimization_solver_contract_registry = save_optimization_solver_contracts
    load_optimization_solver_contract_registry = load_optimization_solver_contracts

    def save_convex_solver_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/solvers/convex_solver', df, summary)
    def load_convex_solver_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/solvers/convex_solver.csv')

    def save_heuristic_solver_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/solvers/heuristic_solver', df, summary)
    def load_heuristic_solver_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/solvers/heuristic_solver.csv')

    def save_grid_search_solver_disabled_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/solvers/grid_search_disabled', df, summary)
    def load_grid_search_solver_disabled_registry(self):
        return self._load_csv('advanced_portfolio_optimization/solvers/grid_search_disabled.csv')

    def save_optimizer_execution_disabled_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/solvers/optimizer_execution_disabled', df, summary)
    def load_optimizer_execution_disabled_registry(self):
        return self._load_csv('advanced_portfolio_optimization/solvers/optimizer_execution_disabled.csv')

    def save_efficient_frontier_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/frontiers/efficient_frontier', df, summary)
    def load_efficient_frontier_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/frontiers/efficient_frontier.csv')

    def save_optimization_result_output_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/outputs/result_output_contracts', df, summary)
    def load_optimization_result_output_contracts(self):
        return self._load_csv('advanced_portfolio_optimization/outputs/result_output_contracts.csv')
    save_optimization_result_output_contract_registry = save_optimization_result_output_contracts
    load_optimization_result_output_contract_registry = load_optimization_result_output_contracts

    def save_allocation_output_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/outputs/allocation_output_contracts', df, summary)
    def load_allocation_output_contracts(self):
        return self._load_csv('advanced_portfolio_optimization/outputs/allocation_output_contracts.csv')
    save_allocation_output_contract_registry = save_allocation_output_contracts
    load_allocation_output_contract_registry = load_allocation_output_contracts

    def save_rebalance_output_contracts(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/outputs/rebalance_output_contracts', df, summary)
    def load_rebalance_output_contracts(self):
        return self._load_csv('advanced_portfolio_optimization/outputs/rebalance_output_contracts.csv')
    save_rebalance_output_contract_registry = save_rebalance_output_contracts
    load_rebalance_output_contract_registry = load_rebalance_output_contracts

    def save_optimization_metric_placeholders(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/metrics/metric_placeholders', df, summary)
    def load_optimization_metric_placeholders(self):
        return self._load_csv('advanced_portfolio_optimization/metrics/metric_placeholders.csv')
    save_optimization_metric_placeholder_registry = save_optimization_metric_placeholders
    load_optimization_metric_placeholder_registry = load_optimization_metric_placeholders

    def save_objective_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/metrics/objective_metrics', df, summary)
    def load_objective_metric_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/metrics/objective_metrics.csv')

    def save_constraint_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/metrics/constraint_metrics', df, summary)
    def load_constraint_metric_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/metrics/constraint_metrics.csv')

    def save_allocation_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/metrics/allocation_metrics', df, summary)
    def load_allocation_metric_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_optimization/metrics/allocation_metrics.csv')

    def save_portfolio_optimization_validation_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/validation/validation_evidence', df, summary)
    def load_portfolio_optimization_validation_evidence_registry(self):
        return self._load_csv('advanced_portfolio_optimization/validation/validation_evidence.csv')

    def save_portfolio_optimization_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/findings/findings_registry', df, summary)
    def load_portfolio_optimization_findings_registry(self):
        return self._load_csv('advanced_portfolio_optimization/findings/findings_registry.csv')

    def save_portfolio_optimization_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/scoring/readiness_score_report', df, summary)
    def load_portfolio_optimization_readiness_score_report(self):
        return self._load_csv('advanced_portfolio_optimization/scoring/readiness_score_report.csv')

    def save_portfolio_optimization_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/manifest/manifest', df, summary)
    def load_portfolio_optimization_manifest(self):
        return self._load_csv('advanced_portfolio_optimization/manifest/manifest.csv')

    def save_portfolio_optimization_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/health/health_check', df, summary)
    def load_portfolio_optimization_health_check(self):
        return self._load_csv('advanced_portfolio_optimization/health/health_check.csv')

    def save_portfolio_optimization_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/validation/validation_report', df, summary)
    def load_portfolio_optimization_validation_report(self):
        return self._load_csv('advanced_portfolio_optimization/validation/validation_report.csv')

    def save_portfolio_optimization_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/safety/safety_boundary', df, summary)
    def load_portfolio_optimization_safety_boundary(self):
        return self._load_csv('advanced_portfolio_optimization/safety/safety_boundary.csv')

    def save_phase_155_portfolio_optimization_allocation_constraints_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_optimization/handoff/phase_155_handoff', df, summary)
    def load_phase_155_portfolio_optimization_allocation_constraints_handoff_report(self):
        return self._load_csv('advanced_portfolio_optimization/handoff/phase_155_handoff.csv')
    save_phase_155_handoff = save_phase_155_portfolio_optimization_allocation_constraints_handoff_report
    load_phase_155_handoff = load_phase_155_portfolio_optimization_allocation_constraints_handoff_report
    save_phase_155_risk_reporting_exposure_attribution_limit_monitoring_handoff_report = save_phase_155_portfolio_optimization_allocation_constraints_handoff_report
    load_phase_155_risk_reporting_exposure_attribution_limit_monitoring_handoff_report = load_phase_155_portfolio_optimization_allocation_constraints_handoff_report

    def save_portfolio_optimization_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_portfolio_optimization' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_portfolio_optimization_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_portfolio_optimization' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_portfolio_optimization_reports(self):
        return pd.DataFrame()

    # =========================================================================
    # Phase 155: Risk Reporting, Exposure Attribution and Limit Monitoring
    # =========================================================================
    def save_risk_reporting_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/profiles/risk_reporting_profile_registry', df, summary)
    def load_risk_reporting_profile_registry(self):
        return self._load_csv('advanced_risk_reporting/profiles/risk_reporting_profile_registry.csv')

    def save_risk_reporting_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/domains/risk_reporting_domain_registry', df, summary)
    def load_risk_reporting_domain_registry(self):
        return self._load_csv('advanced_risk_reporting/domains/risk_reporting_domain_registry.csv')

    def save_risk_reporting_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/scope/risk_reporting_scope_registry', df, summary)
    def load_risk_reporting_scope_registry(self):
        return self._load_csv('advanced_risk_reporting/scope/risk_reporting_scope_registry.csv')

    def save_risk_report_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/contracts/risk_report_contract_registry', df, summary)
    def load_risk_report_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/contracts/risk_report_contract_registry.csv')

    def save_exposure_attribution_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/contracts/exposure_attribution_contract_registry', df, summary)
    def load_exposure_attribution_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/contracts/exposure_attribution_contract_registry.csv')

    def save_limit_monitoring_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/contracts/limit_monitoring_contract_registry', df, summary)
    def load_limit_monitoring_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/contracts/limit_monitoring_contract_registry.csv')

    def save_portfolio_risk_summary_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/contracts/portfolio_risk_summary_contract_registry', df, summary)
    def load_portfolio_risk_summary_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/contracts/portfolio_risk_summary_contract_registry.csv')

    def save_portfolio_exposure_summary_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/contracts/portfolio_exposure_summary_contract_registry', df, summary)
    def load_portfolio_exposure_summary_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/contracts/portfolio_exposure_summary_contract_registry.csv')

    def save_gross_exposure_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/exposure/gross_exposure_placeholder_registry', df, summary)
    def load_gross_exposure_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/exposure/gross_exposure_placeholder_registry.csv')

    def save_net_exposure_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/exposure/net_exposure_placeholder_registry', df, summary)
    def load_net_exposure_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/exposure/net_exposure_placeholder_registry.csv')

    def save_currency_exposure_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/exposure/currency_exposure_placeholder_registry', df, summary)
    def load_currency_exposure_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/exposure/currency_exposure_placeholder_registry.csv')

    def save_cross_asset_exposure_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/exposure/cross_asset_exposure_placeholder_registry', df, summary)
    def load_cross_asset_exposure_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/exposure/cross_asset_exposure_placeholder_registry.csv')

    def save_concentration_exposure_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/exposure/concentration_exposure_placeholder_registry', df, summary)
    def load_concentration_exposure_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/exposure/concentration_exposure_placeholder_registry.csv')

    def save_liquidity_exposure_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/exposure/liquidity_exposure_placeholder_registry', df, summary)
    def load_liquidity_exposure_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/exposure/liquidity_exposure_placeholder_registry.csv')

    def save_leverage_exposure_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/exposure/leverage_exposure_placeholder_registry', df, summary)
    def load_leverage_exposure_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/exposure/leverage_exposure_placeholder_registry.csv')

    def save_margin_exposure_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/exposure/margin_exposure_placeholder_registry', df, summary)
    def load_margin_exposure_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/exposure/margin_exposure_placeholder_registry.csv')

    def save_risk_contribution_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/monitors/risk_contribution_placeholder_registry', df, summary)
    def load_risk_contribution_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/monitors/risk_contribution_placeholder_registry.csv')

    def save_drawdown_monitor_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/monitors/drawdown_monitor_placeholder_registry', df, summary)
    def load_drawdown_monitor_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/monitors/drawdown_monitor_placeholder_registry.csv')

    def save_var_monitor_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/monitors/var_monitor_placeholder_registry', df, summary)
    def load_var_monitor_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/monitors/var_monitor_placeholder_registry.csv')

    def save_expected_shortfall_monitor_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/monitors/expected_shortfall_monitor_placeholder_registry', df, summary)
    def load_expected_shortfall_monitor_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/monitors/expected_shortfall_monitor_placeholder_registry.csv')

    def save_limit_definition_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/limits/limit_definition_contract_registry', df, summary)
    def load_limit_definition_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/limits/limit_definition_contract_registry.csv')

    def save_exposure_limit_monitoring_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/limits/exposure_limit_monitoring_contract_registry', df, summary)
    def load_exposure_limit_monitoring_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/limits/exposure_limit_monitoring_contract_registry.csv')

    def save_concentration_limit_monitoring_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/limits/concentration_limit_monitoring_contract_registry', df, summary)
    def load_concentration_limit_monitoring_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/limits/concentration_limit_monitoring_contract_registry.csv')

    def save_leverage_limit_monitoring_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/limits/leverage_limit_monitoring_contract_registry', df, summary)
    def load_leverage_limit_monitoring_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/limits/leverage_limit_monitoring_contract_registry.csv')

    def save_margin_limit_monitoring_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/limits/margin_limit_monitoring_contract_registry', df, summary)
    def load_margin_limit_monitoring_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/limits/margin_limit_monitoring_contract_registry.csv')

    def save_drawdown_limit_monitoring_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/limits/drawdown_limit_monitoring_contract_registry', df, summary)
    def load_drawdown_limit_monitoring_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/limits/drawdown_limit_monitoring_contract_registry.csv')

    def save_limit_breach_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/placeholders/limit_breach_placeholder_registry', df, summary)
    def load_limit_breach_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/placeholders/limit_breach_placeholder_registry.csv')

    def save_risk_alert_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/placeholders/risk_alert_placeholder_registry', df, summary)
    def load_risk_alert_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/placeholders/risk_alert_placeholder_registry.csv')

    def save_alert_routing_disabled_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/disabled_execution/alert_routing_disabled_registry', df, summary)
    def load_alert_routing_disabled_registry(self):
        return self._load_csv('advanced_risk_reporting/disabled_execution/alert_routing_disabled_registry.csv')

    def save_dashboard_contract_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/placeholders/dashboard_contract_placeholder_registry', df, summary)
    def load_dashboard_contract_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/placeholders/dashboard_contract_placeholder_registry.csv')

    def save_risk_report_output_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/outputs/risk_report_output_contract_registry', df, summary)
    def load_risk_report_output_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/outputs/risk_report_output_contract_registry.csv')

    def save_exposure_attribution_output_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/outputs/exposure_attribution_output_contract_registry', df, summary)
    def load_exposure_attribution_output_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/outputs/exposure_attribution_output_contract_registry.csv')

    def save_limit_monitoring_output_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/outputs/limit_monitoring_output_contract_registry', df, summary)
    def load_limit_monitoring_output_contract_registry(self):
        return self._load_csv('advanced_risk_reporting/outputs/limit_monitoring_output_contract_registry.csv')

    def save_risk_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/metrics/risk_metric_placeholder_registry', df, summary)
    def load_risk_metric_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/metrics/risk_metric_placeholder_registry.csv')

    def save_exposure_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/metrics/exposure_metric_placeholder_registry', df, summary)
    def load_exposure_metric_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/metrics/exposure_metric_placeholder_registry.csv')

    def save_attribution_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/metrics/attribution_metric_placeholder_registry', df, summary)
    def load_attribution_metric_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/metrics/attribution_metric_placeholder_registry.csv')

    def save_limit_monitoring_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/metrics/limit_monitoring_metric_placeholder_registry', df, summary)
    def load_limit_monitoring_metric_placeholder_registry(self):
        return self._load_csv('advanced_risk_reporting/metrics/limit_monitoring_metric_placeholder_registry.csv')

    def save_risk_reporting_exposure_claim_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/guards/exposure_claim_guard_registry', df, summary)
    def load_risk_reporting_exposure_claim_guard_registry(self):
        return self._load_csv('advanced_risk_reporting/guards/exposure_claim_guard_registry.csv')

    def save_risk_reporting_limit_breach_claim_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/guards/limit_breach_claim_guard_registry', df, summary)
    def load_risk_reporting_limit_breach_claim_guard_registry(self):
        return self._load_csv('advanced_risk_reporting/guards/limit_breach_claim_guard_registry.csv')

    def save_risk_reporting_investment_advice_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/guards/investment_advice_guard_registry', df, summary)
    def load_risk_reporting_investment_advice_guard_registry(self):
        return self._load_csv('advanced_risk_reporting/guards/investment_advice_guard_registry.csv')

    def save_risk_reporting_portfolio_adjustment_guard_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/guards/portfolio_adjustment_guard_registry', df, summary)
    def load_risk_reporting_portfolio_adjustment_guard_registry(self):
        return self._load_csv('advanced_risk_reporting/guards/portfolio_adjustment_guard_registry.csv')

    def save_risk_reporting_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/guards/forbidden_column_policy_registry', df, summary)
    def load_risk_reporting_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_risk_reporting/guards/forbidden_column_policy_registry.csv')

    def save_risk_report_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/disabled_execution/risk_report_execution_disabled', df, summary)
    def load_risk_report_execution_disabled_report(self):
        return self._load_csv('advanced_risk_reporting/disabled_execution/risk_report_execution_disabled.csv')

    def save_exposure_attribution_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/disabled_execution/exposure_attribution_execution_disabled', df, summary)
    def load_exposure_attribution_execution_disabled_report(self):
        return self._load_csv('advanced_risk_reporting/disabled_execution/exposure_attribution_execution_disabled.csv')

    def save_limit_monitoring_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/disabled_execution/limit_monitoring_execution_disabled', df, summary)
    def load_limit_monitoring_execution_disabled_report(self):
        return self._load_csv('advanced_risk_reporting/disabled_execution/limit_monitoring_execution_disabled.csv')

    def save_risk_metric_calculation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/disabled_execution/risk_metric_calculation_disabled', df, summary)
    def load_risk_metric_calculation_disabled_report(self):
        return self._load_csv('advanced_risk_reporting/disabled_execution/risk_metric_calculation_disabled.csv')

    def save_limit_alerting_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/disabled_execution/limit_alerting_disabled', df, summary)
    def load_limit_alerting_disabled_report(self):
        return self._load_csv('advanced_risk_reporting/disabled_execution/limit_alerting_disabled.csv')

    def save_dashboard_generation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/disabled_execution/dashboard_generation_disabled', df, summary)
    def load_dashboard_generation_disabled_report(self):
        return self._load_csv('advanced_risk_reporting/disabled_execution/dashboard_generation_disabled.csv')

    def save_portfolio_adjustment_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/disabled_execution/portfolio_adjustment_disabled', df, summary)
    def load_portfolio_adjustment_disabled_report(self):
        return self._load_csv('advanced_risk_reporting/disabled_execution/portfolio_adjustment_disabled.csv')

    def save_risk_reporting_live_trading_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/disabled_execution/live_trading_disabled', df, summary)
    def load_risk_reporting_live_trading_disabled_report(self):
        return self._load_csv('advanced_risk_reporting/disabled_execution/live_trading_disabled.csv')

    def save_risk_reporting_broker_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/disabled_execution/broker_execution_disabled', df, summary)
    def load_risk_reporting_broker_execution_disabled_report(self):
        return self._load_csv('advanced_risk_reporting/disabled_execution/broker_execution_disabled.csv')

    def save_risk_reporting_validation_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/evidence/validation_evidence', df, summary)
    def load_risk_reporting_validation_evidence_registry(self):
        return self._load_csv('advanced_risk_reporting/evidence/validation_evidence.csv')

    def save_risk_reporting_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/findings/findings_registry', df, summary)
    def load_risk_reporting_findings_registry(self):
        return self._load_csv('advanced_risk_reporting/findings/findings_registry.csv')

    def save_risk_reporting_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/scoring/readiness_score_report', df, summary)
    def load_risk_reporting_readiness_score_report(self):
        return self._load_csv('advanced_risk_reporting/scoring/readiness_score_report.csv')

    def save_risk_reporting_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/manifest/manifest', df, summary)
    def load_risk_reporting_manifest(self):
        return self._load_csv('advanced_risk_reporting/manifest/manifest.csv')

    def save_risk_reporting_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/health/health_check', df, summary)
    def load_risk_reporting_health_check(self):
        return self._load_csv('advanced_risk_reporting/health/health_check.csv')

    def save_risk_reporting_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/validation/validation_report', df, summary)
    def load_risk_reporting_validation_report(self):
        return self._load_csv('advanced_risk_reporting/validation/validation_report.csv')

    def save_risk_reporting_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/safety/safety_boundary', df, summary)
    def load_risk_reporting_safety_boundary(self):
        return self._load_csv('advanced_risk_reporting/safety/safety_boundary.csv')

    def save_phase_156_portfolio_scenario_testing_drawdown_control_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_risk_reporting/handoff/phase_156_handoff', df, summary)
    def load_phase_156_portfolio_scenario_testing_drawdown_control_handoff_report(self):
        return self._load_csv('advanced_risk_reporting/handoff/phase_156_handoff.csv')
    save_phase_156_handoff = save_phase_156_portfolio_scenario_testing_drawdown_control_handoff_report
    load_phase_156_handoff = load_phase_156_portfolio_scenario_testing_drawdown_control_handoff_report

    def save_risk_reporting_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_risk_reporting' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_risk_reporting_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_risk_reporting' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_risk_reporting_reports(self):
        return pd.DataFrame()

    # =========================================================================
    # Phase 156: Portfolio Scenario Testing and Drawdown Control
    # =========================================================================
    def save_portfolio_scenario_control_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/profiles/profile_registry', df, summary)
    def load_portfolio_scenario_control_profile_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/profiles/profile_registry.csv')

    def save_portfolio_scenario_control_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/domains/domain_registry', df, summary)
    def load_portfolio_scenario_control_domain_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/domains/domain_registry.csv')

    def save_portfolio_scenario_control_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/scope/scope_registry', df, summary)
    def load_portfolio_scenario_control_scope_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/scope/scope_registry.csv')

    def save_portfolio_scenario_testing_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/contracts/scenario_testing_contract_registry', df, summary)
    def load_portfolio_scenario_testing_contract_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/contracts/scenario_testing_contract_registry.csv')

    def save_portfolio_resilience_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/contracts/resilience_contract_registry', df, summary)
    def load_portfolio_resilience_contract_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/contracts/resilience_contract_registry.csv')

    def save_portfolio_scenario_library_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/contracts/scenario_library_contract_registry', df, summary)
    def load_portfolio_scenario_library_contract_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/contracts/scenario_library_contract_registry.csv')

    def save_historical_portfolio_scenario_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/contracts/historical_scenario_contract_registry', df, summary)
    def load_historical_portfolio_scenario_contract_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/contracts/historical_scenario_contract_registry.csv')

    def save_hypothetical_portfolio_scenario_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/contracts/hypothetical_scenario_contract_registry', df, summary)
    def load_hypothetical_portfolio_scenario_contract_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/contracts/hypothetical_scenario_contract_registry.csv')

    def save_portfolio_drawdown_control_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/contracts/drawdown_control_contract_registry', df, summary)
    def load_portfolio_drawdown_control_contract_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/contracts/drawdown_control_contract_registry.csv')

    def save_drawdown_threshold_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/thresholds/drawdown_threshold_contract_registry', df, summary)
    def load_drawdown_threshold_contract_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/thresholds/drawdown_threshold_contract_registry.csv')

    def save_drawdown_warning_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/placeholders/warning_placeholder_registry', df, summary)
    def load_drawdown_warning_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/placeholders/warning_placeholder_registry.csv')

    def save_drawdown_breach_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/placeholders/breach_placeholder_registry', df, summary)
    def load_drawdown_breach_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/placeholders/breach_placeholder_registry.csv')

    def save_drawdown_recovery_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/placeholders/recovery_placeholder_registry', df, summary)
    def load_drawdown_recovery_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/placeholders/recovery_placeholder_registry.csv')

    def save_exposure_reduction_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/actions/exposure_reduction_placeholder_registry', df, summary)
    def load_exposure_reduction_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/actions/exposure_reduction_placeholder_registry.csv')

    def save_de_risking_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/actions/de_risking_placeholder_registry', df, summary)
    def load_de_risking_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/actions/de_risking_placeholder_registry.csv')

    def save_hedge_control_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/actions/hedge_control_placeholder_registry', df, summary)
    def load_hedge_control_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/actions/hedge_control_placeholder_registry.csv')

    def save_rebalance_control_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/actions/rebalance_control_placeholder_registry', df, summary)
    def load_rebalance_control_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/actions/rebalance_control_placeholder_registry.csv')

    def save_stop_control_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/actions/stop_control_placeholder_registry', df, summary)
    def load_stop_control_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/actions/stop_control_placeholder_registry.csv')

    def save_portfolio_freeze_control_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/actions/portfolio_freeze_control_placeholder_registry', df, summary)
    def load_portfolio_freeze_control_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/actions/portfolio_freeze_control_placeholder_registry.csv')

    def save_portfolio_resume_control_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/actions/portfolio_resume_control_placeholder_registry', df, summary)
    def load_portfolio_resume_control_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/actions/portfolio_resume_control_placeholder_registry.csv')

    def save_scenario_output_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/outputs/scenario_output_contract_registry', df, summary)
    def load_scenario_output_contract_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/outputs/scenario_output_contract_registry.csv')

    def save_drawdown_control_output_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/outputs/drawdown_control_output_contract_registry', df, summary)
    def load_drawdown_control_output_contract_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/outputs/drawdown_control_output_contract_registry.csv')

    def save_resilience_output_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/outputs/resilience_output_contract_registry', df, summary)
    def load_resilience_output_contract_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/outputs/resilience_output_contract_registry.csv')

    def save_scenario_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/metrics/scenario_metric_placeholder_registry', df, summary)
    def load_scenario_metric_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/metrics/scenario_metric_placeholder_registry.csv')

    def save_drawdown_metric_placeholder_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/metrics/drawdown_metric_placeholder_registry', df, summary)
    def load_drawdown_metric_placeholder_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/metrics/drawdown_metric_placeholder_registry.csv')

    def save_portfolio_scenario_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/dependencies/dependency_registry', df, summary)
    def load_portfolio_scenario_dependency_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/dependencies/dependency_registry.csv')

    def save_portfolio_scenario_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/guards/forbidden_column_policy_registry', df, summary)
    def load_portfolio_scenario_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/guards/forbidden_column_policy_registry.csv')

    def save_portfolio_scenario_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/disabled_execution/scenario_execution_disabled', df, summary)
    def load_portfolio_scenario_execution_disabled_report(self):
        return self._load_csv('advanced_portfolio_scenario_control/disabled_execution/scenario_execution_disabled.csv')

    def save_drawdown_control_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/disabled_execution/drawdown_control_execution_disabled', df, summary)
    def load_drawdown_control_execution_disabled_report(self):
        return self._load_csv('advanced_portfolio_scenario_control/disabled_execution/drawdown_control_execution_disabled.csv')

    def save_portfolio_control_action_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/disabled_execution/portfolio_control_action_disabled', df, summary)
    def load_portfolio_control_action_disabled_report(self):
        return self._load_csv('advanced_portfolio_scenario_control/disabled_execution/portfolio_control_action_disabled.csv')

    def save_portfolio_scenario_live_trading_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/disabled_execution/live_trading_disabled', df, summary)
    def load_portfolio_scenario_live_trading_disabled_report(self):
        return self._load_csv('advanced_portfolio_scenario_control/disabled_execution/live_trading_disabled.csv')

    def save_portfolio_scenario_broker_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/disabled_execution/broker_execution_disabled', df, summary)
    def load_portfolio_scenario_broker_execution_disabled_report(self):
        return self._load_csv('advanced_portfolio_scenario_control/disabled_execution/broker_execution_disabled.csv')

    def save_portfolio_scenario_validation_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/evidence/validation_evidence', df, summary)
    def load_portfolio_scenario_validation_evidence_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/evidence/validation_evidence.csv')

    def save_portfolio_scenario_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/findings/findings_registry', df, summary)
    def load_portfolio_scenario_findings_registry(self):
        return self._load_csv('advanced_portfolio_scenario_control/findings/findings_registry.csv')

    def save_portfolio_scenario_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/scoring/readiness_score_report', df, summary)
    def load_portfolio_scenario_readiness_score_report(self):
        return self._load_csv('advanced_portfolio_scenario_control/scoring/readiness_score_report.csv')

    def save_portfolio_scenario_control_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/manifest/manifest', df, summary)
    def load_portfolio_scenario_control_manifest(self):
        return self._load_csv('advanced_portfolio_scenario_control/manifest/manifest.csv')

    def save_portfolio_scenario_control_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/health/health_check', df, summary)
    def load_portfolio_scenario_control_health_check(self):
        return self._load_csv('advanced_portfolio_scenario_control/health/health_check.csv')

    def save_portfolio_scenario_control_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/validation/validation_report', df, summary)
    def load_portfolio_scenario_control_validation_report(self):
        return self._load_csv('advanced_portfolio_scenario_control/validation/validation_report.csv')

    def save_portfolio_scenario_control_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/safety/safety_boundary', df, summary)
    def load_portfolio_scenario_control_safety_boundary(self):
        return self._load_csv('advanced_portfolio_scenario_control/safety/safety_boundary.csv')

    def save_phase_157_portfolio_acceptance_report_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_scenario_control/handoff/phase_157_handoff', df, summary)
    def load_phase_157_portfolio_acceptance_report_handoff_report(self):
        return self._load_csv('advanced_portfolio_scenario_control/handoff/phase_157_handoff.csv')
    save_phase_157_handoff = save_phase_157_portfolio_acceptance_report_handoff_report
    load_phase_157_handoff = load_phase_157_portfolio_acceptance_report_handoff_report

    def save_portfolio_scenario_control_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_portfolio_scenario_control' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_portfolio_scenario_control_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_portfolio_scenario_control' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_portfolio_scenario_control_reports(self):
        return pd.DataFrame()

    # Phase 157 Portfolio Acceptance Report Methods
    def save_portfolio_acceptance_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/profiles/profile_registry', df, summary)
    def load_portfolio_acceptance_profile_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/profiles/profile_registry.csv')

    def save_portfolio_acceptance_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/domains/domain_registry', df, summary)
    def load_portfolio_acceptance_domain_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/domains/domain_registry.csv')

    def save_portfolio_acceptance_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/scope/scope_registry', df, summary)
    def load_portfolio_acceptance_scope_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/scope/scope_registry.csv')

    def save_portfolio_acceptance_component_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/components/component_registry', df, summary)
    def load_portfolio_acceptance_component_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/components/component_registry.csv')

    def save_portfolio_acceptance_component_checkpoint_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/checkpoints/checkpoint_registry', df, summary)
    def load_portfolio_acceptance_component_checkpoint_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/checkpoints/checkpoint_registry.csv')

    def save_phase_153_portfolio_construction_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/phase_153/phase_153_acceptance', df, summary)
    def load_phase_153_portfolio_construction_acceptance_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/phase_153/phase_153_acceptance.csv')

    def save_phase_154_portfolio_optimization_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/phase_154/phase_154_acceptance', df, summary)
    def load_phase_154_portfolio_optimization_acceptance_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/phase_154/phase_154_acceptance.csv')

    def save_phase_155_risk_reporting_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/phase_155/phase_155_acceptance', df, summary)
    def load_phase_155_risk_reporting_acceptance_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/phase_155/phase_155_acceptance.csv')

    def save_phase_156_portfolio_scenario_control_acceptance_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/phase_156/phase_156_acceptance', df, summary)
    def load_phase_156_portfolio_scenario_control_acceptance_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/phase_156/phase_156_acceptance.csv')

    def save_portfolio_acceptance_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/dependencies/dependency_registry', df, summary)
    def load_portfolio_acceptance_dependency_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/dependencies/dependency_registry.csv')

    def save_portfolio_acceptance_validation_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/evidence/validation_evidence', df, summary)
    def load_portfolio_acceptance_validation_evidence_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/evidence/validation_evidence.csv')

    def save_portfolio_acceptance_safety_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/safety/safety_boundary_registry', df, summary)
    def load_portfolio_acceptance_safety_boundary_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/safety/safety_boundary_registry.csv')

    def save_portfolio_acceptance_non_production_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/non_production/non_production_boundary_registry', df, summary)
    def load_portfolio_acceptance_non_production_boundary_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/non_production/non_production_boundary_registry.csv')

    def save_portfolio_acceptance_manual_review_gate_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/review_gates/manual_review_gate_registry', df, summary)
    def load_portfolio_acceptance_manual_review_gate_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/review_gates/manual_review_gate_registry.csv')

    def save_portfolio_acceptance_go_no_go_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/go_no_go/go_no_go_boundary_registry', df, summary)
    def load_portfolio_acceptance_go_no_go_boundary_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/go_no_go/go_no_go_boundary_registry.csv')

    def save_portfolio_acceptance_blocker_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/blockers/blocker_registry', df, summary)
    def load_portfolio_acceptance_blocker_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/blockers/blocker_registry.csv')

    def save_portfolio_acceptance_gap_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/gaps/gap_registry', df, summary)
    def load_portfolio_acceptance_gap_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/gaps/gap_registry.csv')

    def save_portfolio_acceptance_warning_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/warnings/warning_registry', df, summary)
    def load_portfolio_acceptance_warning_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/warnings/warning_registry.csv')

    def save_portfolio_acceptance_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/findings/findings_registry', df, summary)
    def load_portfolio_acceptance_findings_registry(self):
        return self._load_csv('advanced_portfolio_acceptance/findings/findings_registry.csv')

    def save_portfolio_acceptance_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/scoring/readiness_score_report', df, summary)
    def load_portfolio_acceptance_readiness_score_report(self):
        return self._load_csv('advanced_portfolio_acceptance/scoring/readiness_score_report.csv')

    def save_portfolio_acceptance_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/manifest/manifest', df, summary)
    def load_portfolio_acceptance_manifest(self):
        return self._load_csv('advanced_portfolio_acceptance/manifest/manifest.csv')

    def save_portfolio_acceptance_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/health/health_check', df, summary)
    def load_portfolio_acceptance_health_check(self):
        return self._load_csv('advanced_portfolio_acceptance/health/health_check.csv')

    def save_portfolio_acceptance_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/validation/validation_report', df, summary)
    def load_portfolio_acceptance_validation_report(self):
        return self._load_csv('advanced_portfolio_acceptance/validation/validation_report.csv')

    def save_portfolio_acceptance_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/safety/safety_boundary', df, summary)
    def load_portfolio_acceptance_safety_boundary(self):
        return self._load_csv('advanced_portfolio_acceptance/safety/safety_boundary.csv')

    def save_phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_portfolio_acceptance/handoff/phase_158_handoff', df, summary)
    def load_phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report(self):
        return self._load_csv('advanced_portfolio_acceptance/handoff/phase_158_handoff.csv')
    save_phase_158_handoff = save_phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report
    load_phase_158_handoff = load_phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report

    def save_portfolio_acceptance_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_portfolio_acceptance' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_portfolio_acceptance_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_portfolio_acceptance' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_portfolio_acceptance_reports(self):
        return pd.DataFrame()

    # =========================================================================
    # Phase 158: Full-System Integration and Advanced Acceptance Rehearsal
    # =========================================================================
    def save_full_system_integration_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/profiles/profile_registry', df, summary)
    def load_full_system_integration_profile_registry(self):
        return self._load_csv('advanced_full_system_integration/profiles/profile_registry.csv')

    def save_full_system_integration_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/domains/domain_registry', df, summary)
    def load_full_system_integration_domain_registry(self):
        return self._load_csv('advanced_full_system_integration/domains/domain_registry.csv')

    def save_full_system_integration_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/scope/scope_registry', df, summary)
    def load_full_system_integration_scope_registry(self):
        return self._load_csv('advanced_full_system_integration/scope/scope_registry.csv')

    def save_system_component_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/components/component_registry', df, summary)
    def load_system_component_registry(self):
        return self._load_csv('advanced_full_system_integration/components/component_registry.csv')

    def save_system_component_dependency_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/dependencies/dependency_registry', df, summary)
    def load_system_component_dependency_registry(self):
        return self._load_csv('advanced_full_system_integration/dependencies/dependency_registry.csv')

    def save_system_component_checkpoint_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/checkpoints/checkpoint_registry', df, summary)
    def load_system_component_checkpoint_registry(self):
        return self._load_csv('advanced_full_system_integration/checkpoints/checkpoint_registry.csv')

    def save_system_contract_integration_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/contracts/contract_integration_registry', df, summary)
    def load_system_contract_integration_registry(self):
        return self._load_csv('advanced_full_system_integration/contracts/contract_integration_registry.csv')

    def save_system_manifest_integration_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/manifests/manifest_integration_registry', df, summary)
    def load_system_manifest_integration_registry(self):
        return self._load_csv('advanced_full_system_integration/manifests/manifest_integration_registry.csv')

    def save_system_validation_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/evidence/validation_evidence_registry', df, summary)
    def load_system_validation_evidence_registry(self):
        return self._load_csv('advanced_full_system_integration/evidence/validation_evidence_registry.csv')

    def save_system_safety_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/safety/safety_boundary_registry', df, summary)
    def load_system_safety_boundary_registry(self):
        return self._load_csv('advanced_full_system_integration/safety/safety_boundary_registry.csv')

    def save_system_non_production_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/non_production/non_production_boundary_registry', df, summary)
    def load_system_non_production_boundary_registry(self):
        return self._load_csv('advanced_full_system_integration/non_production/non_production_boundary_registry.csv')

    def save_system_dry_run_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/dry_run/dry_run_boundary_registry', df, summary)
    def load_system_dry_run_boundary_registry(self):
        return self._load_csv('advanced_full_system_integration/dry_run/dry_run_boundary_registry.csv')

    def save_system_manual_review_gate_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/review_gates/manual_review_gate_registry', df, summary)
    def load_system_manual_review_gate_registry(self):
        return self._load_csv('advanced_full_system_integration/review_gates/manual_review_gate_registry.csv')

    def save_advanced_acceptance_rehearsal_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/rehearsal/acceptance_rehearsal_registry', df, summary)
    def load_advanced_acceptance_rehearsal_registry(self):
        return self._load_csv('advanced_full_system_integration/rehearsal/acceptance_rehearsal_registry.csv')

    def save_advanced_acceptance_rehearsal_checkpoint_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/rehearsal/rehearsal_checkpoint_registry', df, summary)
    def load_advanced_acceptance_rehearsal_checkpoint_registry(self):
        return self._load_csv('advanced_full_system_integration/rehearsal/rehearsal_checkpoint_registry.csv')

    def save_data_pipeline_integration_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/subsystems/data_pipeline_integration_registry', df, summary)
    def load_data_pipeline_integration_registry(self):
        return self._load_csv('advanced_full_system_integration/subsystems/data_pipeline_integration_registry.csv')

    def save_feature_factor_integration_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/subsystems/feature_factor_integration_registry', df, summary)
    def load_feature_factor_integration_registry(self):
        return self._load_csv('advanced_full_system_integration/subsystems/feature_factor_integration_registry.csv')

    def save_regime_integration_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/subsystems/regime_integration_registry', df, summary)
    def load_regime_integration_registry(self):
        return self._load_csv('advanced_full_system_integration/subsystems/regime_integration_registry.csv')

    def save_ml_governance_integration_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/subsystems/ml_governance_integration_registry', df, summary)
    def load_ml_governance_integration_registry(self):
        return self._load_csv('advanced_full_system_integration/subsystems/ml_governance_integration_registry.csv')

    def save_backtest_acceptance_integration_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/subsystems/backtest_acceptance_integration_registry', df, summary)
    def load_backtest_acceptance_integration_registry(self):
        return self._load_csv('advanced_full_system_integration/subsystems/backtest_acceptance_integration_registry.csv')

    def save_portfolio_acceptance_integration_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/subsystems/portfolio_acceptance_integration_registry', df, summary)
    def load_portfolio_acceptance_integration_registry(self):
        return self._load_csv('advanced_full_system_integration/subsystems/portfolio_acceptance_integration_registry.csv')

    def save_risk_reporting_integration_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/subsystems/risk_reporting_integration_registry', df, summary)
    def load_risk_reporting_integration_registry(self):
        return self._load_csv('advanced_full_system_integration/subsystems/risk_reporting_integration_registry.csv')

    def save_scenario_control_integration_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/subsystems/scenario_control_integration_registry', df, summary)
    def load_scenario_control_integration_registry(self):
        return self._load_csv('advanced_full_system_integration/subsystems/scenario_control_integration_registry.csv')

    def save_reporting_integration_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/subsystems/reporting_integration_registry', df, summary)
    def load_reporting_integration_registry(self):
        return self._load_csv('advanced_full_system_integration/subsystems/reporting_integration_registry.csv')

    def save_forbidden_column_system_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/safety/forbidden_column_system_policy_registry', df, summary)
    def load_forbidden_column_system_policy_registry(self):
        return self._load_csv('advanced_full_system_integration/safety/forbidden_column_system_policy_registry.csv')

    def save_system_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/disabled_execution/system_execution_disabled_report', df, summary)
    def load_system_execution_disabled_report(self):
        return self._load_csv('advanced_full_system_integration/disabled_execution/system_execution_disabled_report.csv')

    def save_live_trading_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/disabled_execution/live_trading_disabled_report', df, summary)
    def load_live_trading_disabled_report(self):
        return self._load_csv('advanced_full_system_integration/disabled_execution/live_trading_disabled_report.csv')

    def save_broker_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/disabled_execution/broker_execution_disabled_report', df, summary)
    def load_broker_execution_disabled_report(self):
        return self._load_csv('advanced_full_system_integration/disabled_execution/broker_execution_disabled_report.csv')

    def save_production_deployment_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/disabled_execution/production_deployment_disabled_report', df, summary)
    def load_production_deployment_disabled_report(self):
        return self._load_csv('advanced_full_system_integration/disabled_execution/production_deployment_disabled_report.csv')

    def save_model_training_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/disabled_execution/model_training_disabled_report', df, summary)
    def load_model_training_disabled_report(self):
        return self._load_csv('advanced_full_system_integration/disabled_execution/model_training_disabled_report.csv')

    def save_model_prediction_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/disabled_execution/model_prediction_disabled_report', df, summary)
    def load_model_prediction_disabled_report(self):
        return self._load_csv('advanced_full_system_integration/disabled_execution/model_prediction_disabled_report.csv')

    def save_order_generation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/disabled_execution/order_generation_disabled_report', df, summary)
    def load_order_generation_disabled_report(self):
        return self._load_csv('advanced_full_system_integration/disabled_execution/order_generation_disabled_report.csv')

    def save_signal_generation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/disabled_execution/signal_generation_disabled_report', df, summary)
    def load_signal_generation_disabled_report(self):
        return self._load_csv('advanced_full_system_integration/disabled_execution/signal_generation_disabled_report.csv')

    def save_investment_advice_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/disabled_execution/investment_advice_disabled_report', df, summary)
    def load_investment_advice_disabled_report(self):
        return self._load_csv('advanced_full_system_integration/disabled_execution/investment_advice_disabled_report.csv')

    def save_system_integration_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/findings/findings_registry', df, summary)
    def load_system_integration_findings_registry(self):
        return self._load_csv('advanced_full_system_integration/findings/findings_registry.csv')

    def save_system_integration_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/scoring/readiness_score_report', df, summary)
    def load_system_integration_readiness_score_report(self):
        return self._load_csv('advanced_full_system_integration/scoring/readiness_score_report.csv')

    def save_full_system_integration_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/manifest/manifest', df, summary)
    def load_full_system_integration_manifest(self):
        return self._load_csv('advanced_full_system_integration/manifest/manifest.csv')

    def save_full_system_integration_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/health/health_check', df, summary)
    def load_full_system_integration_health_check(self):
        return self._load_csv('advanced_full_system_integration/health/health_check.csv')

    def save_full_system_integration_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/validation/validation_report', df, summary)
    def load_full_system_integration_validation_report(self):
        return self._load_csv('advanced_full_system_integration/validation/validation_report.csv')

    def save_full_system_integration_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/safety/safety_boundary', df, summary)
    def load_full_system_integration_safety_boundary(self):
        return self._load_csv('advanced_full_system_integration/safety/safety_boundary.csv')

    def save_phase_159_final_hardening_operator_runbook_release_candidate_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_full_system_integration/handoff/phase_159_handoff', df, summary)
    def load_phase_159_final_hardening_operator_runbook_release_candidate_handoff_report(self):
        return self._load_csv('advanced_full_system_integration/handoff/phase_159_handoff.csv')
    save_phase_159_handoff = save_phase_159_final_hardening_operator_runbook_release_candidate_handoff_report
    load_phase_159_handoff = load_phase_159_final_hardening_operator_runbook_release_candidate_handoff_report

    def save_full_system_integration_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_full_system_integration' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_full_system_integration_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_full_system_integration' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_full_system_integration_reports(self):
        return pd.DataFrame()

    # Phase 159 Final Hardening and Release Candidate Methods
    def save_final_hardening_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/profiles/profile_registry', df, summary)
    def load_final_hardening_profile_registry(self):
        return self._load_csv('advanced_final_hardening/profiles/profile_registry.csv')

    def save_final_hardening_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/domains/domain_registry', df, summary)
    def load_final_hardening_domain_registry(self):
        return self._load_csv('advanced_final_hardening/domains/domain_registry.csv')

    def save_final_hardening_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/scope/scope_registry', df, summary)
    def load_final_hardening_scope_registry(self):
        return self._load_csv('advanced_final_hardening/scope/scope_registry.csv')

    def save_final_hardening_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/contracts/contract_registry', df, summary)
    def load_final_hardening_contract_registry(self):
        return self._load_csv('advanced_final_hardening/contracts/contract_registry.csv')

    def save_operator_runbook_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/runbooks/runbook_contract_registry', df, summary)
    def load_operator_runbook_contract_registry(self):
        return self._load_csv('advanced_final_hardening/runbooks/runbook_contract_registry.csv')

    def save_release_candidate_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/contracts/release_candidate_contract_registry', df, summary)
    def load_release_candidate_contract_registry(self):
        return self._load_csv('advanced_final_hardening/contracts/release_candidate_contract_registry.csv')

    def save_final_configuration_freeze_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/freezes/configuration_freeze_registry', df, summary)
    def load_final_configuration_freeze_contract_registry(self):
        return self._load_csv('advanced_final_hardening/freezes/configuration_freeze_registry.csv')

    def save_final_documentation_freeze_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/freezes/documentation_freeze_registry', df, summary)
    def load_final_documentation_freeze_contract_registry(self):
        return self._load_csv('advanced_final_hardening/freezes/documentation_freeze_registry.csv')

    def save_final_safety_freeze_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/freezes/safety_freeze_registry', df, summary)
    def load_final_safety_freeze_contract_registry(self):
        return self._load_csv('advanced_final_hardening/freezes/safety_freeze_registry.csv')

    def save_final_validation_freeze_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/freezes/validation_freeze_registry', df, summary)
    def load_final_validation_freeze_contract_registry(self):
        return self._load_csv('advanced_final_hardening/freezes/validation_freeze_registry.csv')

    def save_final_dependency_freeze_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/freezes/dependency_freeze_registry', df, summary)
    def load_final_dependency_freeze_contract_registry(self):
        return self._load_csv('advanced_final_hardening/freezes/dependency_freeze_registry.csv')

    def save_final_manifest_freeze_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/freezes/manifest_freeze_registry', df, summary)
    def load_final_manifest_freeze_contract_registry(self):
        return self._load_csv('advanced_final_hardening/freezes/manifest_freeze_registry.csv')

    def save_final_report_freeze_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/freezes/report_freeze_registry', df, summary)
    def load_final_report_freeze_contract_registry(self):
        return self._load_csv('advanced_final_hardening/freezes/report_freeze_registry.csv')

    def save_final_settings_audit_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/audits/settings_audit_registry', df, summary)
    def load_final_settings_audit_contract_registry(self):
        return self._load_csv('advanced_final_hardening/audits/settings_audit_registry.csv')

    def save_final_env_template_audit_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/audits/env_template_audit_registry', df, summary)
    def load_final_env_template_audit_contract_registry(self):
        return self._load_csv('advanced_final_hardening/audits/env_template_audit_registry.csv')

    def save_final_paths_audit_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/audits/paths_audit_registry', df, summary)
    def load_final_paths_audit_contract_registry(self):
        return self._load_csv('advanced_final_hardening/audits/paths_audit_registry.csv')

    def save_final_script_inventory_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/inventories/script_inventory_registry', df, summary)
    def load_final_script_inventory_registry(self):
        return self._load_csv('advanced_final_hardening/inventories/script_inventory_registry.csv')

    def save_final_test_inventory_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/inventories/test_inventory_registry', df, summary)
    def load_final_test_inventory_registry(self):
        return self._load_csv('advanced_final_hardening/inventories/test_inventory_registry.csv')

    def save_final_docs_inventory_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/inventories/docs_inventory_registry', df, summary)
    def load_final_docs_inventory_registry(self):
        return self._load_csv('advanced_final_hardening/inventories/docs_inventory_registry.csv')

    def save_final_report_inventory_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/inventories/report_inventory_registry', df, summary)
    def load_final_report_inventory_registry(self):
        return self._load_csv('advanced_final_hardening/inventories/report_inventory_registry.csv')

    def save_final_system_component_inventory_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/inventories/system_component_inventory_registry', df, summary)
    def load_final_system_component_inventory_registry(self):
        return self._load_csv('advanced_final_hardening/inventories/system_component_inventory_registry.csv')

    def save_final_disabled_execution_inventory_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/inventories/disabled_execution_inventory_registry', df, summary)
    def load_final_disabled_execution_inventory_registry(self):
        return self._load_csv('advanced_final_hardening/inventories/disabled_execution_inventory_registry.csv')

    def save_final_safety_boundary_inventory_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/inventories/safety_boundary_inventory_registry', df, summary)
    def load_final_safety_boundary_inventory_registry(self):
        return self._load_csv('advanced_final_hardening/inventories/safety_boundary_inventory_registry.csv')

    def save_operator_startup_runbook_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/runbooks/startup_runbook_registry', df, summary)
    def load_operator_startup_runbook_contract_registry(self):
        return self._load_csv('advanced_final_hardening/runbooks/startup_runbook_registry.csv')

    def save_operator_shutdown_runbook_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/runbooks/shutdown_runbook_registry', df, summary)
    def load_operator_shutdown_runbook_contract_registry(self):
        return self._load_csv('advanced_final_hardening/runbooks/shutdown_runbook_registry.csv')

    def save_operator_config_check_runbook_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/runbooks/config_check_runbook_registry', df, summary)
    def load_operator_config_check_runbook_contract_registry(self):
        return self._load_csv('advanced_final_hardening/runbooks/config_check_runbook_registry.csv')

    def save_operator_troubleshooting_runbook_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/runbooks/troubleshooting_runbook_registry', df, summary)
    def load_operator_troubleshooting_runbook_contract_registry(self):
        return self._load_csv('advanced_final_hardening/runbooks/troubleshooting_runbook_registry.csv')

    def save_operator_recovery_runbook_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/runbooks/recovery_runbook_registry', df, summary)
    def load_operator_recovery_runbook_contract_registry(self):
        return self._load_csv('advanced_final_hardening/runbooks/recovery_runbook_registry.csv')

    def save_operator_no_go_protocol_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/protocols/no_go_protocol_registry', df, summary)
    def load_operator_no_go_protocol_registry(self):
        return self._load_csv('advanced_final_hardening/protocols/no_go_protocol_registry.csv')

    def save_operator_safe_usage_protocol_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/protocols/safe_usage_protocol_registry', df, summary)
    def load_operator_safe_usage_protocol_registry(self):
        return self._load_csv('advanced_final_hardening/protocols/safe_usage_protocol_registry.csv')

    def save_release_candidate_checklist_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/checklists/checklist_registry', df, summary)
    def load_release_candidate_checklist_registry(self):
        return self._load_csv('advanced_final_hardening/checklists/checklist_registry.csv')

    def save_release_candidate_component_checkpoint_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/checkpoints/component_checkpoint_registry', df, summary)
    def load_release_candidate_component_checkpoint_registry(self):
        return self._load_csv('advanced_final_hardening/checkpoints/component_checkpoint_registry.csv')

    def save_release_candidate_dependency_checkpoint_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/checkpoints/dependency_checkpoint_registry', df, summary)
    def load_release_candidate_dependency_checkpoint_registry(self):
        return self._load_csv('advanced_final_hardening/checkpoints/dependency_checkpoint_registry.csv')

    def save_release_candidate_validation_checkpoint_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/checkpoints/validation_checkpoint_registry', df, summary)
    def load_release_candidate_validation_checkpoint_registry(self):
        return self._load_csv('advanced_final_hardening/checkpoints/validation_checkpoint_registry.csv')

    def save_release_candidate_safety_checkpoint_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/checkpoints/safety_checkpoint_registry', df, summary)
    def load_release_candidate_safety_checkpoint_registry(self):
        return self._load_csv('advanced_final_hardening/checkpoints/safety_checkpoint_registry.csv')

    def save_release_candidate_no_go_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/boundaries/no_go_boundary_registry', df, summary)
    def load_release_candidate_no_go_boundary_registry(self):
        return self._load_csv('advanced_final_hardening/boundaries/no_go_boundary_registry.csv')

    def save_release_candidate_go_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/boundaries/go_boundary_registry', df, summary)
    def load_release_candidate_go_boundary_registry(self):
        return self._load_csv('advanced_final_hardening/boundaries/go_boundary_registry.csv')

    def save_release_candidate_blocker_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/blockers/blocker_registry', df, summary)
    def load_release_candidate_blocker_registry(self):
        return self._load_csv('advanced_final_hardening/blockers/blocker_registry.csv')

    def save_release_candidate_gap_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/gaps/gap_registry', df, summary)
    def load_release_candidate_gap_registry(self):
        return self._load_csv('advanced_final_hardening/gaps/gap_registry.csv')

    def save_release_candidate_warning_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/warnings/warning_registry', df, summary)
    def load_release_candidate_warning_registry(self):
        return self._load_csv('advanced_final_hardening/warnings/warning_registry.csv')

    def save_release_candidate_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/findings/findings_registry', df, summary)
    def load_release_candidate_findings_registry(self):
        return self._load_csv('advanced_final_hardening/findings/findings_registry.csv')

    def save_release_candidate_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/scoring/readiness_score_report', df, summary)
    def load_release_candidate_readiness_score_report(self):
        return self._load_csv('advanced_final_hardening/scoring/readiness_score_report.csv')

    def save_release_candidate_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/manifest/manifest', df, summary)
    def load_release_candidate_manifest(self):
        return self._load_csv('advanced_final_hardening/manifest/manifest.csv')

    def save_release_candidate_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/health/health_check', df, summary)
    def load_release_candidate_health_check(self):
        return self._load_csv('advanced_final_hardening/health/health_check.csv')

    def save_release_candidate_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/validation/validation_report', df, summary)
    def load_release_candidate_validation_report(self):
        return self._load_csv('advanced_final_hardening/validation/validation_report.csv')

    def save_release_candidate_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/safety/safety_boundary', df, summary)
    def load_release_candidate_safety_boundary(self):
        return self._load_csv('advanced_final_hardening/safety/safety_boundary.csv')

    def save_phase_160_full_advanced_bot_final_delivery_handoff_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_hardening/handoff/phase_160_handoff', df, summary)
    def load_phase_160_full_advanced_bot_final_delivery_handoff_report(self):
        return self._load_csv('advanced_final_hardening/handoff/phase_160_handoff.csv')
    save_phase_160_handoff = save_phase_160_full_advanced_bot_final_delivery_handoff_report
    load_phase_160_handoff = load_phase_160_full_advanced_bot_final_delivery_handoff_report

    def save_final_hardening_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_final_hardening' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_final_hardening_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_final_hardening' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_final_hardening_reports(self):
        return pd.DataFrame()

    # Phase 160: Full Advanced Bot Final Delivery methods
    def save_final_delivery_profile_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/profiles/profile_registry', df, summary)
    def load_final_delivery_profile_registry(self):
        return self._load_csv('advanced_final_delivery/profiles/profile_registry.csv')

    def save_final_delivery_domain_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/domains/domain_registry', df, summary)
    def load_final_delivery_domain_registry(self):
        return self._load_csv('advanced_final_delivery/domains/domain_registry.csv')

    def save_final_delivery_scope_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/scope/scope_registry', df, summary)
    def load_final_delivery_scope_registry(self):
        return self._load_csv('advanced_final_delivery/scope/scope_registry.csv')

    def save_final_delivery_package_contract_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/contracts/package_contract_registry', df, summary)
    def load_final_delivery_package_contract_registry(self):
        return self._load_csv('advanced_final_delivery/contracts/package_contract_registry.csv')

    def save_final_delivery_component_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/components/component_registry', df, summary)
    def load_final_delivery_component_registry(self):
        return self._load_csv('advanced_final_delivery/components/component_registry.csv')

    def save_final_delivery_module_inventory_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/inventory/module_inventory_registry', df, summary)
    def load_final_delivery_module_inventory_registry(self):
        return self._load_csv('advanced_final_delivery/inventory/module_inventory_registry.csv')

    def save_final_delivery_script_inventory_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/inventory/script_inventory_registry', df, summary)
    def load_final_delivery_script_inventory_registry(self):
        return self._load_csv('advanced_final_delivery/inventory/script_inventory_registry.csv')

    def save_final_delivery_test_inventory_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/inventory/test_inventory_registry', df, summary)
    def load_final_delivery_test_inventory_registry(self):
        return self._load_csv('advanced_final_delivery/inventory/test_inventory_registry.csv')

    def save_final_delivery_docs_inventory_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/inventory/docs_inventory_registry', df, summary)
    def load_final_delivery_docs_inventory_registry(self):
        return self._load_csv('advanced_final_delivery/inventory/docs_inventory_registry.csv')

    def save_final_delivery_report_inventory_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/inventory/report_inventory_registry', df, summary)
    def load_final_delivery_report_inventory_registry(self):
        return self._load_csv('advanced_final_delivery/inventory/report_inventory_registry.csv')

    def save_final_delivery_acceptance_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/evidence/acceptance_evidence_registry', df, summary)
    def load_final_delivery_acceptance_evidence_registry(self):
        return self._load_csv('advanced_final_delivery/evidence/acceptance_evidence_registry.csv')

    def save_final_delivery_manifest_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/evidence/manifest_evidence_registry', df, summary)
    def load_final_delivery_manifest_evidence_registry(self):
        return self._load_csv('advanced_final_delivery/evidence/manifest_evidence_registry.csv')

    def save_final_delivery_validation_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/evidence/validation_evidence_registry', df, summary)
    def load_final_delivery_validation_evidence_registry(self):
        return self._load_csv('advanced_final_delivery/evidence/validation_evidence_registry.csv')

    def save_final_delivery_safety_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/evidence/safety_evidence_registry', df, summary)
    def load_final_delivery_safety_evidence_registry(self):
        return self._load_csv('advanced_final_delivery/evidence/safety_evidence_registry.csv')

    def save_final_delivery_disabled_execution_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/evidence/disabled_execution_evidence_registry', df, summary)
    def load_final_delivery_disabled_execution_evidence_registry(self):
        return self._load_csv('advanced_final_delivery/evidence/disabled_execution_evidence_registry.csv')

    def save_final_delivery_manual_review_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/evidence/manual_review_evidence_registry', df, summary)
    def load_final_delivery_manual_review_evidence_registry(self):
        return self._load_csv('advanced_final_delivery/evidence/manual_review_evidence_registry.csv')

    def save_final_delivery_runbook_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/evidence/runbook_evidence_registry', df, summary)
    def load_final_delivery_runbook_evidence_registry(self):
        return self._load_csv('advanced_final_delivery/evidence/runbook_evidence_registry.csv')

    def save_final_delivery_release_candidate_evidence_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/evidence/release_candidate_evidence_registry', df, summary)
    def load_final_delivery_release_candidate_evidence_registry(self):
        return self._load_csv('advanced_final_delivery/evidence/release_candidate_evidence_registry.csv')

    def save_final_delivery_phase_map_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/phase_maps/phase_map_registry', df, summary)
    def load_final_delivery_phase_map_registry(self):
        return self._load_csv('advanced_final_delivery/phase_maps/phase_map_registry.csv')

    def save_final_delivery_phase_1_100_mvp_summary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/summaries/phase_1_100_mvp_summary_registry', df, summary)
    def load_final_delivery_phase_1_100_mvp_summary_registry(self):
        return self._load_csv('advanced_final_delivery/summaries/phase_1_100_mvp_summary_registry.csv')

    def save_final_delivery_phase_101_160_advanced_summary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/summaries/phase_101_160_advanced_summary_registry', df, summary)
    def load_final_delivery_phase_101_160_advanced_summary_registry(self):
        return self._load_csv('advanced_final_delivery/summaries/phase_101_160_advanced_summary_registry.csv')

    def save_final_delivery_backtest_block_summary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/summaries/backtest_block_summary_registry', df, summary)
    def load_final_delivery_backtest_block_summary_registry(self):
        return self._load_csv('advanced_final_delivery/summaries/backtest_block_summary_registry.csv')

    def save_final_delivery_portfolio_block_summary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/summaries/portfolio_block_summary_registry', df, summary)
    def load_final_delivery_portfolio_block_summary_registry(self):
        return self._load_csv('advanced_final_delivery/summaries/portfolio_block_summary_registry.csv')

    def save_final_delivery_full_system_block_summary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/summaries/full_system_block_summary_registry', df, summary)
    def load_final_delivery_full_system_block_summary_registry(self):
        return self._load_csv('advanced_final_delivery/summaries/full_system_block_summary_registry.csv')

    def save_final_delivery_operator_handover_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/handover/operator_handover_registry', df, summary)
    def load_final_delivery_operator_handover_registry(self):
        return self._load_csv('advanced_final_delivery/handover/operator_handover_registry.csv')

    def save_final_delivery_no_go_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/boundaries/no_go_boundary_registry', df, summary)
    def load_final_delivery_no_go_boundary_registry(self):
        return self._load_csv('advanced_final_delivery/boundaries/no_go_boundary_registry.csv')

    def save_final_delivery_go_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/boundaries/go_boundary_registry', df, summary)
    def load_final_delivery_go_boundary_registry(self):
        return self._load_csv('advanced_final_delivery/boundaries/go_boundary_registry.csv')

    def save_final_delivery_safety_boundary_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/boundaries/safety_boundary_registry', df, summary)
    def load_final_delivery_safety_boundary_registry(self):
        return self._load_csv('advanced_final_delivery/boundaries/safety_boundary_registry.csv')

    def save_final_delivery_forbidden_column_policy_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/boundaries/forbidden_column_policy_registry', df, summary)
    def load_final_delivery_forbidden_column_policy_registry(self):
        return self._load_csv('advanced_final_delivery/boundaries/forbidden_column_policy_registry.csv')

    def save_final_delivery_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/disabled_execution/execution_disabled_report', df, summary)
    def load_final_delivery_execution_disabled_report(self):
        return self._load_csv('advanced_final_delivery/disabled_execution/execution_disabled_report.csv')

    def save_final_delivery_live_trading_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/disabled_execution/live_trading_disabled_report', df, summary)
    def load_final_delivery_live_trading_disabled_report(self):
        return self._load_csv('advanced_final_delivery/disabled_execution/live_trading_disabled_report.csv')

    def save_final_delivery_broker_execution_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/disabled_execution/broker_execution_disabled_report', df, summary)
    def load_final_delivery_broker_execution_disabled_report(self):
        return self._load_csv('advanced_final_delivery/disabled_execution/broker_execution_disabled_report.csv')

    def save_final_delivery_signal_generation_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/disabled_execution/signal_generation_disabled_report', df, summary)
    def load_final_delivery_signal_generation_disabled_report(self):
        return self._load_csv('advanced_final_delivery/disabled_execution/signal_generation_disabled_report.csv')

    def save_final_delivery_prediction_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/disabled_execution/prediction_disabled_report', df, summary)
    def load_final_delivery_prediction_disabled_report(self):
        return self._load_csv('advanced_final_delivery/disabled_execution/prediction_disabled_report.csv')

    def save_final_delivery_deployment_disabled_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/disabled_execution/deployment_disabled_report', df, summary)
    def load_final_delivery_deployment_disabled_report(self):
        return self._load_csv('advanced_final_delivery/disabled_execution/deployment_disabled_report.csv')

    def save_final_delivery_findings_registry(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/findings/findings_registry', df, summary)
    def load_final_delivery_findings_registry(self):
        return self._load_csv('advanced_final_delivery/findings/findings_registry.csv')

    def save_final_delivery_readiness_score_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/scoring/readiness_score_report', df, summary)
    def load_final_delivery_readiness_score_report(self):
        return self._load_csv('advanced_final_delivery/scoring/readiness_score_report.csv')

    def save_final_delivery_manifest(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/manifest/manifest', df, summary)
    def load_final_delivery_manifest(self):
        return self._load_csv('advanced_final_delivery/manifest/manifest.csv')

    def save_final_delivery_health_check(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/health/health_check', df, summary)
    def load_final_delivery_health_check(self):
        return self._load_csv('advanced_final_delivery/health/health_check.csv')

    def save_final_delivery_validation_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/validation/validation_report', df, summary)
    def load_final_delivery_validation_report(self):
        return self._load_csv('advanced_final_delivery/validation/validation_report.csv')

    def save_final_delivery_safety_boundary(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/safety/safety_boundary', df, summary)
    def load_final_delivery_safety_boundary(self):
        return self._load_csv('advanced_final_delivery/safety/safety_boundary.csv')

    def save_final_system_summary_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/summaries/final_system_summary_report', df, summary)
    def load_final_system_summary_report(self):
        return self._load_csv('advanced_final_delivery/summaries/final_system_summary_report.csv')

    def save_final_local_offline_package_summary_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/summaries/final_local_offline_package_summary_report', df, summary)
    def load_final_local_offline_package_summary_report(self):
        return self._load_csv('advanced_final_delivery/summaries/final_local_offline_package_summary_report.csv')

    def save_final_manual_review_summary_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/summaries/final_manual_review_summary_report', df, summary)
    def load_final_manual_review_summary_report(self):
        return self._load_csv('advanced_final_delivery/summaries/final_manual_review_summary_report.csv')

    def save_final_no_live_no_broker_safety_summary_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/summaries/final_no_live_no_broker_safety_summary_report', df, summary)
    def load_final_no_live_no_broker_safety_summary_report(self):
        return self._load_csv('advanced_final_delivery/summaries/final_no_live_no_broker_safety_summary_report.csv')

    def save_final_operator_handover_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/handover/final_operator_handover_report', df, summary)
    def load_final_operator_handover_report(self):
        return self._load_csv('advanced_final_delivery/handover/final_operator_handover_report.csv')

    def save_final_160_phase_completion_report(self, df, summary=None):
        return self._save_csv_json('advanced_final_delivery/completion/final_160_phase_completion_report', df, summary)
    def load_final_160_phase_completion_report(self):
        return self._load_csv('advanced_final_delivery/completion/final_160_phase_completion_report.csv')

    def save_final_delivery_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.base_dir / 'reports' / 'output' / 'advanced_final_delivery' / f'report_{profile_name}.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        if markdown:
            md_path = path.with_suffix('.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return path

    def load_final_delivery_report(self, profile_name: str):
        path = self.base_dir / 'reports' / 'output' / 'advanced_final_delivery' / f'report_{profile_name}.json'
        if not path.exists():
            return {}
        import json
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_final_delivery_reports(self):
        return pd.DataFrame()

    # Phase 106 Data Provider Abstraction Methods
    def save_data_provider_abstraction_profile_registry(self, df, summary=None): pass
    def load_data_provider_abstraction_profile_registry(self): return pd.DataFrame()
    def save_provider_domain_registry(self, df, summary=None): pass
    def load_provider_domain_registry(self): return pd.DataFrame()
    def save_provider_type_registry(self, df, summary=None): pass
    def load_provider_type_registry(self): return pd.DataFrame()
    def save_provider_capability_registry(self, df, summary=None): pass
    def load_provider_capability_registry(self): return pd.DataFrame()
    def save_provider_metadata_schema(self, df, summary=None): pass
    def load_provider_metadata_schema(self): return pd.DataFrame()
    def save_provider_metadata_registry(self, df, summary=None): pass
    def load_provider_metadata_registry(self): return pd.DataFrame()
    def save_provider_request_schema(self, df, summary=None): pass
    def load_provider_request_schema(self): return pd.DataFrame()
    def save_provider_response_schema(self, df, summary=None): pass
    def load_provider_response_schema(self): return pd.DataFrame()
    def save_provider_error_schema(self, df, summary=None): pass
    def load_provider_error_schema(self): return pd.DataFrame()
    def save_provider_interface_contract(self, df, summary=None): pass
    def load_provider_interface_contract(self): return pd.DataFrame()
    def save_provider_adapter_contract(self, df, summary=None): pass
    def load_provider_adapter_contract(self): return pd.DataFrame()
    def save_provider_registry(self, df, summary=None): pass
    def load_provider_registry(self): return pd.DataFrame()
    def save_provider_resolver_map(self, df, summary=None): pass
    def load_provider_resolver_map(self): return pd.DataFrame()
    def save_provider_preference_resolver_report(self, df, summary=None): pass
    def load_provider_preference_resolver_report(self): return pd.DataFrame()
    def save_provider_capability_matcher_report(self, df, summary=None): pass
    def load_provider_capability_matcher_report(self): return pd.DataFrame()
    def save_provider_dry_run_fixture_report(self, df, summary=None): pass
    def load_provider_dry_run_fixture_report(self): return pd.DataFrame()
    def save_manual_file_provider_placeholder(self, df, summary=None): pass
    def load_manual_file_provider_placeholder(self): return pd.DataFrame()
    def save_local_cache_provider_placeholder(self, df, summary=None): pass
    def load_local_cache_provider_placeholder(self): return pd.DataFrame()
    def save_official_api_provider_placeholder(self, df, summary=None): pass
    def load_official_api_provider_placeholder(self): return pd.DataFrame()
    def save_licensed_provider_placeholder(self, df, summary=None): pass
    def load_licensed_provider_placeholder(self): return pd.DataFrame()
    def save_provider_output_schema_contract(self, df, summary=None): pass
    def load_provider_output_schema_contract(self): return pd.DataFrame()
    def save_provider_safety_boundary_report(self, df, summary=None): pass
    def load_provider_safety_boundary_report(self): return pd.DataFrame()
    def save_provider_health_check_report(self, df, summary=None): pass
    def load_provider_health_check_report(self): return pd.DataFrame()
    def save_provider_readiness_score_report(self, df, summary=None): pass
    def load_provider_readiness_score_report(self): return pd.DataFrame()
    def save_provider_quality_report(self, df, summary=None): pass
    def load_provider_quality_report(self): return pd.DataFrame()




