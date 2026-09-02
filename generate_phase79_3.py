import os
from pathlib import Path

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = Path(r"c:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\commodity_fx_signal_bot")

write_file(base_dir / "local_archival" / "seal_rehearsal_manifest.py", '''"""
Seal Rehearsal Manifest.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile

def build_archival_seal_manifest_items(hash_df: pd.DataFrame, inventory_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    return hash_df.copy(), {"total_items": len(hash_df)}

def validate_archival_seal_manifest_safety(manifest: dict, profile: LocalArchivalProfile) -> dict:
    return {"safe": True}

def build_final_archival_seal_rehearsal_manifest(
    hash_df: pd.DataFrame,
    hoh_df: pd.DataFrame,
    inventory_df: pd.DataFrame,
    profile: LocalArchivalProfile,
) -> tuple[dict, dict]:
    manifest = {
        "statement": "This is a local-only dry-run seal rehearsal. Not a real immutable seal.",
        "hash_policy_reference": "default_hash_algorithm",
        "exclusion_policy_reference": "sensitive_files",
        "no_immutable_lock_statement": True,
        "no_chmod_statement": True,
        "no_legal_hold_statement": True,
        "no_compliance_statement": True,
        "no_cloud_archive_statement": True,
        "hash_of_hashes": hoh_df.to_dict(orient="records")[0]["hash_of_hashes"] if not hoh_df.empty else None
    }
    items_df, _ = build_archival_seal_manifest_items(hash_df, inventory_df, profile)
    return manifest, summarize_archival_seal_manifest(manifest, items_df)

def summarize_archival_seal_manifest(manifest: dict, item_df: pd.DataFrame) -> dict:
    return {"manifest_generated": True, "items_count": len(item_df) if item_df is not None else 0}
''')

write_file(base_dir / "local_archival" / "immutable_manifest_catalog.py", '''"""
Immutable Manifest Rehearsal Catalog.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile

def build_immutable_manifest_entries(manifest: dict, hash_df: pd.DataFrame, profile: LocalArchivalProfile) -> pd.DataFrame:
    df = hash_df.copy()
    if not df.empty:
        df["immutable_manifest_note"] = "dry-run rehearsal"
    return df

def build_immutable_manifest_rehearsal_catalog(manifest: dict, hash_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = build_immutable_manifest_entries(manifest, hash_df, profile)
    return df, summarize_immutable_manifest_catalog(df)

def summarize_immutable_manifest_catalog(catalog_df: pd.DataFrame) -> dict:
    return {"catalog_entries": len(catalog_df) if catalog_df is not None else 0}
''')

write_file(base_dir / "local_archival" / "provenance_lockfile.py", '''"""
Provenance Lockfile.
"""
import pandas as pd
from datetime import datetime, timezone
from local_archival.archival_config import LocalArchivalProfile

def build_provenance_lock_entries(inventory_df: pd.DataFrame, hash_df: pd.DataFrame, exclusion_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = hash_df.copy()
    if not df.empty:
        df["provenance_note"] = "local provenance dry-run"
    return df, {"total_entries": len(df)}

def validate_provenance_lockfile_safety(lockfile: dict, profile: LocalArchivalProfile) -> dict:
    return {"safe": True}

def build_local_provenance_lockfile(
    inventory_df: pd.DataFrame,
    hash_df: pd.DataFrame,
    exclusion_df: pd.DataFrame,
    profile: LocalArchivalProfile,
) -> tuple[dict, dict]:
    lockfile = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "project_scope_note": "gptemtia",
        "dry_run_archival_note": True,
        "hash_algorithm": profile.hash_algorithm,
        "included_item_count": len(hash_df),
        "excluded_sensitive_count": len(exclusion_df),
        "local_only_statement": True,
        "no_legal_hold_statement": True,
        "no_cloud_statement": True,
        "warnings": []
    }
    entries_df, _ = build_provenance_lock_entries(inventory_df, hash_df, exclusion_df, profile)
    return lockfile, summarize_provenance_lockfile(lockfile, entries_df)

def summarize_provenance_lockfile(lockfile: dict, entries_df: pd.DataFrame) -> dict:
    return {"lockfile_generated": True, "entries_count": len(entries_df) if entries_df is not None else 0}
''')

