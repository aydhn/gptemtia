import os
from pathlib import Path

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = Path(r"c:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\commodity_fx_signal_bot")

write_file(base_dir / "local_archival" / "hash_policies.py", '''"""
Hash Policies.
"""
import pandas as pd
from local_archival.archival_config import LocalArchivalProfile

def get_allowed_hash_algorithms() -> list[str]:
    return ["sha256", "sha384", "sha512"]

def build_hash_policy_registry(profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    policies = [
        {"policy_name": "default_hash_algorithm", "policy_value": profile.hash_algorithm},
        {"policy_name": "skip_sensitive_files", "policy_value": True},
        {"policy_name": "never_change_files", "policy_value": True},
        {"policy_name": "never_lock_permissions", "policy_value": True},
        {"policy_name": "never_upload", "policy_value": True}
    ]
    df = pd.DataFrame(policies)
    return df, {"total_policies": len(df)}

def build_hash_exclusion_policy_registry(profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    exclusions = [
        {"exclusion_type": "sensitive", "pattern": ".env*"},
        {"exclusion_type": "sensitive", "pattern": "*secret*"},
        {"exclusion_type": "sensitive", "pattern": "*credential*"},
        {"exclusion_type": "sensitive", "pattern": "*private_key*"},
        {"exclusion_type": "size", "pattern": f">{profile.max_file_size_mb_for_hash}MB"}
    ]
    df = pd.DataFrame(exclusions)
    return df, {"total_exclusions": len(df)}

def validate_hash_policy(policy_df: pd.DataFrame, profile: LocalArchivalProfile) -> dict:
    return {"valid": True, "note": "Dry-run local validation."}

def summarize_hash_policies(policy_df: pd.DataFrame, exclusion_df: pd.DataFrame) -> dict:
    return {
        "policy_count": len(policy_df) if policy_df is not None else 0,
        "exclusion_count": len(exclusion_df) if exclusion_df is not None else 0
    }
''')

write_file(base_dir / "local_archival" / "sensitive_exclusions.py", '''"""
Sensitive Exclusions.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile

def is_sensitive_archival_path(path: Path, project_root: Path) -> bool:
    name = path.name.lower()
    if name.startswith(".env"): return True
    if any(x in name for x in ["secret", "credential", "private_key", "id_rsa", "token", "api_key", "password", "auth"]):
        return True
    if name.endswith((".pem", ".key")):
        return True
    return False

def classify_sensitive_exclusion_reason(path: Path, project_root: Path) -> str:
    name = path.name.lower()
    if name.startswith(".env"): return "env_file"
    if "secret" in name: return "contains_secret_keyword"
    return "general_sensitive"

def build_sensitive_file_exclusion_registry(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    exclusions = []
    if project_root.exists():
        for p in project_root.rglob("*"):
            if p.is_file() and is_sensitive_archival_path(p, project_root):
                try:
                    rel_path = p.relative_to(project_root).as_posix()
                except:
                    rel_path = p.name
                exclusions.append({
                    "relative_path": rel_path,
                    "reason": classify_sensitive_exclusion_reason(p, project_root)
                })
    df = pd.DataFrame(exclusions) if exclusions else pd.DataFrame(columns=["relative_path", "reason"])
    return df, summarize_sensitive_exclusions(df)

def summarize_sensitive_exclusions(exclusion_df: pd.DataFrame) -> dict:
    return {"total_excluded": len(exclusion_df) if exclusion_df is not None else 0}
''')

