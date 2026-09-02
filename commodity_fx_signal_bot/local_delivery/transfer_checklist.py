import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile
from local_delivery.delivery_models import DeliveryChecklistItem, build_delivery_checklist_id, delivery_checklist_item_to_dict

def build_default_transfer_checklist_items(profile: LocalDeliveryProfile) -> list[DeliveryChecklistItem]:
    names = [
        "README present", "SAFE_USAGE_GUIDE present", "OPERATOR_MANUAL present",
        "CODEX_AGENT_GUIDE present", "PROJECT_COMPLETION_DOSSIER present",
        "FINAL_SAFETY_BOUNDARY_BINDER present", "INDEPENDENT_REVIEWER_PACK present",
        "FINAL_VERIFICATION_EVIDENCE_BINDER present", "RC_DRY_RUN_FREEZE_MANIFEST present",
        "final delivery manifest present", "reports/output present", "data/lake present",
        "scripts present", "tests present", ".env.example present",
        ".env secret excluded", "no-go/safe-go summary present"
    ]
    return [
        DeliveryChecklistItem(
            checklist_id=build_delivery_checklist_id(n),
            checklist_name=n,
            description=f"Check if {n}",
            readiness_label="transfer_ready_for_manual_review",
            evidence_refs=[],
            manual_review_required=True,
            warnings=[]
        ) for n in names
    ]

def build_final_local_transfer_checklist(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_transfer_checklist_items(profile)
    df = pd.DataFrame([delivery_checklist_item_to_dict(i) for i in items])
    return df, summarize_transfer_checklist(df)

def evaluate_transfer_checklist(checklist_df: pd.DataFrame, project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    return checklist_df, summarize_transfer_checklist(checklist_df)

def summarize_transfer_checklist(checklist_df: pd.DataFrame) -> dict:
    return {"total_checklist_items": len(checklist_df)}
