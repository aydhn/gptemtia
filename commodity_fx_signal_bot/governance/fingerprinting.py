import hashlib
import json
from pathlib import Path

import pandas as pd

from governance.governance_config import GovernanceProfile


def calculate_file_fingerprint(path: Path, max_mb: int = 50) -> tuple[str | None, dict]:
    warnings = []
    if not path.exists() or not path.is_file():
        warnings.append(f"File not found or not a file: {path}")
        return None, {"warnings": warnings}

    size_mb = path.stat().st_size / (1024 * 1024)
    if size_mb > max_mb:
        warnings.append(f"File size {size_mb:.2f}MB exceeds limit of {max_mb}MB. Skipping content fingerprint.")
        return None, {"warnings": warnings, "skipped_reason": "size_limit"}

    try:
        hash_md5 = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest(), {"warnings": warnings}
    except Exception as e:
        warnings.append(f"Error calculating file fingerprint: {e}")
        return None, {"warnings": warnings, "error": str(e)}

def calculate_dataframe_schema_fingerprint(df: pd.DataFrame) -> str:
    dtypes = df.dtypes.astype(str).to_dict()
    schema_str = json.dumps(dtypes, sort_keys=True)
    return hashlib.sha256(schema_str.encode('utf-8')).hexdigest()

def calculate_dataframe_content_sample_fingerprint(df: pd.DataFrame, sample_rows: int = 100) -> str:
    sample_df = df.head(sample_rows)
    # Mask secrets/sensitive data if any (just in case, though dataframe shouldn't have it directly)
    # Convert to string and hash
    content_str = sample_df.to_string()
    return hashlib.sha256(content_str.encode('utf-8')).hexdigest()

def calculate_json_fingerprint(path: Path, max_mb: int = 50) -> tuple[str | None, dict]:
    return calculate_file_fingerprint(path, max_mb)

def calculate_csv_fingerprint(path: Path, max_mb: int = 50) -> tuple[dict, dict]:
    warnings = []
    res = {
        "row_count": None,
        "column_count": None,
        "schema_fingerprint": None,
        "content_fingerprint": None
    }

    if not path.exists():
        warnings.append("File does not exist.")
        return res, {"warnings": warnings}

    size_mb = path.stat().st_size / (1024 * 1024)
    if size_mb > max_mb:
        warnings.append(f"File size {size_mb:.2f}MB exceeds max_mb {max_mb}. Skipping detailed CSV fingerprinting.")
        return res, {"warnings": warnings, "skipped_reason": "size_limit"}

    try:
        df = pd.read_csv(path, nrows=100)
        res["column_count"] = len(df.columns)
        res["schema_fingerprint"] = calculate_dataframe_schema_fingerprint(df)
        res["content_fingerprint"] = calculate_dataframe_content_sample_fingerprint(df)

        # for row count, we might read full if small enough
        if size_mb < 10:
            df_full = pd.read_csv(path, usecols=[df.columns[0]])
            res["row_count"] = len(df_full)
        else:
            warnings.append(f"File size {size_mb:.2f}MB is too large for full row count. Approximating or skipping.")
    except Exception as e:
        warnings.append(f"Error reading CSV: {e}")

    return res, {"warnings": warnings}

def calculate_parquet_fingerprint(path: Path, max_mb: int = 50) -> tuple[dict, dict]:
    warnings = []
    res = {
        "row_count": None,
        "column_count": None,
        "schema_fingerprint": None,
        "content_fingerprint": None
    }

    if not path.exists():
        warnings.append("File does not exist.")
        return res, {"warnings": warnings}

    size_mb = path.stat().st_size / (1024 * 1024)

    try:
        if size_mb > max_mb:
            warnings.append(f"File size {size_mb:.2f}MB exceeds max_mb {max_mb}. Skipping detailed Parquet fingerprinting.")
            return res, {"warnings": warnings, "skipped_reason": "size_limit"}

        df = pd.read_parquet(path)
        res["row_count"] = len(df)
        res["column_count"] = len(df.columns)
        res["schema_fingerprint"] = calculate_dataframe_schema_fingerprint(df)
        res["content_fingerprint"] = calculate_dataframe_content_sample_fingerprint(df)
    except Exception as e:
        warnings.append(f"Error reading Parquet: {e}")

    return res, {"warnings": warnings}

def build_artifact_fingerprint(path: Path, profile: GovernanceProfile) -> tuple[dict, dict]:
    warnings = []
    metadata = {}

    if not path.exists():
        warnings.append("File does not exist.")
        return {}, {"warnings": warnings}

    ext = path.suffix.lower()

    # Try file hash
    content_hash = None
    if profile.capture_file_hashes:
        content_hash, meta = calculate_file_fingerprint(path, profile.max_file_hash_mb)
        metadata.update(meta)
        if meta.get("warnings"):
            warnings.extend(meta["warnings"])

    res = {
        "content_fingerprint": content_hash,
        "schema_fingerprint": None,
        "row_count": None,
        "column_count": None
    }

    # Try specialized parsing if enabled
    if profile.capture_schema_fingerprints:
        if ext == '.csv':
            csv_res, csv_meta = calculate_csv_fingerprint(path, profile.max_file_hash_mb)
            res.update({k: v for k, v in csv_res.items() if v is not None})
            if csv_meta.get("warnings"):
                warnings.extend(csv_meta["warnings"])
        elif ext == '.parquet':
            pq_res, pq_meta = calculate_parquet_fingerprint(path, profile.max_file_hash_mb)
            res.update({k: v for k, v in pq_res.items() if v is not None})
            if pq_meta.get("warnings"):
                warnings.extend(pq_meta["warnings"])

    if not profile.capture_row_counts:
        res["row_count"] = None

    metadata["warnings"] = list(set(warnings))
    return res, metadata
