"""Phase 124 Feature Store Source Preservation Policies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

PROHIBITED_ACTIONS: List[str] = [
    "overwrite_source",
    "delete_source",
    "move_source",
    "destructive_clean",
    "auto_impute_overwrite",
    "auto_drop_feature",
    "mutate_input_dataframe",
]

PRESERVATION_POLICIES = [
    {
        "policy_id": "SPP_001",
        "action": "overwrite_source",
        "rule": "Kaynağın üzerine yazma kesinlikle yasaktır; her zaman yeni snapshot veya sürüm eklenir.",
        "allowed": False,
    },
    {
        "policy_id": "SPP_002",
        "action": "delete_source",
        "rule": "Kaynak veriyi veya kolonları silmek kesinlikle yasaktır; sorunlu kayıtlar inceleme kuyruğuna alınır.",
        "allowed": False,
    },
    {
        "policy_id": "SPP_003",
        "action": "destructive_clean",
        "rule": "Yıkıcı temizlik yapılamaz; veri orijinal formatında korunmalıdır.",
        "allowed": False,
    },
    {
        "policy_id": "SPP_004",
        "action": "auto_impute_overwrite",
        "rule": "Otomatik doldurma (imputation) ile kaynak değerlerin mutasyonu yasaktır.",
        "allowed": False,
    },
    {
        "policy_id": "SPP_005",
        "action": "auto_drop_feature",
        "rule": "Düşük kaliteli veya boş feature'ların otomatik düşürülmesi yasaktır.",
        "allowed": False,
    },
]


def validate_source_preservation_policy(action: str) -> Dict[str, Any]:
    """Validate action against source preservation principles."""
    act = action.lower().strip()
    is_prohibited = act in PROHIBITED_ACTIONS

    return {
        "action": action,
        "is_prohibited": is_prohibited,
        "is_safe": not is_prohibited,
        "destructive_action_allowed": False,
        "source_preserved": not is_prohibited,
    }


def build_feature_store_source_preservation_policy_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of source preservation policies."""
    records = list(PRESERVATION_POLICIES)
    df = pd.DataFrame(records)
    summary = {
        "total_preservation_policies": len(records),
        "prohibited_actions_count": len(PROHIBITED_ACTIONS),
        "source_preserved": True,
        "destructive_action_allowed": False,
    }
    return df, summary


def summarize_feature_store_source_preservation_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize source preservation policies."""
    return {
        "total_policies": len(df) if not df.empty else 0,
        "source_preserved": True,
        "destructive_action_allowed": False,
    }
