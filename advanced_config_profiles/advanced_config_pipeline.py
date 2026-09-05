import os
import pandas as pd
from pathlib import Path
from .advanced_config import AdvancedConfigSystemProfile, get_default_advanced_config_system_profile
from .config_profile_registry import build_advanced_config_profile_registry
from .research_mode_presets import build_research_mode_preset_registry
from .universe_profiles import build_universe_profile_registry
from .timeframe_profiles import build_timeframe_profile_registry
from .asset_class_profiles import build_asset_class_profile_registry
from .strategy_family_profiles import build_strategy_family_profile_registry
from .risk_preference_profiles import build_risk_preference_profile_registry
from .data_provider_preference_profiles import build_data_provider_preference_profile_registry
from .feature_profiles import build_feature_profile_registry
from .regime_profiles import build_regime_profile_registry
from .ml_profiles import build_ml_profile_registry
from .backtest_profiles import build_backtest_profile_registry
from .portfolio_profiles import build_portfolio_profile_registry
from .report_profiles import build_report_profile_registry
from .safety_profiles import build_safety_profile_registry
from .profile_composition import build_composed_research_profile_registry
from .profile_compatibility import build_profile_compatibility_matrix
from .profile_validation import build_profile_validation_report
from .profile_quality import build_profile_quality_report
from .profile_scoring import build_profile_readiness_score_report
from .advanced_config_report_builder import *
from data.storage.data_lake import DataLake

class AdvancedConfigProfilePipeline:
    def __init__(self, data_lake, settings, project_root, profile=None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_advanced_config_system_profile()
        self.registry_df = None
        self.preset_df = None
        self.composed_df = None
        self.compatibility_df = None
        self.validation_df = None
        self.quality = None
        self.score_df = None

    def build_profile_registries(self, save: bool = True) -> tuple[dict, dict]:
        registries = {}
        summaries = {}
        
        funcs = [
            ("main", build_advanced_config_profile_registry),
            ("universe", build_universe_profile_registry),
            ("timeframe", build_timeframe_profile_registry),
            ("asset_class", build_asset_class_profile_registry),
            ("strategy_family", build_strategy_family_profile_registry),
            ("risk_preference", build_risk_preference_profile_registry),
            ("data_provider_preference", build_data_provider_preference_profile_registry),
            ("feature", build_feature_profile_registry),
            ("regime", build_regime_profile_registry),
            ("ml", build_ml_profile_registry),
            ("backtest", build_backtest_profile_registry),
            ("portfolio", build_portfolio_profile_registry),
            ("report", build_report_profile_registry),
            ("safety", build_safety_profile_registry)
        ]
        
        for name, func in funcs:
            df, summary = func(self.profile)
            registries[name] = df
            summaries[name] = summary
        
        self.registry_df = registries["main"]
        if save:
            try:
                self.data_lake.save_advanced_config_profile_registry(self.registry_df, summaries["main"])
                self.data_lake.save_universe_profile_registry(registries["universe"])
                self.data_lake.save_timeframe_profile_registry(registries["timeframe"])
                self.data_lake.save_asset_class_profile_registry(registries["asset_class"])
                self.data_lake.save_strategy_family_profile_registry(registries["strategy_family"])
                self.data_lake.save_risk_preference_profile_registry(registries["risk_preference"])
                self.data_lake.save_data_provider_preference_profile_registry(registries["data_provider_preference"])
                self.data_lake.save_feature_profile_registry(registries["feature"])
                self.data_lake.save_regime_profile_registry(registries["regime"])
                self.data_lake.save_ml_profile_registry(registries["ml"])
                self.data_lake.save_backtest_profile_registry(registries["backtest"])
                self.data_lake.save_portfolio_profile_registry(registries["portfolio"])
                self.data_lake.save_report_profile_registry(registries["report"])
                self.data_lake.save_safety_profile_registry(registries["safety"])
            except Exception as e:
                pass
        return registries, summaries

    def build_research_mode_presets(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        self.preset_df, summary = build_research_mode_preset_registry(self.profile)
        if save:
            try:
                self.data_lake.save_research_mode_preset_registry(self.preset_df, summary)
            except Exception:
                pass
        return self.preset_df, summary

    def build_composed_research_profiles(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        self.composed_df, summary = build_composed_research_profile_registry(self.profile)
        if save:
            try:
                self.data_lake.save_composed_research_profile_registry(self.composed_df, summary)
            except Exception:
                pass
        return self.composed_df, summary

    def build_profile_compatibility_matrix(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        self.compatibility_df, summary = build_profile_compatibility_matrix(self.profile)
        if save:
            try:
                self.data_lake.save_profile_compatibility_matrix(self.compatibility_df, summary)
            except Exception:
                pass
        return self.compatibility_df, summary

    def build_profile_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        self.validation_df, val_summary = build_profile_validation_report(
            {"registry": self.registry_df, "preset": self.preset_df, "composed": self.composed_df}, 
            self.profile
        )
        self.quality = build_profile_quality_report({}, self.registry_df, self.composed_df)
        self.score_df, score_summary = build_profile_readiness_score_report(
            self.registry_df, self.preset_df, self.composed_df, self.compatibility_df, self.validation_df, self.profile
        )
        
        if save:
            try:
                self.data_lake.save_profile_validation_report(self.validation_df, val_summary)
                self.data_lake.save_profile_quality_report(self.profile.name, self.quality)
                self.data_lake.save_profile_readiness_score_report(self.score_df, score_summary)
                
                md = build_profile_quality_markdown_report({}, self.quality)
                self.data_lake.save_advanced_config_report(self.profile.name, {"validation": val_summary, "quality": self.quality}, md)
            except Exception:
                pass
                
        return self.quality, score_summary

    def build_advanced_config_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        status_df = pd.DataFrame([{"module": "Advanced Config", "status": "Generated"}])
        if save:
            try:
                md = build_advanced_config_status_markdown_report({}, status_df)
                self.data_lake.save_advanced_config_report(self.profile.name + "_status", {}, md)
            except Exception:
                pass
        return status_df, {"total": len(status_df)}
