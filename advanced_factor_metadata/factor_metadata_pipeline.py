"""Phase 122 Factor Metadata Pipeline Orchestrator.

Coordinates end-to-end factor taxonomy construction, contract registration,
dependency lineage, safety boundaries, health auditing, and quality handoff generation.
Strictly non-signal and research-only.
"""

from pathlib import Path
from typing import Any, Dict, Tuple
import pandas as pd

from advanced_factor_metadata.calendar_event_factor_families import (
    build_calendar_event_factor_family_registry,
)
from advanced_factor_metadata.composite_factor_placeholders import (
    build_composite_factor_placeholder_registry,
)
from advanced_factor_metadata.cross_asset_context_factor_families import (
    build_cross_asset_context_factor_family_registry,
)
from advanced_factor_metadata.factor_contract_registry import (
    build_factor_contract_registry,
)
from advanced_factor_metadata.factor_dependency_registry import (
    build_factor_dependency_registry,
)
from advanced_factor_metadata.factor_family_registry import (
    build_factor_family_registry,
)
from advanced_factor_metadata.factor_forbidden_claims import (
    build_factor_forbidden_claim_registry,
)
from advanced_factor_metadata.factor_input_feature_sets import (
    build_factor_input_feature_set_registry,
)
from advanced_factor_metadata.factor_manual_review_registry import (
    build_factor_manual_review_registry,
)
from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_domain_registry import (
    build_factor_metadata_domain_registry,
)
from advanced_factor_metadata.factor_metadata_health import (
    build_factor_metadata_health_check,
)
from advanced_factor_metadata.factor_metadata_manifest import (
    build_factor_metadata_manifest,
)
from advanced_factor_metadata.factor_metadata_models import FORBIDDEN_FACTOR_TOKENS
from advanced_factor_metadata.factor_metadata_profile_registry import (
    build_factor_metadata_profile_registry,
)
from advanced_factor_metadata.factor_metadata_report_builder import (
    build_factor_contract_markdown_report,
    build_factor_dependency_markdown_report,
    build_factor_family_markdown_report,
    build_factor_health_markdown_report,
    build_factor_manifest_markdown_report,
    build_factor_metadata_profile_markdown_report,
    build_factor_safety_markdown_report,
    build_factor_validation_markdown_report,
    build_macro_event_news_factor_markdown_report,
    build_phase_123_handoff_markdown_report,
    build_technical_factor_markdown_report,
)
from advanced_factor_metadata.factor_metadata_safety_boundary import (
    build_factor_metadata_safety_boundary,
)
from advanced_factor_metadata.factor_metadata_validation import (
    build_factor_metadata_validation_report,
)
from advanced_factor_metadata.factor_namespace_registry import (
    build_factor_namespace_registry,
)
from advanced_factor_metadata.factor_non_signal_policies import (
    build_factor_non_signal_policy_registry,
)
from advanced_factor_metadata.factor_output_schema import (
    build_factor_output_schema_registry,
)
from advanced_factor_metadata.factor_quality_dependencies import (
    build_factor_quality_dependency_registry,
)
from advanced_factor_metadata.factor_validation_dependencies import (
    build_factor_validation_dependency_registry,
)
from advanced_factor_metadata.macro_context_factor_families import (
    build_macro_context_factor_family_registry,
)
from advanced_factor_metadata.mean_reversion_factor_families import (
    build_mean_reversion_factor_family_registry,
)
from advanced_factor_metadata.momentum_factor_families import (
    build_momentum_factor_family_registry,
)
from advanced_factor_metadata.news_attention_factor_families import (
    build_news_attention_factor_family_registry,
)
from advanced_factor_metadata.phase_123_handoff import (
    build_phase_123_feature_quality_drift_handoff_report,
)
from advanced_factor_metadata.quote_microstructure_factor_placeholders import (
    build_quote_microstructure_factor_placeholder_registry,
)
from advanced_factor_metadata.regime_prep_factor_placeholders import (
    build_regime_prep_factor_placeholder_registry,
)
from advanced_factor_metadata.return_factor_families import (
    build_return_factor_family_registry,
)
from advanced_factor_metadata.technical_factor_families import (
    build_technical_factor_family_registry,
)
from advanced_factor_metadata.trend_factor_families import (
    build_trend_factor_family_registry,
)
from advanced_factor_metadata.volatility_factor_families import (
    build_volatility_factor_family_registry,
)


