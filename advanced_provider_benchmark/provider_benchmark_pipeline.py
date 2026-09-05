from pathlib import Path
from typing import Tuple, Dict, Any, Optional
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import (
    ProviderBenchmarkProfile,
    get_default_provider_benchmark_profile,
)
from advanced_provider_benchmark.provider_benchmark_profile_registry import (
    build_provider_benchmark_profile_registry,
)
from advanced_provider_benchmark.provider_benchmark_domain_registry import (
    build_provider_benchmark_domain_registry,
)
from advanced_provider_benchmark.provider_benchmark_metric_registry import (
    build_provider_benchmark_metric_registry,
)
from advanced_provider_benchmark.provider_benchmark_weight_registry import (
    build_provider_benchmark_weight_registry,
)
from advanced_provider_benchmark.provider_coverage_benchmark import (
    build_provider_coverage_benchmark_report,
)
from advanced_provider_benchmark.provider_capability_benchmark import (
    build_provider_capability_benchmark_report,
)
from advanced_provider_benchmark.provider_quality_benchmark import (
    build_provider_quality_benchmark_report,
)
from advanced_provider_benchmark.provider_normalization_benchmark import (
    build_provider_normalization_benchmark_report,
)
from advanced_provider_benchmark.provider_traceability_benchmark import (
    build_provider_traceability_benchmark_report,
)
from advanced_provider_benchmark.provider_license_provenance_benchmark import (
    build_provider_license_provenance_benchmark_report,
)
from advanced_provider_benchmark.provider_no_scraping_compliance import (
    build_provider_no_scraping_compliance_report,
)
from advanced_provider_benchmark.provider_metadata_only_compliance import (
    build_provider_metadata_only_compliance_report,
)
from advanced_provider_benchmark.provider_manual_review_benchmark import (
    build_provider_manual_review_benchmark_report,
)
from advanced_provider_benchmark.fx_provider_benchmark import (
    build_fx_provider_benchmark_report,
)
from advanced_provider_benchmark.commodity_provider_benchmark import (
    build_commodity_provider_benchmark_report,
)
from advanced_provider_benchmark.macro_provider_benchmark import (
    build_macro_provider_benchmark_report,
)
from advanced_provider_benchmark.calendar_provider_benchmark import (
    build_calendar_provider_benchmark_report,
)
from advanced_provider_benchmark.news_metadata_provider_benchmark import (
    build_news_metadata_provider_benchmark_report,
)
from advanced_provider_benchmark.cross_domain_provider_benchmark import (
    build_cross_domain_provider_benchmark_report,
)
from advanced_provider_benchmark.provider_benchmark_scoring import (
    build_provider_benchmark_score_report,
)
from advanced_provider_benchmark.provider_ranking_research import (
    build_provider_ranking_research_report,
)
from advanced_provider_benchmark.provider_benchmark_findings import (
    build_provider_benchmark_findings_registry,
)
from advanced_provider_benchmark.provider_benchmark_manual_review_queue import (
    build_provider_benchmark_manual_review_queue,
)
from advanced_provider_benchmark.provider_benchmark_health import (
    build_provider_benchmark_health_check,
)
from advanced_provider_benchmark.provider_benchmark_validation import (
    build_provider_benchmark_validation_report,
)
from advanced_provider_benchmark.provider_benchmark_safety_boundary import (
    build_provider_benchmark_safety_boundary,
)
from advanced_provider_benchmark.phase_116_handoff import (
    build_phase_116_indicator_feature_factor_engine_handoff_report,
)
from advanced_provider_benchmark.provider_benchmark_report_builder import (
    build_provider_benchmark_profile_markdown_report,
    build_provider_benchmark_metric_markdown_report,
    build_provider_coverage_markdown_report,
    build_provider_capability_markdown_report,
    build_provider_quality_markdown_report,
    build_provider_normalization_markdown_report,
    build_provider_traceability_markdown_report,
    build_provider_compliance_markdown_report,
    build_domain_provider_benchmark_markdown_report,
    build_cross_domain_provider_benchmark_markdown_report,
    build_provider_benchmark_score_markdown_report,
    build_provider_ranking_research_markdown_report,
    build_provider_benchmark_findings_markdown_report,
    build_provider_benchmark_manual_review_markdown_report,
    build_provider_benchmark_health_markdown_report,
    build_provider_benchmark_validation_markdown_report,
    build_provider_benchmark_safety_markdown_report,
    build_phase_116_handoff_markdown_report,
)


