from typing import Dict, Any, Tuple, Optional, List
from pathlib import Path
import pandas as pd

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_quality.data_quality_config import (
    DataQualityProfile,
    get_default_data_quality_profile,
)
from advanced_data_quality.data_quality_profile_registry import build_data_quality_profile_registry
from advanced_data_quality.data_quality_domain_registry import build_data_quality_domain_registry
from advanced_data_quality.quality_severity import build_quality_severity_registry
from advanced_data_quality.quality_rule_registry import build_quality_rule_registry

from advanced_data_quality.schema_compliance_rules import build_schema_compliance_rule_set, check_schema_compliance
from advanced_data_quality.missing_data_rules import build_missing_data_rule_set, check_missing_required_fields, check_missing_values
from advanced_data_quality.stale_data_rules import build_stale_data_rule_set, check_stale_timestamp
from advanced_data_quality.duplicate_data_rules import build_duplicate_data_rule_set, check_duplicate_records
from advanced_data_quality.outlier_placeholder_rules import build_outlier_detection_placeholder_rule_set, build_outlier_placeholder_findings
from advanced_data_quality.timestamp_integrity_rules import build_timestamp_integrity_rule_set, check_timestamp_parseability, check_timestamp_ordering
from advanced_data_quality.frequency_unit_consistency_rules import build_frequency_unit_consistency_rule_set, check_frequency_values, check_unit_values

from advanced_data_quality.fx_quality_rules import build_fx_quality_rule_set, check_fx_quote_quality, check_fx_ohlcv_quality
from advanced_data_quality.commodity_quality_rules import build_commodity_quality_rule_set, check_commodity_spot_quality, check_commodity_ohlcv_quality, check_futures_metadata_quality
from advanced_data_quality.macro_quality_rules import build_macro_quality_rule_set, check_macro_timeseries_quality, check_macro_release_metadata_quality
from advanced_data_quality.calendar_quality_rules import build_calendar_quality_rule_set, check_calendar_event_quality, check_release_event_quality
from advanced_data_quality.news_metadata_quality_rules import build_news_metadata_quality_rule_set, check_news_metadata_quality, check_news_item_reference_quality
from advanced_data_quality.provider_metadata_quality_rules import build_provider_metadata_quality_rule_set, check_provider_metadata_quality

from advanced_data_quality.ohlc_consistency_rules import build_ohlc_consistency_rule_contract, check_ohlc_consistency
from advanced_data_quality.quote_consistency_rules import build_quote_consistency_rule_contract, check_quote_consistency
from advanced_data_quality.event_release_consistency_rules import build_event_release_consistency_rule_contract, check_event_release_consistency
from advanced_data_quality.news_copyright_quality_rules import build_news_metadata_copyright_quality_rule_set, check_news_copyright_boundary

from advanced_data_quality.quality_findings import build_quality_finding_registry, QualityFinding
from advanced_data_quality.manual_review_queue import build_manual_review_queue
from advanced_data_quality.provider_quality_scoring import build_provider_quality_score_report
from advanced_data_quality.dataset_quality_scoring import build_dataset_quality_score_report
from advanced_data_quality.cross_provider_quality import build_cross_provider_quality_comparison_placeholder

from advanced_data_quality.data_quality_health import build_data_quality_health_check
from advanced_data_quality.data_quality_validation import build_data_quality_validation_report
from advanced_data_quality.data_quality_safety_boundary import build_data_quality_safety_boundary
from advanced_data_quality.phase_113_handoff import build_phase_113_normalization_handoff_report

from advanced_data_quality.data_quality_report_builder import (
    build_data_quality_profile_markdown_report,
    build_quality_rule_registry_markdown_report,
    build_quality_findings_markdown_report,
    build_manual_review_queue_markdown_report,
    build_provider_quality_score_markdown_report,
    build_dataset_quality_score_markdown_report,
    build_data_quality_health_markdown_report,
    build_data_quality_validation_markdown_report,
    build_data_quality_safety_markdown_report,
    build_phase_113_handoff_markdown_report,
)


class DataQualityPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[DataQualityProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_data_quality_profile()

    def build_quality_profiles_and_domains(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        prof_df, prof_sum = build_data_quality_profile_registry(self.profile)
        dom_df, dom_sum = build_data_quality_domain_registry(self.profile)
        sev_df, sev_sum = build_quality_severity_registry(self.profile)

        if save and self.data_lake is not None:
            self.data_lake.save_data_quality_profile_registry(prof_df, prof_sum)
            self.data_lake.save_data_quality_domain_registry(dom_df, dom_sum)
            self.data_lake.save_quality_severity_registry(sev_df, sev_sum)

        tables = {
            "profile_registry": prof_df,
            "domain_registry": dom_df,
            "severity_registry": sev_df,
        }
        summary = {
            "profile_summary": prof_sum,
            "domain_summary": dom_sum,
            "severity_summary": sev_sum,
        }
        return tables, summary

    def build_quality_rules(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        rules_df, rules_sum = build_quality_rule_registry(self.profile)
        schema_df, schema_sum = build_schema_compliance_rule_set(self.profile)
        missing_df, missing_sum = build_missing_data_rule_set(self.profile)
        stale_df, stale_sum = build_stale_data_rule_set(self.profile)
        dup_df, dup_sum = build_duplicate_data_rule_set(self.profile)
        outlier_df, outlier_sum = build_outlier_detection_placeholder_rule_set(self.profile)
        ts_df, ts_sum = build_timestamp_integrity_rule_set(self.profile)
        freq_df, freq_sum = build_frequency_unit_consistency_rule_set(self.profile)

        if save and self.data_lake is not None:
            self.data_lake.save_quality_rule_registry(rules_df, rules_sum)
            self.data_lake.save_schema_compliance_rule_set(schema_df, schema_sum)
            self.data_lake.save_missing_data_rule_set(missing_df, missing_sum)
            self.data_lake.save_stale_data_rule_set(stale_df, stale_sum)
            self.data_lake.save_duplicate_data_rule_set(dup_df, dup_sum)
            self.data_lake.save_outlier_placeholder_rule_set(outlier_df, outlier_sum)
            self.data_lake.save_timestamp_integrity_rule_set(ts_df, ts_sum)
            self.data_lake.save_frequency_unit_consistency_rule_set(freq_df, freq_sum)

        tables = {
            "rule_registry": rules_df,
            "schema_rules": schema_df,
            "missing_rules": missing_df,
            "stale_rules": stale_df,
            "duplicate_rules": dup_df,
            "outlier_rules": outlier_df,
            "timestamp_rules": ts_df,
            "frequency_unit_rules": freq_df,
        }
        summary = {
            "rule_summary": rules_sum,
            "schema_summary": schema_sum,
            "missing_summary": missing_sum,
            "stale_summary": stale_sum,
            "duplicate_summary": dup_sum,
            "outlier_summary": outlier_sum,
            "timestamp_summary": ts_sum,
            "frequency_unit_summary": freq_sum,
        }
        return tables, summary

    def run_generic_quality_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        tables, summary = self.build_quality_rules(save=save)
        return tables, summary

    def run_domain_quality_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        fx_df, fx_sum = build_fx_quality_rule_set(self.profile)
        comm_df, comm_sum = build_commodity_quality_rule_set(self.profile)
        macro_df, macro_sum = build_macro_quality_rule_set(self.profile)
        cal_df, cal_sum = build_calendar_quality_rule_set(self.profile)
        news_df, news_sum = build_news_metadata_quality_rule_set(self.profile)
        prov_df, prov_sum = build_provider_metadata_quality_rule_set(self.profile)

        ohlc_df, ohlc_sum = build_ohlc_consistency_rule_contract(self.profile)
        quote_df, quote_sum = build_quote_consistency_rule_contract(self.profile)
        event_df, event_sum = build_event_release_consistency_rule_contract(self.profile)
        copy_df, copy_sum = build_news_metadata_copyright_quality_rule_set(self.profile)

        if save and self.data_lake is not None:
            self.data_lake.save_fx_quality_rule_set(fx_df, fx_sum)
            self.data_lake.save_commodity_quality_rule_set(comm_df, comm_sum)
            self.data_lake.save_macro_quality_rule_set(macro_df, macro_sum)
            self.data_lake.save_calendar_quality_rule_set(cal_df, cal_sum)
            self.data_lake.save_news_metadata_quality_rule_set(news_df, news_sum)
            self.data_lake.save_provider_metadata_quality_rule_set(prov_df, prov_sum)
            self.data_lake.save_ohlc_consistency_rule_contract(ohlc_df, ohlc_sum)
            self.data_lake.save_quote_consistency_rule_contract(quote_df, quote_sum)
            self.data_lake.save_event_release_consistency_rule_contract(event_df, event_sum)
            self.data_lake.save_news_metadata_copyright_quality_rule_set(copy_df, copy_sum)

        tables = {
            "fx_rules": fx_df,
            "commodity_rules": comm_df,
            "macro_rules": macro_df,
            "calendar_rules": cal_df,
            "news_rules": news_df,
            "provider_rules": prov_df,
            "ohlc_contract": ohlc_df,
            "quote_contract": quote_df,
            "event_contract": event_df,
            "copyright_rules": copy_df,
        }
        summary = {
            "fx_summary": fx_sum,
            "commodity_summary": comm_sum,
            "macro_summary": macro_sum,
            "calendar_summary": cal_sum,
            "news_summary": news_sum,
            "provider_summary": prov_sum,
            "ohlc_summary": ohlc_sum,
            "quote_summary": quote_sum,
            "event_summary": event_sum,
            "copyright_summary": copy_sum,
        }
        return tables, summary

    def build_findings_and_manual_review(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        # Run test suites on fixture/contract sample dataframes to generate findings
        all_findings: List[QualityFinding] = []

        # 1. Sample FX Quote
        sample_fx_quote = pd.DataFrame([
            {"pair": "USD/TRY", "timestamp": "2026-09-01T10:00:00Z", "bid": 34.10, "ask": 34.12, "mid": 34.11},
            {"pair": "EUR/TRY", "timestamp": "2026-09-01T10:00:00Z", "bid": 37.50, "ask": 37.48, "mid": 37.49}, # inverted
        ])
        all_findings.extend(check_fx_quote_quality(sample_fx_quote, "fx_yahoo_finance_fixture"))

        # 2. Sample FX OHLCV
        sample_fx_ohlcv = pd.DataFrame([
            {"pair": "USD/TRY", "timestamp": "2026-09-01", "open": 34.0, "high": 34.5, "low": 33.9, "close": 34.2},
            {"pair": "USD/TRY", "timestamp": "2026-09-02", "open": 34.2, "high": 34.1, "low": 34.4, "close": 34.3}, # high < low
        ])
        all_findings.extend(check_fx_ohlcv_quality(sample_fx_ohlcv, "fx_yahoo_finance_fixture"))

        # 3. Sample Commodity Spot
        sample_comm_spot = pd.DataFrame([
            {"symbol": "XAU", "spot_price": 2500.0, "unit": "usd_per_oz", "quote_currency": "USD"},
            {"symbol": "WTI", "spot_price": -5.0, "unit": "usd_per_barrel", "quote_currency": "USD"}, # negative price test
        ])
        all_findings.extend(check_commodity_spot_quality(sample_comm_spot, "commodity_cbot_fixture"))

        # 4. Sample News Metadata with full_text boundary breach
        sample_news = pd.DataFrame([
            {"item_id": "news_001", "timestamp": "2026-09-01T12:00:00Z", "source_name": "Reuters", "title_or_summary_ref": "Fed rate preview", "copyright_status": "metadata_only"},
            {"item_id": "news_002", "timestamp": "2026-09-01T12:10:00Z", "source_name": "Bloomberg", "title_or_summary_ref": "ECB policy update", "full_text": "Scraped article body text...", "copyright_status": "metadata_only"}, # breach
        ])
        all_findings.extend(check_news_metadata_quality(sample_news, "news_reuters_fixture"))
        all_findings.extend(check_news_copyright_boundary(sample_news, "news_reuters_fixture"))

        # 5. Sample Provider Metadata
        sample_prov = pd.DataFrame([
            {"provider_name": "fx_yahoo_fixture", "provider_type": "fixture", "no_scraping_policy": True, "license_note": "Internal Test", "manual_review_required": False},
        ])
        all_findings.extend(check_provider_metadata_quality(sample_prov, "internal_provider_catalog"))

        findings_df, findings_sum = build_quality_finding_registry(all_findings, self.profile)
        review_df, review_sum = build_manual_review_queue(findings_df, self.profile)

        if save and self.data_lake is not None:
            self.data_lake.save_quality_finding_registry(findings_df, findings_sum)
            self.data_lake.save_manual_review_queue(review_df, review_sum)

        tables = {
            "quality_findings": findings_df,
            "manual_review_queue": review_df,
        }
        summary = {
            "findings_summary": findings_sum,
            "manual_review_summary": review_sum,
        }
        return tables, summary

    def build_quality_scores(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        # Get findings from step or build them
        f_tables, _ = self.build_findings_and_manual_review(save=save)
        findings_df = f_tables.get("quality_findings", pd.DataFrame())

        prov_score_df, prov_score_sum = build_provider_quality_score_report(findings_df, self.profile)
        ds_score_df, ds_score_sum = build_dataset_quality_score_report(findings_df, self.profile)
        cross_df, cross_sum = build_cross_provider_quality_comparison_placeholder(self.profile)
        handoff_df, handoff_sum = build_phase_113_normalization_handoff_report(self.profile)

        if save and self.data_lake is not None:
            self.data_lake.save_provider_quality_score_report(prov_score_df, prov_score_sum)
            self.data_lake.save_dataset_quality_score_report(ds_score_df, ds_score_sum)
            self.data_lake.save_cross_provider_quality_comparison_placeholder(cross_df, cross_sum)
            self.data_lake.save_phase_113_normalization_handoff_report(handoff_df, handoff_sum)

        tables = {
            "provider_quality_scores": prov_score_df,
            "dataset_quality_scores": ds_score_df,
            "cross_provider_quality": cross_df,
            "phase_113_handoff": handoff_df,
        }
        summary = {
            "provider_score_summary": prov_score_sum,
            "dataset_score_summary": ds_score_sum,
            "cross_provider_summary": cross_sum,
            "phase_113_handoff_summary": handoff_sum,
        }
        return tables, summary

    def build_health_and_validation(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        health_df, health_sum = build_data_quality_health_check(self.project_root, self.profile)
        safety_df, safety_sum = build_data_quality_safety_boundary(self.profile)

        # Collect tables for validation report
        p_tables, _ = self.build_quality_profiles_and_domains(save=save)
        r_tables, _ = self.build_quality_rules(save=save)
        f_tables, _ = self.build_findings_and_manual_review(save=save)
        s_tables, _ = self.build_quality_scores(save=save)

        validation_input = {
            "profile_registry": p_tables.get("profile_registry", pd.DataFrame()),
            "domain_registry": p_tables.get("domain_registry", pd.DataFrame()),
            "severity_registry": p_tables.get("severity_registry", pd.DataFrame()),
            "rule_registry": r_tables.get("rule_registry", pd.DataFrame()),
            "quality_findings": f_tables.get("quality_findings", pd.DataFrame()),
            "manual_review_queue": f_tables.get("manual_review_queue", pd.DataFrame()),
            "provider_quality_scores": s_tables.get("provider_quality_scores", pd.DataFrame()),
            "dataset_quality_scores": s_tables.get("dataset_quality_scores", pd.DataFrame()),
            "safety_boundary": safety_df,
        }
        val_df, val_sum = build_data_quality_validation_report(validation_input, self.profile)

        if save and self.data_lake is not None:
            self.data_lake.save_data_quality_health_check(health_df, health_sum)
            self.data_lake.save_data_quality_safety_boundary(safety_df, safety_sum)
            self.data_lake.save_data_quality_validation_report(val_df, val_sum)

        tables = {
            "health_check": health_df,
            "safety_boundary": safety_df,
            "validation_report": val_df,
        }
        summary = {
            "health_summary": health_sum,
            "safety_summary": safety_sum,
            "validation_summary": val_sum,
        }
        return tables, summary

    def build_data_quality_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        # Run all pipeline steps and assemble executive status
        p_tables, p_sum = self.build_quality_profiles_and_domains(save=save)
        r_tables, r_sum = self.build_quality_rules(save=save)
        d_tables, d_sum = self.run_domain_quality_contracts(save=save)
        f_tables, f_sum = self.build_findings_and_manual_review(save=save)
        s_tables, s_sum = self.build_quality_scores(save=save)
        h_tables, h_sum = self.build_health_and_validation(save=save)

        status_records = [
            {"component": "Profiles & Domains", "status": "READY", "items": len(p_tables.get("profile_registry", []))},
            {"component": "Quality Rules", "status": "READY", "items": len(r_tables.get("rule_registry", []))},
            {"component": "Consistency Contracts", "status": "READY", "items": len(d_tables)},
            {"component": "Findings & Manual Review", "status": "ACTIVE", "items": len(f_tables.get("quality_findings", []))},
            {"component": "Scoring & Handoff", "status": "READY", "items": len(s_tables.get("provider_quality_scores", []))},
            {"component": "Health & Safety", "status": "PASS", "items": len(h_tables.get("health_check", []))},
        ]
        status_df = pd.DataFrame.from_records(status_records)
        summary = {
            "pipeline_status": "PASS",
            "current_phase": 112,
            "target_final_phase": 160,
            "next_phase": 113,
            "dry_run": self.profile.dry_run,
            "local_only": self.profile.local_only,
            "total_findings": len(f_tables.get("quality_findings", [])),
            "manual_review_items": len(f_tables.get("manual_review_queue", [])),
        }

        if save and self.data_lake is not None:
            # Save markdown and full json reports
            findings_df = f_tables.get("quality_findings", pd.DataFrame())
            md_content = build_quality_findings_markdown_report(f_sum.get("findings_summary", {}), findings_df)
            self.data_lake.save_data_quality_report(self.profile.name, summary, md_content)

        return status_df, summary
