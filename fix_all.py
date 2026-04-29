import re
import os
import pandas as pd

# Fix Settings
with open('commodity_fx_signal_bot/config/settings.py', 'r') as f:
    settings_content = f.read()

momentum_settings = """
    # Phase 8: Momentum Features & Events Settings
    momentum_features_enabled: bool = field(default_factory=lambda: os.getenv("MOMENTUM_FEATURES_ENABLED", "true").lower() == "true")
    momentum_events_enabled: bool = field(default_factory=lambda: os.getenv("MOMENTUM_EVENTS_ENABLED", "true").lower() == "true")
    default_momentum_windows: tuple[int, ...] = field(default_factory=lambda: tuple(int(x) for x in os.getenv("DEFAULT_MOMENTUM_WINDOWS", "7,14,21,28").split(",")))
    default_roc_windows: tuple[int, ...] = field(default_factory=lambda: tuple(int(x) for x in os.getenv("DEFAULT_ROC_WINDOWS", "5,10,20").split(",")))
    default_momentum_overbought_rsi: float = field(default_factory=lambda: float(os.getenv("DEFAULT_MOMENTUM_OVERBOUGHT_RSI", "70.0")))
    default_momentum_oversold_rsi: float = field(default_factory=lambda: float(os.getenv("DEFAULT_MOMENTUM_OVERSOLD_RSI", "30.0")))
    default_stochastic_overbought: float = field(default_factory=lambda: float(os.getenv("DEFAULT_STOCHASTIC_OVERBOUGHT", "80.0")))
    default_stochastic_oversold: float = field(default_factory=lambda: float(os.getenv("DEFAULT_STOCHASTIC_OVERSOLD", "20.0")))
    save_momentum_features: bool = field(default_factory=lambda: os.getenv("SAVE_MOMENTUM_FEATURES", "true").lower() == "true")
    save_momentum_events: bool = field(default_factory=lambda: os.getenv("SAVE_MOMENTUM_EVENTS", "true").lower() == "true")
"""
if "default_momentum_overbought_rsi" not in settings_content:
    settings_content = settings_content.replace(
        "    paper_trading_enabled: bool = field(",
        f"{momentum_settings}\n    paper_trading_enabled: bool = field("
    )
    with open('commodity_fx_signal_bot/config/settings.py', 'w') as f:
        f.write(settings_content)


# Fix Report Builder
with open('commodity_fx_signal_bot/reports/report_builder.py', 'r') as f:
    report_content = f.read()

new_report_functions = """

def build_momentum_feature_preview_report(symbol: str, timeframe: str, summary: dict, tail_df: pd.DataFrame) -> str:
    lines = [
        "=== MOMENTUM FEATURE PREVIEW ===",
        f"Sembol: {symbol}",
        f"Zaman Dilimi: {timeframe}",
        f"Input Satır: {summary.get('input_rows', 0)}",
        f"Output Satır: {summary.get('output_rows', 0)}",
        f"Feature Sayısı: {summary.get('feature_count', 0)}",
        f"Event Sayısı: {summary.get('event_count', 0)}",
        f"Eksik Veri Oranı: %{summary.get('total_nan_ratio', 0) * 100:.2f}",
        "",
        "Üretilen Feature Kolonları:",
    ]
    for col in summary.get('feature_columns', []):
        lines.append(f"  - {col}")

    lines.append("")
    lines.append("Son Satırlar (Örnek):")
    lines.append(tail_df.to_string())
    lines.append("================================")

    return "\\n".join(lines)


def build_momentum_event_preview_report(symbol: str, timeframe: str, summary: dict, event_tail_df: pd.DataFrame) -> str:
    lines = [
        "=== MOMENTUM EVENT PREVIEW ===",
        f"Sembol: {symbol}",
        f"Zaman Dilimi: {timeframe}",
        "Uyarı: Bu eventler nihai al/sat sinyali değildir. Sadece ön aday sinyallerdir.",
        "",
        f"Toplam Event Tipi Sayısı: {len(summary.get('event_columns', []))}",
        f"Tarihsel Toplam Event Adedi: {summary.get('total_event_count', 0)}",
        "",
        "En Sık Oluşan Eventler:",
    ]

    counts = summary.get('event_count_by_column', {})
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    for k, v in sorted_counts[:10]:
        lines.append(f"  - {k}: {v} kez")

    lines.append("")
    lines.append("Son Satırdaki Aktif Eventler:")
    for ev in summary.get('active_last_row_events', []):
        lines.append(f"  - {ev}")

    lines.append("")
    lines.append("Son Satırlar (Örnek):")
    lines.append(event_tail_df.to_string())
    lines.append("==============================")

    return "\\n".join(lines)


def build_momentum_batch_report(summary: dict) -> str:
    lines = [
        "=== MOMENTUM BATCH BUILD RAPORU ===",
        f"Toplam Deneme: {summary.get('total_attempts', 0)}",
        f"Başarılı: {summary.get('success_count', 0)}",
        f"Atlanan: {summary.get('skipped_count', 0)}",
        f"Başarısız: {summary.get('failure_count', 0)}",
        "===================================="
    ]
    return "\\n".join(lines)


def build_momentum_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = [
        "=== MOMENTUM DATA LAKE STATUS ===",
        f"Toplam Sembol-Zaman Dilimi Kombinasyonu: {summary.get('total_combinations', 0)}",
        f"Technical Feature Var ama Momentum Yok: {summary.get('missing_momentum', 0)}",
        f"Processed Data Var ama Momentum Yok: {summary.get('processed_without_momentum', 0)}",
        "",
    ]

    if not status_df.empty:
        missing = status_df[~status_df["Has Momentum"]]
        if not missing.empty:
            lines.append("Eksik Momentum Feature'ları Olanlar (Örnek 10):")
            for idx, row in missing.head(10).iterrows():
                lines.append(f"  - {row['Symbol']} ({row['Timeframe']})")
    else:
        lines.append("Mevcut data yok.")

    lines.append("=================================")
    return "\\n".join(lines)
"""
if "build_momentum_feature_preview_report" not in report_content:
    report_content = report_content + new_report_functions
    with open('commodity_fx_signal_bot/reports/report_builder.py', 'w') as f:
        f.write(report_content)
