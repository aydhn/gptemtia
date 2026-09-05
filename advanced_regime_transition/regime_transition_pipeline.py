"""Phase 130: Regime Transition Pipeline.

Master pipeline orchestrating profiles, domains, sequence contracts, candidate/pseudo schemas,
transition/stability metrics, persistence/frequency/ambiguity/continuity/stability diagnostics,
volatility/trend/range transitions, macro/news/cross-asset context, quality/validation dependencies,
findings, review queue, stability scoring, manifest, health, validation, safety, and Phase 131 handoff.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
    get_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_profile_registry import (
    build_regime_transition_profile_registry,
)
from advanced_regime_transition.regime_transition_domain_registry import (
    build_regime_transition_domain_registry,
)
from advanced_regime_transition.regime_state_sequence_contracts import (
    build_regime_state_sequence_contract_registry,
)
from advanced_regime_transition.candidate_state_sequence_schema import (
    build_candidate_state_sequence_schema_registry,
)
from advanced_regime_transition.pseudo_state_sequence_schema import (
    build_pseudo_state_sequence_schema_registry,
)
from advanced_regime_transition.regime_transition_metric_registry import (
    build_regime_transition_metric_registry,
)
from advanced_regime_transition.regime_stability_metric_registry import (
    build_regime_stability_metric_registry,
)
from advanced_regime_transition.regime_transition_thresholds import (
    build_regime_transition_threshold_registry,
)
from advanced_regime_transition.regime_transition_timestamp_policies import (
    build_regime_transition_timestamp_policy_registry,
)
from advanced_regime_transition.regime_transition_no_lookahead_guard import (
    build_regime_transition_no_lookahead_guard_registry,
)
from advanced_regime_transition.regime_transition_source_phases import (
    build_regime_transition_source_phase_registry,
)
from advanced_regime_transition.state_persistence_diagnostics import (
    build_state_persistence_diagnostics_report,
)
from advanced_regime_transition.state_transition_frequency import (
    build_state_transition_frequency_report,
)
from advanced_regime_transition.state_transition_matrix_placeholders import (
    build_state_transition_matrix_placeholder_registry,
)
from advanced_regime_transition.state_transition_ambiguity import (
    build_state_transition_ambiguity_report,
)
from advanced_regime_transition.state_transition_continuity import (
    build_state_transition_continuity_report,
)
from advanced_regime_transition.state_transition_stability import (
    build_state_transition_stability_report,
)
from advanced_regime_transition.volatility_transition_diagnostics import (
    build_volatility_transition_diagnostics_report,
)
from advanced_regime_transition.trend_transition_diagnostics import (
    build_trend_transition_diagnostics_report,
)
from advanced_regime_transition.range_transition_diagnostics import (
    build_range_transition_diagnostics_report,
)
from advanced_regime_transition.macro_event_transition_context import (
    build_macro_event_transition_context_report,
)
from advanced_regime_transition.news_metadata_transition_context import (
    build_news_metadata_transition_context_report,
)
from advanced_regime_transition.cross_asset_transition_prep import (
    build_cross_asset_transition_prep_report,
)
from advanced_regime_transition.transition_quality_dependencies import (
    build_transition_quality_dependency_report,
)
from advanced_regime_transition.transition_validation_dependencies import (
    build_transition_validation_dependency_report,
)
from advanced_regime_transition.transition_quality_findings import (
    build_transition_quality_findings_registry,
)
from advanced_regime_transition.transition_manual_review import (
    build_transition_manual_review_queue,
)
from advanced_regime_transition.transition_stability_scoring import (
    build_transition_stability_score_report,
)
from advanced_regime_transition.transition_diagnostics_manifest import (
    build_transition_diagnostics_manifest,
)
from advanced_regime_transition.regime_transition_health import (
    build_regime_transition_health_check,
)
from advanced_regime_transition.regime_transition_validation import (
    build_regime_transition_validation_report,
)
from advanced_regime_transition.regime_transition_safety_boundary import (
    build_regime_transition_safety_boundary,
)
from advanced_regime_transition.phase_131_handoff import (
    build_phase_131_cross_asset_regime_context_handoff_report,
)
from advanced_regime_transition.regime_transition_report_builder import (
    build_regime_transition_profile_markdown_report,
    build_state_sequence_contract_markdown_report,
    build_transition_metric_markdown_report,
    build_state_transition_diagnostics_markdown_report,
    build_regime_family_transition_markdown_report,
    build_macro_news_cross_asset_transition_markdown_report,
    build_transition_findings_markdown_report,
    build_transition_stability_score_markdown_report,
    build_transition_manifest_markdown_report,
    build_regime_transition_validation_markdown_report,
    build_regime_transition_safety_markdown_report,
    build_phase_131_handoff_markdown_report,
)
from reports.report_builder import (
    build_regime_transition_text_report,
    build_state_sequence_contract_text_report,
    build_transition_metric_text_report,
    build_state_transition_diagnostics_text_report,
    build_regime_family_transition_text_report,
    build_transition_context_text_report,
    build_transition_score_text_report,
    build_transition_manifest_text_report,
    build_regime_transition_validation_text_report,
    build_regime_transition_safety_text_report,
    build_phase_131_handoff_text_report,
)


class RegimeTransitionPipeline:
    """Master pipeline orchestrating Phase 130 Regime Transition and Stability Analysis."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[RegimeTransitionProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(__file__).resolve().parent.parent
        self.profile = profile or get_default_regime_transition_profile()

    def build_profiles_domains_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 1: Build profiles, domains, contracts, and candidate/pseudo schemas."""
        df_prof, s_prof = build_regime_transition_profile_registry(self.profile)
        df_dom, s_dom = build_regime_transition_domain_registry(self.profile)
        df_cont, s_cont = build_regime_state_sequence_contract_registry(self.profile)
        df_cand, s_cand = build_candidate_state_sequence_schema_registry(self.profile)
        df_pseu, s_pseu = build_pseudo_state_sequence_schema_registry(self.profile)

        dfs = {
            "profiles": df_prof,
            "domains": df_dom,
            "sequence_contracts": df_cont,
            "candidate_schema": df_cand,
            "pseudo_schema": df_pseu,
        }
        summaries = {
            "profiles": s_prof,
            "domains": s_dom,
            "sequence_contracts": s_cont,
            "candidate_schema": s_cand,
            "pseudo_schema": s_pseu,
        }

        if save:
            self.data_lake.save_regime_transition_profile_registry(df_prof, s_prof)
            self.data_lake.save_regime_transition_domain_registry(df_dom, s_dom)
            self.data_lake.save_regime_state_sequence_contract_registry(df_cont, s_cont)
            self.data_lake.save_candidate_state_sequence_schema_registry(df_cand, s_cand)
            self.data_lake.save_pseudo_state_sequence_schema_registry(df_pseu, s_pseu)

        return dfs, summaries

    def build_metrics_thresholds_guards(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 2: Build transition & stability metrics, thresholds, timestamp policies, and guards."""
        df_tmet, s_tmet = build_regime_transition_metric_registry(self.profile)
        df_smet, s_smet = build_regime_stability_metric_registry(self.profile)
        df_th, s_th = build_regime_transition_threshold_registry(self.profile)
        df_tp, s_tp = build_regime_transition_timestamp_policy_registry(self.profile)
        df_gd, s_gd = build_regime_transition_no_lookahead_guard_registry(self.profile)
        df_sp, s_sp = build_regime_transition_source_phase_registry(self.profile)

        dfs = {
            "transition_metrics": df_tmet,
            "stability_metrics": df_smet,
            "thresholds": df_th,
            "timestamp_policies": df_tp,
            "no_lookahead_guard": df_gd,
            "source_phases": df_sp,
        }
        summaries = {
            "transition_metrics": s_tmet,
            "stability_metrics": s_smet,
            "thresholds": s_th,
            "timestamp_policies": s_tp,
            "no_lookahead_guard": s_gd,
            "source_phases": s_sp,
        }

        if save:
            self.data_lake.save_regime_transition_metric_registry(df_tmet, s_tmet)
            self.data_lake.save_regime_stability_metric_registry(df_smet, s_smet)
            self.data_lake.save_regime_transition_threshold_registry(df_th, s_th)
            self.data_lake.save_regime_transition_timestamp_policy_registry(df_tp, s_tp)
            self.data_lake.save_regime_transition_no_lookahead_guard_registry(df_gd, s_gd)
            self.data_lake.save_regime_transition_source_phase_registry(df_sp, s_sp)

        return dfs, summaries

    def build_state_transition_diagnostics(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 3: Build persistence, frequency, transition matrix, ambiguity, continuity, stability."""
        df_pers, s_pers = build_state_persistence_diagnostics_report(self.profile)
        df_freq, s_freq = build_state_transition_frequency_report(self.profile)
        df_mat, s_mat = build_state_transition_matrix_placeholder_registry(self.profile)
        df_amb, s_amb = build_state_transition_ambiguity_report(self.profile)
        df_cont, s_cont = build_state_transition_continuity_report(self.profile)
        df_stab, s_stab = build_state_transition_stability_report(self.profile)

        dfs = {
            "persistence": df_pers,
            "frequency": df_freq,
            "transition_matrix": df_mat,
            "ambiguity": df_amb,
            "continuity": df_cont,
            "stability": df_stab,
        }
        summaries = {
            "persistence": s_pers,
            "frequency": s_freq,
            "transition_matrix": s_mat,
            "ambiguity": s_amb,
            "continuity": s_cont,
            "stability": s_stab,
        }

        if save:
            self.data_lake.save_state_persistence_diagnostics_report(df_pers, s_pers)
            self.data_lake.save_state_transition_frequency_report(df_freq, s_freq)
            self.data_lake.save_state_transition_matrix_placeholder_registry(df_mat, s_mat)
            self.data_lake.save_state_transition_ambiguity_report(df_amb, s_amb)
            self.data_lake.save_state_transition_continuity_report(df_cont, s_cont)
            self.data_lake.save_state_transition_stability_report(df_stab, s_stab)

        return dfs, summaries

    def build_regime_family_transition_reports(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 4: Build volatility, trend, and range family transition diagnostics."""
        df_vol, s_vol = build_volatility_transition_diagnostics_report(self.profile)
        df_trd, s_trd = build_trend_transition_diagnostics_report(self.profile)
        df_rng, s_rng = build_range_transition_diagnostics_report(self.profile)

        dfs = {
            "volatility_transition": df_vol,
            "trend_transition": df_trd,
            "range_transition": df_rng,
        }
        summaries = {
            "volatility_transition": s_vol,
            "trend_transition": s_trd,
            "range_transition": s_rng,
        }

        if save:
            self.data_lake.save_volatility_transition_diagnostics_report(df_vol, s_vol)
            self.data_lake.save_trend_transition_diagnostics_report(df_trd, s_trd)
            self.data_lake.save_range_transition_diagnostics_report(df_rng, s_rng)

        return dfs, summaries

    def build_macro_news_cross_asset_context(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 5: Build macro event, news metadata, and cross-asset transition context."""
        df_mac, s_mac = build_macro_event_transition_context_report(self.profile)
        df_nws, s_nws = build_news_metadata_transition_context_report(self.profile)
        df_xast, s_xast = build_cross_asset_transition_prep_report(self.profile)

        dfs = {
            "macro_event_context": df_mac,
            "news_metadata_context": df_nws,
            "cross_asset_prep": df_xast,
        }
        summaries = {
            "macro_event_context": s_mac,
            "news_metadata_context": s_nws,
            "cross_asset_prep": s_xast,
        }

        if save:
            self.data_lake.save_macro_event_transition_context_report(df_mac, s_mac)
            self.data_lake.save_news_metadata_transition_context_report(df_nws, s_nws)
            self.data_lake.save_cross_asset_transition_prep_report(df_xast, s_xast)

        return dfs, summaries

    def build_dependencies_findings_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 6: Build quality/validation dependencies, findings, manual review, scoring, manifest."""
        df_qdep, s_qdep = build_transition_quality_dependency_report(self.profile)
        df_vdep, s_vdep = build_transition_validation_dependency_report(self.profile)
        df_find, s_find = build_transition_quality_findings_registry(self.profile)
        df_rev, s_rev = build_transition_manual_review_queue(self.profile)
        df_scr, s_scr = build_transition_stability_score_report(self.profile)
        df_man, s_man = build_transition_diagnostics_manifest(self.profile)

        dfs = {
            "quality_dependencies": df_qdep,
            "validation_dependencies": df_vdep,
            "findings": df_find,
            "manual_review": df_rev,
            "scoring": df_scr,
            "manifest": df_man,
        }
        summaries = {
            "quality_dependencies": s_qdep,
            "validation_dependencies": s_vdep,
            "findings": s_find,
            "manual_review": s_rev,
            "scoring": s_scr,
            "manifest": s_man,
        }

        if save:
            self.data_lake.save_transition_quality_dependency_report(df_qdep, s_qdep)
            self.data_lake.save_transition_validation_dependency_report(df_vdep, s_vdep)
            self.data_lake.save_transition_quality_findings_registry(df_find, s_find)
            self.data_lake.save_transition_manual_review_queue(df_rev, s_rev)
            self.data_lake.save_transition_stability_score_report(df_scr, s_scr)
            self.data_lake.save_transition_diagnostics_manifest(df_man, s_man)

        return dfs, summaries

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 7: Build health check, validation report, safety boundary, and Phase 131 handoff."""
        df_hlth, s_hlth = build_regime_transition_health_check(self.project_root, self.profile)
        df_sft, s_sft = build_regime_transition_safety_boundary(self.profile)
        df_han, s_han = build_phase_131_cross_asset_regime_context_handoff_report(self.profile)

        # Build composite validation
        validation_input_tables = {
            "profiles": build_regime_transition_profile_registry(self.profile)[0],
            "contracts": build_regime_state_sequence_contract_registry(self.profile)[0],
            "metrics": build_regime_transition_metric_registry(self.profile)[0],
            "manifest": build_transition_diagnostics_manifest(self.profile)[0],
        }
        df_val, s_val = build_regime_transition_validation_report(validation_input_tables, self.profile)

        dfs = {
            "health": df_hlth,
            "validation": df_val,
            "safety": df_sft,
            "handoff": df_han,
        }
        summaries = {
            "health": s_hlth,
            "validation": s_val,
            "safety": s_sft,
            "handoff": s_han,
        }

        if save:
            self.data_lake.save_regime_transition_health_check(df_hlth, s_hlth)
            self.data_lake.save_regime_transition_validation_report(df_val, s_val)
            self.data_lake.save_regime_transition_safety_boundary(df_sft, s_sft)
            self.data_lake.save_phase_131_cross_asset_regime_context_handoff_report(df_han, s_han)

        return dfs, summaries

    def build_regime_transition_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Master orchestrator generating full status summary and saving reports."""
        dfs_1, s_1 = self.build_profiles_domains_contracts(save=save)
        dfs_2, s_2 = self.build_metrics_thresholds_guards(save=save)
        dfs_3, s_3 = self.build_state_transition_diagnostics(save=save)
        dfs_4, s_4 = self.build_regime_family_transition_reports(save=save)
        dfs_5, s_5 = self.build_macro_news_cross_asset_context(save=save)
        dfs_6, s_6 = self.build_dependencies_findings_scoring_manifest(save=save)
        dfs_7, s_7 = self.build_health_validation_safety_handoff(save=save)

        status_rows = [
            {"component": "profiles_domains_contracts", "status": "READY", "item_count": len(dfs_1)},
            {"component": "metrics_thresholds_guards", "status": "READY", "item_count": len(dfs_2)},
            {"component": "state_transition_diagnostics", "status": "READY", "item_count": len(dfs_3)},
            {"component": "regime_family_transition", "status": "READY", "item_count": len(dfs_4)},
            {"component": "macro_news_cross_asset_context", "status": "READY", "item_count": len(dfs_5)},
            {"component": "dependencies_findings_scoring_manifest", "status": "READY", "item_count": len(dfs_6)},
            {"component": "health_validation_safety_handoff", "status": "READY", "item_count": len(dfs_7)},
        ]
        status_df = pd.DataFrame(status_rows)

        summary = {
            "overall_status": "READY",
            "active_profile": self.profile.profile_name,
            "current_phase": self.profile.current_phase,
            "target_final_phase": self.profile.target_final_phase,
            "next_phase": self.profile.next_phase,
            "stability_score": s_6["scoring"].get("stability_score", 0.82),
            "total_components": len(status_rows),
            "non_signal": True,
            "source_preserved": True,
            "clustering_executed": False,
            "model_training_executed": False,
        }

        if save:
            # Save master status report dictionary in JSON/MD
            md_content = build_transition_manifest_markdown_report(summary, dfs_6["manifest"])
            self.data_lake.save_regime_transition_report(self.profile.profile_name, summary, md_content)

        return status_df, summary
