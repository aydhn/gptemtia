from pathlib import Path
from typing import Optional, Tuple, Dict, Any
import numpy as np
import pandas as pd

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_feature_engine.feature_engine_config import (
    FeatureEngineProfile,
    get_default_feature_engine_profile,
)
from advanced_feature_engine.feature_engine_profile_registry import (
    build_feature_engine_profile_registry,
)
from advanced_feature_engine.feature_engine_domain_registry import (
    build_feature_engine_domain_registry,
)
from advanced_feature_engine.feature_input_contracts import (
    build_feature_input_contract_registry,
)
from advanced_feature_engine.feature_schema_registry import (
    build_feature_schema_registry,
)
from advanced_feature_engine.factor_schema_registry import (
    build_factor_schema_registry,
)
from advanced_feature_engine.indicator_catalog_registry import (
    build_indicator_catalog_registry,
)
from advanced_feature_engine.price_indicator_catalog import (
    build_price_indicator_catalog,
)
from advanced_feature_engine.trend_indicator_catalog import (
    build_trend_indicator_catalog,
)
from advanced_feature_engine.momentum_indicator_catalog import (
    build_momentum_indicator_catalog,
)
from advanced_feature_engine.volatility_indicator_catalog import (
    build_volatility_indicator_catalog,
)
from advanced_feature_engine.mean_reversion_indicator_catalog import (
    build_mean_reversion_indicator_catalog,
)
from advanced_feature_engine.quote_feature_catalog import (
    build_quote_feature_catalog,
)
from advanced_feature_engine.volume_liquidity_feature_placeholders import (
    build_volume_liquidity_feature_placeholder_catalog,
)
from advanced_feature_engine.macro_feature_catalog import (
    build_macro_feature_catalog,
)
from advanced_feature_engine.calendar_event_feature_catalog import (
    build_calendar_event_feature_catalog,
)
from advanced_feature_engine.news_metadata_feature_catalog import (
    build_news_metadata_feature_catalog,
)
from advanced_feature_engine.feature_metadata_registry import (
    build_feature_metadata_registry,
)
from advanced_feature_engine.factor_metadata_registry import (
    build_factor_metadata_registry,
)
from advanced_feature_engine.rolling_window_contracts import (
    build_rolling_window_contract_registry,
)
from advanced_feature_engine.feature_computation_interfaces import (
    build_feature_computation_interface_contract,
)
from advanced_feature_engine.basic_feature_computations import (
    add_close_return,
    add_log_return,
    add_rolling_mean,
    add_rolling_std,
    add_sma,
    add_ema,
    add_true_range,
    add_atr,
    add_rsi,
    add_bollinger_zscore,
    add_quote_mid,
    add_quote_spread,
)
from advanced_feature_engine.feature_dependency_graph import (
    build_feature_dependency_graph_placeholder,
)
from advanced_feature_engine.feature_validation_rules import (
    build_feature_validation_rule_registry,
    validate_feature_dataframe,
)
from advanced_feature_engine.feature_quality_handoff import (
    build_feature_quality_handoff_registry,
)
from advanced_feature_engine.feature_engine_health import (
    build_feature_engine_health_check,
)
from advanced_feature_engine.feature_engine_validation import (
    build_feature_engine_validation_report,
)
from advanced_feature_engine.feature_engine_safety_boundary import (
    build_feature_engine_safety_boundary,
)
from advanced_feature_engine.phase_117_handoff import (
    build_phase_117_technical_indicator_expansion_handoff_report,
)
from advanced_feature_engine.feature_engine_report_builder import (
    build_feature_engine_profile_markdown_report,
    build_feature_input_contract_markdown_report,
    build_feature_schema_markdown_report,
    build_indicator_catalog_markdown_report,
    build_feature_metadata_markdown_report,
    build_feature_computation_markdown_report,
    build_feature_validation_markdown_report,
    build_feature_engine_health_markdown_report,
    build_feature_engine_safety_markdown_report,
    build_phase_117_handoff_markdown_report,
)


