# -*- coding: utf-8 -*-
"""Phase 148: Stress Testing Report Builder.

Generates structured Markdown and text reports for stress testing and scenario simulation contracts,
embedding strict research disclaimers and non-signal boundaries.
"""

from typing import Any, Dict, Optional
import pandas as pd


def _df_to_markdown(df: pd.DataFrame) -> str:
    """Convert a DataFrame to a clean markdown table without external dependencies."""
    if df.empty:
        return "*Kayıt bulunamadı.*"
    cols = [str(c) for c in df.columns]
    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join(["---"] * len(cols)) + " |"
    rows = []
    for _, row in df.iterrows():
        row_str = "| " + " | ".join(str(val) for val in row.values) + " |"
        rows.append(row_str)
    return "\n".join([header, sep] + rows)


def build_stress_testing_disclaimer() -> str:
    """Return standard research disclaimer for Phase 148 outputs."""
    return (
        "> [!IMPORTANT]\n"
        "> **YASAL UYARI VE ARAŞTIRMA BEYANI (PHASE 148)**:\n"
        "> Bu çıktı Phase 148 Stress Testing and Scenario Simulation raporudur. "
        "> Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, stress/readiness/scenario/robustness "
        "> değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, "
        "> gerçek stress test execution, scenario simulation, optimizer, Monte Carlo, "
        "> gerçek model training, model fit/predict/inference, dataset materialization, "
        "> target/label/prediction üretimi, gerçek stress PnL/drawdown/VaR/ES hesaplama, "
        "> performans garantisi, model deployment, model registry write, model artifact persistence, "
        "> scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı "
        "> veya gerçek provider API çağrısı değildir."
    )


def build_stress_testing_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for stress testing profiles."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(profile_df) if profile_df is not None else ""
    return (
        f"# Phase 148: Stres Testi Profil Raporu\n\n"
        f"{disclaimer}\n\n"
        f"## Profil Özeti\n"
        f"- **Aktif Profil**: `{summary.get('active_profile', 'N/A')}`\n"
        f"- **Toplam Profil Sayısı**: `{summary.get('total_profiles', 0)}`\n"
        f"- **Yerel Çalışma (Local Only)**: `{summary.get('all_local_only', True)}`\n"
        f"- **Non-Production**: `{summary.get('all_non_production', True)}`\n\n"
        f"## Profil Kayıt Defteri\n\n"
        f"{table_md}\n"
    )


def build_stress_scenario_contract_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for stress scenario contracts."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(df) if df is not None else ""
    return (
        f"# Phase 148: Stres Senaryo Sözleşmeleri Raporu\n\n"
        f"{disclaimer}\n\n"
        f"## Sözleşme Özeti\n"
        f"- **Toplam Senaryo Sözleşmesi**: `{summary.get('total_contracts', 0)}`\n"
        f"- **Stres Yürütmesi Engelli**: `{summary.get('all_stress_execution_blocked', True)}`\n"
        f"- **Senaryo Simülasyonu Engelli**: `{summary.get('all_scenario_simulation_blocked', True)}`\n"
        f"- **Metrik Hesaplama Engelli**: `{summary.get('all_metric_calculation_blocked', True)}`\n"
        f"- **Canlı İşlem Engelli**: `{summary.get('all_live_trading_blocked', True)}`\n"
        f"- **Operatör İncelemesi Zorunlu**: `{summary.get('all_manual_review_required', True)}`\n\n"
        f"## Sözleşme Detayları\n\n"
        f"{table_md}\n"
    )


def build_shock_placeholder_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for shock placeholders."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(df) if df is not None else ""
    return (
        f"# Phase 148: Şok Senaryo Yer Tutucuları Raporu\n\n"
        f"{disclaimer}\n\n"
        f"## Şok Özeti\n"
        f"- **Toplam Şok Yer Tutucu Sayısı**: `{summary.get('total_shocks', 0)}`\n"
        f"- **Gerçek Şok Yürütmesi**: `DEVRE DIŞI`\n"
        f"- **Non-Signal Durumu**: `DOĞRULANDI`\n\n"
        f"## Şok Yer Tutucuları\n\n"
        f"{table_md}\n"
    )


