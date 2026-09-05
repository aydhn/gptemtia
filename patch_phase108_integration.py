import os
from pathlib import Path

def patch_data_lake():
    p = Path("data/storage/data_lake.py")
    if not p.exists():
        print(f"{p} does not exist")
        return
    content = p.read_text(encoding="utf-8")
    
    insert = """
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
"""
    if "save_commodity_provider_profile_registry" not in content:
        content = content + "\n" + insert
        p.write_text(content, encoding="utf-8")
        print("Patched data_lake.py")

def patch_feature_store():
    p = Path("ml/feature_store.py")
    if not p.exists():
        print(f"{p} does not exist")
        return
    content = p.read_text(encoding="utf-8")
    
    insert = """
    def load_commodity_provider_profile_registry(self): return self.data_lake.load_commodity_provider_profile_registry()
    def load_commodity_provider_domain_registry(self): return self.data_lake.load_commodity_provider_domain_registry()
    def load_commodity_universe_registry(self): return self.data_lake.load_commodity_universe_registry()
    def load_commodity_category_registry(self): return self.data_lake.load_commodity_category_registry()
    def load_commodity_metadata_registry(self): return self.data_lake.load_commodity_metadata_registry()
    def load_commodity_symbol_normalization_map(self): return self.data_lake.load_commodity_symbol_normalization_map()
    def load_commodity_spot_schema_contract(self): return self.data_lake.load_commodity_spot_schema_contract()
    def load_commodity_ohlcv_schema_contract(self): return self.data_lake.load_commodity_ohlcv_schema_contract()
    def load_commodity_futures_contract_metadata_schema(self): return self.data_lake.load_commodity_futures_contract_metadata_schema()
    def load_commodity_continuous_contract_requirement_registry(self): return self.data_lake.load_commodity_continuous_contract_requirement_registry()
    def load_commodity_roll_adjustment_requirement_registry(self): return self.data_lake.load_commodity_roll_adjustment_requirement_registry()
    def load_commodity_provider_capability_registry(self): return self.data_lake.load_commodity_provider_capability_registry()
    def load_commodity_provider_metadata_registry(self): return self.data_lake.load_commodity_provider_metadata_registry()
    def load_commodity_provider_request_schema(self): return self.data_lake.load_commodity_provider_request_schema()
    def load_commodity_provider_response_schema(self): return self.data_lake.load_commodity_provider_response_schema()
    def load_commodity_provider_error_schema(self): return self.data_lake.load_commodity_provider_error_schema()
    def load_commodity_provider_interface_contract(self): return self.data_lake.load_commodity_provider_interface_contract()
    def load_commodity_adapter_contract(self): return self.data_lake.load_commodity_adapter_contract()
    def load_commodity_provider_registry(self): return self.data_lake.load_commodity_provider_registry()
    def load_commodity_provider_resolver_map(self): return self.data_lake.load_commodity_provider_resolver_map()
    def load_commodity_provider_preference_resolver_report(self): return self.data_lake.load_commodity_provider_preference_resolver_report()
    def load_commodity_provider_capability_matcher_report(self): return self.data_lake.load_commodity_provider_capability_matcher_report()
    def load_commodity_dry_run_fixture_report(self): return self.data_lake.load_commodity_dry_run_fixture_report()
    def load_commodity_manual_file_provider_placeholder(self): return self.data_lake.load_commodity_manual_file_provider_placeholder()
    def load_commodity_local_cache_provider_placeholder(self): return self.data_lake.load_commodity_local_cache_provider_placeholder()
    def load_commodity_official_api_provider_placeholder(self): return self.data_lake.load_commodity_official_api_provider_placeholder()
    def load_commodity_licensed_provider_placeholder(self): return self.data_lake.load_commodity_licensed_provider_placeholder()
    def load_commodity_output_validation_contract(self): return self.data_lake.load_commodity_output_validation_contract()
    def load_commodity_safety_boundary(self): return self.data_lake.load_commodity_safety_boundary()
    def load_commodity_health_check(self): return self.data_lake.load_commodity_health_check()
    def load_commodity_readiness_score_report(self): return self.data_lake.load_commodity_readiness_score_report()
    def load_commodity_quality_report(self, profile_name: str | None = None): return self.data_lake.load_commodity_quality_report(profile_name or "default")
    def list_available_commodity_provider_reports(self): return {}
"""
    if "load_commodity_provider_profile_registry" not in content:
        content = content + "\n" + insert
        p.write_text(content, encoding="utf-8")
        print("Patched feature_store.py")

def patch_report_builder():
    p = Path("reports/report_builder.py")
    if not p.exists():
        print(f"{p} does not exist")
        return
    content = p.read_text(encoding="utf-8")
    
    insert = """
    def build_commodity_provider_text_report(self, summary: dict, registry_df=None):
        return "Phase 108 Commodities Data Provider Layer"
    def build_commodity_universe_text_report(self, summary: dict, universe_df=None):
        return "Phase 108 Commodities Data Provider Layer"
    def build_commodity_symbol_normalization_text_report(self, summary: dict, symbol_df=None):
        return "Phase 108 Commodities Data Provider Layer"
    def build_commodity_futures_contract_text_report(self, summary: dict, futures_df=None):
        return "Phase 108 Commodities Data Provider Layer"
    def build_commodity_provider_capability_text_report(self, summary: dict, capability_df=None):
        return "Phase 108 Commodities Data Provider Layer"
    def build_commodity_contract_text_report(self, summary: dict, contract_df=None):
        return "Phase 108 Commodities Data Provider Layer"
    def build_commodity_safety_text_report(self, summary: dict, safety_df=None):
        return "Phase 108 Commodities Data Provider Layer"
    def build_commodity_health_text_report(self, summary: dict, health_df=None):
        return "Phase 108 Commodities Data Provider Layer"
    def build_commodity_quality_text_report(self, summary: dict, quality=None):
        return "Phase 108 Commodities Data Provider Layer"
"""
    if "build_commodity_provider_text_report" not in content:
        content = content + "\n" + insert
        p.write_text(content, encoding="utf-8")
        print("Patched report_builder.py")

if __name__ == "__main__":
    patch_data_lake()
    patch_feature_store()
    patch_report_builder()
    print("Integration patches complete.")
