from typing import Tuple, Dict, Any
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile

HANDOFF_ITEMS = [
    {
        "domain": "multi_window_moving_averages",
        "topic": "Multi-window SMA/EMA/WMA/DEMA grid",
        "readiness": "READY",
        "notes": "Pencereler [5, 10, 20, 50, 100, 200] parametrik grid üretimine uygun.",
    },
    {
        "domain": "multi_window_momentum",
        "topic": "Multi-window RSI/ROC/Momentum grid",
        "readiness": "READY",
        "notes": "RSI ve ROC için [7, 14, 21, 28] grid pencereleri hazır.",
    },
    {
        "domain": "multi_window_volatility",
        "topic": "Multi-window ATR/Rolling STD/Realized Vol grid",
        "readiness": "READY",
        "notes": "ATR ve oynaklık oranları pencereli yapıya uygun.",
    },
    {
        "domain": "multi_window_channels",
        "topic": "Multi-window Bollinger/Donchian grid",
        "readiness": "READY",
        "notes": "Bant genişliği ve percent_b çoklu pencere üretimine hazır.",
    },
    {
        "domain": "feature_naming_convention",
        "topic": "Grid feature adlandırma standardı",
        "readiness": "READY",
        "notes": "{indicator}_{window} formatı standartlaştırıldı.",
    },
    {
        "domain": "rolling_warmup_nan_handling",
        "topic": "Pencereye göre dinamik NaN politikası",
        "readiness": "READY",
        "notes": "Pencere büyüdükçe beklenen NaN sayısı estimate_warmup_nan_count ile belirlenebilir.",
    },
    {
        "domain": "no_lookahead_multi_window_guard",
        "topic": "Çoklu pencere hesaplamalarında lookahead koruması",
        "readiness": "READY",
        "notes": "Tüm grid hesaplamaları geçmiş veriye dayalı (shift >= 0).",
    },
    {
        "domain": "duplicate_feature_detection",
        "topic": "Tekrarlı feature kontrol altyapısı",
        "readiness": "READY",
        "notes": "Aynı pencere ve indikatör için mükerrer kolon üretimi engellenir.",
    },
    {
        "domain": "feature_dependency_expansion",
        "topic": "Bağımlılık grafiği genişletmesi",
        "readiness": "READY",
        "notes": "İndikatör girdi zincirleri indicator_dependency_registry ile hazırlandı.",
    },
    {
        "domain": "phase_121_validation_readiness",
        "topic": "Phase 121 doğrulama ve lookahead denetimine devir",
        "readiness": "READY",
        "notes": "Katmanlı no-lookahead ve non-signal sınırları devrediliyor.",
    },
]


def build_phase_118_multi_window_feature_grid_handoff_report(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame(HANDOFF_ITEMS)
    all_ready = bool((df["readiness"] == "READY").all())
    summary = {
        "total_handoff_items": len(df),
        "all_items_ready": all_ready,
        "handoff_status": "READY" if all_ready else "PENDING",
        "current_phase": profile.current_phase,
        "next_phase": profile.next_phase,
        "target_final_phase": profile.target_final_phase,
    }
    return df, summary


def summarize_phase_118_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_items": len(df),
        "status": "READY" if not df.empty else "EMPTY",
    }
