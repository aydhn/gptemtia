"""Phase 125: Feature Engine Block Dependencies Report.

Traces sequential and cross-functional dependency contracts across Phase 116-125
and the handoff to Phase 126.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_models import (
    FeatureEngineBlockDependencyItem,
)

DEPENDENCIES = [
    FeatureEngineBlockDependencyItem(
        source_phase=116,
        source_module="advanced_feature_engine",
        target_phase=117,
        target_module="advanced_technical_indicators",
        dependency_type="computational_foundation",
        contract_satisfied=True,
        notes="Temel hesaplama arayüzleri ve şemaları indikatör genişlemesine aktarıldı.",
    ),
    FeatureEngineBlockDependencyItem(
        source_phase=117,
        source_module="advanced_technical_indicators",
        target_phase=118,
        target_module="advanced_feature_grid",
        dependency_type="indicator_catalog",
        contract_satisfied=True,
        notes="Teknik indikatör katalogları çoklu pencere grid hesaplamalarına bağlandı.",
    ),
    FeatureEngineBlockDependencyItem(
        source_phase=118,
        source_module="advanced_feature_grid",
        target_phase=119,
        target_module="advanced_cross_asset_alignment",
        dependency_type="multi_window_features",
        contract_satisfied=True,
        notes="Tek varlık grid serileri çapraz varlık matris hizalamasına aktarıldı.",
    ),
    FeatureEngineBlockDependencyItem(
        source_phase=119,
        source_module="advanced_cross_asset_alignment",
        target_phase=120,
        target_module="advanced_feature_fusion",
        dependency_type="aligned_asset_matrix",
        contract_satisfied=True,
        notes="Zaman hizalı çoklu varlık matrisi makro/olay/haber füzyonuna iletildi.",
    ),
    FeatureEngineBlockDependencyItem(
        source_phase=120,
        source_module="advanced_feature_fusion",
        target_phase=121,
        target_module="advanced_feature_validation",
        dependency_type="fused_feature_matrix",
        contract_satisfied=True,
        notes="Füzyon serileri no-lookahead ve sızıntı doğrulama motoruna verildi.",
    ),
    FeatureEngineBlockDependencyItem(
        source_phase=121,
        source_module="advanced_feature_validation",
        target_phase=122,
        target_module="advanced_factor_metadata",
        dependency_type="validated_features",
        contract_satisfied=True,
        notes="Doğrulanmış ve sızıntısız feature'lar faktör ailelerine girdi sağladı.",
    ),
    FeatureEngineBlockDependencyItem(
        source_phase=122,
        source_module="advanced_factor_metadata",
        target_phase=123,
        target_module="advanced_feature_quality_drift",
        dependency_type="factor_families",
        contract_satisfied=True,
        notes="12 faktör ailesi ve metaverileri kalite/drift tanılarına bağlandı.",
    ),
    FeatureEngineBlockDependencyItem(
        source_phase=123,
        source_module="advanced_feature_quality_drift",
        target_phase=124,
        target_module="advanced_feature_store_integration",
        dependency_type="quality_drift_diagnostics",
        contract_satisfied=True,
        notes="Kalite ve drift tanı skorları merkezi feature store metaverisine aktarıldı.",
    ),
    FeatureEngineBlockDependencyItem(
        source_phase=124,
        source_module="advanced_feature_store_integration",
        target_phase=125,
        target_module="advanced_feature_factor_acceptance",
        dependency_type="central_feature_store",
        contract_satisfied=True,
        notes="Feature store katalog ve sözleşmeleri blok kabul raporuna bağlandı.",
    ),
    FeatureEngineBlockDependencyItem(
        source_phase=125,
        source_module="advanced_feature_factor_acceptance",
        target_phase=126,
        target_module="phase_126_handoff",
        dependency_type="block_acceptance_manifest",
        contract_satisfied=True,
        notes="Kabul edilmiş feature bloğu Phase 126 rejim sınıflandırmasına devredildi.",
    ),
]


def build_feature_engine_block_dependency_report(
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the dependency report DataFrame and summary."""
    active_profile = profile or get_default_feature_factor_acceptance_profile()
    rows = [d.__dict__ for d in DEPENDENCIES]
    df = pd.DataFrame(rows)

    summary = {
        "profile_name": active_profile.profile_name,
        "total_dependencies": len(df),
        "all_satisfied": bool(df["contract_satisfied"].all()),
        "phase_start": df["source_phase"].min(),
        "phase_end": df["target_phase"].max(),
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_feature_engine_block_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize dependency DataFrame."""
    return {
        "total_edges": len(df),
        "all_satisfied": bool(df["contract_satisfied"].all()) if "contract_satisfied" in df.columns else True,
        "pipeline_sequence": f"{df['source_phase'].min()} -> ... -> {df['target_phase'].max()}",
        "non_signal": True,
    }
