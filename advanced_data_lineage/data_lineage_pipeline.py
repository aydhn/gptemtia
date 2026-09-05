from pathlib import Path
from typing import Tuple, Dict, Any, Optional
import pandas as pd

from advanced_data_lineage.data_lineage_config import (
    DataLineageProfile,
    get_default_data_lineage_profile,
)
from advanced_data_lineage.data_lineage_profile_registry import (
    build_data_lineage_profile_registry,
)
from advanced_data_lineage.data_lineage_domain_registry import (
    build_data_lineage_domain_registry,
)
from advanced_data_lineage.provenance_source_registry import (
    build_provenance_source_registry,
)
from advanced_data_lineage.source_reference_registry import (
    build_source_reference_registry,
)
from advanced_data_lineage.provider_provenance_registry import (
    build_provider_provenance_registry,
)
from advanced_data_lineage.dataset_provenance_registry import (
    build_dataset_provenance_registry,
)
from advanced_data_lineage.schema_provenance_registry import (
    build_schema_provenance_registry,
)
from advanced_data_lineage.transformation_provenance_registry import (
    build_transformation_provenance_registry,
)
from advanced_data_lineage.normalization_lineage_registry import (
    build_normalization_lineage_registry,
)
from advanced_data_lineage.quality_finding_lineage_registry import (
    build_quality_finding_lineage_registry,
)
from advanced_data_lineage.manual_review_lineage_registry import (
    build_manual_review_lineage_registry,
)
from advanced_data_lineage.normalized_output_lineage_registry import (
    build_normalized_output_lineage_registry,
)
from advanced_data_lineage.fx_lineage_registry import (
    build_fx_lineage_registry,
)
from advanced_data_lineage.commodity_lineage_registry import (
    build_commodity_lineage_registry,
)
from advanced_data_lineage.macro_lineage_registry import (
    build_macro_lineage_registry,
)
from advanced_data_lineage.calendar_lineage_registry import (
    build_calendar_lineage_registry,
)
from advanced_data_lineage.news_metadata_lineage_registry import (
    build_news_metadata_lineage_registry,
)
from advanced_data_lineage.license_provenance_registry import (
    build_license_provenance_registry,
)
from advanced_data_lineage.copyright_boundary_provenance import (
    build_copyright_boundary_provenance_registry,
)
from advanced_data_lineage.metadata_only_provenance import (
    build_metadata_only_provenance_registry,
)
from advanced_data_lineage.data_usage_boundary_registry import (
    build_data_usage_boundary_registry,
)
from advanced_data_lineage.audit_trail_event_registry import (
    build_audit_trail_event_registry,
)
from advanced_data_lineage.transformation_audit_trail import (
    build_transformation_audit_trail_registry,
)
from advanced_data_lineage.lineage_findings import (
    build_lineage_finding_registry,
)
from advanced_data_lineage.provenance_scoring import (
    build_provenance_confidence_score_report,
)
from advanced_data_lineage.traceability_scoring import (
    build_dataset_traceability_score_report,
    build_provider_traceability_score_report,
)
from advanced_data_lineage.lineage_graph_placeholder import (
    build_lineage_graph_placeholder,
)
from advanced_data_lineage.cross_domain_provenance_map import (
    build_cross_domain_provenance_map,
)
from advanced_data_lineage.phase_115_handoff import (
    build_phase_115_provider_benchmark_handoff_report,
)
from advanced_data_lineage.data_lineage_health import (
    build_data_lineage_health_check,
)
from advanced_data_lineage.data_lineage_validation import (
    build_data_lineage_validation_report,
)
from advanced_data_lineage.data_lineage_safety_boundary import (
    build_data_lineage_safety_boundary,
)
from advanced_data_lineage.data_lineage_report_builder import (
    build_data_lineage_profile_markdown_report,
    build_provenance_source_markdown_report,
    build_provider_provenance_markdown_report,
    build_dataset_provenance_markdown_report,
    build_transformation_provenance_markdown_report,
    build_domain_lineage_markdown_report,
    build_license_copyright_markdown_report,
    build_audit_trail_markdown_report,
    build_lineage_finding_markdown_report,
    build_traceability_score_markdown_report,
    build_cross_domain_provenance_markdown_report,
    build_data_lineage_health_markdown_report,
    build_data_lineage_validation_markdown_report,
    build_data_lineage_safety_markdown_report,
    build_phase_115_handoff_markdown_report,
)


