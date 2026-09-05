from pathlib import Path
from typing import Dict, Any, Tuple, Optional, List
import pandas as pd

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_normalization.data_normalization_config import (
    DataNormalizationProfile,
    get_default_data_normalization_profile,
)
from advanced_data_normalization.data_normalization_profile_registry import (
    build_data_normalization_profile_registry,
)
from advanced_data_normalization.data_normalization_domain_registry import (
    build_data_normalization_domain_registry,
)
from advanced_data_normalization.normalization_status import (
    build_normalization_status_registry,
)
from advanced_data_normalization.normalization_rule_registry import (
    build_normalization_rule_registry,
)
from advanced_data_normalization.canonical_schema_registry import (
    build_canonical_schema_registry,
)
from advanced_data_normalization.canonical_field_registry import (
    build_canonical_field_registry,
)
from advanced_data_normalization.schema_version_normalization import (
    build_schema_version_normalization_registry,
)
from advanced_data_normalization.provider_name_normalization import (
    build_provider_name_normalization_registry,
)
from advanced_data_normalization.fx_symbol_normalization_enforcement import (
    build_fx_symbol_normalization_enforcement_report,
    normalize_fx_symbol_dataframe,
)
from advanced_data_normalization.commodity_symbol_normalization_enforcement import (
    build_commodity_symbol_normalization_enforcement_report,
    normalize_commodity_symbol_dataframe,
)
from advanced_data_normalization.macro_indicator_normalization_enforcement import (
    build_macro_indicator_normalization_enforcement_report,
    normalize_macro_indicator_dataframe,
)
from advanced_data_normalization.calendar_event_normalization_enforcement import (
    build_calendar_event_normalization_enforcement_report,
    normalize_calendar_event_dataframe,
)
from advanced_data_normalization.news_topic_tag_normalization_enforcement import (
    build_news_topic_tag_normalization_enforcement_report,
    normalize_news_tags_dataframe,
)
from advanced_data_normalization.region_currency_normalization import (
    build_region_country_currency_normalization_registry,
    normalize_region_currency_dataframe,
)
from advanced_data_normalization.timestamp_timezone_normalization import (
    build_timestamp_timezone_normalization_registry,
    normalize_timestamp_dataframe,
)
from advanced_data_normalization.session_alignment_requirements import (
    build_session_alignment_requirement_registry,
)
from advanced_data_normalization.frequency_normalization import (
    build_frequency_normalization_registry,
    normalize_frequency_dataframe,
)
from advanced_data_normalization.unit_normalization import (
    build_unit_normalization_registry,
    normalize_unit_dataframe,
)
from advanced_data_normalization.numeric_type_normalization import (
    build_numeric_type_normalization_registry,
    normalize_numeric_dataframe,
)
from advanced_data_normalization.string_case_slug_normalization import (
    build_string_case_slug_normalization_registry,
    normalize_string_dataframe,
)
from advanced_data_normalization.duplicate_key_normalization import (
    build_duplicate_key_normalization_registry,
    add_duplicate_key_column,
)
from advanced_data_normalization.normalized_view_models import (
    build_normalized_view_registry,
    create_normalized_view_manifest,
)
from advanced_data_normalization.normalization_findings import (
    build_normalization_finding_registry,
    NormalizationFinding,
)
from advanced_data_normalization.normalization_decisions import (
    build_normalization_decision_registry,
)
from advanced_data_normalization.manual_review_normalization_queue import (
    build_manual_review_normalization_queue,
)
from advanced_data_normalization.normalized_output_writer import (
    build_normalized_output_manifest,
    write_normalized_view_copy,
)
from advanced_data_normalization.normalization_scoring import (
    build_normalization_score_report,
)
from advanced_data_normalization.cross_domain_mapping_report import (
    build_cross_domain_normalized_mapping_report,
)
from advanced_data_normalization.phase_114_handoff import (
    build_phase_114_lineage_provenance_handoff_report,
)
from advanced_data_normalization.data_normalization_health import (
    build_data_normalization_health_check,
)
from advanced_data_normalization.data_normalization_validation import (
    build_data_normalization_validation_report,
)
from advanced_data_normalization.data_normalization_safety_boundary import (
    build_data_normalization_safety_boundary,
)


class DataNormalizationPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[DataNormalizationProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = Path(project_root)
        self.profile = profile or get_default_data_normalization_profile()

    def build_normalization_profiles_and_domains(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        prof_df, prof_sum = build_data_normalization_profile_registry(self.profile)
        dom_df, dom_sum = build_data_normalization_domain_registry(self.profile)
        stat_df, stat_sum = build_normalization_status_registry(self.profile)

        if save and hasattr(self.data_lake, "save_data_normalization_profile_registry"):
            self.data_lake.save_data_normalization_profile_registry(prof_df, prof_sum)
            self.data_lake.save_data_normalization_domain_registry(dom_df, dom_sum)
            self.data_lake.save_normalization_status_registry(stat_df, stat_sum)

        tables = {
            "profile_registry": prof_df,
            "domain_registry": dom_df,
            "status_registry": stat_df,
        }
        summary = {
            "profile_summary": prof_sum,
            "domain_summary": dom_sum,
            "status_summary": stat_sum,
        }
        return tables, summary

    def build_normalization_rules_and_canonical_schema(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        rule_df, rule_sum = build_normalization_rule_registry(self.profile)
        schema_df, schema_sum = build_canonical_schema_registry(self.profile)
        field_df, field_sum = build_canonical_field_registry(self.profile)
        ver_df, ver_sum = build_schema_version_normalization_registry(self.profile)
        prov_df, prov_sum = build_provider_name_normalization_registry(self.profile)

        if save and hasattr(self.data_lake, "save_normalization_rule_registry"):
            self.data_lake.save_normalization_rule_registry(rule_df, rule_sum)
            self.data_lake.save_canonical_schema_registry(schema_df, schema_sum)
            self.data_lake.save_canonical_field_registry(field_df, field_sum)
            self.data_lake.save_schema_version_normalization_registry(ver_df, ver_sum)
            self.data_lake.save_provider_name_normalization_registry(prov_df, prov_sum)

        tables = {
            "rule_registry": rule_df,
            "canonical_schema_registry": schema_df,
            "canonical_field_registry": field_df,
            "schema_version_registry": ver_df,
            "provider_name_registry": prov_df,
        }
        summary = {
            "rule_summary": rule_sum,
            "schema_summary": schema_sum,
            "field_summary": field_sum,
            "schema_version_summary": ver_sum,
            "provider_name_summary": prov_sum,
        }
        return tables, summary

    def run_symbol_indicator_event_tag_normalization(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        fx_df, fx_sum = build_fx_symbol_normalization_enforcement_report(self.profile)
        comm_df, comm_sum = build_commodity_symbol_normalization_enforcement_report(self.profile)
        macro_df, macro_sum = build_macro_indicator_normalization_enforcement_report(self.profile)
        cal_df, cal_sum = build_calendar_event_normalization_enforcement_report(self.profile)
        news_df, news_sum = build_news_topic_tag_normalization_enforcement_report(self.profile)

        if save and hasattr(self.data_lake, "save_fx_symbol_normalization_enforcement_report"):
            self.data_lake.save_fx_symbol_normalization_enforcement_report(fx_df, fx_sum)
            self.data_lake.save_commodity_symbol_normalization_enforcement_report(comm_df, comm_sum)
            self.data_lake.save_macro_indicator_normalization_enforcement_report(macro_df, macro_sum)
            self.data_lake.save_calendar_event_normalization_enforcement_report(cal_df, cal_sum)
            self.data_lake.save_news_topic_tag_normalization_enforcement_report(news_df, news_sum)

        tables = {
            "fx_symbol_report": fx_df,
            "commodity_symbol_report": comm_df,
            "macro_indicator_report": macro_df,
            "calendar_event_report": cal_df,
            "news_topic_tag_report": news_df,
        }
        summary = {
            "fx_symbol_summary": fx_sum,
            "commodity_symbol_summary": comm_sum,
            "macro_indicator_summary": macro_sum,
            "calendar_event_summary": cal_sum,
            "news_topic_tag_summary": news_sum,
        }
        return tables, summary

    def run_region_time_frequency_unit_normalization(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        reg_df, reg_sum = build_region_country_currency_normalization_registry(self.profile)
        ts_df, ts_sum = build_timestamp_timezone_normalization_registry(self.profile)
        sess_df, sess_sum = build_session_alignment_requirement_registry(self.profile)
        freq_df, freq_sum = build_frequency_normalization_registry(self.profile)
        unit_df, unit_sum = build_unit_normalization_registry(self.profile)

        if save and hasattr(self.data_lake, "save_region_country_currency_normalization_registry"):
            self.data_lake.save_region_country_currency_normalization_registry(reg_df, reg_sum)
            self.data_lake.save_timestamp_timezone_normalization_registry(ts_df, ts_sum)
            self.data_lake.save_session_alignment_requirement_registry(sess_df, sess_sum)
            self.data_lake.save_frequency_normalization_registry(freq_df, freq_sum)
            self.data_lake.save_unit_normalization_registry(unit_df, unit_sum)

        tables = {
            "region_currency_registry": reg_df,
            "timestamp_timezone_registry": ts_df,
            "session_alignment_registry": sess_df,
            "frequency_registry": freq_df,
            "unit_registry": unit_df,
        }
        summary = {
            "region_currency_summary": reg_sum,
            "timestamp_timezone_summary": ts_sum,
            "session_alignment_summary": sess_sum,
            "frequency_summary": freq_sum,
            "unit_summary": unit_sum,
        }
        return tables, summary

    def run_numeric_string_duplicate_normalization(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        num_df, num_sum = build_numeric_type_normalization_registry(self.profile)
        str_df, str_sum = build_string_case_slug_normalization_registry(self.profile)
        dup_df, dup_sum = build_duplicate_key_normalization_registry(self.profile)

        if save and hasattr(self.data_lake, "save_numeric_type_normalization_registry"):
            self.data_lake.save_numeric_type_normalization_registry(num_df, num_sum)
            self.data_lake.save_string_case_slug_normalization_registry(str_df, str_sum)
            self.data_lake.save_duplicate_key_normalization_registry(dup_df, dup_sum)

        tables = {
            "numeric_type_registry": num_df,
            "string_slug_registry": str_df,
            "duplicate_key_registry": dup_df,
        }
        summary = {
            "numeric_type_summary": num_sum,
            "string_slug_summary": str_sum,
            "duplicate_key_summary": dup_sum,
        }
        return tables, summary

    def build_normalized_views_and_findings(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        # Run test transformations on representative fixture contracts non-destructively
        findings: List[NormalizationFinding] = []

        # 1. FX quote fixture transformation
        fx_fixture = pd.DataFrame([
            {"timestamp": "2026-03-01 10:00:00", "pair": "EURUSD", "bid": "1.0850", "ask": "1.0852", "provider": "FX Dry Run"},
            {"timestamp": "2026-03-01 10:01:00", "pair": "USD_TRY", "bid": "36.20", "ask": "36.25", "provider": "FX Dry Run"},
            {"timestamp": "2026-03-01 10:02:00", "pair": "INVALID_P", "bid": "bad", "ask": "1.20", "provider": "FX Dry Run"},
        ])
        norm_fx, f_fx = normalize_fx_symbol_dataframe(fx_fixture, field="pair")
        findings.extend(f_fx)
        norm_fx, f_ts = normalize_timestamp_dataframe(norm_fx, timestamp_field="timestamp")
        findings.extend(f_ts)
        norm_fx, f_num = normalize_numeric_dataframe(norm_fx, fields=["bid", "ask"])
        findings.extend(f_num)

        # 2. Commodity spot fixture transformation
        comm_fixture = pd.DataFrame([
            {"timestamp": "2026-03-01 12:00:00", "symbol": "GOLD", "price": "2850.5", "currency": "USDollar", "unit": "USD/oz", "provider": "commodity dry run"},
            {"timestamp": "2026-03-01 12:00:00", "symbol": "CL", "price": "75.2", "currency": "USD", "unit": "USD/barrel", "provider": "commodity dry run"},
        ])
        norm_comm, f_comm = normalize_commodity_symbol_dataframe(comm_fixture, field="symbol")
        findings.extend(f_comm)
        norm_comm, f_cunit = normalize_unit_dataframe(norm_comm, field="unit")
        findings.extend(f_cunit)

        # 3. Macro timeseries fixture transformation
        macro_fixture = pd.DataFrame([
            {"timestamp": "2026-02-01", "indicator": "US10Y", "value": "4.25%", "region": "United States", "frequency": "daily", "unit": "%", "provider": "macro official"},
            {"timestamp": "2026-02-01", "indicator": "CPI_US_YOY", "value": "2.8", "region": "USA", "frequency": "monthly", "unit": "percent", "provider": "macro official"},
        ])
        norm_macro, f_mind = normalize_macro_indicator_dataframe(macro_fixture, field="indicator")
        findings.extend(f_mind)
        norm_macro, f_mfreq = normalize_frequency_dataframe(norm_macro, field="frequency")
        findings.extend(f_mfreq)
        norm_macro, f_mreg = normalize_region_currency_dataframe(norm_macro, region_field="region", currency_field="currency")
        findings.extend(f_mreg)

        # Build registries
        manifests = [
            create_normalized_view_manifest("fx_quote_fixture", "dataset_fx_quote", "fx_dry_run_fixture_provider", "raw_fixture", "normalized_views/fx_quote.csv", "v1.0", len(norm_fx), len(norm_fx.columns)),
            create_normalized_view_manifest("commodity_spot_fixture", "dataset_commodity_spot", "commodity_dry_run_fixture_provider", "raw_fixture", "normalized_views/commodity_spot.csv", "v1.0", len(norm_comm), len(norm_comm.columns)),
            create_normalized_view_manifest("macro_timeseries_fixture", "dataset_macro_timeseries", "macro_official_api_provider_placeholder", "raw_fixture", "normalized_views/macro_timeseries.csv", "v1.0", len(norm_macro), len(norm_macro.columns)),
        ]
        view_df, view_sum = build_normalized_view_registry(manifests, self.profile)
        find_df, find_sum = build_normalization_finding_registry(findings, self.profile)
        dec_df, dec_sum = build_normalization_decision_registry(find_df, self.profile)
        queue_df, queue_sum = build_manual_review_normalization_queue(find_df, self.profile)
        out_man_df, out_man_sum = build_normalized_output_manifest(self.profile)

        if save:
            if hasattr(self.data_lake, "save_normalized_view_registry"):
                self.data_lake.save_normalized_view_registry(view_df, view_sum)
                self.data_lake.save_normalization_finding_registry(find_df, find_sum)
                self.data_lake.save_normalization_decision_registry(dec_df, dec_sum)
                self.data_lake.save_manual_review_normalization_queue(queue_df, queue_sum)
                self.data_lake.save_normalized_output_manifest(out_man_df, out_man_sum)
            # Write normalized fixture copies non-destructively
            view_dir = self.project_root / "data" / "lake" / "advanced_data_normalization" / "normalized_views"
            write_normalized_view_copy(norm_fx, view_dir / "fx_quotes_normalized.csv", allow_overwrite=True)
            write_normalized_view_copy(norm_comm, view_dir / "commodity_spot_normalized.csv", allow_overwrite=True)
            write_normalized_view_copy(norm_macro, view_dir / "macro_timeseries_normalized.csv", allow_overwrite=True)

        tables = {
            "normalized_views": view_df,
            "findings_registry": find_df,
            "decision_registry": dec_df,
            "manual_review_queue": queue_df,
            "output_manifest": out_man_df,
            "norm_fx_dataframe": norm_fx,
            "norm_comm_dataframe": norm_comm,
            "norm_macro_dataframe": norm_macro,
        }
        summary = {
            "view_summary": view_sum,
            "finding_summary": find_sum,
            "decision_summary": dec_sum,
            "manual_review_summary": queue_sum,
            "output_manifest_summary": out_man_sum,
        }
        return tables, summary

    def build_normalization_scores_and_mapping(
        self,
        findings_df: Optional[pd.DataFrame] = None,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        f_df = findings_df if findings_df is not None else pd.DataFrame()
        score_df, score_sum = build_normalization_score_report(f_df, self.profile)
        map_df, map_sum = build_cross_domain_normalized_mapping_report(self.profile)

        if save and hasattr(self.data_lake, "save_normalization_score_report"):
            self.data_lake.save_normalization_score_report(score_df, score_sum)
            self.data_lake.save_cross_domain_normalized_mapping_report(map_df, map_sum)

        tables = {
            "score_report": score_df,
            "cross_domain_mapping": map_df,
        }
        summary = {
            "score_summary": score_sum,
            "cross_domain_summary": map_sum,
        }
        return tables, summary

    def build_health_validation_safety_and_handoff(
        self,
        tables_to_validate: Optional[Dict[str, pd.DataFrame]] = None,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        health_df, health_sum = build_data_normalization_health_check(self.project_root, self.profile)
        val_tables = tables_to_validate or {}
        val_df, val_sum = build_data_normalization_validation_report(val_tables, self.profile)
        safety_df, safety_sum = build_data_normalization_safety_boundary(self.profile)
        handoff_df, handoff_sum = build_phase_114_lineage_provenance_handoff_report(self.profile)

        if save and hasattr(self.data_lake, "save_data_normalization_health_check"):
            self.data_lake.save_data_normalization_health_check(health_df, health_sum)
            self.data_lake.save_data_normalization_validation_report(val_df, val_sum)
            self.data_lake.save_data_normalization_safety_boundary(safety_df, safety_sum)
            self.data_lake.save_phase_114_lineage_provenance_handoff_report(handoff_df, handoff_sum)

        tables = {
            "health_check": health_df,
            "validation_report": val_df,
            "safety_boundary": safety_df,
            "phase_114_handoff": handoff_df,
        }
        summary = {
            "health_summary": health_sum,
            "validation_summary": val_sum,
            "safety_summary": safety_sum,
            "handoff_summary": handoff_sum,
        }
        return tables, summary

    def build_data_normalization_status(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        records = [
            {"component": "profile_registry", "status": "READY", "non_destructive": True},
            {"component": "domain_registry", "status": "READY", "non_destructive": True},
            {"component": "status_registry", "status": "READY", "non_destructive": True},
            {"component": "rule_registry", "status": "READY", "non_destructive": True},
            {"component": "canonical_schema_registry", "status": "READY", "non_destructive": True},
            {"component": "canonical_field_registry", "status": "READY", "non_destructive": True},
            {"component": "schema_version_normalization", "status": "READY", "non_destructive": True},
            {"component": "provider_name_normalization", "status": "READY", "non_destructive": True},
            {"component": "fx_symbol_enforcement", "status": "READY", "non_destructive": True},
            {"component": "commodity_symbol_enforcement", "status": "READY", "non_destructive": True},
            {"component": "macro_indicator_enforcement", "status": "READY", "non_destructive": True},
            {"component": "calendar_event_enforcement", "status": "READY", "non_destructive": True},
            {"component": "news_topic_tag_enforcement", "status": "READY", "non_destructive": True},
            {"component": "region_currency_normalization", "status": "READY", "non_destructive": True},
            {"component": "timestamp_timezone_normalization", "status": "READY", "non_destructive": True},
            {"component": "session_alignment_requirements", "status": "READY", "non_destructive": True},
            {"component": "frequency_normalization", "status": "READY", "non_destructive": True},
            {"component": "unit_normalization", "status": "READY", "non_destructive": True},
            {"component": "numeric_type_normalization", "status": "READY", "non_destructive": True},
            {"component": "string_case_slug_normalization", "status": "READY", "non_destructive": True},
            {"component": "duplicate_key_normalization", "status": "READY", "non_destructive": True},
            {"component": "normalized_views", "status": "READY", "non_destructive": True},
            {"component": "findings_registry", "status": "READY", "non_destructive": True},
            {"component": "decision_registry", "status": "READY", "non_destructive": True},
            {"component": "manual_review_queue", "status": "READY", "non_destructive": True},
            {"component": "normalized_output_manifest", "status": "READY", "non_destructive": True},
            {"component": "normalization_scoring", "status": "READY", "non_destructive": True},
            {"component": "cross_domain_mapping", "status": "READY", "non_destructive": True},
            {"component": "data_normalization_health", "status": "READY", "non_destructive": True},
            {"component": "data_normalization_validation", "status": "READY", "non_destructive": True},
            {"component": "data_normalization_safety_boundary", "status": "READY", "non_destructive": True},
            {"component": "phase_114_handoff", "status": "READY", "non_destructive": True},
        ]
        df = pd.DataFrame.from_records(records)
        summary = {
            "total_components": len(df),
            "all_ready": bool((df["status"] == "READY").all()),
            "all_non_destructive": bool(df["non_destructive"].all()),
            "current_phase": 113,
            "target_final_phase": 160,
        }
        return df, summary