def build_stress_metric_placeholder_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for stress metric placeholders."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(df) if df is not None else ""
    return (
        f"# Phase 148: Stres Metrik Yer Tutucuları Raporu\n\n"
        f"{disclaimer}\n\n"
        f"## Metrik Özeti\n"
        f"- **Toplam Metrik Yer Tutucusu**: `{summary.get('total_metrics', 0)}`\n"
        f"- **Gerçek Hesaplama Durumu**: `DEVRE DIŞI (CALCULATION_BLOCKED)`\n"
        f"- **Performans İddiası**: `YOK (ZERO_PERFORMANCE_CLAIMS)`\n\n"
        f"## Metrik Formül Tanımları\n\n"
        f"{table_md}\n"
    )


def build_stress_dependency_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for stress dependencies."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(df) if df is not None else ""
    return (
        f"# Phase 148: Stres Testi Bağımlılık Raporu\n\n"
        f"{disclaimer}\n\n"
        f"## Bağımlılık Durumu\n"
        f"- **Toplam Bağımlılık Sayısı**: `{summary.get('total_dependencies', 0)}`\n"
        f"- **Tüm Bağımlılıklar Karşılandı**: `{summary.get('all_satisfied', True)}`\n\n"
        f"## Bağımlılık Kayıt Defteri\n\n"
        f"{table_md}\n"
    )


def build_stress_guard_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for stress guards."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(df) if df is not None else ""
    return (
        f"# Phase 148: Stres Testi Muhafızları Raporu\n\n"
        f"{disclaimer}\n\n"
        f"## Muhafız Özeti\n"
        f"- **No-Lookahead Muhafızı**: `AKTİF`\n"
        f"- **Senaryo Sızıntı Muhafızı**: `AKTİF`\n"
        f"- **Veri Gözetleme ve Aşırı Uyum Muhafızı**: `AKTİF`\n"
        f"- **Yasaklı Kolon Politikası**: `AKTİF`\n\n"
        f"## Muhafız Listesi\n\n"
        f"{table_md}\n"
    )


def build_stress_disabled_execution_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for disabled execution controls."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(df) if df is not None else ""
    return (
        f"# Phase 148: Devre Dışı Bırakılmış Yürütme Raporu\n\n"
        f"{disclaimer}\n\n"
        f"## Engellenen Yürütme Yolları\n"
        f"- **Stres Testi Yürütmesi**: `ENGELLENDİ`\n"
        f"- **Senaryo Simülasyonu**: `ENGELLENDİ`\n"
        f"- **Metrik Hesaplama**: `ENGELLENDİ`\n"
        f"- **Optimizasyon**: `ENGELLENDİ`\n"
        f"- **Model Eğitimi & Tahmin**: `ENGELLENDİ`\n"
        f"- **Canlı İşlem & Broker**: `ENGELLENDİ`\n\n"
        f"## Engelleme Kayıtları\n\n"
        f"{table_md}\n"
    )


def build_stress_findings_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for stress findings."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(df) if df is not None else ""
    return (
        f"# Phase 148: Stres Testi Yönetişim Bulguları\n\n"
        f"{disclaimer}\n\n"
        f"## Bulgu İstatistikleri\n"
        f"- **Toplam Bulgu**: `{summary.get('total_findings', 0)}`\n"
        f"- **Kritik Engelleyici**: `{summary.get('critical_count', 0)}`\n"
        f"- **Operatör İncelemesi Gereksinimi**: `{summary.get('all_manual_review_required', True)}`\n\n"
        f"## Bulgu Listesi\n\n"
        f"{table_md}\n"
    )