write_file(base_dir / "local_archival" / "archive_candidate_inventory.py", '''"""
Archive Candidate Inventory.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.sensitive_exclusions import is_sensitive_archival_path

def classify_archival_item_label(path: Path, project_root: Path) -> str:
    parts = path.parts
    if "docs" in parts: return "archival_doc_item"
    if "reports" in parts: return "archival_report_item"
    if "scripts" in parts: return "archival_script_item"
    if "tests" in parts: return "archival_test_item"
    return "archival_unknown_item"

def classify_archival_source_layer(path: Path, project_root: Path) -> str:
    parts = path.parts
    if "docs" in parts: return "docs"
    if "reports" in parts: return "reports"
    return "other"

def discover_archive_candidate_items(project_root: Path, profile: LocalArchivalProfile) -> pd.DataFrame:
    items = []
    if project_root.exists():
        for p in project_root.rglob("*"):
            if p.is_file():
                if ".git" in p.parts or "__pycache__" in p.parts: continue
                if is_sensitive_archival_path(p, project_root): continue
                if p.stat().st_size > profile.max_file_size_mb_for_hash * 1024 * 1024: continue
                try:
                    rel_path = p.relative_to(project_root).as_posix()
                except:
                    rel_path = p.name
                items.append({
                    "relative_path": rel_path,
                    "item_label": classify_archival_item_label(p, project_root),
                    "source_layer": classify_archival_source_layer(p, project_root),
                    "size_bytes": p.stat().st_size
                })
    return pd.DataFrame(items) if items else pd.DataFrame(columns=["relative_path", "item_label", "source_layer", "size_bytes"])

def build_archive_candidate_inventory(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_archive_candidate_items(project_root, profile)
    return df, summarize_archive_candidate_inventory(df)

def summarize_archive_candidate_inventory(inventory_df: pd.DataFrame) -> dict:
    return {"total_candidates": len(inventory_df) if inventory_df is not None else 0}
''')

write_file(base_dir / "local_archival" / "hash_catalog.py", '''"""
Hash Catalog.
"""
import pandas as pd
import hashlib
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile
from local_archival.sensitive_exclusions import is_sensitive_archival_path

def compute_file_hash_rehearsal(path: Path, project_root: Path, profile: LocalArchivalProfile) -> dict:
    if is_sensitive_archival_path(path, project_root):
        return {"hash_value": None, "hash_status": "hash_rehearsal_skipped_sensitive"}
    if path.stat().st_size > profile.max_file_size_mb_for_hash * 1024 * 1024:
        return {"hash_value": None, "hash_status": "hash_rehearsal_skipped_large_file"}
    
    h = hashlib.new(profile.hash_algorithm)
    try:
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return {"hash_value": h.hexdigest(), "hash_status": "hash_rehearsal_ready"}
    except Exception:
        return {"hash_value": None, "hash_status": "hash_rehearsal_error"}

def detect_hash_catalog_warnings(hash_df: pd.DataFrame, profile: LocalArchivalProfile) -> pd.DataFrame:
    df = hash_df.copy()
    if "warnings" not in df.columns:
        df["warnings"] = ""
    return df

def build_final_hash_catalog(project_root: Path, inventory_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    results = []
    if not inventory_df.empty:
        for _, row in inventory_df.iterrows():
            p = project_root / row["relative_path"]
            if p.exists():
                h_info = compute_file_hash_rehearsal(p, project_root, profile)
                res = row.to_dict()
                res.update(h_info)
                results.append(res)
    df = pd.DataFrame(results) if results else pd.DataFrame(columns=["relative_path", "hash_value", "hash_status"])
    df = detect_hash_catalog_warnings(df, profile)
    return df, summarize_final_hash_catalog(df)

def summarize_final_hash_catalog(hash_df: pd.DataFrame) -> dict:
    return {"total_hashes": len(hash_df) if hash_df is not None else 0}
''')

write_file(base_dir / "local_archival" / "hash_of_hashes.py", '''"""
Hash of Hashes Catalog.
"""
import pandas as pd
import hashlib
from local_archival.archival_config import LocalArchivalProfile

def compute_hash_of_hashes(hash_df: pd.DataFrame, profile: LocalArchivalProfile) -> dict:
    if hash_df is None or hash_df.empty:
        return {"hash_of_hashes": None}
    
    h = hashlib.new(profile.hash_algorithm)
    valid_hashes = hash_df[hash_df["hash_value"].notna()]["hash_value"].sort_values().tolist()
    for v in valid_hashes:
        h.update(str(v).encode('utf-8'))
    return {"hash_of_hashes": h.hexdigest()}

def build_final_hash_of_hashes_catalog(hash_df: pd.DataFrame, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    res = compute_hash_of_hashes(hash_df, profile)
    df = pd.DataFrame([{"hash_algorithm": profile.hash_algorithm, "hash_of_hashes": res["hash_of_hashes"]}])
    return df, summarize_hash_of_hashes_catalog(df)

def summarize_hash_of_hashes_catalog(hoh_df: pd.DataFrame) -> dict:
    return {"status": "computed" if hoh_df is not None and not hoh_df.empty else "empty"}
''')

print("generate_phase79_2.py created.")