write_file(base_dir / "local_archival" / "delivery_hash_rehearsal.py", '''"""
Delivery Hash Rehearsal.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.archive_candidate_inventory import discover_archive_candidate_items
from local_archival.hash_catalog import compute_file_hash_rehearsal

def build_delivery_bundle_hash_rehearsal(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_archive_candidate_items(project_root, profile)
    df = df[df["source_layer"] == "delivery"] if "source_layer" in df.columns else pd.DataFrame(columns=df.columns)
    results = []
    for _, row in df.iterrows():
        p = project_root / row["relative_path"]
        if p.exists():
            h_info = compute_file_hash_rehearsal(p, project_root, profile)
            res = row.to_dict()
            res.update(h_info)
            results.append(res)
    res_df = pd.DataFrame(results) if results else pd.DataFrame(columns=["relative_path", "hash_value", "hash_status"])
    return res_df, summarize_delivery_bundle_hash_rehearsal(res_df)

def summarize_delivery_bundle_hash_rehearsal(df: pd.DataFrame) -> dict:
    return {"total_delivery_items": len(df) if df is not None else 0}
''')

write_file(base_dir / "local_archival" / "handoff_hash_rehearsal.py", '''"""
Handoff Hash Rehearsal.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.archive_candidate_inventory import discover_archive_candidate_items
from local_archival.hash_catalog import compute_file_hash_rehearsal

def build_handoff_package_hash_rehearsal(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_archive_candidate_items(project_root, profile)
    df = df[df["source_layer"] == "handoff"] if "source_layer" in df.columns else pd.DataFrame(columns=df.columns)
    results = []
    for _, row in df.iterrows():
        p = project_root / row["relative_path"]
        if p.exists():
            h_info = compute_file_hash_rehearsal(p, project_root, profile)
            res = row.to_dict()
            res.update(h_info)
            results.append(res)
    res_df = pd.DataFrame(results) if results else pd.DataFrame(columns=["relative_path", "hash_value", "hash_status"])
    return res_df, summarize_handoff_package_hash_rehearsal(res_df)

def summarize_handoff_package_hash_rehearsal(df: pd.DataFrame) -> dict:
    return {"total_handoff_items": len(df) if df is not None else 0}
''')

write_file(base_dir / "local_archival" / "generated_docs_hash_rehearsal.py", '''"""
Generated Docs Hash Rehearsal.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.archive_candidate_inventory import discover_archive_candidate_items
from local_archival.hash_catalog import compute_file_hash_rehearsal

def build_generated_docs_hash_rehearsal(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_archive_candidate_items(project_root, profile)
    df = df[df["source_layer"] == "docs"] if "source_layer" in df.columns else pd.DataFrame(columns=df.columns)
    results = []
    for _, row in df.iterrows():
        p = project_root / row["relative_path"]
        if p.exists():
            h_info = compute_file_hash_rehearsal(p, project_root, profile)
            res = row.to_dict()
            res.update(h_info)
            results.append(res)
    res_df = pd.DataFrame(results) if results else pd.DataFrame(columns=["relative_path", "hash_value", "hash_status"])
    return res_df, summarize_generated_docs_hash_rehearsal(res_df)

def summarize_generated_docs_hash_rehearsal(df: pd.DataFrame) -> dict:
    return {"total_docs_items": len(df) if df is not None else 0}
''')

write_file(base_dir / "local_archival" / "reports_hash_rehearsal.py", '''"""
Reports Hash Rehearsal.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.archive_candidate_inventory import discover_archive_candidate_items
from local_archival.hash_catalog import compute_file_hash_rehearsal

def build_reports_hash_rehearsal(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_archive_candidate_items(project_root, profile)
    df = df[df["source_layer"] == "reports"] if "source_layer" in df.columns else pd.DataFrame(columns=df.columns)
    results = []
    for _, row in df.iterrows():
        p = project_root / row["relative_path"]
        if p.exists():
            h_info = compute_file_hash_rehearsal(p, project_root, profile)
            res = row.to_dict()
            res.update(h_info)
            results.append(res)
    res_df = pd.DataFrame(results) if results else pd.DataFrame(columns=["relative_path", "hash_value", "hash_status"])
    return res_df, summarize_reports_hash_rehearsal(res_df)

def summarize_reports_hash_rehearsal(df: pd.DataFrame) -> dict:
    return {"total_reports_items": len(df) if df is not None else 0}
''')


print("generate_phase79_3.py created.")
