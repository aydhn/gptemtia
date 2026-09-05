"""Phase 124 Feature Store Manual Review Blockers Registry.

Tracks validation failures, lookahead ambiguity, forbidden column alerts,
and missing lineage without dropping or mutating features.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

CORE_BLOCKERS = [
    {
        "blocker_id": "BLK_001",
        "target_item": "raw_feed_delta_check",
        "blocker_type": "no_lookahead_unresolved",
        "reason": "İleriye dönük zaman damgası şüphesi manuel doğrulama bekliyor.",
        "blocking_status": True,
        "non_signal": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    },
    {
        "blocker_id": "BLK_002",
        "target_item": "vendor_feed_column_check",
        "blocker_type": "forbidden_column_risk",
        "reason": "Harici dosyadaki kolon adı kontrolü; otomatik silme yapılmadı.",
        "blocking_status": True,
        "non_signal": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    },
    {
        "blocker_id": "BLK_003",
        "target_item": "news_headline_feed_review",
        "blocker_type": "metadata_only_boundary_unresolved",
        "reason": "Haber metaveri sınırı teyidi; telifli tam metin kopyalama yasak.",
        "blocking_status": True,
        "non_signal": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    },
    {
        "blocker_id": "BLK_004",
        "target_item": "factor_dependency_tree_check",
        "blocker_type": "factor_dependency_unresolved",
        "reason": "Faktör girdi bağımlılık grafiğinde eksik girdi incelemesi.",
        "blocking_status": True,
        "non_signal": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    },
]


def build_feature_store_manual_review_blocker_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of manual review blockers."""
    records = list(CORE_BLOCKERS)
    df = pd.DataFrame(records)
    summary = {
        "total_blockers": len(records),
        "active_blocking_count": len([r for r in records if r["blocking_status"]]),
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
        "non_signal": True,
    }
    return df, summary


def summarize_feature_store_manual_review_blockers(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review blockers."""
    if df.empty:
        return {"total_blockers": 0, "active_blocking_count": 0, "destructive_action_allowed": False}
    return {
        "total_blockers": len(df),
        "active_blocking_count": int((df.get("blocking_status", pd.Series()) == True).sum()),
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
    }
