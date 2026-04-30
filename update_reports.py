with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

reports_to_add = """
def build_trend_feature_preview_report(
    symbol: str, timeframe: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = [
        "=== TREND FEATURE PREVIEW ===",
        f"Sembol: {symbol}",
        f"Zaman Dilimi: {timeframe}",
        f"Input Satır: {summary.get('input_rows', 0)}",
        f"Output Satır: {summary.get('output_rows', 0)}",
        f"Feature Sayısı: {summary.get('feature_count', 0)}",
        f"Event Sayısı: {summary.get('event_count', 0)}",
        f"Eksik Veri Oranı: %{summary.get('total_nan_ratio', 0) * 100:.2f}",
        "",
        "Uyarılar:",
    ]
    for w in summary.get("warnings", []):
        lines.append(f"  - {w}")

    lines.append("")
    lines.append("Üretilen Feature Kolonları:")
    for col in summary.get("feature_columns", []):
        lines.append(f"  - {col}")

    lines.append("")
    lines.append("Son Satırlar (Örnek):")
    lines.append(tail_df.to_string())
    lines.append("================================")

    return "\\n".join(lines)


def build_trend_event_preview_report(
    symbol: str, timeframe: str, summary: dict, event_tail_df: pd.DataFrame
) -> str:
    lines = [
        "=== TREND EVENT PREVIEW ===",
        f"Sembol: {symbol}",
        f"Zaman Dilimi: {timeframe}",
        "Uyarı: Bu eventler nihai al/sat sinyali değildir. Sadece ön aday sinyallerdir.",
        "",
        f"Toplam Event Tipi Sayısı: {len(summary.get('event_columns', []))}",
        f"Tarihsel Toplam Event Adedi: {summary.get('total_event_count', 0)}",
        "",
        "En Sık Oluşan Eventler:",
    ]

    counts = summary.get("event_count_by_column", {})
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    for k, v in sorted_counts[:10]:
        lines.append(f"  - {k}: {v} kez")

    lines.append("")
    lines.append("Son Satırdaki Aktif Eventler:")
    for ev in summary.get("active_last_row_events", []):
        lines.append(f"  - {ev}")

    lines.append("")
    lines.append("Son Satırlar (Örnek):")
    lines.append(event_tail_df.to_string())
    lines.append("==============================")

    return "\\n".join(lines)


def build_trend_batch_report(summary: dict) -> str:
    lines = [
        "=== TREND BATCH BUILD RAPORU ===",
        f"Toplam Deneme: {summary.get('total_attempts', 0)}",
        f"Başarılı: {summary.get('success_count', 0)}",
        f"Atlanan: {summary.get('skipped_count', 0)}",
        f"Başarısız: {summary.get('failure_count', 0)}",
        "====================================",
    ]
    return "\\n".join(lines)


def build_trend_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = [
        "=== TREND DATA LAKE STATUS ===",
        f"Toplam Sembol-Zaman Dilimi Kombinasyonu: {summary.get('total_combinations', 0)}",
        f"Technical Feature Var ama Trend Yok: {summary.get('missing_trend', 0)}",
        f"Processed Data Var ama Trend Yok: {summary.get('processed_without_trend', 0)}",
        "",
    ]

    if not status_df.empty:
        missing = status_df[~status_df["Has Trend"]]
        if not missing.empty:
            lines.append("Eksik Trend Feature'ları Olanlar (Örnek 10):")
            for idx, row in missing.head(10).iterrows():
                lines.append(f"  - {row['Symbol']} ({row['Timeframe']})")
    else:
        lines.append("Mevcut data yok.")

    lines.append("=================================")
    return "\\n".join(lines)
"""

if "build_trend_feature_preview_report" not in content:
    content += reports_to_add
    with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
        f.write(content)
