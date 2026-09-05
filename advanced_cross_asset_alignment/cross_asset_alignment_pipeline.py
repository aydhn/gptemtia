"""Phase 119: Cross-Asset Feature Alignment Master Orchestration Pipeline.

Orchestrates all 32 Phase 119 steps across profile registries, domain registries,
universe definitions, symbol mappings, namespace standards, timestamp contracts,
session calendar bucketing, feature matrix contracts, backward asof join policies,
lookahead guards, domain alignment registries, cross-domain feature matrices,
manifest registries, validation rules, health checks, safety boundaries,
and Phase 120 feature fusion handoff.
"""

from pathlib import Path
from typing import Dict, Any, Tuple, Optional
import pandas as pd

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)
from advanced_cross_asset_alignment.cross_asset_alignment_profile_registry import build_cross_asset_alignment_profile_registry
from advanced_cross_asset_alignment.cross_asset_alignment_domain_registry import build_cross_asset_alignment_domain_registry
from advanced_cross_asset_alignment.asset_universe_alignment import build_asset_universe_registry
from advanced_cross_asset_alignment.asset_symbol_mapping import build_asset_symbol_mapping_registry
from advanced_cross_asset_alignment.cross_domain_feature_namespace import build_feature_namespace_registry
from advanced_cross_asset_alignment.timestamp_alignment_contracts import build_timestamp_alignment_contract_registry
from advanced_cross_asset_alignment.session_calendar_alignment import build_session_calendar_alignment_registry
from advanced_cross_asset_alignment.feature_matrix_contracts import build_feature_matrix_contract_registry
from advanced_cross_asset_alignment.feature_matrix_join_policies import build_feature_matrix_join_policy_registry
from advanced_cross_asset_alignment.fx_commodity_alignment import build_fx_commodity_alignment_registry
from advanced_cross_asset_alignment.fx_macro_alignment import build_fx_macro_alignment_registry
from advanced_cross_asset_alignment.fx_calendar_alignment import build_fx_calendar_alignment_registry
from advanced_cross_asset_alignment.fx_news_metadata_alignment import build_fx_news_metadata_alignment_registry
from advanced_cross_asset_alignment.commodity_macro_alignment import build_commodity_macro_alignment_registry
from advanced_cross_asset_alignment.commodity_calendar_alignment import build_commodity_calendar_alignment_registry
from advanced_cross_asset_alignment.commodity_news_metadata_alignment import build_commodity_news_metadata_alignment_registry
from advanced_cross_asset_alignment.macro_calendar_alignment import build_macro_calendar_alignment_registry
from advanced_cross_asset_alignment.calendar_news_metadata_alignment import build_calendar_news_metadata_alignment_registry
from advanced_cross_asset_alignment.cross_domain_feature_matrix import build_cross_domain_feature_matrix_placeholder
from advanced_cross_asset_alignment.aligned_feature_matrix_manifest import build_aligned_feature_matrix_manifest_registry
from advanced_cross_asset_alignment.cross_asset_feature_metadata import build_cross_asset_feature_metadata_registry
from advanced_cross_asset_alignment.cross_asset_alignment_validation_rules import build_cross_asset_alignment_validation_rule_registry
from advanced_cross_asset_alignment.cross_asset_alignment_quality_handoff import build_cross_asset_alignment_quality_handoff_report
from advanced_cross_asset_alignment.cross_asset_alignment_health import build_cross_asset_alignment_health_check
from advanced_cross_asset_alignment.cross_asset_alignment_safety_boundary import build_cross_asset_alignment_safety_boundary
from advanced_cross_asset_alignment.cross_asset_alignment_validation import build_cross_asset_alignment_validation_report
from advanced_cross_asset_alignment.phase_120_handoff import build_phase_120_cross_asset_feature_fusion_handoff_report
from advanced_cross_asset_alignment.cross_asset_alignment_report_builder import (
    build_cross_asset_alignment_profile_markdown_report,
    build_cross_asset_alignment_domain_markdown_report,
    build_asset_universe_markdown_report,
    build_asset_symbol_mapping_markdown_report,
    build_feature_namespace_markdown_report,
    build_timestamp_session_markdown_report,
    build_feature_matrix_contracts_markdown_report,
    build_domain_alignment_markdown_report,
    build_cross_domain_matrix_markdown_report,
    build_aligned_manifest_markdown_report,
    build_cross_asset_alignment_validation_markdown_report,
    build_cross_asset_alignment_health_markdown_report,
    build_cross_asset_alignment_safety_markdown_report,
    build_phase_120_handoff_markdown_report,
)


