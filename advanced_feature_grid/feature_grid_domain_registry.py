from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile
from advanced_feature_grid.feature_grid_models import FeatureGridDomain, build_feature_grid_domain_id


DOMAIN_DEFINITIONS = [
    {
        "label": "feature_grid_profile_domain",
        "name": "Feature Grid Profile Domain",
        "description": "Multi-window feature grid profillerinin ve parametre kısıtlarının yönetildiği alan.",
        "required_outputs": ["profile_registry", "profile_summary"],
    },
    {
        "label": "window_grid_contract_domain",
        "name": "Window Grid Contract Domain",
        "description": "Kısa, orta, uzun ve dengeli window grid sözleşmelerinin tanımlandığı alan.",
        "required_outputs": ["window_contracts", "contract_summary"],
    },
    {
        "label": "parameter_grid_domain",
        "name": "Indicator Parameter Grid Domain",
        "description": "SMA, EMA, RSI, ATR, Bollinger vb. indikatörler için parametre matrisleri.",
        "required_outputs": ["parameter_grid_registry", "grid_expansion_summary"],
    },
    {
        "label": "naming_domain",
        "name": "Feature Grid Naming Domain",
        "description": "Deterministik ve non-signal feature isimlendirme kuralları.",
        "required_outputs": ["naming_registry", "naming_rules"],
    },
    {
        "label": "output_schema_domain",
        "name": "Output Schema Domain",
        "description": "Grid çıktılarının veri tipleri, nullability ve yasak alias denetimi.",
        "required_outputs": ["output_schema_registry", "schema_validation"],
    },
    {
        "label": "warmup_nan_policy_domain",
        "name": "Warmup NaN Policy Domain",
        "description": "Rolling pencereler nedeniyle oluşan ilk satır NaN değerlerinin muhafaza politikası.",
        "required_outputs": ["warmup_policy_registry", "warmup_estimates"],
    },
    {
        "label": "no_lookahead_guard_domain",
        "name": "No-Lookahead Guard Domain",
        "description": "shift(-1), forward return ve target/label üretimini engelleyen denetim katmanı.",
        "required_outputs": ["no_lookahead_registry", "guard_findings"],
    },
    {
        "label": "duplicate_detection_domain",
        "name": "Duplicate Detection Domain",
        "description": "Aynı feature'ın mükerrer hesaplanmasını tespit eden registry.",
        "required_outputs": ["duplicate_registry", "duplicate_findings"],
    },
    {
        "label": "moving_average_grid_domain",
        "name": "Moving Average Window Grid Domain",
        "description": "SMA, EMA, WMA, DEMA/TEMA çoklu pencere varyantları.",
        "required_outputs": ["moving_average_grid", "ma_summary"],
    },
    {
        "label": "momentum_grid_domain",
        "name": "Momentum Window Grid Domain",
        "description": "RSI, ROC, Momentum, CMO çoklu pencere varyantları.",
        "required_outputs": ["momentum_grid", "momentum_summary"],
    },
    {
        "label": "volatility_grid_domain",
        "name": "Volatility Window Grid Domain",
        "description": "ATR, rolling std, realized volatility, Parkinson çoklu pencere varyantları.",
        "required_outputs": ["volatility_grid", "volatility_summary"],
    },
    {
        "label": "range_channel_grid_domain",
        "name": "Range & Channel Window Grid Domain",
        "description": "Bollinger Bands, Donchian Channel, rolling range parametre gridleri.",
        "required_outputs": ["range_channel_grid", "channel_summary"],
    },
    {
        "label": "mean_reversion_grid_domain",
        "name": "Mean Reversion Window Grid Domain",
        "description": "Rolling z-score, distance to MA, percentile rank gridleri.",
        "required_outputs": ["mean_reversion_grid", "mr_summary"],
    },
    {
        "label": "return_grid_domain",
        "name": "Return Window Grid Domain",
        "description": "Simple return, log return, cumulative return çoklu window varyantları.",
        "required_outputs": ["return_grid", "return_summary"],
    },
    {
        "label": "quote_grid_placeholder_domain",
        "name": "Quote Microstructure Grid Placeholder Domain",
        "description": "Spread, staleness, quote mid return placeholder gridleri.",
        "required_outputs": ["quote_placeholder_grid"],
    },
    {
        "label": "macro_grid_placeholder_domain",
        "name": "Macro Indicator Grid Placeholder Domain",
        "description": "Macro value change, rolling change placeholder gridleri.",
        "required_outputs": ["macro_placeholder_grid"],
    },
    {
        "label": "calendar_grid_placeholder_domain",
        "name": "Economic Calendar Grid Placeholder Domain",
        "description": "Pre/post event window flags, rolling event count placeholder gridleri.",
        "required_outputs": ["calendar_placeholder_grid"],
    },
    {
        "label": "news_grid_placeholder_domain",
        "name": "News Metadata Grid Placeholder Domain",
        "description": "News topic count, asset tag count placeholder gridleri.",
        "required_outputs": ["news_placeholder_grid"],
    },
    {
        "label": "computation_interface_domain",
        "name": "Computation Interface Domain",
        "description": "In-place DataFrame mutasyonunu engelleyen safe computation arayüzü.",
        "required_outputs": ["computation_interfaces"],
    },
    {
        "label": "computation_rehearsal_domain",
        "name": "Computation Rehearsal Domain",
        "description": "Sentetik verilerle non-signal prova ve doğrulama motoru.",
        "required_outputs": ["rehearsal_report"],
    },
    {
        "label": "metadata_domain",
        "name": "Feature Grid Metadata Domain",
        "description": "Tüm grid feature'larının parametre, warmup ve handoff metadata kataloğu.",
        "required_outputs": ["metadata_registry"],
    },
    {
        "label": "dependency_domain",
        "name": "Feature Grid Dependency Domain",
        "description": "Grid girdilerinin OHLCV alan bağımlılıkları haritası.",
        "required_outputs": ["dependency_registry"],
    },
    {
        "label": "validation_domain",
        "name": "Validation Rule Domain",
        "description": "Sayısal geçerlilik, forbidden column ve row count denetimleri.",
        "required_outputs": ["validation_rules", "validation_findings"],
    },
    {
        "label": "quality_handoff_domain",
        "name": "Quality Handoff Domain",
        "description": "Phase 119 ve sonraki fazlar için hazır bulunuşluk ve kalite handoff'u.",
        "required_outputs": ["quality_handoff_report"],
    },
    {
        "label": "feature_grid_health_domain",
        "name": "Feature Grid Health Domain",
        "description": "Modül importları, bağımlılıklar ve test sağlık durumu.",
        "required_outputs": ["health_check_report"],
    },
    {
        "label": "feature_grid_safety_domain",
        "name": "Safety Boundary Domain",
        "description": "No-go ve Safe-go koşullarının kesin sınır matrisi.",
        "required_outputs": ["safety_boundary_report"],
    },
    {
        "label": "phase_119_handoff_domain",
        "name": "Phase 119 Cross-Asset Alignment Handoff Domain",
        "description": "Cross-asset feature alignment aşamasına aktarılacak sözleşmeler.",
        "required_outputs": ["phase_119_handoff_report"],
    },
]


def build_feature_grid_domain_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    domains = []

    for item in DOMAIN_DEFINITIONS:
        domain = FeatureGridDomain(
            domain_id=build_feature_grid_domain_id(item["label"]),
            domain_label=item["label"],
            domain_name=item["name"],
            description=item["description"],
            required_outputs=item["required_outputs"],
            warnings=[],
        )
        domains.append(domain.to_dict())

    df = pd.DataFrame(domains)
    summary = {
        "profile": active_profile.name,
        "total_domains": len(df),
        "current_phase": active_profile.current_phase,
        "status": "READY",
        "non_signal": True,
    }
    return df, summary
