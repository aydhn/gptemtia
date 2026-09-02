import pandas as pd
from pathlib import Path
from local_acceptance.acceptance_config import LocalAcceptanceProfile
from local_acceptance.acceptance_models import AcceptanceChecklistItem, build_acceptance_checklist_item_id, acceptance_checklist_item_to_dict

def build_acceptance_checklist_items(profile: LocalAcceptanceProfile) -> list[AcceptanceChecklistItem]:
    items_def = [
        "final synthesis outputs mevcut",
        "hardening outputs mevcut",
        "safety boundary dokümante",
        "non-use policy dokümante",
        "master indexes mevcut",
        "contract catalogs mevcut",
        "documentation freeze snapshot mevcut",
        "RC dry-run manifest mevcut",
        "quality reports mevcut",
        "acceptance evidence trail üretilebilir",
        "reviewer pack üretilebilir",
        "no-go register üretilebilir",
        "raw secret output yok",
        "live/broker/deploy claim yok",
        "investment advice claim yok"
    ]
    
    items = []
    for nm in items_def:
        items.append(AcceptanceChecklistItem(
            item_id=build_acceptance_checklist_item_id("final_acceptance_domain", nm),
            domain_label="final_acceptance_domain",
            item_name=nm,
            description=f"Check for {nm}",
            status="acceptance_ready_for_rehearsal",
            evidence_refs=[],
            manual_review_required=True,
            warnings=["Bu madde resmi kabul değildir."]
        ))
    return items

def evaluate_acceptance_checklist_items(checklist_df: pd.DataFrame, project_root: Path, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    df = checklist_df.copy()
    if not df.empty:
        df["status"] = "acceptance_ready_for_rehearsal"
        df["manual_review_required"] = True
    return df, {}

def build_final_acceptance_simulation_checklist(project_root: Path, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_acceptance_checklist_items(profile)
    df = pd.DataFrame([acceptance_checklist_item_to_dict(i) for i in items])
    eval_df, _ = evaluate_acceptance_checklist_items(df, project_root, profile)
    summary = summarize_acceptance_simulation(eval_df)
    return eval_df, summary

def summarize_acceptance_simulation(checklist_df: pd.DataFrame) -> dict:
    return {
        "total_items": len(checklist_df),
        "status_counts": checklist_df["status"].value_counts().to_dict() if not checklist_df.empty else {}
    }