class ProviderBenchmarkPipeline:
    def __init__(
        self,
        data_lake: Any,
        settings: Any,
        project_root: Path,
        profile: Optional[ProviderBenchmarkProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = Path(project_root)
        self.profile = profile or get_default_provider_benchmark_profile()

    def build_profiles_domains_metrics(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        prof_df, prof_sum = build_provider_benchmark_profile_registry(self.profile)
        dom_df, dom_sum = build_provider_benchmark_domain_registry(self.profile)
        met_df, met_sum = build_provider_benchmark_metric_registry(self.profile)
        wgt_df, wgt_sum = build_provider_benchmark_weight_registry(self.profile)

        tables = {
            "profiles": prof_df,
            "domains": dom_df,
            "metrics": met_df,
            "weights": wgt_df,
        }
        summary = {
            "profile_summary": prof_sum,
            "domain_summary": dom_sum,
            "metric_summary": met_sum,
            "weight_summary": wgt_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_provider_benchmark_profile_registry(prof_df, prof_sum)
            self.data_lake.save_provider_benchmark_domain_registry(dom_df, dom_sum)
            self.data_lake.save_provider_benchmark_metric_registry(met_df, met_sum)
            self.data_lake.save_provider_benchmark_weight_registry(wgt_df, wgt_sum)

        return tables, summary

    def build_core_benchmarks(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        cov_df, cov_sum = build_provider_coverage_benchmark_report(self.profile)
        cap_df, cap_sum = build_provider_capability_benchmark_report(self.profile)
        qual_df, qual_sum = build_provider_quality_benchmark_report(self.profile)
        norm_df, norm_sum = build_provider_normalization_benchmark_report(self.profile)
        trace_df, trace_sum = build_provider_traceability_benchmark_report(self.profile)
        lic_df, lic_sum = build_provider_license_provenance_benchmark_report(self.profile)
        noscrap_df, noscrap_sum = build_provider_no_scraping_compliance_report(self.profile)
        meta_df, meta_sum = build_provider_metadata_only_compliance_report(self.profile)
        manrev_df, manrev_sum = build_provider_manual_review_benchmark_report(self.profile)

        tables = {
            "coverage": cov_df,
            "capability": cap_df,
            "quality": qual_df,
            "normalization": norm_df,
            "traceability": trace_df,
            "license_provenance": lic_df,
            "no_scraping": noscrap_df,
            "metadata_only": meta_df,
            "manual_review": manrev_df,
        }
        summary = {
            "coverage_summary": cov_sum,
            "capability_summary": cap_sum,
            "quality_summary": qual_sum,
            "normalization_summary": norm_sum,
            "traceability_summary": trace_sum,
            "license_provenance_summary": lic_sum,
            "no_scraping_summary": noscrap_sum,
            "metadata_only_summary": meta_sum,
            "manual_review_summary": manrev_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_provider_coverage_benchmark_report(cov_df, cov_sum)
            self.data_lake.save_provider_capability_benchmark_report(cap_df, cap_sum)
            self.data_lake.save_provider_quality_benchmark_report(qual_df, qual_sum)
            self.data_lake.save_provider_normalization_benchmark_report(norm_df, norm_sum)
            self.data_lake.save_provider_traceability_benchmark_report(trace_df, trace_sum)
            self.data_lake.save_provider_license_provenance_benchmark_report(lic_df, lic_sum)
            self.data_lake.save_provider_no_scraping_compliance_report(noscrap_df, noscrap_sum)
            self.data_lake.save_provider_metadata_only_compliance_report(meta_df, meta_sum)
            self.data_lake.save_provider_manual_review_benchmark_report(manrev_df, manrev_sum)

        return tables, summary

    def build_domain_benchmarks(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        fx_df, fx_sum = build_fx_provider_benchmark_report(self.profile)
        com_df, com_sum = build_commodity_provider_benchmark_report(self.profile)
        mac_df, mac_sum = build_macro_provider_benchmark_report(self.profile)
        cal_df, cal_sum = build_calendar_provider_benchmark_report(self.profile)
        news_df, news_sum = build_news_metadata_provider_benchmark_report(self.profile)

        tables = {
            "fx_benchmark": fx_df,
            "commodity_benchmark": com_df,
            "macro_benchmark": mac_df,
            "calendar_benchmark": cal_df,
            "news_metadata_benchmark": news_df,
        }
        summary = {
            "fx_summary": fx_sum,
            "commodity_summary": com_sum,
            "macro_summary": mac_sum,
            "calendar_summary": cal_sum,
            "news_metadata_summary": news_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_fx_provider_benchmark_report(fx_df, fx_sum)
            self.data_lake.save_commodity_provider_benchmark_report(com_df, com_sum)
            self.data_lake.save_macro_provider_benchmark_report(mac_df, mac_sum)
            self.data_lake.save_calendar_provider_benchmark_report(cal_df, cal_sum)
            self.data_lake.save_news_metadata_provider_benchmark_report(news_df, news_sum)

        return tables, summary

    def build_cross_domain_benchmarks(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        cd_df, cd_sum = build_cross_domain_provider_benchmark_report(self.profile)
        tables = {"cross_domain": cd_df}
        summary = {"cross_domain_summary": cd_sum}

        if save and self.data_lake is not None:
            self.data_lake.save_cross_domain_provider_benchmark_report(cd_df, cd_sum)

        return tables, summary

    def build_scores_rankings_findings(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        scr_df, scr_sum = build_provider_benchmark_score_report(self.profile)
        rnk_df, rnk_sum = build_provider_ranking_research_report(self.profile)
        fnd_df, fnd_sum = build_provider_benchmark_findings_registry(self.profile)
        rev_df, rev_sum = build_provider_benchmark_manual_review_queue(fnd_df, self.profile)

        tables = {
            "scores": scr_df,
            "ranking": rnk_df,
            "findings": fnd_df,
            "manual_review_queue": rev_df,
        }
        summary = {
            "score_summary": scr_sum,
            "ranking_summary": rnk_sum,
            "findings_summary": fnd_sum,
            "manual_review_queue_summary": rev_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_provider_benchmark_score_report(scr_df, scr_sum)
            self.data_lake.save_provider_ranking_research_report(rnk_df, rnk_sum)
            self.data_lake.save_provider_benchmark_findings_registry(fnd_df, fnd_sum)
            self.data_lake.save_provider_benchmark_manual_review_queue(rev_df, rev_sum)

        return tables, summary

    def build_health_validation_safety_and_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        hlth_df, hlth_sum = build_provider_benchmark_health_check(self.project_root, self.profile)
        safe_df, safe_sum = build_provider_benchmark_safety_boundary(self.profile)
        h116_df, h116_sum = build_phase_116_indicator_feature_factor_engine_handoff_report(self.profile)

        tables_to_validate = {
            "health": hlth_df,
            "safety": safe_df,
            "handoff": h116_df,
        }
        val_df, val_sum = build_provider_benchmark_validation_report(tables_to_validate, self.profile)

        tables = {
            "health": hlth_df,
            "validation": val_df,
            "safety": safe_df,
            "phase_116_handoff": h116_df,
        }
        summary = {
            "health_summary": hlth_sum,
            "validation_summary": val_sum,
            "safety_summary": safe_sum,
            "phase_116_handoff_summary": h116_sum,
        }

        if save and self.data_lake is not None:
            self.data_lake.save_provider_benchmark_health_check(hlth_df, hlth_sum)
            self.data_lake.save_provider_benchmark_validation_report(val_df, val_sum)
            self.data_lake.save_provider_benchmark_safety_boundary(safe_df, safe_sum)
            self.data_lake.save_phase_116_indicator_feature_factor_engine_handoff_report(h116_df, h116_sum)

        return tables, summary

    def build_provider_benchmark_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        t_pdm, s_pdm = self.build_profiles_domains_metrics(save=save)
        t_core, s_core = self.build_core_benchmarks(save=save)
        t_dom, s_dom = self.build_domain_benchmarks(save=save)
        t_cd, s_cd = self.build_cross_domain_benchmarks(save=save)
        t_srf, s_srf = self.build_scores_rankings_findings(save=save)
        t_hvs, s_hvs = self.build_health_validation_safety_and_handoff(save=save)

        status_rows = [
            {"component": "profiles_domains_metrics", "status": "READY", "records": len(t_pdm["profiles"]) + len(t_pdm["metrics"])},
            {"component": "core_benchmarks", "status": "READY", "records": len(t_core["coverage"]) + len(t_core["quality"]) + len(t_core["normalization"])},
            {"component": "domain_benchmarks", "status": "READY", "records": len(t_dom["fx_benchmark"]) + len(t_dom["commodity_benchmark"]) + len(t_dom["macro_benchmark"])},
            {"component": "cross_domain_benchmarks", "status": "READY", "records": len(t_cd["cross_domain"])},
            {"component": "scores_rankings_findings", "status": "READY", "records": len(t_srf["scores"]) + len(t_srf["ranking"])},
            {"component": "health_validation_safety", "status": "READY", "records": len(t_hvs["health"]) + len(t_hvs["validation"])},
            {"component": "phase_116_handoff", "status": "READY", "records": len(t_hvs["phase_116_handoff"])},
        ]
        status_df = pd.DataFrame.from_records(status_rows)
        overall_summary = {
            "current_phase": 115,
            "phase_name": "Data Provider Benchmark Report",
            "target_final_phase": 160,
            "next_phase": 116,
            "total_subsystems": len(status_df),
            "all_subsystems_ready": True,
            "mean_benchmark_score": s_srf["score_summary"].get("mean_benchmark_score", 0.0),
        }

        if save and self.data_lake is not None:
            self.data_lake.save_provider_benchmark_report(
                self.profile.name,
                overall_summary,
                build_provider_benchmark_profile_markdown_report(s_pdm["profile_summary"], t_pdm["profiles"]),
            )

        return status_df, overall_summary
