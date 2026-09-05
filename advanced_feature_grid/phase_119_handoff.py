from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


HANDOFF_ITEMS = [
    {
        "topic": "cross_asset_naming_compatibility",
        "description": "FX ve emtia varlıkları arasında tutarlı ve normalize kolon isimlendirme formatı.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "feature_grid_naming_registry",
    },
    {
        "topic": "fx_commodity_multi_window_alignment",
        "description": "Farklı işlem saatlerine ve takvimlere sahip FX ve Emtia pencerelerinin senkronizasyonu.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "window_grid_contracts",
    },
    {
        "topic": "macro_calendar_news_placeholder_alignment",
        "description": "Fiyat serilerine makro/takvim/haber placeholder pencerelerinin hizalanma sözleşmesi.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "placeholder_grid_registries",
    },
    {
        "topic": "timestamp_alignment_dependency",
        "description": "UTC zaman damgalı ortak zaman ızgarası üzerinde feature alignment gereksinimi.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "phase_113_data_normalization",
    },
    {
        "topic": "normalized_symbol_dependency",
        "description": "Varlık kimliklerinin (canonical symbols) feature grid ön ekleriyle eşleştirilmesi.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "phase_113_data_normalization",
    },
    {
        "topic": "feature_grid_metadata_dependency",
        "description": "Her bir hizalanmış kolonun pencere ve hesaplama metadatasının taşınması.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "feature_grid_metadata_registry",
    },
    {
        "topic": "warmup_nan_alignment_policy",
        "description": "Farklı uzunluktaki geçmiş veriler için warmup NaN hizalama ve maskeleme politikası.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "feature_grid_warmup_nan_policy",
    },
    {
        "topic": "duplicate_feature_resolution_requirement",
        "description": "Cross-asset birleşiminde oluşabilecek mükerrer kolonların deterministik çözümü.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "feature_grid_duplicate_detection",
    },
    {
        "topic": "cross_domain_dependency_mapping",
        "description": "Farklı veri alanları (FX, Emtia, Makro) arasındaki feature bağımlılık haritası.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "feature_grid_dependency_registry",
    },
    {
        "topic": "phase_121_no_lookahead_guard_dependency",
        "description": "Hizalanmış çoklu varlık matrisinde lookahead sızıntısını engelleyen sıkı guard.",
        "target_phase": 121,
        "status": "FORWARD_CONTRACT",
        "dependency": "feature_grid_no_lookahead_guard",
    },
    {
        "topic": "phase_124_feature_store_integration_dependency",
        "description": "Hizalanmış feature tablosunun offline FeatureStore katmanına şemalı kaydı.",
        "target_phase": 124,
        "status": "FORWARD_CONTRACT",
        "dependency": "feature_grid_output_schema",
    },
]


def build_phase_119_cross_asset_feature_alignment_handoff_report(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    df = pd.DataFrame(HANDOFF_ITEMS)
    summary = summarize_phase_119_handoff(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_phase_119_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_handoff_items": 0, "status": "EMPTY"}

    return {
        "total_handoff_items": len(df),
        "target_phase": 119,
        "ready_items_count": int((df["status"] == "READY").sum()) if "status" in df.columns else 0,
        "forward_contract_count": int((df["status"] == "FORWARD_CONTRACT").sum()) if "status" in df.columns else 0,
        "non_signal": True,
        "handoff_status": "READY",
    }
