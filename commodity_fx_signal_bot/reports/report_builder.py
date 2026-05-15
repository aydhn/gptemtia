"""
Report generation utilities.
"""

from pathlib import Path
from typing import List

import pandas as pd

from config.symbols import SymbolSpec
from data.universe_analyzer import SymbolReliabilityResult, UniverseAnalyzer


def build_universe_report(symbols: List[SymbolSpec]) -> str:
    """
    Build a text summary report of the symbol universe.
    """
    total = len(symbols)
    enabled = sum(1 for s in symbols if s.enabled)
    analysis = sum(1 for s in symbols if s.enabled and s.analysis_enabled)
    paper_trade = sum(1 for s in symbols if s.enabled and s.paper_trade_enabled)

    # Count by asset class
    classes = {}
    data_sources = {}
    for s in symbols:
        if s.enabled:
            classes[s.asset_class] = classes.get(s.asset_class, 0) + 1
            data_sources[s.data_source] = data_sources.get(s.data_source, 0) + 1

    lines = [
        "=== Symbol Universe Summary ===",
        f"Total Symbols: {total}",
        f"Enabled Symbols: {enabled}",
        f"Analysis Enabled: {analysis}",
        f"Paper Trade Enabled: {paper_trade}",
        "",
        "Breakdown by Asset Class:",
    ]
    for ac, count in sorted(classes.items()):
        lines.append(f"  - {ac}: {count}")

    lines.append("")
    lines.append("Breakdown by Data Source:")
    for ds, count in sorted(data_sources.items()):
        lines.append(f"  - {ds}: {count}")

    lines.append("=============================")
    return "\n".join(lines)


def build_reliability_report(results: List[SymbolReliabilityResult]) -> str:
    """
    Build a text report summarizing the reliability scan results.
    """
    summary = UniverseAnalyzer.summarize_results(results)
    if not summary:
        return "No reliability results available."

    lines = [
        "=== Symbol Reliability Report ===",
        f"Total Analyzed: {summary['total_analyzed']}",
        f"Success: {summary['success_count']}",
        f"Failed: {summary['fail_count']}",
        f"Average Score: {summary['avg_score']:.2f}",
        "",
        "Grade Distribution:",
    ]
    for grade, count in sorted(summary["grade_distribution"].items()):
        lines.append(f"  - {grade}: {count}")

    lines.append("")
    lines.append("Asset Class Success Rate:")
    for ac, rate in sorted(summary["asset_class_success_rate"].items()):
        lines.append(f"  - {ac}: {rate*100:.1f}%")

    lines.append("")
    lines.append("Top 10 Most Reliable:")
    for b in summary["best_10"]:
        lines.append(
            f"  - {b['symbol']}: {b['reliability_score']:.1f} ({b['reliability_grade']})"
        )

    lines.append("")
    lines.append("Bottom 10 Least Reliable:")
    for w in summary["worst_10"]:
        err_msg = f" - {w['error'][:50]}..." if w["error"] else ""
        lines.append(
            f"  - {w['symbol']}: {w['reliability_score']:.1f} ({w['reliability_grade']}){err_msg}"
        )

    lines.append("")
    lines.append(f"Alias Used: {len(summary['used_alias_symbols'])}")
    if summary["used_alias_symbols"]:
        lines.append(f"  Symbols: {', '.join(summary['used_alias_symbols'])}")

    lines.append("")
    lines.append(f"Errors Found: {len(summary['error_symbols'])}")
    for e in summary["error_symbols"][:10]:  # print first 10
        lines.append(f"  - {e['symbol']}: {e['error'][:80]}...")
    if len(summary["error_symbols"]) > 10:
        lines.append(f"  ... and {len(summary['error_symbols']) - 10} more")

    lines.append("=================================")
    return "\n".join(lines)


def build_asset_class_summary(results: List[SymbolReliabilityResult]) -> str:
    """
    Build a brief summary of results by asset class.
    """
    summary = UniverseAnalyzer.summarize_results(results)
    if not summary:
        return "No data"

    lines = ["Asset Class Success Rates:"]
    for ac, rate in sorted(summary["asset_class_success_rate"].items()):
        lines.append(f"{ac}: {rate*100:.1f}%")
    return "\n".join(lines)


def save_text_report(text: str, path: Path) -> None:
    """Save text report to file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(text)


def save_dataframe_report(df: pd.DataFrame, path: Path) -> None:
    """Save dataframe to CSV."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def build_timeframe_compatibility_report(
    symbols: List[SymbolSpec], scan_plan: dict
) -> str:
    pass

    lines = [
        "=== Timeframe Compatibility Audit ===",
        f"Total Symbols: {scan_plan['total_symbols']}",
        "",
        "Asset Class Breakdowns (Eligible Symbols):",
    ]
    for ac, count in scan_plan.get("by_asset_class", {}).items():
        lines.append(f"  - {ac}: {count}")

    lines.append("")
    lines.append("Excluded Timeframes (Found in Symbols):")
    for s in symbols:
        if s.excluded_timeframes:
            lines.append(f"  - {s.symbol}: {s.excluded_timeframes}")

    lines.append("")
    lines.append("Preferred Timeframes (Found in Symbols):")
    for s in symbols:
        if s.preferred_timeframes:
            lines.append(f"  - {s.symbol}: {s.preferred_timeframes}")

    lines.append("")
    lines.append("Scan Plan Info:")
    lines.append(f"  - Profile: {scan_plan['profile']}")
    lines.append(f"  - Eligible Symbols: {len(scan_plan['eligible_symbols'])}")
    lines.append(f"  - Skipped Symbols: {len(scan_plan['skipped_symbols'])}")

    return "\n".join(lines)


def build_scan_plan_report(scan_plan: dict) -> str:
    lines = [
        "=== Scan Plan ===",
        f"Profile: {scan_plan['profile']}",
        f"Time: {scan_plan['now']}",
        f"Interval: {scan_plan['scan_interval_minutes']}m",
        f"Eligible: {len(scan_plan['eligible_symbols'])}",
        f"Skipped: {len(scan_plan['skipped_symbols'])}",
        "=================",
    ]
    return "\n".join(lines)


def build_data_lake_update_report(summary: dict) -> str:
    """Build a text report for Data Lake update results."""
    lines = [
        "=== Veri Gölü Güncelleme Raporu ===",
        f"Toplam Deneme: {summary.get('total_attempts', 0)}",
        f"Başarılı İndirme: {summary.get('success_count', 0)}",
        f"Başarısız İndirme: {summary.get('failure_count', 0)}",
        f"Atlanan Sembol: {summary.get('skipped_count', 0)}",
        "",
        "Varlık Sınıfına Göre Başarılar:",
    ]

    for ac, count in sorted(summary.get("by_asset_class", {}).items()):
        lines.append(f"  - {ac}: {count}")

    lines.append("")
    lines.append("Zaman Dilimine Göre Başarılar:")
    for tf, count in sorted(summary.get("by_timeframe", {}).items()):
        lines.append(f"  - {tf}: {count}")

    errors = summary.get("errors", [])
    if errors:
        lines.append("")
        lines.append(f"Alınan Hatalar ({len(errors)}):")
        for err in errors[:10]:
            lines.append(f"  - {err}")
        if len(errors) > 10:
            lines.append(f"  ... ve {len(errors) - 10} hata daha.")

    lines.append("===================================")
    return "\n".join(lines)


def build_data_lake_status_report(
    manifest_summary: dict, manifest_df: pd.DataFrame
) -> str:
    """Build a text report for Data Lake status."""
    lines = [
        "=== Veri Gölü Durum Raporu ===",
        f"Beklenen Dosya Sayısı: {manifest_summary.get('total_expected', 0)}",
        f"Mevcut Dosya Sayısı: {manifest_summary.get('total_existing', 0)}",
        f"Eksik Dosya Sayısı: {manifest_summary.get('missing', 0)}",
        f"Tamamlanma Oranı: %{manifest_summary.get('completion_rate', 0) * 100:.1f}",
        "",
        "Kalite Notu Dağılımı (Mevcut Dosyalar):",
    ]

    for grade, count in sorted(manifest_summary.get("grades", {}).items()):
        lines.append(f"  - {grade}: {count}")

    lines.append("")
    lines.append("Zaman Dilimi Durumu (Mevcut / Beklenen):")
    for tf, stats in sorted(manifest_summary.get("by_timeframe", {}).items()):
        lines.append(f"  - {tf}: {stats['existing']} / {stats['expected']}")

    # Find weakest links (Grade D or F)
    weak_df = manifest_df[manifest_df["quality_grade"].isin(["D", "F"])]
    if not weak_df.empty:
        lines.append("")
        lines.append(f"Zayıf Kaliteli Dosyalar ({len(weak_df)}):")
        for _, row in weak_df.head(10).iterrows():
            lines.append(
                f"  - {row['symbol']} ({row['timeframe']}): {row['quality_grade']}"
            )
        if len(weak_df) > 10:
            lines.append(f"  ... ve {len(weak_df) - 10} dosya daha.")

    lines.append("==============================")
    return "\n".join(lines)


def build_download_journal_report(journal_summary: dict) -> str:
    """Build a text report from the download journal summary."""
    lines = [
        "=== Veri İndirme Günlüğü Özeti ===",
        f"Toplam Kayıt: {journal_summary.get('total_entries', 0)}",
        f"Başarılı İndirme: {journal_summary.get('success_count', 0)}",
        f"Başarısız İndirme: {journal_summary.get('failure_count', 0)}",
        f"Başarı Oranı: %{journal_summary.get('success_rate', 0) * 100:.1f}",
        f"Önbellek (Cache) Kullanımı: {journal_summary.get('cache_hits', 0)}",
        f"Alias Kullanımı: {journal_summary.get('alias_used', 0)}",
    ]

    recent_errors = journal_summary.get("recent_errors", [])
    if recent_errors:
        lines.append("")
        lines.append("Son Hatalar:")
        for err in recent_errors:
            lines.append(f"  - {err}")

    lines.append("==================================")
    return "\n".join(lines)


def build_data_quality_audit_report(audit_df: pd.DataFrame, summary: dict) -> str:
    """Build a human-readable text report for data quality audit."""
    if audit_df.empty:
        return "No data available for audit."

    lines = []
    lines.append("DATA QUALITY AUDIT REPORT")
    lines.append("=" * 50)
    lines.append("")

    lines.append("1. GENEL ÖZET")
    lines.append("-" * 30)
    lines.append(f"Toplam Taranan Dosya: {summary.get('total_files', 0)}")
    lines.append(f"Ortalama Kalite Skoru: {summary.get('avg_score', 0):.1f}/100")
    lines.append(f"Toplam Kritik Hata: {summary.get('total_errors', 0)}")
    lines.append("")

    lines.append("2. KALİTE NOTU DAĞILIMI (Grade Distribution)")
    lines.append("-" * 30)
    grades = summary.get("grades", {})
    for grade, count in sorted(grades.items()):
        lines.append(f"Grade {grade}: {count} dosya")
    lines.append("")

    lines.append("3. EN PROBLEMLİ DOSYALAR (D & F Grades)")
    lines.append("-" * 30)
    problematic = audit_df[audit_df["Grade"].isin(["D", "F"])].sort_values(by="Score")
    if problematic.empty:
        lines.append("Harika! D veya F notu alan sorunlu dosya bulunamadı.")
    else:
        for idx, row in problematic.head(20).iterrows():
            lines.append(
                f"{row['Symbol']} ({row['Timeframe']}): Grade {row['Grade']} (Score: {row['Score']:.1f}) - Hatalar: {row['Errors']}, Boşluk: {row['Gaps']}, Duplicate: {row['Duplicates']}"
            )
    lines.append("")

    lines.append("4. EN ÇOK BOŞLUK (GAP) İÇERENLER")
    lines.append("-" * 30)
    gappy = audit_df[audit_df["Gaps"] > 0].sort_values(by="Gaps", ascending=False)
    if gappy.empty:
        lines.append("Önemli bir boşluk (gap) bulunamadı.")
    else:
        for idx, row in gappy.head(10).iterrows():
            lines.append(f"{row['Symbol']} ({row['Timeframe']}): {row['Gaps']} Gap")

    return "\n".join(lines)


def build_data_cleaning_report(summary_df: pd.DataFrame, summary: dict) -> str:
    """Build a human-readable text report for data cleaning process."""
    if summary_df.empty:
        return "No data was cleaned."

    lines = []
    lines.append("VERİ TEMİZLİK (CLEANING) RAPORU")
    lines.append("=" * 50)
    lines.append("")

    lines.append("1. TEMİZLİK ÖZETİ")
    lines.append("-" * 30)
    lines.append(f"Toplam Temizlenen: {summary.get('total_cleaned', 0)}")
    lines.append(f"Kalitesi Artan: {summary.get('improved', 0)}")
    lines.append(f"Kalitesi Düşen (veya Veri Kaybeden): {summary.get('degraded', 0)}")
    lines.append(f"Ortalama Skor Artışı: +{summary.get('avg_improvement', 0):.2f}")
    lines.append(f"Silinen Duplicate Satır: {summary.get('total_dupes_removed', 0)}")
    lines.append("")

    lines.append("2. EN ÇOK İYİLEŞENLER")
    lines.append("-" * 30)
    improved_df = summary_df[summary_df["Score Change"] > 0].sort_values(
        by="Score Change", ascending=False
    )
    if improved_df.empty:
        lines.append("Skorunda artış olan dosya yok.")
    else:
        for idx, row in improved_df.head(15).iterrows():
            lines.append(
                f"{row['Symbol']} ({row['Timeframe']}): {row['Grade Before']} -> {row['Grade After']} (+{row['Score Change']:.1f})"
            )
    lines.append("")

    return "\n".join(lines)


