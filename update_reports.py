import re

file_path = "commodity_fx_signal_bot/reports/report_builder.py"
with open(file_path, "r") as f:
    content = f.read()

new_functions = """
def build_regime_feature_preview_report(
    symbol: str, timeframe: str, profile_name: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = []
    lines.append(f"=== Rejim Feature Önizleme: {symbol} ===")
    lines.append(f"Profil: {profile_name}")
    lines.append(f"Zaman Dilimi: {timeframe}")
    lines.append(f"Kullanılan Feature Setleri: {summary.get('feature_sets')}")
    lines.append(f"Eksik Feature Setleri: {summary.get('missing_feature_sets')}")
    lines.append(f"Satır Sayısı: {summary.get('rows')}")
    lines.append(f"Kolon Sayısı: {summary.get('columns')}")
    lines.append(f"Son Rejim: {summary.get('latest_regime')} (Güven: {summary.get('latest_confidence', 0.0):.2f})")
    lines.append("")

    qr = summary.get("quality_report", {})
    lines.append("--- Kalite Raporu ---")
    lines.append(f"Testleri Geçti mi: {qr.get('passed', False)}")
    lines.append(f"Ortalama Güven: {qr.get('average_confidence', 0.0):.2f}")
    lines.append(f"Düşük Güven Oranı: {qr.get('low_confidence_ratio', 0.0):.2%}")
    lines.append(f"Stabilite Skoru: {qr.get('stability_score', 0.0):.2f}")

    warnings = summary.get("warnings", [])
    if warnings:
        lines.append("\nUyarılar:")
        for w in warnings:
            lines.append(f"  - {w}")

    lines.append("\nUyarı: Rejimler piyasa bağlamını ifade eder, nihai AL/SAT işlemi (trade signal) değildir.")

    lines.append("\nSon Satırlar:")
    lines.append(tail_df.to_string())

    return "\n".join(lines)


def build_regime_event_preview_report(
    symbol: str, timeframe: str, profile_name: str, summary: dict, event_tail_df: pd.DataFrame
) -> str:
    lines = []
    lines.append(f"=== Rejim Event Önizleme: {symbol} ===")
    lines.append(f"Profil: {profile_name}")
    lines.append(f"Zaman Dilimi: {timeframe}")
    lines.append(f"Toplam Olay Sayısı: {summary.get('total_event_count', 0)}")
    lines.append("")

    lines.append("En Sık Oluşan Olaylar:")
    counts = summary.get("event_count_by_column", {})
    for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)[:5]:
        lines.append(f"  - {k}: {v}")

    lines.append("")
    lines.append(f"Aktif Son Satır Olayları: {summary.get('active_last_row_events', [])}")

    lines.append("\nUyarılar:")
    for w in summary.get("warnings", []):
        lines.append(f"  - {w}")

    lines.append(f"\nNot: {summary.get('notes', '')}")
    lines.append("Bu eventler nihai al/sat sinyali değildir.")

    lines.append("\nSon Satırlar (Olaylar):")
    lines.append(event_tail_df.to_string())

    return "\n".join(lines)


def build_regime_batch_report(summary: dict) -> str:
    lines = []
    lines.append("=== Rejim Toplu İşlem Raporu ===")

    success_count = 0
    error_count = 0
    skipped_count = 0

    for sym, tfs in summary.items():
        if isinstance(tfs, dict):
            for tf, res in tfs.items():
                status = res.get("status")
                if status == "success":
                    success_count += 1
                elif status == "error":
                    error_count += 1
                elif status == "skipped":
                    skipped_count += 1

    lines.append(f"Toplam Başarılı: {success_count}")
    lines.append(f"Toplam Hatalı: {error_count}")
    lines.append(f"Toplam Atlanan: {skipped_count}")
    lines.append("")

    lines.append("Detaylar:")
    for sym, tfs in summary.items():
        if isinstance(tfs, dict):
            for tf, res in tfs.items():
                status = res.get("status")
                if status == "success":
                    lines.append(f"{sym} {tf}: Başarılı - Son Rejim: {res.get('latest_regime')} ({res.get('latest_confidence', 0):.2f})")
                else:
                    lines.append(f"{sym} {tf}: {status} - Hata: {res.get('error')} Uyarı: {res.get('warnings')}")

    return "\n".join(lines)


def build_regime_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = []
    lines.append("=== Rejim Durum Raporu ===")
    lines.append(f"Toplam Sembol: {len(status_df)}")
    if not status_df.empty:
        lines.append(f"Rejim Feature Olanlar: {status_df['has_regime'].sum()}")
        lines.append(f"Rejim Event Olanlar: {status_df['has_regime_events'].sum()}")

        # Missing regimes (has basic features but no regimes)
        missing = status_df[status_df["has_technical"] & ~status_df["has_regime"]]
        lines.append(f"\nRejimi Eksik Olanlar (Teknik feature var ama rejim yok): {len(missing)}")
        for _, row in missing.iterrows():
            lines.append(f" - {row['symbol']} {row['timeframe']}")

    return "\n".join(lines)
"""

if "build_regime_feature_preview_report" not in content:
    content += "\n" + new_functions

with open(file_path, "w") as f:
    f.write(content)
