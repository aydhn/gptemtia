import os

def update_data_lake():
    path = "data/storage/data_lake.py"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_methods = """
    # FX Provider Data Lake Methods
    def save_fx_provider_profile_registry(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/profiles", "fx_provider_profile_registry")
    def load_fx_provider_profile_registry(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/profiles", "fx_provider_profile_registry")
    def save_fx_provider_domain_registry(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/domains", "fx_provider_domain_registry")
    def load_fx_provider_domain_registry(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/domains", "fx_provider_domain_registry")
    def save_fx_pair_universe_registry(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/pairs", "fx_pair_universe_registry")
    def load_fx_pair_universe_registry(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/pairs", "fx_pair_universe_registry")
    def save_fx_currency_metadata_registry(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/currencies", "fx_currency_metadata_registry")
    def load_fx_currency_metadata_registry(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/currencies", "fx_currency_metadata_registry")
    def save_fx_symbol_normalization_map(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/symbols", "fx_symbol_normalization_map")
    def load_fx_symbol_normalization_map(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/symbols", "fx_symbol_normalization_map")
    def save_fx_quote_schema_contract(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/schemas", "fx_quote_schema_contract")
    def load_fx_quote_schema_contract(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/schemas", "fx_quote_schema_contract")
    def save_fx_ohlcv_schema_contract(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/schemas", "fx_ohlcv_schema_contract")
    def load_fx_ohlcv_schema_contract(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/schemas", "fx_ohlcv_schema_contract")
    def save_fx_cross_rate_requirement_registry(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/cross_rates", "fx_cross_rate_requirement_registry")
    def load_fx_cross_rate_requirement_registry(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/cross_rates", "fx_cross_rate_requirement_registry")
    def save_fx_provider_capability_registry(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/capabilities", "fx_provider_capability_registry")
    def load_fx_provider_capability_registry(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/capabilities", "fx_provider_capability_registry")
    def save_fx_provider_metadata_registry(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/metadata", "fx_provider_metadata_registry")
    def load_fx_provider_metadata_registry(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/metadata", "fx_provider_metadata_registry")
    def save_fx_provider_request_schema(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/request_response", "fx_provider_request_schema")
    def load_fx_provider_request_schema(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/request_response", "fx_provider_request_schema")
    def save_fx_provider_response_schema(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/request_response", "fx_provider_response_schema")
    def load_fx_provider_response_schema(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/request_response", "fx_provider_response_schema")
    def save_fx_provider_error_schema(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/request_response", "fx_provider_error_schema")
    def load_fx_provider_error_schema(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/request_response", "fx_provider_error_schema")
    def save_fx_provider_interface_contract(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/contracts", "fx_provider_interface_contract")
    def load_fx_provider_interface_contract(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/contracts", "fx_provider_interface_contract")
    def save_fx_adapter_contract(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/contracts", "fx_adapter_contract")
    def load_fx_adapter_contract(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/contracts", "fx_adapter_contract")
    def save_fx_provider_registry(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/registry", "fx_provider_registry")
    def load_fx_provider_registry(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/registry", "fx_provider_registry")
    def save_fx_provider_resolver_map(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/resolver", "fx_provider_resolver_map")
    def load_fx_provider_resolver_map(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/resolver", "fx_provider_resolver_map")
    def save_fx_provider_preference_resolver_report(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/preferences", "fx_provider_preference_resolver_report")
    def load_fx_provider_preference_resolver_report(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/preferences", "fx_provider_preference_resolver_report")
    def save_fx_provider_capability_matcher_report(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/matcher", "fx_provider_capability_matcher_report")
    def load_fx_provider_capability_matcher_report(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/matcher", "fx_provider_capability_matcher_report")
    def save_fx_dry_run_fixture_report(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/dry_run", "fx_dry_run_fixture_report")
    def load_fx_dry_run_fixture_report(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/dry_run", "fx_dry_run_fixture_report")
    def save_fx_manual_file_provider_placeholder(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/placeholders", "fx_manual_file_provider_placeholder")
    def load_fx_manual_file_provider_placeholder(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/placeholders", "fx_manual_file_provider_placeholder")
    def save_fx_local_cache_provider_placeholder(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/placeholders", "fx_local_cache_provider_placeholder")
    def load_fx_local_cache_provider_placeholder(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/placeholders", "fx_local_cache_provider_placeholder")
    def save_fx_official_api_provider_placeholder(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/placeholders", "fx_official_api_provider_placeholder")
    def load_fx_official_api_provider_placeholder(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/placeholders", "fx_official_api_provider_placeholder")
    def save_fx_licensed_provider_placeholder(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/placeholders", "fx_licensed_provider_placeholder")
    def load_fx_licensed_provider_placeholder(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/placeholders", "fx_licensed_provider_placeholder")
    def save_fx_output_validation_contract(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/output_validation", "fx_output_validation_contract")
    def load_fx_output_validation_contract(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/output_validation", "fx_output_validation_contract")
    def save_fx_safety_boundary(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/safety", "fx_safety_boundary")
    def load_fx_safety_boundary(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/safety", "fx_safety_boundary")
    def save_fx_health_check(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/health", "fx_health_check")
    def load_fx_health_check(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/health", "fx_health_check")
    def save_fx_readiness_score_report(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/scoring", "fx_readiness_score_report")
    def load_fx_readiness_score_report(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/scoring", "fx_readiness_score_report")
    def save_fx_validation_report(self, df: pd.DataFrame, summary: dict = None) -> Path: return self._save_df(df, "advanced_fx_providers/validation", "fx_validation_report")
    def load_fx_validation_report(self) -> pd.DataFrame: return self._load_df("advanced_fx_providers/validation", "fx_validation_report")
    def save_fx_quality_report(self, profile_name: str, quality: dict) -> Path: return self._save_dict(quality, f"advanced_fx_providers/quality", f"{profile_name}_quality")
    def load_fx_quality_report(self, profile_name: str) -> dict: return self._load_dict(f"advanced_fx_providers/quality", f"{profile_name}_quality")
    def save_fx_provider_report(self, profile_name: str, report: dict, markdown: str = None) -> Path: 
        if markdown:
            with open(self.base_path / "reports/output/advanced_fx_providers" / f"{profile_name}_report.md", "w", encoding="utf-8") as f:
                f.write(markdown)
        return self._save_dict(report, "advanced_fx_providers/reports", f"{profile_name}_report")
    def load_fx_provider_report(self, profile_name: str) -> dict: return self._load_dict("advanced_fx_providers/reports", f"{profile_name}_report")
    def list_fx_provider_reports(self) -> pd.DataFrame: return pd.DataFrame()
"""

    if "save_fx_provider_profile_registry" not in content:
        # insert at the end of the class
        idx = content.rfind("def ")
        # just append if class is at root
        if "class DataLake" in content:
            content += "\n" + new_methods
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

