import pandas as pd
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake


class FeatureStore:

    # Phase 67: Local Timeline
    def load_project_event_registry(self) -> pd.DataFrame:
        return self.data_lake.load_project_event_registry()

    def load_phase_chronology_registry(self) -> pd.DataFrame:
        return self.data_lake.load_phase_chronology_registry()

    def load_artifact_evolution_registry(self) -> pd.DataFrame:
        return self.data_lake.load_artifact_evolution_registry()

    def load_file_modification_timeline(self) -> pd.DataFrame:
        return self.data_lake.load_file_modification_timeline()

    def load_report_generation_timeline(self) -> pd.DataFrame:
        return self.data_lake.load_report_generation_timeline()

    def load_datalake_artifact_timeline(self) -> pd.DataFrame:
        return self.data_lake.load_datalake_artifact_timeline()

    def load_documentation_evolution_timeline(self) -> pd.DataFrame:
        return self.data_lake.load_documentation_evolution_timeline()

    def load_command_script_evolution_timeline(self) -> pd.DataFrame:
        return self.data_lake.load_command_script_evolution_timeline()

    def load_evidence_timeline(self) -> pd.DataFrame:
        return self.data_lake.load_evidence_timeline()

    def load_metadata_card_timeline(self) -> pd.DataFrame:
        return self.data_lake.load_metadata_card_timeline()

    def load_knowledge_graph_evolution_timeline(self) -> pd.DataFrame:
        return self.data_lake.load_knowledge_graph_evolution_timeline()

    def load_scenario_regression_event_timeline(self) -> pd.DataFrame:
        return self.data_lake.load_scenario_regression_event_timeline()

    def load_quality_safety_event_timeline(self) -> pd.DataFrame:
        return self.data_lake.load_quality_safety_event_timeline()

    def load_backup_packaging_secrets_event_timeline(self) -> pd.DataFrame:
        return self.data_lake.load_backup_packaging_secrets_event_timeline()

    def load_artifact_temporal_lineage(self) -> pd.DataFrame:
        return self.data_lake.load_artifact_temporal_lineage()

    def load_module_event_cluster_report(self) -> pd.DataFrame:
        return self.data_lake.load_module_event_cluster_report()

    def load_event_freshness_report(self) -> pd.DataFrame:
        return self.data_lake.load_event_freshness_report()

    def load_stale_artifact_timeline_report(self) -> pd.DataFrame:
        return self.data_lake.load_stale_artifact_timeline_report()

    def load_event_gap_report(self) -> pd.DataFrame:
        return self.data_lake.load_event_gap_report()

    def load_phase_event_digest(self) -> str:
        return self.data_lake.load_phase_event_digest()

    def load_change_history_digest(self) -> str:
        return self.data_lake.load_change_history_digest()

    def load_timeline_query_results(self, query_name: str) -> pd.DataFrame:
        return self.data_lake.load_timeline_query_results(query_name)

    def load_timeline_export_manifest(self) -> dict:
        return self.data_lake.load_timeline_export_manifest()

    def load_timeline_validation_report(self) -> pd.DataFrame:
        return self.data_lake.load_timeline_validation_report()

    def load_timeline_quality(self, profile_name: str = "balanced_local_timeline") -> dict:
        return self.data_lake.load_timeline_quality(profile_name)

    def load_local_timeline_report(self, profile_name: str = "balanced_local_timeline") -> dict:
        return self.data_lake.load_local_timeline_report(profile_name)

    def list_available_local_timeline_reports(self) -> pd.DataFrame:
        return self.data_lake.list_local_timeline_reports()

    # Phase 66: Local Knowledge Graph
    def load_graph_node_registry(self) -> pd.DataFrame:
        return self.data_lake.load_graph_node_registry()

    def load_graph_edge_registry(self) -> pd.DataFrame:
        return self.data_lake.load_graph_edge_registry()

    def load_artifact_relationship_graph(self) -> dict:
        return self.data_lake.load_artifact_relationship_graph()

    def load_module_relationship_graph(self) -> pd.DataFrame:
        return self.data_lake.load_module_relationship_graph()

    def load_report_relationship_graph(self) -> pd.DataFrame:
        return self.data_lake.load_report_relationship_graph()

    def load_evidence_relationship_graph(self) -> pd.DataFrame:
        return self.data_lake.load_evidence_relationship_graph()

    def load_card_relationship_graph(self) -> pd.DataFrame:
        return self.data_lake.load_card_relationship_graph()

    def load_scenario_regression_relationship_graph(self) -> pd.DataFrame:
        return self.data_lake.load_scenario_regression_relationship_graph()

    def load_command_report_relationship_graph(self) -> pd.DataFrame:
        return self.data_lake.load_command_report_relationship_graph()

    def load_local_semantic_keyword_index(self) -> pd.DataFrame:
        return self.data_lake.load_local_semantic_keyword_index()

    def load_local_tfidf_index_manifest(self) -> dict:
        return self.data_lake.load_local_tfidf_index_manifest()

    def load_relationship_query_results(self, query_name: str) -> pd.DataFrame:
        return self.data_lake.load_relationship_query_results(query_name)

    def load_graph_neighborhood_report(self, node_id: str) -> pd.DataFrame:
        return self.data_lake.load_graph_neighborhood_report(node_id)

    def load_graph_centrality_summary(self) -> pd.DataFrame:
        return self.data_lake.load_graph_centrality_summary()

    def load_orphan_artifact_report(self) -> pd.DataFrame:
        return self.data_lake.load_orphan_artifact_report()

    def load_graph_gap_report(self) -> pd.DataFrame:
        return self.data_lake.load_graph_gap_report()

    def load_stale_relationship_report(self) -> pd.DataFrame:
        return self.data_lake.load_stale_relationship_report()

    def load_graph_export_manifest(self) -> dict:
        return self.data_lake.load_graph_export_manifest()

    def load_graph_validation_report(self) -> pd.DataFrame:
        return self.data_lake.load_graph_validation_report()

    def load_graph_quality(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_graph_quality(profile_name or "balanced_local_graph")

    def load_local_knowledge_graph_report(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_local_knowledge_graph_report(profile_name or "balanced_local_graph")

    def list_available_local_knowledge_graph_reports(self) -> dict:
        return {"reports": []}


    # ARTIFACT METADATA METHODS
    def load_research_artifact_inventory(self) -> pd.DataFrame:
        return self.data_lake.load_research_artifact_inventory()

    def load_research_artifact_metadata_registry(self) -> pd.DataFrame:
        return self.data_lake.load_research_artifact_metadata_registry()

    def load_model_card_registry(self) -> pd.DataFrame:
        return self.data_lake.load_model_card_registry()

    def load_dataset_card_registry(self) -> pd.DataFrame:
        return self.data_lake.load_dataset_card_registry()

    def load_experiment_card_registry(self) -> pd.DataFrame:
        return self.data_lake.load_experiment_card_registry()

    def load_reproducibility_card_registry(self) -> pd.DataFrame:
        return self.data_lake.load_reproducibility_card_registry()

    def load_backtest_card_registry(self) -> pd.DataFrame:
        return self.data_lake.load_backtest_card_registry()

    def load_scenario_card_registry(self) -> pd.DataFrame:
        return self.data_lake.load_scenario_card_registry()

    def load_regression_card_registry(self) -> pd.DataFrame:
        return self.data_lake.load_regression_card_registry()

    def load_feature_set_card_registry(self) -> pd.DataFrame:
        return self.data_lake.load_feature_set_card_registry()

    def load_synthetic_data_card_registry(self) -> pd.DataFrame:
        return self.data_lake.load_synthetic_data_card_registry()

    def load_research_report_card_registry(self) -> pd.DataFrame:
        return self.data_lake.load_research_report_card_registry()

    def load_artifact_lineage_cards(self) -> pd.DataFrame:
        return self.data_lake.load_artifact_lineage_cards()

    def load_artifact_limitation_cards(self) -> pd.DataFrame:
        return self.data_lake.load_artifact_limitation_cards()

    def load_intended_use_cards(self) -> pd.DataFrame:
        return self.data_lake.load_intended_use_cards()

    def load_non_use_policy_cards(self) -> pd.DataFrame:
        return self.data_lake.load_non_use_policy_cards()

    def load_reproducibility_checklist(self) -> pd.DataFrame:
        return self.data_lake.load_reproducibility_checklist()

    def load_metadata_completeness_report(self) -> pd.DataFrame:
        return self.data_lake.load_metadata_completeness_report()

    def load_metadata_freshness_report(self) -> pd.DataFrame:
        return self.data_lake.load_metadata_freshness_report()

    def load_card_validation_report(self) -> pd.DataFrame:
        return self.data_lake.load_card_validation_report()

    def load_metadata_quality(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_metadata_quality(profile_name or "balanced_local_metadata")

    def load_research_artifact_metadata_export(self) -> dict:
        return self.data_lake.load_research_artifact_metadata_export()

    def load_artifact_metadata_report(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_artifact_metadata_report(profile_name or "balanced_local_metadata")

    def list_available_artifact_metadata_reports(self) -> dict:
        return {"reports": []}



    def load_scenario_regression_registry(self) -> pd.DataFrame:
        return self.data_lake.load_scenario_regression_registry()

    def load_golden_outputs(self) -> pd.DataFrame:
        return self.data_lake.load_golden_outputs()

    def load_golden_output_manifest(self) -> dict:
        return self.data_lake.load_golden_output_manifest()

    def load_snapshot_manifest(self) -> pd.DataFrame:
        return self.data_lake.load_snapshot_manifest()

    def load_snapshot_diff_report(self) -> pd.DataFrame:
        return self.data_lake.load_snapshot_diff_report()

    def load_deterministic_replay_report(self) -> pd.DataFrame:
        return self.data_lake.load_deterministic_replay_report()

    def load_fixture_reproducibility_report(self) -> pd.DataFrame:
        return self.data_lake.load_fixture_reproducibility_report()

    def load_scenario_output_contract_validation(self) -> pd.DataFrame:
        return self.data_lake.load_scenario_output_contract_validation()

    def load_demo_workflow_regression_report(self) -> pd.DataFrame:
        return self.data_lake.load_demo_workflow_regression_report()

    def load_end_to_end_demo_acceptance(self) -> pd.DataFrame:
        return self.data_lake.load_end_to_end_demo_acceptance()

    def load_scenario_drift_report(self) -> pd.DataFrame:
        return self.data_lake.load_scenario_drift_report()

    def load_regression_failure_register(self) -> pd.DataFrame:
        return self.data_lake.load_regression_failure_register()

    def load_regression_acceptance_checklist(self) -> pd.DataFrame:
        return self.data_lake.load_regression_acceptance_checklist()

    def load_scenario_regression_quality(self, profile_name: str | None = None) -> dict:
        if profile_name is None:
            from config.settings import settings
            profile_name = settings.default_scenario_regression_profile
        return self.data_lake.load_scenario_regression_quality(profile_name)

    def load_scenario_regression_report(self, profile_name: str | None = None) -> dict:
        if profile_name is None:
            from config.settings import settings
            profile_name = settings.default_scenario_regression_profile
        return self.data_lake.load_scenario_regression_report(profile_name)

    def list_available_scenario_regression_reports(self) -> dict:
        df = self.data_lake.list_scenario_regression_reports()
        if df.empty:
            return {"reports": []}
        return {"reports": df.to_dict(orient="records")}

    def load_scenario_registry(self) -> pd.DataFrame:
        """Loads scenario registry."""
        return self.data_lake.load_scenario_registry()

    def load_scenario_sample_data_manifest(self) -> pd.DataFrame:
        """Loads scenario sample data manifest."""
        return self.data_lake.load_scenario_sample_data_manifest()

    def load_scenario_fixtures(self) -> pd.DataFrame:
        """Loads scenario fixtures."""
        return self.data_lake.load_scenario_fixtures()

    def load_scenario_expected_outputs(self) -> pd.DataFrame:
        """Loads expected outputs."""
        return self.data_lake.load_scenario_expected_outputs()

    def load_scenario_workflow_packs(self) -> pd.DataFrame:
        """Loads scenario workflow packs."""
        return self.data_lake.load_scenario_workflow_packs()

    def load_demo_command_sequences(self) -> pd.DataFrame:
        """Loads demo command sequences."""
        return self.data_lake.load_demo_command_sequences()

    def load_scenario_dry_run_results(self) -> pd.DataFrame:
        """Loads scenario dry run results."""
        return self.data_lake.load_scenario_dry_run_results()

    def load_scenario_validation_report(self) -> pd.DataFrame:
        """Loads scenario validation report."""
        return self.data_lake.load_scenario_validation_report()

    def load_case_studies(self) -> pd.DataFrame:
        """Loads case studies."""
        return self.data_lake.load_case_studies()

    def load_module_demo_flows(self) -> pd.DataFrame:
        """Loads module demo flows."""
        return self.data_lake.load_module_demo_flows()

    def load_end_to_end_demo_report(self, report_name: str) -> dict:
        """Loads end to end demo report."""
        return self.data_lake.load_end_to_end_demo_report(report_name)

    def load_scenario_quality(self, profile_name: str = None) -> dict:
        """Loads scenario quality report."""
        if profile_name is None:
            profile_name = self.settings.default_scenario_profile
        return self.data_lake.load_scenario_quality(profile_name)

    def load_scenario_report(self, profile_name: str = None) -> dict:
        """Loads scenario report."""
        if profile_name is None:
            profile_name = self.settings.default_scenario_profile
        return self.data_lake.load_scenario_report(profile_name)

    def list_available_scenario_reports(self) -> dict:
        """Lists available scenario reports."""
        df = self.data_lake.list_scenario_reports()
        if df.empty:
            return {"reports": []}
        return {"reports": df.to_dict(orient="records")}


    # Phase 50: Command Center Methods
    def load_command_registry(self) -> pd.DataFrame:
        return self.data_lake.load_command_registry()

    def load_guided_workflows(self) -> pd.DataFrame:
        return self.data_lake.load_guided_workflows()

    def load_safe_runbooks(self) -> pd.DataFrame:
        return self.data_lake.load_safe_runbooks()

    def load_command_dry_run_plan(self, plan_name: str) -> pd.DataFrame:
        return self.data_lake.load_command_dry_run_plan(plan_name)

    def load_project_status(self) -> pd.DataFrame:
        return self.data_lake.load_project_status()

    def load_module_health(self) -> pd.DataFrame:
        return self.data_lake.load_module_health()

    def load_script_availability_matrix(self) -> pd.DataFrame:
        return self.data_lake.load_script_availability_matrix()

    def load_phase_coverage_matrix(self) -> pd.DataFrame:
        return self.data_lake.load_phase_coverage_matrix()

    def load_project_consolidation_report(self, profile_name: str | None = None) -> dict:
        profile = profile_name or "balanced_offline_command_center"
        return self.data_lake.load_project_consolidation_report(profile)

    def load_command_center_quality(self, profile_name: str | None = None) -> dict:
        profile = profile_name or "balanced_offline_command_center"
        return self.data_lake.load_command_center_quality(profile)

    def load_command_center_status(self) -> pd.DataFrame:
        return self.data_lake.load_command_center_status()

    def list_available_command_center_reports(self) -> dict:
        df = self.data_lake.list_command_center_reports()
        if df is None or df.empty:
            return {}
        return {"reports_found": len(df)}

    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def load_mtf_features(
        self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "mtf"):
            return self.data_lake.load_features(spec, timeframe, "mtf")
        return pd.DataFrame()

    def load_mtf_events(
        self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "mtf_events"):
            return self.data_lake.load_features(spec, timeframe, "mtf_events")
        return pd.DataFrame()

    def list_available_mtf_features(self, spec: SymbolSpec) -> dict:
        return {
            "mtf": self.data_lake.list_feature_timeframes(spec, "mtf"),
            "mtf_events": self.data_lake.list_feature_timeframes(spec, "mtf_events"),
        }

    def load_regime_features(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "regime"):
            return self.data_lake.load_features(spec, timeframe, "regime")
        return pd.DataFrame()

    def load_regime_events(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "regime_events"):
            return self.data_lake.load_features(spec, timeframe, "regime_events")
        return pd.DataFrame()

    def list_available_regime_features(self, spec: SymbolSpec) -> dict:
        return {
            "regime": self.data_lake.list_feature_timeframes(spec, "regime"),
            "regime_events": self.data_lake.list_feature_timeframes(
                spec, "regime_events"
            ),
        }

    def load_macro_features(self) -> pd.DataFrame:
        """Load macro features from the data lake."""
        try:
            return self.data_lake.load_feature_set("macro", "macro_features")
        except Exception:
            return pd.DataFrame()

    def load_macro_events(self) -> pd.DataFrame:
        """Load macro events from the data lake."""
        try:
            return self.data_lake.load_feature_set("macro_events", "macro_events")
        except Exception:
            return pd.DataFrame()

    def load_benchmark_features(self) -> pd.DataFrame:
        """Load benchmark features from the data lake."""
        try:
            return self.data_lake.load_feature_set("benchmarks", "benchmark_features")
        except Exception:
            return pd.DataFrame()

    def list_available_macro_features(self) -> dict:
        """List available macro and benchmark features."""
        features = {}

        macro_df = self.load_macro_features()
        if not macro_df.empty:
            features["macro_features"] = list(macro_df.columns)

        events_df = self.load_macro_events()
        if not events_df.empty:
            features["macro_events"] = list(events_df.columns)

        benchmarks_df = self.load_benchmark_features()
        if not benchmarks_df.empty:
            features["benchmarks"] = list(benchmarks_df.columns)

        return features

    def load_asset_profile_features(
        self, spec: SymbolSpec, timeframe: str
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "asset_profiles"):
            return self.data_lake.load_features(spec, timeframe, "asset_profiles")
        return pd.DataFrame()

    def load_asset_profile_events(
        self, spec: SymbolSpec, timeframe: str
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "asset_profile_events"):
            return self.data_lake.load_features(spec, timeframe, "asset_profile_events")
        return pd.DataFrame()

    def load_group_features(self, asset_class: str, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_group_features(asset_class, timeframe):
            return self.data_lake.load_group_features(asset_class, timeframe)
        return pd.DataFrame()

    def list_available_asset_profile_features(self, spec: SymbolSpec) -> dict:
        return {
            "asset_profiles": self.data_lake.list_feature_timeframes(
                spec, "asset_profiles"
            ),
            "asset_profile_events": self.data_lake.list_feature_timeframes(
                spec, "asset_profile_events"
            ),
        }

    def list_available_group_features(self, asset_class: str) -> dict:
        return {
            "group_features": self.data_lake.list_group_feature_timeframes(asset_class)
        }

    def load_signal_candidates(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "signal_candidates"):
            return self.data_lake.load_features(spec, timeframe, "signal_candidates")
        return pd.DataFrame()

    def load_signal_pool(
        self, timeframe: str, profile_name: str = "balanced_candidate_scoring"
    ) -> pd.DataFrame:
        if self.data_lake.has_signal_pool(timeframe, profile_name):
            return self.data_lake.load_signal_pool(timeframe, profile_name)
        return pd.DataFrame()

    def list_available_signal_candidates(self, spec: SymbolSpec) -> dict:
        return {
            "signal_candidates": self.data_lake.list_feature_timeframes(
                spec, "signal_candidates"
            )
        }

    def list_available_signal_pools(self) -> dict:
        # Simplistic implementation just to satisfy API
        return {"signal_pool": ["1d"]}

    def load_decision_candidates(
        self, spec: SymbolSpec, timeframe: str
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "decision_candidates"):
            return self.data_lake.load_features(spec, timeframe, "decision_candidates")
        return pd.DataFrame()

    def load_decision_pool(
        self, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        prof = profile_name or "balanced_directional_decision"
        if self.data_lake.has_decision_pool(timeframe, prof):
            return self.data_lake.load_decision_pool(timeframe, prof)
        return pd.DataFrame()

    def list_available_decision_candidates(self, spec: SymbolSpec) -> dict:
        return {
            "decision_candidates": self.data_lake.list_feature_timeframes(
                spec, "decision_candidates"
            )
        }

    def list_available_decision_pools(self) -> dict:
        return {"decision_pool": ["1d"]}

    # --- Risk Candidates (Phase 23 fix if missing) ---
    def load_risk_candidates(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if not self.data_lake.has_features(spec, timeframe, "risk_candidates"):
            return pd.DataFrame()
        return self.data_lake.load_features(spec, timeframe, "risk_candidates")

    def load_risk_pool(
        self, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        p_name = profile_name or self.settings.default_risk_profile
        try:
            # Assuming data_lake has load_risk_pool, fallback if not
            if hasattr(self.data_lake, "load_risk_pool"):
                return self.data_lake.load_risk_pool(timeframe, p_name)
            return pd.DataFrame()
        except FileNotFoundError:
            return pd.DataFrame()

    # --- Sizing Candidates (Phase 24) ---
    def load_sizing_candidates(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if not self.data_lake.has_features(spec, timeframe, "sizing_candidates"):
            return pd.DataFrame()
        return self.data_lake.load_features(spec, timeframe, "sizing_candidates")

    def load_sizing_pool(
        self, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        p_name = profile_name or self.settings.default_sizing_profile
        try:
            return self.data_lake.load_sizing_pool(timeframe, p_name)
        except FileNotFoundError:
            return pd.DataFrame()

    def list_available_sizing_candidates(self, spec: SymbolSpec) -> list[str]:
        return self.data_lake.list_feature_timeframes(spec, "sizing_candidates")

    def list_available_sizing_pools(self) -> dict:
        # Simplistic implementation matching others if exists
        return {}

    def load_level_candidates(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "level_candidates"):
            return self.data_lake.load_features(spec, timeframe, "level_candidates")
        return pd.DataFrame()

    def load_level_pool(
        self, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        prof = profile_name or "balanced_theoretical_levels"
        return self.data_lake.load_level_pool(timeframe, prof)

    def list_available_level_candidates(self, spec: SymbolSpec) -> dict:
        return {
            "level_candidates": self.data_lake.list_feature_timeframes(
                spec, "level_candidates"
            ),
        }

    def list_available_level_pools(self) -> dict:
        # Dummy implementation
        return {"level_pools": []}

    def load_backtest_trades(
        self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        prof = profile_name or "balanced_candidate_backtest"
        if hasattr(self.lake, "load_backtest_trades"):
            return self.lake.load_backtest_trades(spec.symbol, timeframe, prof)
        return pd.DataFrame()

    def load_backtest_equity_curve(
        self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        prof = profile_name or "balanced_candidate_backtest"
        if hasattr(self.lake, "load_backtest_equity_curve"):
            return self.lake.load_backtest_equity_curve(spec.symbol, timeframe, prof)
        return pd.DataFrame()

    def list_available_backtests(self, spec: SymbolSpec | None = None) -> dict:
        if hasattr(self.lake, "list_backtest_runs"):
            runs = self.lake.list_backtest_runs()
            if not runs.empty and spec:
                runs = runs[runs["symbol"] == spec.symbol]
            return runs.to_dict(orient="records") if not runs.empty else []
        return []

    # --- ML Dataset Methods ---
    def load_ml_feature_matrix(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        return self.data_lake.load_ml_feature_matrix(spec.symbol, timeframe, profile_name)

    def load_ml_target_frame(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        return self.data_lake.load_ml_target_frame(spec.symbol, timeframe, profile_name)

    def load_ml_supervised_dataset(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        return self.data_lake.load_ml_supervised_dataset(spec.symbol, timeframe, profile_name)

    def load_ml_dataset_metadata(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None) -> dict:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        return self.data_lake.load_ml_dataset_metadata(spec.symbol, timeframe, profile_name)

    def list_available_ml_datasets(self, spec: SymbolSpec | None = None) -> dict:
        df = self.data_lake.list_ml_datasets()
        if df.empty:
             return {}
        if spec:
             df = df[df['symbol'] == spec.symbol]

        result = {}
        for _, row in df.iterrows():
             sym = row['symbol']
             tf = row['timeframe']
             prof = row['profile']
             key = f"{sym}_{tf}_{prof}"
             result[key] = row.to_dict()
        return result

    def load_ml_model_evaluation(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None, model_id: str | None = None) -> dict:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        if not model_id:
             return {}
        return self.data_lake.load_ml_model_evaluation(spec.symbol, timeframe, profile_name, model_id)

    def load_ml_cv_results(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None, model_id: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        if not model_id:
             return pd.DataFrame()
        return self.data_lake.load_ml_cv_results(spec.symbol, timeframe, profile_name, model_id)

    def load_ml_model_quality(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None, model_id: str | None = None) -> dict:
        if profile_name is None:
             from config.settings import settings
             profile_name = settings.default_ml_dataset_profile
        if not model_id:
             return {}
        return self.data_lake.load_ml_model_quality(spec.symbol, timeframe, profile_name, model_id)

    def list_available_ml_models(self, spec: SymbolSpec | None = None) -> dict:
        df = self.data_lake.list_ml_model_registry()
        if df.empty:
             return {}
        if spec:
             df = df[df['symbol'] == spec.symbol]

        result = {}
        for _, row in df.iterrows():
            sym = row.get("symbol")
            tf = row.get("timeframe")
            if sym not in result:
                result[sym] = {}
            if tf not in result[sym]:
                result[sym][tf] = []
            result[sym][tf].append(row.to_dict())
        return result


    # --- PHASE 32: ML CONTEXT INTEGRATION ---
    def load_ml_integration_features(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None, layer: str = "context") -> pd.DataFrame:
        profile = profile_name or "balanced_ml_context_integration"
        return self.data_lake.load_ml_integration_features(spec.symbol, timeframe, profile, layer)

    def load_ml_alignment_report(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None, layer: str = "signal") -> pd.DataFrame:
        profile = profile_name or "balanced_ml_context_integration"
        return self.data_lake.load_ml_alignment_report(spec.symbol, timeframe, profile, layer)

    def load_ml_conflict_report(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_ml_context_integration"
        return self.data_lake.load_ml_conflict_report(spec.symbol, timeframe, profile)

    def load_ml_integration_quality(self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None) -> dict:
        profile = profile_name or "balanced_ml_context_integration"
        return self.data_lake.load_ml_integration_quality(spec.symbol, timeframe, profile)

    def list_available_ml_integration_reports(self, spec: SymbolSpec | None = None) -> dict:
        df = self.data_lake.list_ml_integration_reports()
        if df.empty:
            return {}

        if spec:
            df = df[df["symbol"] == spec.symbol]

        if df.empty:
            return {}

        # Group by symbol and timeframe
        res = {}
        for _, row in df.iterrows():
            sym = row["symbol"]
            tf = row["timeframe"]
            key = f"{sym}_{tf}"
            if key not in res:
                res[key] = []
            res[key].append({
                "layer": row["layer"],
                "profile": row["profile"]
            })
        return res

    # --- Observability Reports Load ---
    def load_latest_system_health_report(self) -> pd.DataFrame:
        """Load the latest system healthcheck report."""
        if hasattr(self.data_lake, "load_observability_health_report"):
            return self.data_lake.load_observability_health_report("system_healthcheck")
        return pd.DataFrame()

    def load_latest_runtime_metrics(self) -> pd.DataFrame:
        """Load the latest runtime metrics."""
        if hasattr(self.data_lake, "load_runtime_metrics"):
            return self.data_lake.load_runtime_metrics("current_session")
        return pd.DataFrame()

    def load_latest_data_freshness_report(self) -> pd.DataFrame:
        """Load the latest data freshness report."""
        if hasattr(self.data_lake, "load_data_freshness_report"):
            return self.data_lake.load_data_freshness_report()
        return pd.DataFrame()

    def load_latest_artifact_integrity_report(self) -> pd.DataFrame:
        """Load the latest artifact integrity report."""
        if hasattr(self.data_lake, "load_artifact_integrity_report"):
            return self.data_lake.load_artifact_integrity_report()
        return pd.DataFrame()

    def load_latest_diagnostics_report(self) -> dict:
        """Load the latest self-diagnostics report."""
        if hasattr(self.data_lake, "load_diagnostics_report"):
            return self.data_lake.load_diagnostics_report("self_diagnostics")
        return {}

    def list_available_observability_reports(self) -> dict:
        """List all available observability reports by type."""
        if hasattr(self.data_lake, "list_observability_reports"):
            df = self.data_lake.list_observability_reports()
            if not df.empty:
                # Group by report_type
                grouped = df.groupby('report_type').apply(lambda x: x.to_dict('records')).to_dict()
                return grouped
        return {}

    def load_latest_security_audit_report(self) -> pd.DataFrame:
        if hasattr(self.data_lake, "load_security_audit_report"): return self.data_lake.load_security_audit_report("security_audit")
        return pd.DataFrame()
    def load_latest_secret_hygiene_report(self) -> pd.DataFrame:
        if hasattr(self.data_lake, "load_secret_hygiene_report"): return self.data_lake.load_secret_hygiene_report()
        return pd.DataFrame()
    def load_latest_config_hardening_report(self) -> pd.DataFrame:
        if hasattr(self.data_lake, "load_config_hardening_report"): return self.data_lake.load_config_hardening_report()
        return pd.DataFrame()
    def load_latest_readiness_audit(self) -> pd.DataFrame:
        if hasattr(self.data_lake, "load_readiness_audit"): return self.data_lake.load_readiness_audit()
        return pd.DataFrame()
    def load_latest_security_quality(self) -> dict:
        if hasattr(self.data_lake, "load_security_quality"): return self.data_lake.load_security_quality("security_audit")
        return {}
    def list_available_security_reports(self) -> dict: return {}


    # Phase 42: Portfolio Regime Research
    def load_portfolio_regimes(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        prof = profile_name or "balanced_regime_portfolio_research"
        if hasattr(self.data_lake, 'load_portfolio_regimes'):
            return self.data_lake.load_portfolio_regimes(timeframe, prof)
        return pd.DataFrame()

    def load_regime_conditioned_returns(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        prof = profile_name or "balanced_regime_portfolio_research"
        if hasattr(self.data_lake, 'load_regime_conditioned_returns'):
            return self.data_lake.load_regime_conditioned_returns(timeframe, prof)
        return pd.DataFrame()

    def load_regime_correlation_summary(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        prof = profile_name or "balanced_regime_portfolio_research"
        if hasattr(self.data_lake, 'load_regime_correlation_summary'):
            return self.data_lake.load_regime_correlation_summary(timeframe, prof)
        return pd.DataFrame()

    def load_macro_scenario_sensitivity(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        prof = profile_name or "balanced_regime_portfolio_research"
        if hasattr(self.data_lake, 'load_macro_scenario_sensitivity'):
            return self.data_lake.load_macro_scenario_sensitivity(timeframe, prof)
        return pd.DataFrame()

    def load_basket_stress_test_results(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        prof = profile_name or "balanced_regime_portfolio_research"
        if hasattr(self.data_lake, 'load_basket_stress_test_results'):
            return self.data_lake.load_basket_stress_test_results(timeframe, prof)
        return pd.DataFrame()

    def load_drawdown_clusters(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        prof = profile_name or "balanced_regime_portfolio_research"
        if hasattr(self.data_lake, 'load_drawdown_clusters'):
            return self.data_lake.load_drawdown_clusters(timeframe, prof)
        return pd.DataFrame()

    def load_recovery_analysis(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        prof = profile_name or "balanced_regime_portfolio_research"
        if hasattr(self.data_lake, 'load_recovery_analysis'):
            return self.data_lake.load_recovery_analysis(timeframe, prof)
        return pd.DataFrame()

    def load_tail_risk_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        prof = profile_name or "balanced_regime_portfolio_research"
        if hasattr(self.data_lake, 'load_tail_risk_table'):
            return self.data_lake.load_tail_risk_table(timeframe, prof)
        return pd.DataFrame()

    def load_risk_regime_exposure(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        prof = profile_name or "balanced_regime_portfolio_research"
        if hasattr(self.data_lake, 'load_risk_regime_exposure'):
            return self.data_lake.load_risk_regime_exposure(timeframe, prof)
        return pd.DataFrame()

    def load_portfolio_regime_report(self, timeframe: str, profile_name: str | None = None) -> dict:
        prof = profile_name or "balanced_regime_portfolio_research"
        if hasattr(self.data_lake, 'load_portfolio_regime_report'):
            return self.data_lake.load_portfolio_regime_report(timeframe, prof)
        return {}

    def list_available_portfolio_regime_reports(self) -> dict:
        return {}

    # Phase 43: Synthetic Indices Data Loading
    def load_synthetic_index_definitions(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_synthetic_index_definitions(timeframe, profile_name)

    def load_synthetic_index_levels(self, index_id: str, timeframe: str) -> pd.DataFrame:
        return self.data_lake.load_synthetic_index_levels(index_id, timeframe)

    def load_relative_strength_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_relative_strength_table(timeframe, profile_name)

    def load_relative_momentum_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_relative_momentum_table(timeframe, profile_name)

    def load_universe_rotation_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_universe_rotation_table(timeframe, profile_name)

    def load_leadership_laggard_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_leadership_laggard_table(timeframe, profile_name)

    def load_synthetic_benchmark_comparison(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_synthetic_benchmark_comparison(timeframe, profile_name)

    def load_synthetic_index_performance(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_synthetic_index_performance(timeframe, profile_name)

    def load_synthetic_index_report(self, timeframe: str, profile_name: str | None = None) -> dict:
        if profile_name is None:
             profile_name = self.settings.default_synthetic_index_profile
        return self.data_lake.load_synthetic_index_report(timeframe, profile_name)

    def list_available_synthetic_index_reports(self) -> dict:
        df = self.data_lake.list_synthetic_index_reports()
        if df.empty:
             return {}
        return df.to_dict(orient="records")

    # --- Phase 44: Factor Research Loading ---

    def load_factor_definitions(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        if profile_name is None:
            profile_name = self.settings.default_factor_research_profile
        return self.data_lake.load_factor_definitions(timeframe, profile_name)

    def load_factor_score_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
         if profile_name is None:
            profile_name = self.settings.default_factor_research_profile
         return self.data_lake.load_factor_score_table(timeframe, profile_name)

    def load_factor_rank_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
         if profile_name is None:
            profile_name = self.settings.default_factor_research_profile
         return self.data_lake.load_factor_rank_table(timeframe, profile_name)

    def load_factor_bucket_returns(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
         if profile_name is None:
            profile_name = self.settings.default_factor_research_profile
         return self.data_lake.load_factor_bucket_returns(timeframe, profile_name)

    def load_factor_backtest_results(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
         if profile_name is None:
            profile_name = self.settings.default_factor_research_profile
         return self.data_lake.load_factor_backtest_results(timeframe, profile_name)

    def load_factor_ic_report(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
         if profile_name is None:
            profile_name = self.settings.default_factor_research_profile
         return self.data_lake.load_factor_ic_report(timeframe, profile_name)

    def load_factor_stability_report(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
         if profile_name is None:
            profile_name = self.settings.default_factor_research_profile
         return self.data_lake.load_factor_stability_report(timeframe, profile_name)

    def load_factor_exposure_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
         if profile_name is None:
            profile_name = self.settings.default_factor_research_profile
         return self.data_lake.load_factor_exposure_table(timeframe, profile_name)

    def load_factor_neutral_basket(self, timeframe: str, profile_name: str | None = None) -> dict:
         if profile_name is None:
            profile_name = self.settings.default_factor_research_profile
         return self.data_lake.load_factor_neutral_basket(timeframe, profile_name)

    def load_factor_research_report(self, timeframe: str, profile_name: str | None = None) -> dict:
         if profile_name is None:
            profile_name = self.settings.default_factor_research_profile
         return self.data_lake.load_factor_research_report(timeframe, profile_name)

    def list_available_factor_research_reports(self) -> dict:
         df = self.data_lake.list_factor_research_reports()
         if df.empty:
             return {}
         return df.to_dict(orient="records")

    # Phase 45: Meta Research
    def load_meta_evidence_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_evidence_table(timeframe, profile)

    def load_meta_source_reliability(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_source_reliability(timeframe, profile)

    def load_meta_consensus_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_consensus_table(timeframe, profile)

    def load_meta_conflict_report(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_conflict_report(timeframe, profile)

    def load_meta_uncertainty_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_uncertainty_table(timeframe, profile)

    def load_meta_ensemble_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_ensemble_table(timeframe, profile)

    def load_meta_quality_adjusted_ranking(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_quality_adjusted_ranking(timeframe, profile)

    def load_meta_symbol_snapshot(self, spec, timeframe: str, profile_name: str | None = None) -> dict:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_symbol_snapshot(spec.symbol, timeframe, profile)

    def load_meta_research_report(self, timeframe: str, profile_name: str | None = None) -> dict:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_research_report(timeframe, profile)

    def list_available_meta_research_reports(self) -> dict:
        df = self.data_lake.list_meta_research_reports()
        if df.empty:
            return {}
        return df.to_dict(orient="records")


    # Phase 47 Governance Methods
    def load_artifact_inventory(self):
        return self.data_lake.load_artifact_inventory()

    def load_artifact_fingerprints(self):
        return self.data_lake.load_artifact_fingerprints()

    def load_provenance_records(self):
        return self.data_lake.load_provenance_records()

    def load_lineage_nodes(self):
        return self.data_lake.load_lineage_nodes()

    def load_lineage_edges(self):
        return self.data_lake.load_lineage_edges()

    def load_dependency_trace(self, trace_name: str):
        return self.data_lake.load_dependency_trace(trace_name)

    def load_audit_trail(self):
        return self.data_lake.load_audit_trail()

    def load_source_attribution(self):
        return self.data_lake.load_source_attribution()

    def load_governance_checklist(self):
        return self.data_lake.load_governance_checklist()

    def load_governance_quality(self, profile_name: str | None = None):
        name = profile_name or "balanced_research_governance"
        return self.data_lake.load_governance_quality(name)

    def load_research_governance_report(self, profile_name: str | None = None):
        name = profile_name or "balanced_research_governance"
        return self.data_lake.load_research_governance_report(name)

    def list_available_governance_reports(self):
        return self.data_lake.list_governance_reports().to_dict(orient="records")


    # Phase 48: Research Planning
    def load_research_planning_signals(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_research_planning_signals(timeframe, profile_name or "balanced_research_planning")

    def load_research_task_registry(self, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_research_task_registry(profile_name or "balanced_research_planning")

    def load_research_backlog(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_research_backlog(timeframe, profile_name or "balanced_research_planning")

    def load_research_priority_scores(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_research_priority_scores(timeframe, profile_name or "balanced_research_planning")

    def load_next_best_experiments(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_next_best_experiments(timeframe, profile_name or "balanced_research_planning")

    def load_research_debt_report(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_research_debt_report(timeframe, profile_name or "balanced_research_planning")

    def load_research_opportunity_report(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_research_opportunity_report(timeframe, profile_name or "balanced_research_planning")

    def load_roadmap_health_snapshot(self, timeframe: str, profile_name: str | None = None) -> dict:
        return self.data_lake.load_roadmap_health_snapshot(timeframe, profile_name or "balanced_research_planning")

    def load_task_orchestration_plan(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        return self.data_lake.load_task_orchestration_plan(timeframe, profile_name or "balanced_research_planning")

    def load_research_planning_report(self, timeframe: str, profile_name: str | None = None) -> dict:
        return self.data_lake.load_research_planning_report(timeframe, profile_name or "balanced_research_planning")

    def list_available_research_planning_reports(self) -> dict:
        df = self.data_lake.list_research_planning_reports()
        if df.empty:
            return {"reports": []}
        return {"reports": df.to_dict("records")}


    # Phase 49 Knowledge Base Methods
    def load_knowledge_documents(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_knowledge_documents'):
            return self.data_lake.load_knowledge_documents()
        return pd.DataFrame()

    def load_knowledge_chunks(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_knowledge_chunks'):
            return self.data_lake.load_knowledge_chunks()
        return pd.DataFrame()

    def load_knowledge_index_summary(self) -> dict:
        if hasattr(self.data_lake, 'load_knowledge_index_summary'):
            return self.data_lake.load_knowledge_index_summary()
        return {}

    def load_retrieval_results(self, query_id: str) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_retrieval_results'):
            return self.data_lake.load_retrieval_results(query_id)
        return pd.DataFrame()

    def load_memory_cards(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_memory_cards'):
            return self.data_lake.load_memory_cards()
        return pd.DataFrame()

    def load_symbol_memory_card(self, symbol: str) -> dict:
        if hasattr(self.data_lake, 'load_symbol_memory_card'):
            return self.data_lake.load_symbol_memory_card(symbol)
        return {}

    def load_decision_journal(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_decision_journal'):
            return self.data_lake.load_decision_journal()
        return pd.DataFrame()

    def load_analyst_notes(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_analyst_notes'):
            return self.data_lake.load_analyst_notes()
        return pd.DataFrame()

    def load_recent_findings_digest(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_recent_findings_digest'):
            return self.data_lake.load_recent_findings_digest()
        return pd.DataFrame()

    def load_workspace_summary(self) -> dict:
        if hasattr(self.data_lake, 'load_workspace_summary'):
            return self.data_lake.load_workspace_summary()
        return {}

    def load_kb_quality(self, profile_name: str | None = None) -> dict:
        if hasattr(self.data_lake, 'load_kb_quality'):
            return self.data_lake.load_kb_quality(profile_name or "balanced_local_knowledge_base")
        return {}

    def load_knowledge_base_report(self, profile_name: str | None = None) -> dict:
        if hasattr(self.data_lake, 'load_knowledge_base_report'):
            return self.data_lake.load_knowledge_base_report(profile_name or "knowledge_index_report")
        return {}

    def list_available_knowledge_base_reports(self) -> dict:
        if hasattr(self.data_lake, 'list_knowledge_base_reports'):
            df = self.data_lake.list_knowledge_base_reports()
            if not df.empty:
                return df.to_dict(orient='records')
        return {}

    def load_runtime_profiles(self) -> pd.DataFrame:
        return self.data_lake.load_runtime_profiles()

    def load_memory_profiles(self) -> pd.DataFrame:
        return self.data_lake.load_memory_profiles()

    def load_cpu_gpu_awareness(self) -> pd.DataFrame:
        return self.data_lake.load_cpu_gpu_awareness()

    def load_resource_budgets(self) -> pd.DataFrame:
        return self.data_lake.load_resource_budgets()

    def load_resource_budget_violations(self) -> pd.DataFrame:
        return self.data_lake.load_resource_budget_violations()

    def load_cache_inventory(self) -> pd.DataFrame:
        return self.data_lake.load_cache_inventory()

    def load_cache_strategy(self) -> pd.DataFrame:
        return self.data_lake.load_cache_strategy()

    def load_cache_hit_miss_report(self) -> pd.DataFrame:
        return self.data_lake.load_cache_hit_miss_report()

    def load_batch_plans(self) -> pd.DataFrame:
        return self.data_lake.load_batch_plans()

    def load_large_run_stability_report(self) -> pd.DataFrame:
        return self.data_lake.load_large_run_stability_report()

    def load_bottleneck_report(self) -> pd.DataFrame:
        return self.data_lake.load_bottleneck_report()

    def load_optimization_recommendations(self) -> pd.DataFrame:
        return self.data_lake.load_optimization_recommendations()

    def load_performance_quality(self, profile_name: str) -> dict:
        return self.data_lake.load_performance_quality(profile_name)

    def load_performance_report(self, profile_name: str) -> dict:
        return self.data_lake.load_performance_report(profile_name)

    def list_available_performance_reports(self) -> pd.DataFrame:
        return self.data_lake.list_performance_reports()


    # --- MAINTENANCE SUPPORT ---
    def load_storage_inventory(self) -> pd.DataFrame:
        return self.data_lake.load_storage_inventory()

    def load_retention_policies(self) -> pd.DataFrame:
        return self.data_lake.load_retention_policies()

    def load_cleanup_candidates(self) -> pd.DataFrame:
        return self.data_lake.load_cleanup_candidates()

    def load_cleanup_dry_run_plan(self) -> pd.DataFrame:
        return self.data_lake.load_cleanup_dry_run_plan()

    def load_archive_candidates(self) -> pd.DataFrame:
        return self.data_lake.load_archive_candidates()

    def load_archive_manifest(self, archive_id: str) -> dict:
        return self.data_lake.load_archive_manifest(archive_id)

    def load_archive_dry_run_plan(self) -> pd.DataFrame:
        return self.data_lake.load_archive_dry_run_plan()

    def load_report_rotation_plan(self) -> pd.DataFrame:
        return self.data_lake.load_report_rotation_plan()

    def load_log_rotation_plan(self) -> pd.DataFrame:
        return self.data_lake.load_log_rotation_plan()

    def load_cache_pruning_plan(self) -> pd.DataFrame:
        return self.data_lake.load_cache_pruning_plan()

    def load_duplicate_artifact_report(self) -> pd.DataFrame:
        return self.data_lake.load_duplicate_artifact_report()

    def load_stale_artifact_report(self) -> pd.DataFrame:
        return self.data_lake.load_stale_artifact_report()

    def load_large_artifact_report(self) -> pd.DataFrame:
        return self.data_lake.load_large_artifact_report()

    def load_storage_growth_report(self) -> pd.DataFrame:
        return self.data_lake.load_storage_growth_report()

    def load_storage_lifecycle_health(self) -> pd.DataFrame:
        return self.data_lake.load_storage_lifecycle_health()

    def load_maintenance_quality(self, profile_name: str | None = None) -> dict:
        if profile_name is None:
            profile_name = "balanced_local_maintenance"
        return self.data_lake.load_maintenance_quality(profile_name)

    def load_maintenance_report(self, profile_name: str | None = None) -> dict:
        if profile_name is None:
            profile_name = "balanced_local_maintenance"
        return self.data_lake.load_maintenance_report(profile_name)

    def list_available_maintenance_reports(self) -> dict:
        df = self.data_lake.list_maintenance_reports()
        return {"count": len(df), "files": df["file_name"].tolist() if not df.empty else []}



    # --- MAINTENANCE SUPPORT ---
    def load_storage_inventory(self) -> pd.DataFrame:
        return self.data_lake.load_storage_inventory()

    def load_retention_policies(self) -> pd.DataFrame:
        return self.data_lake.load_retention_policies()

    def load_cleanup_candidates(self) -> pd.DataFrame:
        return self.data_lake.load_cleanup_candidates()

    def load_cleanup_dry_run_plan(self) -> pd.DataFrame:
        return self.data_lake.load_cleanup_dry_run_plan()

    def load_archive_candidates(self) -> pd.DataFrame:
        return self.data_lake.load_archive_candidates()

    def load_archive_manifest(self, archive_id: str) -> dict:
        return self.data_lake.load_archive_manifest(archive_id)

    def load_archive_dry_run_plan(self) -> pd.DataFrame:
        return self.data_lake.load_archive_dry_run_plan()

    def load_report_rotation_plan(self) -> pd.DataFrame:
        return self.data_lake.load_report_rotation_plan()

    def load_log_rotation_plan(self) -> pd.DataFrame:
        return self.data_lake.load_log_rotation_plan()

    def load_cache_pruning_plan(self) -> pd.DataFrame:
        return self.data_lake.load_cache_pruning_plan()

    def load_duplicate_artifact_report(self) -> pd.DataFrame:
        return self.data_lake.load_duplicate_artifact_report()

    def load_stale_artifact_report(self) -> pd.DataFrame:
        return self.data_lake.load_stale_artifact_report()

    def load_large_artifact_report(self) -> pd.DataFrame:
        return self.data_lake.load_large_artifact_report()

    def load_storage_growth_report(self) -> pd.DataFrame:
        return self.data_lake.load_storage_growth_report()

    def load_storage_lifecycle_health(self) -> pd.DataFrame:
        return self.data_lake.load_storage_lifecycle_health()

    def load_maintenance_quality(self, profile_name: str | None = None) -> dict:
        if profile_name is None:
            profile_name = "balanced_local_maintenance"
        return self.data_lake.load_maintenance_quality(profile_name)

    def load_maintenance_report(self, profile_name: str | None = None) -> dict:
        if profile_name is None:
            profile_name = "balanced_local_maintenance"
        return self.data_lake.load_maintenance_report(profile_name)

    def list_available_maintenance_reports(self) -> dict:
        df = self.data_lake.list_maintenance_reports()
        return {"count": len(df), "files": df["file_name"].tolist() if not df.empty else []}


    # --- Analyst UX Support ---
    def load_command_alias_registry(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_command_alias_registry'):
            return self.data_lake.load_command_alias_registry()
        return pd.DataFrame()

    def load_analyst_intents(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_analyst_intents'):
            return self.data_lake.load_analyst_intents()
        return pd.DataFrame()

    def load_safe_command_suggestions(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_safe_command_suggestions'):
            return self.data_lake.load_safe_command_suggestions()
        return pd.DataFrame()

    def load_prompt_pack_registry(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_prompt_pack_registry'):
            return self.data_lake.load_prompt_pack_registry()
        return pd.DataFrame()

    def load_prompt_pack_manifest(self) -> dict:
        if hasattr(self.data_lake, 'load_prompt_pack_manifest'):
            return self.data_lake.load_prompt_pack_manifest()
        return {}

    def load_workflow_shortcuts(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_workflow_shortcuts'):
            return self.data_lake.load_workflow_shortcuts()
        return pd.DataFrame()

    def load_query_mappings(self, report_name: str) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_query_mappings'):
            return self.data_lake.load_query_mappings(report_name)
        return pd.DataFrame()

    def load_analyst_task_board(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_analyst_task_board'):
            return self.data_lake.load_analyst_task_board()
        return pd.DataFrame()

    def load_productivity_checklist(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_productivity_checklist'):
            return self.data_lake.load_productivity_checklist()
        return pd.DataFrame()

    def load_ux_validation_report(self) -> pd.DataFrame:
        if hasattr(self.data_lake, 'load_ux_validation_report'):
            return self.data_lake.load_ux_validation_report()
        return pd.DataFrame()

    def load_ux_quality(self, profile_name: str | None = None) -> dict:
        if hasattr(self.data_lake, 'load_ux_quality'):
            return self.data_lake.load_ux_quality(profile_name or "balanced_analyst_productivity")
        return {}

    def load_ux_report(self, report_name: str) -> dict:
        if hasattr(self.data_lake, 'load_ux_report'):
            return self.data_lake.load_ux_report(report_name)
        return {}

    def list_available_ux_reports(self) -> dict:
        if hasattr(self.data_lake, 'list_ux_reports'):
            df = self.data_lake.list_ux_reports()
            return {"count": len(df), "files": df["file_name"].tolist() if not df.empty else []}
        return {}

    # --- Final Review ---
    def load_architecture_audit(self) -> pd.DataFrame:
        return self.data_lake.load_architecture_audit()

    def load_safety_audit(self) -> pd.DataFrame:
        return self.data_lake.load_safety_audit()

    def load_integration_audit(self) -> pd.DataFrame:
        return self.data_lake.load_integration_audit()

    def load_command_audit(self) -> pd.DataFrame:
        return self.data_lake.load_command_audit()

    def load_datalake_contract_audit(self) -> pd.DataFrame:
        return self.data_lake.load_datalake_contract_audit()

    def load_report_output_audit(self) -> pd.DataFrame:
        return self.data_lake.load_report_output_audit()

    def load_documentation_audit(self) -> pd.DataFrame:
        return self.data_lake.load_documentation_audit()

    def load_quality_gate_audit(self) -> pd.DataFrame:
        return self.data_lake.load_quality_gate_audit()

    def load_readiness_audit(self) -> pd.DataFrame:
        return self.data_lake.load_readiness_audit()

    def load_final_risk_register(self) -> pd.DataFrame:
        return self.data_lake.load_final_risk_register()

    def load_final_gap_register(self) -> pd.DataFrame:
        return self.data_lake.load_final_gap_register()

    def load_final_acceptance_checklist(self) -> pd.DataFrame:
        return self.data_lake.load_final_acceptance_checklist()

    def load_final_acceptance_snapshot(self) -> dict:
        return self.data_lake.load_final_acceptance_snapshot()

    def load_release_readiness_dry_run(self) -> pd.DataFrame:
        return self.data_lake.load_release_readiness_dry_run()

    def load_final_review_quality(self, profile_name: str = "balanced_final_review") -> dict:
        return self.data_lake.load_final_review_quality(profile_name)

    def load_final_review_report(self, profile_name: str = "balanced_final_review") -> dict:
        return self.data_lake.load_final_review_report(profile_name)

    def list_available_final_review_reports(self) -> pd.DataFrame:
        return self.data_lake.list_final_review_reports()


    # Phase 61: Portable Packaging
    def load_environment_snapshot(self) -> dict:
        return self.data_lake.load_environment_snapshot()

    def load_installed_packages_snapshot(self) -> pd.DataFrame:
        return self.data_lake.load_installed_packages_snapshot()

    def load_dependency_inventory(self) -> pd.DataFrame:
        return self.data_lake.load_dependency_inventory()

    def load_requirements_export_report(self) -> pd.DataFrame:
        return self.data_lake.load_requirements_export_report()

    def load_install_verification_report(self) -> pd.DataFrame:
        return self.data_lake.load_install_verification_report()

    def load_import_verification_report(self) -> pd.DataFrame:
        return self.data_lake.load_import_verification_report()

    def load_script_verification_report(self) -> pd.DataFrame:
        return self.data_lake.load_script_verification_report()

    def load_config_template_verification(self) -> pd.DataFrame:
        return self.data_lake.load_config_template_verification()

    def load_bundle_artifact_inventory(self) -> pd.DataFrame:
        return self.data_lake.load_bundle_artifact_inventory()

    def load_portable_bundle_manifest(self) -> dict:
        return self.data_lake.load_portable_bundle_manifest()

    def load_archive_manifest(self) -> dict:
        return self.data_lake.load_archive_manifest()

    def load_source_policy(self, policy_name: str) -> pd.DataFrame:
        return self.data_lake.load_source_policy(policy_name)

    def load_reproducible_setup_guide(self) -> str:
        return self.data_lake.load_reproducible_setup_guide()

    def load_environment_drift_report(self) -> pd.DataFrame:
        return self.data_lake.load_environment_drift_report()

    def load_packaging_safety_report(self) -> pd.DataFrame:
        return self.data_lake.load_packaging_safety_report()

    def load_packaging_quality(self, profile_name: str = None) -> dict:
        from config.settings import settings
        p = profile_name or settings.default_portable_packaging_profile
        return self.data_lake.load_packaging_quality(p)

    def load_portable_packaging_report(self, profile_name: str = None) -> dict:
        from config.settings import settings
        p = profile_name or settings.default_portable_packaging_profile
        return self.data_lake.load_portable_packaging_report(p)

    def list_available_portable_packaging_reports(self) -> dict:
        df = self.data_lake.list_portable_packaging_reports()
        return df.to_dict(orient="records") if not df.empty else {}


    def load_project_state_inventory(self) -> pd.DataFrame:
        return self.data_lake.load_project_state_inventory()
    def load_backup_policies(self) -> pd.DataFrame:
        return self.data_lake.load_backup_policies()
    def load_backup_scope_table(self) -> pd.DataFrame:
        return self.data_lake.load_backup_scope_table()
    def load_critical_artifact_registry(self) -> pd.DataFrame:
        return self.data_lake.load_critical_artifact_registry()
    def load_noncritical_artifact_registry(self) -> pd.DataFrame:
        return self.data_lake.load_noncritical_artifact_registry()
    def load_excluded_secret_artifact_registry(self) -> pd.DataFrame:
        return self.data_lake.load_excluded_secret_artifact_registry()
    def load_backup_manifest(self) -> dict:
        return self.data_lake.load_backup_manifest()
    def load_backup_dry_run_plan(self) -> pd.DataFrame:
        return self.data_lake.load_backup_dry_run_plan()
    def load_restore_dry_run_plan(self) -> pd.DataFrame:
        return self.data_lake.load_restore_dry_run_plan()
    def load_restore_verification_report(self) -> pd.DataFrame:
        return self.data_lake.load_restore_verification_report()
    def load_disaster_recovery_manifest(self) -> dict:
        return self.data_lake.load_disaster_recovery_manifest()
    def load_recovery_runbook(self) -> str:
        return self.data_lake.load_recovery_runbook()
    def load_backup_integrity_manifest(self) -> pd.DataFrame:
        return self.data_lake.load_backup_integrity_manifest()
    def load_restore_integrity_verification(self) -> pd.DataFrame:
        return self.data_lake.load_restore_integrity_verification()
    def load_recovery_gap_report(self) -> pd.DataFrame:
        return self.data_lake.load_recovery_gap_report()
    def load_backup_safety_report(self) -> pd.DataFrame:
        return self.data_lake.load_backup_safety_report()
    def load_backup_quality(self, profile_name: str | None = None) -> dict:
        # Simplified load
        if profile_name:
            return self.data_lake.load_backup_quality(profile_name)
        return {}
    def load_backup_recovery_report(self, profile_name: str | None = None) -> dict:
        if profile_name:
            return self.data_lake.load_backup_recovery_report(profile_name)
        return {}
    def list_available_backup_recovery_reports(self) -> dict:
        return self.data_lake.list_backup_recovery_reports().to_dict('records')

    # --- Local Consistency Methods ---
    def load_consistency_check_registry(self) -> pd.DataFrame:
        return self.data_lake.load_consistency_check_registry()

    def load_cross_layer_consistency_matrix(self) -> pd.DataFrame:
        return self.data_lake.load_cross_layer_consistency_matrix()

    def load_config_env_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_config_env_consistency_report()

    def load_settings_docs_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_settings_docs_consistency_report()

    def load_paths_datalake_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_paths_datalake_consistency_report()

    def load_script_report_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_script_report_consistency_report()

    def load_report_datalake_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_report_datalake_consistency_report()

    def load_docs_phase_log_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_docs_phase_log_consistency_report()

    def load_evidence_control_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_evidence_control_consistency_report()

    def load_metadata_artifact_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_metadata_artifact_consistency_report()

    def load_graph_metadata_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_graph_metadata_consistency_report()

    def load_timeline_artifact_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_timeline_artifact_consistency_report()

    def load_backup_packaging_secrets_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_backup_packaging_secrets_consistency_report()

    def load_non_use_policy_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_non_use_policy_consistency_report()

    def load_disclaimer_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_disclaimer_consistency_report()

    def load_safety_boundary_consistency_report(self) -> pd.DataFrame:
        return self.data_lake.load_safety_boundary_consistency_report()

    def load_contradiction_detection_report(self) -> pd.DataFrame:
        return self.data_lake.load_contradiction_detection_report()

    def load_missing_reference_report(self) -> pd.DataFrame:
        return self.data_lake.load_missing_reference_report()

    def load_broken_reference_report(self) -> pd.DataFrame:
        return self.data_lake.load_broken_reference_report()

    def load_stale_artifact_reconciliation_plan(self) -> pd.DataFrame:
        return self.data_lake.load_stale_artifact_reconciliation_plan()

    def load_consistency_gap_register(self) -> pd.DataFrame:
        return self.data_lake.load_consistency_gap_register()

    def load_cross_layer_coherence_score_report(self) -> pd.DataFrame:
        return self.data_lake.load_cross_layer_coherence_score_report()

    def load_system_coherence_report(self) -> dict:
        return self.data_lake.load_system_coherence_report()

    def load_reconciliation_recommendations(self) -> pd.DataFrame:
        return self.data_lake.load_reconciliation_recommendations()

    def load_consistency_validation_report(self) -> pd.DataFrame:
        return self.data_lake.load_consistency_validation_report()

    def load_consistency_quality(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_consistency_quality(profile_name or "default")

    def load_local_consistency_report(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_local_consistency_report(profile_name or "default")

    def list_available_local_consistency_reports(self) -> dict:
        return {}


    # --- Local Maintenance ---
    def load_maintenance_domain_registry(self) -> pd.DataFrame:
        return self.data_lake.load_maintenance_domain_registry()

    def load_maintenance_task_registry(self) -> pd.DataFrame:
        return self.data_lake.load_maintenance_task_registry()

    def load_periodic_review_calendar(self) -> pd.DataFrame:
        return self.data_lake.load_periodic_review_calendar()

    def load_report_refresh_cadence_registry(self) -> pd.DataFrame:
        return self.data_lake.load_report_refresh_cadence_registry()

    def load_datalake_refresh_cadence_registry(self) -> pd.DataFrame:
        return self.data_lake.load_datalake_refresh_cadence_registry()

    def load_documentation_refresh_cadence_registry(self) -> pd.DataFrame:
        return self.data_lake.load_documentation_refresh_cadence_registry()

    def load_test_refresh_cadence_registry(self) -> pd.DataFrame:
        return self.data_lake.load_test_refresh_cadence_registry()

    def load_safety_security_refresh_cadence_registry(self) -> pd.DataFrame:
        return self.data_lake.load_safety_security_refresh_cadence_registry()

    def load_backup_packaging_refresh_cadence_registry(self) -> pd.DataFrame:
        return self.data_lake.load_backup_packaging_refresh_cadence_registry()

    def load_cross_layer_refresh_cadence_registry(self) -> pd.DataFrame:
        return self.data_lake.load_cross_layer_refresh_cadence_registry()

    def load_dependency_aging_watch_report(self) -> pd.DataFrame:
        return self.data_lake.load_dependency_aging_watch_report()

    def load_dependency_review_checklist(self) -> pd.DataFrame:
        return self.data_lake.load_dependency_review_checklist()

    def load_deprecated_artifact_watch_report(self) -> pd.DataFrame:
        return self.data_lake.load_deprecated_artifact_watch_report()

    def load_stale_report_watch_report(self) -> pd.DataFrame:
        return self.data_lake.load_stale_report_watch_report()

    def load_stale_documentation_watch_report(self) -> pd.DataFrame:
        return self.data_lake.load_stale_documentation_watch_report()

    def load_stale_test_watch_report(self) -> pd.DataFrame:
        return self.data_lake.load_stale_test_watch_report()

    def load_manual_review_queue(self) -> pd.DataFrame:
        return self.data_lake.load_manual_review_queue()

    def load_maintenance_gap_register(self) -> pd.DataFrame:
        return self.data_lake.load_maintenance_gap_register()

    def load_maintenance_risk_summary(self) -> pd.DataFrame:
        return self.data_lake.load_maintenance_risk_summary()

    def load_sustainability_score_report(self) -> pd.DataFrame:
        return self.data_lake.load_sustainability_score_report()

    def load_operator_periodic_review_checklist(self) -> pd.DataFrame:
        return self.data_lake.load_operator_periodic_review_checklist()

    def load_monthly_review_template(self) -> str:
        return self.data_lake.load_monthly_review_template()

    def load_quarterly_review_template(self) -> str:
        return self.data_lake.load_quarterly_review_template()

    def load_refresh_command_plan(self) -> pd.DataFrame:
        return self.data_lake.load_refresh_command_plan()

    def load_maintenance_runbook(self) -> str:
        return self.data_lake.load_maintenance_runbook()

    def load_long_term_sustainability_binder(self) -> str:
        return self.data_lake.load_long_term_sustainability_binder()

    def load_maintenance_validation_report(self) -> pd.DataFrame:
        return self.data_lake.load_maintenance_validation_report()

    def load_maintenance_quality(self, profile_name: str) -> dict:
        return self.data_lake.load_maintenance_quality(profile_name)
