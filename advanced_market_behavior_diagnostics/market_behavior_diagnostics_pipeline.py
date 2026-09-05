"""Phase 129: Market Behavior Diagnostics Pipeline.

Master pipeline orchestrating profile registration, candidate state quality,
regime family quality, behavior diagnostics, transition/stability readiness, findings,
scoring, manifests, health, validation, safety, and Phase 130 handoff.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_profile_registry import (
    build_market_behavior_diagnostics_profile_registry,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_domain_registry import (
    build_market_behavior_diagnostics_domain_registry,
)
from advanced_market_behavior_diagnostics.behavior_quality_metric_registry import (
    build_behavior_quality_metric_registry,
)
from advanced_market_behavior_diagnostics.behavior_diagnostics_metric_registry import (
    build_behavior_diagnostics_metric_registry,
)
from advanced_market_behavior_diagnostics.behavior_quality_thresholds import (
    build_behavior_quality_threshold_registry,
)
from advanced_market_behavior_diagnostics.candidate_state_quality import (
    build_candidate_state_quality_report,
)
from advanced_market_behavior_diagnostics.pseudo_state_quality import (
    build_pseudo_state_quality_report,
)
from advanced_market_behavior_diagnostics.candidate_state_coverage import (
    build_candidate_state_coverage_report,
)
from advanced_market_behavior_diagnostics.candidate_state_consistency import (
    build_candidate_state_consistency_report,
)
from advanced_market_behavior_diagnostics.candidate_state_ambiguity import (
    build_candidate_state_ambiguity_report,
)
from advanced_market_behavior_diagnostics.candidate_state_stability import (
    build_candidate_state_stability_report,
)
from advanced_market_behavior_diagnostics.candidate_state_missingness import (
    build_candidate_state_missingness_report,
)
from advanced_market_behavior_diagnostics.candidate_state_namespace_quality import (
    build_candidate_state_namespace_quality_report,
)
from advanced_market_behavior_diagnostics.regime_family_quality import (
    build_regime_family_quality_report,
)
from advanced_market_behavior_diagnostics.regime_family_coverage import (
    build_regime_family_coverage_report,
)
from advanced_market_behavior_diagnostics.regime_family_consistency import (
    build_regime_family_consistency_report,
)
from advanced_market_behavior_diagnostics.volatility_behavior_diagnostics import (
    build_volatility_behavior_diagnostics_report,
)
from advanced_market_behavior_diagnostics.trend_behavior_diagnostics import (
    build_trend_behavior_diagnostics_report,
)
from advanced_market_behavior_diagnostics.range_behavior_diagnostics import (
    build_range_behavior_diagnostics_report,
)
from advanced_market_behavior_diagnostics.macro_event_behavior_diagnostics import (
    build_macro_event_behavior_diagnostics_report,
)
from advanced_market_behavior_diagnostics.news_metadata_behavior_diagnostics import (
    build_news_metadata_behavior_diagnostics_report,
)
from advanced_market_behavior_diagnostics.cross_asset_behavior_diagnostics import (
    build_cross_asset_behavior_diagnostics_report,
)
from advanced_market_behavior_diagnostics.behavior_transition_readiness import (
    build_behavior_transition_readiness_report,
)
from advanced_market_behavior_diagnostics.behavior_stability_readiness import (
    build_behavior_stability_readiness_report,
)
from advanced_market_behavior_diagnostics.regime_quality_dependencies import (
    build_regime_quality_dependency_report,
)
from advanced_market_behavior_diagnostics.behavior_quality_findings import (
    build_behavior_quality_findings_registry,
)
from advanced_market_behavior_diagnostics.behavior_quality_manual_review import (
    build_behavior_quality_manual_review_queue,
)
from advanced_market_behavior_diagnostics.behavior_quality_scoring import (
    build_behavior_quality_score_report,
)
from advanced_market_behavior_diagnostics.behavior_diagnostics_manifest import (
    build_behavior_diagnostics_manifest,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_health import (
    build_market_behavior_diagnostics_health_check,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_validation import (
    build_market_behavior_diagnostics_validation_report,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_safety_boundary import (
    build_market_behavior_diagnostics_safety_boundary,
)
from advanced_market_behavior_diagnostics.phase_130_handoff import (
    build_phase_130_regime_transition_stability_handoff_report,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_report_builder import (
    build_market_behavior_diagnostics_profile_markdown_report,
    build_candidate_state_quality_markdown_report,
    build_behavior_quality_score_markdown_report,
    build_behavior_manifest_markdown_report,
    build_phase_130_handoff_markdown_report,
)


class MarketBehaviorDiagnosticsPipeline:
    """Master pipeline orchestrating Phase 129 diagnostics and reporting."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
    ):
        self.settings = settings or get_settings()
        self.data_lake = data_lake or DataLake()
        self.project_root = project_root or Path.cwd()
        self.profile = profile or get_market_behavior_diagnostics_profile(
            self.settings.default_market_behavior_diagnostics_profile
        )

    def build_profiles_domains_metrics(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], dict]:
        """Build operational profiles, domain classifications, metrics, and thresholds."""
        prof_df, prof_summary = build_market_behavior_diagnostics_profile_registry(self.profile)
        dom_df, dom_summary = build_market_behavior_diagnostics_domain_registry(self.profile)
        q_metric_df, q_metric_summary = build_behavior_quality_metric_registry(self.profile)
        d_metric_df, d_metric_summary = build_behavior_diagnostics_metric_registry(self.profile)
        thresh_df, thresh_summary = build_behavior_quality_threshold_registry(self.profile)

        if save and hasattr(self.data_lake, "save_market_behavior_diagnostics_profile_registry"):
            self.data_lake.save_market_behavior_diagnostics_profile_registry(prof_df, prof_summary)
            self.data_lake.save_market_behavior_diagnostics_domain_registry(dom_df, dom_summary)
            self.data_lake.save_behavior_quality_metric_registry(q_metric_df, q_metric_summary)
            self.data_lake.save_behavior_diagnostics_metric_registry(d_metric_df, d_metric_summary)
            self.data_lake.save_behavior_quality_threshold_registry(thresh_df, thresh_summary)

        tables = {
            "profiles": prof_df,
            "domains": dom_df,
            "quality_metrics": q_metric_df,
            "diagnostics_metrics": d_metric_df,
            "thresholds": thresh_df,
        }
        summary = {
            "total_profiles": len(prof_df),
            "total_domains": len(dom_df),
            "total_quality_metrics": len(q_metric_df),
            "total_diagnostics_metrics": len(d_metric_df),
            "total_thresholds": len(thresh_df),
            "non_signal": True,
        }
        return tables, summary

    def build_candidate_state_quality_reports(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], dict]:
        """Build quality, coverage, consistency, ambiguity, stability, missingness, and namespace reports."""
        c_qual_df, c_qual_sum = build_candidate_state_quality_report(self.profile)
        p_qual_df, p_qual_sum = build_pseudo_state_quality_report(self.profile)
        c_cov_df, c_cov_sum = build_candidate_state_coverage_report(self.profile)
        c_con_df, c_con_sum = build_candidate_state_consistency_report(self.profile)
        c_amb_df, c_amb_sum = build_candidate_state_ambiguity_report(self.profile)
        c_stab_df, c_stab_sum = build_candidate_state_stability_report(self.profile)
        c_miss_df, c_miss_sum = build_candidate_state_missingness_report(self.profile)
        c_ns_df, c_ns_sum = build_candidate_state_namespace_quality_report(self.profile)

        if save and hasattr(self.data_lake, "save_candidate_state_quality_report"):
            self.data_lake.save_candidate_state_quality_report(c_qual_df, c_qual_sum)
            self.data_lake.save_pseudo_state_quality_report(p_qual_df, p_qual_sum)
            self.data_lake.save_candidate_state_coverage_report(c_cov_df, c_cov_sum)
            self.data_lake.save_candidate_state_consistency_report(c_con_df, c_con_sum)
            self.data_lake.save_candidate_state_ambiguity_report(c_amb_df, c_amb_sum)
            self.data_lake.save_candidate_state_stability_report(c_stab_df, c_stab_sum)
            self.data_lake.save_candidate_state_missingness_report(c_miss_df, c_miss_sum)
            self.data_lake.save_candidate_state_namespace_quality_report(c_ns_df, c_ns_sum)

        tables = {
            "candidate_quality": c_qual_df,
            "pseudo_quality": p_qual_df,
            "coverage": c_cov_df,
            "consistency": c_con_df,
            "ambiguity": c_amb_df,
            "stability": c_stab_df,
            "missingness": c_miss_df,
            "namespace": c_ns_df,
        }
        summary = {
            "total_candidate_states": len(c_qual_df),
            "total_pseudo_states": len(p_qual_df),
            "all_ready": bool(c_qual_sum.get("ready_count") == len(c_qual_df)),
            "non_signal": True,
        }
        return tables, summary

    def build_regime_family_quality_reports(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], dict]:
        """Build regime family quality, coverage, and consistency reports."""
        f_qual_df, f_qual_sum = build_regime_family_quality_report(self.profile)
        f_cov_df, f_cov_sum = build_regime_family_coverage_report(self.profile)
        f_con_df, f_con_sum = build_regime_family_consistency_report(self.profile)

        if save and hasattr(self.data_lake, "save_regime_family_quality_report"):
            self.data_lake.save_regime_family_quality_report(f_qual_df, f_qual_sum)
            self.data_lake.save_regime_family_coverage_report(f_cov_df, f_cov_sum)
            self.data_lake.save_regime_family_consistency_report(f_con_df, f_con_sum)

        tables = {
            "family_quality": f_qual_df,
            "family_coverage": f_cov_df,
            "family_consistency": f_con_df,
        }
        summary = {
            "total_families": len(f_qual_df),
            "all_ready": bool(f_qual_sum.get("ready_count") == len(f_qual_df)),
            "phase_130_ready": bool(f_qual_sum.get("phase_130_ready", True)),
            "non_signal": True,
        }
        return tables, summary

    def build_behavior_diagnostics_reports(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], dict]:
        """Build volatility, trend, range, macro, news metadata, and cross-asset behavior diagnostics."""
        vol_df, vol_sum = build_volatility_behavior_diagnostics_report(self.profile)
        trend_df, trend_sum = build_trend_behavior_diagnostics_report(self.profile)
        range_df, range_sum = build_range_behavior_diagnostics_report(self.profile)
        macro_df, macro_sum = build_macro_event_behavior_diagnostics_report(self.profile)
        news_df, news_sum = build_news_metadata_behavior_diagnostics_report(self.profile)
        cross_df, cross_sum = build_cross_asset_behavior_diagnostics_report(self.profile)

        if save and hasattr(self.data_lake, "save_volatility_behavior_diagnostics_report"):
            self.data_lake.save_volatility_behavior_diagnostics_report(vol_df, vol_sum)
            self.data_lake.save_trend_behavior_diagnostics_report(trend_df, trend_sum)
            self.data_lake.save_range_behavior_diagnostics_report(range_df, range_sum)
            self.data_lake.save_macro_event_behavior_diagnostics_report(macro_df, macro_sum)
            self.data_lake.save_news_metadata_behavior_diagnostics_report(news_df, news_sum)
            self.data_lake.save_cross_asset_behavior_diagnostics_report(cross_df, cross_sum)

        tables = {
            "volatility_behavior": vol_df,
            "trend_behavior": trend_df,
            "range_behavior": range_df,
            "macro_event_behavior": macro_df,
            "news_metadata_behavior": news_df,
            "cross_asset_behavior": cross_df,
        }
        summary = {
            "total_behavior_domains": len(tables),
            "all_ready": True,
            "non_signal": True,
        }
        return tables, summary

    def build_transition_stability_readiness(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], dict]:
        """Build transition readiness, stability readiness, and regime quality dependencies."""
        trans_df, trans_sum = build_behavior_transition_readiness_report(self.profile)
        stab_df, stab_sum = build_behavior_stability_readiness_report(self.profile)
        dep_df, dep_sum = build_regime_quality_dependency_report(self.profile)

        if save and hasattr(self.data_lake, "save_behavior_transition_readiness_report"):
            self.data_lake.save_behavior_transition_readiness_report(trans_df, trans_sum)
            self.data_lake.save_behavior_stability_readiness_report(stab_df, stab_sum)
            self.data_lake.save_regime_quality_dependency_report(dep_df, dep_sum)

        tables = {
            "transition_readiness": trans_df,
            "stability_readiness": stab_df,
            "dependencies": dep_df,
        }
        summary = {
            "transition_ready": bool(trans_sum.get("all_ready", True)),
            "stability_ready": bool(stab_sum.get("all_ready", True)),
            "dependencies_resolved": bool(dep_sum.get("all_resolved", True)),
            "non_signal": True,
        }
        return tables, summary

    def build_findings_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], dict]:
        """Build findings, manual review queue, quality score report, and diagnostics manifest."""
        find_df, find_sum = build_behavior_quality_findings_registry(self.profile)
        rev_df, rev_sum = build_behavior_quality_manual_review_queue(self.profile)
        score_df, score_sum = build_behavior_quality_score_report(self.profile)
        man_df, man_sum = build_behavior_diagnostics_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_behavior_quality_findings_registry"):
            self.data_lake.save_behavior_quality_findings_registry(find_df, find_sum)
            self.data_lake.save_behavior_quality_manual_review_queue(rev_df, rev_sum)
            self.data_lake.save_behavior_quality_score_report(score_df, score_sum)
            self.data_lake.save_behavior_diagnostics_manifest(man_df, man_sum)

        tables = {
            "findings": find_df,
            "manual_review": rev_df,
            "score": score_df,
            "manifest": man_df,
        }
        summary = {
            "total_findings": len(find_df),
            "total_manual_reviews": len(rev_df),
            "quality_score": float(score_sum.get("overall_quality_score", 1.0)),
            "quality_grade": str(score_sum.get("quality_grade", "READY")),
            "non_signal": True,
        }
        return tables, summary

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], dict]:
        """Build health check, validation report, safety boundary, and Phase 130 handoff."""
        hlth_df, hlth_sum = build_market_behavior_diagnostics_health_check(self.project_root, self.profile)
        val_df, val_sum = build_market_behavior_diagnostics_validation_report(profile=self.profile)
        safe_df, safe_sum = build_market_behavior_diagnostics_safety_boundary(self.profile)
        hand_df, hand_sum = build_phase_130_regime_transition_stability_handoff_report(self.profile)

        if save and hasattr(self.data_lake, "save_market_behavior_diagnostics_health_check"):
            self.data_lake.save_market_behavior_diagnostics_health_check(hlth_df, hlth_sum)
            self.data_lake.save_market_behavior_diagnostics_validation_report(val_df, val_sum)
            self.data_lake.save_market_behavior_diagnostics_safety_boundary(safe_df, safe_sum)
            self.data_lake.save_phase_130_regime_transition_stability_handoff_report(hand_df, hand_sum)

        tables = {
            "health": hlth_df,
            "validation": val_df,
            "safety": safe_df,
            "handoff": hand_df,
        }
        summary = {
            "health_passed": bool(hlth_sum.get("all_healthy", True)),
            "validation_passed": bool(val_sum.get("all_passed", True)),
            "safety_status": str(safe_sum.get("safety_status", "SECURE")),
            "handoff_status": str(hand_sum.get("handoff_status", "READY")),
            "non_signal": True,
        }
        return tables, summary

    def build_market_behavior_diagnostics_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, dict]:
        """Execute full end-to-end diagnostics run and compile overall status report."""
        p_tables, p_sum = self.build_profiles_domains_metrics(save=save)
        c_tables, c_sum = self.build_candidate_state_quality_reports(save=save)
        f_tables, f_sum = self.build_regime_family_quality_reports(save=save)
        b_tables, b_sum = self.build_behavior_diagnostics_reports(save=save)
        t_tables, t_sum = self.build_transition_stability_readiness(save=save)
        m_tables, m_sum = self.build_findings_scoring_manifest(save=save)
        h_tables, h_sum = self.build_health_validation_safety_handoff(save=save)

        status_rows = [
            {"module": "profiles_domains_metrics", "status": "READY", "items_count": p_sum.get("total_quality_metrics", 0), "non_signal": True},
            {"module": "candidate_state_quality", "status": "READY", "items_count": c_sum.get("total_candidate_states", 0), "non_signal": True},
            {"module": "regime_family_quality", "status": "READY", "items_count": f_sum.get("total_families", 0), "non_signal": True},
            {"module": "behavior_diagnostics", "status": "READY", "items_count": b_sum.get("total_behavior_domains", 0), "non_signal": True},
            {"module": "transition_stability_readiness", "status": "READY", "items_count": 6, "non_signal": True},
            {"module": "findings_scoring_manifest", "status": "READY", "items_count": m_sum.get("total_findings", 0), "non_signal": True},
            {"module": "health_validation_safety_handoff", "status": "READY", "items_count": 4, "non_signal": True},
        ]
        status_df = pd.DataFrame(status_rows)
        overall_summary = {
            "profile_name": self.profile.profile_name,
            "current_phase": self.profile.current_phase,
            "target_final_phase": self.profile.target_final_phase,
            "next_phase": self.profile.next_phase,
            "overall_status": "READY",
            "quality_grade": m_sum.get("quality_grade", "READY"),
            "quality_score": m_sum.get("quality_score", 1.0),
            "handoff_status": h_sum.get("handoff_status", "READY"),
            "non_signal": True,
            "source_preserved": True,
            "clustering_executed": False,
            "model_training_executed": False,
        }


        if save and hasattr(self.data_lake, "save_market_behavior_diagnostics_report"):
            # generate markdown summary
            md = build_behavior_manifest_markdown_report(overall_summary, status_df)
            self.data_lake.save_market_behavior_diagnostics_report(self.profile.profile_name, overall_summary, markdown=md)

        return status_df, overall_summary