class FactorMetadataPipeline:
    """Master Pipeline for Phase 122 Factor Metadata and Factor Families Layer."""

    def __init__(
        self,
        data_lake: Any,
        settings: Any,
        project_root: Path,
        profile: FactorMetadataProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = Path(project_root)
        self.profile = profile or get_default_factor_metadata_profile()

    def build_profiles_domains_families(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build profile, domain, and family registries."""
        df_prof, s_prof = build_factor_metadata_profile_registry(self.profile)
        df_dom, s_dom = build_factor_metadata_domain_registry(self.profile)
        df_fam, s_fam = build_factor_family_registry(self.profile)

        if save and self.data_lake:
            self.data_lake.save_factor_metadata_profile_registry(df_prof, s_prof)
            self.data_lake.save_factor_metadata_domain_registry(df_dom, s_dom)
            self.data_lake.save_factor_family_registry(df_fam, s_fam)

        dfs = {"profiles": df_prof, "domains": df_dom, "families": df_fam}
        summaries = {"profiles": s_prof, "domains": s_dom, "families": s_fam}
        return dfs, summaries

    def build_contracts_namespace_schema(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build contract, input feature set, namespace, and output schema registries."""
        df_cntr, s_cntr = build_factor_contract_registry(self.profile)
        df_fset, s_fset = build_factor_input_feature_set_registry(self.profile)
        df_ns, s_ns = build_factor_namespace_registry(self.profile)
        df_sch, s_sch = build_factor_output_schema_registry(self.profile)

        if save and self.data_lake:
            self.data_lake.save_factor_contract_registry(df_cntr, s_cntr)
            self.data_lake.save_factor_input_feature_set_registry(df_fset, s_fset)
            self.data_lake.save_factor_namespace_registry(df_ns, s_ns)
            self.data_lake.save_factor_output_schema_registry(df_sch, s_sch)

        dfs = {"contracts": df_cntr, "input_feature_sets": df_fset, "namespaces": df_ns, "schemas": df_sch}
        summaries = {"contracts": s_cntr, "input_feature_sets": s_fset, "namespaces": s_ns, "schemas": s_sch}
        return dfs, summaries

    def build_dependencies(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build general dependencies, validation dependencies, and quality dependencies."""
        df_dep, s_dep = build_factor_dependency_registry(self.profile)
        df_vdep, s_vdep = build_factor_validation_dependency_registry(self.profile)
        df_qdep, s_qdep = build_factor_quality_dependency_registry(self.profile)

        if save and self.data_lake:
            self.data_lake.save_factor_dependency_registry(df_dep, s_dep)
            self.data_lake.save_factor_validation_dependency_registry(df_vdep, s_vdep)
            self.data_lake.save_factor_quality_dependency_registry(df_qdep, s_qdep)

        dfs = {"dependencies": df_dep, "validation_dependencies": df_vdep, "quality_dependencies": df_qdep}
        summaries = {"dependencies": s_dep, "validation_dependencies": s_vdep, "quality_dependencies": s_qdep}
        return dfs, summaries

    def build_technical_factor_families(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build technical, trend, momentum, volatility, mean-reversion, return, and quote registries."""
        df_tech, s_tech = build_technical_factor_family_registry(self.profile)
        df_trend, s_trend = build_trend_factor_family_registry(self.profile)
        df_mom, s_mom = build_momentum_factor_family_registry(self.profile)
        df_vol, s_vol = build_volatility_factor_family_registry(self.profile)
        df_mr, s_mr = build_mean_reversion_factor_family_registry(self.profile)
        df_ret, s_ret = build_return_factor_family_registry(self.profile)
        df_quote, s_quote = build_quote_microstructure_factor_placeholder_registry(self.profile)

        if save and self.data_lake:
            self.data_lake.save_technical_factor_family_registry(df_tech, s_tech)
            self.data_lake.save_trend_factor_family_registry(df_trend, s_trend)
            self.data_lake.save_momentum_factor_family_registry(df_mom, s_mom)
            self.data_lake.save_volatility_factor_family_registry(df_vol, s_vol)
            self.data_lake.save_mean_reversion_factor_family_registry(df_mr, s_mr)
            self.data_lake.save_return_factor_family_registry(df_ret, s_ret)
            self.data_lake.save_quote_microstructure_factor_placeholder_registry(df_quote, s_quote)

        dfs = {
            "technical": df_tech,
            "trend": df_trend,
            "momentum": df_mom,
            "volatility": df_vol,
            "mean_reversion": df_mr,
            "returns": df_ret,
            "quote_microstructure": df_quote,
        }
        summaries = {
            "technical": s_tech,
            "trend": s_trend,
            "momentum": s_mom,
            "volatility": s_vol,
            "mean_reversion": s_mr,
            "returns": s_ret,
            "quote_microstructure": s_quote,
        }
        return dfs, summaries

    def build_macro_event_news_cross_asset_families(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build macro, calendar event, news attention, cross-asset, regime-prep, and composite registries."""
        df_macro, s_macro = build_macro_context_factor_family_registry(self.profile)
        df_event, s_event = build_calendar_event_factor_family_registry(self.profile)
        df_news, s_news = build_news_attention_factor_family_registry(self.profile)
        df_cross, s_cross = build_cross_asset_context_factor_family_registry(self.profile)
        df_regime, s_regime = build_regime_prep_factor_placeholder_registry(self.profile)
        df_comp, s_comp = build_composite_factor_placeholder_registry(self.profile)

        if save and self.data_lake:
            self.data_lake.save_macro_context_factor_family_registry(df_macro, s_macro)
            self.data_lake.save_calendar_event_factor_family_registry(df_event, s_event)
            self.data_lake.save_news_attention_factor_family_registry(df_news, s_news)
            self.data_lake.save_cross_asset_context_factor_family_registry(df_cross, s_cross)
            self.data_lake.save_regime_prep_factor_placeholder_registry(df_regime, s_regime)
            self.data_lake.save_composite_factor_placeholder_registry(df_comp, s_comp)

        dfs = {
            "macro_context": df_macro,
            "calendar_event": df_event,
            "news_attention": df_news,
            "cross_asset_context": df_cross,
            "regime_prep": df_regime,
            "composite": df_comp,
        }
        summaries = {
            "macro_context": s_macro,
            "calendar_event": s_event,
            "news_attention": s_news,
            "cross_asset_context": s_cross,
            "regime_prep": s_regime,
            "composite": s_comp,
        }
        return dfs, summaries

    def build_manifest_review_policies(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build factor manifest, manual review queue, non-signal policies, and forbidden claims."""
        df_manf, s_manf = build_factor_metadata_manifest(self.profile)
        df_rev, s_rev = build_factor_manual_review_registry(self.profile)
        df_nsp, s_nsp = build_factor_non_signal_policy_registry(self.profile)
        df_fc, s_fc = build_factor_forbidden_claim_registry(self.profile)

        if save and self.data_lake:
            self.data_lake.save_factor_metadata_manifest(df_manf, s_manf)
            self.data_lake.save_factor_manual_review_registry(df_rev, s_rev)
            self.data_lake.save_factor_non_signal_policy_registry(df_nsp, s_nsp)
            self.data_lake.save_factor_forbidden_claim_registry(df_fc, s_fc)

        dfs = {
            "manifest": df_manf,
            "manual_review": df_rev,
            "non_signal_policies": df_nsp,
            "forbidden_claims": df_fc,
        }
        summaries = {
            "manifest": s_manf,
            "manual_review": s_rev,
            "non_signal_policies": s_nsp,
            "forbidden_claims": s_fc,
        }
        return dfs, summaries

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build health check, safety boundary, validation report, and Phase 123 handoff."""
        df_health, s_health = build_factor_metadata_health_check(self.project_root, self.profile)
        df_safety, s_safety = build_factor_metadata_safety_boundary(self.profile)
        df_handoff, s_handoff = build_phase_123_feature_quality_drift_handoff_report(self.profile)

        # Collect registries for validation report
        df_prof, s_prof = build_factor_metadata_profile_registry(self.profile)
        df_fam, s_fam = build_factor_family_registry(self.profile)
        df_cntr, s_cntr = build_factor_contract_registry(self.profile)
        df_ns, s_ns = build_factor_namespace_registry(self.profile)
        df_sch, s_sch = build_factor_output_schema_registry(self.profile)
        df_manf, s_manf = build_factor_metadata_manifest(self.profile)

        tables_to_validate = {
            "profiles": df_prof,
            "families": df_fam,
            "contracts": df_cntr,
            "namespaces": df_ns,
            "schemas": df_sch,
            "manifests": df_manf,
        }
        df_val, s_val = build_factor_metadata_validation_report(tables_to_validate, self.profile)

        if save and self.data_lake:
            self.data_lake.save_factor_health_check(df_health, s_health)
            self.data_lake.save_factor_safety_boundary(df_safety, s_safety)
            self.data_lake.save_factor_validation_report(df_val, s_val)
            self.data_lake.save_phase_123_feature_quality_drift_handoff_report(df_handoff, s_handoff)

            # Save Markdown reports
            md_prof = build_factor_metadata_profile_markdown_report(s_prof, df_prof)
            md_fam = build_factor_family_markdown_report(s_fam, df_fam)
            md_cntr = build_factor_contract_markdown_report(s_cntr, df_cntr)
            md_val = build_factor_validation_markdown_report(s_val, df_val)
            md_health = build_factor_health_markdown_report(s_health, df_health)
            md_safety = build_factor_safety_markdown_report(s_safety, df_safety)
            md_handoff = build_phase_123_handoff_markdown_report(s_handoff, df_handoff)

            full_report = {
                "profile": s_prof,
                "families": s_fam,
                "contracts": s_cntr,
                "validation": s_val,
                "health": s_health,
                "safety": s_safety,
                "handoff": s_handoff,
            }
            self.data_lake.save_factor_metadata_report(
                self.profile.name,
                full_report,
                f"{md_prof}\n\n---\n\n{md_fam}\n\n---\n\n{md_cntr}\n\n---\n\n{md_val}\n\n---\n\n{md_health}\n\n---\n\n{md_safety}\n\n---\n\n{md_handoff}",
            )

        dfs = {
            "health": df_health,
            "safety": df_safety,
            "validation": df_val,
            "handoff": df_handoff,
        }
        summaries = {
            "health": s_health,
            "safety": s_safety,
            "validation": s_val,
            "handoff": s_handoff,
        }
        return dfs, summaries

    def build_factor_metadata_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Consolidate high-level status across all factor metadata components."""
        p_dfs, p_sums = self.build_profiles_domains_families(save=save)
        c_dfs, c_sums = self.build_contracts_namespace_schema(save=save)
        d_dfs, d_sums = self.build_dependencies(save=save)
        t_dfs, t_sums = self.build_technical_factor_families(save=save)
        m_dfs, m_sums = self.build_macro_event_news_cross_asset_families(save=save)
        f_dfs, f_sums = self.build_manifest_review_policies(save=save)
        h_dfs, h_sums = self.build_health_validation_safety_handoff(save=save)

        status_rows = [
            {"component": "Profiles Registry", "count": len(p_dfs["profiles"]), "status": p_sums["profiles"]["status"]},
            {"component": "Domains Registry", "count": len(p_dfs["domains"]), "status": p_sums["domains"]["status"]},
            {"component": "Families Registry", "count": len(p_dfs["families"]), "status": p_sums["families"]["status"]},
            {"component": "Contracts Registry", "count": len(c_dfs["contracts"]), "status": c_sums["contracts"]["status"]},
            {"component": "Input Feature Sets", "count": len(c_dfs["input_feature_sets"]), "status": c_sums["input_feature_sets"]["status"]},
            {"component": "Namespace Registry", "count": len(c_dfs["namespaces"]), "status": c_sums["namespaces"]["status"]},
            {"component": "Output Schema", "count": len(c_dfs["schemas"]), "status": c_sums["schemas"]["status"]},
            {"component": "Factor Dependencies", "count": len(d_dfs["dependencies"]), "status": d_sums["dependencies"]["status"]},
            {"component": "Validation Dependencies", "count": len(d_dfs["validation_dependencies"]), "status": d_sums["validation_dependencies"]["status"]},
            {"component": "Quality Dependencies", "count": len(d_dfs["quality_dependencies"]), "status": d_sums["quality_dependencies"]["status"]},
            {"component": "Technical Factors", "count": len(t_dfs["technical"]), "status": t_sums["technical"]["status"]},
            {"component": "Trend Factors", "count": len(t_dfs["trend"]), "status": t_sums["trend"]["status"]},
            {"component": "Momentum Factors", "count": len(t_dfs["momentum"]), "status": t_sums["momentum"]["status"]},
            {"component": "Volatility Factors", "count": len(t_dfs["volatility"]), "status": t_sums["volatility"]["status"]},
            {"component": "Mean Reversion Factors", "count": len(t_dfs["mean_reversion"]), "status": t_sums["mean_reversion"]["status"]},
            {"component": "Return Factors", "count": len(t_dfs["returns"]), "status": t_sums["returns"]["status"]},
            {"component": "Quote Microstructure", "count": len(t_dfs["quote_microstructure"]), "status": t_sums["quote_microstructure"]["status"]},
            {"component": "Macro Context Factors", "count": len(m_dfs["macro_context"]), "status": m_sums["macro_context"]["status"]},
            {"component": "Calendar Event Factors", "count": len(m_dfs["calendar_event"]), "status": m_sums["calendar_event"]["status"]},
            {"component": "News Attention Factors", "count": len(m_dfs["news_attention"]), "status": m_sums["news_attention"]["status"]},
            {"component": "Cross-Asset Context", "count": len(m_dfs["cross_asset_context"]), "status": m_sums["cross_asset_context"]["status"]},
            {"component": "Regime Prep Placeholders", "count": len(m_dfs["regime_prep"]), "status": m_sums["regime_prep"]["status"]},
            {"component": "Composite Placeholders", "count": len(m_dfs["composite"]), "status": m_sums["composite"]["status"]},
            {"component": "Factor Manifest", "count": len(f_dfs["manifest"]), "status": f_sums["manifest"]["status"]},
            {"component": "Manual Review Queue", "count": len(f_dfs["manual_review"]), "status": f_sums["manual_review"]["status"]},
            {"component": "Non-Signal Policies", "count": len(f_dfs["non_signal_policies"]), "status": f_sums["non_signal_policies"]["status"]},
            {"component": "Forbidden Claims", "count": len(f_dfs["forbidden_claims"]), "status": f_sums["forbidden_claims"]["status"]},
            {"component": "Health Check", "count": len(h_dfs["health"]), "status": h_sums["health"]["health_status"]},
            {"component": "Validation Report", "count": len(h_dfs["validation"]), "status": h_sums["validation"]["status"]},
            {"component": "Safety Boundary", "count": len(h_dfs["safety"]), "status": h_sums["safety"]["safety_status"]},
            {"component": "Phase 123 Handoff", "count": len(h_dfs["handoff"]), "status": h_sums["handoff"]["handoff_status"]},
        ]

        status_df = pd.DataFrame(status_rows)
        summary = {
            "active_profile": self.profile.name,
            "total_components": len(status_rows),
            "current_phase": 122,
            "target_final_phase": 160,
            "next_phase": 123,
            "non_signal": True,
            "status": "factor_ready",
        }
        return status_df, summary
