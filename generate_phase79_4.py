import os
from pathlib import Path

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = Path(r"c:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\commodity_fx_signal_bot")

write_file(base_dir / "local_archival" / "datalake_hash_rehearsal.py", '''"""
DataLake Hash Rehearsal.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.archive_candidate_inventory import discover_archive_candidate_items
from local_archival.hash_catalog import compute_file_hash_rehearsal

def build_datalake_hash_rehearsal(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_archive_candidate_items(project_root, profile)
    df = df[df["source_layer"] == "datalake"] if "source_layer" in df.columns else pd.DataFrame(columns=df.columns)
    results = []
    for _, row in df.iterrows():
        p = project_root / row["relative_path"]
        if p.exists():
            h_info = compute_file_hash_rehearsal(p, project_root, profile)
            res = row.to_dict()
            res.update(h_info)
            results.append(res)
    res_df = pd.DataFrame(results) if results else pd.DataFrame(columns=["relative_path", "hash_value", "hash_status"])
    return res_df, summarize_datalake_hash_rehearsal(res_df)

def summarize_datalake_hash_rehearsal(df: pd.DataFrame) -> dict:
    return {"total_datalake_items": len(df) if df is not None else 0}
''')

write_file(base_dir / "local_archival" / "scripts_tests_hash_rehearsal.py", '''"""
Scripts Tests Hash Rehearsal.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.archive_candidate_inventory import discover_archive_candidate_items
from local_archival.hash_catalog import compute_file_hash_rehearsal

def build_scripts_tests_hash_rehearsal(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_archive_candidate_items(project_root, profile)
    df = df[df["item_label"].isin(["archival_script_item", "archival_test_item"])] if "item_label" in df.columns else pd.DataFrame(columns=df.columns)
    results = []
    for _, row in df.iterrows():
        p = project_root / row["relative_path"]
        if p.exists():
            h_info = compute_file_hash_rehearsal(p, project_root, profile)
            res = row.to_dict()
            res.update(h_info)
            results.append(res)
    res_df = pd.DataFrame(results) if results else pd.DataFrame(columns=["relative_path", "hash_value", "hash_status"])
    return res_df, summarize_scripts_tests_hash_rehearsal(res_df)

def summarize_scripts_tests_hash_rehearsal(df: pd.DataFrame) -> dict:
    return {"total_scripts_tests_items": len(df) if df is not None else 0}
''')

write_file(base_dir / "local_archival" / "safety_boundary_hash_rehearsal.py", '''"""
Safety Boundary Hash Rehearsal.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.archive_candidate_inventory import discover_archive_candidate_items
from local_archival.hash_catalog import compute_file_hash_rehearsal

def build_safety_boundary_hash_rehearsal(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_archive_candidate_items(project_root, profile)
    df = df[df["source_layer"] == "safety"] if "source_layer" in df.columns else pd.DataFrame(columns=df.columns)
    results = []
    for _, row in df.iterrows():
        p = project_root / row["relative_path"]
        if p.exists():
            h_info = compute_file_hash_rehearsal(p, project_root, profile)
            res = row.to_dict()
            res.update(h_info)
            results.append(res)
    res_df = pd.DataFrame(results) if results else pd.DataFrame(columns=["relative_path", "hash_value", "hash_status"])
    return res_df, summarize_safety_boundary_hash_rehearsal(res_df)

def summarize_safety_boundary_hash_rehearsal(df: pd.DataFrame) -> dict:
    return {"total_safety_boundary_items": len(df) if df is not None else 0}
''')

write_file(base_dir / "local_archival" / "evidence_hash_rehearsal.py", '''"""
Evidence Hash Rehearsal.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.archive_candidate_inventory import discover_archive_candidate_items
from local_archival.hash_catalog import compute_file_hash_rehearsal

def build_acceptance_delivery_evidence_hash_rehearsal(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_archive_candidate_items(project_root, profile)
    df = df[df["source_layer"] == "evidence"] if "source_layer" in df.columns else pd.DataFrame(columns=df.columns)
    results = []
    for _, row in df.iterrows():
        p = project_root / row["relative_path"]
        if p.exists():
            h_info = compute_file_hash_rehearsal(p, project_root, profile)
            res = row.to_dict()
            res.update(h_info)
            results.append(res)
    res_df = pd.DataFrame(results) if results else pd.DataFrame(columns=["relative_path", "hash_value", "hash_status"])
    return res_df, summarize_evidence_hash_rehearsal(res_df)

def summarize_evidence_hash_rehearsal(df: pd.DataFrame) -> dict:
    return {"total_evidence_items": len(df) if df is not None else 0}
''')

write_file(base_dir / "local_archival" / "custody_chain.py", '''"""
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
''')

write_file(base_dir / "local_archival" / "custody_guide.py", '''"""
Custody Guide.
"""
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile

def build_custody_guide_sections(profile: LocalArchivalProfile) -> list[dict]:
    return [
        {"title": "Overview", "content": "This is a dry-run guide for long-term custody rehearsal."},
        {"title": "Disclaimer", "content": "Not a legal advice or official custody chain."},
        {"title": "Storage", "content": "All artifacts are stored locally in data/lake."}
    ]

def build_long_term_custody_rehearsal_guide(profile: LocalArchivalProfile) -> tuple[str, dict]:
    sections = build_custody_guide_sections(profile)
    text = "\\n\\n".join([f"# {s['title']}\\n{s['content']}" for s in sections])
    return text, summarize_custody_guide(text)

def save_long_term_custody_rehearsal_guide(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    return output_path

def summarize_custody_guide(text: str) -> dict:
    return {"guide_length": len(text) if text else 0}
''')

write_file(base_dir / "local_archival" / "retention_notes.py", '''"""
Retention Notes.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile

def build_default_retention_notes(profile: LocalArchivalProfile) -> pd.DataFrame:
    notes = [
        {"note_id": "r1", "policy": "local_dry_run_only", "description": "Retention is purely local.", "legal_claim": False}
    ]
    return pd.DataFrame(notes)

def build_retention_note_registry(profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_retention_notes(profile)
    return df, summarize_retention_notes(df)

def summarize_retention_notes(retention_df: pd.DataFrame) -> dict:
    return {"total_retention_notes": len(retention_df) if retention_df is not None else 0}
''')


print("generate_phase79_4.py created.")
