"""Phase 126: Regime Foundation Report Builder.

Generates structured Markdown reports for all Phase 126 registries, taxonomies, health, and handoff.
Includes the canonical Phase 126 research disclaimer.
"""

from typing import Any, Dict, Optional
import pandas as pd

REGIME_FOUNDATION_DISCLAIMER: str = (
    "Bu çıktı Phase 126 Regime Classification and Market Behavior Foundation raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, regime state değerini trade sinyali olarak kullanma, "
    "strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target üretimi, "
    "production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, "
    "model deployment, scraping veya gerçek provider API çağrısı değildir."
)


def build_regime_foundation_disclaimer() -> str:
    """Return the canonical Phase 126 non-signal research disclaimer."""
    return REGIME_FOUNDATION_DISCLAIMER


def _dataframe_to_markdown_table(df: pd.DataFrame, max_rows: int = 50) -> str:
    """Convert pandas DataFrame to Markdown table without external tabulate dependency."""
    if df.empty:
        return "*Kayıt bulunamadı.*"
    cols = list(df.columns)
    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join(["---"] * len(cols)) + " |"
    rows = []
    for _, row in df.head(max_rows).iterrows():
        row_vals = [str(row[c]).replace("\n", " ").replace("|", "/") for c in cols]
        rows.append("| " + " | ".join(row_vals) + " |")
    return "\n".join([header, sep] + rows)


def build_regime_foundation_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build Markdown report for Regime Foundation Profiles."""
    lines = [
        "# Phase 126: Regime Foundation Profile Registry Report",
        "",
        f"> **UYARI / DISCLAIMER:** {REGIME_FOUNDATION_DISCLAIMER}",
        "",
        "## Özet",
        f"- **Aktif Profil:** `{summary.get('active_profile')}`",
        f"- **Toplam Profil Sayısı:** `{summary.get('total_profiles')}`",
        f"- **Mevcut Faz:** `{summary.get('current_phase')}`",
        f"- **Sıradaki Faz:** `{summary.get('next_phase')}`",
        f"- **Hedef Final Faz:** `{summary.get('target_final_phase')}`",
        f"- **Tüm Profiller Non-Signal:** `{summary.get('all_non_signal')}`",
        f"- **Tüm Profiller Yerel/Çevrimdışı:** `{summary.get('all_local_only')}`",
        f"- **Model Eğitimi Engellendi:** `{summary.get('all_model_training_disabled')}`",
        f"- **Clustering Engellendi:** `{summary.get('all_clustering_disabled')}`",
        "",
        "## Profil Tablosu",
    ]
    if profile_df is not None:
        lines.append(_dataframe_to_markdown_table(profile_df))
    return "\n".join(lines)


def build_market_behavior_taxonomy_markdown_report(
    summary: Dict[str, Any],
    taxonomy_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build Markdown report for Market Behavior Taxonomy."""
    lines = [
        "# Phase 126: Market Behavior Taxonomy Report",
        "",
        f"> **UYARI / DISCLAIMER:** {REGIME_FOUNDATION_DISCLAIMER}",
        "",
        "## Özet",
        f"- **Toplam Davranış Sayısı:** `{summary.get('total_behaviors')}`",
        f"- **Hazır Davranışlar:** `{summary.get('ready_behaviors')}`",
        f"- **Yer Tutucu (Placeholder) Davranışlar:** `{summary.get('placeholder_behaviors')}`",
        f"- **Tümü Non-Signal:** `{summary.get('all_non_signal')}`",
        f"- **Ticari Al/Sat Tavsiyesi Yok:** `{summary.get('no_trading_recommendations')}`",
        "",
        "## Piyasa Davranışları Tablosu",
    ]
    if taxonomy_df is not None:
        lines.append(_dataframe_to_markdown_table(taxonomy_df))
    return "\n".join(lines)


