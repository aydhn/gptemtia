import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile
from local_review_governance.review_models import ApprovalLedgerItem, build_approval_ledger_item_id, approval_ledger_item_to_dict

def build_manual_approval_ledger_sections(profile: LocalReviewGovernanceProfile) -> list[dict]:
    return [
        {"title": "Safety boundary reviewed", "content": "Manual review ok."},
        {"title": "No-go/safe-go reviewed", "content": "Manual review ok."},
        {"title": "Quality warnings reviewed", "content": "Manual review ok."},
        {"title": "Atlas reviewed", "content": "Manual review ok."},
        {"title": "Continuity reviewed", "content": "Manual review ok."},
        {"title": "Preservation reviewed", "content": "Manual review ok."},
        {"title": "Completion reviewed", "content": "Manual review ok."},
        {"title": "Release-candidate reviewed", "content": "Manual review ok."},
        {"title": "Incident/redteam/governance reviewed", "content": "Manual review ok."},
        {"title": "No official approval claim", "content": "Rehearsal only."},
        {"title": "Manual review required", "content": "Always required."}
    ]

def build_manual_approval_ledger_rehearsal(profile: LocalReviewGovernanceProfile) -> tuple[str, dict]:
    sections = build_manual_approval_ledger_sections(profile)
    lines = ["# Manual Approval Ledger Rehearsal\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    text = "\n".join(lines)
    return text, summarize_manual_approval_ledger(text)

def summarize_manual_approval_ledger(text: str) -> dict:
    return {"length": len(text)}

def build_default_approval_ledger_items(profile: LocalReviewGovernanceProfile) -> list[ApprovalLedgerItem]:
    return [
        ApprovalLedgerItem(
            ledger_id=build_approval_ledger_item_id("Safety", "approval_rehearsal_manual_review_required"),
            approval_area="Safety",
            approval_status="approval_rehearsal_manual_review_required",
            boundary_note="Not real approval",
            evidence_refs=[],
            manual_review_required=True,
            warnings=["No official signoff"]
        )
    ]

def build_manual_approval_ledger_registry(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_approval_ledger_items(profile)
    df = pd.DataFrame([approval_ledger_item_to_dict(i) for i in items])
    return df, summarize_approval_ledger_registry(df)

def summarize_approval_ledger_registry(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
