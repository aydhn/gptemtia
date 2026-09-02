"""
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