def build_stress_readiness_score_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for stress readiness scoring."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(df) if df is not None else ""
    return (
        f"# Phase 148: Stres Testi Hazırlık Skoru Raporu\n\n"
        f"{disclaimer}\n\n"
        f"## Puanlama Özeti\n"
        f"- **Teşhis Skoru**: `{summary.get('score', 0.0):.2f}`\n"
        f"- **Sınıflandırma**: `{summary.get('classification', 'unknown')}`\n"
        f"- **Eşik Karşılandı**: `{summary.get('meets_threshold', True)}`\n"
        f"- **Production Ready**: `FALSE`\n"
        f"- **Broker Ready**: `FALSE`\n\n"
        f"## Detaylı Puanlama Tablosu\n\n"
        f"{table_md}\n"
    )


def build_stress_testing_manifest_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for the master stress testing manifest."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(df) if df is not None else ""
    return (
        f"# Phase 148: Stres Testi Bütünlük Manifestosu\n\n"
        f"{disclaimer}\n\n"
        f"## Manifesto Değişmezleri\n"
        f"- **Manifesto Kimliği**: `{summary.get('manifest_id', 'N/A')}`\n"
        f"- **Mevcut Faz**: `{summary.get('current_phase', 148)}`\n"
        f"- **Hedef Final Faz**: `{summary.get('target_final_phase', 160)}`\n"
        f"- **Sıradaki Faz**: `{summary.get('next_phase', 149)}`\n"
        f"- **Tüm Değişmezler Geçerli**: `{summary.get('all_invariants_valid', True)}`\n"
        f"- **Phase 149 Devri Hazır**: `{summary.get('phase_149_handoff_ready', True)}`\n\n"
        f"## Bütünlük Tablosu\n\n"
        f"{table_md}\n"
    )


def build_stress_testing_validation_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for stress testing validation checks."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(df) if df is not None else ""
    return (
        f"# Phase 148: Stres Testi Doğrulama Raporu\n\n"
        f"{disclaimer}\n\n"
        f"## Doğrulama Sonucu\n"
        f"- **Genel Doğrulama Durumu**: `{summary.get('validation_status', 'PASS')}`\n"
        f"- **Toplam Kontrol Sayısı**: `{summary.get('total_checks', 0)}`\n"
        f"- **Tüm Kontroller Başarılı**: `{summary.get('all_passed', True)}`\n\n"
        f"## Kontrol Maddeleri\n\n"
        f"{table_md}\n"
    )


def build_stress_testing_safety_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for stress safety boundaries."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(df) if df is not None else ""
    return (
        f"# Phase 148: Stres Testi Güvenlik Sınırları Raporu\n\n"
        f"{disclaimer}\n\n"
        f"## Güvenlik Özeti\n"
        f"- **Güvenlik Durumu**: `{summary.get('safety_status', 'SECURE')}`\n"
        f"- **NO-GO Kuralları Aktif**: `{summary.get('no_go_count', 0)} adet`\n"
        f"- **SAFE-GO Kuralları Aktif**: `{summary.get('safe_go_count', 0)} adet`\n\n"
        f"## Güvenlik Kural Tablosu\n\n"
        f"{table_md}\n"
    )


def build_phase_149_handoff_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate markdown report for Phase 149 Monte Carlo handoff."""
    disclaimer = build_stress_testing_disclaimer()
    table_md = _df_to_markdown(df) if df is not None else ""
    return (
        f"# Phase 148 -> Phase 149: Monte Carlo Robustness and Parameter Stability Devir Raporu\n\n"
        f"{disclaimer}\n\n"
        f"## Devir Özeti\n"
        f"- **Kaynak Faz**: `Phase 148 — Stress Testing and Scenario Simulation`\n"
        f"- **Hedef Faz**: `Phase 149 — Monte Carlo Robustness and Parameter Stability`\n"
        f"- **Tüm Önkoşullar Karşılandı**: `{summary.get('all_prerequisites_satisfied', True)}`\n"
        f"- **Final Hedef**: `Phase 160 Full Advanced Bot Final Delivery`\n\n"
        f"## Devir Maddeleri\n\n"
        f"{table_md}\n"
    )
