"""
Custody Chain.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile
from local_archival.archival_models import CustodyRehearsalItem, build_custody_rehearsal_item_id, custody_rehearsal_item_to_dict

def build_default_custody_steps(profile: LocalArchivalProfile) -> list[CustodyRehearsalItem]:
    steps = [
        "prepare local archive candidate inventory",
        "review sensitive exclusions",
        "review hash policy",
        "produce hash catalog",
        "produce hash-of-hashes catalog",
        "review provenance lockfile",
        "review delivery manifest references",
        "review acceptance evidence references",
        "record manual reviewer note",
        "record storage location note manually",
        "schedule manual periodic review"
    ]
    items = []
    for step in steps:
        items.append(CustodyRehearsalItem(
            custody_id=build_custody_rehearsal_item_id(step),
            custody_step=step,
            custody_status="custody_rehearsal_ready",
            responsible_role_hint="Analyst/Operator",
            evidence_refs=[],
            warnings=["Not a real chain of custody."]
        ))
    return items

def build_custody_chain_simulation_registry(profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_custody_steps(profile)
    df = pd.DataFrame([custody_rehearsal_item_to_dict(i) for i in items])
    return df, summarize_custody_chain_simulation(df)

def summarize_custody_chain_simulation(custody_df: pd.DataFrame) -> dict:
    return {"total_custody_steps": len(custody_df) if custody_df is not None else 0}
