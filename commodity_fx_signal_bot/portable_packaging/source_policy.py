import pandas as pd
from typing import Dict, Any

from portable_packaging.packaging_config import PortablePackagingProfile

def build_source_inclusion_policy(profile: PortablePackagingProfile) -> pd.DataFrame:
    rules = []
    if profile.include_source:
        rules.append({"pattern": "*.py", "reason": "include_source"})
    if profile.include_tests:
        rules.append({"pattern": "tests/*", "reason": "include_tests"})
    if profile.include_docs:
        rules.append({"pattern": "docs/*", "reason": "include_docs"})
        rules.append({"pattern": "README.md", "reason": "include_docs"})
    if profile.include_configs:
        rules.append({"pattern": "pyproject.toml", "reason": "include_configs"})
        rules.append({"pattern": "requirements*.txt", "reason": "include_configs"})
        rules.append({"pattern": ".env.example", "reason": "include_configs"})

    return pd.DataFrame(rules)

def build_source_exclusion_policy(profile: PortablePackagingProfile) -> pd.DataFrame:
    rules = [
        {"pattern": ".env", "reason": "secret_exclusion"},
        {"pattern": "*secret*", "reason": "secret_exclusion"},
        {"pattern": "*token*", "reason": "secret_exclusion"},
        {"pattern": "*private_key*", "reason": "secret_exclusion"},
        {"pattern": "__pycache__", "reason": "runtime_exclusion"},
        {"pattern": ".pytest_cache", "reason": "runtime_exclusion"},
        {"pattern": ".git", "reason": "vcs_exclusion"},
    ]
    if profile.include_data_manifest_only:
        rules.append({"pattern": "data/lake/*", "reason": "manifest_only"})
    if profile.include_reports_manifest_only:
        rules.append({"pattern": "reports/output/*", "reason": "manifest_only"})

    return pd.DataFrame(rules)

def validate_source_policy(inclusion_df: pd.DataFrame, exclusion_df: pd.DataFrame) -> Dict[str, Any]:
    return {"valid": not inclusion_df.empty and not exclusion_df.empty}

def summarize_source_policy(inclusion_df: pd.DataFrame, exclusion_df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "included_rules": len(inclusion_df),
        "excluded_rules": len(exclusion_df)
    }
