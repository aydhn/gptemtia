from typing import Tuple, Dict, Any
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile
from advanced_technical_indicators.technical_indicator_models import (
    TechnicalIndicatorDomain,
    build_technical_indicator_domain_id,
)

DOMAINS_DATA = [
    {
        "label": "technical_indicator_profile_domain",
        "name": "Technical Indicator Profile Registry Domain",
        "desc": "Offline teknik indikatör profilleri ve güvenlik sınırları.",
        "outputs": ["technical_indicator_profile_registry.csv"],
    },
    {
        "label": "technical_indicator_domain",
        "name": "Technical Indicator Core Domain",
        "desc": "Genel teknik gösterge motoru alan tanımları.",
        "outputs": ["technical_indicator_catalog_expansion.csv"],
    },
    {
        "label": "price_action_domain",
        "name": "Price Action Indicator Domain",
        "desc": "High/Low range, Close/Open range, range pct, gap, close location value.",
        "outputs": ["price_action_indicator_registry.csv"],
    },
    {
        "label": "return_indicator_domain",
        "name": "Return Indicator Domain",
        "desc": "Simple return, log return, cumulative return, rolling return sum, return/vol ratio.",
        "outputs": ["return_indicator_registry.csv"],
    },
    {
        "label": "moving_average_domain",
        "name": "Moving Average Indicator Domain",
        "desc": "SMA, EMA, WMA, DEMA, TEMA, MA distance.",
        "outputs": ["moving_average_indicator_registry.csv"],
    },
    {
        "label": "trend_indicator_domain",
        "name": "Trend Indicator Domain",
        "desc": "MACD, PPO, Donchian channel, Aroon, ADX/DMI placeholder, Ichimoku placeholder.",
        "outputs": ["trend_indicator_expansion_registry.csv"],
    },
    {
        "label": "momentum_indicator_domain",
        "name": "Momentum Indicator Domain",
        "desc": "Momentum, ROC, RSI, CMO, TSI placeholder.",
        "outputs": ["momentum_indicator_expansion_registry.csv"],
    },
    {
        "label": "oscillator_indicator_domain",
        "name": "Oscillator Indicator Domain",
        "desc": "Stochastic, Williams %R, CCI, Ultimate Oscillator placeholder, MFI placeholder.",
        "outputs": ["oscillator_indicator_registry.csv"],
    },
    {
        "label": "volatility_indicator_domain",
        "name": "Volatility Indicator Domain",
        "desc": "True Range, ATR, Rolling STD, Realized Vol, Parkinson Vol, Garman-Klass placeholder.",
        "outputs": ["volatility_indicator_expansion_registry.csv"],
    },
    {
        "label": "range_indicator_domain",
        "name": "Range Indicator Domain",
        "desc": "Rolling High-Low range, Rolling range pct, Average range, Range z-score.",
        "outputs": ["range_indicator_registry.csv"],
    },
    {
        "label": "channel_indicator_domain",
        "name": "Channel Indicator Domain",
        "desc": "Bollinger Bands, Bandwidth, %B, Keltner Channel placeholder, Donchian position.",
        "outputs": ["channel_indicator_registry.csv"],
    },
    {
        "label": "candle_anatomy_domain",
        "name": "Candle Anatomy Feature Domain",
        "desc": "Candle body size, body pct, upper wick, lower wick, wick balance.",
        "outputs": ["candle_anatomy_feature_registry.csv"],
    },
    {
        "label": "quote_microstructure_domain",
        "name": "Quote Microstructure Feature Domain",
        "desc": "Quote mid, spread, spread pct, bid/ask ratio placeholder, staleness placeholder.",
        "outputs": ["quote_microstructure_feature_registry.csv"],
    },
    {
        "label": "mean_reversion_domain",
        "name": "Mean Reversion Feature Domain",
        "desc": "Rolling z-score, distance to SMA/EMA, percentile rank placeholder, deviation ratio.",
        "outputs": ["mean_reversion_indicator_expansion_registry.csv"],
    },
    {
        "label": "indicator_parameter_domain",
        "name": "Indicator Parameter Contract Domain",
        "desc": "Pencere ve çarpan parametre doğrulama kuralları.",
        "outputs": ["indicator_parameter_contract_registry.csv"],
    },
    {
        "label": "indicator_output_schema_domain",
        "name": "Indicator Output Schema Domain",
        "desc": "Çıktı kolon isimleri ve yasaklı takma ad kontrolleri.",
        "outputs": ["indicator_output_schema_registry.csv"],
    },
    {
        "label": "warmup_nan_policy_domain",
        "name": "Warmup NaN Policy Domain",
        "desc": "Pencere büyüklüğüne göre beklenen başlangıç NaN politikası.",
        "outputs": ["indicator_warmup_nan_policy_registry.csv"],
    },
    {
        "label": "no_lookahead_guard_domain",
        "name": "No Lookahead Guard Domain",
        "desc": "Negatif shift ve gelecek tahmin kolonlarının engellenmesi.",
        "outputs": ["no_lookahead_indicator_guard_registry.csv"],
    },
    {
        "label": "computation_interface_domain",
        "name": "Indicator Computation Interface Domain",
        "desc": "Standart hesaplama arayüz sözleşmesi.",
        "outputs": ["indicator_computation_interface_contract.csv"],
    },
    {
        "label": "computation_rehearsal_domain",
        "name": "Computation Rehearsal Domain",
        "desc": "Sentetik verilerle non-mutating hesaplama provası.",
        "outputs": ["indicator_computation_rehearsal_report.csv"],
    },
    {
        "label": "validation_rule_domain",
        "name": "Indicator Validation Rule Domain",
        "desc": "Sayısal geçerlilik ve kural kontrolleri.",
        "outputs": ["indicator_validation_rule_registry.csv"],
    },
    {
        "label": "dependency_domain",
        "name": "Indicator Dependency Domain",
        "desc": "İndikatörler arası bağımlılık grafiği.",
        "outputs": ["indicator_dependency_registry.csv"],
    },
    {
        "label": "quality_handoff_domain",
        "name": "Quality Handoff Domain",
        "desc": "Kalite güvencesi ve Phase 118 devir kontrolleri.",
        "outputs": ["indicator_quality_handoff_report.csv"],
    },
    {
        "label": "technical_indicator_health_domain",
        "name": "Health Check Domain",
        "desc": "Sistem sağlık durumu kontrolü.",
        "outputs": ["technical_indicator_health_check.csv"],
    },
    {
        "label": "technical_indicator_validation_domain",
        "name": "Validation Domain",
        "desc": "Bütünlük ve kural doğrulama raporu.",
        "outputs": ["technical_indicator_validation_report.csv"],
    },
    {
        "label": "technical_indicator_safety_domain",
        "name": "Safety Boundary Domain",
        "desc": "Safe-Go ve No-Go kuralları.",
        "outputs": ["technical_indicator_safety_boundary.csv"],
    },
    {
        "label": "phase_118_handoff_domain",
        "name": "Phase 118 Multi-Window Feature Grid Handoff Domain",
        "desc": "Phase 118 multi-window devir raporu.",
        "outputs": ["phase_118_multi_window_feature_grid_handoff_report.csv"],
    },
]


def build_technical_indicator_domain_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = []
    for d in DOMAINS_DATA:
        dom = TechnicalIndicatorDomain(
            domain_id=build_technical_indicator_domain_id(d["label"]),
            domain_label=d["label"],
            domain_name=d["name"],
            description=d["desc"],
            required_outputs=d["outputs"],
            warnings=[],
        )
        items.append(dom.to_dict())

    df = pd.DataFrame(items)
    summary = {
        "total_domains": len(df),
        "status": "READY",
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
    }
    return df, summary
