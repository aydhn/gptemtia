"""Phase 124 Feature Store Partition Policies."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

PARTITION_POLICIES = [
    {
        "partition_strategy": "by_source_phase",
        "partition_key": "source_phase",
        "description": "Özellikleri ve faktörleri kaynak faz numarasına göre bölümler (ör. phase_117, phase_118).",
        "sample_partitions": "phase_116,phase_117,phase_118,phase_119,phase_120,phase_121,phase_122,phase_123",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "partition_strategy": "by_entity_type",
        "partition_key": "entity_type",
        "description": "Varlık tipine göre bölümler (fx_pair, commodity_symbol, macro_indicator).",
        "sample_partitions": "entity_fx_pair,entity_commodity_symbol,entity_macro_indicator",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "partition_strategy": "by_feature_family",
        "partition_key": "feature_family",
        "description": "Özellik ailesine göre bölümler (moving_average, momentum, volatility).",
        "sample_partitions": "technical,trend,momentum,volatility,mean_reversion",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "partition_strategy": "by_date_bucket_placeholder",
        "partition_key": "year_month",
        "description": "Tarih kovası yer tutucusu (YYYY-MM) temelinde bölümler.",
        "sample_partitions": "2026_01,2026_02,2026_03",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "partition_strategy": "by_validation_status",
        "partition_key": "validation_status",
        "description": "Validasyon sonucuna göre bölümler (validation_pass, validation_manual_review).",
        "sample_partitions": "validation_pass,validation_pass_with_warnings,validation_manual_review_required",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "partition_strategy": "by_manual_review_required",
        "partition_key": "manual_review_required",
        "description": "Manuel inceleme gerektiren ve gerektirmeyen kayıtları bölümler.",
        "sample_partitions": "review_required_true,review_required_false",
        "non_signal": True,
        "source_preserved": True,
    },
]


def build_feature_store_partition_policy_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of partition policies."""
    records = list(PARTITION_POLICIES)
    df = pd.DataFrame(records)
    summary = {
        "total_partition_policies": len(records),
        "supported_strategies": [r["partition_strategy"] for r in records],
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_store_partition_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize partition policies."""
    return {
        "total_policies": len(df) if not df.empty else 0,
        "non_signal": True,
        "source_preserved": True,
    }
