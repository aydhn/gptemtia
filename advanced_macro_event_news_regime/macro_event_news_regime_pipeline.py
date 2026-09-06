"""Phase 132: Macro/Event/News Regime Pipeline.

Coordinates the end-to-end execution of macro indicators, economic calendar,
and news metadata regime context expansion with lookahead-free and non-signal guarantees.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)
from advanced_macro_event_news_regime.macro_event_news_regime_profile_registry import (
    build_macro_event_news_regime_profile_registry,
)
from advanced_macro_event_news_regime.macro_event_news_regime_domain_registry import (
    build_macro_event_news_regime_domain_registry,
)
from advanced_macro_event_news_regime.macro_regime_entities import (
    build_macro_regime_entity_registry,
)
from advanced_macro_event_news_regime.event_regime_entities import (
    build_event_regime_entity_registry,
)
from advanced_macro_event_news_regime.news_metadata_regime_entities import (
    build_news_metadata_regime_entity_registry,
)
from advanced_macro_event_news_regime.macro_regime_context_taxonomy import (
    build_macro_regime_context_taxonomy_registry,
)
from advanced_macro_event_news_regime.event_regime_context_taxonomy import (
    build_event_regime_context_taxonomy_registry,
)
from advanced_macro_event_news_regime.news_metadata_regime_context_taxonomy import (
    build_news_metadata_regime_context_taxonomy_registry,
)
from advanced_macro_event_news_regime.macro_indicator_regime_context import (
    build_macro_indicator_regime_context_registry,
)
from advanced_macro_event_news_regime.macro_release_regime_context import (
    build_macro_release_regime_context_registry,
)
from advanced_macro_event_news_regime.macro_revision_regime_context import (
    build_macro_revision_regime_context_registry,
)
from advanced_macro_event_news_regime.macro_surprise_placeholders import (
    build_macro_surprise_placeholder_registry,
)
from advanced_macro_event_news_regime.calendar_event_regime_context import (
    build_calendar_event_regime_context_registry,
)
from advanced_macro_event_news_regime.event_window_regime_context import (
    build_event_window_regime_context_registry,
)
from advanced_macro_event_news_regime.pre_event_regime_context import (
    build_pre_event_regime_context_registry,
)
from advanced_macro_event_news_regime.post_event_regime_context import (
    build_post_event_regime_context_registry,
)
from advanced_macro_event_news_regime.event_importance_regime_context import (
    build_event_importance_regime_context_registry,
)
from advanced_macro_event_news_regime.release_lag_regime_context import (
    build_release_lag_regime_context_registry,
)
from advanced_macro_event_news_regime.scheduled_actual_release_alignment import (
    build_scheduled_actual_release_alignment_registry,
)
from advanced_macro_event_news_regime.news_topic_regime_context import (
    build_news_topic_regime_context_registry,
)
from advanced_macro_event_news_regime.news_asset_tag_regime_context import (
    build_news_asset_tag_regime_context_registry,
)
from advanced_macro_event_news_regime.news_macro_tag_regime_context import (
    build_news_macro_tag_regime_context_registry,
)
from advanced_macro_event_news_regime.news_event_linkage_regime_context import (
    build_news_event_linkage_regime_context_registry,
)
from advanced_macro_event_news_regime.news_freshness_regime_context_placeholders import (
    build_news_freshness_regime_context_placeholder_registry,
)
from advanced_macro_event_news_regime.metadata_only_news_boundary import (
    build_metadata_only_news_boundary_registry,
)
from advanced_macro_event_news_regime.macro_event_news_cross_asset_context import (
    build_macro_event_news_cross_asset_context_registry,
)
from advanced_macro_event_news_regime.macro_event_news_transition_context import (
    build_macro_event_news_transition_context_registry,
)
from advanced_macro_event_news_regime.macro_event_news_regime_context_contracts import (
    build_macro_event_news_regime_context_contract_registry,
)
from advanced_macro_event_news_regime.macro_event_news_timestamp_policies import (
    build_macro_event_news_timestamp_policy_registry,
)
from advanced_macro_event_news_regime.macro_event_news_asof_join_policies import (
    build_macro_event_news_asof_join_policy_registry,
)
from advanced_macro_event_news_regime.macro_event_news_no_lookahead_guard import (
    build_macro_event_news_no_lookahead_guard_registry,
)
from advanced_macro_event_news_regime.macro_event_news_validation_dependencies import (
    build_macro_event_news_validation_dependency_registry,
)
from advanced_macro_event_news_regime.macro_event_news_quality_dependencies import (
    build_macro_event_news_quality_dependency_registry,
)
from advanced_macro_event_news_regime.macro_event_news_source_phases import (
    build_macro_event_news_source_phase_registry,
)
from advanced_macro_event_news_regime.macro_event_news_context_findings import (
    build_macro_event_news_context_findings_registry,
)
from advanced_macro_event_news_regime.macro_event_news_manual_review import (
    build_macro_event_news_manual_review_queue,
)
from advanced_macro_event_news_regime.macro_event_news_context_scoring import (
    build_macro_event_news_context_score_report,
)
from advanced_macro_event_news_regime.macro_event_news_regime_context_manifest import (
    build_macro_event_news_regime_context_manifest,
)
from advanced_macro_event_news_regime.macro_event_news_regime_health import (
    build_macro_event_news_regime_health_check,
)
from advanced_macro_event_news_regime.macro_event_news_regime_validation import (
    build_macro_event_news_regime_validation_report,
)
from advanced_macro_event_news_regime.macro_event_news_regime_safety_boundary import (
    build_macro_event_news_regime_safety_boundary,
)
from advanced_macro_event_news_regime.phase_133_handoff import (
    build_phase_133_regime_validation_no_lookahead_acceptance_handoff_report,
)
from advanced_macro_event_news_regime.macro_event_news_regime_report_builder import (
    build_macro_event_news_regime_profile_markdown_report,
    build_macro_event_news_entity_markdown_report,
    build_macro_context_markdown_report,
    build_event_context_markdown_report,
    build_news_metadata_context_markdown_report,
    build_metadata_only_boundary_markdown_report,
    build_macro_event_news_cross_asset_markdown_report,
    build_macro_event_news_findings_markdown_report,
    build_macro_event_news_score_markdown_report,
    build_macro_event_news_manifest_markdown_report,
    build_macro_event_news_validation_markdown_report,
    build_macro_event_news_safety_markdown_report,
    build_phase_133_handoff_markdown_report,
)


class MacroEventNewsRegimePipeline:
    """Orchestrates Phase 132 Macro/Event/News Regime Context Expansion."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[MacroEventNewsRegimeProfile] = None,
    ):
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(__file__).resolve().parent.parent
        self.data_lake = data_lake or DataLake(self.project_root)
        self.profile = profile or get_macro_event_news_regime_profile(
            self.settings.default_macro_event_news_regime_profile
        )

    def build_profiles_domains_entities(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build profile, domain, and entity registries."""
        prof_df, prof_summary = build_macro_event_news_regime_profile_registry(self.profile)
        dom_df, dom_summary = build_macro_event_news_regime_domain_registry(self.profile)
        macro_ent_df, macro_ent_summary = build_macro_regime_entity_registry(self.profile)
        event_ent_df, event_ent_summary = build_event_regime_entity_registry(self.profile)
        news_ent_df, news_ent_summary = build_news_metadata_regime_entity_registry(self.profile)

        if save and hasattr(self.data_lake, "save_macro_event_news_regime_profile_registry"):
            self.data_lake.save_macro_event_news_regime_profile_registry(prof_df, prof_summary)
            self.data_lake.save_macro_event_news_regime_domain_registry(dom_df, dom_summary)
            self.data_lake.save_macro_regime_entity_registry(macro_ent_df, macro_ent_summary)
            self.data_lake.save_event_regime_entity_registry(event_ent_df, event_ent_summary)
            self.data_lake.save_news_metadata_regime_entity_registry(news_ent_df, news_ent_summary)

        tables = {
            "profiles": prof_df,
            "domains": dom_df,
            "macro_entities": macro_ent_df,
            "event_entities": event_ent_df,
            "news_metadata_entities": news_ent_df,
        }
        summary = {
            "total_profiles": len(prof_df),
            "total_domains": len(dom_df),
            "total_macro_entities": len(macro_ent_df),
            "total_event_entities": len(event_ent_df),
            "total_news_metadata_entities": len(news_ent_df),
        }
        return tables, summary

    def build_context_taxonomies(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build macro, event, and news context taxonomy registries."""
        macro_tax_df, m_summary = build_macro_regime_context_taxonomy_registry(self.profile)
        event_tax_df, e_summary = build_event_regime_context_taxonomy_registry(self.profile)
        news_tax_df, n_summary = build_news_metadata_regime_context_taxonomy_registry(self.profile)

        if save and hasattr(self.data_lake, "save_macro_regime_context_taxonomy_registry"):
            self.data_lake.save_macro_regime_context_taxonomy_registry(macro_tax_df, m_summary)
            self.data_lake.save_event_regime_context_taxonomy_registry(event_tax_df, e_summary)
            self.data_lake.save_news_metadata_regime_context_taxonomy_registry(news_tax_df, n_summary)

        tables = {
            "macro_taxonomy": macro_tax_df,
            "event_taxonomy": event_tax_df,
            "news_taxonomy": news_tax_df,
        }
        summary = {
            "macro_taxonomies": len(macro_tax_df),
            "event_taxonomies": len(event_tax_df),
            "news_taxonomies": len(news_tax_df),
        }
        return tables, summary

    def build_macro_contexts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build macro indicator, release, revision, and surprise context registries."""
        ind_df, ind_summary = build_macro_indicator_regime_context_registry(self.profile)
        rel_df, rel_summary = build_macro_release_regime_context_registry(self.profile)
        rev_df, rev_summary = build_macro_revision_regime_context_registry(self.profile)
        surp_df, surp_summary = build_macro_surprise_placeholder_registry(self.profile)

        if save and hasattr(self.data_lake, "save_macro_indicator_regime_context_registry"):
            self.data_lake.save_macro_indicator_regime_context_registry(ind_df, ind_summary)
            self.data_lake.save_macro_release_regime_context_registry(rel_df, rel_summary)
            self.data_lake.save_macro_revision_regime_context_registry(rev_df, rev_summary)
            self.data_lake.save_macro_surprise_placeholder_registry(surp_df, surp_summary)

        tables = {
            "macro_indicators": ind_df,
            "macro_releases": rel_df,
            "macro_revisions": rev_df,
            "macro_surprises": surp_df,
        }
        summary = {
            "indicator_contexts": len(ind_df),
            "release_contexts": len(rel_df),
            "revision_contexts": len(rev_df),
            "surprise_placeholders": len(surp_df),
        }
        return tables, summary

    def build_event_contexts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build calendar events, event windows, and release lag context registries."""
        cal_df, cal_summary = build_calendar_event_regime_context_registry(self.profile)
        win_df, win_summary = build_event_window_regime_context_registry(self.profile)
        pre_df, pre_summary = build_pre_event_regime_context_registry(self.profile)
        post_df, post_summary = build_post_event_regime_context_registry(self.profile)
        imp_df, imp_summary = build_event_importance_regime_context_registry(self.profile)
        lag_df, lag_summary = build_release_lag_regime_context_registry(self.profile)
        align_df, align_summary = build_scheduled_actual_release_alignment_registry(self.profile)

        if save and hasattr(self.data_lake, "save_calendar_event_regime_context_registry"):
            self.data_lake.save_calendar_event_regime_context_registry(cal_df, cal_summary)
            self.data_lake.save_event_window_regime_context_registry(win_df, win_summary)
            self.data_lake.save_pre_event_regime_context_registry(pre_df, pre_summary)
            self.data_lake.save_post_event_regime_context_registry(post_df, post_summary)
            self.data_lake.save_event_importance_regime_context_registry(imp_df, imp_summary)
            self.data_lake.save_release_lag_regime_context_registry(lag_df, lag_summary)
            self.data_lake.save_scheduled_actual_release_alignment_registry(align_df, align_summary)

        tables = {
            "calendar_events": cal_df,
            "event_windows": win_df,
            "pre_events": pre_df,
            "post_events": post_df,
            "event_importance": imp_df,
            "release_lag": lag_df,
            "release_alignment": align_df,
        }
        summary = {
            "calendar_events": len(cal_df),
            "event_windows": len(win_df),
            "pre_events": len(pre_df),
            "post_events": len(post_df),
            "release_lags": len(lag_df),
            "alignments": len(align_df),
        }
        return tables, summary

    def build_news_metadata_contexts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build news metadata, topic, tag, linkage, and boundary registries."""
        top_df, top_summary = build_news_topic_regime_context_registry(self.profile)
        asset_df, asset_summary = build_news_asset_tag_regime_context_registry(self.profile)
        mtag_df, mtag_summary = build_news_macro_tag_regime_context_registry(self.profile)
        link_df, link_summary = build_news_event_linkage_regime_context_registry(self.profile)
        fresh_df, fresh_summary = build_news_freshness_regime_context_placeholder_registry(self.profile)
        bound_df, bound_summary = build_metadata_only_news_boundary_registry(self.profile)

        if save and hasattr(self.data_lake, "save_news_topic_regime_context_registry"):
            self.data_lake.save_news_topic_regime_context_registry(top_df, top_summary)
            self.data_lake.save_news_asset_tag_regime_context_registry(asset_df, asset_summary)
            self.data_lake.save_news_macro_tag_regime_context_registry(mtag_df, mtag_summary)
            self.data_lake.save_news_event_linkage_regime_context_registry(link_df, link_summary)
            self.data_lake.save_news_freshness_regime_context_placeholder_registry(fresh_df, fresh_summary)
            self.data_lake.save_metadata_only_news_boundary_registry(bound_df, bound_summary)

        tables = {
            "news_topics": top_df,
            "news_asset_tags": asset_df,
            "news_macro_tags": mtag_df,
            "news_event_linkages": link_df,
            "news_freshness": fresh_df,
            "metadata_boundary": bound_df,
        }
        summary = {
            "topic_contexts": len(top_df),
            "asset_tags": len(asset_df),
            "macro_tags": len(mtag_df),
            "event_linkages": len(link_df),
            "boundary_rules": len(bound_df),
        }
        return tables, summary

    def build_cross_asset_transition_contracts_guards(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build cross-asset context, transition context, contracts, and no-lookahead guards."""
        cross_df, cross_summary = build_macro_event_news_cross_asset_context_registry(self.profile)
        trans_df, trans_summary = build_macro_event_news_transition_context_registry(self.profile)
        cont_df, cont_summary = build_macro_event_news_regime_context_contract_registry(self.profile)
        ts_df, ts_summary = build_macro_event_news_timestamp_policy_registry(self.profile)
        asof_df, asof_summary = build_macro_event_news_asof_join_policy_registry(self.profile)
        guard_df, guard_summary = build_macro_event_news_no_lookahead_guard_registry(self.profile)

        if save and hasattr(self.data_lake, "save_macro_event_news_cross_asset_context_registry"):
            self.data_lake.save_macro_event_news_cross_asset_context_registry(cross_df, cross_summary)
            self.data_lake.save_macro_event_news_transition_context_registry(trans_df, trans_summary)
            self.data_lake.save_macro_event_news_regime_context_contract_registry(cont_df, cont_summary)
            self.data_lake.save_macro_event_news_timestamp_policy_registry(ts_df, ts_summary)
            self.data_lake.save_macro_event_news_asof_join_policy_registry(asof_df, asof_summary)
            self.data_lake.save_macro_event_news_no_lookahead_guard_registry(guard_df, guard_summary)

        tables = {
            "cross_asset_context": cross_df,
            "transition_context": trans_df,
            "contracts": cont_df,
            "timestamp_policies": ts_df,
            "asof_policies": asof_df,
            "no_lookahead_guard": guard_df,
        }
        summary = {
            "cross_asset_contexts": len(cross_df),
            "transition_contexts": len(trans_df),
            "contracts": len(cont_df),
            "guards": len(guard_df),
        }
        return tables, summary

    def build_dependencies_findings_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build dependencies, diagnostic findings, manual review queue, scoring, and manifest."""
        val_dep_df, val_dep_summary = build_macro_event_news_validation_dependency_registry(self.profile)
        qual_dep_df, qual_dep_summary = build_macro_event_news_quality_dependency_registry(self.profile)
        source_df, source_summary = build_macro_event_news_source_phase_registry(self.profile)
        find_df, find_summary = build_macro_event_news_context_findings_registry(self.profile)
        rev_df, rev_summary = build_macro_event_news_manual_review_queue(self.profile)
        score_df, score_summary = build_macro_event_news_context_score_report(self.profile)
        man_df, man_summary = build_macro_event_news_regime_context_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_macro_event_news_validation_dependency_registry"):
            self.data_lake.save_macro_event_news_validation_dependency_registry(val_dep_df, val_dep_summary)
            self.data_lake.save_macro_event_news_quality_dependency_registry(qual_dep_df, qual_dep_summary)
            self.data_lake.save_macro_event_news_source_phase_registry(source_df, source_summary)
            self.data_lake.save_macro_event_news_context_findings_registry(find_df, find_summary)
            self.data_lake.save_macro_event_news_manual_review_queue(rev_df, rev_summary)
            self.data_lake.save_macro_event_news_context_score_report(score_df, score_summary)
            self.data_lake.save_macro_event_news_regime_context_manifest(man_df, man_summary)

        tables = {
            "validation_dependencies": val_dep_df,
            "quality_dependencies": qual_dep_df,
            "source_phases": source_df,
            "findings": find_df,
            "manual_review": rev_df,
            "scoring": score_df,
            "manifest": man_df,
        }
        summary = {
            "validation_dependencies": len(val_dep_df),
            "quality_dependencies": len(qual_dep_df),
            "source_phases": len(source_df),
            "findings": len(find_df),
            "manual_reviews": len(rev_df),
            "context_score": float(score_df["context_score"].iloc[0]),
        }
        return tables, summary

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build health check, safety boundary, validation report, and Phase 133 handoff."""
        prof_df, _ = build_macro_event_news_regime_profile_registry(self.profile)
        bound_df, _ = build_metadata_only_news_boundary_registry(self.profile)
        cont_df, _ = build_macro_event_news_regime_context_contract_registry(self.profile)
        man_df, _ = build_macro_event_news_regime_context_manifest(self.profile)

        val_tables = {
            "profiles": prof_df,
            "boundary": bound_df,
            "contracts": cont_df,
            "manifest": man_df,
        }

        health_df, health_summary = build_macro_event_news_regime_health_check(self.project_root, self.profile)
        safety_df, safety_summary = build_macro_event_news_regime_safety_boundary(self.profile)
        val_df, val_summary = build_macro_event_news_regime_validation_report(val_tables, self.profile)
        handoff_df, handoff_summary = build_phase_133_regime_validation_no_lookahead_acceptance_handoff_report(self.profile)

        if save and hasattr(self.data_lake, "save_macro_event_news_regime_health_check"):
            self.data_lake.save_macro_event_news_regime_health_check(health_df, health_summary)
            self.data_lake.save_macro_event_news_regime_safety_boundary(safety_df, safety_summary)
            self.data_lake.save_macro_event_news_regime_validation_report(val_df, val_summary)
            self.data_lake.save_phase_133_regime_validation_no_lookahead_acceptance_handoff_report(handoff_df, handoff_summary)

        tables = {
            "health": health_df,
            "safety": safety_df,
            "validation": val_df,
            "handoff": handoff_df,
        }
        summary = {
            "health_status": health_summary["overall_status"],
            "safety_status": safety_summary["safety_status"],
            "validation_status": val_summary["validation_status"],
            "handoff_status": handoff_summary["handoff_status"],
        }
        return tables, summary

    def build_macro_event_news_regime_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Run all steps, produce reports, and return status summary DataFrame."""
        t1, s1 = self.build_profiles_domains_entities(save=save)
        t2, s2 = self.build_context_taxonomies(save=save)
        t3, s3 = self.build_macro_contexts(save=save)
        t4, s4 = self.build_event_contexts(save=save)
        t5, s5 = self.build_news_metadata_contexts(save=save)
        t6, s6 = self.build_cross_asset_transition_contracts_guards(save=save)
        t7, s7 = self.build_dependencies_findings_scoring_manifest(save=save)
        t8, s8 = self.build_health_validation_safety_handoff(save=save)

        status_rows = [
            {"component": "profiles_domains_entities", "status": "READY", "items": s1["total_macro_entities"] + s1["total_event_entities"] + s1["total_news_metadata_entities"]},
            {"component": "context_taxonomies", "status": "READY", "items": s2["macro_taxonomies"] + s2["event_taxonomies"] + s2["news_taxonomies"]},
            {"component": "macro_contexts", "status": "READY", "items": s3["indicator_contexts"] + s3["release_contexts"]},
            {"component": "event_contexts", "status": "READY", "items": s4["calendar_events"] + s4["event_windows"]},
            {"component": "news_metadata_contexts", "status": "READY", "items": s5["topic_contexts"] + s5["boundary_rules"]},
            {"component": "cross_asset_transition_guards", "status": "READY", "items": s6["cross_asset_contexts"] + s6["guards"]},
            {"component": "dependencies_manifest", "status": "READY", "items": s7["validation_dependencies"] + s7["findings"]},
            {"component": "health_validation_handoff", "status": "READY", "items": len(t8["health"]) + len(t8["validation"])},
        ]
        status_df = pd.DataFrame(status_rows)

        if save and hasattr(self.data_lake, "save_macro_event_news_regime_report"):
            report_dict = {
                "profile": self.profile.profile_name,
                "current_phase": 132,
                "target_final_phase": 160,
                "next_phase": 133,
                "health": s8["health_status"],
                "validation": s8["validation_status"],
                "safety": s8["safety_status"],
                "handoff": s8["handoff_status"],
                "score": s7["context_score"],
            }
            md_report = build_macro_event_news_manifest_markdown_report(report_dict, t7["manifest"])
            self.data_lake.save_macro_event_news_regime_report(self.profile.profile_name, report_dict, md_report)

        summary = {
            "pipeline_status": "COMPLETED",
            "current_phase": 132,
            "next_phase": 133,
            "health_status": s8["health_status"],
            "validation_status": s8["validation_status"],
            "context_score": s7["context_score"],
            "non_signal": True,
            "source_preserved": True,
        }
        return status_df, summary