class DataLineagePipeline:
    def __init__(
        self,
        data_lake: Any,
        settings: Any,
        project_root: Path,
        profile: Optional[DataLineageProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_data_lineage_profile()

    def build_lineage_profiles_and_domains(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        prof_df, prof_sum = build_data_lineage_profile_registry(self.profile)
        dom_df, dom_sum = build_data_lineage_domain_registry(self.profile)
        tables = {"profiles": prof_df, "domains": dom_df}
        summary = {"profile_summary": prof_sum, "domain_summary": dom_sum}

        if save and self.data_lake is not None:
            self.data_lake.save_data_lineage_profile_registry(prof_df, prof_sum)
            self.data_lake.save_data_lineage_domain_registry(dom_df, dom_sum)

        return tables, summary

    def build_source_and_provider_provenance(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        src_df, src_sum = build_provenance_source_registry(self.profile)
        ref_df, ref_sum = build_source_reference_registry(self.profile)
        prov_df, prov_sum = build_provider_provenance_registry(self.profile)
        tables = {
            "sources": src_df,
            "source_references": ref_df,
            "providers": prov_df,
        }
        summary = {
            "source_summary": src_sum,
            "reference_summary": ref_sum,
            "provider_summary": prov_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_provenance_source_registry(src_df, src_sum)
            self.data_lake.save_source_reference_registry(ref_df, ref_sum)
            self.data_lake.save_provider_provenance_registry(prov_df, prov_sum)

        return tables, summary

    def build_dataset_schema_transformation_provenance(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        ds_df, ds_sum = build_dataset_provenance_registry(self.profile)
        sch_df, sch_sum = build_schema_provenance_registry(self.profile)
        trans_df, trans_sum = build_transformation_provenance_registry(self.profile)
        tables = {
            "datasets": ds_df,
            "schemas": sch_df,
            "transformations": trans_df,
        }
        summary = {
            "dataset_summary": ds_sum,
            "schema_summary": sch_sum,
            "transformation_summary": trans_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_dataset_provenance_registry(ds_df, ds_sum)
            self.data_lake.save_schema_provenance_registry(sch_df, sch_sum)
            self.data_lake.save_transformation_provenance_registry(trans_df, trans_sum)

        return tables, summary

    def build_normalization_quality_manual_lineage(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        norm_df, norm_sum = build_normalization_lineage_registry(self.profile)
        qf_df, qf_sum = build_quality_finding_lineage_registry(self.profile)
        rev_df, rev_sum = build_manual_review_lineage_registry(self.profile)
        out_df, out_sum = build_normalized_output_lineage_registry(self.profile)
        tables = {
            "normalization_lineage": norm_df,
            "quality_findings_lineage": qf_df,
            "manual_review_lineage": rev_df,
            "normalized_output_lineage": out_df,
        }
        summary = {
            "normalization_summary": norm_sum,
            "quality_finding_summary": qf_sum,
            "manual_review_summary": rev_sum,
            "normalized_output_summary": out_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_normalization_lineage_registry(norm_df, norm_sum)
            self.data_lake.save_quality_finding_lineage_registry(qf_df, qf_sum)
            self.data_lake.save_manual_review_lineage_registry(rev_df, rev_sum)
            self.data_lake.save_normalized_output_lineage_registry(out_df, out_sum)

        return tables, summary

    def build_domain_lineage(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        fx_df, fx_sum = build_fx_lineage_registry(self.profile)
        com_df, com_sum = build_commodity_lineage_registry(self.profile)
        mac_df, mac_sum = build_macro_lineage_registry(self.profile)
        cal_df, cal_sum = build_calendar_lineage_registry(self.profile)
        news_df, news_sum = build_news_metadata_lineage_registry(self.profile)
        tables = {
            "fx_lineage": fx_df,
            "commodity_lineage": com_df,
            "macro_lineage": mac_df,
            "calendar_lineage": cal_df,
            "news_metadata_lineage": news_df,
        }
        summary = {
            "fx_summary": fx_sum,
            "commodity_summary": com_sum,
            "macro_summary": mac_sum,
            "calendar_summary": cal_sum,
            "news_metadata_summary": news_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_fx_lineage_registry(fx_df, fx_sum)
            self.data_lake.save_commodity_lineage_registry(com_df, com_sum)
            self.data_lake.save_macro_lineage_registry(mac_df, mac_sum)
            self.data_lake.save_calendar_lineage_registry(cal_df, cal_sum)
            self.data_lake.save_news_metadata_lineage_registry(news_df, news_sum)

        return tables, summary

    def build_license_copyright_usage_boundaries(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        lic_df, lic_sum = build_license_provenance_registry(self.profile)
        cop_df, cop_sum = build_copyright_boundary_provenance_registry(self.profile)
        meta_df, meta_sum = build_metadata_only_provenance_registry(self.profile)
        use_df, use_sum = build_data_usage_boundary_registry(self.profile)
        tables = {
            "licenses": lic_df,
            "copyright": cop_df,
            "metadata_only": meta_df,
            "usage_boundary": use_df,
        }
        summary = {
            "license_summary": lic_sum,
            "copyright_summary": cop_sum,
            "metadata_only_summary": meta_sum,
            "usage_boundary_summary": use_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_license_provenance_registry(lic_df, lic_sum)
            self.data_lake.save_copyright_boundary_provenance_registry(cop_df, cop_sum)
            self.data_lake.save_metadata_only_provenance_registry(meta_df, meta_sum)
            self.data_lake.save_data_usage_boundary_registry(use_df, use_sum)

        return tables, summary

    def build_audit_findings_and_scores(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        aud_df, aud_sum = build_audit_trail_event_registry(self.profile)
        taud_df, taud_sum = build_transformation_audit_trail_registry(self.profile)
        find_df, find_sum = build_lineage_finding_registry(self.profile)
        pconf_df, pconf_sum = build_provenance_confidence_score_report(self.profile)
        dtrace_df, dtrace_sum = build_dataset_traceability_score_report(self.profile)
        ptrace_df, ptrace_sum = build_provider_traceability_score_report(self.profile)
        graph_df, graph_sum = build_lineage_graph_placeholder(self.profile)

        tables = {
            "audit_trail": aud_df,
            "transformation_audit": taud_df,
            "findings": find_df,
            "provenance_confidence": pconf_df,
            "dataset_traceability": dtrace_df,
            "provider_traceability": ptrace_df,
            "lineage_graph": graph_df,
        }
        summary = {
            "audit_summary": aud_sum,
            "transformation_audit_summary": taud_sum,
            "findings_summary": find_sum,
            "provenance_confidence_summary": pconf_sum,
            "dataset_traceability_summary": dtrace_sum,
            "provider_traceability_summary": ptrace_sum,
            "graph_summary": graph_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_audit_trail_event_registry(aud_df, aud_sum)
            self.data_lake.save_transformation_audit_trail_registry(taud_df, taud_sum)
            self.data_lake.save_lineage_finding_registry(find_df, find_sum)
            self.data_lake.save_provenance_confidence_score_report(pconf_df, pconf_sum)
            self.data_lake.save_dataset_traceability_score_report(dtrace_df, dtrace_sum)
            self.data_lake.save_provider_traceability_score_report(ptrace_df, ptrace_sum)
            self.data_lake.save_lineage_graph_placeholder(graph_df, graph_sum)

        return tables, summary

    def build_cross_domain_and_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        cd_df, cd_sum = build_cross_domain_provenance_map(self.profile)
        h115_df, h115_sum = build_phase_115_provider_benchmark_handoff_report(self.profile)
        tables = {
            "cross_domain": cd_df,
            "phase_115_handoff": h115_df,
        }
        summary = {
            "cross_domain_summary": cd_sum,
            "phase_115_handoff_summary": h115_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_cross_domain_provenance_map(cd_df, cd_sum)
            self.data_lake.save_phase_115_provider_benchmark_handoff_report(h115_df, h115_sum)

        return tables, summary

    def build_health_validation_safety(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        hlth_df, hlth_sum = build_data_lineage_health_check(self.project_root, self.profile)
        safe_df, safe_sum = build_data_lineage_safety_boundary(self.profile)
        tables_to_validate = {
            "health": hlth_df,
            "safety": safe_df,
        }
        val_df, val_sum = build_data_lineage_validation_report(tables_to_validate, self.profile)

        tables = {
            "health": hlth_df,
            "validation": val_df,
            "safety": safe_df,
        }
        summary = {
            "health_summary": hlth_sum,
            "validation_summary": val_sum,
            "safety_summary": safe_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_data_lineage_health_check(hlth_df, hlth_sum)
            self.data_lake.save_data_lineage_validation_report(val_df, val_sum)
            self.data_lake.save_data_lineage_safety_boundary(safe_df, safe_sum)

        return tables, summary

    def build_data_lineage_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        t_prof, s_prof = self.build_lineage_profiles_and_domains(save=save)
        t_prov, s_prov = self.build_source_and_provider_provenance(save=save)
        t_ds, s_ds = self.build_dataset_schema_transformation_provenance(save=save)
        t_norm, s_norm = self.build_normalization_quality_manual_lineage(save=save)
        t_dom, s_dom = self.build_domain_lineage(save=save)
        t_bnd, s_bnd = self.build_license_copyright_usage_boundaries(save=save)
        t_aud, s_aud = self.build_audit_findings_and_scores(save=save)
        t_cd, s_cd = self.build_cross_domain_and_handoff(save=save)
        t_hlth, s_hlth = self.build_health_validation_safety(save=save)

        status_rows = [
            {"component": "profiles_and_domains", "status": "READY", "records": len(t_prof["profiles"]) + len(t_prof["domains"])},
            {"component": "source_and_provider", "status": "READY", "records": len(t_prov["sources"]) + len(t_prov["providers"])},
            {"component": "dataset_and_transformations", "status": "READY", "records": len(t_ds["datasets"]) + len(t_ds["transformations"])},
            {"component": "normalization_and_manifest", "status": "READY", "records": len(t_norm["normalization_lineage"]) + len(t_norm["normalized_output_lineage"])},
            {"component": "domain_lineage", "status": "READY", "records": len(t_dom["fx_lineage"]) + len(t_dom["commodity_lineage"]) + len(t_dom["macro_lineage"]) + len(t_dom["calendar_lineage"]) + len(t_dom["news_metadata_lineage"])},
            {"component": "license_and_copyright_boundary", "status": "READY", "records": len(t_bnd["licenses"]) + len(t_bnd["copyright"])},
            {"component": "audit_trail_and_scoring", "status": "READY", "records": len(t_aud["audit_trail"]) + len(t_aud["dataset_traceability"])},
            {"component": "cross_domain_and_handoff", "status": "READY", "records": len(t_cd["cross_domain"]) + len(t_cd["phase_115_handoff"])},
            {"component": "health_and_validation", "status": "READY", "records": len(t_hlth["health"]) + len(t_hlth["validation"])},
        ]
        status_df = pd.DataFrame.from_records(status_rows)
        overall_summary = {
            "current_phase": 114,
            "phase_name": "Data Lineage and Provenance",
            "target_final_phase": 160,
            "next_phase": 115,
            "total_subsystems": len(status_df),
            "all_subsystems_ready": True,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_data_lineage_report(
                self.profile.name,
                overall_summary,
                build_data_lineage_profile_markdown_report(s_prof["profile_summary"], t_prof["profiles"]),
            )

        return status_df, overall_summary
