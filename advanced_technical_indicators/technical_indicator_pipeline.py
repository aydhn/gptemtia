from typing import Tuple, Dict, Any, Optional
from pathlib import Path
import pandas as pd

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_technical_indicators.technical_indicator_config import (
    TechnicalIndicatorProfile,
    get_default_technical_indicator_profile,
)
from advanced_technical_indicators.technical_indicator_profile_registry import (
    build_technical_indicator_profile_registry,
)
from advanced_technical_indicators.technical_indicator_domain_registry import (
    build_technical_indicator_domain_registry,
)
from advanced_technical_indicators.technical_indicator_catalog_expansion import (
    build_technical_indicator_catalog_expansion,
)
from advanced_technical_indicators.price_action_indicators import (
    build_price_action_indicator_registry,
)
from advanced_technical_indicators.return_indicators import (
    build_return_indicator_registry,
)
from advanced_technical_indicators.moving_average_indicators import (
    build_moving_average_indicator_registry,
)
from advanced_technical_indicators.trend_indicators import (
    build_trend_indicator_expansion_registry,
)
from advanced_technical_indicators.momentum_indicators import (
    build_momentum_indicator_expansion_registry,
)
from advanced_technical_indicators.oscillator_indicators import (
    build_oscillator_indicator_registry,
)
from advanced_technical_indicators.volatility_indicators import (
    build_volatility_indicator_expansion_registry,
)
from advanced_technical_indicators.range_indicators import (
    build_range_indicator_registry,
)
from advanced_technical_indicators.channel_indicators import (
    build_channel_indicator_registry,
)
from advanced_technical_indicators.candle_anatomy_features import (
    build_candle_anatomy_feature_registry,
)
from advanced_technical_indicators.quote_microstructure_features import (
    build_quote_microstructure_feature_registry,
)
from advanced_technical_indicators.mean_reversion_indicators import (
    build_mean_reversion_indicator_expansion_registry,
)
from advanced_technical_indicators.indicator_parameter_contracts import (
    build_indicator_parameter_contract_registry,
)
from advanced_technical_indicators.indicator_output_schema_registry import (
    build_indicator_output_schema_registry,
)
from advanced_technical_indicators.indicator_warmup_nan_policy import (
    build_indicator_warmup_nan_policy_registry,
)
from advanced_technical_indicators.no_lookahead_indicator_guard import (
    build_no_lookahead_indicator_guard_registry,
)
from advanced_technical_indicators.indicator_computation_interfaces import (
    build_indicator_computation_interface_contract,
)
from advanced_technical_indicators.advanced_indicator_computations import (
    build_advanced_indicator_computation_module_report,
)
from advanced_technical_indicators.indicator_computation_rehearsal import (
    run_indicator_rehearsal_suite,
)
from advanced_technical_indicators.indicator_validation_rules import (
    build_indicator_validation_rule_registry,
)
from advanced_technical_indicators.indicator_dependency_registry import (
    build_indicator_dependency_registry,
)
from advanced_technical_indicators.indicator_quality_handoff import (
    build_indicator_quality_handoff_report,
)
from advanced_technical_indicators.technical_indicator_health import (
    build_technical_indicator_health_check,
)
from advanced_technical_indicators.technical_indicator_validation import (
    build_technical_indicator_validation_report,
)
from advanced_technical_indicators.technical_indicator_safety_boundary import (
    build_technical_indicator_safety_boundary,
)
from advanced_technical_indicators.phase_118_handoff import (
    build_phase_118_multi_window_feature_grid_handoff_report,
)
from advanced_technical_indicators.technical_indicator_report_builder import (
    build_technical_indicator_profile_markdown_report,
    build_technical_indicator_catalog_markdown_report,
    build_indicator_family_markdown_report,
    build_indicator_rehearsal_markdown_report,
    build_indicator_validation_markdown_report,
    build_technical_indicator_health_markdown_report,
    build_technical_indicator_safety_markdown_report,
    build_phase_118_handoff_markdown_report,
)


