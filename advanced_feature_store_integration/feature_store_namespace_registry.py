"""Phase 124 Feature Store Namespace Registry and Validation."""

import re
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

FORBIDDEN_NAMESPACE_TERMS: List[str] = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "future_return",
    "forward_return",
    "next_return",
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "embedding",
    "vector",
]

ALLOWED_ENTITY_PREFIXES: List[str] = [
    "fx",
    "commodity",
    "macro",
    "calendar",
    "news",
    "cross_asset",
    "factor",
    "quality_drift",
    "validation",
]


def build_store_feature_key(entity: str, namespace: str, feature_name: str) -> str:
    """Build canonical store feature key with lowercase snake_case."""
    e = entity.strip().lower()
    ns = namespace.strip().lower().replace(".", "__").replace("/", "__")
    fn = feature_name.strip().lower()
    return f"{e}__{ns}__{fn}"


def validate_store_feature_key(key: str) -> Dict[str, Any]:
    """Validate feature store key against namespace policy."""
    lowered = key.lower()
    issues = []

    # Check snake_case pattern
    if not re.match(r"^[a-z0-9_]+$", key):
        issues.append("Key must be strictly lowercase alphanumeric and underscores.")

    # Check prefix
    parts = lowered.split("__")
    if len(parts) < 2 or parts[0] not in ALLOWED_ENTITY_PREFIXES:
        issues.append(f"Key must start with one of allowed prefixes: {ALLOWED_ENTITY_PREFIXES}")

    # Check forbidden words
    tokens = set([t for t in re.split(r"_+", lowered) if t])
    for term in FORBIDDEN_NAMESPACE_TERMS:
        if "_" in term:
            if term in lowered:
                issues.append(f"Forbidden term detected in namespace: '{term}'")
        else:
            if term in tokens:
                issues.append(f"Forbidden term detected in namespace: '{term}'")

    return {
        "key": key,
        "is_valid": len(issues) == 0,
        "issues": issues,
        "non_signal": len([i for i in issues if "Forbidden term" in i]) == 0,
    }


def build_feature_store_namespace_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of namespace policies."""
    prof = profile or get_default_feature_store_integration_profile()
    records = []
    for prefix in ALLOWED_ENTITY_PREFIXES:
        records.append({
            "prefix": prefix,
            "policy_rule": f"Canonical namespace must start with '{prefix}__'",
            "forbidden_terms_enforced": len(FORBIDDEN_NAMESPACE_TERMS),
            "source_phase": prof.current_phase,
            "non_signal": True,
            "source_preserved": True,
            "status": "enforced",
        })

    df = pd.DataFrame(records)
    summary = {
        "total_namespaces": len(records),
        "allowed_prefixes": ALLOWED_ENTITY_PREFIXES,
        "total_forbidden_terms": len(FORBIDDEN_NAMESPACE_TERMS),
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_store_namespace_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize namespace registry."""
    return {
        "total_prefixes": len(df) if not df.empty else 0,
        "forbidden_terms_count": len(FORBIDDEN_NAMESPACE_TERMS),
        "non_signal": True,
    }
