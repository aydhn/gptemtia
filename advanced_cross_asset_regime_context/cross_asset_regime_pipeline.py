"""Phase 131: Cross-Asset Regime Pipeline.

Master pipeline orchestrating profiles, domains, entities, pairs, relationship taxonomy,
FX/Commodity/Macro/Calendar/News contexts, transition alignment, volatility/trend/range linkages,
divergence/convergence diagnostics, correlation/lead-lag placeholders, contracts, timestamp policies,
asof join policies, no-lookahead guards, dependencies, findings, scoring, manifest, health, validation,
safety boundaries, and Phase 132 handoff.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
    get_cross_asset_regime_profile,
)
from advanced_cross_asset_regime_context.cross_asset_regime_profile_registry import (
    build_cross_asset_regime_profile_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_domain_registry import (
    build_cross_asset_regime_domain_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_entities import (
    build_cross_asset_regime_entity_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_pairs import (
    build_cross_asset_regime_pair_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_relationship_taxonomy import (
    build_cross_asset_regime_relationship_taxonomy_registry,
)
from advanced_cross_asset_regime_context.fx_commodity_regime_context import (
    build_fx_commodity_regime_context_registry,
)
from advanced_cross_asset_regime_context.fx_macro_regime_context import (
    build_fx_macro_regime_context_registry,
)
from advanced_cross_asset_regime_context.commodity_macro_regime_context import (
    build_commodity_macro_regime_context_registry,
)
from advanced_cross_asset_regime_context.macro_calendar_cross_asset_context import (
    build_macro_calendar_cross_asset_context_registry,
)
from advanced_cross_asset_regime_context.calendar_news_cross_asset_context import (
    build_calendar_news_cross_asset_context_registry,
)
from advanced_cross_asset_regime_context.cross_asset_transition_alignment import (
    build_cross_asset_transition_alignment_registry,
)
from advanced_cross_asset_regime_context.cross_asset_volatility_linkage import (
    build_cross_asset_volatility_linkage_registry,
)
from advanced_cross_asset_regime_context.cross_asset_trend_linkage import (
    build_cross_asset_trend_linkage_registry,
)
from advanced_cross_asset_regime_context.cross_asset_range_linkage import (
    build_cross_asset_range_linkage_registry,
)
from advanced_cross_asset_regime_context.cross_asset_divergence_context import (
    build_cross_asset_divergence_context_registry,
)
from advanced_cross_asset_regime_context.cross_asset_convergence_context import (
    build_cross_asset_convergence_context_registry,
)
from advanced_cross_asset_regime_context.cross_asset_correlation_placeholders import (
    build_cross_asset_correlation_placeholder_registry,
)
from advanced_cross_asset_regime_context.cross_asset_lead_lag_placeholders import (
    build_cross_asset_lead_lag_placeholder_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_context_contracts import (
    build_cross_asset_regime_context_contract_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_timestamp_policies import (
    build_cross_asset_regime_timestamp_policy_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_asof_join_policies import (
    build_cross_asset_regime_asof_join_policy_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_no_lookahead_guard import (
    build_cross_asset_regime_no_lookahead_guard_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_validation_dependencies import (
    build_cross_asset_regime_validation_dependency_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_quality_dependencies import (
    build_cross_asset_regime_quality_dependency_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_source_phases import (
    build_cross_asset_regime_source_phase_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_manual_review import (
    build_cross_asset_regime_manual_review_queue,
)
from advanced_cross_asset_regime_context.cross_asset_regime_context_findings import (
    build_cross_asset_regime_context_findings_registry,
)
from advanced_cross_asset_regime_context.cross_asset_regime_context_scoring import (
    build_cross_asset_regime_context_score_report,
)
from advanced_cross_asset_regime_context.cross_asset_regime_context_manifest import (
    build_cross_asset_regime_context_manifest,
)
from advanced_cross_asset_regime_context.cross_asset_regime_health import (
    build_cross_asset_regime_health_check,
)
from advanced_cross_asset_regime_context.cross_asset_regime_validation import (
    build_cross_asset_regime_validation_report,
)
from advanced_cross_asset_regime_context.cross_asset_regime_safety_boundary import (
    build_cross_asset_regime_safety_boundary,
)
from advanced_cross_asset_regime_context.phase_132_handoff import (
    build_phase_132_macro_event_news_regime_context_handoff_report,
)
from advanced_cross_asset_regime_context.cross_asset_regime_report_builder import (
    build_cross_asset_regime_profile_markdown_report,
    build_cross_asset_entity_pair_markdown_report,
    build_cross_asset_relationship_taxonomy_markdown_report,
    build_fx_commodity_context_markdown_report,
    build_macro_calendar_news_context_markdown_report,
    build_cross_asset_linkage_markdown_report,
    build_divergence_convergence_markdown_report,
    build_cross_asset_findings_markdown_report,
    build_cross_asset_score_markdown_report,
    build_cross_asset_manifest_markdown_report,
    build_cross_asset_validation_markdown_report,
    build_cross_asset_safety_markdown_report,
    build_phase_132_handoff_markdown_report,
)


class CrossAssetRegimePipeline:
    """Master pipeline orchestrating Phase 131 Cross-Asset Regime Context Expansion."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[CrossAssetRegimeProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(__file__).resolve().parent.parent
        self.profile = profile or get_default_cross_asset_regime_profile()

    def build_profiles_domains_entities(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 1: Build profiles, domains, entities, pairs, and relationship taxonomy."""
        df_prof, s_prof = build_cross_asset_regime_profile_registry(self.profile)
        df_dom, s_dom = build_cross_asset_regime_domain_registry(self.profile)
        df_ent, s_ent = build_cross_asset_regime_entity_registry(self.profile)
        df_pair, s_pair = build_cross_asset_regime_pair_registry(self.profile)
        df_tax, s_tax = build_cross_asset_regime_relationship_taxonomy_registry(self.profile)

        if save and hasattr(self.data_lake, "save_cross_asset_regime_profile_registry"):
            self.data_lake.save_cross_asset_regime_profile_registry(df_prof, s_prof)
            self.data_lake.save_cross_asset_regime_domain_registry(df_dom, s_dom)
            self.data_lake.save_cross_asset_regime_entity_registry(df_ent, s_ent)
            self.data_lake.save_cross_asset_regime_pair_registry(df_pair, s_pair)
            self.data_lake.save_cross_asset_regime_relationship_taxonomy_registry(df_tax, s_tax)

        dfs = {
            "profiles": df_prof,
            "domains": df_dom,
            "entities": df_ent,
            "pairs": df_pair,
            "taxonomy": df_tax,
        }
        summaries = {
            "profiles": s_prof,
            "domains": s_dom,
            "entities": s_ent,
            "pairs": s_pair,
            "taxonomy": s_tax,
        }
        return dfs, summaries

    def build_context_registries(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 2: Build FX/commodity, FX/macro, commodity/macro, macro/calendar, calendar/news contexts."""
        df_fxc, s_fxc = build_fx_commodity_regime_context_registry(self.profile)
        df_fxm, s_fxm = build_fx_macro_regime_context_registry(self.profile)
        df_cmdm, s_cmdm = build_commodity_macro_regime_context_registry(self.profile)
        df_mcal, s_mcal = build_macro_calendar_cross_asset_context_registry(self.profile)
        df_calnews, s_calnews = build_calendar_news_cross_asset_context_registry(self.profile)

        if save and hasattr(self.data_lake, "save_fx_commodity_regime_context_registry"):
            self.data_lake.save_fx_commodity_regime_context_registry(df_fxc, s_fxc)
            self.data_lake.save_fx_macro_regime_context_registry(df_fxm, s_fxm)
            self.data_lake.save_commodity_macro_regime_context_registry(df_cmdm, s_cmdm)
            self.data_lake.save_macro_calendar_cross_asset_context_registry(df_mcal, s_mcal)
            self.data_lake.save_calendar_news_cross_asset_context_registry(df_calnews, s_calnews)

        dfs = {
            "fx_commodity": df_fxc,
            "fx_macro": df_fxm,
            "commodity_macro": df_cmdm,
            "macro_calendar": df_mcal,
            "calendar_news": df_calnews,
        }
        summaries = {
            "fx_commodity": s_fxc,
            "fx_macro": s_fxm,
            "commodity_macro": s_cmdm,
            "macro_calendar": s_mcal,
            "calendar_news": s_calnews,
        }
        return dfs, summaries

    def build_linkage_reports(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 3: Build transition alignment, volatility/trend/range linkages, divergence/convergence, correlation/lead-lag."""
        df_trans, s_trans = build_cross_asset_transition_alignment_registry(self.profile)
        df_vol, s_vol = build_cross_asset_volatility_linkage_registry(self.profile)
        df_trend, s_trend = build_cross_asset_trend_linkage_registry(self.profile)
        df_range, s_range = build_cross_asset_range_linkage_registry(self.profile)
        df_div, s_div = build_cross_asset_divergence_context_registry(self.profile)
        df_conv, s_conv = build_cross_asset_convergence_context_registry(self.profile)
        df_corr, s_corr = build_cross_asset_correlation_placeholder_registry(self.profile)
        df_leadlag, s_leadlag = build_cross_asset_lead_lag_placeholder_registry(self.profile)

        if save and hasattr(self.data_lake, "save_cross_asset_transition_alignment_registry"):
            self.data_lake.save_cross_asset_transition_alignment_registry(df_trans, s_trans)
            self.data_lake.save_cross_asset_volatility_linkage_registry(df_vol, s_vol)
            self.data_lake.save_cross_asset_trend_linkage_registry(df_trend, s_trend)
            self.data_lake.save_cross_asset_range_linkage_registry(df_range, s_range)
            self.data_lake.save_cross_asset_divergence_context_registry(df_div, s_div)
            self.data_lake.save_cross_asset_convergence_context_registry(df_conv, s_conv)
            self.data_lake.save_cross_asset_correlation_placeholder_registry(df_corr, s_corr)
            self.data_lake.save_cross_asset_lead_lag_placeholder_registry(df_leadlag, s_leadlag)

        dfs = {
            "transition_alignment": df_trans,
            "volatility_linkage": df_vol,
            "trend_linkage": df_trend,
            "range_linkage": df_range,
            "divergence": df_div,
            "convergence": df_conv,
            "correlation": df_corr,
            "lead_lag": df_leadlag,
        }
        summaries = {
            "transition_alignment": s_trans,
            "volatility_linkage": s_vol,
            "trend_linkage": s_trend,
            "range_linkage": s_range,
            "divergence": s_div,
            "convergence": s_conv,
            "correlation": s_corr,
            "lead_lag": s_leadlag,
        }
        return dfs, summaries

    def build_contracts_alignment_guards(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 4: Build contracts, timestamp policies, asof join policies, and no-lookahead guards."""
        df_cont, s_cont = build_cross_asset_regime_context_contract_registry(self.profile)
        df_ts, s_ts = build_cross_asset_regime_timestamp_policy_registry(self.profile)
        df_asof, s_asof = build_cross_asset_regime_asof_join_policy_registry(self.profile)
        df_guard, s_guard = build_cross_asset_regime_no_lookahead_guard_registry(self.profile)

        if save and hasattr(self.data_lake, "save_cross_asset_regime_context_contract_registry"):
            self.data_lake.save_cross_asset_regime_context_contract_registry(df_cont, s_cont)
            self.data_lake.save_cross_asset_regime_timestamp_policy_registry(df_ts, s_ts)
            self.data_lake.save_cross_asset_regime_asof_join_policy_registry(df_asof, s_asof)
            self.data_lake.save_cross_asset_regime_no_lookahead_guard_registry(df_guard, s_guard)

        dfs = {
            "contracts": df_cont,
            "timestamp_policies": df_ts,
            "asof_join_policies": df_asof,
            "no_lookahead_guard": df_guard,
        }
        summaries = {
            "contracts": s_cont,
            "timestamp_policies": s_ts,
            "asof_join_policies": s_asof,
            "no_lookahead_guard": s_guard,
        }
        return dfs, summaries

    def build_dependencies_findings_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 5: Build validation/quality dependencies, source phases, findings, review queue, scores, manifest."""
        df_val_dep, s_val_dep = build_cross_asset_regime_validation_dependency_registry(self.profile)
        df_qual_dep, s_qual_dep = build_cross_asset_regime_quality_dependency_registry(self.profile)
        df_src, s_src = build_cross_asset_regime_source_phase_registry(self.profile)
        df_find, s_find = build_cross_asset_regime_context_findings_registry(self.profile)
        df_rev, s_rev = build_cross_asset_regime_manual_review_queue(self.profile)
        df_score, s_score = build_cross_asset_regime_context_score_report(self.profile)
        df_man, s_man = build_cross_asset_regime_context_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_cross_asset_regime_validation_dependency_registry"):
            self.data_lake.save_cross_asset_regime_validation_dependency_registry(df_val_dep, s_val_dep)
            self.data_lake.save_cross_asset_regime_quality_dependency_registry(df_qual_dep, s_qual_dep)
            self.data_lake.save_cross_asset_regime_source_phase_registry(df_src, s_src)
            self.data_lake.save_cross_asset_regime_context_findings_registry(df_find, s_find)
            self.data_lake.save_cross_asset_regime_manual_review_queue(df_rev, s_rev)
            self.data_lake.save_cross_asset_regime_context_score_report(df_score, s_score)
            self.data_lake.save_cross_asset_regime_context_manifest(df_man, s_man)

        dfs = {
            "validation_dependencies": df_val_dep,
            "quality_dependencies": df_qual_dep,
            "source_phases": df_src,
            "findings": df_find,
            "manual_review": df_rev,
            "scoring": df_score,
            "manifest": df_man,
        }
        summaries = {
            "validation_dependencies": s_val_dep,
            "quality_dependencies": s_qual_dep,
            "source_phases": s_src,
            "findings": s_find,
            "manual_review": s_rev,
            "scoring": s_score,
            "manifest": s_man,
        }
        return dfs, summaries

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 6: Build health check, validation report, safety boundary, and Phase 132 handoff."""
        df_hlth, s_hlth = build_cross_asset_regime_health_check(self.project_root, self.profile)
        df_safe, s_safe = build_cross_asset_regime_safety_boundary(self.profile)
        df_hand, s_hand = build_phase_132_macro_event_news_regime_context_handoff_report(self.profile)

        # Validation requires cross-table checking
        tables_to_validate = {
            "profiles": build_cross_asset_regime_profile_registry(self.profile)[0],
            "pairs": build_cross_asset_regime_pair_registry(self.profile)[0],
            "contracts": build_cross_asset_regime_context_contract_registry(self.profile)[0],
            "manifest": build_cross_asset_regime_context_manifest(self.profile)[0],
        }
        df_val, s_val = build_cross_asset_regime_validation_report(tables_to_validate, self.profile)

        if save and hasattr(self.data_lake, "save_cross_asset_regime_health_check"):
            self.data_lake.save_cross_asset_regime_health_check(df_hlth, s_hlth)
            self.data_lake.save_cross_asset_regime_safety_boundary(df_safe, s_safe)
            self.data_lake.save_cross_asset_regime_validation_report(df_val, s_val)
            self.data_lake.save_phase_132_macro_event_news_regime_context_handoff_report(df_hand, s_hand)

        dfs = {
            "health": df_hlth,
            "validation": df_val,
            "safety": df_safe,
            "handoff": df_hand,
        }
        summaries = {
            "health": s_hlth,
            "validation": s_val,
            "safety": s_safe,
            "handoff": s_hand,
        }
        return dfs, summaries

    def build_cross_asset_regime_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Build high-level master status report across all Phase 131 deliverables."""
        d1, s1 = self.build_profiles_domains_entities(save=save)
        d2, s2 = self.build_context_registries(save=save)
        d3, s3 = self.build_linkage_reports(save=save)
        d4, s4 = self.build_contracts_alignment_guards(save=save)
        d5, s5 = self.build_dependencies_findings_scoring_manifest(save=save)
        d6, s6 = self.build_health_validation_safety_handoff(save=save)

        status_rows = [
            {"component": "profiles", "items": len(d1["profiles"]), "status": "READY", "non_signal": True},
            {"component": "domains", "items": len(d1["domains"]), "status": "READY", "non_signal": True},
            {"component": "entities", "items": len(d1["entities"]), "status": "READY", "non_signal": True},
            {"component": "pairs", "items": len(d1["pairs"]), "status": "READY", "non_signal": True},
            {"component": "taxonomy", "items": len(d1["taxonomy"]), "status": "READY", "non_signal": True},
            {"component": "fx_commodity_context", "items": len(d2["fx_commodity"]), "status": "READY", "non_signal": True},
            {"component": "fx_macro_context", "items": len(d2["fx_macro"]), "status": "READY", "non_signal": True},
            {"component": "commodity_macro_context", "items": len(d2["commodity_macro"]), "status": "READY", "non_signal": True},
            {"component": "macro_calendar_context", "items": len(d2["macro_calendar"]), "status": "READY", "non_signal": True},
            {"component": "calendar_news_context", "items": len(d2["calendar_news"]), "status": "READY", "non_signal": True},
            {"component": "transition_alignment", "items": len(d3["transition_alignment"]), "status": "READY", "non_signal": True},
            {"component": "volatility_linkage", "items": len(d3["volatility_linkage"]), "status": "READY", "non_signal": True},
            {"component": "trend_linkage", "items": len(d3["trend_linkage"]), "status": "READY", "non_signal": True},
            {"component": "range_linkage", "items": len(d3["range_linkage"]), "status": "READY", "non_signal": True},
            {"component": "divergence", "items": len(d3["divergence"]), "status": "READY", "non_signal": True},
            {"component": "convergence", "items": len(d3["convergence"]), "status": "READY", "non_signal": True},
            {"component": "correlation_placeholders", "items": len(d3["correlation"]), "status": "READY", "non_signal": True},
            {"component": "lead_lag_placeholders", "items": len(d3["lead_lag"]), "status": "READY", "non_signal": True},
            {"component": "contracts", "items": len(d4["contracts"]), "status": "READY", "non_signal": True},
            {"component": "timestamp_policies", "items": len(d4["timestamp_policies"]), "status": "READY", "non_signal": True},
            {"component": "asof_join_policies", "items": len(d4["asof_join_policies"]), "status": "READY", "non_signal": True},
            {"component": "no_lookahead_guard", "items": len(d4["no_lookahead_guard"]), "status": "READY", "non_signal": True},
            {"component": "validation_dependencies", "items": len(d5["validation_dependencies"]), "status": "READY", "non_signal": True},
            {"component": "quality_dependencies", "items": len(d5["quality_dependencies"]), "status": "READY", "non_signal": True},
            {"component": "source_phases", "items": len(d5["source_phases"]), "status": "READY", "non_signal": True},
            {"component": "findings", "items": len(d5["findings"]), "status": "READY", "non_signal": True},
            {"component": "manual_review", "items": len(d5["manual_review"]), "status": "READY", "non_signal": True},
            {"component": "scoring", "items": len(d5["scoring"]), "status": "READY", "non_signal": True},
            {"component": "manifest", "items": len(d5["manifest"]), "status": "READY", "non_signal": True},
            {"component": "health", "items": len(d6["health"]), "status": s6["health"]["overall_status"], "non_signal": True},
            {"component": "validation", "items": len(d6["validation"]), "status": s6["validation"]["validation_status"], "non_signal": True},
            {"component": "safety", "items": len(d6["safety"]), "status": s6["safety"]["safety_status"], "non_signal": True},
            {"component": "phase_132_handoff", "items": len(d6["handoff"]), "status": s6["handoff"]["handoff_status"], "non_signal": True},
        ]

        df_status = pd.DataFrame(status_rows)
        master_summary = {
            "current_phase": 131,
            "next_phase": 132,
            "target_final_phase": 160,
            "overall_status": "READY",
            "active_profile": self.profile.profile_name,
            "non_signal": True,
            "source_preserved": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
            "zero_trading_signals": True,
            "zero_model_training": True,
            "zero_clustering": True,
        }

        if save and hasattr(self.data_lake, "save_cross_asset_regime_report"):
            report_dict = {
                "summary": master_summary,
                "status_table": df_status.to_dict(orient="records"),
            }
            md_text = build_cross_asset_manifest_markdown_report(s5["manifest"], d5["manifest"])
            self.data_lake.save_cross_asset_regime_report(self.profile.profile_name, report_dict, md_text)

        return df_status, master_summary

    def run_all(self, save: bool = True) -> Dict[str, Any]:
        """Run all pipeline stages and return combined dataframes and summaries."""
        d1, s1 = self.build_profiles_domains_entities(save=save)
        d2, s2 = self.build_context_registries(save=save)
        d3, s3 = self.build_linkage_reports(save=save)
        d4, s4 = self.build_contracts_alignment_guards(save=save)
        d5, s5 = self.build_dependencies_findings_scoring_manifest(save=save)
        d6, s6 = self.build_health_validation_safety_handoff(save=save)
        df_status, s_master = self.build_cross_asset_regime_status(save=save)

        combined_dfs = {
            **d1,
            **d2,
            **d3,
            **d4,
            **d5,
            **d6,
            "status": df_status,
        }
        combined_summaries = {
            **s1,
            **s2,
            **s3,
            **s4,
            **s5,
            **s6,
            "pipeline": s_master,
        }
        return {
            "dataframes": combined_dfs,
            "summaries": combined_summaries,
        }
