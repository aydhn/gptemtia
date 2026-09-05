import pandas as pd
from pathlib import Path
from typing import Tuple, Dict, Optional
from config.settings import Settings
from data.storage.data_lake import DataLake
from .fx_provider_config import FXProviderProfile, get_default_fx_provider_profile

from .fx_provider_profile_registry import build_fx_provider_profile_registry
from .fx_provider_domain_registry import build_fx_provider_domain_registry
from .fx_pair_universe import build_fx_pair_universe_registry
from .fx_currency_metadata import build_fx_currency_metadata_registry
from .fx_symbol_normalization import build_fx_symbol_normalization_map
from .fx_quote_schema import build_fx_quote_schema_contract
from .fx_ohlcv_schema import build_fx_ohlcv_schema_contract
from .fx_cross_rate_requirements import build_fx_cross_rate_requirement_registry
from .fx_provider_capabilities import build_fx_provider_capability_registry
from .fx_provider_metadata import build_fx_provider_metadata_registry
from .fx_provider_request import build_fx_provider_request_schema
from .fx_provider_response import build_fx_provider_response_schema
from .fx_provider_errors import build_fx_provider_error_schema
from .fx_provider_interfaces import build_fx_provider_interface_contract
from .fx_adapter_contracts import build_fx_adapter_contract
from .fx_provider_registry import build_fx_provider_registry
from .fx_provider_resolver import build_fx_provider_resolver_map
from .fx_provider_preference_resolver import build_fx_provider_preference_resolver_report
from .fx_provider_capability_matcher import build_fx_provider_capability_matcher_report
from .fx_dry_run_fixture import build_fx_dry_run_fixture_report
from .fx_manual_file_provider import build_fx_manual_file_provider_placeholder
from .fx_local_cache_provider import build_fx_local_cache_provider_placeholder
from .fx_official_api_provider import build_fx_official_api_provider_placeholder
from .fx_licensed_provider import build_fx_licensed_provider_placeholder
from .fx_output_validation import build_fx_output_validation_contract
from .fx_safety_boundary import build_fx_safety_boundary
from .fx_health import build_fx_health_check
from .fx_scoring import build_fx_readiness_score_report
from .fx_validation import build_fx_validation_report
from .fx_quality import build_fx_quality_report

class FXProviderPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[FXProviderProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_fx_provider_profile()

    def build_fx_profiles_and_domains(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        prof_df, prof_sum = build_fx_provider_profile_registry(self.profile)
        dom_df, dom_sum = build_fx_provider_domain_registry(self.profile)
        if save:
            self.data_lake.save_fx_provider_profile_registry(prof_df, prof_sum)
            self.data_lake.save_fx_provider_domain_registry(dom_df, dom_sum)
        return {"profiles": prof_df, "domains": dom_df}, {"profiles": prof_sum, "domains": dom_sum}

    def build_fx_universe_and_symbols(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        pair_df, pair_sum = build_fx_pair_universe_registry(self.profile)
        curr_df, curr_sum = build_fx_currency_metadata_registry(self.profile)
        sym_df, sym_sum = build_fx_symbol_normalization_map(self.profile)
        if save:
            self.data_lake.save_fx_pair_universe_registry(pair_df, pair_sum)
            self.data_lake.save_fx_currency_metadata_registry(curr_df, curr_sum)
            self.data_lake.save_fx_symbol_normalization_map(sym_df, sym_sum)
        return {"pairs": pair_df, "currencies": curr_df, "symbols": sym_df}, {"pairs": pair_sum, "currencies": curr_sum, "symbols": sym_sum}

    def build_fx_schemas_and_cross_rates(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        q_df, q_sum = build_fx_quote_schema_contract(self.profile)
        o_df, o_sum = build_fx_ohlcv_schema_contract(self.profile)
        c_df, c_sum = build_fx_cross_rate_requirement_registry(self.profile)
        if save:
            self.data_lake.save_fx_quote_schema_contract(q_df, q_sum)
            self.data_lake.save_fx_ohlcv_schema_contract(o_df, o_sum)
            self.data_lake.save_fx_cross_rate_requirement_registry(c_df, c_sum)
        return {"quotes": q_df, "ohlcv": o_df, "cross_rates": c_df}, {"quotes": q_sum, "ohlcv": o_sum, "cross_rates": c_sum}

    def build_fx_metadata_and_capabilities(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        m_df, m_sum = build_fx_provider_metadata_registry(self.profile)
        c_df, c_sum = build_fx_provider_capability_registry(self.profile)
        if save:
            self.data_lake.save_fx_provider_metadata_registry(m_df, m_sum)
            self.data_lake.save_fx_provider_capability_registry(c_df, c_sum)
        return {"metadata": m_df, "capabilities": c_df}, {"metadata": m_sum, "capabilities": c_sum}

    def build_fx_request_response_schemas(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        req_df, req_sum = build_fx_provider_request_schema(self.profile)
        resp_df, resp_sum = build_fx_provider_response_schema(self.profile)
        err_df, err_sum = build_fx_provider_error_schema(self.profile)
        if save:
            self.data_lake.save_fx_provider_request_schema(req_df, req_sum)
            self.data_lake.save_fx_provider_response_schema(resp_df, resp_sum)
            self.data_lake.save_fx_provider_error_schema(err_df, err_sum)
        return {"req": req_df, "resp": resp_df, "err": err_df}, {"req": req_sum, "resp": resp_sum, "err": err_sum}

    def build_fx_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        i_df, i_sum = build_fx_provider_interface_contract(self.profile)
        a_df, a_sum = build_fx_adapter_contract(self.profile)
        v_df, v_sum = build_fx_output_validation_contract(self.profile)
        s_df, s_sum = build_fx_safety_boundary(self.profile)
        if save:
            self.data_lake.save_fx_provider_interface_contract(i_df, i_sum)
            self.data_lake.save_fx_adapter_contract(a_df, a_sum)
            self.data_lake.save_fx_output_validation_contract(v_df, v_sum)
            self.data_lake.save_fx_safety_boundary(s_df, s_sum)
        return {"interface": i_df, "adapter": a_df, "validation": v_df, "safety": s_df}, {"interface": i_sum, "adapter": a_sum, "validation": v_sum, "safety": s_sum}

    def build_fx_registry_and_resolver(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        reg_df, reg_sum = build_fx_provider_registry(self.profile)
        res_df, res_sum = build_fx_provider_resolver_map(self.profile)
        pref_df, pref_sum = build_fx_provider_preference_resolver_report(self.profile)
        match_df, match_sum = build_fx_provider_capability_matcher_report(self.profile)
        if save:
            self.data_lake.save_fx_provider_registry(reg_df, reg_sum)
            self.data_lake.save_fx_provider_resolver_map(res_df, res_sum)
            self.data_lake.save_fx_provider_preference_resolver_report(pref_df, pref_sum)
            self.data_lake.save_fx_provider_capability_matcher_report(match_df, match_sum)
        return {"registry": reg_df, "resolver": res_df, "pref": pref_df, "match": match_df}, {"registry": reg_sum, "resolver": res_sum, "pref": pref_sum, "match": match_sum}

    def build_fx_dry_run_fixture(self, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        df, sum_d = build_fx_dry_run_fixture_report(self.profile)
        if save: self.data_lake.save_fx_dry_run_fixture_report(df, sum_d)
        return df, sum_d

    def build_fx_placeholders(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        m_df, m_sum = build_fx_manual_file_provider_placeholder(self.profile)
        l_df, l_sum = build_fx_local_cache_provider_placeholder(self.profile)
        o_df, o_sum = build_fx_official_api_provider_placeholder(self.profile)
        li_df, li_sum = build_fx_licensed_provider_placeholder(self.profile)
        if save:
            self.data_lake.save_fx_manual_file_provider_placeholder(m_df, m_sum)
            self.data_lake.save_fx_local_cache_provider_placeholder(l_df, l_sum)
            self.data_lake.save_fx_official_api_provider_placeholder(o_df, o_sum)
            self.data_lake.save_fx_licensed_provider_placeholder(li_df, li_sum)
        return {"manual": m_df, "local": l_df, "official": o_df, "licensed": li_df}, {"manual": m_sum, "local": l_sum, "official": o_sum, "licensed": li_sum}

    def build_fx_health_check(self, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        df, sum_d = build_fx_health_check(self.project_root, self.profile)
        if save: self.data_lake.save_fx_health_check(df, sum_d)
        return df, sum_d

    def build_fx_quality_report(self, save: bool = True) -> Tuple[Dict, Dict]:
        q = build_fx_quality_report({})
        if save: self.data_lake.save_fx_quality_report(self.profile.name, q)
        return q, q

    def build_fx_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        df = pd.DataFrame([{"status": "ready"}])
        sum_d = {"ready": True}
        return df, sum_d