update_data_lake()

def update_feature_store():
    path = "ml/feature_store.py"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_methods = """
    # FX Provider Feature Store Methods
    def load_fx_provider_profile_registry(self) -> pd.DataFrame: return self.data_lake.load_fx_provider_profile_registry()
    def load_fx_provider_domain_registry(self) -> pd.DataFrame: return self.data_lake.load_fx_provider_domain_registry()
    def load_fx_pair_universe_registry(self) -> pd.DataFrame: return self.data_lake.load_fx_pair_universe_registry()
    def load_fx_currency_metadata_registry(self) -> pd.DataFrame: return self.data_lake.load_fx_currency_metadata_registry()
    def load_fx_symbol_normalization_map(self) -> pd.DataFrame: return self.data_lake.load_fx_symbol_normalization_map()
    def load_fx_quote_schema_contract(self) -> pd.DataFrame: return self.data_lake.load_fx_quote_schema_contract()
    def load_fx_ohlcv_schema_contract(self) -> pd.DataFrame: return self.data_lake.load_fx_ohlcv_schema_contract()
    def load_fx_cross_rate_requirement_registry(self) -> pd.DataFrame: return self.data_lake.load_fx_cross_rate_requirement_registry()
    def load_fx_provider_capability_registry(self) -> pd.DataFrame: return self.data_lake.load_fx_provider_capability_registry()
    def load_fx_provider_metadata_registry(self) -> pd.DataFrame: return self.data_lake.load_fx_provider_metadata_registry()
    def load_fx_provider_request_schema(self) -> pd.DataFrame: return self.data_lake.load_fx_provider_request_schema()
    def load_fx_provider_response_schema(self) -> pd.DataFrame: return self.data_lake.load_fx_provider_response_schema()
    def load_fx_provider_error_schema(self) -> pd.DataFrame: return self.data_lake.load_fx_provider_error_schema()
    def load_fx_provider_interface_contract(self) -> pd.DataFrame: return self.data_lake.load_fx_provider_interface_contract()
    def load_fx_adapter_contract(self) -> pd.DataFrame: return self.data_lake.load_fx_adapter_contract()
    def load_fx_provider_registry(self) -> pd.DataFrame: return self.data_lake.load_fx_provider_registry()
    def load_fx_provider_resolver_map(self) -> pd.DataFrame: return self.data_lake.load_fx_provider_resolver_map()
    def load_fx_provider_preference_resolver_report(self) -> pd.DataFrame: return self.data_lake.load_fx_provider_preference_resolver_report()
    def load_fx_provider_capability_matcher_report(self) -> pd.DataFrame: return self.data_lake.load_fx_provider_capability_matcher_report()
    def load_fx_dry_run_fixture_report(self) -> pd.DataFrame: return self.data_lake.load_fx_dry_run_fixture_report()
    def load_fx_manual_file_provider_placeholder(self) -> pd.DataFrame: return self.data_lake.load_fx_manual_file_provider_placeholder()
    def load_fx_local_cache_provider_placeholder(self) -> pd.DataFrame: return self.data_lake.load_fx_local_cache_provider_placeholder()
    def load_fx_official_api_provider_placeholder(self) -> pd.DataFrame: return self.data_lake.load_fx_official_api_provider_placeholder()
    def load_fx_licensed_provider_placeholder(self) -> pd.DataFrame: return self.data_lake.load_fx_licensed_provider_placeholder()
    def load_fx_output_validation_contract(self) -> pd.DataFrame: return self.data_lake.load_fx_output_validation_contract()
    def load_fx_safety_boundary(self) -> pd.DataFrame: return self.data_lake.load_fx_safety_boundary()
    def load_fx_health_check(self) -> pd.DataFrame: return self.data_lake.load_fx_health_check()
    def load_fx_readiness_score_report(self) -> pd.DataFrame: return self.data_lake.load_fx_readiness_score_report()
    def load_fx_quality_report(self, profile_name: str = None) -> dict: return self.data_lake.load_fx_quality_report(profile_name or "default")
    def list_available_fx_provider_reports(self) -> dict: return {}
"""

    if "load_fx_provider_profile_registry" not in content:
        if "class FeatureStore" in content:
            content += "\n" + new_methods
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

