"""Phase 126: Regime Foundation Pipeline Orchestrator.

Coordinates full generation of taxonomies, families, contexts, contracts, validation,
health checks, manifests, and handoff reports with dry-run and DataLake integration.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)
from advanced_regime_foundation.regime_foundation_profile_registry import (
    build_regime_foundation_profile_registry,
)
from advanced_regime_foundation.regime_foundation_domain_registry import (
    build_regime_foundation_domain_registry,
)
from advanced_regime_foundation.market_behavior_taxonomy import (
    build_market_behavior_taxonomy_registry,
)
from advanced_regime_foundation.regime_state_taxonomy import (
    build_regime_state_taxonomy_registry,
)
from advanced_regime_foundation.regime_family_registry import (
    build_regime_family_registry,
)
from advanced_regime_foundation.volatility_regime_families import (
    build_volatility_regime_family_registry,
)
from advanced_regime_foundation.trend_regime_families import (
    build_trend_regime_family_registry,
)
from advanced_regime_foundation.range_regime_families import (
    build_range_regime_family_registry,
)
from advanced_regime_foundation.liquidity_regime_placeholders import (
    build_liquidity_regime_placeholder_registry,
)
from advanced_regime_foundation.macro_regime_context import (
    build_macro_regime_context_registry,
)
from advanced_regime_foundation.event_regime_context import (
    build_event_regime_context_registry,
)
from advanced_regime_foundation.news_metadata_regime_context import (
    build_news_metadata_regime_context_registry,
)
from advanced_regime_foundation.cross_asset_regime_context import (
    build_cross_asset_regime_context_registry,
)
from advanced_regime_foundation.regime_input_feature_contracts import (
    build_regime_input_feature_contract_registry,
)
from advanced_regime_foundation.regime_factor_dependencies import (
    build_regime_factor_dependency_registry,
)
from advanced_regime_foundation.regime_validation_dependencies import (
    build_regime_validation_dependency_registry,
)
from advanced_regime_foundation.regime_quality_dependencies import (
    build_regime_quality_dependency_registry,
)
from advanced_regime_foundation.regime_state_output_schema import (
    build_regime_state_output_schema_registry,
)
from advanced_regime_foundation.regime_namespace_registry import (
    build_regime_namespace_registry,
)
from advanced_regime_foundation.regime_non_signal_policies import (
    build_regime_non_signal_policy_registry,
)
from advanced_regime_foundation.regime_forbidden_claims import (
    build_regime_forbidden_claim_registry,
)
from advanced_regime_foundation.regime_foundation_manifest import (
    build_regime_foundation_manifest,
)
from advanced_regime_foundation.regime_foundation_safety_boundary import (
    build_regime_foundation_safety_boundary,
)
from advanced_regime_foundation.regime_foundation_health import (
    build_regime_foundation_health_check,
)
from advanced_regime_foundation.regime_foundation_validation import (
    build_regime_foundation_validation_report,
)
from advanced_regime_foundation.phase_127_handoff import (
    build_phase_127_regime_feature_matrix_handoff_report,
)


class RegimeFoundationPipeline:
    """Master pipeline coordinating all Phase 126 foundation components."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[RegimeFoundationProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(__file__).resolve().parent.parent
        self.profile = profile or get_default_regime_foundation_profile()

    def build_profiles_domains_taxonomy(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist profile, domain, and behavior taxonomy registries."""
        df_prof, s_prof = build_regime_foundation_profile_registry(self.profile)
        df_dom, s_dom = build_regime_foundation_domain_registry(self.profile)
        df_beh, s_beh = build_market_behavior_taxonomy_registry(self.profile)
        df_state, s_state = build_regime_state_taxonomy_registry(self.profile)

        if save and hasattr(self.data_lake, "save_regime_foundation_profile_registry"):
            self.data_lake.save_regime_foundation_profile_registry(df_prof, s_prof)
            self.data_lake.save_regime_foundation_domain_registry(df_dom, s_dom)
            self.data_lake.save_market_behavior_taxonomy_registry(df_beh, s_beh)
            self.data_lake.save_regime_state_taxonomy_registry(df_state, s_state)

        tables = {
            "profiles": df_prof,
            "domains": df_dom,
            "market_behavior": df_beh,
            "regime_states": df_state,
        }
        summaries = {
            "profiles": s_prof,
            "domains": s_dom,
            "market_behavior": s_beh,
            "regime_states": s_state,
        }
        return tables, summaries

    def build_regime_families(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist master and specialized regime families."""
        df_fam, s_fam = build_regime_family_registry(self.profile)
        df_vol, s_vol = build_volatility_regime_family_registry(self.profile)
        df_trend, s_trend = build_trend_regime_family_registry(self.profile)
        df_range, s_range = build_range_regime_family_registry(self.profile)
        df_liq, s_liq = build_liquidity_regime_placeholder_registry(self.profile)

        if save and hasattr(self.data_lake, "save_regime_family_registry"):
            self.data_lake.save_regime_family_registry(df_fam, s_fam)
            self.data_lake.save_volatility_regime_family_registry(df_vol, s_vol)
            self.data_lake.save_trend_regime_family_registry(df_trend, s_trend)
            self.data_lake.save_range_regime_family_registry(df_range, s_range)
            self.data_lake.save_liquidity_regime_placeholder_registry(df_liq, s_liq)

        tables = {
            "regime_families": df_fam,
            "volatility": df_vol,
            "trend": df_trend,
            "range": df_range,
            "liquidity": df_liq,
        }
        summaries = {
            "regime_families": s_fam,
            "volatility": s_vol,
            "trend": s_trend,
            "range": s_range,
            "liquidity": s_liq,
        }
        return tables, summaries

    def build_context_registries(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist macro, event, news metadata, and cross-asset contexts."""
        df_macro, s_macro = build_macro_regime_context_registry(self.profile)
        df_event, s_event = build_event_regime_context_registry(self.profile)
        df_news, s_news = build_news_metadata_regime_context_registry(self.profile)
        df_cross, s_cross = build_cross_asset_regime_context_registry(self.profile)

        if save and hasattr(self.data_lake, "save_macro_regime_context_registry"):
            self.data_lake.save_macro_regime_context_registry(df_macro, s_macro)
            self.data_lake.save_event_regime_context_registry(df_event, s_event)
            self.data_lake.save_news_metadata_regime_context_registry(df_news, s_news)
            self.data_lake.save_cross_asset_regime_context_registry(df_cross, s_cross)

        tables = {
            "macro": df_macro,
            "event": df_event,
            "news_metadata": df_news,
            "cross_asset": df_cross,
        }
        summaries = {
            "macro": s_macro,
            "event": s_event,
            "news_metadata": s_news,
            "cross_asset": s_cross,
        }
        return tables, summaries

    def build_contracts_dependencies_schema(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist feature contracts, factor/val/qual dependencies, and schema."""
        df_cont, s_cont = build_regime_input_feature_contract_registry(self.profile)
        df_fact, s_fact = build_regime_factor_dependency_registry(self.profile)
        df_val, s_val = build_regime_validation_dependency_registry(self.profile)
        df_qual, s_qual = build_regime_quality_dependency_registry(self.profile)
        df_schema, s_schema = build_regime_state_output_schema_registry(self.profile)
        df_ns, s_ns = build_regime_namespace_registry(self.profile)

        if save and hasattr(self.data_lake, "save_regime_input_feature_contract_registry"):
            self.data_lake.save_regime_input_feature_contract_registry(df_cont, s_cont)
            self.data_lake.save_regime_factor_dependency_registry(df_fact, s_fact)
            self.data_lake.save_regime_validation_dependency_registry(df_val, s_val)
            self.data_lake.save_regime_quality_dependency_registry(df_qual, s_qual)
            self.data_lake.save_regime_state_output_schema_registry(df_schema, s_schema)
            self.data_lake.save_regime_namespace_registry(df_ns, s_ns)

        tables = {
            "contracts": df_cont,
            "factor_dependencies": df_fact,
            "validation_dependencies": df_val,
            "quality_dependencies": df_qual,
            "output_schema": df_schema,
            "namespace": df_ns,
        }
        summaries = {
            "contracts": s_cont,
            "factor_dependencies": s_fact,
            "validation_dependencies": s_val,
            "quality_dependencies": s_qual,
            "output_schema": s_schema,
            "namespace": s_ns,
        }
        return tables, summaries

    def build_manifest_policies(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist policies, forbidden claims, and foundation manifest."""
        df_nsp, s_nsp = build_regime_non_signal_policy_registry(self.profile)
        df_fc, s_fc = build_regime_forbidden_claim_registry(self.profile)
        df_man, s_man = build_regime_foundation_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_regime_non_signal_policy_registry"):
            self.data_lake.save_regime_non_signal_policy_registry(df_nsp, s_nsp)
            self.data_lake.save_regime_forbidden_claim_registry(df_fc, s_fc)
            self.data_lake.save_regime_foundation_manifest(df_man, s_man)

        tables = {
            "non_signal_policies": df_nsp,
            "forbidden_claims": df_fc,
            "manifest": df_man,
        }
        summaries = {
            "non_signal_policies": s_nsp,
            "forbidden_claims": s_fc,
            "manifest": s_man,
        }
        return tables, summaries

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist health, safety boundary, validation, and handoff report."""
        df_health, s_health = build_regime_foundation_health_check(self.project_root, self.profile)
        df_safety, s_safety = build_regime_foundation_safety_boundary(self.profile)
        df_hand, s_hand = build_phase_127_regime_feature_matrix_handoff_report(self.profile)

        # For validation, aggregate essential tables
        t_prof, _ = self.build_profiles_domains_taxonomy(save=False)
        t_fam, _ = self.build_regime_families(save=False)
        t_man, _ = self.build_manifest_policies(save=False)
        val_inputs = {**t_prof, **t_fam, **t_man}

        df_val_rep, s_val_rep = build_regime_foundation_validation_report(val_inputs, self.profile)

        if save and hasattr(self.data_lake, "save_regime_foundation_health_check"):
            self.data_lake.save_regime_foundation_health_check(df_health, s_health)
            self.data_lake.save_regime_foundation_safety_boundary(df_safety, s_safety)
            self.data_lake.save_regime_foundation_validation_report(df_val_rep, s_val_rep)
            self.data_lake.save_phase_127_regime_feature_matrix_handoff_report(df_hand, s_hand)

        tables = {
            "health": df_health,
            "safety": df_safety,
            "validation_report": df_val_rep,
            "handoff": df_hand,
        }
        summaries = {
            "health": s_health,
            "safety": s_safety,
            "validation_report": s_val_rep,
            "handoff": s_hand,
        }
        return tables, summaries

    def build_regime_foundation_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Synthesize overarching system status for Phase 126."""
        t_h, s_h = self.build_health_validation_safety_handoff(save=False)
        t_m, s_m = self.build_manifest_policies(save=False)

        manifest_sum = s_m["manifest"]
        val_sum = s_h["validation_report"]
        health_sum = s_h["health"]
        hand_sum = s_h["handoff"]

        status_rows = [
            {
                "subsystem": "advanced_regime_foundation",
                "phase": 126,
                "target_final_phase": 160,
                "next_phase": 127,
                "profile": self.profile.profile_name,
                "health_status": health_sum.get("health_status", "HEALTHY"),
                "validation_status": val_sum.get("validation_status", "VALIDATION_PASS"),
                "handoff_status": hand_sum.get("handoff_status", "READY"),
                "non_signal": True,
                "model_training_executed": False,
                "clustering_executed": False,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
                "status": "READY",
            }
        ]
        df = pd.DataFrame(status_rows)
        summary = {
            "phase": 126,
            "profile": self.profile.profile_name,
            "overall_status": "READY",
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        }

        if save and hasattr(self.data_lake, "save_regime_foundation_report"):
            self.data_lake.save_regime_foundation_report(self.profile.profile_name, summary)

        return df, summary
