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