update_feature_store()

def update_report_builder():
    path = "reports/report_builder.py"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_methods = """
    # FX Provider Report Builder Methods
    def _fx_disclaimer(self) -> str:
        return "Bu rapor Phase 107 FX Data Provider Layer çıktısıdır. Gerçek FX veri indirme zorunluluğu, scraping, broker talimatı, canlı emir, kesin AL/SAT, yatırım tavsiyesi, production deployment veya official approval değildir."

    def build_fx_provider_text_report(self, summary: dict, registry_df: pd.DataFrame = None) -> str: return f"FX Provider Report\\n\\n{self._fx_disclaimer()}"
    def build_fx_pair_universe_text_report(self, summary: dict, pair_df: pd.DataFrame = None) -> str: return f"FX Pair Universe Report\\n\\n{self._fx_disclaimer()}"
    def build_fx_symbol_normalization_text_report(self, summary: dict, symbol_df: pd.DataFrame = None) -> str: return f"FX Symbol Normalization Report\\n\\n{self._fx_disclaimer()}"
    def build_fx_provider_capability_text_report(self, summary: dict, capability_df: pd.DataFrame = None) -> str: return f"FX Capabilities Report\\n\\n{self._fx_disclaimer()}"
    def build_fx_contract_text_report(self, summary: dict, contract_df: pd.DataFrame = None) -> str: return f"FX Contract Report\\n\\n{self._fx_disclaimer()}"
    def build_fx_safety_text_report(self, summary: dict, safety_df: pd.DataFrame = None) -> str: return f"FX Safety Report\\n\\n{self._fx_disclaimer()}"
    def build_fx_health_text_report(self, summary: dict, health_df: pd.DataFrame = None) -> str: return f"FX Health Report\\n\\n{self._fx_disclaimer()}"
    def build_fx_quality_text_report(self, summary: dict, quality: dict = None) -> str: return f"FX Quality Report\\n\\n{self._fx_disclaimer()}"
"""

    if "build_fx_provider_text_report" not in content:
        if "class ReportBuilder" in content:
            content += "\n" + new_methods
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

update_report_builder()