def build_processed_data_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    """Build a human-readable report for processed data lake status."""
    if status_df.empty:
        return "No data found."

    lines = []
    lines.append("PROCESSED DATA LAKE STATUS")
    lines.append("=" * 50)
    lines.append("")

    lines.append("1. DURUM ÖZETİ")
    lines.append("-" * 30)
    lines.append(
        f"Toplam Kombinasyon (Symbol+TF): {summary.get('total_combinations', 0)}"
    )
    lines.append(f"İşlenmiş (Processed) Hazır: {summary.get('fully_processed', 0)}")
    lines.append(
        f"İşlenmeyi Bekleyen (Ham var, Processed Yok): {summary.get('missing_processed', 0)}"
    )
    lines.append("")

    lines.append("2. PROCESSED KALİTE DAĞILIMI")
    lines.append("-" * 30)
    grades = summary.get("processed_grades", {})
    for grade, count in sorted(grades.items()):
        lines.append(f"Grade {grade}: {count} dosya")
    lines.append("")

    missing_df = status_df[
        (status_df["Has Raw"] == True) & (status_df["Has Processed"] == False)
    ]
    if not missing_df.empty:
        lines.append("3. TEMİZLENMEYİ BEKLEYENLER")
        lines.append("-" * 30)
        for idx, row in missing_df.head(20).iterrows():
            lines.append(
                f"{row['Symbol']} ({row['Timeframe']}): Raw Rows: {row['Raw Rows']}"
            )

    return "\n".join(lines)


def build_momentum_feature_preview_report(
    symbol: str, timeframe: str, summary: dict, tail_df: pd.DataFrame
) -> str:
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
    for col in summary.get("feature_columns", []):
        lines.append(f"  - {col}")

    lines.append("")
    lines.append("Son Satırlar (Örnek):")
    lines.append(tail_df.to_string())
    lines.append("================================")

    return "\n".join(lines)


def build_momentum_event_preview_report(
    symbol: str, timeframe: str, summary: dict, event_tail_df: pd.DataFrame
) -> str:
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

    return "\n".join(lines)


def build_momentum_batch_report(summary: dict) -> str:
    lines = [
        "=== MOMENTUM BATCH BUILD RAPORU ===",
        f"Toplam Deneme: {summary.get('total_attempts', 0)}",
        f"Başarılı: {summary.get('success_count', 0)}",
        f"Atlanan: {summary.get('skipped_count', 0)}",
        f"Başarısız: {summary.get('failure_count', 0)}",
        "====================================",
    ]
    return "\n".join(lines)


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
    return "\n".join(lines)


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

    return "\n".join(lines)


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

    return "\n".join(lines)


def build_trend_batch_report(summary: dict) -> str:
    lines = [
        "=== TREND BATCH BUILD RAPORU ===",
        f"Toplam Deneme: {summary.get('total_attempts', 0)}",
        f"Başarılı: {summary.get('success_count', 0)}",
        f"Atlanan: {summary.get('skipped_count', 0)}",
        f"Başarısız: {summary.get('failure_count', 0)}",
        "====================================",
    ]
    return "\n".join(lines)


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
    return "\n".join(lines)


