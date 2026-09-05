from pathlib import Path
from typing import Dict, Any, Tuple, Optional
import pandas as pd

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_feature_grid.feature_grid_config import (
    FeatureGridProfile,
    get_default_feature_grid_profile,
)
from advanced_feature_grid.feature_grid_profile_registry import build_feature_grid_profile_registry
from advanced_feature_grid.feature_grid_domain_registry import build_feature_grid_domain_registry
from advanced_feature_grid.window_grid_contracts import build_window_grid_contract_registry
from advanced_feature_grid.indicator_parameter_grid_registry import build_indicator_parameter_grid_registry
from advanced_feature_grid.feature_grid_naming import build_feature_grid_naming_registry
from advanced_feature_grid.feature_grid_output_schema import build_feature_grid_output_schema_registry
from advanced_feature_grid.feature_grid_warmup_nan_policy import build_feature_grid_warmup_nan_policy_registry
from advanced_feature_grid.feature_grid_no_lookahead_guard import build_feature_grid_no_lookahead_guard_registry
from advanced_feature_grid.feature_grid_duplicate_detection import build_feature_grid_duplicate_detection_registry
from advanced_feature_grid.moving_average_window_grid import build_moving_average_window_grid_registry
from advanced_feature_grid.momentum_window_grid import build_momentum_window_grid_registry
from advanced_feature_grid.volatility_window_grid import build_volatility_window_grid_registry
from advanced_feature_grid.range_channel_window_grid import build_range_channel_window_grid_registry
from advanced_feature_grid.mean_reversion_window_grid import build_mean_reversion_window_grid_registry
from advanced_feature_grid.return_window_grid import build_return_window_grid_registry
from advanced_feature_grid.quote_feature_grid_placeholders import build_quote_feature_grid_placeholder_registry
from advanced_feature_grid.macro_feature_grid_placeholders import build_macro_feature_grid_placeholder_registry
from advanced_feature_grid.calendar_feature_grid_placeholders import build_calendar_feature_grid_placeholder_registry
from advanced_feature_grid.news_metadata_feature_grid_placeholders import build_news_metadata_feature_grid_placeholder_registry
from advanced_feature_grid.feature_grid_computation_interfaces import build_feature_grid_computation_interface_contract
from advanced_feature_grid.feature_grid_computations import build_feature_grid_computation_module_report
from advanced_feature_grid.feature_grid_computation_rehearsal import build_feature_grid_computation_rehearsal_report
from advanced_feature_grid.feature_grid_metadata_registry import build_feature_grid_metadata_registry
from advanced_feature_grid.feature_grid_dependency_registry import build_feature_grid_dependency_registry
from advanced_feature_grid.feature_grid_validation_rules import build_feature_grid_validation_rule_registry
from advanced_feature_grid.feature_grid_quality_handoff import build_feature_grid_quality_handoff_report
from advanced_feature_grid.feature_grid_health import build_feature_grid_health_check
from advanced_feature_grid.feature_grid_safety_boundary import build_feature_grid_safety_boundary
from advanced_feature_grid.feature_grid_validation import build_feature_grid_validation_report
from advanced_feature_grid.phase_119_handoff import build_phase_119_cross_asset_feature_alignment_handoff_report
from advanced_feature_grid.feature_grid_report_builder import (
    build_feature_grid_profile_markdown_report,
    build_window_grid_contract_markdown_report,
    build_parameter_grid_markdown_report,
    build_feature_grid_family_markdown_report,
    build_feature_grid_rehearsal_markdown_report,
    build_feature_grid_validation_markdown_report,
    build_feature_grid_health_markdown_report,
    build_feature_grid_safety_markdown_report,
    build_phase_119_handoff_markdown_report,
)


class FeatureGridPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[FeatureGridProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_feature_grid_profile()

    def build_profiles_domains_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_prof, sum_prof = build_feature_grid_profile_registry(self.profile)
        df_dom, sum_dom = build_feature_grid_domain_registry(self.profile)
        df_wgc, sum_wgc = build_window_grid_contract_registry(self.profile)

        tables = {
            "profiles": df_prof,
            "domains": df_dom,
            "window_contracts": df_wgc,
        }
        summary = {
            "profiles": sum_prof,
            "domains": sum_dom,
            "window_contracts": sum_wgc,
        }

        if save:
            self.data_lake.save_feature_grid_profile_registry(df_prof, sum_prof)
            self.data_lake.save_feature_grid_domain_registry(df_dom, sum_dom)
            self.data_lake.save_window_grid_contract_registry(df_wgc, sum_wgc)

            # Write markdown
            md = build_feature_grid_profile_markdown_report(sum_prof, df_prof)
            self.data_lake.save_feature_grid_report("profiles", sum_prof, md)
            md_wgc = build_window_grid_contract_markdown_report(sum_wgc, df_wgc)
            self.data_lake.save_feature_grid_report("window_contracts", sum_wgc, md_wgc)

        return tables, summary

    def build_parameter_naming_schema_policies(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_param, sum_param = build_indicator_parameter_grid_registry(self.profile)
        df_nam, sum_nam = build_feature_grid_naming_registry(self.profile)
        df_sch, sum_sch = build_feature_grid_output_schema_registry(self.profile)
        df_warm, sum_warm = build_feature_grid_warmup_nan_policy_registry(self.profile)
        df_nl, sum_nl = build_feature_grid_no_lookahead_guard_registry(self.profile)
        df_dup, sum_dup = build_feature_grid_duplicate_detection_registry(self.profile)

        tables = {
            "parameter_grids": df_param,
            "naming": df_nam,
            "output_schema": df_sch,
            "warmup_nan": df_warm,
            "no_lookahead": df_nl,
            "duplicates": df_dup,
        }
        summary = {
            "parameter_grids": sum_param,
            "naming": sum_nam,
            "output_schema": sum_sch,
            "warmup_nan": sum_warm,
            "no_lookahead": sum_nl,
            "duplicates": sum_dup,
        }

        if save:
            self.data_lake.save_indicator_parameter_grid_registry(df_param, sum_param)
            self.data_lake.save_feature_grid_naming_registry(df_nam, sum_nam)
            self.data_lake.save_feature_grid_output_schema_registry(df_sch, sum_sch)
            self.data_lake.save_feature_grid_warmup_nan_policy_registry(df_warm, sum_warm)
            self.data_lake.save_feature_grid_no_lookahead_guard_registry(df_nl, sum_nl)
            self.data_lake.save_feature_grid_duplicate_detection_registry(df_dup, sum_dup)

            md = build_parameter_grid_markdown_report(sum_param, df_param)
            self.data_lake.save_feature_grid_report("parameter_grids", sum_param, md)

        return tables, summary

    def build_window_grid_registries(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_ma, sum_ma = build_moving_average_window_grid_registry(self.profile)
        df_mom, sum_mom = build_momentum_window_grid_registry(self.profile)
        df_vol, sum_vol = build_volatility_window_grid_registry(self.profile)
        df_rc, sum_rc = build_range_channel_window_grid_registry(self.profile)
        df_mr, sum_mr = build_mean_reversion_window_grid_registry(self.profile)
        df_ret, sum_ret = build_return_window_grid_registry(self.profile)

        df_quote, sum_quote = build_quote_feature_grid_placeholder_registry(self.profile)
        df_macro, sum_macro = build_macro_feature_grid_placeholder_registry(self.profile)
        df_cal, sum_cal = build_calendar_feature_grid_placeholder_registry(self.profile)
        df_news, sum_news = build_news_metadata_feature_grid_placeholder_registry(self.profile)

        tables = {
            "moving_average": df_ma,
            "momentum": df_mom,
            "volatility": df_vol,
            "range_channel": df_rc,
            "mean_reversion": df_mr,
            "returns": df_ret,
            "quote_placeholders": df_quote,
            "macro_placeholders": df_macro,
            "calendar_placeholders": df_cal,
            "news_placeholders": df_news,
        }
        summary = {
            "moving_average": sum_ma,
            "momentum": sum_mom,
            "volatility": sum_vol,
            "range_channel": sum_rc,
            "mean_reversion": sum_mr,
            "returns": sum_ret,
            "quote_placeholders": sum_quote,
            "macro_placeholders": sum_macro,
            "calendar_placeholders": sum_cal,
            "news_placeholders": sum_news,
        }

        if save:
            self.data_lake.save_moving_average_window_grid_registry(df_ma, sum_ma)
            self.data_lake.save_momentum_window_grid_registry(df_mom, sum_mom)
            self.data_lake.save_volatility_window_grid_registry(df_vol, sum_vol)
            self.data_lake.save_range_channel_window_grid_registry(df_rc, sum_rc)
            self.data_lake.save_mean_reversion_window_grid_registry(df_mr, sum_mr)
            self.data_lake.save_return_window_grid_registry(df_ret, sum_ret)
            self.data_lake.save_quote_feature_grid_placeholder_registry(df_quote, sum_quote)
            self.data_lake.save_macro_feature_grid_placeholder_registry(df_macro, sum_macro)
            self.data_lake.save_calendar_feature_grid_placeholder_registry(df_cal, sum_cal)
            self.data_lake.save_news_metadata_feature_grid_placeholder_registry(df_news, sum_news)

            md = build_feature_grid_family_markdown_report(sum_ma, df_ma)
            self.data_lake.save_feature_grid_report("moving_average_grid", sum_ma, md)

        return tables, summary

    def run_feature_grid_computation_rehearsal(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_int, sum_int = build_feature_grid_computation_interface_contract(self.profile)
        df_mod, sum_mod = build_feature_grid_computation_module_report(self.profile)
        df_reh, sum_reh = build_feature_grid_computation_rehearsal_report(self.profile)

        tables = {
            "computation_interfaces": df_int,
            "computation_modules": df_mod,
            "rehearsal": df_reh,
        }
        summary = {
            "computation_interfaces": sum_int,
            "computation_modules": sum_mod,
            "rehearsal": sum_reh,
        }

        if save:
            self.data_lake.save_feature_grid_computation_interface_contract(df_int, sum_int)
            self.data_lake.save_feature_grid_computation_rehearsal_report(df_reh, sum_reh)

            md = build_feature_grid_rehearsal_markdown_report(sum_reh, df_reh)
            self.data_lake.save_feature_grid_report("rehearsal", sum_reh, md)

        return tables, summary

    def build_metadata_dependency_quality(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_meta, sum_meta = build_feature_grid_metadata_registry(self.profile)
        df_dep, sum_dep = build_feature_grid_dependency_registry(self.profile)
        df_rules, sum_rules = build_feature_grid_validation_rule_registry(self.profile)
        df_qual, sum_qual = build_feature_grid_quality_handoff_report(self.profile)

        tables = {
            "metadata": df_meta,
            "dependencies": df_dep,
            "validation_rules": df_rules,
            "quality_handoff": df_qual,
        }
        summary = {
            "metadata": sum_meta,
            "dependencies": sum_dep,
            "validation_rules": sum_rules,
            "quality_handoff": sum_qual,
        }

        if save:
            self.data_lake.save_feature_grid_metadata_registry(df_meta, sum_meta)
            self.data_lake.save_feature_grid_dependency_registry(df_dep, sum_dep)
            self.data_lake.save_feature_grid_validation_rule_registry(df_rules, sum_rules)
            self.data_lake.save_feature_grid_quality_handoff_report(df_qual, sum_qual)

        return tables, summary

    def build_health_validation_safety_handoff(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_health, sum_health = build_feature_grid_health_check(self.project_root, self.profile)
        df_safe, sum_safe = build_feature_grid_safety_boundary(self.profile)

        # Collect tables for validation report
        rehearsal_tables, _ = self.run_feature_grid_computation_rehearsal(save=False)
        profile_tables, _ = self.build_profiles_domains_contracts(save=False)
        param_tables, _ = self.build_parameter_naming_schema_policies(save=False)

        val_tables_in = {
            "profiles": profile_tables["profiles"],
            "window_contracts": profile_tables["window_contracts"],
            "parameter_grids": param_tables["parameter_grids"],
            "rehearsal": rehearsal_tables["rehearsal"],
        }
        df_val, sum_val = build_feature_grid_validation_report(val_tables_in, self.profile)
        df_ho, sum_ho = build_phase_119_cross_asset_feature_alignment_handoff_report(self.profile)

        tables = {
            "health": df_health,
            "safety": df_safe,
            "validation": df_val,
            "phase_119_handoff": df_ho,
        }
        summary = {
            "health": sum_health,
            "safety": sum_safe,
            "validation": sum_val,
            "phase_119_handoff": sum_ho,
        }

        if save:
            self.data_lake.save_multi_window_feature_health_check(df_health, sum_health)
            self.data_lake.save_multi_window_feature_safety_boundary(df_safe, sum_safe)
            self.data_lake.save_multi_window_feature_validation_report(df_val, sum_val)
            self.data_lake.save_phase_119_cross_asset_feature_alignment_handoff_report(df_ho, sum_ho)

            md_h = build_feature_grid_health_markdown_report(sum_health, df_health)
            self.data_lake.save_feature_grid_report("health", sum_health, md_h)
            md_s = build_feature_grid_safety_markdown_report(sum_safe, df_safe)
            self.data_lake.save_feature_grid_report("safety", sum_safe, md_s)
            md_v = build_feature_grid_validation_markdown_report(sum_val, df_val)
            self.data_lake.save_feature_grid_report("validation", sum_val, md_v)
            md_ho = build_phase_119_handoff_markdown_report(sum_ho, df_ho)
            self.data_lake.save_feature_grid_report("phase_119_handoff", sum_ho, md_ho)

        return tables, summary

    def build_feature_grid_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        p_tables, p_sum = self.build_profiles_domains_contracts(save=save)
        c_tables, c_sum = self.build_parameter_naming_schema_policies(save=save)
        w_tables, w_sum = self.build_window_grid_registries(save=save)
        r_tables, r_sum = self.run_feature_grid_computation_rehearsal(save=save)
        m_tables, m_sum = self.build_metadata_dependency_quality(save=save)
        h_tables, h_sum = self.build_health_validation_safety_handoff(save=save)

        status_rows = [
            {"component": "profiles_registry", "status": p_sum["profiles"]["status"], "count": p_sum["profiles"]["total_profiles"]},
            {"component": "domains_registry", "status": p_sum["domains"]["status"], "count": p_sum["domains"]["total_domains"]},
            {"component": "window_contracts", "status": p_sum["window_contracts"]["status"], "count": p_sum["window_contracts"]["total_contracts"]},
            {"component": "parameter_grids", "status": c_sum["parameter_grids"]["status"], "count": c_sum["parameter_grids"]["total_grids"]},
            {"component": "moving_average_grid", "status": w_sum["moving_average"]["status"], "count": w_sum["moving_average"]["total_grid_features"]},
            {"component": "momentum_grid", "status": w_sum["momentum"]["status"], "count": w_sum["momentum"]["total_grid_features"]},
            {"component": "volatility_grid", "status": w_sum["volatility"]["status"], "count": w_sum["volatility"]["total_grid_features"]},
            {"component": "range_channel_grid", "status": w_sum["range_channel"]["status"], "count": w_sum["range_channel"]["total_grid_features"]},
            {"component": "mean_reversion_grid", "status": w_sum["mean_reversion"]["status"], "count": w_sum["mean_reversion"]["total_grid_features"]},
            {"component": "return_grid", "status": w_sum["returns"]["status"], "count": w_sum["returns"]["total_grid_features"]},
            {"component": "computation_rehearsal", "status": r_sum["rehearsal"]["status"], "count": r_sum["rehearsal"]["total_rehearsals"]},
            {"component": "metadata_registry", "status": m_sum["metadata"]["status"], "count": m_sum["metadata"]["total_metadata_entries"]},
            {"component": "health_check", "status": h_sum["health"]["health_status"], "count": h_sum["health"]["total_components"]},
            {"component": "validation_report", "status": h_sum["validation"]["validation_status"], "count": h_sum["validation"]["rules_checked"]},
            {"component": "safety_boundary", "status": h_sum["safety"]["safety_status"], "count": h_sum["safety"]["total_conditions"]},
            {"component": "phase_119_handoff", "status": h_sum["phase_119_handoff"]["handoff_status"], "count": h_sum["phase_119_handoff"]["total_handoff_items"]},
        ]

        df = pd.DataFrame(status_rows)
        summary = {
            "profile": self.profile.name,
            "total_components": len(df),
            "current_phase": self.profile.current_phase,
            "target_final_phase": self.profile.target_final_phase,
            "next_phase": self.profile.next_phase,
            "non_signal": True,
            "status": "OPERATIONAL",
        }
        return df, summary
