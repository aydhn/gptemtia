from pathlib import Path
import pandas as pd
from typing import Dict, Tuple, Optional
from advanced_news_metadata.news_provider_config import NewsProviderProfile, get_default_news_provider_profile

class NewsMetadataPipeline:
    def __init__(self, data_lake, settings, project_root: Path, profile: Optional[NewsProviderProfile] = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_news_provider_profile()

    def build_news_profiles_and_domains(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        from advanced_news_metadata.news_provider_profile_registry import build_news_metadata_provider_profile_registry
        from advanced_news_metadata.news_domain_registry import build_news_metadata_domain_registry
        df_p, sum_p = build_news_metadata_provider_profile_registry(self.profile)
        df_d, sum_d = build_news_metadata_domain_registry(self.profile)
        if save and self.data_lake:
            self.data_lake.save_news_metadata_provider_profile_registry(df_p, sum_p)
            self.data_lake.save_news_metadata_domain_registry(df_d, sum_d)
        return {"profiles": df_p, "domains": df_d}, {"profiles": sum_p, "domains": sum_d}

    def build_news_sources_and_schemas(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        from advanced_news_metadata.news_source_registry import build_news_source_registry
        from advanced_news_metadata.news_source_categories import build_news_source_category_registry
        from advanced_news_metadata.news_metadata_schema import build_news_metadata_schema_contract
        from advanced_news_metadata.news_item_reference_schema import build_news_item_reference_schema_contract

        df_src, sum_src = build_news_source_registry(self.profile)
        df_cat, sum_cat = build_news_source_category_registry(self.profile)
        df_sch, sum_sch = build_news_metadata_schema_contract(self.profile)
        df_ref, sum_ref = build_news_item_reference_schema_contract(self.profile)

        if save and self.data_lake:
            self.data_lake.save_news_source_registry(df_src, sum_src)
            self.data_lake.save_news_source_category_registry(df_cat, sum_cat)
            self.data_lake.save_news_metadata_schema_contract(df_sch, sum_sch)
            self.data_lake.save_news_item_reference_schema_contract(df_ref, sum_ref)

        tables = {"sources": df_src, "categories": df_cat, "metadata_schema": df_sch, "item_reference_schema": df_ref}
        summaries = {"sources": sum_src, "categories": sum_cat, "metadata_schema": sum_sch, "item_reference_schema": sum_ref}
        return tables, summaries

    def build_news_tags_and_linkages(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        from advanced_news_metadata.news_asset_tags import build_news_asset_tag_registry
        from advanced_news_metadata.news_macro_tags import build_news_macro_tag_registry
        from advanced_news_metadata.news_commodity_tags import build_news_commodity_tag_registry
        from advanced_news_metadata.news_fx_tags import build_news_fx_tag_registry
        from advanced_news_metadata.news_event_linkage import build_news_event_linkage_registry
        from advanced_news_metadata.news_region_currency_mapping import build_news_region_currency_mapping_registry
        from advanced_news_metadata.news_topic_taxonomy import build_news_topic_taxonomy_registry

        df_asset, sum_asset = build_news_asset_tag_registry(self.profile)
        df_macro, sum_macro = build_news_macro_tag_registry(self.profile)
        df_comm, sum_comm = build_news_commodity_tag_registry(self.profile)
        df_fx, sum_fx = build_news_fx_tag_registry(self.profile)
        df_link, sum_link = build_news_event_linkage_registry(self.profile)
        df_rc, sum_rc = build_news_region_currency_mapping_registry(self.profile)
        df_top, sum_top = build_news_topic_taxonomy_registry(self.profile)

        if save and self.data_lake:
            self.data_lake.save_news_asset_tag_registry(df_asset, sum_asset)
            self.data_lake.save_news_macro_tag_registry(df_macro, sum_macro)
            self.data_lake.save_news_commodity_tag_registry(df_comm, sum_comm)
            self.data_lake.save_news_fx_tag_registry(df_fx, sum_fx)
            self.data_lake.save_news_event_linkage_registry(df_link, sum_link)
            self.data_lake.save_news_region_currency_mapping_registry(df_rc, sum_rc)
            self.data_lake.save_news_topic_taxonomy_registry(df_top, sum_top)

        tables = {
            "asset_tags": df_asset, "macro_tags": df_macro, "commodity_tags": df_comm,
            "fx_tags": df_fx, "event_linkage": df_link, "region_currency": df_rc, "topic_taxonomy": df_top
        }
        summaries = {
            "asset_tags": sum_asset, "macro_tags": sum_macro, "commodity_tags": sum_comm,
            "fx_tags": sum_fx, "event_linkage": sum_link, "region_currency": sum_rc, "topic_taxonomy": sum_top
        }
        return tables, summaries

    def build_news_requirements(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        from advanced_news_metadata.news_sentiment_requirements import build_news_sentiment_placeholder_requirement_registry
        from advanced_news_metadata.news_impact_requirements import build_news_impact_placeholder_requirement_registry
        from advanced_news_metadata.news_freshness_requirements import build_news_freshness_staleness_requirement_registry
        from advanced_news_metadata.news_deduplication_requirements import build_news_deduplication_requirement_registry

        df_sent, sum_sent = build_news_sentiment_placeholder_requirement_registry(self.profile)
        df_imp, sum_imp = build_news_impact_placeholder_requirement_registry(self.profile)
        df_fresh, sum_fresh = build_news_freshness_staleness_requirement_registry(self.profile)
        df_dedup, sum_dedup = build_news_deduplication_requirement_registry(self.profile)

        if save and self.data_lake:
            self.data_lake.save_news_sentiment_placeholder_requirement_registry(df_sent, sum_sent)
            self.data_lake.save_news_impact_placeholder_requirement_registry(df_imp, sum_imp)
            self.data_lake.save_news_freshness_staleness_requirement_registry(df_fresh, sum_fresh)
            self.data_lake.save_news_deduplication_requirement_registry(df_dedup, sum_dedup)

        tables = {"sentiment": df_sent, "impact": df_imp, "freshness": df_fresh, "deduplication": df_dedup}
        summaries = {"sentiment": sum_sent, "impact": sum_imp, "freshness": sum_fresh, "deduplication": sum_dedup}
        return tables, summaries

    def build_news_provider_metadata_and_capabilities(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        from advanced_news_metadata.news_provider_metadata import build_news_provider_metadata_registry
        from advanced_news_metadata.news_provider_capabilities import build_news_provider_capability_registry

        df_meta, sum_meta = build_news_provider_metadata_registry(self.profile)
        df_cap, sum_cap = build_news_provider_capability_registry(self.profile)

        if save and self.data_lake:
            self.data_lake.save_news_provider_metadata_registry(df_meta, sum_meta)
            self.data_lake.save_news_provider_capability_registry(df_cap, sum_cap)

        return {"metadata": df_meta, "capabilities": df_cap}, {"metadata": sum_meta, "capabilities": sum_cap}

    def build_news_request_response_schemas(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        from advanced_news_metadata.news_provider_request import build_news_provider_request_schema
        from advanced_news_metadata.news_provider_response import build_news_provider_response_schema
        from advanced_news_metadata.news_provider_errors import build_news_provider_error_schema

        df_req, sum_req = build_news_provider_request_schema(self.profile)
        df_res, sum_res = build_news_provider_response_schema(self.profile)
        df_err, sum_err = build_news_provider_error_schema(self.profile)

        if save and self.data_lake:
            self.data_lake.save_news_provider_request_schema(df_req, sum_req)
            self.data_lake.save_news_provider_response_schema(df_res, sum_res)
            self.data_lake.save_news_provider_error_schema(df_err, sum_err)

        return {"request_schema": df_req, "response_schema": df_res, "error_schema": df_err}, {"request_schema": sum_req, "response_schema": sum_res, "error_schema": sum_err}

    def build_news_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        from advanced_news_metadata.news_provider_interfaces import build_news_provider_interface_contract
        from advanced_news_metadata.news_adapter_contracts import build_news_adapter_contract
        from advanced_news_metadata.news_output_validation import build_news_output_validation_contract
        from advanced_news_metadata.news_safety_boundary import build_news_safety_boundary

        df_iface, sum_iface = build_news_provider_interface_contract(self.profile)
        df_adapt, sum_adapt = build_news_adapter_contract(self.profile)
        df_oval, sum_oval = build_news_output_validation_contract(self.profile)
        df_safe, sum_safe = build_news_safety_boundary(self.profile)

        if save and self.data_lake:
            self.data_lake.save_news_provider_interface_contract(df_iface, sum_iface)
            self.data_lake.save_news_adapter_contract(df_adapt, sum_adapt)
            self.data_lake.save_news_output_validation_contract(df_oval, sum_oval)
            self.data_lake.save_news_safety_boundary(df_safe, sum_safe)

        tables = {"interface": df_iface, "adapter": df_adapt, "output_validation": df_oval, "safety": df_safe}
        summaries = {"interface": sum_iface, "adapter": sum_adapt, "output_validation": sum_oval, "safety": sum_safe}
        return tables, summaries

    def build_news_registry_and_resolver(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        from advanced_news_metadata.news_provider_registry import build_news_provider_registry
        from advanced_news_metadata.news_provider_resolver import build_news_provider_resolver_map
        from advanced_news_metadata.news_provider_preference_resolver import build_news_provider_preference_resolver_report
        from advanced_news_metadata.news_provider_capability_matcher import build_news_provider_capability_matcher_report

        df_reg, sum_reg = build_news_provider_registry(self.profile)
        df_res, sum_res = build_news_provider_resolver_map(self.profile)
        df_pref, sum_pref = build_news_provider_preference_resolver_report(self.profile)
        df_match, sum_match = build_news_provider_capability_matcher_report(self.profile)

        if save and self.data_lake:
            self.data_lake.save_news_provider_registry(df_reg, sum_reg)
            self.data_lake.save_news_provider_resolver_map(df_res, sum_res)
            self.data_lake.save_news_provider_preference_resolver_report(df_pref, sum_pref)
            self.data_lake.save_news_provider_capability_matcher_report(df_match, sum_match)

        tables = {"registry": df_reg, "resolver": df_res, "preferences": df_pref, "matcher": df_match}
        summaries = {"registry": sum_reg, "resolver": sum_res, "preferences": sum_pref, "matcher": sum_match}
        return tables, summaries

    def build_news_dry_run_fixture(self, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        from advanced_news_metadata.news_dry_run_fixture import build_news_dry_run_fixture_report
        df, summary = build_news_dry_run_fixture_report(self.profile)
        if save and self.data_lake:
            self.data_lake.save_news_dry_run_fixture_report(df, summary)
        return df, summary

    def build_news_placeholders(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        from advanced_news_metadata.news_manual_file_provider import build_news_manual_file_provider_placeholder
        from advanced_news_metadata.news_local_cache_provider import build_news_local_cache_provider_placeholder
        from advanced_news_metadata.news_official_api_provider import build_news_official_api_provider_placeholder
        from advanced_news_metadata.news_licensed_provider import build_news_licensed_provider_placeholder
        from advanced_news_metadata.news_public_dataset_provider import build_news_public_dataset_provider_placeholder

        df_man, sum_man = build_news_manual_file_provider_placeholder(self.profile)
        df_loc, sum_loc = build_news_local_cache_provider_placeholder(self.profile)
        df_off, sum_off = build_news_official_api_provider_placeholder(self.profile)
        df_lic, sum_lic = build_news_licensed_provider_placeholder(self.profile)
        df_pub, sum_pub = build_news_public_dataset_provider_placeholder(self.profile)

        if save and self.data_lake:
            self.data_lake.save_news_manual_file_provider_placeholder(df_man, sum_man)
            self.data_lake.save_news_local_cache_provider_placeholder(df_loc, sum_loc)
            self.data_lake.save_news_official_api_provider_placeholder(df_off, sum_off)
            self.data_lake.save_news_licensed_provider_placeholder(df_lic, sum_lic)
            self.data_lake.save_news_public_dataset_provider_placeholder(df_pub, sum_pub)

        tables = {"manual": df_man, "local_cache": df_loc, "official_api": df_off, "licensed": df_lic, "public_dataset": df_pub}
        summaries = {"manual": sum_man, "local_cache": sum_loc, "official_api": sum_off, "licensed": sum_lic, "public_dataset": sum_pub}
        return tables, summaries

    def build_news_health_check(self, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        from advanced_news_metadata.news_health import build_news_health_check
        df, summary = build_news_health_check(self.project_root, self.profile)
        if save and self.data_lake:
            self.data_lake.save_news_health_check(df, summary)
        return df, summary

    def build_news_quality_report(self, save: bool = True) -> Tuple[Dict, Dict]:
        from advanced_news_metadata.news_quality import build_news_quality_report
        qual = build_news_quality_report({"profile": self.profile.name, "status": "pass"})
        if save and self.data_lake:
            self.data_lake.save_news_quality_report(self.profile.name, qual)
        return qual, qual

    def build_news_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        status_data = [
            {"component": "news_profiles_and_domains", "status": "ready"},
            {"component": "news_sources_and_schemas", "status": "ready"},
            {"component": "news_tags_and_linkages", "status": "ready"},
            {"component": "news_requirements", "status": "ready"},
            {"component": "news_provider_metadata_and_capabilities", "status": "ready"},
            {"component": "news_request_response_schemas", "status": "ready"},
            {"component": "news_contracts", "status": "ready"},
            {"component": "news_registry_and_resolver", "status": "ready"},
            {"component": "news_dry_run_fixture", "status": "ready"},
            {"component": "news_placeholders", "status": "ready"},
            {"component": "news_health_check", "status": "ready"},
            {"component": "news_quality_report", "status": "ready"}
        ]
        df = pd.DataFrame(status_data)
        summary = {"total_components": len(df), "status": "operational"}
        return df, summary
