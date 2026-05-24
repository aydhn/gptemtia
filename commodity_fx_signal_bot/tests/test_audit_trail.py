import pandas as pd

from governance.audit_trail import AuditTrail, build_audit_events_from_inventory
from governance.governance_models import AuditTrailRecord


def test_add_load_event(tmp_path):
    audit_dir = tmp_path / "gov"
    audit = AuditTrail(audit_dir)

    rec = AuditTrailRecord("id1", "artifact_created", "a1", "actor", "now", "desc", {}, [])
    audit.add_event(rec)

    df = audit.load_events()
    assert not df.empty
    assert df.iloc[0]["audit_id"] == "id1"

def test_build_events_from_inventory():
    inv_df = pd.DataFrame([{"artifact_id": "a1", "file_name": "f", "path": "p"}])
    df, meta = build_audit_events_from_inventory(inv_df)
    assert not df.empty
    assert "artifact_scanned" in df["event_label"].values
