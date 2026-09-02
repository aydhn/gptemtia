import pandas as pd
from pathlib import Path
from .governance_control_config import LocalGovernanceControlProfile
from .governance_control_models import ManualApprovalItem, build_manual_approval_id, manual_approval_item_to_dict

def build_default_manual_approval_items(profile: LocalGovernanceControlProfile) -> list[ManualApprovalItem]:
    scopes = [
        "safe usage reviewed",
        "no-go/safe-go reviewed",
        "quality warnings reviewed",
        "generated docs reviewed",
        "DataLake output reviewed",
        "delivery package reviewed",
        "archival/provenance reviewed",
        "closure dossier reviewed",
        "performance budget reviewed",
        "usability path reviewed",
        "simplification candidates reviewed"
    ]
    items = []
    for s in scopes:
        items.append(ManualApprovalItem(
            approval_id=build_manual_approval_id("Rehearsal", s),
            approval_name="Manual Review Rehearsal",
            approval_scope=s,
            approval_status="approval_rehearsal_pending",
            evidence_refs=["doc_evidence"],
            decision_note="Offline rehearsal review required.",
            manual_review_required=True,
            warnings=["Bu gerçek bir onay değildir."]
        ))
    return items

def build_manual_approval_ledger(project_root: Path, profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_manual_approval_items(profile)
    df = pd.DataFrame([manual_approval_item_to_dict(i) for i in items])
    summary = summarize_manual_approval_ledger(df)
    return df, summary

def summarize_manual_approval_ledger(approval_df: pd.DataFrame) -> dict:
    if approval_df is None or approval_df.empty:
        return {"total": 0}
    return {
        "total": len(approval_df),
        "pending": len(approval_df[approval_df["approval_status"] == "approval_rehearsal_pending"])
    }
