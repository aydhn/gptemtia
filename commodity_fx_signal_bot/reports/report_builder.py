"""
Report generation utilities.
"""

from pathlib import Path
from typing import List

import pandas as pd

from config.symbols import SymbolSpec
from data.universe_analyzer import SymbolReliabilityResult, UniverseAnalyzer



def _get_regression_disclaimer_rb() -> str:
    return (
        "*** WARNING / UYARI ***\n"
        "Bu çıktı offline scenario regression/deterministic replay raporudur. "
        "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        "otomatik trade onayı veya yatırım tavsiyesi değildir.\n"
        "***\n\n"
    )

def build_scenario_regression_registry_text_report(summary: dict, regression_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Scenario Regression Registry Report\n\n"
    txt += f"Total definitions: {summary.get('total_definitions', 0)}\n\n"
    if regression_df is not None and not regression_df.empty:
        txt += regression_df.head(10).to_string() + "\n"
    return txt

def build_golden_output_text_report(summary: dict, golden_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Golden Output Report\n\n"
    txt += f"Total golden outputs: {summary.get('total_golden_outputs', 0)}\n\n"
    if golden_df is not None and not golden_df.empty:
        txt += golden_df.head(10).to_string() + "\n"
    return txt

def build_snapshot_comparison_text_report(summary: dict, diff_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Snapshot Comparison Report\n\n"
    txt += f"Total diffs: {summary.get('total_diffs', 0)}\n\n"
    if diff_df is not None and not diff_df.empty:
        txt += diff_df.head(10).to_string() + "\n"
    return txt

def build_deterministic_replay_text_report(summary: dict, replay_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Deterministic Replay Report\n\n"
    txt += f"Total replays: {summary.get('total_replays', 0)}\n\n"
    if replay_df is not None and not replay_df.empty:
        txt += replay_df.head(10).to_string() + "\n"
    return txt

def build_demo_acceptance_text_report(summary: dict, acceptance_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Demo Acceptance Report\n\n"
    txt += f"Score: {summary.get('score', 0)}\n"
    txt += f"Label: {summary.get('label', 'unknown')}\n\n"
    if acceptance_df is not None and not acceptance_df.empty:
        txt += acceptance_df.to_string() + "\n"
    return txt

def build_scenario_regression_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Scenario Regression Status\n\n"
    if status_df is not None and not status_df.empty:
        txt += status_df.to_string() + "\n"
    return txt

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

# -------------------------------------------------------------------------
# Orchestration Reports
# -------------------------------------------------------------------------

def _get_orchestration_disclaimer() -> str:
    return "WARNING: Bu çıktı offline pipeline orchestration raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir."

def build_workflow_status_report(status_df: 'pd.DataFrame', summary: dict) -> str:
    """Build workflow status report."""
    lines = [
        "==================================================",
        " WORKFLOW STATUS REPORT",
        "==================================================",
        _get_orchestration_disclaimer(),
        "",
        f"Registered Jobs: {summary.get('registered_jobs_count', 0)}",
        f"Job Registry Valid: {summary.get('job_registry_valid', False)}",
        f"Workflow Templates: {summary.get('templates_count', 0)}",
        f"Template Registry Valid: {summary.get('template_registry_valid', False)}",
        f"Total Orchestration Runs: {summary.get('total_runs', 0)}",
        ""
    ]
    if status_df is not None and not status_df.empty:
        lines.append("Recent Runs:")
        lines.append(status_df.head(10).to_string(index=False))
    return "\n".join(lines)

def build_dependency_check_report(summary: dict, dependency_df: 'pd.DataFrame' = None) -> str:
    """Build dependency check report."""
    lines = [
        "==================================================",
        " DEPENDENCY CHECK REPORT",
        "==================================================",
        _get_orchestration_disclaimer(),
        "",
        f"Total Checks: {summary.get('total_checks', 0)}",
        f"Available: {summary.get('available_count', 0)}",
        f"Missing Required: {summary.get('missing_count', 0)}",
        f"Missing Optional: {summary.get('optional_missing_count', 0)}",
        ""
    ]
    if dependency_df is not None and not dependency_df.empty:
        lines.append("Dependency Details:")
        lines.append(dependency_df.to_string(index=False))
    return "\n".join(lines)

def build_pipeline_workflow_report(summary: dict, job_df: 'pd.DataFrame' = None) -> str:
    """Build pipeline workflow report."""
    lines = [
        "==================================================",
        " PIPELINE WORKFLOW REPORT",
        "==================================================",
        _get_orchestration_disclaimer(),
        "",
        f"Run ID: {summary.get('run_id', 'unknown')}",
        f"Status: {summary.get('status', 'unknown')}",
        f"Dry Run: {summary.get('dry_run', True)}",
        f"Total Jobs: {summary.get('total_jobs', 0)}",
        f"Success: {summary.get('success', 0)}",
        f"Failed: {summary.get('failed', 0)}",
        f"Skipped: {summary.get('skipped', 0)}",
        ""
    ]
    if job_df is not None and not job_df.empty:
        lines.append("Job Execution Results:")
        lines.append(job_df.to_string(index=False))
    return "\n".join(lines)

def build_full_research_workflow_report(summary: dict, job_df: 'pd.DataFrame' = None) -> str:
    """Build full research workflow report."""
    return build_pipeline_workflow_report(summary, job_df).replace("PIPELINE WORKFLOW", "FULL RESEARCH WORKFLOW")

def build_daily_research_workflow_report(summary: dict, job_df: 'pd.DataFrame' = None) -> str:
    """Build daily research workflow report."""
    return build_pipeline_workflow_report(summary, job_df).replace("PIPELINE WORKFLOW", "DAILY RESEARCH WORKFLOW")

def build_paper_reporting_workflow_report(summary: dict, job_df: 'pd.DataFrame' = None) -> str:
    """Build paper reporting workflow report."""
    return build_pipeline_workflow_report(summary, job_df).replace("PIPELINE WORKFLOW", "PAPER REPORTING WORKFLOW")

def build_failed_jobs_report(summary: dict, failed_df: 'pd.DataFrame' = None) -> str:
    """Build failed jobs report."""
    lines = [
        "==================================================",
        " FAILED JOBS REPORT",
        "==================================================",
        _get_orchestration_disclaimer(),
        "",
        f"Failed Jobs Found: {summary.get('failed_count', 0)}",
        f"Blocked Jobs Found: {summary.get('blocked_count', 0)}",
        ""
    ]

    retry_plan = summary.get('retry_plan', {})
    if retry_plan:
        lines.append(f"Retry Policy Enabled: {retry_plan.get('policy_enabled', False)}")
        lines.append(f"Retry Candidates: {retry_plan.get('candidate_count', 0)}")
        lines.append("")

    if failed_df is not None and not failed_df.empty:
        lines.append("Failed Job Details:")
        lines.append(failed_df.to_string(index=False))
    return "\n".join(lines)

# --- Phase 36: Observability Reports ---
def build_system_healthcheck_report(health_df: pd.DataFrame, summary: dict) -> str:
    """Build a text summary report of the system health."""
    lines = [
        "SİSTEM SAĞLIK KONTROLÜ RAPORU",
        "=============================",
        "Bu çıktı sistem sağlık/observability raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.",
        "",
        f"Genel Durum: {summary.get('overall_status', 'unknown')}",
        f"Genel Skor: {summary.get('overall_score', 0.0):.2f}",
        f"Geçen Kontrol Sayısı: {summary.get('total_checks_passed', 0)}",
        f"Başarısız Kontrol Sayısı: {summary.get('total_checks_failed', 0)}",
        ""
    ]

    if not health_df.empty:
        lines.append("Bileşen Detayları:")
        lines.append("-" * 30)
        for _, row in health_df.iterrows():
            lines.append(f"{row['component'].upper()}: {row['status']} (Skor: {row['health_score']:.2f})")
            if row.get('errors_count', 0) > 0:
                lines.append(f"  Hatalar: {row['errors_count']}")
            if row.get('warnings_count', 0) > 0:
                lines.append(f"  Uyarılar: {row['warnings_count']}")

    return "\n".join(lines)

def build_component_healthcheck_report(health_df: pd.DataFrame, summary: dict) -> str:
    """Build a text summary report of component health."""
    lines = [
        "BİLEŞEN SAĞLIK KONTROLÜ RAPORU",
        "==============================",
        "Bu çıktı sistem sağlık/observability raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.",
        "",
        f"Genel Durum: {summary.get('overall_status', 'unknown')}",
        f"Genel Skor: {summary.get('overall_score', 0.0):.2f}",
        f"Kontrol Edilen Bileşen Sayısı: {summary.get('components_checked', 0)}",
        f"Kritik Bileşen Sayısı: {summary.get('critical_components', 0)}",
        ""
    ]

    if not health_df.empty:
        for _, row in health_df.iterrows():
            lines.append(f"{row['component']}: {row['status']} ({row['health_score']:.2f})")

    return "\n".join(lines)

def build_data_freshness_report(freshness_df: pd.DataFrame, summary: dict) -> str:
    """Build a text summary report of data freshness."""
    lines = [
        "VERİ TAZELİĞİ (FRESHNESS) RAPORU",
        "================================",
        "Bu çıktı sistem sağlık/observability raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.",
        "",
        f"Genel Durum: {summary.get('status', 'unknown')}",
        f"Kontrol Edilen Artifact Sayısı: {summary.get('total_artifacts_checked', 0)}",
        f"Eksik Artifact Sayısı: {summary.get('missing_count', 0)}",
        f"Stale (Eski) Artifact Sayısı: {summary.get('stale_count', 0)}",
        f"Taze Artifact Sayısı: {summary.get('fresh_count', 0)}",
        f"Ortalama Yaş (Saat): {summary.get('avg_age_hours', 0.0):.1f}",
        ""
    ]

    if not freshness_df.empty and 'stale' in freshness_df.columns:
        stale_df = freshness_df[freshness_df['stale'] == True]
        if not stale_df.empty:
            lines.append("Stale (Eski) Artifact Detayları:")
            lines.append("-" * 30)
            for _, row in stale_df.iterrows():
                lines.append(f"{row.get('symbol', 'unknown')} - {row.get('artifact_type', 'unknown')}: {row.get('age_hours', 'N/A')} saat")

    return "\n".join(lines)

def build_artifact_integrity_report(integrity_df: pd.DataFrame, summary: dict) -> str:
    """Build a text summary report of artifact integrity."""
    lines = [
        "ARTIFACT BÜTÜNLÜĞÜ (INTEGRITY) RAPORU",
        "=====================================",
        "Bu çıktı sistem sağlık/observability raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.",
        "",
        f"Genel Durum: {summary.get('status', 'unknown')}",
        f"Kontrol Edilen Dosya Sayısı: {summary.get('total_checked', 0)}",
        f"Geçerli (Valid) Dosya Sayısı: {summary.get('valid_count', 0)}",
        f"Geçersiz/Bozuk (Invalid) Dosya Sayısı: {summary.get('invalid_count', 0)}",
        f"Boş Dosya Sayısı: {summary.get('empty_count', 0)}",
        ""
    ]

    if not integrity_df.empty and 'valid' in integrity_df.columns:
        invalid_df = integrity_df[integrity_df['valid'] == False]
        if not invalid_df.empty:
            lines.append("Geçersiz/Bozuk Dosya Detayları:")
            lines.append("-" * 30)
            for _, row in invalid_df.iterrows():
                lines.append(f"{row['filename']}: {row.get('error', 'Bilinmeyen Hata')}")

    return "\n".join(lines)

def build_runtime_metrics_report(metrics_df: pd.DataFrame, summary: dict) -> str:
    """Build a text summary report of runtime metrics."""
    lines = [
        "ÇALIŞMA ZAMANI (RUNTIME METRICS) RAPORU",
        "=======================================",
        "Bu çıktı sistem sağlık/observability raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.",
        "",
        f"Toplam Kaydedilen Metrik: {summary.get('metric_count', 0)}",
        f"Toplam Süre (Sn): {summary.get('total_duration_seconds', 0.0):.2f}",
        f"Ortalama Süre (Sn): {summary.get('avg_duration_seconds', 0.0):.2f}",
        f"En Uzun Süre (Sn): {summary.get('max_duration_seconds', 0.0):.2f}",
        ""
    ]

    if 'by_component' in summary and summary['by_component']:
        lines.append("Bileşen Bazlı Ortalama Süreler:")
        lines.append("-" * 30)
        for comp, stats in summary['by_component'].items():
            lines.append(f"{comp}: {stats.get('mean', 0.0):.2f} sn (Adet: {stats.get('count', 0)})")
        lines.append("")

    if 'slowest_operations' in summary and summary['slowest_operations']:
        lines.append("En Yavaş 5 Operasyon:")
        lines.append("-" * 30)
        for op in summary['slowest_operations']:
            lines.append(f"{op.get('component')} - {op.get('operation')} ({op.get('symbol')}): {op.get('duration_seconds', 0.0):.2f} sn")

    return "\n".join(lines)

def build_error_taxonomy_report(error_df: pd.DataFrame, summary: dict) -> str:
    """Build a text summary of the error taxonomy."""
    lines = [
        "HATA TAKSONOMİSİ (ERROR TAXONOMY) RAPORU",
        "========================================",
        "Bu çıktı sistem sağlık/observability raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.",
        "",
        f"Tanımlı Hata Kodu Sayısı: {summary.get('total_errors_defined', 0)}",
        ""
    ]

    if 'by_category' in summary and summary['by_category']:
        lines.append("Kategori Dağılımı:")
        for cat, count in summary['by_category'].items():
            lines.append(f"  {cat}: {count}")
        lines.append("")

    if 'by_severity' in summary and summary['by_severity']:
        lines.append("Önem Derecesi (Severity) Dağılımı:")
        for sev, count in summary['by_severity'].items():
            lines.append(f"  {sev}: {count}")

    return "\n".join(lines)

def build_self_diagnostics_report(summary: dict) -> str:
    """Build a text summary of the self-diagnostics results."""
    lines = [
        "SİSTEM OTO-DİYAGNOSTİK (SELF DIAGNOSTICS) RAPORU",
        "================================================",
        "Bu çıktı sistem sağlık/observability raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.",
        "",
        f"Genel Sağlık Durumu: {summary.get('overall_health_status', 'unknown')}",
        f"Genel Sağlık Skoru: {summary.get('overall_health_score', 0.0):.2f}",
        f"Kritik Sorun Sayısı: {summary.get('critical_count', 0)}",
        f"Hata Sayısı: {summary.get('error_count', 0)}",
        f"Uyarı Sayısı: {summary.get('warning_count', 0)}",
        ""
    ]

    if summary.get('unhealthy_components'):
        lines.append("Sağlıksız Bileşenler:")
        for comp in summary['unhealthy_components']:
            lines.append(f"- {comp}")
        lines.append("")

    if summary.get('degraded_components'):
        lines.append("Performansı Düşük (Degraded) Bileşenler:")
        for comp in summary['degraded_components']:
            lines.append(f"- {comp}")
        lines.append("")

    if summary.get('recommended_system_actions'):
        lines.append("Önerilen Sistem Aksiyonları:")
        for action in summary['recommended_system_actions']:
            lines.append(f"- {action}")

    return "\n".join(lines)

def build_observability_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    """Build a text summary of the observability data lake status."""
    lines = [
        "OBSERVABILITY VERİ GÖLÜ DURUM RAPORU",
        "====================================",
        "Bu çıktı sistem sağlık/observability raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.",
        "",
        f"Zaman: {summary.get('timestamp', 'unknown')}",
        f"Bulunan Rapor Sayısı: {summary.get('reports_found', 0)}",
        ""
    ]

    if summary.get('report_types'):
        lines.append("Mevcut Rapor Türleri:")
        for rtype in summary['report_types']:
            lines.append(f"- {rtype}")

    return "\n".join(lines)

    # --- Phase 37: Security ---
    def build_security_audit_report(self, findings_df: pd.DataFrame, summary: dict) -> str:
        report = "SECURITY AUDIT REPORT\n"
        report += "Bu çıktı güvenlik/readiness denetim raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal, production deploy onayı veya yatırım tavsiyesi değildir.\n\n"
        report += f"Total Findings: {summary.get('total_findings', 0)}\n"
        return report
    def build_secret_hygiene_report(self, findings_df: pd.DataFrame, summary: dict) -> str:
        report = "SECRET HYGIENE REPORT\nBu çıktı güvenlik/readiness denetim raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal, production deploy onayı veya yatırım tavsiyesi değildir.\n\n"
        return report
    def build_config_hardening_report(self, findings_df: pd.DataFrame, summary: dict) -> str:
        report = "CONFIG HARDENING REPORT\nBu çıktı güvenlik/readiness denetim raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal, production deploy onayı veya yatırım tavsiyesi değildir.\n\n"
        return report
    def build_safe_defaults_report(self, findings_df: pd.DataFrame, summary: dict) -> str:
        report = "SAFE DEFAULTS REPORT\nBu çıktı güvenlik/readiness denetim raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal, production deploy onayı veya yatırım tavsiyesi değildir.\n\n"
        return report
    def build_permission_boundary_report(self, findings_df: pd.DataFrame, summary: dict) -> str:
        report = "PERMISSION BOUNDARY REPORT\nBu çıktı güvenlik/readiness denetim raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal, production deploy onayı veya yatırım tavsiyesi değildir.\n\n"
        return report
    def build_production_readiness_audit_report(self, readiness_df: pd.DataFrame, summary: dict) -> str:
        report = "PRODUCTION READINESS AUDIT REPORT\nBu çıktı güvenlik/readiness denetim raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal, production deploy onayı veya yatırım tavsiyesi değildir.\n\n"
        report += f"Readiness Score: {summary.get('readiness_score', 0.0)}\n"
        report += f"Readiness Label: {summary.get('readiness_label', 'unknown')}\n"
        return report
    def build_security_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        report = "SECURITY STATUS REPORT\nBu çıktı güvenlik/readiness denetim raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal, production deploy onayı veya yatırım tavsiyesi değildir.\n\n"
        return report

def build_cli_catalog_report(catalog_df: pd.DataFrame, summary: dict) -> str:
    msg = "Bu çıktı developer experience / repo bakım raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.\n\n"
    msg += f"Total Commands: {summary.get('total_commands', 0)}\n\n"
    if not catalog_df.empty:
        msg += catalog_df.to_string()
    return msg

def build_cli_help_audit_report(help_df: pd.DataFrame, summary: dict) -> str:
    msg = "Bu çıktı developer experience / repo bakım raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.\n\n"
    msg += f"Summary: {summary}\n\n"
    if not help_df.empty:
        msg += help_df.to_string()
    return msg

def build_import_smoke_test_report(import_df: pd.DataFrame, summary: dict) -> str:
    msg = "Bu çıktı developer experience / repo bakım raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.\n\n"
    msg += f"Summary: {summary}\n\n"
    if not import_df.empty:
        msg += import_df.to_string()
    return msg

def build_test_matrix_report(test_df: pd.DataFrame, summary: dict) -> str:
    msg = "Bu çıktı developer experience / repo bakım raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.\n\n"
    msg += f"Summary: {summary}\n\n"
    if not test_df.empty:
        msg += test_df.to_string()
    return msg

def build_package_audit_report(findings_df: pd.DataFrame, summary: dict) -> str:
    msg = "Bu çıktı developer experience / repo bakım raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.\n\n"
    msg += f"Summary: {summary}\n\n"
    if not findings_df.empty:
        msg += findings_df.to_string()
    return msg

def build_repo_hygiene_report(findings_df: pd.DataFrame, summary: dict) -> str:
    msg = "Bu çıktı developer experience / repo bakım raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.\n\n"
    msg += f"Summary: {summary}\n\n"
    if not findings_df.empty:
        msg += findings_df.to_string()
    return msg

def build_docs_audit_report(findings_df: pd.DataFrame, summary: dict) -> str:
    msg = "Bu çıktı developer experience / repo bakım raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.\n\n"
    msg += f"Summary: {summary}\n\n"
    if not findings_df.empty:
        msg += findings_df.to_string()
    return msg

def build_dx_quality_report(findings_df: pd.DataFrame, summary: dict) -> str:
    msg = "Bu çıktı developer experience / repo bakım raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.\n\n"
    msg += f"DX Summary: {summary}\n\n"
    if not findings_df.empty:
        msg += findings_df.to_string()
    return msg

def build_local_dev_check_report(summary: dict, findings_df: pd.DataFrame | None = None) -> str:
    msg = "Bu çıktı developer experience / repo bakım raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.\n\n"
    msg += f"Summary: {summary}\n\n"
    if findings_df is not None and not findings_df.empty:
        msg += findings_df.to_string()
    return msg


# Phase 39: Research Reports
def build_symbol_research_text_report(report, snapshot=None) -> str:
    lines = [
        f"Research Report: {report.title}",
        f"Profile: {report.profile_name} | Timeframe: {report.timeframe}",
        "--------------------------------------------------",
        report.markdown,
        "--------------------------------------------------",
        "Bu çıktı offline araştırma/simülasyon raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir."
    ]
    return "\n".join(lines)

def build_universe_research_text_report(report, ranking_df=None) -> str:
    lines = [
        f"Universe Research Report: {report.title}",
        f"Profile: {report.profile_name} | Timeframe: {report.timeframe}",
        "--------------------------------------------------",
        report.markdown,
        "--------------------------------------------------",
        "Bu çıktı offline araştırma/simülasyon raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir."
    ]
    return "\n".join(lines)

def build_daily_research_digest_text_report(report, ranking_df=None) -> str:
    lines = [
        f"Daily Research Digest: {report.title}",
        f"Profile: {report.profile_name} | Timeframe: {report.timeframe}",
        "--------------------------------------------------",
        report.markdown,
        "--------------------------------------------------",
        "Bu çıktı offline araştırma/simülasyon raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir."
    ]
    return "\n".join(lines)

def build_research_ranking_text_report(ranking_df, summary: dict) -> str:
    lines = [
        "Research Ranking Report",
        "--------------------------------------------------",
    ]
    if not ranking_df.empty:
        lines.append(ranking_df.to_string(index=False))
    else:
         lines.append("No rankings available.")
    lines.append("--------------------------------------------------")
    lines.append("Bu çıktı offline araştırma/simülasyon raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.")
    return "\n".join(lines)

def build_research_report_status_report(status_df, summary: dict) -> str:
    lines = [
        "Research Report Status",
        "--------------------------------------------------",
    ]
    if not status_df.empty:
         lines.append(status_df.to_string(index=False))
    else:
         lines.append("No status available.")
    lines.append("--------------------------------------------------")
    lines.append("Bu çıktı offline araştırma/simülasyon raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.")
    return "\n".join(lines)


def build_regime_portfolio_text_report(summary: dict, tables: dict[str, pd.DataFrame] | None = None) -> str:
    """Builds regime portfolio text report."""
    report = "REGIME-AWARE PORTFOLIO RESEARCH REPORT\n"
    report += "=" * 50 + "\n"
    report += "UYARI: Bu çıktı offline rejim bazlı portföy araştırması/sanal stres testi raporudur. Gerçek allocation, canlı emir, broker talimatı, gerçek pozisyon veya yatırım tavsiyesi değildir.\n\n"
    report += f"Profile: {summary.get('profile', 'Unknown')}\n\n"
    return report

def build_macro_scenario_sensitivity_text_report(summary: dict, sensitivity_df: pd.DataFrame | None = None) -> str:
    """Builds macro scenario sensitivity text report."""
    report = "MACRO SCENARIO SENSITIVITY REPORT\n"
    report += "=" * 50 + "\n"
    report += "UYARI: Bu çıktı offline rejim bazlı portföy araştırması/sanal stres testi raporudur. Gerçek allocation, canlı emir, broker talimatı, gerçek pozisyon veya yatırım tavsiyesi değildir.\n\n"
    return report

def build_basket_stress_test_text_report(summary: dict, stress_df: pd.DataFrame | None = None) -> str:
    """Builds basket stress test text report."""
    report = "BASKET STRESS TEST REPORT\n"
    report += "=" * 50 + "\n"
    report += "UYARI: Bu çıktı offline rejim bazlı portföy araştırması/sanal stres testi raporudur. Gerçek allocation, canlı emir, broker talimatı, gerçek pozisyon veya yatırım tavsiyesi değildir.\n\n"
    return report

def build_drawdown_cluster_text_report(summary: dict, cluster_df: pd.DataFrame | None = None, recovery_df: pd.DataFrame | None = None) -> str:
    """Builds drawdown cluster text report."""
    report = "DRAWDOWN CLUSTER REPORT\n"
    report += "=" * 50 + "\n"
    report += "UYARI: Bu çıktı offline rejim bazlı portföy araştırması/sanal stres testi raporudur. Gerçek allocation, canlı emir, broker talimatı, gerçek pozisyon veya yatırım tavsiyesi değildir.\n\n"
    return report

def build_risk_regime_exposure_text_report(summary: dict, exposure_df: pd.DataFrame | None = None) -> str:
    """Builds risk regime exposure text report."""
    report = "RISK REGIME EXPOSURE REPORT\n"
    report += "=" * 50 + "\n"
    report += "UYARI: Bu çıktı offline rejim bazlı portföy araştırması/sanal stres testi raporudur. Gerçek allocation, canlı emir, broker talimatı, gerçek pozisyon veya yatırım tavsiyesi değildir.\n\n"
    return report

def build_portfolio_regime_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    """Builds portfolio regime status text report."""
    report = "PORTFOLIO REGIME STATUS REPORT\n"
    report += "=" * 50 + "\n"
    report += "UYARI: Bu çıktı offline rejim bazlı portföy araştırması/sanal stres testi raporudur. Gerçek allocation, canlı emir, broker talimatı, gerçek pozisyon veya yatırım tavsiyesi değildir.\n\n"
    return report


def build_synthetic_benchmark_text_report(summary: dict, definitions_df: pd.DataFrame | None = None) -> str:
    from synthetic_indices.index_report_builder import build_synthetic_index_disclaimer
    lines = ["SYNTHETIC BENCHMARK REPORT", "=" * 30, ""]
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    for k, v in summary.items():
        if k != "warnings":
            lines.append(f"{k}: {v}")
    if definitions_df is not None and not definitions_df.empty:
        lines.append("")
        lines.append(definitions_df.to_string())
    return "\n".join(lines)

def build_composite_index_text_report(summary: dict, performance_df: pd.DataFrame | None = None) -> str:
    from synthetic_indices.index_report_builder import build_synthetic_index_disclaimer
    lines = ["COMPOSITE INDEX PERFORMANCE REPORT", "=" * 40, ""]
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    for k, v in summary.items():
        if k != "warnings":
            lines.append(f"{k}: {v}")
    if performance_df is not None and not performance_df.empty:
        lines.append("")
        lines.append(performance_df.to_string())
    return "\n".join(lines)

def build_relative_strength_text_report(summary: dict, rs_df: pd.DataFrame | None = None) -> str:
    from synthetic_indices.index_report_builder import build_synthetic_index_disclaimer
    lines = ["RELATIVE STRENGTH REPORT", "=" * 30, ""]
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    if rs_df is not None and not rs_df.empty:
        lines.append(rs_df.to_string())
    return "\n".join(lines)

def build_universe_rotation_text_report(summary: dict, rotation_df: pd.DataFrame | None = None) -> str:
    from synthetic_indices.index_report_builder import build_synthetic_index_disclaimer
    lines = ["UNIVERSE ROTATION REPORT", "=" * 30, ""]
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    for k, v in summary.items():
        if k != "warnings":
            lines.append(f"{k}: {v}")
    if rotation_df is not None and not rotation_df.empty:
        lines.append("")
        lines.append(rotation_df.to_string())
    return "\n".join(lines)

def build_leadership_laggard_text_report(summary: dict, leader_laggard_df: pd.DataFrame | None = None) -> str:
    from synthetic_indices.index_report_builder import build_synthetic_index_disclaimer
    lines = ["LEADERSHIP AND LAGGARD REPORT", "=" * 30, ""]
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    for k, v in summary.items():
        if k != "warnings":
            lines.append(f"{k}: {v}")
    if leader_laggard_df is not None and not leader_laggard_df.empty:
        lines.append("")
        lines.append(leader_laggard_df.to_string())
    return "\n".join(lines)

def build_synthetic_index_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    from synthetic_indices.index_report_builder import build_synthetic_index_disclaimer
    lines = ["SYNTHETIC INDEX STATUS REPORT", "=" * 30, ""]
    lines.append(build_synthetic_index_disclaimer())
    lines.append("")
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if not status_df.empty:
        lines.append("")
        lines.append(status_df.to_string())


    # Phase 47 Governance Text Reports


def build_artifact_inventory_text_report(summary: dict, inventory_df=None) -> str:
    rep = "=== ARTIFACT INVENTORY REPORT ===\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\n\n"
    rep += f"Total Artifacts: {summary.get('total_artifacts', 0)}\n"
    rep += f"Total Size (MB): {summary.get('total_size_mb', 0):.2f}\n"
    rep += "\nTypes:\n"
    for t, c in summary.get("artifacts_by_type", {}).items():
        rep += f"- {t}: {c}\n"
    return rep

def build_lineage_graph_text_report(summary: dict, node_df=None, edge_df=None) -> str:
    rep = "=== LINEAGE GRAPH REPORT ===\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\n\n"
    rep += f"Nodes: {summary.get('node_count', 0)}\n"
    rep += f"Edges: {summary.get('edge_count', 0)}\n"
    cycles = summary.get("cycles", {})
    rep += f"Has Cycles: {cycles.get('has_cycles', False)}\n"
    return rep

def build_provenance_text_report(summary: dict, provenance_df=None) -> str:
    rep = "=== PROVENANCE REPORT ===\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\n\n"
    rep += f"Total Records: {summary.get('total_records', 0)}\n"
    rep += f"Unique Artifacts: {summary.get('unique_artifacts', 0)}\n"
    rep += "\nSources:\n"
    for s, c in summary.get("sources", {}).items():
        rep += f"- {s}: {c}\n"
    return rep

def build_dependency_trace_text_report(summary: dict, trace_df=None) -> str:
    rep = "=== DEPENDENCY TRACE REPORT ===\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\n\n"
    if summary.get("warnings"):
        rep += "Warnings:\n"
        for w in summary["warnings"]:
            rep += f"- {w}\n"
        rep += "\n"
    if trace_df is not None and not trace_df.empty:
        rep += f"Trace nodes found: {len(trace_df)}\n"
    else:
        rep += "No trace found.\n"
    return rep

def build_audit_trail_text_report(summary: dict, audit_df=None) -> str:
    rep = "=== AUDIT TRAIL REPORT ===\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\n\n"
    rep += f"Total Events: {summary.get('total_events', 0)}\n"
    rep += "\nEvent Types:\n"
    for t, c in summary.get("event_types", {}).items():
        rep += f"- {t}: {c}\n"
    return rep

def build_research_governance_text_report(summary: dict, checklist_df=None) -> str:
    rep = "=== RESEARCH GOVERNANCE REPORT ===\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\n\n"
    q = summary.get("quality", {})
    rep += f"Passed Governance: {q.get('passed', False)}\n"
    rep += f"Warning Count: {q.get('warning_count', 0)}\n"
    return rep

def build_governance_status_report(status_df=None, summary: dict=None) -> str:
    rep = "=== GOVERNANCE STATUS REPORT ===\n"
    rep += "Uyari: Bu cikti offline research governance/data lineage raporudur. Canli emir, broker talimati, gercek pozisyon, production compliance onayi veya yatirim tavsiyesi degildir.\n\n"
    if status_df is not None and not status_df.empty:
        rep += f"Files found: {len(status_df)}\n"
        for _, r in status_df.iterrows():
            rep += f"- {r.get('report_name', 'unknown')}: {r.get('path', 'unknown')}\n"
    else:
        rep += "No governance files found.\n"
    return rep


# Phase 48: Research Planning
def build_research_backlog_text_report(summary: dict, backlog_df: pd.DataFrame | None = None) -> str:
    from research_planning.planning_report_builder import build_research_planning_disclaimer
    text = "=== Research Backlog Report ===\n"
    text += build_research_planning_disclaimer()
    text += f"Total Tasks: {summary.get('total_tasks', 0)}\n"
    return text

def build_priority_scoring_text_report(summary: dict, priority_df: pd.DataFrame | None = None) -> str:
    from research_planning.planning_report_builder import build_research_planning_disclaimer
    text = "=== Priority Scoring Report ===\n"
    text += build_research_planning_disclaimer()
    text += f"Average Score: {summary.get('average_score', 0.0):.2f}\n"
    return text

def build_next_best_experiment_text_report(summary: dict, next_best_df: pd.DataFrame | None = None) -> str:
    from research_planning.planning_report_builder import build_research_planning_disclaimer
    text = "=== Next Best Experiment Report ===\n"
    text += build_research_planning_disclaimer()
    text += f"Total Recommendations: {summary.get('total', 0)}\n"
    return text

def build_research_debt_text_report(summary: dict, debt_df: pd.DataFrame | None = None) -> str:
    from research_planning.planning_report_builder import build_research_planning_disclaimer
    text = "=== Research Debt Report ===\n"
    text += build_research_planning_disclaimer()
    text += f"Total Debt Items: {summary.get('total_debt_items', 0)}\n"
    return text

def build_roadmap_health_text_report(summary: dict, roadmap_snapshot: dict | None = None) -> str:
    from research_planning.planning_report_builder import build_research_planning_disclaimer
    text = "=== Roadmap Health Report ===\n"
    text += build_research_planning_disclaimer()
    text += f"Status: {summary.get('roadmap_status', 'Unknown')}\n"
    text += f"Health Score: {summary.get('roadmap_health_score', 0.0):.2f}\n"
    return text

def build_research_planning_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    from research_planning.planning_report_builder import build_research_planning_disclaimer
    text = "=== Research Planning Status Report ===\n"
    text += build_research_planning_disclaimer()
    text += f"Total Files: {summary.get('total_files', 0)}\n"
    return text


# Phase 49: Knowledge Base & Analyst Workspace Text Reports

def _kb_disclaimer() -> str:
    return "\n--- \nBu çıktı offline knowledge base/analyst workspace raporudur. Canlı emir, broker talimatı, gerçek pozisyon, otomatik trade onayı veya yatırım tavsiyesi değildir."

def build_knowledge_index_text_report(summary: dict, documents_df: pd.DataFrame | None = None, chunks_df: pd.DataFrame | None = None) -> str:
    lines = ["*** KNOWLEDGE INDEX REPORT ***\n"]
    for k, v in summary.items():
        if isinstance(v, dict):
            lines.append(f"{k.upper()}:")
            for sub_k, sub_v in v.items():
                lines.append(f"  - {sub_k}: {sub_v}")
        else:
            lines.append(f"{k.upper()}: {v}")
    lines.append(_kb_disclaimer())
    return "\n".join(lines)

def build_research_query_text_report(summary: dict, results_df: pd.DataFrame | None = None) -> str:
    lines = ["*** RESEARCH QUERY REPORT ***\n"]
    for k, v in summary.items():
        lines.append(f"{k.upper()}: {v}")
    lines.append(_kb_disclaimer())
    return "\n".join(lines)

def build_symbol_memory_text_report(summary: dict, memory_card: dict | None = None) -> str:
    lines = ["*** SYMBOL MEMORY REPORT ***\n"]
    for k, v in summary.items():
        lines.append(f"{k.upper()}: {v}")

    if memory_card:
        lines.append("\nCARD DATA:")
        lines.append(f"Summary: {memory_card.get('summary', '')}")
        lines.append(f"Warnings: {len(memory_card.get('warnings', []))}")

    lines.append(_kb_disclaimer())
    return "\n".join(lines)

def build_decision_journal_text_report(summary: dict, journal_df: pd.DataFrame | None = None) -> str:
    lines = ["*** DECISION JOURNAL ***\n"]
    for k, v in summary.items():
        lines.append(f"{k.upper()}: {v}")
    lines.append(_kb_disclaimer())
    return "\n".join(lines)

def build_recent_findings_text_report(summary: dict, findings_df: pd.DataFrame | None = None) -> str:
    lines = ["*** RECENT FINDINGS DIGEST ***\n"]
    for k, v in summary.items():
        lines.append(f"{k.upper()}: {v}")
    lines.append(_kb_disclaimer())
    return "\n".join(lines)

def build_analyst_workspace_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = ["*** ANALYST WORKSPACE STATUS ***\n"]
    for k, v in summary.items():
        lines.append(f"{k.upper()}: {v}")
    lines.append(_kb_disclaimer())
    return "\n".join(lines)



def build_command_catalog_text_report(summary: dict, commands_df: pd.DataFrame | None = None) -> str:
    txt = "COMMAND CATALOG REPORT\n"
    txt += "=" * 40 + "\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\n\n"
    for k, v in summary.items():
        txt += f"{k}: {v}\n"
    txt += "\nCommands:\n"
    if commands_df is not None and not commands_df.empty:
        txt += commands_df.to_string(index=False)
    else:
        txt += "No commands found.\n"
    return txt

def build_guided_workflow_text_report(summary: dict, workflows_df: pd.DataFrame | None = None) -> str:
    txt = "GUIDED WORKFLOW REPORT\n"
    txt += "=" * 40 + "\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\n\n"
    for k, v in summary.items():
        txt += f"{k}: {v}\n"
    txt += "\nWorkflows:\n"
    if workflows_df is not None and not workflows_df.empty:
        txt += workflows_df.to_string(index=False)
    else:
        txt += "No workflows found.\n"
    return txt

def build_safe_runbook_text_report(summary: dict, runbooks_df: pd.DataFrame | None = None) -> str:
    txt = "SAFE RUNBOOK REPORT\n"
    txt += "=" * 40 + "\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\n\n"
    for k, v in summary.items():
        txt += f"{k}: {v}\n"
    txt += "\nRunbooks:\n"
    if runbooks_df is not None and not runbooks_df.empty:
        txt += runbooks_df.to_string(index=False)
    else:
        txt += "No runbooks found.\n"
    return txt

def build_project_status_text_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    txt = "PROJECT STATUS REPORT\n"
    txt += "=" * 40 + "\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\n\n"
    for k, v in summary.items():
        txt += f"{k}: {v}\n"
    txt += "\nModule Status:\n"
    if status_df is not None and not status_df.empty:
        txt += status_df.to_string(index=False)
    else:
        txt += "No status data found.\n"
    return txt

def build_project_consolidation_text_report(summary: dict, consolidation_df: pd.DataFrame | None = None) -> str:
    txt = "PROJECT CONSOLIDATION REPORT\n"
    txt += "=" * 40 + "\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\n\n"
    for k, v in summary.items():
        if isinstance(v, dict):
            txt += f"{k}:\n"
            for sub_k, sub_v in v.items():
                txt += f"  {sub_k}: {sub_v}\n"
        else:
            txt += f"{k}: {v}\n"
    txt += "\nConsolidation Details:\n"
    if consolidation_df is not None and not consolidation_df.empty:
        txt += consolidation_df.to_string(index=False)
    return txt

def build_analyst_command_query_text_report(summary: dict, result_df: pd.DataFrame | None = None) -> str:
    txt = "ANALYST COMMAND QUERY REPORT\n"
    txt += "=" * 40 + "\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\n\n"
    for k, v in summary.items():
        txt += f"{k}: {v}\n"
    txt += "\nSuggested Commands:\n"
    if result_df is not None and not result_df.empty:
        txt += result_df.to_string(index=False)
    else:
        txt += "No suggested commands found.\n"
    return txt

def build_command_center_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    txt = "COMMAND CENTER STATUS REPORT\n"
    txt += "=" * 40 + "\n"
    txt += "Bu cikti offline command center/project consolidation raporudur. Canli emir, broker talimati, gercek pozisyon, model deployment, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\n\n"
    for k, v in summary.items():
        txt += f"{k}: {v}\n"
    txt += "\nStatus:\n"
    if status_df is not None and not status_df.empty:
        txt += status_df.to_string(index=False)
    return txt

    def build_performance_profile_text_report(self, summary: dict, runtime_df: pd.DataFrame | None = None, memory_df: pd.DataFrame | None = None) -> str:
        from performance.performance_report_builder import build_performance_profile_markdown_report
        return build_performance_profile_markdown_report(summary, runtime_df, memory_df)

    def build_resource_budget_text_report(self, summary: dict, budget_df: pd.DataFrame | None = None, violation_df: pd.DataFrame | None = None) -> str:
        from performance.performance_report_builder import build_resource_budget_markdown_report
        return build_resource_budget_markdown_report(summary, budget_df, violation_df)

    def build_cache_strategy_text_report(self, summary: dict, cache_df: pd.DataFrame | None = None, policy_df: pd.DataFrame | None = None) -> str:
        from performance.performance_report_builder import build_cache_strategy_markdown_report
        return build_cache_strategy_markdown_report(summary, cache_df, policy_df)

    def build_large_run_stability_text_report(self, summary: dict, stability_df: pd.DataFrame | None = None) -> str:
        from performance.performance_report_builder import build_large_run_stability_markdown_report
        return build_large_run_stability_markdown_report(summary, stability_df)

    def build_runtime_optimization_text_report(self, summary: dict, recommendation_df: pd.DataFrame | None = None) -> str:
        from performance.performance_report_builder import build_runtime_optimization_markdown_report
        return build_runtime_optimization_markdown_report(summary, recommendation_df)

    def build_performance_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        from performance.performance_report_builder import build_performance_disclaimer
        txt = "Performance Status Report\n"
        txt += build_performance_disclaimer()
        for k, v in summary.items():
            txt += f"{k}: {v}\n"
        txt += "\nReports:\n"
        if not status_df.empty:
            txt += status_df.to_string(index=False)
        return txt


    # --- MAINTENANCE REPORTING ---
    def build_storage_inventory_text_report(self, summary: dict, inventory_df: pd.DataFrame | None = None) -> str:
        rep = "*** DISCLAIMER ***\n"
        rep += "Bu çıktı offline data retention/storage lifecycle maintenance raporudur. "
        rep += "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        rep += "otomatik trade onayı veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        rep += "dosyalar otomatik silinmez veya taşınmaz.\n"
        rep += "******************\n\n"
        rep += "STORAGE INVENTORY REPORT\n"
        rep += "========================\n\n"
        rep += f"Total Files: {summary.get('total_files', 0)}\n"
        rep += f"Total Size (Bytes): {summary.get('total_size_bytes', 0)}\n"
        rep += f"Protected Files: {summary.get('protected_files', 0)}\n"
        return rep

    def build_retention_policy_text_report(self, summary: dict, policies_df: pd.DataFrame | None = None) -> str:
        rep = "*** DISCLAIMER ***\n"
        rep += "Bu çıktı offline data retention/storage lifecycle maintenance raporudur. "
        rep += "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        rep += "otomatik trade onayı veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        rep += "dosyalar otomatik silinmez veya taşınmaz.\n"
        rep += "******************\n\n"
        rep += "RETENTION POLICIES REPORT\n"
        rep += "=========================\n\n"
        rep += f"Total Policies: {summary.get('total_policies', 0)}\n"
        return rep

    def build_cleanup_dry_run_text_report(self, summary: dict, cleanup_df: pd.DataFrame | None = None) -> str:
        rep = "*** DISCLAIMER ***\n"
        rep += "Bu çıktı offline data retention/storage lifecycle maintenance raporudur. "
        rep += "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        rep += "otomatik trade onayı veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        rep += "dosyalar otomatik silinmez veya taşınmaz.\n"
        rep += "******************\n\n"
        rep += "CLEANUP DRY-RUN REPORT\n"
        rep += "======================\n\n"
        rep += f"Cleanup Candidates: {summary.get('candidate_count', 0)}\n"
        rep += f"Reclaimable Storage (Bytes): {summary.get('reclaimable_bytes', 0)}\n"
        return rep

    def build_archive_dry_run_text_report(self, summary: dict, archive_df: pd.DataFrame | None = None) -> str:
        rep = "*** DISCLAIMER ***\n"
        rep += "Bu çıktı offline data retention/storage lifecycle maintenance raporudur. "
        rep += "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        rep += "otomatik trade onayı veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        rep += "dosyalar otomatik silinmez veya taşınmaz.\n"
        rep += "******************\n\n"
        rep += "ARCHIVE DRY-RUN REPORT\n"
        rep += "======================\n\n"
        rep += f"Archive Candidates: {summary.get('candidate_count', 0)}\n"
        rep += f"Total Archive Size (Bytes): {summary.get('total_size_bytes', 0)}\n"
        return rep

    def build_storage_lifecycle_text_report(self, summary: dict, health_df: pd.DataFrame | None = None) -> str:
        rep = "*** DISCLAIMER ***\n"
        rep += "Bu çıktı offline data retention/storage lifecycle maintenance raporudur. "
        rep += "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        rep += "otomatik trade onayı veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        rep += "dosyalar otomatik silinmez veya taşınmaz.\n"
        rep += "******************\n\n"
        rep += "STORAGE LIFECYCLE REPORT\n"
        rep += "========================\n\n"
        if "health" in summary:
            rep += f"Storage Pressure Score: {summary['health'].get('score', 0.0)}\n"
            rep += f"Health Label: {summary['health'].get('label', 'unknown')}\n"
        else:
            rep += f"Storage Pressure Score: {summary.get('score', 0.0)}\n"
            rep += f"Health Label: {summary.get('label', 'unknown')}\n"
        return rep

    def build_maintenance_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        rep = "*** DISCLAIMER ***\n"
        rep += "Bu çıktı offline data retention/storage lifecycle maintenance raporudur. "
        rep += "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        rep += "otomatik trade onayı veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        rep += "dosyalar otomatik silinmez veya taşınmaz.\n"
        rep += "******************\n\n"
        rep += "MAINTENANCE STATUS REPORT\n"
        rep += "=========================\n\n"
        rep += f"Status: {summary.get('status', 'OK')}\n"
        return rep

def build_documentation_pack_text_report(summary: dict, docs_df) -> str:
    lines = [
        "DOCUMENTATION PACK REPORT",
        "=" * 50,
        "UYARI: Bu çıktı offline/local documentation pack raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        "-" * 50,
        f"Profile: {summary.get('profile', 'Unknown')}",
        f"Quality Score: {summary.get('quality_score', 0.0):.2f}",
        "-" * 50
    ]
    if docs_df is not None and not docs_df.empty:
        for _, row in docs_df.iterrows():
            lines.append(f"{row['relative_path']}: {row['document_type']} ({row['status']})")
    return "\n".join(lines)

def build_documentation_quality_text_report(summary: dict, quality: dict | None = None) -> str:
    if quality is None:
         quality = {}
    lines = [
        "DOCUMENTATION QUALITY REPORT",
        "=" * 50,
        "UYARI: Bu çıktı offline/local documentation pack raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        "-" * 50,
        f"Status: {'PASSED' if quality.get('passed') else 'FAILED'}",
        f"Warnings: {quality.get('warning_count', 0)}",
        "-" * 50
    ]
    warnings = quality.get("warnings", [])
    if warnings:
        lines.append("Warnings Details:")
        for w in warnings:
             lines.append(f" - {w}")
    return "\n".join(lines)

def build_safe_usage_docs_text_report(summary: dict, safety_df) -> str:
    lines = [
        "SAFE USAGE DOCS REPORT",
        "=" * 50,
        "UYARI: Bu çıktı offline/local documentation pack raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        "-" * 50
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append(safety_df.to_string())
    return "\n".join(lines)

def build_script_reference_text_report(summary: dict, scripts_df) -> str:
    lines = [
        "SCRIPT REFERENCE REPORT",
        "=" * 50,
        "UYARI: Bu çıktı offline/local documentation pack raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        "-" * 50
    ]
    if scripts_df is not None and not scripts_df.empty:
        lines.append(scripts_df.to_string())
    return "\n".join(lines)

def build_output_reference_text_report(summary: dict, outputs_df) -> str:
    lines = [
        "OUTPUT REFERENCE REPORT",
        "=" * 50,
        "UYARI: Bu çıktı offline/local documentation pack raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        "-" * 50
    ]
    if outputs_df is not None and not outputs_df.empty:
        lines.append(outputs_df.to_string())
    return "\n".join(lines)

def build_documentation_status_report(status_df, summary: dict) -> str:
    lines = [
        "DOCUMENTATION STATUS REPORT",
        "=" * 50,
        "UYARI: Bu çıktı offline/local documentation pack raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        "-" * 50
    ]
    if status_df is not None and not status_df.empty:
        lines.append(status_df.to_string())
    return "\n".join(lines)


    # --- Analyst UX Text Reports ---
    @staticmethod
    def _build_ux_disclaimer() -> str:
        return "UYARI: Bu çıktı offline analyst UX/productivity raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir."

    @staticmethod
    def build_ux_alias_text_report(summary: dict, aliases_df: pd.DataFrame = None) -> str:
        lines = ["--- Command Alias Registry Report ---", "", ReportBuilder._build_ux_disclaimer(), ""]
        if aliases_df is not None and not aliases_df.empty:
            lines.append(aliases_df.to_string(index=False))
        return "\n".join(lines)

    @staticmethod
    def build_safe_command_suggestion_text_report(summary: dict, suggestions_df: pd.DataFrame = None) -> str:
        lines = ["--- Safe Command Suggestions Report ---", "", ReportBuilder._build_ux_disclaimer(), ""]
        if suggestions_df is not None and not suggestions_df.empty:
            lines.append(suggestions_df.to_string(index=False))
        return "\n".join(lines)

    @staticmethod
    def build_prompt_pack_text_report(summary: dict, prompts_df: pd.DataFrame = None) -> str:
        lines = ["--- Prompt Pack Report ---", "", ReportBuilder._build_ux_disclaimer(), ""]
        if prompts_df is not None and not prompts_df.empty:
            lines.append(prompts_df.to_string(index=False))
        return "\n".join(lines)

    @staticmethod
    def build_productivity_checklist_text_report(summary: dict, checklist_df: pd.DataFrame = None) -> str:
        lines = ["--- Productivity Checklist Report ---", "", ReportBuilder._build_ux_disclaimer(), ""]
        if checklist_df is not None and not checklist_df.empty:
            lines.append(checklist_df.to_string(index=False))
        return "\n".join(lines)

    @staticmethod
    def build_analyst_task_board_text_report(summary: dict, task_df: pd.DataFrame = None) -> str:
        lines = ["--- Analyst Task Board Report ---", "", ReportBuilder._build_ux_disclaimer(), ""]
        if task_df is not None and not task_df.empty:
            lines.append(task_df.to_string(index=False))
        return "\n".join(lines)

    @staticmethod
    def build_operator_productivity_status_report(status_df: pd.DataFrame, summary: dict) -> str:
        lines = ["--- Operator Productivity Status Report ---", "", ReportBuilder._build_ux_disclaimer(), ""]
        if status_df is not None and not status_df.empty:
            lines.append(status_df.to_string(index=False))
        return "\n".join(lines)

    # --- Final Review Text Reports ---
    @staticmethod
    def _build_final_review_disclaimer() -> str:
        return "DISCLAIMER: Bu çıktı offline final system review/release readiness dry-run raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production release, otomatik trade onayı veya yatırım tavsiyesi değildir."

    @staticmethod
    def build_final_system_review_text_report(summary: dict, audit_tables: Optional[Dict[str, pd.DataFrame]] = None) -> str:
        lines = ["--- Final System Review Report ---", "", ReportBuilder._build_final_review_disclaimer(), ""]
        lines.append(f"Passed: {summary.get('passed', False)}")
        if audit_tables:
            for name, df in audit_tables.items():
                lines.append(f"\n[{name.upper()}]")
                lines.append(df.to_string(index=False))
        return "\n".join(lines)

    @staticmethod
    def build_architecture_audit_text_report(summary: dict, audit_df: Optional[pd.DataFrame] = None) -> str:
        lines = ["--- Architecture Audit Report ---", "", ReportBuilder._build_final_review_disclaimer(), ""]
        if audit_df is not None and not audit_df.empty:
            lines.append(audit_df.to_string(index=False))
        return "\n".join(lines)

    @staticmethod
    def build_safety_audit_text_report(summary: dict, safety_df: Optional[pd.DataFrame] = None) -> str:
        lines = ["--- Safety Audit Report ---", "", ReportBuilder._build_final_review_disclaimer(), ""]
        lines.append(f"Passed: {summary.get('passed', False)}")
        lines.append(f"Critical Issues: {summary.get('critical_issues', 0)}")
        if safety_df is not None and not safety_df.empty:
            lines.append("\n" + safety_df.to_string(index=False))
        return "\n".join(lines)

    @staticmethod
    def build_offline_acceptance_text_report(summary: dict, acceptance_df: Optional[pd.DataFrame] = None) -> str:
        lines = ["--- Offline Acceptance Audit Report ---", "", ReportBuilder._build_final_review_disclaimer(), ""]
        if acceptance_df is not None and not acceptance_df.empty:
            lines.append(acceptance_df.to_string(index=False))
        return "\n".join(lines)

    @staticmethod
    def build_release_readiness_dry_run_text_report(summary: dict, dry_run_df: Optional[pd.DataFrame] = None) -> str:
        lines = ["--- Release Readiness Dry-Run Report ---", "", ReportBuilder._build_final_review_disclaimer(), ""]
        lines.append(f"Ready: {summary.get('is_ready', False)}")
        if dry_run_df is not None and not dry_run_df.empty:
            lines.append("\n" + dry_run_df.to_string(index=False))
        return "\n".join(lines)

    @staticmethod
    def build_final_consolidation_text_report(summary: dict, phase_df: Optional[pd.DataFrame] = None) -> str:
        lines = ["--- Final Consolidation Audit Report ---", "", ReportBuilder._build_final_review_disclaimer(), ""]
        if phase_df is not None and not phase_df.empty:
            lines.append(phase_df.to_string(index=False))
        return "\n".join(lines)

    @staticmethod
    def build_final_review_status_report(status_df: pd.DataFrame, summary: dict) -> str:
        lines = ["--- Final Review Status Report ---", "", ReportBuilder._build_final_review_disclaimer(), ""]
        lines.append(f"Passed: {summary.get('passed', False)}")
        if not status_df.empty:
            lines.append("\n" + status_df.to_string(index=False))
        return "\n".join(lines)




    # Report Summarization Support
    @staticmethod
    def build_report_summary_registry_text_report(summary: dict, inventory_df: "pd.DataFrame | None" = None) -> str:
        text = "REPORT SUMMARY REGISTRY\n"
        text += "Bu çıktı offline/local report summarization ve research briefing raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"
        text += f"Total Reports: {summary.get('total_reports', 0)}\n"
        return text

    @staticmethod
    def build_executive_summary_text_report(summary: dict, executive_text: "str | None" = None) -> str:
        text = "EXECUTIVE SUMMARY\n"
        text += "Bu çıktı offline/local report summarization ve research briefing raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"
        if executive_text:
            text += executive_text
        return text

    @staticmethod
    def build_analyst_brief_text_report(summary: dict, analyst_brief_text: "str | None" = None) -> str:
        text = "ANALYST BRIEF\n"
        text += "Bu çıktı offline/local report summarization ve research briefing raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"
        if analyst_brief_text:
            text += analyst_brief_text
        return text

    @staticmethod
    def build_weekly_offline_review_text_report(summary: dict, review_text: "str | None" = None) -> str:
        text = "WEEKLY OFFLINE REVIEW PACK\n"
        text += "Bu çıktı offline/local report summarization ve research briefing raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"
        if review_text:
            text += review_text
        return text

    @staticmethod
    def build_research_digest_text_report(summary: dict, cards_df: "pd.DataFrame | None" = None) -> str:
        text = "RESEARCH DIGEST\n"
        text += "Bu çıktı offline/local report summarization ve research briefing raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"
        text += f"Total Cards: {summary.get('total_cards', 0)}\n"
        return text

    @staticmethod
    def build_summary_quality_text_report(summary: dict, quality: "dict | None" = None) -> str:
        text = "SUMMARY QUALITY REPORT\n"
        text += "Bu çıktı offline/local report summarization ve research briefing raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"
        if quality:
            text += f"Passed: {quality.get('passed', False)}\n"
            text += f"Warnings: {quality.get('warning_count', 0)}\n"
        return text

    @staticmethod
    def build_briefing_status_report(status_df: "pd.DataFrame", summary: dict) -> str:
        text = "BRIEFING STATUS\n"
        text += "Bu çıktı offline/local report summarization ve research briefing raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"
        text += f"Status files checked: {len(status_df)}\n"
        return text


def build_scenario_registry_text_report(summary: dict, scenarios_df: pd.DataFrame = None) -> str:
    lines = [
        "SCENARIO REGISTRY REPORT",
        "------------------------",
        "Bu çıktı offline controlled research scenario/demo raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        f"Total Scenarios: {summary.get('total_scenarios', 0)}"
    ]
    if scenarios_df is not None and not scenarios_df.empty:
        lines.append("Scenarios:")
        # only add if columns exist
        cols = [c for c in ["scenario_name", "scenario_type"] if c in scenarios_df.columns]
        if cols:
            lines.append(scenarios_df[cols].to_string())
    return "\n".join(lines)

def build_sample_data_text_report(summary: dict, sample_df: pd.DataFrame = None) -> str:
    lines = [
        "SAMPLE DATA REPORT",
        "------------------",
        "Bu çıktı offline controlled research scenario/demo raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        f"Files Saved: {summary.get('files_saved', 0)}"
    ]
    if sample_df is not None and not sample_df.empty:
        lines.append("Series:")
        cols = [c for c in ["series_name", "synthetic"] if c in sample_df.columns]
        if cols:
            lines.append(sample_df[cols].to_string())
    return "\n".join(lines)

def build_scenario_dry_run_text_report(summary: dict, dry_run_df: pd.DataFrame = None) -> str:
    lines = [
        "SCENARIO DRY RUN REPORT",
        "-----------------------",
        "Bu çıktı offline controlled research scenario/demo raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        f"Total Runs: {summary.get('total_runs', 0)}",
        f"Passed Runs: {summary.get('passed_runs', summary.get('passed', 0))}"
    ]
    return "\n".join(lines)

def build_case_study_text_report(summary: dict, case_df: pd.DataFrame = None) -> str:
    lines = [
        "CASE STUDIES REPORT",
        "-------------------",
        "Bu çıktı offline controlled research scenario/demo raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        f"Total Case Studies: {summary.get('total', 0)}"
    ]
    return "\n".join(lines)

def build_demo_workflow_text_report(summary: dict, workflow_df: pd.DataFrame = None) -> str:
    lines = [
        "DEMO WORKFLOWS REPORT",
        "---------------------",
        "Bu çıktı offline controlled research scenario/demo raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        f"Total Packs: {summary.get('total_packs', 0)}"
    ]
    return "\n".join(lines)

def build_end_to_end_demo_text_report(summary: dict, plan_df: pd.DataFrame = None) -> str:
    lines = [
        "END-TO-END DEMO REPORT",
        "----------------------",
        "Bu çıktı offline controlled research scenario/demo raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        f"Total Steps: {summary.get('total_steps', 0)}"
    ]
    return "\n".join(lines)

def build_scenario_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = [
        "SCENARIO STATUS REPORT",
        "----------------------",
        "Bu çıktı offline controlled research scenario/demo raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.",
        f"Total Components: {summary.get('total_components', 0)}"
    ]
    if status_df is not None and not status_df.empty:
        lines.append("Components:")
        lines.append(status_df.to_string())
    return "\n".join(lines)


def build_project_state_inventory_text_report(summary: dict, inventory_df: pd.DataFrame | None = None) -> str:
    from backup_recovery.backup_report_builder import build_backup_disclaimer
    return build_backup_disclaimer() + "Project State Inventory Report\n\n" + str(summary)

def build_backup_manifest_text_report(summary: dict, manifest_json: dict | None = None) -> str:
    from backup_recovery.backup_report_builder import build_backup_disclaimer
    return build_backup_disclaimer() + "Backup Manifest Report\n\n" + str(summary)

def build_backup_dry_run_text_report(summary: dict, backup_plan_df: pd.DataFrame | None = None) -> str:
    from backup_recovery.backup_report_builder import build_backup_disclaimer
    return build_backup_disclaimer() + "Backup Dry-Run Plan Report\n\n" + str(summary)

def build_restore_dry_run_text_report(summary: dict, restore_plan_df: pd.DataFrame | None = None) -> str:
    from backup_recovery.backup_report_builder import build_backup_disclaimer
    return build_backup_disclaimer() + "Restore Dry-Run Plan Report\n\n" + str(summary)

def build_disaster_recovery_text_report(summary: dict, dr_manifest: dict | None = None) -> str:
    from backup_recovery.backup_report_builder import build_backup_disclaimer
    return build_backup_disclaimer() + "Disaster Recovery Manifest Report\n\n" + str(summary)

def build_restore_verification_text_report(summary: dict, verification_df: pd.DataFrame | None = None) -> str:
    from backup_recovery.backup_report_builder import build_backup_disclaimer
    return build_backup_disclaimer() + "Restore Verification Report\n\n" + str(summary)

def build_backup_quality_text_report(summary: dict, quality: dict | None = None) -> str:
    from backup_recovery.backup_report_builder import build_backup_disclaimer
    return build_backup_disclaimer() + "Backup Quality Report\n\n" + str(summary)

def build_backup_recovery_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    from backup_recovery.backup_report_builder import build_backup_disclaimer
    return build_backup_disclaimer() + "Backup Recovery Status Report\n\n" + str(summary)



# Phase 66: Local Knowledge Graph
def build_graph_disclaimer() -> str:
    return "Bu çıktı offline/local knowledge graph ve artifact relationship raporudur. Canlı emir, broker talimatı, gerçek pozisyon, external vector DB, cloud graph DB, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir."

def build_graph_node_edge_registry_text_report(summary: dict, node_df: pd.DataFrame | None = None, edge_df: pd.DataFrame | None = None) -> str:
    lines = ["# GRAPH NODE AND EDGE REGISTRY REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if node_df is not None:
        lines.append("\n## NODES\n" + node_df.head(100).to_string())
    if edge_df is not None:
        lines.append("\n## EDGES\n" + edge_df.head(100).to_string())
    return "\n".join(lines)

def build_artifact_relationship_graph_text_report(summary: dict, graph_df: pd.DataFrame | None = None) -> str:
    lines = ["# ARTIFACT RELATIONSHIP GRAPH REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if graph_df is not None:
        lines.append("\n## GRAPH\n" + graph_df.head(100).to_string())
    return "\n".join(lines)

def build_semantic_index_text_report(summary: dict, keyword_df: pd.DataFrame | None = None) -> str:
    lines = ["# LOCAL SEMANTIC KEYWORD INDEX REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if keyword_df is not None:
        lines.append("\n## INDEX\n" + keyword_df.head(100).to_string())
    return "\n".join(lines)

def build_relationship_query_text_report(summary: dict, results_df: pd.DataFrame | None = None) -> str:
    lines = ["# RELATIONSHIP QUERY REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if results_df is not None:
        lines.append("\n## RESULTS\n" + results_df.head(100).to_string())
    return "\n".join(lines)

def build_graph_analysis_text_report(summary: dict, centrality_df: pd.DataFrame | None = None, gap_df: pd.DataFrame | None = None) -> str:
    lines = ["# GRAPH ANALYSIS REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if centrality_df is not None:
        lines.append("\n## CENTRALITY\n" + centrality_df.head(100).to_string())
    if gap_df is not None:
        lines.append("\n## GAPS\n" + gap_df.head(100).to_string())
    return "\n".join(lines)

def build_graph_quality_text_report(summary: dict, quality: dict | None = None) -> str:
    lines = ["# GRAPH QUALITY REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if quality is not None:
        lines.append("\n## QUALITY\n")
        for k, v in quality.items():
            lines.append(f"{k}: {v}")
    return "\n".join(lines)

def build_graph_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = ["# GRAPH STATUS REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    lines.append("\n## STATUS\n" + status_df.to_string())
    return "\n".join(lines)

# Phase 67: Local Timeline
def build_project_event_registry_text_report(summary: dict, event_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Project Event Registry Report\n\n"
    txt += f"Total Events: {summary.get('total_events', 0)}\n\n"
    if event_df is not None and not event_df.empty:
        txt += event_df.head(20).to_string() + "\n"
    return txt

def build_phase_chronology_text_report(summary: dict, phase_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Phase Chronology Report\n\n"
    txt += f"Total Phases: {summary.get('total_phases', 0)}\n\n"
    if phase_df is not None and not phase_df.empty:
        txt += phase_df.to_string() + "\n"
    return txt

def build_artifact_evolution_text_report(summary: dict, evolution_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Artifact Evolution Report\n\n"
    txt += f"Total Artifacts: {summary.get('total_artifacts', 0)}\n\n"
    if evolution_df is not None and not evolution_df.empty:
        txt += evolution_df.head(20).to_string() + "\n"
    return txt

def build_change_history_digest_text_report(summary: dict, digest_text: str | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Change History Digest\n\n"
    if digest_text:
        txt += digest_text + "\n"
    return txt

def build_timeline_query_text_report(summary: dict, results_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Timeline Query Results\n\n"
    txt += f"Total Results: {summary.get('total_results', 0)}\n\n"
    if results_df is not None and not results_df.empty:
        txt += results_df.to_string() + "\n"
    return txt

def build_timeline_quality_text_report(summary: dict, quality: dict | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Timeline Quality Report\n\n"
    if quality:
        for k, v in quality.items():
            txt += f"- **{k}**: {v}\n"
    return txt

def build_timeline_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Timeline Status Report\n\n"
    if status_df is not None and not status_df.empty:
        txt += status_df.to_string() + "\n"
    return txt

    # --- Local Consistency Reports ---
    def build_consistency_check_registry_text_report(self, summary: dict, check_df: pd.DataFrame | None = None) -> str:
        return "Bu çıktı offline/local consistency ve system coherence raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik düzeltme, otomatik trade onayı veya yatırım tavsiyesi değildir.\n"

    def build_cross_layer_consistency_matrix_text_report(self, summary: dict, matrix_df: pd.DataFrame | None = None) -> str:
        return "Bu çıktı offline/local consistency ve system coherence raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik düzeltme, otomatik trade onayı veya yatırım tavsiyesi değildir.\n"

    def build_contradiction_detection_text_report(self, summary: dict, contradiction_df: pd.DataFrame | None = None) -> str:
        return "Bu çıktı offline/local consistency ve system coherence raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik düzeltme, otomatik trade onayı veya yatırım tavsiyesi değildir.\n"

    def build_stale_reconciliation_text_report(self, summary: dict, plan_df: pd.DataFrame | None = None) -> str:
        return "Bu çıktı offline/local consistency ve system coherence raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik düzeltme, otomatik trade onayı veya yatırım tavsiyesi değildir.\n"

    def build_system_coherence_text_report(self, summary: dict, score_df: pd.DataFrame | None = None, findings_df: pd.DataFrame | None = None) -> str:
        return "Bu çıktı offline/local consistency ve system coherence raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik düzeltme, otomatik trade onayı veya yatırım tavsiyesi değildir.\n"

    def build_consistency_quality_text_report(self, summary: dict, quality: dict | None = None) -> str:
        return "Bu çıktı offline/local consistency ve system coherence raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik düzeltme, otomatik trade onayı veya yatırım tavsiyesi değildir.\n"

    def build_consistency_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        return "Bu çıktı offline/local consistency ve system coherence raporudur. Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik düzeltme, otomatik trade onayı veya yatırım tavsiyesi değildir.\n"

# Phase 69: Local Readiness
def build_readiness_gate_registry_text_report(summary: dict, gate_df: pd.DataFrame | None = None) -> str:
    from local_readiness.readiness_report_builder import build_readiness_disclaimer
    txt = build_readiness_disclaimer()
    txt += "Readiness Gate Registry Report\n\n"
    txt += f"Total Gates: {summary.get('total_gates', 0)}\n"
    txt += f"Passed: {summary.get('passed_gates', 0)}\n"
    txt += f"Failed: {summary.get('failed_gates', 0)}\n\n"
    if gate_df is not None and not gate_df.empty:
        txt += gate_df.to_string() + "\n"
    return txt

def build_final_operator_checklist_text_report(summary: dict, checklist_df: pd.DataFrame | None = None) -> str:
    from local_readiness.readiness_report_builder import build_readiness_disclaimer
    txt = build_readiness_disclaimer()
    txt += "Final Operator Checklist Report\n\n"
    if checklist_df is not None and not checklist_df.empty:
        txt += checklist_df.to_string() + "\n"
    return txt

def build_readiness_reports_text_report(summary: dict, readiness_df: pd.DataFrame | None = None) -> str:
    from local_readiness.readiness_report_builder import build_readiness_disclaimer
    txt = build_readiness_disclaimer()
    txt += "Readiness Reports Summary\n\n"
    if readiness_df is not None and not readiness_df.empty:
        txt += readiness_df.to_string() + "\n"
    return txt

def build_handoff_package_manifest_text_report(summary: dict, manifest: dict | None = None) -> str:
    from local_readiness.readiness_report_builder import build_readiness_disclaimer
    import json
    txt = build_readiness_disclaimer()
    txt += "Handoff Package Manifest Report\n\n"
    if manifest:
        txt += json.dumps(manifest, indent=2) + "\n"
    return txt

def build_final_local_readiness_binder_text_report(summary: dict, binder_text: str | None = None) -> str:
    from local_readiness.readiness_report_builder import build_readiness_disclaimer
    txt = build_readiness_disclaimer()
    txt += "Final Local Readiness Binder Report\n\n"
    if binder_text:
        txt += binder_text + "\n"
    return txt

def build_readiness_quality_text_report(summary: dict, quality: dict | None = None) -> str:
    from local_readiness.readiness_report_builder import build_readiness_disclaimer
    import json
    txt = build_readiness_disclaimer()
    txt += "Readiness Quality Report\n\n"
    if quality:
        txt += json.dumps(quality, indent=2) + "\n"
    return txt

def build_readiness_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    from local_readiness.readiness_report_builder import build_readiness_disclaimer
    txt = build_readiness_disclaimer()
    txt += "Readiness Status Report\n\n"
    if status_df is not None and not status_df.empty:
        txt += status_df.to_string() + "\n"
    return txt