class CrossAssetAlignmentPipeline:
    """Master pipeline orchestrating Phase 119 cross-asset feature alignment."""

    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[CrossAssetAlignmentProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_cross_asset_alignment_profile()

    def build_profiles_domains_universes_symbols(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Phase 119 Group 1: Profiles, Domain Registries, Universes, and Symbol Mappings."""
        df_prof, sum_prof = build_cross_asset_alignment_profile_registry(self.profile)
        df_dom, sum_dom = build_cross_asset_alignment_domain_registry(self.profile)
        df_univ, sum_univ = build_asset_universe_registry(self.profile)
        df_sym, sum_sym = build_asset_symbol_mapping_registry(self.profile)

        tables = {
            "profiles": df_prof,
            "domains": df_dom,
            "universes": df_univ,
            "symbols": df_sym,
        }
        summary = {
            "profiles": sum_prof,
            "domains": sum_dom,
            "universes": sum_univ,
            "symbols": sum_sym,
        }

        if save:
            self.data_lake.save_cross_asset_alignment_profile_registry(df_prof, sum_prof)
            self.data_lake.save_cross_asset_alignment_domain_registry(df_dom, sum_dom)
            self.data_lake.save_asset_universe_registry(df_univ, sum_univ)
            self.data_lake.save_asset_symbol_mapping_registry(df_sym, sum_sym)

            md_prof = build_cross_asset_alignment_profile_markdown_report(sum_prof, df_prof)
            self.data_lake.save_cross_asset_alignment_report("profiles", sum_prof, md_prof)
            md_dom = build_cross_asset_alignment_domain_markdown_report(sum_dom, df_dom)
            self.data_lake.save_cross_asset_alignment_report("domains", sum_dom, md_dom)
            md_univ = build_asset_universe_markdown_report(sum_univ, df_univ)
            self.data_lake.save_cross_asset_alignment_report("universes", sum_univ, md_univ)
            md_sym = build_asset_symbol_mapping_markdown_report(sum_sym, df_sym)
            self.data_lake.save_cross_asset_alignment_report("symbols", sum_sym, md_sym)

        return tables, summary

    def build_namespaces_timestamps_session_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Phase 119 Group 2: Namespaces, Timestamp Contracts, Sessions, Matrix Contracts & Join Policies."""
        df_ns, sum_ns = build_feature_namespace_registry(self.profile)
        df_ts, sum_ts = build_timestamp_alignment_contract_registry(self.profile)
        df_sess, sum_sess = build_session_calendar_alignment_registry(self.profile)
        df_cont, sum_cont = build_feature_matrix_contract_registry(self.profile)
        df_jp, sum_jp = build_feature_matrix_join_policy_registry(self.profile)

        tables = {
            "namespaces": df_ns,
            "timestamps": df_ts,
            "sessions": df_sess,
            "matrix_contracts": df_cont,
            "join_policies": df_jp,
        }
        summary = {
            "namespaces": sum_ns,
            "timestamps": sum_ts,
            "sessions": sum_sess,
            "matrix_contracts": sum_cont,
            "join_policies": sum_jp,
        }

        if save:
            self.data_lake.save_feature_namespace_registry(df_ns, sum_ns)
            self.data_lake.save_timestamp_alignment_contract_registry(df_ts, sum_ts)
            self.data_lake.save_session_calendar_alignment_registry(df_sess, sum_sess)
            self.data_lake.save_feature_matrix_contract_registry(df_cont, sum_cont)
            self.data_lake.save_feature_matrix_join_policy_registry(df_jp, sum_jp)

            md_ns = build_feature_namespace_markdown_report(sum_ns, df_ns)
            self.data_lake.save_cross_asset_alignment_report("namespaces", sum_ns, md_ns)
            md_ts = build_timestamp_session_markdown_report(sum_ts, df_ts)
            self.data_lake.save_cross_asset_alignment_report("timestamps", sum_ts, md_ts)
            md_sess = build_timestamp_session_markdown_report(sum_sess, df_sess)
            self.data_lake.save_cross_asset_alignment_report("sessions", sum_sess, md_sess)
            md_cont = build_feature_matrix_contracts_markdown_report(sum_cont, df_cont)
            self.data_lake.save_cross_asset_alignment_report("matrix_contracts", sum_cont, md_cont)
            md_jp = build_feature_matrix_contracts_markdown_report(sum_jp, df_jp)
            self.data_lake.save_cross_asset_alignment_report("join_policies", sum_jp, md_jp)

        return tables, summary

    def build_domain_alignments(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Phase 119 Group 3: 9 Cross-Domain Alignment Registries."""
        df_fc, sum_fc = build_fx_commodity_alignment_registry(self.profile)
        df_fm, sum_fm = build_fx_macro_alignment_registry(self.profile)
        df_fcal, sum_fcal = build_fx_calendar_alignment_registry(self.profile)
        df_fn, sum_fn = build_fx_news_metadata_alignment_registry(self.profile)
        df_cm, sum_cm = build_commodity_macro_alignment_registry(self.profile)
        df_ccal, sum_ccal = build_commodity_calendar_alignment_registry(self.profile)
        df_cn, sum_cn = build_commodity_news_metadata_alignment_registry(self.profile)
        df_mc, sum_mc = build_macro_calendar_alignment_registry(self.profile)
        df_cnm, sum_cnm = build_calendar_news_metadata_alignment_registry(self.profile)

        tables = {
            "fx_commodity": df_fc,
            "fx_macro": df_fm,
            "fx_calendar": df_fcal,
            "fx_news": df_fn,
            "commodity_macro": df_cm,
            "commodity_calendar": df_ccal,
            "commodity_news": df_cn,
            "macro_calendar": df_mc,
            "calendar_news": df_cnm,
        }
        summary = {
            "fx_commodity": sum_fc,
            "fx_macro": sum_fm,
            "fx_calendar": sum_fcal,
            "fx_news": sum_fn,
            "commodity_macro": sum_cm,
            "commodity_calendar": sum_ccal,
            "commodity_news": sum_cn,
            "macro_calendar": sum_mc,
            "calendar_news": sum_cnm,
        }

        if save:
            self.data_lake.save_fx_commodity_alignment_registry(df_fc, sum_fc)
            self.data_lake.save_fx_macro_alignment_registry(df_fm, sum_fm)
            self.data_lake.save_fx_calendar_alignment_registry(df_fcal, sum_fcal)
            self.data_lake.save_fx_news_metadata_alignment_registry(df_fn, sum_fn)
            self.data_lake.save_commodity_macro_alignment_registry(df_cm, sum_cm)
            self.data_lake.save_commodity_calendar_alignment_registry(df_ccal, sum_ccal)
            self.data_lake.save_commodity_news_metadata_alignment_registry(df_cn, sum_cn)
            self.data_lake.save_macro_calendar_alignment_registry(df_mc, sum_mc)
            self.data_lake.save_calendar_news_metadata_alignment_registry(df_cnm, sum_cnm)

            md_fc = build_domain_alignment_markdown_report("FX - Commodity Alignment", sum_fc, df_fc)
            self.data_lake.save_cross_asset_alignment_report("fx_commodity_alignment", sum_fc, md_fc)
            md_fm = build_domain_alignment_markdown_report("FX - Macro Alignment", sum_fm, df_fm)
            self.data_lake.save_cross_asset_alignment_report("fx_macro_alignment", sum_fm, md_fm)
            md_fcal = build_domain_alignment_markdown_report("FX - Calendar Alignment", sum_fcal, df_fcal)
            self.data_lake.save_cross_asset_alignment_report("fx_calendar_alignment", sum_fcal, md_fcal)
            md_fn = build_domain_alignment_markdown_report("FX - News Metadata Alignment", sum_fn, df_fn)
            self.data_lake.save_cross_asset_alignment_report("fx_news_alignment", sum_fn, md_fn)
            md_cm = build_domain_alignment_markdown_report("Commodity - Macro Alignment", sum_cm, df_cm)
            self.data_lake.save_cross_asset_alignment_report("commodity_macro_alignment", sum_cm, md_cm)
            md_ccal = build_domain_alignment_markdown_report("Commodity - Calendar Alignment", sum_ccal, df_ccal)
            self.data_lake.save_cross_asset_alignment_report("commodity_calendar_alignment", sum_ccal, md_ccal)
            md_cn = build_domain_alignment_markdown_report("Commodity - News Metadata Alignment", sum_cn, df_cn)
            self.data_lake.save_cross_asset_alignment_report("commodity_news_alignment", sum_cn, md_cn)
            md_mc = build_domain_alignment_markdown_report("Macro - Calendar Alignment", sum_mc, df_mc)
            self.data_lake.save_cross_asset_alignment_report("macro_calendar_alignment", sum_mc, md_mc)
            md_cnm = build_domain_alignment_markdown_report("Calendar - News Metadata Alignment", sum_cnm, df_cnm)
            self.data_lake.save_cross_asset_alignment_report("calendar_news_alignment", sum_cnm, md_cnm)

        return tables, summary

    def build_matrices_manifests_metadata(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Phase 119 Group 4: Cross-Domain Matrices, Aligned Manifests, and Metadata."""
        df_mat, sum_mat = build_cross_domain_feature_matrix_placeholder(self.profile)
        df_man, sum_man = build_aligned_feature_matrix_manifest_registry(self.profile)
        df_meta, sum_meta = build_cross_asset_feature_metadata_registry(self.profile)

        tables = {
            "cross_domain_matrix": df_mat,
            "manifests": df_man,
            "feature_metadata": df_meta,
        }
        summary = {
            "cross_domain_matrix": sum_mat,
            "manifests": sum_man,
            "feature_metadata": sum_meta,
        }

        if save:
            self.data_lake.save_cross_domain_feature_matrix(df_mat, sum_mat)
            self.data_lake.save_aligned_feature_matrix_manifest_registry(df_man, sum_man)
            self.data_lake.save_cross_asset_feature_metadata_registry(df_meta, sum_meta)

            md_mat = build_cross_domain_matrix_markdown_report(sum_mat, df_mat)
            self.data_lake.save_cross_asset_alignment_report("cross_domain_matrix", sum_mat, md_mat)
            md_man = build_aligned_manifest_markdown_report(sum_man, df_man)
            self.data_lake.save_cross_asset_alignment_report("manifests", sum_man, md_man)
            md_meta = build_feature_namespace_markdown_report(sum_meta, df_meta)
            self.data_lake.save_cross_asset_alignment_report("feature_metadata", sum_meta, md_meta)

        return tables, summary

    def build_governance_validation_health_safety(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Phase 119 Group 5: Validation Rules, Quality Handoff, Health Checks, Safety Boundary, and Phase 120 Handoff."""
        df_vr, sum_vr = build_cross_asset_alignment_validation_rule_registry(self.profile)
        df_qh, sum_qh = build_cross_asset_alignment_quality_handoff_report(self.profile)
        df_val, sum_val = build_cross_asset_alignment_validation_report(self.profile)
        df_hlth, sum_hlth = build_cross_asset_alignment_health_check(self.project_root, self.profile)
        df_safe, sum_safe = build_cross_asset_alignment_safety_boundary(self.profile)
        df_p120, sum_p120 = build_phase_120_cross_asset_feature_fusion_handoff_report(self.profile)

        tables = {
            "validation_rules": df_vr,
            "quality_handoff": df_qh,
            "validation_report": df_val,
            "health_check": df_hlth,
            "safety_boundary": df_safe,
            "phase_120_handoff": df_p120,
        }
        summary = {
            "validation_rules": sum_vr,
            "quality_handoff": sum_qh,
            "validation_report": sum_val,
            "health_check": sum_hlth,
            "safety_boundary": sum_safe,
            "phase_120_handoff": sum_p120,
        }

        if save:
            self.data_lake.save_cross_asset_alignment_validation_rule_registry(df_vr, sum_vr)
            self.data_lake.save_cross_asset_alignment_quality_handoff_report(df_qh, sum_qh)
            self.data_lake.save_cross_asset_alignment_validation_report(df_val, sum_val)
            self.data_lake.save_cross_asset_alignment_health_check(df_hlth, sum_hlth)
            self.data_lake.save_cross_asset_alignment_safety_boundary(df_safe, sum_safe)
            self.data_lake.save_phase_120_cross_asset_feature_fusion_handoff_report(df_p120, sum_p120)

            md_val = build_cross_asset_alignment_validation_markdown_report(sum_val, df_val)
            self.data_lake.save_cross_asset_alignment_report("validation_report", sum_val, md_val)
            md_hlth = build_cross_asset_alignment_health_markdown_report(sum_hlth, df_hlth)
            self.data_lake.save_cross_asset_alignment_report("health_check", sum_hlth, md_hlth)
            md_safe = build_cross_asset_alignment_safety_markdown_report(sum_safe, df_safe)
            self.data_lake.save_cross_asset_alignment_report("safety_boundary", sum_safe, md_safe)
            md_p120 = build_phase_120_handoff_markdown_report(sum_p120, df_p120)
            self.data_lake.save_cross_asset_alignment_report("phase_120_handoff", sum_p120, md_p120)

        return tables, summary

    def run_full_pipeline(self, save: bool = True) -> Dict[str, Any]:
        """Execute the entire 32-step Phase 119 Cross-Asset Alignment Pipeline."""
        t1, s1 = self.build_profiles_domains_universes_symbols(save=save)
        t2, s2 = self.build_namespaces_timestamps_session_contracts(save=save)
        t3, s3 = self.build_domain_alignments(save=save)
        t4, s4 = self.build_matrices_manifests_metadata(save=save)
        t5, s5 = self.build_governance_validation_health_safety(save=save)

        all_tables = {**t1, **t2, **t3, **t4, **t5}
        all_summaries = {**s1, **s2, **s3, **s4, **s5}

        pipeline_result = {
            "phase": 119,
            "target_final_phase": 160,
            "next_phase": 120,
            "profile": self.profile.name,
            "pipeline_status": "SUCCESS",
            "total_tables_generated": len(all_tables),
            "summaries": all_summaries,
            "non_signal": True,
            "future_data_allowed": False,
        }

        if save:
            self.data_lake.save_cross_asset_alignment_report("master_pipeline_summary", pipeline_result)

        return pipeline_result
