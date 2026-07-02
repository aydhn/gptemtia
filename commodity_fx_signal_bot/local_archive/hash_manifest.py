from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Optional
import hashlib
from .archive_config import LocalArchiveProfile

def calculate_archive_item_hash(path: Path, profile: LocalArchiveProfile) -> Tuple[Optional[str], Dict]:
    try: size = path.stat().st_size
    except OSError: return None, {"status": "error", "message": "Could not read size"}
    mb = size / (1024 * 1024)
    if mb > profile.max_file_mb_for_hash:
        return None, {"status": "skipped", "message": f"File too large ({mb:.2f} MB)"}
    hash_obj = hashlib.sha256()
    try:
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_obj.update(chunk)
        return hash_obj.hexdigest(), {"status": "success"}
    except Exception as e:
        return None, {"status": "error", "message": str(e)}

def build_archive_hash_manifest(item_df: pd.DataFrame, project_root: Path, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    hashes = []
    if not item_df.empty and 'item_status' in item_df.columns:
        cand_df = item_df[item_df['item_status'] == 'archive_candidate'].copy()
        for _, row in cand_df.iterrows():
            path = project_root / row['relative_path']
            if not path.exists():
                h, status = None, "integrity_path_missing"
            else:
                h, res = calculate_archive_item_hash(path, profile)
                if res['status'] == 'success': status = "integrity_hash_available"
                elif res['status'] == 'skipped': status = "integrity_hash_skipped_large_file"
                else: status = "integrity_missing_hash"
            hashes.append({
                "item_id": row['item_id'],
                "relative_path": row['relative_path'],
                "sha256": h,
                "integrity_status": status
            })
    df = pd.DataFrame(hashes)
    return df, summarize_archive_hash_manifest(df)

def summarize_archive_hash_manifest(hash_df: pd.DataFrame) -> Dict:
    if hash_df.empty: return {"total_hashes": 0}
    avail = int((hash_df['integrity_status'] == 'integrity_hash_available').sum()) if 'integrity_status' in hash_df.columns else 0
    skip = int((hash_df['integrity_status'] == 'integrity_hash_skipped_large_file').sum()) if 'integrity_status' in hash_df.columns else 0
    return {"total_items_checked": len(hash_df), "hashes_available": avail, "hashes_skipped": skip, "notice": "Hashes are for offline manual verification only."}