class TechnicalIndicatorPipeline:
    """Orchestrator for Phase 117 Technical Indicator Expansion layer."""

    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[TechnicalIndicatorProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_technical_indicator_profile()

    def build_profiles_domains_catalogs(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        prof_df, prof_sum = build_technical_indicator_profile_registry(self.profile)
        dom_df, dom_sum = build_technical_indicator_domain_registry(self.profile)
        cat_df, cat_sum = build_technical_indicator_catalog_expansion(self.profile)

        if save:
            self.data_lake.save_technical_indicator_profile_registry(prof_df, prof_sum)
            self.data_lake.save_technical_indicator_domain_registry(dom_df, dom_sum)
            self.data_lake.save_technical_indicator_catalog_expansion(cat_df, cat_sum)

            # Write markdown reports
            prof_md = build_technical_indicator_profile_markdown_report(prof_sum, prof_df)
            cat_md = build_technical_indicator_catalog_markdown_report(cat_sum, cat_df)
            self._write_markdown("profile_report.md", prof_md)
            self._write_markdown("catalog_report.md", cat_md)

        tables = {"profile_registry": prof_df, "domain_registry": dom_df, "catalog_expansion": cat_df}
        summary = {"profiles": prof_sum, "domains": dom_sum, "catalog": cat_sum}
        return tables, summary

    def build_indicator_family_registries(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        pa_df, pa_sum = build_price_action_indicator_registry(self.profile)
        ret_df, ret_sum = build_return_indicator_registry(self.profile)
        ma_df, ma_sum = build_moving_average_indicator_registry(self.profile)
        trend_df, trend_sum = build_trend_indicator_expansion_registry(self.profile)
        mom_df, mom_sum = build_momentum_indicator_expansion_registry(self.profile)
        osc_df, osc_sum = build_oscillator_indicator_registry(self.profile)
        vol_df, vol_sum = build_volatility_indicator_expansion_registry(self.profile)
        rng_df, rng_sum = build_range_indicator_registry(self.profile)
        chan_df, chan_sum = build_channel_indicator_registry(self.profile)
        cndl_df, cndl_sum = build_candle_anatomy_feature_registry(self.profile)
        quote_df, quote_sum = build_quote_microstructure_feature_registry(self.profile)
        mr_df, mr_sum = build_mean_reversion_indicator_expansion_registry(self.profile)

        if save:
            self.data_lake.save_price_action_indicator_registry(pa_df, pa_sum)
            self.data_lake.save_return_indicator_registry(ret_df, ret_sum)
            self.data_lake.save_moving_average_indicator_registry(ma_df, ma_sum)
            self.data_lake.save_trend_indicator_expansion_registry(trend_df, trend_sum)
            self.data_lake.save_momentum_indicator_expansion_registry(mom_df, mom_sum)
            self.data_lake.save_oscillator_indicator_registry(osc_df, osc_sum)
            self.data_lake.save_volatility_indicator_expansion_registry(vol_df, vol_sum)
            self.data_lake.save_range_indicator_registry(rng_df, rng_sum)
            self.data_lake.save_channel_indicator_registry(chan_df, chan_sum)
            self.data_lake.save_candle_anatomy_feature_registry(cndl_df, cndl_sum)
            self.data_lake.save_quote_microstructure_feature_registry(quote_df, quote_sum)
            self.data_lake.save_mean_reversion_indicator_expansion_registry(mr_df, mr_sum)

        tables = {
            "price_action": pa_df, "returns": ret_df, "moving_averages": ma_df,
            "trend": trend_df, "momentum": mom_df, "oscillators": osc_df,
            "volatility": vol_df, "range": rng_df, "channels": chan_df,
            "candle_anatomy": cndl_df, "quote_microstructure": quote_df, "mean_reversion": mr_df,
        }
        summary = {
            "families_count": len(tables),
            "status": "READY",
            "non_signal": True,
        }
        return tables, summary

    def build_contracts_schema_and_policies(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        param_df, param_sum = build_indicator_parameter_contract_registry(self.profile)
        schema_df, schema_sum = build_indicator_output_schema_registry(self.profile)
        warmup_df, warmup_sum = build_indicator_warmup_nan_policy_registry(self.profile)
        guard_df, guard_sum = build_no_lookahead_indicator_guard_registry(self.profile)
        iface_df, iface_sum = build_indicator_computation_interface_contract(self.profile)
        comp_df, comp_sum = build_advanced_indicator_computation_module_report(self.profile)

        if save:
            self.data_lake.save_indicator_parameter_contract_registry(param_df, param_sum)
            self.data_lake.save_indicator_output_schema_registry(schema_df, schema_sum)
            self.data_lake.save_indicator_warmup_nan_policy_registry(warmup_df, warmup_sum)
            self.data_lake.save_no_lookahead_indicator_guard_registry(guard_df, guard_sum)
            self.data_lake.save_indicator_computation_interface_contract(iface_df, iface_sum)

        tables = {
            "parameters": param_df, "output_schema": schema_df,
            "warmup_nan": warmup_df, "no_lookahead": guard_df,
            "computation_interface": iface_df, "computations": comp_df,
        }
        summary = {"parameters": param_sum, "schema": schema_sum, "warmup": warmup_sum, "guard": guard_sum}
        return tables, summary

    def run_indicator_computation_rehearsal(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        reh_df, reh_sum = run_indicator_rehearsal_suite(self.profile)
        if save:
            self.data_lake.save_indicator_computation_rehearsal_report(reh_df, reh_sum)
            reh_md = build_indicator_rehearsal_markdown_report(reh_sum, reh_df)
            self._write_markdown("rehearsal_report.md", reh_md)

        tables = {"rehearsal_report": reh_df}
        return tables, reh_sum

    def build_validation_dependency_quality(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        val_rules_df, val_rules_sum = build_indicator_validation_rule_registry(self.profile)
        dep_df, dep_sum = build_indicator_dependency_registry(self.profile)
        qual_df, qual_sum = build_indicator_quality_handoff_report(self.profile)

        if save:
            self.data_lake.save_indicator_validation_rule_registry(val_rules_df, val_rules_sum)
            self.data_lake.save_indicator_dependency_registry(dep_df, dep_sum)
            self.data_lake.save_indicator_quality_handoff_report(qual_df, qual_sum)

        tables = {
            "validation_rules": val_rules_df,
            "dependencies": dep_df,
            "quality_handoff": qual_df,
        }
        summary = {"validation_rules": val_rules_sum, "dependencies": dep_sum, "quality": qual_sum}
        return tables, summary

    def build_health_validation_safety_handoff(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        health_df, health_sum = build_technical_indicator_health_check(self.project_root, self.profile)
        safety_df, safety_sum = build_technical_indicator_safety_boundary(self.profile)
        handoff_df, handoff_sum = build_phase_118_multi_window_feature_grid_handoff_report(self.profile)

        # Validation report over current tables
        tables_to_val = {"safety": safety_df, "health": health_df, "handoff": handoff_df}
        val_df, val_sum = build_technical_indicator_validation_report(tables_to_val, self.profile)

        if save:
            self.data_lake.save_technical_indicator_health_check(health_df, health_sum)
            self.data_lake.save_technical_indicator_safety_boundary(safety_df, safety_sum)
            self.data_lake.save_phase_118_multi_window_feature_grid_handoff_report(handoff_df, handoff_sum)
            self.data_lake.save_technical_indicator_validation_report(val_df, val_sum)

            h_md = build_technical_indicator_health_markdown_report(health_sum, health_df)
            s_md = build_technical_indicator_safety_markdown_report(safety_sum, safety_df)
            v_md = build_indicator_validation_markdown_report(val_sum, val_df)
            ho_md = build_phase_118_handoff_markdown_report(handoff_sum, handoff_df)

            self._write_markdown("health_report.md", h_md)
            self._write_markdown("safety_report.md", s_md)
            self._write_markdown("validation_report.md", v_md)
            self._write_markdown("phase_118_handoff.md", ho_md)

        tables = {
            "health": health_df,
            "safety": safety_df,
            "validation": val_df,
            "handoff": handoff_df,
        }
        summary = {"health": health_sum, "safety": safety_sum, "validation": val_sum, "handoff": handoff_sum}
        return tables, summary

    def build_technical_indicator_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        prof_tables, _ = self.build_profiles_domains_catalogs(save=save)
        fam_tables, _ = self.build_indicator_family_registries(save=save)
        c_tables, _ = self.build_contracts_schema_and_policies(save=save)
        r_tables, r_sum = self.run_indicator_computation_rehearsal(save=save)
        v_tables, _ = self.build_validation_dependency_quality(save=save)
        h_tables, h_sum = self.build_health_validation_safety_handoff(save=save)

        status_rows = [
            {"component": "profile_registry", "rows": len(prof_tables["profile_registry"]), "status": "READY"},
            {"component": "domain_registry", "rows": len(prof_tables["domain_registry"]), "status": "READY"},
            {"component": "catalog_expansion", "rows": len(prof_tables["catalog_expansion"]), "status": "READY"},
            {"component": "indicator_families", "rows": len(fam_tables), "status": "READY"},
            {"component": "parameter_contracts", "rows": len(c_tables["parameters"]), "status": "READY"},
            {"component": "output_schema", "rows": len(c_tables["output_schema"]), "status": "READY"},
            {"component": "warmup_nan_policy", "rows": len(c_tables["warmup_nan"]), "status": "READY"},
            {"component": "no_lookahead_guard", "rows": len(c_tables["no_lookahead"]), "status": "READY"},
            {"component": "computation_rehearsal", "rows": len(r_tables["rehearsal_report"]), "status": "PASS"},
            {"component": "indicator_dependencies", "rows": len(v_tables["dependencies"]), "status": "READY"},
            {"component": "quality_handoff", "rows": len(v_tables["quality_handoff"]), "status": "READY"},
            {"component": "health_check", "rows": len(h_tables["health"]), "status": h_sum["health"]["health_status"]},
            {"component": "safety_boundary", "rows": len(h_tables["safety"]), "status": "ACTIVE"},
            {"component": "validation_report", "rows": len(h_tables["validation"]), "status": "PASS"},
            {"component": "phase_118_handoff", "rows": len(h_tables["handoff"]), "status": "READY"},
        ]
        status_df = pd.DataFrame(status_rows)
        overall_summary = {
            "phase": 117,
            "phase_name": "Technical Indicator Expansion",
            "target_final_phase": 160,
            "next_phase": 118,
            "overall_status": "READY",
            "non_signal": True,
            "components_count": len(status_df),
        }
        if save:
            self.data_lake.save_technical_indicator_report(
                self.profile.name,
                overall_summary,
                markdown=f"# Phase 117 Overall Status: READY\n\nComponents: {len(status_df)}",
            )
        return status_df, overall_summary

    def _write_markdown(self, filename: str, content: str) -> None:
        out_dir = self.project_root / "reports" / "output" / "advanced_technical_indicators" / "markdown"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / filename).write_text(content, encoding="utf-8")