def build_volatility_feature_preview_report(
    symbol: str, timeframe: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = []
    lines.append(f"=== VOLATILITY FEATURE PREVIEW: {symbol} ({timeframe}) ===")
    lines.append(f"Feature Type: {summary.get('type', 'compact')}")
    lines.append(f"Input Rows: {summary.get('input_rows', 0)}")
    lines.append(f"Output Rows: {summary.get('output_rows', 0)}")
    lines.append(f"Feature Count: {summary.get('feature_count', 0)}")
    lines.append(f"Event Count: {summary.get('event_count', 0)}")
    lines.append(f"Total NaN Ratio: {summary.get('total_nan_ratio', 0.0):.4f}")

    if summary.get("failed_components"):
        lines.append(f"Failed Components: {', '.join(summary['failed_components'])}")

    lines.append("\n=== TAIL DATA ===")
    lines.append(tail_df.to_string())

    if summary.get("warnings"):
        lines.append("\n=== WARNINGS ===")
        for w in summary["warnings"]:
            lines.append(f"- {w}")

    return "\n".join(lines)


def build_volatility_event_preview_report(
    symbol: str, timeframe: str, summary: dict, event_tail_df: pd.DataFrame
) -> str:
    lines = []
    lines.append(f"=== VOLATILITY EVENT PREVIEW: {symbol} ({timeframe}) ===")
    lines.append(f"Input Rows: {summary.get('input_rows', 0)}")
    lines.append(f"Total Event Columns: {len(summary.get('event_columns', []))}")
    lines.append(f"Total Events Triggered: {summary.get('total_event_count', 0)}")

    lines.append("\n=== TOP EVENTS (By Frequency) ===")
    counts = summary.get("event_count_by_column", {})
    sorted_events = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    for k, v in sorted_events[:10]:
        lines.append(f"{k}: {v}")

    lines.append("\n=== ACTIVE EVENTS IN LAST ROW ===")
    active_last = summary.get("active_last_row_events", [])
    if active_last:
        for event in active_last:
            lines.append(f"- {event}")
    else:
        lines.append("- None")

    lines.append("\n=== TAIL DATA (Events) ===")
    if not event_tail_df.empty:
        # Show only rows where at least one event is 1 to save space, or just tail
        lines.append(event_tail_df.to_string())
    else:
        lines.append("No event data.")

    lines.append("\n=== NOTES ===")
    lines.append(
        summary.get(
            "notes", "These events are candidates, not direct buy/sell signals."
        )
    )

    return "\n".join(lines)


def build_volatility_batch_report(summary: dict) -> str:
    lines = []
    lines.append("=== VOLATILITY BATCH BUILD SUMMARY ===")
    lines.append(f"Total Attempts: {summary.get('total_attempts', 0)}")
    lines.append(f"Success: {summary.get('success_count', 0)}")
    lines.append(f"Failed: {summary.get('fail_count', 0)}")
    lines.append(f"Skipped: {summary.get('skipped_count', 0)}")

    if summary.get("fail_count", 0) > 0:
        lines.append("\n=== FAILURES ===")
        for d in summary.get("details", []):
            if not d.get("success") and not d.get("skipped"):
                lines.append(
                    f"{d.get('symbol')} ({d.get('timeframe')}): {d.get('error')}"
                )

    return "\n".join(lines)


def build_volatility_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = []
    lines.append("=== VOLATILITY STATUS REPORT ===")
    lines.append(f"Total Symbols: {summary.get('total_symbols', 0)}")
    lines.append(
        f"With Volatility Features: {summary.get('with_volatility_features', 0)}"
    )
    lines.append(f"With Volatility Events: {summary.get('with_volatility_events', 0)}")
    lines.append(
        f"Missing (have processed): {summary.get('missing_but_have_processed', 0)}"
    )
    lines.append(
        f"Missing (have technical): {summary.get('missing_but_have_technical', 0)}"
    )

    if not status_df.empty:
        missing = status_df[
            (~status_df["has_volatility_features"])
            & (status_df["has_processed"] | status_df["has_technical"])
        ]
        if not missing.empty:
            lines.append("\n=== MISSING VOLATILITY FEATURES (Sample) ===")
            lines.append(
                missing[["symbol", "timeframe", "has_processed", "has_technical"]]
                .head(20)
                .to_string()
            )

    return "\n".join(lines)


def build_volume_feature_preview_report(
    symbol: str, timeframe: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = []
    lines.append(f"=== VOLUME FEATURE PREVIEW: {symbol} ({timeframe}) ===")
    lines.append(f"Input Rows: {summary.get('input_rows', 0)}")
    lines.append(f"Output Rows: {summary.get('output_rows', 0)}")
    lines.append(f"Volume Usable: {summary.get('volume_usable', False)}")
    lines.append(f"Volume Valid Ratio: {summary.get('volume_valid_ratio', 0.0):.2f}")

    if summary.get("warnings"):
        lines.append("\nWARNINGS:")
        for w in summary.get("warnings"):
            lines.append(f"- {w}")

    lines.append("\nFEATURE COLUMNS:")
    for col in summary.get("feature_columns", []):
        lines.append(f"- {col}")

    lines.append("\nEVENT COLUMNS:")
    for col in summary.get("event_columns", []):
        lines.append(f"- {col}")

    lines.append("\nLATEST DATA:")
    lines.append(tail_df.to_string())
    return "\n".join(lines)


def build_volume_event_preview_report(
    symbol: str, timeframe: str, summary: dict, event_tail_df: pd.DataFrame
) -> str:
    lines = []
    lines.append(f"=== VOLUME EVENT PREVIEW: {symbol} ({timeframe}) ===")
    lines.append("NOTE: These events are candidates, not final trade signals.")
    lines.append(f"Volume Usable: {summary.get('volume_usable', False)}")
    lines.append(f"Volume Valid Ratio: {summary.get('volume_valid_ratio', 0.0):.2f}")

    if summary.get("warnings"):
        lines.append("\nWARNINGS:")
        for w in summary.get("warnings"):
            lines.append(f"- {w}")

    lines.append(f"\nTotal Events Found: {summary.get('total_event_count', 0)}")

    lines.append("\nEVENT FREQUENCIES:")
    for col, count in summary.get("event_count_by_column", {}).items():
        if count > 0:
            lines.append(f"- {col}: {count}")

    lines.append("\nACTIVE EVENTS ON LAST ROW:")
    active = summary.get("active_last_row_events", [])
    if active:
        for a in active:
            lines.append(f"- {a}")
    else:
        lines.append("- None")

    lines.append("\nLATEST EVENT DATA:")
    lines.append(event_tail_df.to_string())
    return "\n".join(lines)


def build_volume_batch_report(summary: dict) -> str:
    lines = []
    lines.append("=== VOLUME BATCH BUILD REPORT ===")
    lines.append(f"Total Targets: {summary.get('total_targets', 0)}")
    lines.append(f"Success: {summary.get('success_count', 0)}")
    lines.append(f"Skipped: {summary.get('skipped_count', 0)}")
    lines.append(f"Failed: {summary.get('failed_count', 0)}")

    if summary.get("failed_count", 0) > 0:
        lines.append("\nFAILURES:")
        for d in summary.get("details", []):
            if not d.get("success") and not d.get("skipped"):
                lines.append(
                    f"{d.get('symbol')} ({d.get('timeframe')}): {d.get('error')}"
                )

    return "\n".join(lines)


def build_volume_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = []
    lines.append("=== VOLUME STATUS REPORT ===")
    lines.append(f"Total Symbols: {summary.get('total_symbols', 0)}")
    lines.append(f"With Volume Features: {summary.get('with_volume', 0)}")
    lines.append(f"With Volume Events: {summary.get('with_volume_events', 0)}")
    lines.append(
        f"Missing (have processed): {summary.get('missing_but_have_processed', 0)}"
    )
    lines.append(
        f"Missing (have technical): {summary.get('missing_but_have_technical', 0)}"
    )

    if not status_df.empty:
        missing = status_df[
            (~status_df["has_volume"])
            & (status_df["has_processed"] | status_df["has_technical"])
        ]
        if not missing.empty:
            lines.append("\n=== MISSING VOLUME FEATURES (Sample) ===")
            lines.append(
                missing[["symbol", "timeframe", "has_processed", "has_technical"]]
                .head(20)
                .to_string()
            )

    return "\n".join(lines)


def build_mean_reversion_feature_preview_report(
    symbol: str, timeframe: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = []
    lines.append(f"=== MEAN REVERSION FEATURE PREVIEW: {symbol} ({timeframe}) ===")
    lines.append(f"Feature Type: {summary.get('type', 'compact')}")
    lines.append(f"Input Rows: {summary.get('input_rows', 0)}")
    lines.append(f"Output Rows: {summary.get('output_rows', 0)}")
    lines.append(f"Feature Count: {summary.get('feature_count', 0)}")
    lines.append(f"Event Count: {summary.get('event_count', 0)}")
    lines.append(f"Total NaN Ratio: {summary.get('total_nan_ratio', 0.0):.4f}")

    if summary.get("failed_components"):
        lines.append(f"Failed Components: {', '.join(summary['failed_components'])}")

    lines.append("\n=== TAIL DATA ===")
    lines.append(tail_df.to_string())

    if summary.get("warnings"):
        lines.append("\n=== WARNINGS ===")
        for w in summary["warnings"]:
            lines.append(f"- {w}")

    return "\n".join(lines)


def build_mean_reversion_event_preview_report(
    symbol: str, timeframe: str, summary: dict, event_tail_df: pd.DataFrame
) -> str:
    lines = []
    lines.append(f"=== MEAN REVERSION EVENT PREVIEW: {symbol} ({timeframe}) ===")
    lines.append(f"Input Rows: {summary.get('input_rows', 0)}")
    lines.append(f"Total Event Columns: {len(summary.get('event_columns', []))}")
    lines.append(f"Total Events Triggered: {summary.get('total_event_count', 0)}")

    lines.append("\n=== TOP EVENTS (By Frequency) ===")
    counts = summary.get("event_count_by_column", {})
    sorted_events = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    for k, v in sorted_events[:10]:
        lines.append(f"{k}: {v}")

    lines.append("\n=== ACTIVE EVENTS IN LAST ROW ===")
    active_last = summary.get("active_last_row_events", [])
    if active_last:
        for event in active_last:
            lines.append(f"- {event}")
    else:
        lines.append("- None")

    lines.append("\n=== TAIL DATA (Events) ===")
    if not event_tail_df.empty:
        lines.append(event_tail_df.to_string())
    else:
        lines.append("No event data.")

    lines.append("\n=== NOTES ===")
    lines.append(
        summary.get(
            "notes", "These events are candidates, not direct buy/sell signals."
        )
    )

    return "\n".join(lines)


def build_mean_reversion_batch_report(summary: dict) -> str:
    lines = []
    lines.append("=== MEAN REVERSION BATCH BUILD SUMMARY ===")
    lines.append(f"Total Attempts: {summary.get('total_attempts', 0)}")
    lines.append(f"Success: {summary.get('success_count', 0)}")
    lines.append(f"Failed: {summary.get('fail_count', 0)}")
    lines.append(f"Skipped: {summary.get('skipped_count', 0)}")

    if summary.get("fail_count", 0) > 0:
        lines.append("\n=== FAILURES ===")
        for d in summary.get("details", []):
            if not d.get("success") and not d.get("skipped"):
                lines.append(
                    f"{d.get('symbol')} ({d.get('timeframe')}): {d.get('error')}"
                )

    return "\n".join(lines)


def build_mean_reversion_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = []
    lines.append("=== MEAN REVERSION STATUS REPORT ===")
    lines.append(f"Total Symbols: {summary.get('total_symbols', 0)}")
    lines.append(
        f"With Mean Reversion Features: {summary.get('with_mean_reversion_features', 0)}"
    )
    lines.append(
        f"With Mean Reversion Events: {summary.get('with_mean_reversion_events', 0)}"
    )
    lines.append(
        f"Missing (have processed): {summary.get('missing_but_have_processed', 0)}"
    )
    lines.append(
        f"Missing (have technical): {summary.get('missing_but_have_technical', 0)}"
    )

    if not status_df.empty:
        missing = status_df[
            (~status_df["has_mean_reversion_features"])
            & (status_df["has_processed"] | status_df["has_technical"])
        ]
        if not missing.empty:
            lines.append("\n=== MISSING MEAN REVERSION FEATURES (Sample) ===")
            lines.append(
                missing[["symbol", "timeframe", "has_processed", "has_technical"]]
                .head(20)
                .to_string()
            )

    return "\n".join(lines)


def build_price_action_feature_preview_report(
    symbol: str, timeframe: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = [
        f"=== PRICE ACTION FEATURE PREVIEW ===",
        f"Symbol: {symbol}",
        f"Timeframe: {timeframe}",
        f"Input Rows: {summary.get('input_rows', 0)}",
        f"Output Rows: {summary.get('output_rows', 0)}",
        f"Feature Count: {summary.get('feature_count', 0)}",
        f"Event Count: {summary.get('event_count', 0)}",
        f"Total NaN Ratio: {summary.get('total_nan_ratio', 0.0):.4f}",
        "",
    ]

    if summary.get("warnings"):
        lines.append("Warnings:")
        for w in summary["warnings"]:
            lines.append(f" - {w}")
        lines.append("")

    if summary.get("failed_components"):
        lines.append("Failed Components:")
        for f in summary["failed_components"]:
            lines.append(f" - {f}")
        lines.append("")

    lines.append("Feature Columns:")
    for c in summary.get("feature_columns", []):
        lines.append(f" - {c}")
    lines.append("")

    lines.append(f"--- Last {len(tail_df)} Rows ---")
    lines.append(tail_df.to_string())

    return "\n".join(lines)


def build_price_action_event_preview_report(
    symbol: str, timeframe: str, summary: dict, event_tail_df: pd.DataFrame
) -> str:
    lines = [
        f"=== PRICE ACTION EVENT PREVIEW ===",
        f"Symbol: {symbol}",
        f"Timeframe: {timeframe}",
        f"Total Events Generated: {summary.get('total_event_count', 0)}",
        "",
    ]

    lines.append("WARNING: These events are candidates and NOT final buy/sell signals.")
    lines.append("")

    lines.append("Event Counts by Column:")
    counts = summary.get("event_count_by_column", {})
    # sort by count desc
    for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        lines.append(f" - {k}: {v}")
    lines.append("")

    lines.append("Active Events in Last Row:")
    for e in summary.get("active_last_row_events", []):
        lines.append(f" - {e}")
    lines.append("")

    # Show last rows where an event occurred
    active_rows = event_tail_df[(event_tail_df > 0).any(axis=1)]
    lines.append(f"--- Active Events in Last {len(event_tail_df)} Rows ---")
    if active_rows.empty:
        lines.append("No active events found.")
    else:
        for idx, row in active_rows.iterrows():
            active = row[row > 0].index.tolist()
            lines.append(f"{idx}: {active}")

    return "\n".join(lines)


def build_price_action_batch_report(summary: dict) -> str:
    lines = ["=== PRICE ACTION BATCH SUMMARY ===", ""]

    success_count = 0
    error_count = 0
    empty_count = 0

    for sym, tfs in summary.items():
        if isinstance(tfs, dict):
            for tf, res in tfs.items():
                status = res.get("status")
                if status == "success":
                    success_count += 1
                elif status == "error":
                    error_count += 1
                elif status == "empty":
                    empty_count += 1

    lines.append(f"Total Success: {success_count}")
    lines.append(f"Total Errors: {error_count}")
    lines.append(f"Total Empty: {empty_count}")
    lines.append("")

    lines.append("Details:")
    for sym, tfs in summary.items():
        if isinstance(tfs, dict):
            for tf, res in tfs.items():
                lines.append(
                    f"{sym} {tf}: {res.get('status')} - Rows: {res.get('rows', 0)} Features: {res.get('features', 0)} Events: {res.get('events', 0)}"
                )
                if res.get("warnings"):
                    lines.append(f"  Warnings: {', '.join(res['warnings'])}")
                if res.get("error"):
                    lines.append(f"  Error: {res['error']}")

    return "\n".join(lines)


def build_price_action_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = [
        "=== PRICE ACTION STATUS REPORT ===",
        f"Total Tradeable Symbols: {summary.get('total_symbols', 0)}",
        f"Symbols with Price Action: {summary.get('with_price_action', 0)}",
        f"Timeframes missing PA (but have technical): {summary.get('missing_but_has_technical', 0)}",
        "",
    ]

    lines.append("Timeframes Missing PA (but have Technical):")
    missing = status_df[status_df["has_technical"] & ~status_df["has_price_action"]]
    for _, row in missing.iterrows():
        lines.append(f" - {row['symbol']} {row['timeframe']}")
    lines.append("")

    return "\n".join(lines)


def build_divergence_feature_preview_report(
    symbol: str, timeframe: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = [
        f"=== DIVERGENCE FEATURE PREVIEW ===",
        f"Symbol: {symbol}",
        f"Timeframe: {timeframe}",
        f"Input Rows: {summary.get('input_rows', 0)}",
        f"Output Rows: {summary.get('output_rows', 0)}",
        f"Feature Count: {summary.get('feature_count', 0)}",
        f"Event Count: {summary.get('event_count', 0)}",
        f"Total NaN Ratio: {summary.get('total_nan_ratio', 0.0):.4f}",
        "",
    ]

    if summary.get("missing_indicator_columns"):
        lines.append("Missing Indicator Columns:")
        for w in summary["missing_indicator_columns"]:
            lines.append(f" - {w}")
        lines.append("")

    if summary.get("warnings"):
        lines.append("Warnings & Notes:")
        for w in summary["warnings"]:
            lines.append(f" - {w}")
        lines.append("")

    if summary.get("failed_components"):
        lines.append("Failed Components:")
        for f in summary["failed_components"]:
            lines.append(f" - {f}")
        lines.append("")

    lines.append("Feature Columns:")
    for c in summary.get("feature_columns", []):
        lines.append(f" - {c}")
    lines.append("")

    lines.append(f"--- Last {len(tail_df)} Rows ---")
    lines.append(tail_df.to_string())

    return "\n".join(lines)


def build_divergence_event_preview_report(
    symbol: str, timeframe: str, summary: dict, event_tail_df: pd.DataFrame
) -> str:
    lines = [
        f"=== DIVERGENCE EVENT PREVIEW ===",
        f"Symbol: {symbol}",
        f"Timeframe: {timeframe}",
        f"Total Events Generated: {summary.get('total_event_count', 0)}",
        "",
    ]

    for note in summary.get("notes", []):
        lines.append(f"WARNING/NOTE: {note}")
    lines.append("These events are candidates and NOT final buy/sell signals.")
    lines.append("")

    lines.append("Event Counts by Column:")
    counts = summary.get("event_count_by_column", {})
    for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        lines.append(f" - {k}: {v}")
    lines.append("")

    lines.append("Active Events in Last Row:")
    for e in summary.get("active_last_row_events", []):
        lines.append(f" - {e}")
    lines.append("")

    active_rows = event_tail_df[(event_tail_df > 0).any(axis=1)]
    lines.append(f"--- Active Events in Last {len(event_tail_df)} Rows ---")
    if active_rows.empty:
        lines.append("No active events found.")
    else:
        for idx, row in active_rows.iterrows():
            active = row[row > 0].index.tolist()
            lines.append(f"{idx}: {active}")

    return "\n".join(lines)


def build_divergence_batch_report(summary: dict) -> str:
    lines = ["=== DIVERGENCE BATCH SUMMARY ===", ""]

    success_count = 0
    error_count = 0
    empty_count = 0

    for sym, tfs in summary.items():
        if isinstance(tfs, dict):
            for tf, res in tfs.items():
                status = res.get("status")
                if status == "success":
                    success_count += 1
                elif status == "error":
                    error_count += 1
                elif status == "empty":
                    empty_count += 1

    lines.append(f"Total Success: {success_count}")
    lines.append(f"Total Errors: {error_count}")
    lines.append(f"Total Empty: {empty_count}")
    lines.append("")

    lines.append("Details:")
    for sym, tfs in summary.items():
        if isinstance(tfs, dict):
            for tf, res in tfs.items():
                lines.append(
                    f"{sym} {tf}: {res.get('status')} - Rows: {res.get('rows', 0)} Features: {res.get('features', 0)} Events: {res.get('events', 0)}"
                )
                if res.get("warnings"):
                    lines.append(f"  Warnings: {', '.join(res['warnings'])}")
                if res.get("error"):
                    lines.append(f"  Error: {res['error']}")

    return "\n".join(lines)


def build_divergence_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = [
        "=== DIVERGENCE STATUS REPORT ===",
        f"Total Tradeable Symbols: {summary.get('total_symbols', 0)}",
        f"Symbols with Divergence: {summary.get('with_divergence', 0)}",
        f"Timeframes missing Divergence (but have technical): {summary.get('missing_but_has_technical', 0)}",
        "",
    ]

    lines.append("Timeframes Missing Divergence (but have Technical):")
    if (
        not status_df.empty
        and "has_technical" in status_df.columns
        and "has_divergence" in status_df.columns
    ):
        missing = status_df[status_df["has_technical"] & ~status_df["has_divergence"]]
        for _, row in missing.iterrows():
            lines.append(f" - {row['symbol']} {row['timeframe']}")
    lines.append("")

    return "\n".join(lines)


def build_mtf_alignment_preview_report(
    symbol: str, profile_name: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = []
    lines.append(f"=== MTF Alignment Preview: {symbol} ===")
    lines.append(f"Profil: {profile_name}")
    lines.append(f"Temel Zaman Dilimi: {summary.get('base_timeframe')}")
    lines.append(f"Bağlam Zaman Dilimleri: {summary.get('context_timeframes')}")
    lines.append(f"Satır Sayısı: {summary.get('rows')}")
    lines.append(f"Kolon Sayısı: {summary.get('columns')}")
    lines.append("")

    qr = summary.get("quality_report", {})
    lines.append("--- Kalite Raporu ---")
    lines.append(f"Testleri Geçti mi: {qr.get('passed', False)}")
    lines.append(f"NaN Oranı: {qr.get('total_nan_ratio', 0.0):.2%}")
    lines.append(f"Eski (Stale) Veri Oranı: {qr.get('stale_context_ratio', 0.0):.2%}")

    warnings = summary.get("warnings", [])
    if warnings:
        lines.append("\nUyarılar:")
        for w in warnings:
            lines.append(f"  - {w}")

    lines.append("\nSon Satırlar:")
    lines.append(tail_df.to_string())

    return "\n".join(lines)


def build_mtf_event_preview_report(
    symbol: str, profile_name: str, summary: dict, event_tail_df: pd.DataFrame
) -> str:
    lines = []
    lines.append(f"=== MTF Event Preview: {symbol} ===")
    lines.append(f"Profil: {profile_name}")
    lines.append(f"Toplam Olay Sayısı: {summary.get('total_event_count', 0)}")
    lines.append(
        f"Aktif Son Satır Olayları: {summary.get('active_last_row_events', [])}"
    )
    lines.append(f"Not: {summary.get('notes', '')}")
    lines.append("\nUyarılar:")
    for w in summary.get("warnings", []):
        lines.append(f"  - {w}")

    lines.append("\nSon Satırlar (Olaylar):")
    lines.append(event_tail_df.to_string())

    return "\n".join(lines)


def build_mtf_batch_report(summary: dict) -> str:
    lines = []
    lines.append("=== MTF Toplu İşlem Raporu ===")
    lines.append(f"Toplam İşlenen: {summary.get('total_processed', 0)}")
    return "\n".join(lines)


def build_mtf_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = []
    lines.append("=== MTF Durum Raporu ===")
    lines.append(f"Toplam Sembol: {len(status_df)}")
    lines.append(f"MTF Feature Olanlar: {status_df['has_mtf'].sum()}")


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
    lines.append(
        f"Son Rejim: {summary.get('latest_regime')} (Güven: {summary.get('latest_confidence', 0.0):.2f})"
    )
    lines.append("")

    qr = summary.get("quality_report", {})
    lines.append("--- Kalite Raporu ---")
    lines.append(f"Testleri Geçti mi: {qr.get('passed', False)}")
    lines.append(f"Ortalama Güven: {qr.get('average_confidence', 0.0):.2f}")
    lines.append(f"Düşük Güven Oranı: {qr.get('low_confidence_ratio', 0.0):.2%}")
    lines.append(f"Stabilite Skoru: {qr.get('stability_score', 0.0):.2f}")

    warnings = summary.get("warnings", [])
    if warnings:
        lines.append("\\nUyarılar:")
        for w in warnings:
            lines.append(f"  - {w}")

    lines.append(
        "\\nUyarı: Rejimler piyasa bağlamını ifade eder, nihai AL/SAT işlemi (trade signal) değildir."
    )

    lines.append("\\nSon Satırlar:")
    lines.append(tail_df.to_string())

    return "\n".join(lines)


def build_regime_event_preview_report(
    symbol: str,
    timeframe: str,
    profile_name: str,
    summary: dict,
    event_tail_df: pd.DataFrame,
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
    lines.append(
        f"Aktif Son Satır Olayları: {summary.get('active_last_row_events', [])}"
    )

    lines.append("\\nUyarılar:")
    for w in summary.get("warnings", []):
        lines.append(f"  - {w}")

    lines.append(f"\\nNot: {summary.get('notes', '')}")
    lines.append("Bu eventler nihai al/sat sinyali değildir.")

    lines.append("\\nSon Satırlar (Olaylar):")
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
                    lines.append(
                        f"{sym} {tf}: Başarılı - Son Rejim: {res.get('latest_regime')} ({res.get('latest_confidence', 0):.2f})"
                    )
                else:
                    lines.append(
                        f"{sym} {tf}: {status} - Hata: {res.get('error')} Uyarı: {res.get('warnings')}"
                    )

    return "\n".join(lines)


def build_regime_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = []
    lines.append("=== Rejim Durum Raporu ===")
    lines.append(f"Toplam Sembol: {len(status_df)}")
    if not status_df.empty:
        lines.append(f"Rejim Feature Olanlar: {status_df['has_regime'].sum()}")
        lines.append(f"Rejim Event Olanlar: {status_df['has_regime_events'].sum()}")

        if "has_technical" in status_df.columns and "has_regime" in status_df.columns:
            missing = status_df[status_df["has_technical"] & ~status_df["has_regime"]]
            lines.append(
                f"\\nRejimi Eksik Olanlar (Teknik feature var ama rejim yok): {len(missing)}"
            )
            for _, row in missing.iterrows():
                lines.append(f" - {row['symbol']} {row['timeframe']}")

    return "\n".join(lines)

    def build_macro_data_update_report(self, summary: dict) -> str:
        """Build report for macro data update."""
        lines = [
            "===========================================================",
            "MAKRO VERİ GÜNCELLEME RAPORU",
            "===========================================================",
        ]

        for k, v in summary.items():
            lines.append(f"{k}: {v}")

        return "\n".join(lines)

    def build_macro_feature_preview_report(
        self, summary: dict, tail_df: pd.DataFrame
    ) -> str:
        """Build report for macro feature preview."""
        lines = [
            "===========================================================",
            "MAKRO ÖZELLİK ÖNİZLEME RAPORU",
            "===========================================================",
        ]

        for k, v in summary.items():
            lines.append(f"{k}: {v}")

        lines.append("\n--- Son Veriler ---")
        if not tail_df.empty:
            lines.append(tail_df.to_string())
        else:
            lines.append("Veri bulunamadı.")

        return "\n".join(lines)

    def build_macro_benchmark_report(
        self, summary: dict, benchmark_tail_df: pd.DataFrame
    ) -> str:
        """Build report for macro benchmark."""
        lines = [
            "===========================================================",
            "MAKRO BENCHMARK RAPORU",
            "===========================================================",
        ]

        for k, v in summary.items():
            lines.append(f"{k}: {v}")

        lines.append("\n--- Benchmark Son Veriler ---")
        if not benchmark_tail_df.empty:
            lines.append(benchmark_tail_df.to_string())
        else:
            lines.append("Veri bulunamadı.")

        return "\n".join(lines)

    def build_macro_batch_report(self, summary: dict) -> str:
        """Build report for macro batch execution."""
        lines = [
            "===========================================================",
            "MAKRO TOPLU İŞLEM RAPORU",
            "===========================================================",
        ]

        for k, v in summary.items():
            lines.append(f"{k}: {v}")

        return "\n".join(lines)

    def build_macro_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        """Build report for macro status."""
        lines = [
            "===========================================================",
            "MAKRO DURUM RAPORU",
            "===========================================================",
        ]

        for k, v in summary.items():
            lines.append(f"{k}: {v}")

        lines.append("\n--- Durum Tablosu ---")
        if not status_df.empty:
            lines.append(status_df.to_string())
        else:
            lines.append("Durum bilgisi bulunamadı.")

        return "\n".join(lines)


def build_asset_profile_preview_report(
    symbol: str, timeframe: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = [
        f"=== ASSET PROFILE PREVIEW ===",
        f"Symbol: {symbol}",
        f"Timeframe: {timeframe}",
        f"Asset Class: {summary.get('asset_class', 'Unknown')}",
        f"Asset Profile: {summary.get('asset_profile', 'Unknown')}",
        f"",
        f"--- DATA STATUS ---",
        f"Rows: {summary.get('rows', 0)}",
        f"Columns: {len(summary.get('columns', []))}",
        f"Missing Feature Sets: {', '.join(summary.get('missing_feature_sets', [])) or 'None'}",
        f"",
        f"--- GROUP CONTEXT ---",
        f"Group Members Expected: {summary.get('group_member_count', 0)}",
        f"Group Members Available: {summary.get('available_group_members', 0)}",
        f"",
        f"--- CURRENT REGIMES ---",
        f"Asset Behavior Regime: {summary.get('latest_asset_regime', 'Unknown')}",
        f"Group Regime: {summary.get('latest_group_regime', 'Unknown')}",
        f"Relative Strength Regime: {summary.get('latest_relative_strength_label', 'Unknown')}",
        f"",
        f"--- QUALITY REPORT ---",
    ]

    qr = summary.get("quality_report", {})
    lines.append(f"Passed: {qr.get('passed', False)}")
    lines.append(f"NaN Ratio: {qr.get('total_nan_ratio', 0.0):.2%}")

    if summary.get("warnings"):
        lines.append("")
        lines.append("--- WARNINGS ---")
        for w in summary["warnings"]:
            lines.append(f"- {w}")

    if not tail_df.empty:
        lines.append("")
        lines.append("--- LATEST FEATURES ---")
        # Select some key features
        cols = [
            c for c in tail_df.columns if "score" in c or "label" in c or "regime" in c
        ]
        lines.append(tail_df[cols].to_string())

    return "\n".join(lines)


def build_asset_group_event_preview_report(
    asset_class: str, timeframe: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = [
        f"=== ASSET GROUP EVENT PREVIEW ===",
        f"Asset Class: {asset_class}",
        f"Timeframe: {timeframe}",
        f"",
        f"--- DATA STATUS ---",
        f"Rows: {summary.get('rows', 0)}",
        f"Available Members: {len(summary.get('members', []))}",
        f"",
    ]

    if summary.get("warnings"):
        lines.append("--- WARNINGS ---")
        for w in summary["warnings"]:
            lines.append(f"- {w}")
        lines.append("")

    if not tail_df.empty:
        lines.append("--- LATEST GROUP FEATURES ---")
        cols = [
            c
            for c in tail_df.columns
            if "regime" in c or "dispersion" in c or "volatility" in c or "return" in c
        ]
        if cols:
            lines.append(tail_df[cols].to_string())
        else:
            lines.append(tail_df.to_string())

    return "\n".join(lines)


def build_asset_profile_batch_report(summary: dict) -> str:
    lines = [
        "=== ASSET PROFILE BATCH BUILD REPORT ===",
        f"Successfully Processed: {summary.get('processed', 0)}",
        f"Errors: {summary.get('errors', 0)}",
        "",
    ]

    for ac, ac_sum in summary.get("asset_classes", {}).items():
        lines.append(f"--- {ac.upper()} ---")
        success = sum(
            1 for s in ac_sum.get("symbols", {}).values() if not s.get("warnings")
        )
        lines.append(f"Success: {success} / {len(ac_sum.get('symbols', {}))}")
        if ac_sum.get("warnings"):
            lines.append("Warnings:")
            for w in ac_sum["warnings"]:
                lines.append(f"  - {w}")
        lines.append("")

    return "\n".join(lines)


def build_asset_profile_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = [
        "=== ASSET PROFILE STATUS REPORT ===",
        f"Total Symbols: {summary.get('total_symbols', 0)}",
        f"Asset Classes: {summary.get('total_asset_classes', 0)}",
        "",
        "--- ASSET CLASS SUMMARY ---",
    ]

    for ac, ac_info in summary.get("asset_classes", {}).items():
        lines.append(
            f"{ac}: {ac_info.get('profiles_count', 0)} profiles, {ac_info.get('group_features_count', 0)} group features"
        )

    if not status_df.empty:
        lines.append("")
        lines.append("--- DETAILS ---")
        lines.append(status_df.to_string())

    return "\n".join(lines)


def build_signal_candidate_preview_report(
    symbol: str, timeframe: str, profile_name: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = [
        f"=== SİNYAL ADAYI ÖNİZLEME RAPORU ===",
        f"Sembol: {symbol}",
        f"Zaman Dilimi: {timeframe}",
        f"Profil: {profile_name}",
        f"",
        f"--- DURUM ---",
        f"Yüklenen Event Grupları: {', '.join(summary.get('loaded_event_groups', [])) or 'Yok'}",
        f"Eksik Event Grupları: {', '.join(summary.get('missing_event_groups', [])) or 'Yok'}",
        f"Toplam Aday Sayısı: {summary.get('candidate_count', 0)}",
        f"Filtreyi Geçen Aday Sayısı: {summary.get('passed_candidate_count', 0)}",
        f"",
        f"--- UYARILAR ---",
        f"Bu çıktılar nihai işlem sinyali değildir. Aday setup ve bağlam skorlarıdır. Canlı emir üretilmez.",
        f"",
    ]
    if summary.get("warnings"):
        for w in summary["warnings"]:
            lines.append(f"- {w}")
        lines.append("")

    if not tail_df.empty:
        lines.append("--- SON ADAYLAR ---")
        cols = [
            "timestamp",
            "candidate_type",
            "directional_bias",
            "candidate_score",
            "confidence_score",
            "passed_pre_filters",
        ]
        avail_cols = [c for c in cols if c in tail_df.columns]
        lines.append(tail_df[avail_cols].to_string())

    return "\n".join(lines)


def build_signal_batch_report(summary: dict) -> str:
    lines = [
        f"=== SİNYAL TOPLU İŞLEM RAPORU ===",
        f"İşlenen: {summary.get('processed', 0)}",
        f"Atlanan: {summary.get('skipped', 0)}",
        f"Hatalı: {summary.get('errors', 0)}",
        f"Toplam Aday: {summary.get('total_candidates', 0)}",
        f"Adayı Olan Sembol Sayısı: {summary.get('symbols_with_candidates', 0)}",
        f"",
        f"Bu çıktılar nihai işlem sinyali değildir. Aday setup ve bağlam skorlarıdır. Canlı emir üretilmez.",
    ]
    return "\n".join(lines)


def build_signal_pool_preview_report(
    timeframe: str, profile_name: str, summary: dict, top_df: pd.DataFrame
) -> str:
    lines = [
        f"=== SİNYAL ADAY HAVUZU ÖNİZLEME ===",
        f"Zaman Dilimi: {timeframe}",
        f"Profil: {profile_name}",
        f"",
        f"--- ÖZET ---",
        f"Toplam Aday: {summary.get('total_candidates', 0)}",
        f"Filtreyi Geçen: {summary.get('passed_candidates', 0)}",
        f"Ortalama Aday Skoru: {summary.get('average_candidate_score', 0):.2f}",
        f"Ortalama Güven Skoru: {summary.get('average_confidence_score', 0):.2f}",
        f"",
        f"--- DAĞILIM ---",
        f"Sembollere Göre: {summary.get('by_symbol', {})}",
        f"Aday Tiplerine Göre: {summary.get('by_candidate_type', {})}",
        f"Yönsel Biase Göre: {summary.get('by_directional_bias', {})}",
        f"",
        f"--- EN İYİ ADAYLAR ---",
    ]

    if not top_df.empty:
        cols = [
            "symbol",
            "timestamp",
            "candidate_type",
            "directional_bias",
            "candidate_score",
            "passed_pre_filters",
        ]
        avail_cols = [c for c in cols if c in top_df.columns]
        lines.append(top_df[avail_cols].to_string())

    lines.append("")
    lines.append(
        "Bu çıktılar nihai işlem sinyali değildir. Aday setup ve bağlam skorlarıdır. Canlı emir üretilmez."
    )

    return "\n".join(lines)


def build_signal_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = [
        f"=== SİNYAL SİSTEMİ DURUM RAPORU ===",
        f"Sinyal Aday Dosyası Olanlar: {summary.get('total_with_candidates', 0)}",
        f"Toplam Aday Sayısı (Havuz): {summary.get('total_pool_candidates', 0)}",
        f"Ortalama Skor: {summary.get('average_pool_score', 0):.2f}",
        f"",
    ]

    if not status_df.empty:
        lines.append("--- DETAYLAR ---")
        lines.append(status_df.to_string())

    lines.append("")
    lines.append(
        "Bu çıktılar nihai işlem sinyali değildir. Aday setup ve bağlam skorlarıdır. Canlı emir üretilmez."
    )

    return "\n".join(lines)


def build_decision_candidate_preview_report(
    symbol: str, timeframe: str, profile_name: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = [
        "===========================================================",
        "           DECISION CANDIDATE PREVIEW",
        "===========================================================",
        f"Symbol:   {symbol}",
        f"Timeframe: {timeframe}",
        f"Profile:   {profile_name}",
        "",
        "** UYARI: Bu çıktılar nihai işlem sinyali değildir. **",
        "** Long/short bias adayları emir değildir. Canlı emir üretilmez. **",
        "",
        f"Loaded Signal Candidates: {summary.get('loaded_signal_candidates', 0)}",
        f"Total Decisions Generated: {summary.get('decision_count', 0)}",
        f"Passed Decisions: {summary.get('passed_decision_count', 0)}",
        "",
    ]

    if summary.get("missing_context_frames"):
        lines.append(
            f"Missing Context Frames: {', '.join(summary['missing_context_frames'])}"
        )
        lines.append("")

    if summary.get("warnings"):
        lines.append("Warnings:")
        for w in summary["warnings"]:
            lines.append(f"  - {w}")
        lines.append("")

    if not tail_df.empty:
        lines.append("--- Son Adaylar ---")
        cols_to_show = [
            "decision_label",
            "directional_bias",
            "decision_score",
            "decision_confidence",
            "conflict_score",
        ]
        exist_cols = [c for c in cols_to_show if c in tail_df.columns]
        lines.append(tail_df[exist_cols].to_string())

    return "\n".join(lines)


def build_decision_batch_report(summary: dict) -> str:
    lines = [
        "===========================================================",
        "           DECISION BATCH BUILD SUMMARY",
        "===========================================================",
        f"Timeframe: {summary.get('timeframe', 'N/A')}",
        f"Profile:   {summary.get('profile', 'N/A')}",
        "",
        "** UYARI: Bu çıktılar nihai işlem sinyali değildir. **",
        "** Long/short bias adayları emir değildir. Canlı emir üretilmez. **",
        "",
        f"Processed Symbols: {summary.get('processed_symbols', 0)}",
        f"Successful Symbols: {summary.get('successful_symbols', 0)}",
        f"Failed Symbols: {summary.get('failed_symbols', 0)}",
        f"Total Decisions Generated: {summary.get('total_decisions', 0)}",
        f"Passed Decisions: {summary.get('passed_decisions', 0)}",
    ]
    return "\n".join(lines)


def build_decision_pool_preview_report(
    timeframe: str, profile_name: str, summary: dict, top_df: pd.DataFrame
) -> str:
    lines = [
        "===========================================================",
        "           DECISION POOL PREVIEW",
        "===========================================================",
        f"Timeframe: {timeframe}",
        f"Profile:   {profile_name}",
        "",
        "** UYARI: Bu çıktılar nihai işlem sinyali değildir. **",
        "** Long/short bias adayları emir değildir. Canlı emir üretilmez. **",
        "",
        f"Total Decisions: {summary.get('total_decisions', 0)}",
        f"Passed Decisions: {summary.get('passed_decisions', 0)}",
        f"Average Score: {summary.get('average_decision_score', 0):.2f}",
        f"Average Confidence: {summary.get('average_confidence', 0):.2f}",
        "",
    ]

    if summary.get("by_decision_label"):
        lines.append("--- By Decision Label ---")
        for label, count in summary["by_decision_label"].items():
            lines.append(f"  {label}: {count}")
        lines.append("")

    if not top_df.empty:
        lines.append("--- Top Decisions ---")
        cols_to_show = [
            "symbol",
            "decision_label",
            "directional_bias",
            "decision_score",
        ]
        exist_cols = [c for c in cols_to_show if c in top_df.columns]
        lines.append(top_df[exist_cols].to_string())

    return "\n".join(lines)


def build_decision_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = [
        "===========================================================",
        "           DECISION PIPELINE STATUS",
        "===========================================================",
        "",
        f"Total Candidate Files: {summary.get('total_candidate_files', 0)}",
        f"Total Pool Files: {summary.get('total_pool_files', 0)}",
        f"Symbols with Decisions: {summary.get('symbols_with_decisions', 0)}",
        "",
    ]

    if not status_df.empty:
        lines.append("--- Status Details ---")
        lines.append(status_df.to_string(index=False))

    return "\n".join(lines)


def build_strategy_candidate_preview_report(
    symbol: str, timeframe: str, profile_name: str, summary: dict, tail_df
) -> str:
    lines = [
        f"=== STRATEGY CANDIDATE PREVIEW ===",
        f"Symbol: {symbol} | Timeframe: {timeframe} | Profile: {profile_name}",
        f"Generated Candidates: {summary.get('strategy_candidate_count', 0)}",
        f"Passed Candidates: {summary.get('passed_strategy_candidate_count', 0)}",
        "WARNING: Bu çıktılar strateji ailesi adaylarıdır. Nihai işlem sinyali, emir, pozisyon talimatı veya canlı işlem kararı değildir.",
        "--------------------------------------------------",
        "Last Candidates:",
    ]

    if not tail_df.empty:
        for _, row in tail_df.iterrows():
            lines.append(
                f"Date: {row.name} | Family: {row.get('strategy_family', 'N/A')} | Status: {row.get('strategy_status', 'N/A')} | Score: {row.get('strategy_selection_score', 0.0):.2f}"
            )
    else:
        lines.append("No candidates found.")

    return "\n".join(lines)


def build_strategy_batch_report(summary: dict) -> str:
    lines = [
        "=== STRATEGY BATCH SUMMARY ===",
        f"Profile: {summary.get('profile', 'N/A')} | Timeframe: {summary.get('timeframe', 'N/A')}",
        f"Processed Symbols: {summary.get('processed_symbols', 0)}",
        f"Success: {summary.get('success_symbols', 0)} | Failed: {summary.get('failed_symbols', 0)}",
        f"Total Candidates: {summary.get('total_strategy_candidates', 0)}",
        "WARNING: Bu çıktılar strateji ailesi adaylarıdır. Nihai işlem sinyali, emir, pozisyon talimatı veya canlı işlem kararı değildir.",
    ]
    return "\n".join(lines)


def build_strategy_pool_preview_report(
    timeframe: str, profile_name: str, summary: dict, top_df
) -> str:
    lines = [
        "=== STRATEGY POOL PREVIEW ===",
        f"Timeframe: {timeframe} | Profile: {profile_name}",
        f"Total Candidates: {summary.get('total_strategy_candidates', 0)}",
        f"Passed Candidates: {summary.get('passed_strategy_candidates', 0)}",
        f"Average Selection Score: {summary.get('average_selection_score', 0.0):.2f}",
        "WARNING: Bu çıktılar strateji ailesi adaylarıdır. Nihai işlem sinyali, emir, pozisyon talimatı veya canlı işlem kararı değildir.",
        "--------------------------------------------------",
        "Top Candidates:",
    ]

    if not top_df.empty:
        for idx, row in top_df.iterrows():
            lines.append(
                f"Symbol: {row.get('symbol', 'N/A')} | Family: {row.get('strategy_family', 'N/A')} | Status: {row.get('strategy_status', 'N/A')} | Score: {row.get('strategy_selection_score', 0.0):.2f}"
            )
    else:
        lines.append("No candidates found in pool.")

    return "\n".join(lines)


def build_strategy_status_report(status_df, summary: dict) -> str:
    lines = [
        "=== STRATEGY STATUS REPORT ===",
        f"Total Items: {len(status_df)}",
        "WARNING: Bu çıktılar strateji ailesi adaylarıdır. Nihai işlem sinyali, emir, pozisyon talimatı veya canlı işlem kararı değildir.",
    ]
    return "\n".join(lines)


def build_risk_precheck_preview_report(
    symbol: str, timeframe: str, profile_name: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = [
        f"=== RISK PRECHECK PREVIEW ({symbol} - {timeframe}) ===",
        f"Profile: {profile_name}",
        "---",
        "UYARI: Bu çıktılar risk ön kontrol adaylarıdır. Risk approval/rejection/watchlist ifadeleri "
        "gerçek işlem onayı, emir iptali, pozisyon talimatı veya broker işlemi değildir. Canlı emir üretilmez.",
        "---",
    ]
    if "error" in summary:
        lines.append(f"Hata: {summary['error']}")
        return "\n".join(lines)
    lines.append(f"Toplam Aday: {summary.get('risk_candidate_count', 0)}")
    lines.append(f"Onaylanan: {summary.get('passed_risk_candidate_count', 0)}")
    lines.append(f"Reddedilen: {summary.get('rejected_risk_candidate_count', 0)}")
    lines.append(f"İzleme Listesi: {summary.get('watchlist_risk_candidate_count', 0)}")
    lines.append("")
    if summary.get("missing_context_frames"):
        lines.append("Eksik Context Frame'leri:")
        for frame in summary["missing_context_frames"]:
            lines.append(f"- {frame}")
        lines.append("")
    if not tail_df.empty:
        lines.append(f"--- Son {len(tail_df)} Risk Adayı ---")
        for _, row in tail_df.iterrows():
            lines.append(
                f"Tarih: {row['timestamp']} | Yön: {row['directional_bias']} | Label: {row['risk_label']}"
            )
            lines.append(f"  Toplam Risk Skoru: {row['total_pretrade_risk_score']:.2f}")
            lines.append(f"  Risk Readiness: {row['risk_readiness_score']:.2f}")
            bl_reasons = row.get("blocking_reasons", [])
            if isinstance(bl_reasons, str):
                bl_reasons = eval(bl_reasons) if bl_reasons.startswith("[") else []
            if bl_reasons:
                lines.append("  Engelleme Nedenleri:")
                for r in bl_reasons:
                    lines.append(f"    - {r}")
            lines.append("")
    return "\n".join(lines)


def build_risk_batch_report(summary: dict) -> str:
    lines = [
        "=== RISK BATCH SUMMARY ===",
        "---",
        "UYARI: Bu çıktılar risk ön kontrol adaylarıdır. Risk approval/rejection/watchlist ifadeleri "
        "gerçek işlem onayı, emir iptali, pozisyon talimatı veya broker işlemi değildir. Canlı emir üretilmez.",
        "---",
        f"İşlenen Sembol Sayısı: {summary.get('processed', 0)}",
        f"Toplam Havuz Adayı: {summary.get('total_candidates', 0)}",
        "--- Sembol Özeti ---",
    ]
    for sym, s_summary in summary.get("symbol_summaries", {}).items():
        if "error" in s_summary:
            lines.append(f"{sym}: Hata - {s_summary['error']}")
        elif "skipped" in s_summary:
            lines.append(f"{sym}: Atlandı - {s_summary.get('reason', '')}")
        else:
            lines.append(
                f"{sym}: {s_summary.get('risk_candidate_count', 0)} aday ({s_summary.get('passed_risk_candidate_count', 0)} geçti)"
            )
    return "\n".join(lines)


def build_risk_pool_preview_report(
    timeframe: str, profile_name: str, summary: dict, top_df: pd.DataFrame
) -> str:
    lines = [
        f"=== RISK POOL PREVIEW ({timeframe}) ===",
        f"Profile: {profile_name}",
        "---",
        "UYARI: Bu çıktılar risk ön kontrol adaylarıdır. Risk approval/rejection/watchlist ifadeleri "
        "gerçek işlem onayı, emir iptali, pozisyon talimatı veya broker işlemi değildir. Canlı emir üretilmez.",
        "---",
        f"Havuz Toplam Aday: {summary.get('total_risk_candidates', 0)}",
        f"Geçen: {summary.get('passed_risk_candidates', 0)}",
        f"Ortalama Total Risk: {summary.get('average_total_pretrade_risk', 0.0):.2f}",
        "",
    ]
    if not top_df.empty:
        lines.append(f"--- Top {len(top_df)} Readiness Scoruna Göre Adaylar ---")
        for _, row in top_df.iterrows():
            lines.append(
                f"Sembol: {row['symbol']} | Tarih: {row['timestamp']} | Yön: {row['directional_bias']}"
            )
            lines.append(
                f"  Strateji: {row['strategy_family']} | Label: {row['risk_label']}"
            )
            lines.append(
                f"  Readiness: {row['risk_readiness_score']:.2f} | Risk: {row['total_pretrade_risk_score']:.2f}"
            )
            lines.append("")
    return "\n".join(lines)


def build_risk_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = [
        "=== RISK STATUS REPORT ===",
        "---",
        "UYARI: Bu çıktılar risk ön kontrol adaylarıdır. Gerçek emir üretilmez.",
        "---",
        f"İşlenmiş Sembol Sayısı: {summary.get('processed_symbols', 0)}",
        f"Toplam Havuz Dosyası: {summary.get('pool_files', 0)}",
        "",
    ]
    if not status_df.empty:
        lines.append("Detaylar CSV dosyasına kaydedildi.")
    return "\n".join(lines)


def build_sizing_candidate_preview_report(
    symbol: str, timeframe: str, profile_name: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    lines = [
        f"--- TEORİK SIZING CANDIDATE PREVIEW ---",
        f"Symbol: {symbol}",
        f"Timeframe: {timeframe}",
        f"Profile: {profile_name}",
        f"Loaded Risk Candidates: {summary.get('loaded_risk_candidates', 0)}",
        f"Sizing Candidates Produced: {summary.get('sizing_candidate_count', 0)}",
        f"Passed: {summary.get('passed_sizing_candidate_count', 0)}",
        f"Rejected: {summary.get('rejected_sizing_candidate_count', 0)}",
        f"Watchlist: {summary.get('watchlist_sizing_candidate_count', 0)}",
        "",
    ]
    if summary.get("warnings"):
        lines.append("Uyarılar:")
        for w in summary["warnings"]:
            lines.append(f" - {w}")
        lines.append("")

    lines.append(
        "UYARI: Bu çıktılar teorik pozisyon boyutu simülasyon adaylarıdır. Gerçek lot/adet/kontrat, emir, pozisyon talimatı, kaldıraç veya canlı işlem kararı değildir. Canlı emir üretilmez."
    )
    lines.append("")

    if not tail_df.empty:
        lines.append("Son Sizing Adayları:")
        for idx, row in tail_df.iterrows():
            lines.append(
                f"[{idx}] Label: {row.get('sizing_label')} | Risk: {row.get('theoretical_risk_amount')} | "
                f"Adj Units: {row.get('adjusted_theoretical_units')} | Adj Notional: {row.get('adjusted_theoretical_notional')}"
            )
            if row.get("block_reasons"):
                lines.append(f"  Block Reasons: {row.get('block_reasons')}")
            if row.get("watchlist_reasons"):
                lines.append(f"  Watchlist Reasons: {row.get('watchlist_reasons')}")

    return "\n".join(lines)


def build_sizing_batch_report(summary: dict) -> str:
    lines = [
        "--- TEORİK SIZING BATCH SUMMARY ---",
        f"Processed Symbols: {summary.get('processed_symbols', 0)}",
        f"Failed Symbols: {summary.get('failed_symbols', 0)}",
        f"Total Candidates in Pool: {summary.get('total_candidates', 0)}",
        "",
    ]
    pool_summary = summary.get("summary", {})
    if pool_summary:
        lines.append(f"Passed: {pool_summary.get('passed_sizing_candidates', 0)}")
        lines.append(f"Rejected: {pool_summary.get('rejected_sizing_candidates', 0)}")
        lines.append(f"Watchlist: {pool_summary.get('watchlist_sizing_candidates', 0)}")
        lines.append(
            f"Avg Readiness: {pool_summary.get('average_sizing_readiness', 0.0):.2f}"
        )

    lines.append("")
    lines.append(
        "UYARI: Bu çıktılar teorik pozisyon boyutu simülasyon adaylarıdır. Gerçek lot/adet/kontrat, emir, pozisyon talimatı, kaldıraç veya canlı işlem kararı değildir. Canlı emir üretilmez."
    )
    return "\n".join(lines)


def build_sizing_pool_preview_report(
    timeframe: str, profile_name: str, summary: dict, top_df: pd.DataFrame
) -> str:
    lines = [
        "--- TEORİK SIZING POOL PREVIEW ---",
        f"Timeframe: {timeframe}",
        f"Profile: {profile_name}",
        f"Total Candidates: {summary.get('total_sizing_candidates', 0)}",
        f"Passed: {summary.get('passed_sizing_candidates', 0)}",
        f"Rejected: {summary.get('rejected_sizing_candidates', 0)}",
        f"Watchlist: {summary.get('watchlist_sizing_candidates', 0)}",
        f"Avg Readiness: {summary.get('average_sizing_readiness', 0.0):.2f}",
        "",
    ]
    lines.append(
        "UYARI: Bu çıktılar teorik pozisyon boyutu simülasyon adaylarıdır. Gerçek lot/adet/kontrat, emir, pozisyon talimatı, kaldıraç veya canlı işlem kararı değildir. Canlı emir üretilmez."
    )
    lines.append("")

    if not top_df.empty:
        lines.append("En Yüksek Puanlı Sizing Adayları:")
        for _, row in top_df.iterrows():
            lines.append(
                f"{row.get('symbol')} | Label: {row.get('sizing_label')} | "
                f"Method: {row.get('sizing_method')} | Risk: {row.get('theoretical_risk_amount')} | "
                f"Readiness: {row.get('sizing_readiness_score', 0.0):.2f} | "
                f"Adj Notional: {row.get('adjusted_theoretical_notional')}"
            )

    return "\n".join(lines)


def build_sizing_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = [
        "--- TEORİK SIZING STATUS ---",
        f"Total Sizing Pools: {summary.get('total_pools', 0)}",
        f"Total Individual Candidates: {summary.get('total_candidates', 0)}",
        "",
    ]
    lines.append(
        "UYARI: Bu çıktılar teorik pozisyon boyutu simülasyon adaylarıdır. Gerçek lot/adet/kontrat, emir, pozisyon talimatı, kaldıraç veya canlı işlem kararı değildir. Canlı emir üretilmez."
    )
    return "\n".join(lines)


def build_level_candidate_preview_report(
    symbol: str, timeframe: str, profile_name: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    report = []
    report.append(
        f"Level Candidate Preview: {symbol} - {timeframe} (Profile: {profile_name})"
    )
    report.append("=" * 80)
    report.append(
        "UYARI: Bu çıktılar teorik stop/target seviye simülasyon adaylarıdır. Stop/target/invalidation ifadeleri gerçek stop-loss, take-profit, emir, pozisyon kapatma/açma veya canlı işlem kararı değildir. Canlı emir üretilmez."
    )
    report.append("-" * 80)
    report.append(f"Missing Context: {summary.get('missing_context_frames', [])}")
    report.append(f"Total Candidates: {summary.get('total_level_candidates', 0)}")
    report.append("-" * 80)
    if tail_df.empty:
        report.append("No candidates available.")
    else:
        cols_to_show = [
            "level_label",
            "theoretical_stop_level",
            "theoretical_target_level",
            "reward_risk",
        ]
        existing_cols = [c for c in cols_to_show if c in tail_df.columns]
        report.append(tail_df[existing_cols].to_string())
    return "\n".join(report)


def build_reward_risk_preview_report(
    symbol: str, timeframe: str, profile_name: str, summary: dict, tail_df: pd.DataFrame
) -> str:
    report = []
    report.append(
        f"Reward/Risk Preview: {symbol} - {timeframe} (Profile: {profile_name})"
    )
    report.append("=" * 80)
    report.append(
        "UYARI: Bu çıktılar teorik stop/target seviye simülasyon adaylarıdır. Stop/target/invalidation ifadeleri gerçek stop-loss, take-profit, emir, pozisyon kapatma/açma veya canlı işlem kararı değildir. Canlı emir üretilmez."
    )
    report.append("-" * 80)
    report.append(f"Average Reward/Risk: {summary.get('average_reward_risk', 0.0):.2f}")
    report.append("-" * 80)
    if tail_df.empty:
        report.append("No candidates available.")
    else:
        cols_to_show = ["level_label", "reward_risk", "block_reasons"]
        existing_cols = [c for c in cols_to_show if c in tail_df.columns]
        report.append(tail_df[existing_cols].to_string())
    return "\n".join(report)


def build_level_batch_report(summary: dict) -> str:
    report = []
    report.append("Level Batch Report")
    report.append("=" * 80)
    report.append(
        "UYARI: Bu çıktılar teorik stop/target seviye simülasyon adaylarıdır. Stop/target/invalidation ifadeleri gerçek stop-loss, take-profit, emir, pozisyon kapatma/açma veya canlı işlem kararı değildir. Canlı emir üretilmez."
    )
    report.append("-" * 80)
    report.append(f"Profile: {summary.get('profile')}")
    report.append(f"Processed Symbols: {summary.get('processed_symbols')}")
    report.append(f"Generated Rows: {summary.get('generated_rows')}")
    return "\n".join(report)


def build_level_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    report = []
    report.append("Level Status Report")
    report.append("=" * 80)
    report.append(
        "UYARI: Bu çıktılar teorik stop/target seviye simülasyon adaylarıdır. Stop/target/invalidation ifadeleri gerçek stop-loss, take-profit, emir, pozisyon kapatma/açma veya canlı işlem kararı değildir. Canlı emir üretilmez."
    )
    report.append("-" * 80)
    if status_df.empty:
        report.append("No level data found.")
    else:
        report.append(status_df.to_string())
    return "\n".join(report)


def build_backtest_preview_report(
    symbol: str,
    timeframe: str,
    profile_name: str,
    summary: dict,
    trades_tail_df: pd.DataFrame,
) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append(f"BACKTEST PREVIEW: {symbol} | {timeframe} | {profile_name}")
    lines.append("=" * 60)
    lines.append("UYARI: Bu çıktılar tarihsel simülasyon/backtest sonuçlarıdır.")
    lines.append(
        "Gerçek emir, canlı işlem, broker talimatı, kesin performans iddiası veya yatırım tavsiyesi değildir."
    )
    lines.append("-" * 60)

    perf = summary.get("performance", {})
    run_sum = summary.get("run_summary", {})

    lines.append(f"Input Candidates  : {run_sum.get('input_candidate_count', 0)}")
    lines.append(f"Simulated Trades  : {run_sum.get('simulated_trade_count', 0)}")
    lines.append(f"Win Rate          : {perf.get('win_rate', 0):.2%}")
    lines.append(f"Profit Factor     : {perf.get('profit_factor', 0):.2f}")
    lines.append(f"Total Return      : {perf.get('total_return_pct', 0):.2%}")

    lines.append("-" * 60)
    if not trades_tail_df.empty:
        lines.append("Son Islemler:")
        lines.append(
            trades_tail_df[
                [
                    "entry_timestamp",
                    "directional_bias",
                    "lifecycle_status",
                    "result_label",
                    "return_pct",
                ]
            ].to_string()
        )

    return "\n".join(lines)


def build_backtest_batch_report(summary: dict) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("BACKTEST BATCH SUMMARY")
    lines.append("=" * 60)
    lines.append("UYARI: Bu çıktılar tarihsel simülasyon/backtest sonuçlarıdır.")
    lines.append(
        "Gerçek emir, canlı işlem, broker talimatı, kesin performans iddiası veya yatırım tavsiyesi değildir."
    )
    lines.append("-" * 60)

    lines.append(f"Profile: {summary.get('profile', '')}")
    lines.append(f"Timeframe: {summary.get('timeframe', '')}")
    lines.append(f"Symbols Processed: {summary.get('symbols_processed', 0)}")
    lines.append(f"Total Trades: {summary.get('total_trades', 0)}")

    perf = summary.get("performance", {})
    lines.append(f"Avg Win Rate: {perf.get('win_rate', 0):.2%}")
    lines.append(f"Avg Profit Factor: {perf.get('profit_factor', 0):.2f}")

    return "\n".join(lines)


def build_backtest_trade_ledger_report(
    symbol: str,
    timeframe: str,
    profile_name: str,
    summary: dict,
    trades_df: pd.DataFrame,
) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append(f"BACKTEST TRADE LEDGER: {symbol} | {timeframe} | {profile_name}")
    lines.append("=" * 60)
    lines.append("UYARI: Bu çıktılar tarihsel simülasyon/backtest sonuçlarıdır.")
    lines.append(
        "Gerçek emir, canlı işlem, broker talimatı, kesin performans iddiası veya yatırım tavsiyesi değildir."
    )
    lines.append("-" * 60)

    lines.append(f"Total Trades: {summary.get('trade_count', 0)}")
    lines.append(
        f"Win/Loss/Breakeven: {summary.get('win_count', 0)} / {summary.get('loss_count', 0)} / {summary.get('breakeven_count', 0)}"
    )

    if not trades_df.empty:
        lines.append("\nSon 5 Islem Detayi:")
        tail = trades_df.tail(5)
        cols = [
            "entry_timestamp",
            "exit_timestamp",
            "directional_bias",
            "exit_reason",
            "net_pnl",
        ]
        cols = [c for c in cols if c in tail.columns]
        lines.append(tail[cols].to_string())

    return "\n".join(lines)


def build_backtest_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("BACKTEST STATUS REPORT")
    lines.append("=" * 60)
    lines.append("UYARI: Bu çıktılar tarihsel simülasyon/backtest sonuçlarıdır.")
    lines.append(
        "Gerçek emir, canlı işlem, broker talimatı, kesin performans iddiası veya yatırım tavsiyesi değildir."
    )
    lines.append("-" * 60)

    if status_df.empty:
        lines.append("No backtest runs found.")
    else:
        lines.append(f"Total Runs Found: {len(status_df)}")
        lines.append(
            status_df[
                ["symbol", "timeframe", "profile", "trade_count", "win_rate"]
            ].to_string()
        )

    return "\n".join(lines)


# --- Validation Reports ---

def build_walk_forward_preview_report(symbol: str, timeframe: str, profile_name: str, summary: dict, split_df: pd.DataFrame | None = None) -> str:
    """Builds a human-readable walk-forward validation report."""
    lines = [
        f"=== WALK-FORWARD VALIDATION PREVIEW ===",
        f"Sembol: {symbol} | Timeframe: {timeframe}",
        f"Profil: {profile_name}",
        "",
        "DİKKAT: Bu rapor tarihsel validasyon analizidir.",
        "Canlı strateji seçimi, gerçek emir, kesin performans iddiası veya yatırım tavsiyesi değildir.",
        "",
        "--- Walk-Forward Özeti ---",
        f"Toplam Split Sayısı: {summary.get('split_count', 0)}",
        f"Geçerli Split Sayısı: {summary.get('valid_split_count', 0)}",
        f"Ortalama Eğitim Getirisi: {summary.get('avg_train_return', 0.0):.2f}%",
        f"Ortalama Test Getirisi: {summary.get('avg_test_return', 0.0):.2f}%",
        f"Ortalama Eğitim Sharpe: {summary.get('avg_train_sharpe', 0.0):.2f}",
        f"Ortalama Test Sharpe: {summary.get('avg_test_sharpe', 0.0):.2f}",
        f"Pozitif Test Split Oranı: {summary.get('test_positive_ratio', 0.0):.2%}",
        f"Eğitim->Test Bozulma Oranı: {summary.get('train_test_degradation', 0.0):.2%}",
        ""
    ]

    robustness = summary.get('robustness', {})
    if robustness:
        lines.extend([
            "--- Robustness (Dayanıklılık) Özeti ---",
            f"Dayanıklılık Skoru: {robustness.get('robustness_score', 0.0):.2f}",
            f"Metric Tutarlılığı: {robustness.get('split_consistency', 0.0):.2f}",
            ""
        ])

    overfitting = summary.get('overfitting', {})
    if overfitting:
        lines.extend([
            "--- Overfitting (Aşırı Uyum) Risk Özeti ---",
            f"Risk Etiketi: {overfitting.get('overfitting_risk_label', 'unknown').upper()}",
            f"Toplam Risk Skoru: {overfitting.get('aggregate_overfitting_risk_score', 0.0):.2f}",
            ""
        ])

    if split_df is not None and not split_df.empty:
        lines.append("--- Split Detayları ---")
        for _, row in split_df.iterrows():
            idx = row.get("split_index", "?")
            lines.append(f"Split {idx}:")
            lines.append(f"  Eğitim: {row.get('train_start', '?')[:10]} -> {row.get('train_end', '?')[:10]} | İşlem: {row.get('train_trade_count', 0)} | Sharpe: {row.get('train_sharpe_ratio', 0.0):.2f}")
            lines.append(f"  Test:   {row.get('test_start', '?')[:10]} -> {row.get('test_end', '?')[:10]} | İşlem: {row.get('test_trade_count', 0)} | Sharpe: {row.get('test_sharpe_ratio', 0.0):.2f}")
        lines.append("")

    quality = summary.get('quality_report', {})
    if quality:
         lines.extend([
            "--- Kalite Kontrolü ---",
            f"Geçti mi: {'EVET' if quality.get('passed', False) else 'HAYIR'}",
         ])
         warnings = quality.get('warnings', [])
         if warnings:
              lines.append("Uyarılar:")
              for w in warnings:
                  lines.append(f"  - {w}")

    return "\n".join(lines)


def build_parameter_sensitivity_preview_report(symbol: str, timeframe: str, profile_name: str, summary: dict, sensitivity_df: pd.DataFrame | None = None) -> str:
    """Builds a human-readable parameter sensitivity report."""
    lines = [
        f"=== PARAMETER SENSITIVITY PREVIEW ===",
        f"Sembol: {symbol} | Timeframe: {timeframe}",
        f"Profil: {profile_name}",
        "",
        "DİKKAT: Bu rapor tarihsel validasyon analizidir.",
        "Canlı parametre seçimi, gerçek emir veya yatırım tavsiyesi değildir.",
        "",
        "--- Hassasiyet Özeti ---",
        f"Test Edilen Kombinasyon: {summary.get('combinations_tested', 0)}",
        f"Genel Stabilite Skoru: {summary.get('overall_stability_score', 0.0):.2f}",
        f"Kırılgan Parametre Değeri Sayısı: {summary.get('fragile_parameter_count', 0)}",
        ""
    ]

    if sensitivity_df is not None and not sensitivity_df.empty:
        fragile_df = sensitivity_df[sensitivity_df.get('fragility_warning', '') != '']
        if not fragile_df.empty:
            lines.append("--- Kırılgan Parametre Uyarıları ---")
            for _, row in fragile_df.iterrows():
                lines.append(f"Parametre: {row.get('parameter_name')} = {row.get('parameter_value')} -> {row.get('fragility_warning')}")
            lines.append("")

        lines.append("--- Parametre Etki Tablosu (Özet) ---")
        for _, row in sensitivity_df.head(15).iterrows():
            lines.append(f"{row.get('parameter_name')} = {row.get('parameter_value')}: Ortalama Metrik={row.get('metric_mean', 0.0):.2f}, Skor={row.get('sensitivity_score', 0.0):.2f}")

    return "\n".join(lines)


def build_optimizer_candidate_preview_report(symbol: str, timeframe: str, profile_name: str, summary: dict, optimizer_df: pd.DataFrame | None = None) -> str:
    """Builds a human-readable optimizer candidate report."""
    lines = [
        f"=== OPTIMIZER CANDIDATE PREVIEW ===",
        f"Sembol: {symbol} | Timeframe: {timeframe}",
        f"Profil: {profile_name}",
        "",
        "DİKKAT: Bu rapor tarihsel optimizer aday analizidir.",
        "Canlı strateji seçimi, gerçek emir, kesin performans iddiası veya yatırım tavsiyesi değildir.",
        "Adayların 'passed' olması canlı işlem onayı anlamına gelmez.",
        "",
        "--- Aday Özeti ---",
        f"Toplam Aday: {summary.get('total_candidates', 0)}",
        f"Geçen (Passed): {summary.get('passed_candidates', 0)}",
        f"İzleme (Watchlist): {summary.get('watchlist_candidates', 0)}",
        f"Aşırı Uyum Riski (Overfit): {summary.get('overfit_warning_candidates', 0)}",
        f"Reddedilen (Rejected): {summary.get('rejected_candidates', 0)}",
        ""
    ]

    if optimizer_df is not None and not optimizer_df.empty:
        lines.append("--- En İyi 10 Aday ---")
        for i, row in optimizer_df.head(10).iterrows():
            params = {k.replace('param_', ''): v for k, v in row.items() if str(k).startswith('param_')}
            lines.append(f"Aday #{i+1} [{row.get('candidate_label')}]")
            lines.append(f"  Skor: {row.get('optimizer_candidate_score', 0.0):.2f} | Metrik: {row.get('primary_metric_value', 0.0):.2f}")
            lines.append(f"  Robustness: {row.get('robustness_score', 0.0):.2f} | Overfit Risk: {row.get('overfitting_risk_score', 0.0):.2f}")
            lines.append(f"  Parametreler: {params}")
            lines.append("")

    return "\n".join(lines)


def build_validation_batch_report(summary: dict, ranking_df: pd.DataFrame | None = None) -> str:
    """Builds a human-readable batch validation summary."""
    lines = [
        f"=== BATCH VALIDATION SUMMARY ===",
        "",
        "DİKKAT: Bu rapor tarihsel validasyon ve optimizer aday analizidir.",
        "Canlı strateji seçimi, gerçek emir veya yatırım tavsiyesi değildir.",
        "",
        f"İşlenen Sembol: {summary.get('processed_count', 0)}",
        f"Geçen (Passed) Sembol: {summary.get('passed_count', 0)}",
        ""
    ]

    if ranking_df is not None and not ranking_df.empty:
        lines.append("--- Sembol Sıralaması (Dayanıklılığa Göre) ---")
        for _, row in ranking_df.iterrows():
            lines.append(f"{row.get('symbol')} [{row.get('validation_status')}]:")
            lines.append(f"  Robustness: {row.get('robustness_score', 0.0):.2f} | Overfit Risk: {row.get('overfitting_risk_score', 0.0):.2f} | Splits: {row.get('split_count', 0)}")

    return "\n".join(lines)


def build_validation_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    """Builds a human-readable validation status report."""
    lines = [
        f"=== VALIDATION STATUS REPORT ===",
        "",
        "DİKKAT: Bu rapor tarihsel validasyon analiz durumunu gösterir.",
        "Canlı işlem onayı değildir.",
        "",
        f"Toplam Kayıtlı Rapor: {summary.get('total_reports', 0)}",
        f"Benzersiz Sembol: {summary.get('unique_symbols', 0)}",
        ""
    ]

    if status_df is not None and not status_df.empty:
        lines.append("--- Rapor Dağılımı ---")
        # Just list a few for preview
        for _, row in status_df.head(20).iterrows():
            lines.append(f"{row.get('symbol')} - {row.get('timeframe')} - {row.get('profile')}")

    return "\n".join(lines)

    def build_ml_dataset_preview_report(
        self,
        symbol: str,
        timeframe: str,
        profile_name: str,
        summary: dict,
        tail_df: pd.DataFrame | None = None
    ) -> str:
        lines = [
            f"=== ML DATASET PREVIEW: {symbol} ({timeframe}) ===",
            f"Profile: {profile_name}",
            f"Dataset ID: {summary.get('dataset_id', 'N/A')}",
            f"Row Count: {summary.get('row_count', 0)}",
            f"Feature Count: {summary.get('feature_count', 0)}",
            f"Target Count: {summary.get('target_count', 0)}",
            "",
            "--- Quality ---",
            f"Quality Passed: {summary.get('quality_report', {}).get('passed', False)}",
            f"Feature NaN Ratio: {summary.get('quality_report', {}).get('feature_nan_ratio', 0.0):.2f}",
            f"Target NaN Ratio: {summary.get('quality_report', {}).get('target_nan_ratio', 0.0):.2f}",
            "",
            "--- Leakage Audit ---",
            f"Audit Passed: {summary.get('leakage_audit', {}).get('passed', False)}",
            f"Risk Score: {summary.get('leakage_audit', {}).get('leakage_risk_score', 0)}",
            "",
            "--- Missing Feature Sets ---",
            str(summary.get('missing_feature_sets', [])),
            "",
            "--- Warnings ---"
        ]

        warnings = summary.get("warnings", [])
        if warnings:
             for w in warnings:
                  lines.append(f"- {w}")
        else:
             lines.append("- Yok")

        lines.append("")
        lines.append("Uyarı: Bu çıktı ML dataset hazırlık raporudur. Model eğitimi, tahmin, canlı sinyal, gerçek emir veya yatırım tavsiyesi değildir.")

        if tail_df is not None and not tail_df.empty:
            lines.append("")
            lines.append("--- Tail Data ---")
            lines.append(tail_df.to_string())

        return "\n".join(lines)

    def build_ml_target_preview_report(
        self,
        symbol: str,
        timeframe: str,
        profile_name: str,
        summary: dict,
        target_tail_df: pd.DataFrame | None = None
    ) -> str:
        lines = [
            f"=== ML TARGET PREVIEW: {symbol} ({timeframe}) ===",
            f"Profile: {profile_name}",
            ""
        ]

        warnings = summary.get("warnings", [])
        if warnings:
             lines.append("--- Warnings ---")
             for w in warnings:
                  lines.append(f"- {w}")
             lines.append("")

        lines.append("Uyarı: Bu çıktı ML dataset hazırlık raporudur. Model eğitimi, tahmin, canlı sinyal, gerçek emir veya yatırım tavsiyesi değildir.")
        lines.append("")

        if target_tail_df is not None and not target_tail_df.empty:
            lines.append("--- Target Data Tail ---")
            lines.append(target_tail_df.to_string())

        return "\n".join(lines)

    def build_ml_dataset_batch_report(self, summary: dict, ranking_df: pd.DataFrame | None = None) -> str:
        lines = [
            "=== ML DATASET BATCH BUILD SUMMARY ===",
            f"Total Processed: {summary.get('processed', 0)}",
            "",
            "Uyarı: Bu çıktı ML dataset hazırlık raporudur. Model eğitimi, tahmin, canlı sinyal, gerçek emir veya yatırım tavsiyesi değildir.",
            ""
        ]

        if ranking_df is not None and not ranking_df.empty:
             lines.append("--- Dataset Ranking ---")
             lines.append(ranking_df.to_string(index=False))

        return "\n".join(lines)

    def build_ml_dataset_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        lines = [
            "=== ML DATASET STATUS ===",
            f"Total Datasets: {len(status_df) if not status_df.empty else 0}",
            "",
            "Uyarı: Bu çıktı ML dataset hazırlık raporudur. Model eğitimi, tahmin, canlı sinyal, gerçek emir veya yatırım tavsiyesi değildir.",
            ""
        ]

        if not status_df.empty:
            lines.append("--- Current Datasets ---")
            display_cols = ["symbol", "timeframe", "profile", "row_count", "feature_count", "target_count", "quality_passed", "leakage_audit_passed"]
            avail_cols = [c for c in display_cols if c in status_df.columns]
            if avail_cols:
                 lines.append(status_df[avail_cols].to_string(index=False))
            else:
                 lines.append(status_df.to_string(index=False))

        return "\n".join(lines)

def build_ml_training_preview_report(symbol: str, timeframe: str, profile_name: str, summary: dict) -> str:
    lines = [
        "=== ML TRAINING PREVIEW ===",
        f"Sembol: {symbol}",
        f"Zaman Dilimi: {timeframe}",
        f"Profil: {profile_name}",
        "",
        "Uyarı: Bu çıktı offline ML eğitim raporudur. Canlı tahmin, canlı sinyal, gerçek emir, broker talimatı veya yatırım tavsiyesi değildir.",
        "",
        "Model Bilgileri:",
        f"  Model ID: {summary.get('model_id')}",
        f"  Model Family: {summary.get('model_family')}",
        f"  Task Type: {summary.get('task_type')}",
        f"  Target: {summary.get('target_column')}",
        f"  Feature Count: {summary.get('feature_count')}",
        f"  Train Rows: {summary.get('train_rows')}",
        f"  Test Rows: {summary.get('test_rows')}",
        "",
        "Metrics:",
    ]

    metrics = summary.get('metrics', {})
    for k, v in metrics.items():
        if isinstance(v, float):
            lines.append(f"  {k}: {v:.4f}")
        else:
            lines.append(f"  {k}: {v}")

    lines.append("")
    lines.append("Quality Status:")
    quality = summary.get('quality_report', {})
    lines.append(f"  Passed: {quality.get('passed', False)}")

    if quality.get('warnings'):
        lines.append("  Warnings:")
        for w in quality['warnings']:
            lines.append(f"    - {w}")

    lines.append("")
    lines.append(f"Registry Status: {summary.get('registry_entry', {}).get('registry_status', 'unknown')}")

    return "\n".join(lines)

def build_ml_model_evaluation_preview_report(symbol: str, timeframe: str, profile_name: str, summary: dict) -> str:
    lines = [
        "=== ML MODEL EVALUATION PREVIEW ===",
        f"Sembol: {symbol}",
        f"Zaman Dilimi: {timeframe}",
        f"Profil: {profile_name}",
        "",
        "Uyarı: Bu çıktı offline ML değerlendirme raporudur. Canlı tahmin, canlı sinyal, gerçek emir, broker talimatı veya yatırım tavsiyesi değildir.",
        "",
    ]

    for k, v in summary.items():
        if k == "confusion_matrix" and isinstance(v, dict):
            lines.append("Confusion Matrix:")
            for k2, v2 in v.items():
                lines.append(f"  {k2}: {v2}")
        elif k == "classification_report" and isinstance(v, dict):
            lines.append("Classification Report (subset):")
            lines.append(f"  Accuracy: {v.get('accuracy', 'N/A')}")
        else:
            if isinstance(v, float):
                lines.append(f"{k}: {v:.4f}")
            else:
                lines.append(f"{k}: {v}")

    return "\n".join(lines)

def build_ml_training_batch_report(summary: dict, ranking_df=None) -> str:
    lines = [
        "=== ML BATCH TRAINING SUMMARY ===",
        f"Total Processed: {summary.get('processed', 0)}",
        "",
        "Uyarı: Bu çıktı offline ML eğitim raporudur. Canlı tahmin, canlı sinyal, gerçek emir, broker talimatı veya yatırım tavsiyesi değildir.",
        "",
    ]

    if ranking_df is not None and not ranking_df.empty:
        lines.append("Top Models:")
        lines.append(ranking_df.to_string())

    return "\n".join(lines)

def build_ml_model_registry_status_report(status_df, summary: dict) -> str:
    lines = [
        "=== ML MODEL REGISTRY STATUS ===",
        f"Total Registered Models: {len(status_df) if not status_df.empty else 0}",
        "",
        "Uyarı: Bu çıktı offline model registry raporudur. Canlı tahmin, canlı sinyal, gerçek emir, broker talimatı veya yatırım tavsiyesi değildir.",
        "",
    ]

    if not status_df.empty:
        cols = ['model_id', 'symbol', 'timeframe', 'model_family', 'registry_status']
        exist_cols = [c for c in cols if c in status_df.columns]
        if exist_cols:
            lines.append(status_df[exist_cols].to_string())

    return "\n".join(lines)

def build_ml_model_artifact_status_report(status_df, summary: dict) -> str:
    lines = [
        "=== ML MODEL ARTIFACT STATUS ===",
        f"Total Models Checked: {len(status_df) if not status_df.empty else 0}",
        "",
        "Uyarı: Bu çıktı offline model artifact raporudur. Canlı tahmin, canlı sinyal, gerçek emir, broker talimatı veya yatırım tavsiyesi değildir.",
        "",
    ]

    if not status_df.empty:
        lines.append(status_df.to_string())

    return "\n".join(lines)



# --- PHASE 32: ML CONTEXT INTEGRATION REPORTS ---

def build_ml_context_integration_preview_report(symbol: str, timeframe: str, profile_name: str, summary: dict) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append(f"ML CONTEXT INTEGRATION PREVIEW [{symbol} - {timeframe}]")
    lines.append("=" * 60)
    lines.append("DIKKAT: Bu cikti offline ML context entegrasyon raporudur.")
    lines.append("Model alignment, support/conflict veya model-aware score canli sinyal, gercek emir, broker talimati veya yatirim tavsiyesi degildir.")
    lines.append("-" * 60)

    lines.append(f"Profile: {profile_name}")
    lines.append(f"ML Context Available: {summary.get('ml_context_available', False)}")
    lines.append(f"Signal Alignment Rows: {summary.get('signal_alignment_rows', 0)}")
    lines.append(f"Decision Alignment Rows: {summary.get('decision_alignment_rows', 0)}")
    lines.append(f"Strategy Alignment Rows: {summary.get('strategy_alignment_rows', 0)}")
    lines.append(f"Conflict Rows: {summary.get('conflict_rows', 0)}")
    lines.append(f"High Conflict Count: {summary.get('high_conflict_count', 0)}")
    lines.append(f"High Uncertainty Count: {summary.get('high_uncertainty_count', 0)}")
    lines.append(f"Adjusted Layers: {', '.join(summary.get('adjustment_applied_layers', []))}")

    q = summary.get("quality_report", {})
    lines.append("-" * 60)
    lines.append("QUALITY REPORT")
    lines.append(f"Passed: {q.get('passed', False)}")
    lines.append(f"Coverage Ratio: {q.get('ml_context_coverage_ratio', 0.0):.2%}")
    lines.append(f"Invalid Scores: {q.get('invalid_score_count', 0)}")

    if q.get('warnings'):
        lines.append("\nWARNINGS:")
        for w in q['warnings']:
            lines.append(f"- {w}")

    if summary.get('warnings'):
        lines.append("\nPIPELINE WARNINGS:")
        for w in summary['warnings']:
            lines.append(f"- {w}")

    lines.append("=" * 60)
    return "\n".join(lines)


def build_model_alignment_preview_report(symbol: str, timeframe: str, profile_name: str, layer: str, summary: dict, tail_df=None) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append(f"MODEL ALIGNMENT PREVIEW [{symbol} - {timeframe} - {layer.upper()}]")
    lines.append("=" * 60)
    lines.append("DIKKAT: Bu cikti offline ML context entegrasyon raporudur.")
    lines.append("Model alignment canli sinyal, gercek emir, broker talimati veya yatirim tavsiyesi degildir.")
    lines.append("-" * 60)

    lines.append(f"Profile: {profile_name}")
    if tail_df is not None and not tail_df.empty:
        lines.append(f"Total alignment rows evaluated: {summary.get(f'{layer}_alignment_rows', len(tail_df))}")

        # Distributions
        if "alignment_label" in tail_df.columns:
            dist = tail_df["alignment_label"].value_counts().to_dict()
            lines.append("\nLabel Distribution (Tail):")
            for k, v in dist.items():
                lines.append(f"  {k}: {v}")

        lines.append("\nRecent Alignments:")
        cols = ["alignment_label", f"model_{layer}_alignment_score", "ml_support_score", "ml_conflict_score", "ml_uncertainty_penalty"]
        exist_cols = [c for c in cols if c in tail_df.columns]
        lines.append(tail_df[exist_cols].to_string())
    else:
        lines.append("No alignment data available.")

    lines.append("=" * 60)
    return "\n".join(lines)


def build_ml_conflict_filter_preview_report(symbol: str, timeframe: str, profile_name: str, layer: str, summary: dict, tail_df=None) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append(f"ML CONFLICT FILTER PREVIEW [{symbol} - {timeframe} - {layer.upper()}]")
    lines.append("=" * 60)
    lines.append("DIKKAT: Bu cikti offline ML context entegrasyon raporudur.")
    lines.append("Model conflict filter canli sinyal veya gercek emir yasagi degildir. Sadece bir arastirma uyarisi uretir.")
    lines.append("-" * 60)

    lines.append(f"Profile: {profile_name}")
    if tail_df is not None and not tail_df.empty:
        conflicts = tail_df[tail_df["conflict_score"] > 0]
        lines.append(f"High Conflict Count: {len(conflicts)}")

        if not conflicts.empty:
            lines.append("\nRecent Conflicts:")
            cols = ["candidate_directional_bias", "ml_predicted_direction", "conflict_score", "conflict_label", "blocking_candidate"]
            exist_cols = [c for c in cols if c in conflicts.columns]
            lines.append(conflicts[exist_cols].to_string())
        else:
            lines.append("No active conflicts in tail.")
    else:
        lines.append("No conflict data available.")

    lines.append("=" * 60)
    return "\n".join(lines)


def build_ml_integration_batch_report(summary: dict, ranking_df=None) -> str:
    lines = []
    lines.append("=" * 80)
    lines.append(f"ML INTEGRATION BATCH REPORT")
    lines.append("=" * 80)
    lines.append("DIKKAT: Bu cikti offline ML context entegrasyon raporudur.")
    lines.append("-" * 80)

    lines.append(f"Processed: {summary.get('processed', 0)}")
    lines.append(f"Timeframe: {summary.get('timeframe', '1d')}")
    lines.append(f"Profile: {summary.get('integration_profile', '')}")

    if ranking_df is not None and not ranking_df.empty:
        lines.append("\nSummary Table:")
        cols = ["symbol", "ml_context_available", "signal_alignment_rows", "high_conflict_count", "quality_passed"]
        exist_cols = [c for c in cols if c in ranking_df.columns]
        lines.append(ranking_df[exist_cols].to_string(index=False))

    lines.append("=" * 80)
    return "\n".join(lines)


def build_ml_integration_status_report(status_df=None, summary: dict=None) -> str:
    if summary is None:
        summary = {}
    lines = []
    lines.append("=" * 80)
    lines.append(f"ML INTEGRATION STATUS REPORT")
    lines.append("=" * 80)
    lines.append(f"Total files found: {summary.get('total_files', 0)}")

    if status_df is not None and not status_df.empty:
        agg = status_df.groupby(["symbol", "layer", "type"]).size().unstack(fill_value=0)
        lines.append("\nAggregation by Symbol/Layer:")
        lines.append(agg.to_string())
    else:
        lines.append("No ML Integration reports found in data lake.")

    lines.append("=" * 80)
    return "\n".join(lines)


    # --- Notifications Specific ---
def _add_notification_disclaimer(lines: list[str]):
        lines.append("\n--- UYARI ---")
        lines.append("Bu çıktı bildirim/raporlama sistemine aittir. Gerçek emir, canlı sinyal, broker talimatı veya yatırım tavsiyesi değildir.")
        lines.append("="*80)

def build_telegram_test_message_report(summary: dict) -> str:
        report_lines = ["="*80, "TELEGRAM TEST MESSAGE REPORT", "="*80]
        report_lines.append(f"Status: {summary.get('status', 'Unknown')}")
        report_lines.append(f"Details: {summary}")
        _add_notification_disclaimer(report_lines)
        return "\n".join(report_lines)

def build_telegram_paper_summary_report(summary: dict, message_text: str | None = None) -> str:
        report_lines = ["="*80, "TELEGRAM PAPER SUMMARY REPORT", "="*80]
        if message_text:
            report_lines.append("\n--- Generated Message ---")
            report_lines.append(message_text)
        report_lines.append("\n--- Summary Data ---")
        for k, v in summary.items():
            report_lines.append(f"{k}: {v}")
        _add_notification_disclaimer(report_lines)
        return "\n".join(report_lines)

def build_telegram_system_status_report(summary: dict, message_text: str | None = None) -> str:
        report_lines = ["="*80, "TELEGRAM SYSTEM STATUS REPORT", "="*80]
        if message_text:
            report_lines.append("\n--- Generated Message ---")
            report_lines.append(message_text)
        report_lines.append("\n--- Summary Data ---")
        for k, v in summary.items():
            report_lines.append(f"{k}: {v}")
        _add_notification_disclaimer(report_lines)
        return "\n".join(report_lines)

def build_telegram_daily_digest_report(summary: dict, message_text: str | None = None) -> str:
        report_lines = ["="*80, "TELEGRAM DAILY DIGEST REPORT", "="*80]
        if message_text:
            report_lines.append("\n--- Generated Message ---")
            report_lines.append(message_text)
        report_lines.append("\n--- Summary Data ---")
        for k, v in summary.items():
            report_lines.append(f"{k}: {v}")
        _add_notification_disclaimer(report_lines)
        return "\n".join(report_lines)

def build_telegram_quality_alerts_report(summary: dict, message_text: str | None = None) -> str:
        report_lines = ["="*80, "TELEGRAM QUALITY ALERTS REPORT", "="*80]
        if message_text:
            report_lines.append("\n--- Generated Message ---")
            report_lines.append(message_text)
        report_lines.append("\n--- Summary Data ---")
        for k, v in summary.items():
            report_lines.append(f"{k}: {v}")
        _add_notification_disclaimer(report_lines)
        return "\n".join(report_lines)

def build_notification_status_report(status_df, summary: dict) -> str:
        report_lines = ["="*80, "NOTIFICATION SYSTEM STATUS REPORT", "="*80]
        report_lines.append("\n--- System Summary ---")
        for k, v in summary.items():
            report_lines.append(f"{k}: {v}")

        if status_df is not None and not status_df.empty:
            report_lines.append("\n--- Recent Logs ---")
            report_lines.append(status_df.to_string())

        _add_notification_disclaimer(report_lines)
        return "\n".join(report_lines)
