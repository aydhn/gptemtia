"""Phase 124 Feature Store Entity Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

CORE_ENTITIES = [
    {
        "entity_type": "entity_fx_pair",
        "entity_id": "fx_pair",
        "description": "Döviz çiftleri varlık tanımlayıcısı (EURUSD, GBPUSD, USDJPY, USDTRY).",
        "identifier_field": "symbol",
        "source_phase": 107,
        "namespace_prefix": "fx",
        "sample_keys": "EURUSD,GBPUSD,USDJPY,USDTRY",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "entity_commodity_symbol",
        "entity_id": "commodity_symbol",
        "description": "Emtia sembolleri varlık tanımlayıcısı (BRENT, WTI, XAUUSD, XAGUSD).",
        "identifier_field": "symbol",
        "source_phase": 108,
        "namespace_prefix": "commodity",
        "sample_keys": "BRENT,WTI,XAUUSD,XAGUSD",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "entity_macro_indicator",
        "entity_id": "macro_indicator",
        "description": "Makroekonomik indikatör serisi tanımlayıcısı (US10Y, DXY, FEDFUNDS).",
        "identifier_field": "indicator_id",
        "source_phase": 109,
        "namespace_prefix": "macro",
        "sample_keys": "US10Y,DXY,FEDFUNDS,US_CPI",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "entity_calendar_event",
        "entity_id": "calendar_event",
        "description": "Ekonomik takvim olay tanımlayıcısı (FOMC, NFP, CPI).",
        "identifier_field": "event_id",
        "source_phase": 110,
        "namespace_prefix": "calendar",
        "sample_keys": "FOMC_RATE_DECISION,US_NFP,US_CPI_RELEASE",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "entity_news_metadata",
        "entity_id": "news_metadata_tag",
        "description": "Haber metaveri etiket tanımlayıcısı (tam metin içermeyen başlık/etiket).",
        "identifier_field": "tag_id",
        "source_phase": 111,
        "namespace_prefix": "news",
        "sample_keys": "ENERGY_SUPPLY_EVENT,CENTRAL_BANK_SPEECH",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "entity_cross_asset_context",
        "entity_id": "cross_asset_context",
        "description": "Çapraz varlık bağlam tanımlayıcısı (döviz-emtia-makro korelasyonu).",
        "identifier_field": "context_id",
        "source_phase": 119,
        "namespace_prefix": "cross_asset",
        "sample_keys": "COMMODITY_FX_CONTEXT,MACRO_COMMODITY_CONTEXT",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "entity_type": "entity_factor_family",
        "entity_id": "factor_family",
        "description": "Faktör ailesi tanımlayıcısı (Phase 122 kanonik faktör taksonomisi).",
        "identifier_field": "family_name",
        "source_phase": 122,
        "namespace_prefix": "factor",
        "sample_keys": "technical,trend,momentum,volatility,macro_context",
        "non_signal": True,
        "source_preserved": True,
    },
]


def build_feature_store_entity_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of feature store entities."""
    prof = profile or get_default_feature_store_integration_profile()
    records = []
    for e in CORE_ENTITIES:
        item = dict(e)
        item["current_phase"] = prof.current_phase
        item["target_final_phase"] = prof.target_final_phase
        records.append(item)

    df = pd.DataFrame(records)
    summary = {
        "total_entities": len(records),
        "entity_types": list(set(r["entity_type"] for r in records)),
        "non_signal": True,
        "source_preserved": True,
        "destructive_action_allowed": False,
    }
    return df, summary


def summarize_feature_store_entity_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize entity registry."""
    return {
        "total_entities": len(df) if not df.empty else 0,
        "non_signal": True,
        "source_preserved": True,
    }
