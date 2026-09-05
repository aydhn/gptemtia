"""Phase 124 Feature Store Lineage References."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

LINEAGE_REFS = [
    {
        "lineage_ref_id": "LIN_REF_114_PROVENANCE",
        "source_phase": 114,
        "module_origin": "advanced_data_lineage",
        "target_entity": "fx_and_commodity_raw",
        "lineage_hash": "sha256:114_provenance_hash",
        "description": "Phase 114 veri kökeni ve kaynak izlenebilirlik referansı.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "lineage_ref_id": "LIN_REF_121_VALIDATION",
        "source_phase": 121,
        "module_origin": "advanced_feature_validation",
        "target_entity": "feature_matrix",
        "lineage_hash": "sha256:121_validation_hash",
        "description": "Phase 121 no-lookahead ve sızıntı denetim onay referansı.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "lineage_ref_id": "LIN_REF_122_FACTOR_METADATA",
        "source_phase": 122,
        "module_origin": "advanced_factor_metadata",
        "target_entity": "factor_families",
        "lineage_hash": "sha256:122_factor_metadata_hash",
        "description": "Phase 122 faktör ailesi taksonomisi ve bağımlılık referansı.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "lineage_ref_id": "LIN_REF_123_QUALITY_DRIFT",
        "source_phase": 123,
        "module_origin": "advanced_feature_quality_drift",
        "target_entity": "feature_quality_diagnostics",
        "lineage_hash": "sha256:123_quality_drift_hash",
        "description": "Phase 123 özellik kalite ve drift skorlama referansı.",
        "non_signal": True,
        "source_preserved": True,
    },
]


def build_feature_store_lineage_reference_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of lineage references."""
    records = list(LINEAGE_REFS)
    df = pd.DataFrame(records)
    summary = {
        "total_lineage_references": len(records),
        "source_phases": sorted(list(set(r["source_phase"] for r in records))),
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_store_lineage_references(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize lineage reference registry."""
    return {
        "total_references": len(df) if not df.empty else 0,
        "non_signal": True,
        "source_preserved": True,
    }