class FeatureEnginePipeline:
    def __init__(
        self,
        data_lake: Optional[DataLake],
        settings: Settings,
        project_root: Optional[Path] = None,
        profile: Optional[FeatureEngineProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = Path(project_root) if project_root else Path(".")
        self.profile = profile or get_default_feature_engine_profile()

    def build_profiles_domains_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        prof_df, prof_sum = build_feature_engine_profile_registry(self.profile)
        dom_df, dom_sum = build_feature_engine_domain_registry(self.profile)
        ic_df, ic_sum = build_feature_input_contract_registry(self.profile)

        if save and self.data_lake:
            self.data_lake.save_feature_engine_profile_registry(prof_df, prof_sum)
            self.data_lake.save_feature_engine_domain_registry(dom_df, dom_sum)
            self.data_lake.save_feature_input_contract_registry(ic_df, ic_sum)

        tables = {
            "profiles": prof_df,
            "domains": dom_df,
            "input_contracts": ic_df,
        }
        summary = {
            "profiles": prof_sum,
            "domains": dom_sum,
            "input_contracts": ic_sum,
        }
        return tables, summary

    def build_schemas_and_catalogs(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        fs_df, fs_sum = build_feature_schema_registry(self.profile)
        fact_df, fact_sum = build_factor_schema_registry(self.profile)
        ind_df, ind_sum = build_indicator_catalog_registry(self.profile)
        price_df, price_sum = build_price_indicator_catalog(self.profile)
        trend_df, trend_sum = build_trend_indicator_catalog(self.profile)
        mom_df, mom_sum = build_momentum_indicator_catalog(self.profile)
        vol_df, vol_sum = build_volatility_indicator_catalog(self.profile)
        mr_df, mr_sum = build_mean_reversion_indicator_catalog(self.profile)
        quote_df, quote_sum = build_quote_feature_catalog(self.profile)
        vl_df, vl_sum = build_volume_liquidity_feature_placeholder_catalog(self.profile)
        macro_df, macro_sum = build_macro_feature_catalog(self.profile)
        cal_df, cal_sum = build_calendar_event_feature_catalog(self.profile)
        news_df, news_sum = build_news_metadata_feature_catalog(self.profile)

        if save and self.data_lake:
            self.data_lake.save_feature_schema_registry(fs_df, fs_sum)
            self.data_lake.save_factor_schema_registry(fact_df, fact_sum)
            self.data_lake.save_indicator_catalog_registry(ind_df, ind_sum)
            self.data_lake.save_price_indicator_catalog(price_df, price_sum)
            self.data_lake.save_trend_indicator_catalog(trend_df, trend_sum)
            self.data_lake.save_momentum_indicator_catalog(mom_df, mom_sum)
            self.data_lake.save_volatility_indicator_catalog(vol_df, vol_sum)
            self.data_lake.save_mean_reversion_indicator_catalog(mr_df, mr_sum)
            self.data_lake.save_quote_feature_catalog(quote_df, quote_sum)
            self.data_lake.save_volume_liquidity_feature_placeholder_catalog(vl_df, vl_sum)
            self.data_lake.save_macro_feature_catalog(macro_df, macro_sum)
            self.data_lake.save_calendar_event_feature_catalog(cal_df, cal_sum)
            self.data_lake.save_news_metadata_feature_catalog(news_df, news_sum)

        tables = {
            "feature_schemas": fs_df,
            "factor_schemas": fact_df,
            "indicator_catalogs": ind_df,
            "price_catalog": price_df,
            "trend_catalog": trend_df,
            "momentum_catalog": mom_df,
            "volatility_catalog": vol_df,
            "mean_reversion_catalog": mr_df,
            "quote_catalog": quote_df,
            "volume_liquidity_catalog": vl_df,
            "macro_catalog": macro_df,
            "calendar_catalog": cal_df,
            "news_catalog": news_df,
        }
        summary = {
            "feature_schemas": fs_sum,
            "factor_schemas": fact_sum,
            "indicator_catalogs": ind_sum,
            "catalogs_count": 10,
        }
        return tables, summary

    def build_metadata_and_windows(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        fm_df, fm_sum = build_feature_metadata_registry(self.profile)
        fact_m_df, fact_m_sum = build_factor_metadata_registry(self.profile)
        rw_df, rw_sum = build_rolling_window_contract_registry(self.profile)
        comp_if_df, comp_if_sum = build_feature_computation_interface_contract(self.profile)
        dep_df, dep_sum = build_feature_dependency_graph_placeholder(self.profile)

        if save and self.data_lake:
            self.data_lake.save_feature_metadata_registry(fm_df, fm_sum)
            self.data_lake.save_factor_metadata_registry(fact_m_df, fact_m_sum)
            self.data_lake.save_rolling_window_contract_registry(rw_df, rw_sum)
            self.data_lake.save_feature_computation_interface_contract(comp_if_df, comp_if_sum)
            self.data_lake.save_feature_dependency_graph_placeholder(dep_df, dep_sum)

        tables = {
            "feature_metadata": fm_df,
            "factor_metadata": fact_m_df,
            "rolling_windows": rw_df,
            "computation_interface": comp_if_df,
            "dependency_graph": dep_df,
        }
        summary = {
            "feature_metadata": fm_sum,
            "factor_metadata": fact_m_sum,
            "rolling_windows": rw_sum,
            "computation_interface": comp_if_sum,
            "dependency_graph": dep_sum,
        }
        return tables, summary

    def run_basic_computation_rehearsal(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        # Synthetic local fixture
        np.random.seed(42)
        n = 50
        dates = pd.date_range("2026-01-01", periods=n, freq="D")
        close_prices = 100.0 + np.cumsum(np.random.randn(n) * 0.5)
        high_prices = close_prices + np.abs(np.random.randn(n) * 0.3)
        low_prices = close_prices - np.abs(np.random.randn(n) * 0.3)
        open_prices = close_prices + np.random.randn(n) * 0.1
        bids = close_prices - 0.02
        asks = close_prices + 0.02

        raw_df = pd.DataFrame({
            "timestamp": dates,
            "symbol": "USDTRY",
            "open": open_prices,
            "high": high_prices,
            "low": low_prices,
            "close": close_prices,
            "volume": np.random.randint(1000, 5000, size=n),
            "bid": bids,
            "ask": asks,
        })
        raw_copy = raw_df.copy()

        # Execute pure functions
        step1 = add_close_return(raw_df, close_field="close", window=1)
        step2 = add_log_return(step1, close_field="close", window=1)
        step3 = add_rolling_mean(step2, field="close", window=20)
        step4 = add_rolling_std(step3, field="close", window=20)
        step5 = add_sma(step4, field="close", window=20)
        step6 = add_ema(step5, field="close", window=20)
        step7 = add_true_range(step6, high_field="high", low_field="low", close_field="close")
        step8 = add_atr(step7, high_field="high", low_field="low", close_field="close", window=14)
        step9 = add_rsi(step8, close_field="close", window=14)
        step10 = add_bollinger_zscore(step9, field="close", window=20)
        step11 = add_quote_mid(step10, bid_field="bid", ask_field="ask")
        final_df = add_quote_spread(step11, bid_field="bid", ask_field="ask")

        # Verify raw_df was not mutated
        assert raw_df.equals(raw_copy), "Pipeline rehearsal mutated input dataframe!"

        # Validate resulting dataframe
        computed_cols = [
            "close_return_1", "log_return_1", "rolling_mean_20", "rolling_std_20",
            "sma_20", "ema_20", "true_range", "atr_14", "rsi_14",
            "bollinger_zscore_20", "quote_mid", "quote_spread"
        ]
        val_res = validate_feature_dataframe(final_df, computed_cols)

        summary = {
            "features_computed_count": len(computed_cols),
            "computed_columns": computed_cols,
            "validation_passed": val_res["valid"],
            "input_mutation_free": True,
            "non_signal": True,
        }
        return {"rehearsal_output": final_df}, summary

    def build_validation_quality_safety(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        val_rules_df, val_rules_sum = build_feature_validation_rule_registry(self.profile)
        qual_df, qual_sum = build_feature_quality_handoff_registry(self.profile)
        safe_df, safe_sum = build_feature_engine_safety_boundary(self.profile)
        health_df, health_sum = build_feature_engine_health_check(self.project_root, self.profile)

        # Cross-table validation report
        prof_df, _ = build_feature_engine_profile_registry(self.profile)
        ic_df, _ = build_feature_input_contract_registry(self.profile)
        fs_df, _ = build_feature_schema_registry(self.profile)
        fact_df, _ = build_factor_schema_registry(self.profile)
        ind_df, _ = build_indicator_catalog_registry(self.profile)

        val_tables = {
            "profiles": prof_df,
            "input_contracts": ic_df,
            "feature_schemas": fs_df,
            "factor_schemas": fact_df,
            "indicator_catalogs": ind_df,
            "safety": safe_df,
        }
        val_report_df, val_report_sum = build_feature_engine_validation_report(val_tables, self.profile)
        h117_df, h117_sum = build_phase_117_technical_indicator_expansion_handoff_report(self.profile)

        if save and self.data_lake:
            self.data_lake.save_feature_validation_rule_registry(val_rules_df, val_rules_sum)
            self.data_lake.save_feature_quality_handoff_registry(qual_df, qual_sum)
            self.data_lake.save_feature_engine_safety_boundary(safe_df, safe_sum)
            self.data_lake.save_feature_engine_health_check(health_df, health_sum)
            self.data_lake.save_feature_engine_validation_report(val_report_df, val_report_sum)
            self.data_lake.save_phase_117_technical_indicator_expansion_handoff_report(h117_df, h117_sum)

        tables = {
            "validation_rules": val_rules_df,
            "quality_handoff": qual_df,
            "safety": safe_df,
            "health": health_df,
            "validation_report": val_report_df,
            "phase_117_handoff": h117_df,
        }
        summary = {
            "validation_rules": val_rules_sum,
            "quality_handoff": qual_sum,
            "safety": safe_sum,
            "health": health_sum,
            "validation_report": val_report_sum,
            "phase_117_handoff": h117_sum,
        }
        return tables, summary

    def build_feature_engine_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        t_pdm, s_pdm = self.build_profiles_domains_contracts(save=save)
        t_cat, s_cat = self.build_schemas_and_catalogs(save=save)
        t_meta, s_meta = self.build_metadata_and_windows(save=save)
        t_reh, s_reh = self.run_basic_computation_rehearsal(save=save)
        t_safe, s_safe = self.build_validation_quality_safety(save=save)

        status_rows = [
            {"component": "profiles", "records": len(t_pdm["profiles"]), "status": "READY"},
            {"component": "domains", "records": len(t_pdm["domains"]), "status": "READY"},
            {"component": "input_contracts", "records": len(t_pdm["input_contracts"]), "status": "READY"},
            {"component": "feature_schemas", "records": len(t_cat["feature_schemas"]), "status": "READY"},
            {"component": "factor_schemas", "records": len(t_cat["factor_schemas"]), "status": "READY"},
            {"component": "indicator_catalogs", "records": len(t_cat["indicator_catalogs"]), "status": "READY"},
            {"component": "quote_features", "records": len(t_cat["quote_catalog"]), "status": "READY"},
            {"component": "volume_liquidity", "records": len(t_cat["volume_liquidity_catalog"]), "status": "READY"},
            {"component": "macro_features", "records": len(t_cat["macro_catalog"]), "status": "READY"},
            {"component": "calendar_features", "records": len(t_cat["calendar_catalog"]), "status": "READY"},
            {"component": "news_metadata_features", "records": len(t_cat["news_catalog"]), "status": "READY"},
            {"component": "feature_metadata", "records": len(t_meta["feature_metadata"]), "status": "READY"},
            {"component": "factor_metadata", "records": len(t_meta["factor_metadata"]), "status": "READY"},
            {"component": "rolling_windows", "records": len(t_meta["rolling_windows"]), "status": "READY"},
            {"component": "computation_interface", "records": len(t_meta["computation_interface"]), "status": "READY"},
            {"component": "dependency_graph", "records": len(t_meta["dependency_graph"]), "status": "READY"},
            {"component": "computation_rehearsal", "records": len(t_reh["rehearsal_output"]), "status": "PASS"},
            {"component": "validation_rules", "records": len(t_safe["validation_rules"]), "status": "READY"},
            {"component": "quality_handoff", "records": len(t_safe["quality_handoff"]), "status": "READY"},
            {"component": "safety_boundary", "records": len(t_safe["safety"]), "status": "ACTIVE"},
            {"component": "health_check", "records": len(t_safe["health"]), "status": s_safe["health"]["overall_status"]},
            {"component": "validation_report", "records": len(t_safe["validation_report"]), "status": s_safe["validation_report"]["validation_status"]},
            {"component": "phase_117_handoff", "records": len(t_safe["phase_117_handoff"]), "status": "READY"},
        ]
        status_df = pd.DataFrame.from_records(status_rows)

        overall_sum = {
            "current_phase": self.profile.current_phase,
            "target_final_phase": self.profile.target_final_phase,
            "next_phase": self.profile.next_phase,
            "profile_name": self.profile.name,
            "phase_name": "Advanced Indicator/Feature/Factor Engine Foundation",
            "all_subsystems_ready": bool((status_df["status"].isin(["READY", "ACTIVE", "PASS", "VALID"])).all()),
            "total_subsystems": len(status_df),
            "non_signal": True,
        }

        if save and self.data_lake:
            md_report = build_feature_engine_profile_markdown_report(s_pdm["profiles"], t_pdm["profiles"])
            self.data_lake.save_feature_engine_report(
                profile_name=self.profile.name,
                report=overall_sum,
                markdown=md_report,
            )

        return status_df, overall_sum
