from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    FeatureEngineDomain,
    build_feature_engine_domain_id,
)


FEATURE_DOMAINS = [
    {
        "domain_label": "feature_engine_profile_domain",
        "domain_name": "Feature Engine Profile Registry Domain",
        "description": "Offline feature engine profilleri ve operasyonel güvenlik parametreleri.",
        "required_outputs": ["feature_engine_profile_registry.csv", "profile_report.json"],
    },
    {
        "domain_label": "feature_input_contract_domain",
        "domain_name": "Feature Input Contract Domain",
        "description": "Kanonik veri setleri için zorunlu ve isteğe bağlı girdi alanı kontratları.",
        "required_outputs": ["feature_input_contract_registry.csv"],
    },
    {
        "domain_label": "feature_schema_domain",
        "domain_name": "Feature Schema Registry Domain",
        "description": "Bireysel feature tanımları, veri tipleri, lookback pencereleri ve zorunlu alanlar.",
        "required_outputs": ["feature_schema_registry.csv"],
    },
    {
        "domain_label": "factor_schema_domain",
        "domain_name": "Factor Schema Registry Domain",
        "description": "Kompozit faktör tanımları, feature bağımlılıkları ve araştırma sahipleri.",
        "required_outputs": ["factor_schema_registry.csv"],
    },
    {
        "domain_label": "indicator_catalog_domain",
        "domain_name": "Indicator Catalog Registry Domain",
        "description": "Desteklenen tüm teknik göstergelerin ana kataloğu ve non-signal kullanım notları.",
        "required_outputs": ["indicator_catalog_registry.csv"],
    },
    {
        "domain_label": "price_indicator_domain",
        "domain_name": "Price Indicator Catalog Domain",
        "description": "Fiyat değişimleri, log return, range ve rolling istatistikler kataloğu.",
        "required_outputs": ["price_indicator_catalog.csv"],
    },
    {
        "domain_label": "trend_indicator_domain",
        "domain_name": "Trend Indicator Catalog Domain",
        "description": "SMA, EMA, WMA, MACD, ADX, Ichimoku ve Donchian trend göstergeleri.",
        "required_outputs": ["trend_indicator_catalog.csv"],
    },
    {
        "domain_label": "momentum_indicator_domain",
        "domain_name": "Momentum Indicator Catalog Domain",
        "description": "RSI, ROC, momentum, stochastic ve Williams %R osilatörleri.",
        "required_outputs": ["momentum_indicator_catalog.csv"],
    },
    {
        "domain_label": "volatility_indicator_domain",
        "domain_name": "Volatility Indicator Catalog Domain",
        "description": "Rolling std, ATR, true range ve realised volatilite metrikleri.",
        "required_outputs": ["volatility_indicator_catalog.csv"],
    },
    {
        "domain_label": "mean_reversion_indicator_domain",
        "domain_name": "Mean Reversion Indicator Catalog Domain",
        "description": "Z-score, bollinger z-score ve hareketli ortalamaya mesafe metrikleri.",
        "required_outputs": ["mean_reversion_indicator_catalog.csv"],
    },
    {
        "domain_label": "quote_feature_domain",
        "domain_name": "Quote Feature Catalog Domain",
        "description": "Bid-ask spread, spread yüzdesi ve mid-price hesaplama özellikleri.",
        "required_outputs": ["quote_feature_catalog.csv"],
    },
    {
        "domain_label": "volume_liquidity_feature_domain",
        "domain_name": "Volume & Liquidity Placeholder Catalog Domain",
        "description": "Hacim değişimi, likidite ve açık pozisyon değişim placeholder'ları.",
        "required_outputs": ["volume_liquidity_placeholder_catalog.csv"],
    },
    {
        "domain_label": "macro_feature_domain",
        "domain_name": "Macro Feature Catalog Domain",
        "description": "Makro değer değişimleri, sürpriz farkları ve revizyon etiketleri.",
        "required_outputs": ["macro_feature_catalog.csv"],
    },
    {
        "domain_label": "calendar_feature_domain",
        "domain_name": "Calendar Event Feature Catalog Domain",
        "description": "Olay günü bayrakları, olay öncesi/sonrası pencereleri ve takvim ağırlıkları.",
        "required_outputs": ["calendar_event_feature_catalog.csv"],
    },
    {
        "domain_label": "news_metadata_feature_domain",
        "domain_name": "News Metadata Feature Catalog Domain",
        "description": "Haber konu bayrakları, varlık etiket sayıları ve tazelik özellikleri (sıfır tam metin).",
        "required_outputs": ["news_metadata_feature_catalog.csv"],
    },
    {
        "domain_label": "feature_metadata_domain",
        "domain_name": "Feature Metadata Registry Domain",
        "description": "Lookahead koruması, warmup gereksinimleri ve hesaplama maliyetleri.",
        "required_outputs": ["feature_metadata_registry.csv"],
    },
    {
        "domain_label": "factor_metadata_domain",
        "domain_name": "Factor Metadata Registry Domain",
        "description": "Faktör ailesi hiyerarşisi, normalizasyon ve Phase 125 genişleme yol haritası.",
        "required_outputs": ["factor_metadata_registry.csv"],
    },
    {
        "domain_label": "rolling_window_domain",
        "domain_name": "Rolling Window Contract Domain",
        "description": "Standart rolling window parametreleri ve lookahead koruma kontratı.",
        "required_outputs": ["rolling_window_contract_registry.csv"],
    },
    {
        "domain_label": "feature_computation_domain",
        "domain_name": "Feature Computation Interface Domain",
        "description": "Non-destructive dataframe dönüşüm arayüzleri ve pandas/numpy fonksiyonları.",
        "required_outputs": ["feature_computation_contract.csv"],
    },
    {
        "domain_label": "feature_dependency_domain",
        "domain_name": "Feature Dependency Graph Domain",
        "description": "Tablosal feature ve faktör bağımlılık haritası placeholder'ı.",
        "required_outputs": ["feature_dependency_graph.csv"],
    },
    {
        "domain_label": "feature_validation_domain",
        "domain_name": "Feature Validation Rule Domain",
        "description": "Sinyal kolonlarını, hedef değişkenleri ve lookahead sızıntılarını engelleyen kurallar.",
        "required_outputs": ["feature_validation_rule_registry.csv"],
    },
    {
        "domain_label": "feature_quality_handoff_domain",
        "domain_name": "Feature Quality Handoff Domain",
        "description": "Phase 112-115 çıktılarını feature engine girdi filtrelerine bağlayan köprü.",
        "required_outputs": ["feature_quality_handoff_registry.csv"],
    },
    {
        "domain_label": "feature_safety_domain",
        "domain_name": "Feature Safety Boundary Domain",
        "description": "No-Go ve Safe-Go güvenlik sınırları.",
        "required_outputs": ["feature_safety_boundary.csv"],
    },
    {
        "domain_label": "phase_117_handoff_domain",
        "domain_name": "Phase 117 Technical Indicator Expansion Handoff Domain",
        "description": "Phase 117 teknik gösterge genişleme handoff raporu.",
        "required_outputs": ["phase_117_handoff_report.csv"],
    },
]


def build_feature_engine_domain_registry(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items: List[Dict[str, Any]] = []

    for d in FEATURE_DOMAINS:
        item = FeatureEngineDomain(
            domain_id=build_feature_engine_domain_id(d["domain_label"]),
            domain_label=d["domain_label"],
            domain_name=d["domain_name"],
            description=d["description"],
            required_outputs=d["required_outputs"],
            warnings=[],
        )
        items.append(item.to_dict())

    df = pd.DataFrame.from_records(items)
    summary = summarize_feature_engine_domain_registry(df, profile)
    return df, summary


def summarize_feature_engine_domain_registry(
    df: pd.DataFrame,
    profile: FeatureEngineProfile,
) -> Dict[str, Any]:
    return {
        "total_domains": len(df),
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "all_domains_defined": len(df) >= 20,
    }
