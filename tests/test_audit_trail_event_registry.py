from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.audit_trail_event_registry import (
    build_audit_trail_event_registry,
    create_audit_trail_event,
    summarize_audit_trail_events,
)


def test_audit_trail_events():
    profile = get_default_data_lineage_profile()
    df, summary = build_audit_trail_event_registry(profile)
    assert len(df) >= 8
    assert summary["zero_destructive_actions"] is True
    assert "audit_source_registered" in summary["event_types"]

    ev = create_audit_trail_event("test_event", "fx", "provider1", "src1", "rec1", "sample note")
    assert ev.destructive_action_allowed is False
