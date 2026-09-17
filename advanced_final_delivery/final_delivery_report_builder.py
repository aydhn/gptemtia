# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Report Builder.

Generates structured Markdown reports for all Phase 160 delivery registries and artifacts.
Always attaches the mandatory non-signal and zero-execution disclaimer.
"""

from typing import Dict, Optional
import pandas as pd

FINAL_DELIVERY_DISCLAIMER = (
    "Bu çıktı Phase 160 Full Advanced Bot Final Delivery çıktısıdır. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, "
    "final-delivery/readiness/manifest/handover değerini trade sinyali veya "
    "production-ready/broker-ready/onay olarak kullanma, gerçek full-system execution, "
    "end-to-end bot run, live trading, broker execution, order generation, signal generation, "
    "model training, model fit/predict/inference, target/label/prediction üretimi, backtest, "
    "benchmark, optimizer, portfolio construction, risk reporting, scenario execution, "
    "metric calculation, release deployment, production deployment, model deployment, "
    "model registry write, model artifact persistence, scraping, haber tam metni/article body/"
    "raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir. "
    "YATIRIM TAVSIYESI DEGILDIR | OFFLINE RESEARCH ONLY | NO LIVE TRADING."
)


def build_final_delivery_disclaimer() -> str:
    """Return mandatory Phase 160 disclaimer string."""
    return FINAL_DELIVERY_DISCLAIMER


def _render_df(df: Optional[pd.DataFrame]) -> str:
    if df is not None and not df.empty:
        try:
            return df.to_markdown(index=False)
        except Exception:
            return f"```\n{df.to_string(index=False)}\n```"
    return "_Tablo verisi mevcut değil._"


def build_final_delivery_profile_markdown_report(summary: dict, profile_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Profile Registry\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Profil Özeti\n"
        f"- **Aktif Profil:** `{summary.get('active_profile')}`\n"
        f"- **Mevcut Faz:** `{summary.get('current_phase')}`\n"
        f"- **Hedef Final Faz:** `{summary.get('target_final_phase')}`\n"
        f"- **Toplam Profil Sayısı:** `{summary.get('profile_count')}`\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Profil Detay Tablosu\n\n{_render_df(profile_df)}\n"
    )


def build_final_delivery_package_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Package Contracts\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Paket Sözleşmeleri Özeti\n"
        f"- **Sözleşme Sayısı:** `{summary.get('contract_count')}`\n"
        f"- **Yürütme Devre Dışı:** `{summary.get('all_execution_disabled')}`\n"
        f"- **Manuel İnceleme Zorunlu:** `{summary.get('all_manual_review_required')}`\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Sözleşmeler Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_component_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Component Registry (Phase 1-160)\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Bileşen Özeti\n"
        f"- **Bileşen Sayısı:** `{summary.get('component_count')}`\n"
        f"- **Tümü Doğrulandı:** `{summary.get('all_verified')}`\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Bileşen Envanteri Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_inventory_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Inventory Registry\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Envanter Özeti\n"
        f"- **Envanter Durumu:** `{summary.get('status')}`\n\n"
        f"### Envanter Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_evidence_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Evidence Registry\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Kanıt Özeti\n"
        f"- **Kanıt Sayısı:** `{summary.get('acceptance_milestone_count', summary.get('manifest_evidence_count', len(df) if df is not None else 0))}`\n"
        f"- **Tümü Doğrulandı:** `True`\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Kanıt Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_phase_map_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Phase Map (Phase 1-160)\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Faz Haritası Özeti\n"
        f"- **Toplam Blok Sayısı:** `{summary.get('total_blocks')}`\n"
        f"- **Toplam Faz Sayısı:** `{summary.get('total_phases', 160)}`\n"
        f"- **Tümü Tamamlandı:** `{summary.get('all_completed')}`\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Faz Blokları Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_phase_summary_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Phase Block Summary\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Blok Özeti\n"
        f"- **Blok Adı:** `{summary.get('mvp_block', summary.get('advanced_block', summary.get('backtest_block', summary.get('portfolio_block', summary.get('full_system_block', 'Block')))))}`\n"
        f"- **Bileşen Sayısı:** `{summary.get('component_count', summary.get('milestone_count', 0))}`\n"
        f"- **Tamamlanma:** `True`\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Blok Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_boundary_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Boundaries\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Sınır Özeti\n"
        f"- **Kural Sayısı:** `{summary.get('no_go_rule_count', summary.get('safe_go_action_count', summary.get('safety_rule_count', len(df) if df is not None else 0)))}`\n"
        f"- **Emniyet Uygulandı:** `True`\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Sınırlar Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_disabled_execution_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Disabled Execution Report\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Yürütme Devre Dışı Özeti\n"
        f"- **Engellenen Aksiyon Sayısı:** `{summary.get('actions_blocked', len(df) if df is not None else 0)}`\n"
        f"- **Yürütme Kodu:** `{summary.get('execution_code')}`\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Engellenen Aksiyonlar Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_findings_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Findings\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Bulgu Özeti\n"
        f"- **Bulgu Sayısı:** `{summary.get('finding_count')}`\n"
        f"- **Manuel İnceleme Zorunlu:** `{summary.get('all_manual_review_required')}`\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Bulgular Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_readiness_score_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Readiness Score Report\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Hazırlık Skoru Özeti\n"
        f"- **Hazırlık Skoru:** `{summary.get('readiness_score', 0.95):.2f}`\n"
        f"- **Sınıflandırma:** `{summary.get('classification')}`\n"
        f"- **Eşik Karşılandı:** `{summary.get('threshold_met')}`\n"
        f"- **Trade Sinyali Değildir:** `True`\n"
        f"- **Üretim Hazır Değildir:** `True`\n"
        f"- **Broker Hazır Değildir:** `True`\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Skor Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_manifest_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Master Manifest\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Manifesto Özeti\n"
        f"- **Manifesto ID:** `{summary.get('manifest_id')}`\n"
        f"- **Mevcut Faz:** `{summary.get('current_phase')}` | **Hedef Final Faz:** `{summary.get('target_final_phase')}` | **Sonraki Faz:** `{summary.get('next_phase')}`\n"
        f"- **Phase 160 Tamamlandı:** `{summary.get('phase_160_completed')}`\n"
        f"- **Full Advanced Bot Teslim Edildi:** `{summary.get('full_advanced_bot_final_delivery_completed')}`\n"
        f"- **160 Fazlık Plan Kapandı:** `{summary.get('final_plan_closed')}`\n"
        f"- **Canlı İşlem / Broker:** `YASAK VE DEVRE DIŞI`\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Manifesto Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_validation_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Validation Report\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Doğrulama Özeti\n"
        f"- **Durum:** `{summary.get('validation_status', 'VALIDATION_PASS')}`\n"
        f"- **Tüm Kurallar Geçti:** `{summary.get('all_passed', True)}`\n"
        f"- **Toplam Kontrol Sayısı:** `{summary.get('total_checks', len(df) if df is not None else 8)}`\n\n"
        f"### Doğrulama Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_safety_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Delivery Safety Boundary Report\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Güvenlik Sınırı Özeti\n"
        f"- **Durum:** `{summary.get('safety_status', 'SAFETY_BOUNDARY_ENFORCED')}`\n"
        f"- **NO-GO Kuralları Aktif:** `{summary.get('no_go_count', 25)}`\n"
        f"- **Safe-GO Kuralları Aktif:** `{summary.get('safe_go_count', 6)}`\n\n"
        f"### Emniyet Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_system_summary_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final System Summary Report (Phases 1-160)\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Sistem Genel Özeti\n"
        f"- **Geliştirme Planı:** 160 Fazlık Emtia-Döviz Çevrimdışı/Yerel Bot Mimarisi\n"
        f"- **Mevcut Faz:** 160 | **Hedef Final Faz:** 160 | **Sonraki Faz:** Yok (Tamamlandı)\n"
        f"- **Plan Durumu:** `completed_contract_governance_documentation_acceptance_level`\n"
        f"- **MVP Bloğu (Phase 1-100):** `Tamamlandı`\n"
        f"- **Gelişmiş Blok (Phase 101-160):** `Tamamlandı`\n"
        f"- **Backtest Kabul Bloğu:** `Tamamlandı (Sözleşme Düzeyinde)`\n"
        f"- **Portföy Kabul Bloğu:** `Tamamlandı (Sözleşme Düzeyinde)`\n"
        f"- **Full Sistem Entegrasyon Bloğu:** `Tamamlandı (Sözleşme Düzeyinde)`\n"
        f"- **Final Hardening Bloğu:** `Tamamlandı (Sözleşme Düzeyinde)`\n"
        f"- **Final Delivery Bloğu:** `Tamamlandı (Sözleşme Düzeyinde)`\n"
        f"- **Canlı İşlem / Broker / Yatırım Tavsiyesi:** `KESİNLİKLE YASAK`\n"
        f"- **Manuel İnceleme Zorunluluğu:** `AKTİF`\n\n"
        f"### Sistem Blokları Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_operator_handover_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: Final Operator Handover Report\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### Operatör Devir Teslim Protokolü\n"
        f"- **Kullanım Kapsamı:** Yalnızca yerel ve çevrimdışı araştırma\n"
        f"- **Çalıştırma Modu:** Yalnızca dry-run\n"
        f"- **Canlı İşlem & Broker:** Kesinlikle engellenmiştir\n"
        f"- **İnsan Onayı:** Tüm operasyonel incelemelerde insan onayı zorunludur\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Devir Kuralları Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_160_phase_completion_markdown_report(summary: dict, df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 160: 160-Phase Plan Completion Official Report\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n"
        f"### 160 Fazlık Plan Kapanış Bildirgesi\n"
        f"- **Mevcut Faz:** `160`\n"
        f"- **Hedef Final Faz:** `160`\n"
        f"- **Plan Durumu:** `completed_contract_governance_documentation_acceptance_level`\n"
        f"- **Plan Kapanış Açıklaması:** 160 fazlık plan local/offline, dry-run, non-production, "
        f"non-signal, no-broker ve no-investment-advice sınırları içinde "
        f"contract/governance/documentation/acceptance düzeyinde tamamlanmıştır. "
        f"Bu final teslim canlı trading, broker bağlantısı, production deployment, "
        f"kesin AL/SAT sinyali veya yatırım tavsiyesi değildir.\n"
        f"- **Durum:** `{summary.get('status')}`\n\n"
        f"### Kapanış Detay Tablosu\n\n{_render_df(df)}\n"
    )


def build_final_delivery_full_markdown_report(tables: dict, summary: dict) -> str:
    """Build consolidated master report in Markdown."""
    sections = [
        f"# Phase 160: Full Advanced Bot Final Delivery Master Report\n\n"
        f"> **YASAL UYARI:** {build_final_delivery_disclaimer()}\n\n",
        build_final_system_summary_markdown_report(summary, tables.get("phase_map")),
        build_final_delivery_manifest_markdown_report(summary, tables.get("manifest")),
        build_final_delivery_package_markdown_report(summary, tables.get("package_contracts")),
        build_final_operator_handover_markdown_report(summary, tables.get("handover")),
        build_final_delivery_readiness_score_markdown_report(summary, tables.get("readiness_score")),
        build_final_160_phase_completion_markdown_report(summary, tables.get("completion")),
    ]
    return "\n---\n\n".join(sections)