def build_regime_state_taxonomy_markdown_report(
    summary: Dict[str, Any],
    state_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build Markdown report for Regime State Taxonomy."""
    lines = [
        "# Phase 126: Regime State Taxonomy Report",
        "",
        f"> **UYARI / DISCLAIMER:** {REGIME_FOUNDATION_DISCLAIMER}",
        "",
        "## Özet",
        f"- **Toplam Rejim Durumları:** `{summary.get('total_states')}`",
        f"- **Hazır Durumlar:** `{summary.get('ready_states')}`",
        f"- **Yer Tutucu Durumlar:** `{summary.get('placeholder_states')}`",
        f"- **Zorunlu Önek ('regime_state_') Uyumlu:** `{summary.get('all_prefixed_correctly')}`",
        f"- **Hedef / Tahmin (Target/Prediction) Yok:** `{summary.get('no_targets_or_predictions')}`",
        f"- **İşlem Tavsiyesi Yok:** `{summary.get('no_trading_recommendations')}`",
        "",
        "## Rejim Durumları Tablosu",
    ]
    if state_df is not None:
        lines.append(_dataframe_to_markdown_table(state_df))
    return "\n".join(lines)


def build_regime_family_markdown_report(
    summary: Dict[str, Any],
    family_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build Markdown report for Master Regime Families."""
    lines = [
        "# Phase 126: Master Regime Family Registry Report",
        "",
        f"> **UYARI / DISCLAIMER:** {REGIME_FOUNDATION_DISCLAIMER}",
        "",
        "## Özet",
        f"- **Toplam Rejim Aileleri:** `{summary.get('total_families')}`",
        f"- **Hazır Aileler:** `{summary.get('ready_families')}`",
        f"- **Yer Tutucu Aileler:** `{summary.get('placeholder_families')}`",
        f"- **Model Eğitimi Çalıştırıldı mı:** `{summary.get('model_training_executed')}`",
        f"- **Kümeleme (Clustering) Çalıştırıldı mı:** `{summary.get('clustering_executed')}`",
        f"- **Non-Signal:** `{summary.get('all_non_signal')}`",
        "",
        "## Rejim Aileleri Tablosu",
    ]
    if family_df is not None:
        lines.append(_dataframe_to_markdown_table(family_df))
    return "\n".join(lines)


def build_regime_context_markdown_report(
    summary: Dict[str, Any],
    context_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build Markdown report for Macro, Event, News Metadata, and Cross-Asset Contexts."""
    lines = [
        "# Phase 126: Regime Environmental Contexts Report",
        "",
        f"> **UYARI / DISCLAIMER:** {REGIME_FOUNDATION_DISCLAIMER}",
        "",
        "## Özet",
        f"- **Bağlam Tipi:** `{summary.get('context_type', 'cross_environmental')}`",
        f"- **Toplam Kayıt:** `{summary.get('total_contexts', len(context_df) if context_df is not None else 0)}`",
        f"- **Haberler Sadece Metaveri:** `{summary.get('all_metadata_only', True)}`",
        f"- **Non-Signal:** `{summary.get('all_non_signal', True)}`",
        "",
        "## Bağlam Tablosu",
    ]
    if context_df is not None:
        lines.append(_dataframe_to_markdown_table(context_df))
    return "\n".join(lines)


def build_regime_contract_dependency_markdown_report(
    summary: Dict[str, Any],
    dependency_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build Markdown report for Input Contracts and Upstream Dependencies."""
    lines = [
        "# Phase 126: Regime Contracts and Dependencies Report",
        "",
        f"> **UYARI / DISCLAIMER:** {REGIME_FOUNDATION_DISCLAIMER}",
        "",
        "## Özet",
        f"- **Toplam Bağımlılık / Sözleşme:** `{summary.get('total_dependencies', summary.get('total_contracts', 0))}`",
        f"- **Tüm Bağımlılıklar Doğrulandı:** `{summary.get('all_verified', True)}`",
        f"- **No-Lookahead Zorunlu:** `{summary.get('all_no_lookahead_required', True)}`",
        f"- **Non-Signal Zorunlu:** `{summary.get('all_non_signal_required', True)}`",
        "",
        "## Bağımlılıklar Tablosu",
    ]
    if dependency_df is not None:
        lines.append(_dataframe_to_markdown_table(dependency_df))
    return "\n".join(lines)


def build_regime_manifest_markdown_report(
    summary: Dict[str, Any],
    manifest_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build Markdown report for Regime Foundation Manifest."""
    lines = [
        "# Phase 126: Regime Foundation Manifest Report",
        "",
        f"> **UYARI / DISCLAIMER:** {REGIME_FOUNDATION_DISCLAIMER}",
        "",
        "## Özet",
        f"- **Temel Adı:** `{summary.get('foundation_name')}`",
        f"- **Mevcut Faz:** `{summary.get('current_phase')}`",
        f"- **Sıradaki Faz:** `{summary.get('next_phase')}`",
        f"- **Hedef Final Faz:** `{summary.get('target_final_phase')}`",
        f"- **Rejim Aile Sayısı:** `{summary.get('regime_family_count')}`",
        f"- **Rejim Durum Sayısı:** `{summary.get('regime_state_count')}`",
        f"- **Toplam Bağımlılık Sayısı:** `{summary.get('dependency_count')}`",
        f"- **Non-Signal:** `{summary.get('non_signal')}`",
        f"- **Kaynak Korundu (Source Preserved):** `{summary.get('source_preserved')}`",
        f"- **Model Eğitimi Yapıldı mı:** `{summary.get('model_training_executed')}`",
        f"- **Resmi Onay:** `{summary.get('official_approval')}`",
        f"- **Canlıya Hazır:** `{summary.get('production_ready')}`",
        f"- **Broker Hazır:** `{summary.get('broker_ready')}`",
        f"- **Manifesto Durumu:** `{summary.get('manifest_status')}`",
        "",
        "## Manifesto Detayları",
    ]
    if manifest_df is not None:
        lines.append(_dataframe_to_markdown_table(manifest_df))
    return "\n".join(lines)


def build_regime_health_markdown_report(
    summary: Dict[str, Any],
    health_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build Markdown report for System Health."""
    lines = [
        "# Phase 126: Regime Foundation Health Check Report",
        "",
        f"> **UYARI / DISCLAIMER:** {REGIME_FOUNDATION_DISCLAIMER}",
        "",
        "## Özet",
        f"- **Genel Sağlık Durumu:** `{summary.get('health_status')}`",
        f"- **Toplam Kontrol:** `{summary.get('total_checks')}`",
        f"- **Başarılı Kontroller:** `{summary.get('healthy_checks')}`",
        f"- **Hatalı Kontroller:** `{summary.get('unhealthy_checks')}`",
        "",
        "## Sağlık Kontrol Tablosu",
    ]
    if health_df is not None:
        lines.append(_dataframe_to_markdown_table(health_df))
    return "\n".join(lines)


def build_regime_validation_markdown_report(
    summary: Dict[str, Any],
    validation_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build Markdown report for Validation Invariants."""
    lines = [
        "# Phase 126: Regime Foundation Validation Report",
        "",
        f"> **UYARI / DISCLAIMER:** {REGIME_FOUNDATION_DISCLAIMER}",
        "",
        "## Özet",
        f"- **Validasyon Durumu:** `{summary.get('validation_status')}`",
        f"- **Toplam Kural:** `{summary.get('total_rules')}`",
        f"- **Geçen Kurallar:** `{summary.get('passed_rules')}`",
        f"- **İhlal Sayısı:** `{summary.get('violations_count', 0)}`",
        f"- **Yasaklı İddia Taraması Temiz:** `{summary.get('forbidden_claims_clean', True)}`",
        "",
        "## Validasyon Tablosu",
    ]
    if validation_df is not None:
        lines.append(_dataframe_to_markdown_table(validation_df))
    return "\n".join(lines)


def build_regime_safety_markdown_report(
    summary: Dict[str, Any],
    safety_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build Markdown report for Safety Boundary."""
    lines = [
        "# Phase 126: Regime Foundation Safety Boundary Report",
        "",
        f"> **UYARI / DISCLAIMER:** {REGIME_FOUNDATION_DISCLAIMER}",
        "",
        "## Özet",
        f"- **Güvenlik Durumu:** `{summary.get('safety_status', 'SECURE')}`",
        f"- **NO-GO Kuralları Sayısı:** `{summary.get('no_go_count')}`",
        f"- **SAFE-GO İlkeleri Sayısı:** `{summary.get('safe_go_count')}`",
        f"- **Non-Signal:** `{summary.get('non_signal', True)}`",
        "",
        "## Güvenlik Sınırları Tablosu",
    ]
    if safety_df is not None:
        lines.append(_dataframe_to_markdown_table(safety_df))
    return "\n".join(lines)


def build_phase_127_handoff_markdown_report(
    summary: Dict[str, Any],
    handoff_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build Markdown report for Phase 127 Regime Feature Matrix Handoff."""
    lines = [
        "# Phase 126: Phase 127 Regime Feature Matrix Handoff Report",
        "",
        f"> **UYARI / DISCLAIMER:** {REGIME_FOUNDATION_DISCLAIMER}",
        "",
        "## Özet",
        f"- **Devir Durumu:** `{summary.get('handoff_status')}`",
        f"- **Kaynak Faz:** `{summary.get('source_phase')}`",
        f"- **Sıradaki Faz:** `{summary.get('next_phase')}`",
        f"- **Hedef Final Faz:** `{summary.get('target_final_phase')}`",
        f"- **Toplam Devir Öğesi:** `{summary.get('total_handoff_items')}`",
        f"- **Hazır Öğeler:** `{summary.get('ready_items')}`",
        f"- **Non-Signal Garantisi:** `{summary.get('non_signal')}`",
        "",
        "## Devir Maddeleri Tablosu",
    ]
    if handoff_df is not None:
        lines.append(_dataframe_to_markdown_table(handoff_df))
    return "\n".join(lines)
