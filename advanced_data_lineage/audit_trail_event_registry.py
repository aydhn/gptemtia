from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile
from advanced_data_lineage.data_lineage_models import (
    AuditTrailEvent,
    build_audit_trail_event_id,
)


def create_audit_trail_event(
    event_type: str,
    dataset_type: str,
    provider_name: str,
    source_id: str,
    related_record_id: str,
    event_note: str,
    manual_review_required: bool = True,
) -> AuditTrailEvent:
    audit_id = build_audit_trail_event_id(event_type, related_record_id)
    return AuditTrailEvent(
        audit_id=audit_id,
        event_type=event_type,
        dataset_type=dataset_type,
        provider_name=provider_name,
        source_id=source_id,
        related_record_id=related_record_id,
        event_note=event_note,
        destructive_action_allowed=False,
        manual_review_required=manual_review_required,
    )


def audit_trail_event_to_dict(event: AuditTrailEvent) -> Dict[str, Any]:
    return event.to_dict()


DEFAULT_AUDIT_EVENTS = [
    ("audit_source_registered", "dataset_fx_quote", "advanced_fx_providers_engine", "prov_src_fx_fixture_provider_fx_dry_run_fixture_source", "ref_prov_src_fx_fixture_provider_fx_dry_run_fixture_source_local_fixture_uri", "FX dry-run fixture registered", False),
    ("audit_provider_registered", "dataset_provider_metadata", "advanced_data_providers_abstraction", "prov_src_public_dataset_placeholder_source", "prov_rec_advanced_data_providers_abstraction", "Multi-provider abstraction registered", False),
    ("audit_schema_linked", "dataset_commodity_spot", "advanced_commodity_providers_engine", "prov_src_commodity_fixture_provider_commodity_dry_run_fixture_source", "schema_prov_dataset_commodity_spot_v1_0", "Commodity spot canonical schema v1.0 linked", False),
    ("audit_quality_finding_linked", "dataset_fx_quote", "advanced_fx_providers_engine", "prov_src_fx_fixture_provider_fx_dry_run_fixture_source", "qf_lin_001", "Missing quote diagnostic finding registered", True),
    ("audit_normalization_applied", "dataset_macro_timeseries", "advanced_macro_providers_engine", "prov_src_macro_fixture_provider_macro_dry_run_fixture_source", "norm_lin_macro_indicator", "Macro indicator standardized to US_10Y_YIELD", False),
    ("audit_normalized_view_created", "dataset_calendar_event", "advanced_economic_calendar_engine", "prov_src_calendar_fixture_provider_calendar_dry_run_fixture_source", "out_lin_calendar_event", "Calendar normalized view created non-destructively", False),
    ("audit_manual_review_required", "dataset_commodity_spot", "advanced_commodity_providers_engine", "prov_src_commodity_fixture_provider_commodity_dry_run_fixture_source", "rev_lin_002", "Unmapped commodity futures root queued for review", True),
    ("audit_license_boundary_recorded", "dataset_provider_metadata", "licensed_vendor_provider_placeholder", "prov_src_licensed_provider_placeholder_source", "lic_prov_007", "Commercial vendor license policy recorded", True),
    ("audit_copyright_boundary_recorded", "dataset_news_metadata", "advanced_news_metadata_engine", "prov_src_news_fixture_provider_news_metadata_dry_run_fixture_source", "news_data_copyright_check", "Zero full-text copyright boundary verified", False),
    ("audit_metadata_only_boundary_recorded", "dataset_news_metadata", "advanced_news_metadata_engine", "prov_src_news_fixture_provider_news_metadata_dry_run_fixture_source", "meta_prov_news", "Metadata-only provenance policy enforced", False),
    ("audit_phase_115_handoff_created", "dataset_provider_metadata", "advanced_data_lineage_engine", "prov_src_public_dataset_placeholder_source", "handoff_phase_115_provider_benchmark", "Benchmark traceability handoff contract prepared", False),
]


def build_audit_trail_event_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    events: List[AuditTrailEvent] = []
    for ev_type, ds_type, provider, s_id, rel_id, note, rev_req in DEFAULT_AUDIT_EVENTS:
        ev = create_audit_trail_event(
            event_type=ev_type,
            dataset_type=ds_type,
            provider_name=provider,
            source_id=s_id,
            related_record_id=rel_id,
            event_note=note,
            manual_review_required=rev_req,
        )
        events.append(ev)
    df = pd.DataFrame.from_records([e.to_dict() for e in events])
    summary = summarize_audit_trail_events(df)
    return df, summary


def summarize_audit_trail_events(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_audit_events": len(df),
        "event_types": df["event_type"].tolist() if "event_type" in df.columns else [],
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 114,
        "target_final_phase": 160,
    }
