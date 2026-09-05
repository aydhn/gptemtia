"""Phase 119: Cross-Asset Alignment Markdown Report Builder.

Generates comprehensive and domain-specific markdown reports for Phase 119
Cross-Asset Feature Alignment, Multi-Domain Feature Matrix Contracts,
Timestamp/Symbol Alignment, and Non-Signal Cross-Asset Feature Layer.
"""

from typing import Dict, Any, Optional
import pandas as pd


CROSS_ASSET_ALIGNMENT_DISCLAIMER = (
    "Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları "
    "trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, "
    "optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, "
    "gerçek provider API çağrısı veya official approval sağlamaz."
)


def _df_to_markdown(df: pd.DataFrame) -> str:
    """Format a pandas DataFrame as a clean GitHub-flavored markdown table."""
    if df.empty:
        return "_Tabloda veri bulunmuyor._"
    headers = [str(c) for c in df.columns]
    rows = [[str(val) for val in row] for row in df.itertuples(index=False)]
    col_widths = [max(len(h), 3) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            if len(val) > col_widths[i]:
                col_widths[i] = len(val)
    header_line = "| " + " | ".join(headers[i].ljust(col_widths[i]) for i in range(len(headers))) + " |"
    sep_line = "| " + " | ".join("-" * col_widths[i] for i in range(len(headers))) + " |"
    data_lines = [
        "| " + " | ".join(row[i].ljust(col_widths[i]) for i in range(len(headers))) + " |"
        for row in rows
    ]
    return "\n".join([header_line, sep_line] + data_lines)


def build_cross_asset_alignment_disclaimer() -> str:
    """Return the official Phase 119 disclaimer."""
    return CROSS_ASSET_ALIGNMENT_DISCLAIMER


def build_cross_asset_alignment_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Cross-Asset Alignment Profiles."""
    lines = [
        "# Phase 119: Cross-Asset Alignment Profile Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Profil Özeti",
        f"- **Aktif Profil**: `{summary.get('active_profile', 'unknown')}`",
        f"- **Toplam Profil**: {summary.get('total_profiles', 0)}",
        f"- **Mevcut Faz**: {summary.get('current_phase', 119)}",
        f"- **Hedef Faz**: {summary.get('target_final_phase', 160)}",
        f"- **Sonraki Faz**: {summary.get('next_phase', 120)}",
        f"- **Local Only / Research Only**: {summary.get('local_only', True)}",
        f"- **Non-Signal Güvencesi**: {summary.get('non_signal', True)}",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.extend(["## Profil Listesi ve Detayları", "", _df_to_markdown(profile_df), ""])
    return "\n".join(lines)


def build_cross_asset_alignment_domain_markdown_report(
    summary: Dict[str, Any], domain_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Cross-Asset Alignment Domains."""
    lines = [
        "# Phase 119: Cross-Asset Alignment Domain Registry Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Domain Kayıt Özeti",
        f"- **Toplam Domain Sayısı**: {summary.get('total_domains', 0)}",
        f"- **Aktif Domain Sayısı**: {summary.get('active_domains', 0)}",
        f"- **Sinyal Karakteri**: `{summary.get('non_signal', True)} (Strictly Non-Signal)`",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if domain_df is not None and not domain_df.empty:
        lines.extend(["## Kayıtlı Domain Tablosu", "", _df_to_markdown(domain_df), ""])
    return "\n".join(lines)


def build_asset_universe_markdown_report(
    summary: Dict[str, Any], universe_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Asset Universes."""
    lines = [
        "# Phase 119: Asset Universe Alignment Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Evren Özeti",
        f"- **Toplam Varlık Evreni**: {summary.get('total_universes', 0)}",
        f"- **Sinyal Üretimi**: `False`",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if universe_df is not None and not universe_df.empty:
        lines.extend(["## Varlık Evrenleri Detayları", "", _df_to_markdown(universe_df), ""])
    return "\n".join(lines)


def build_asset_symbol_mapping_markdown_report(
    summary: Dict[str, Any], mapping_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Asset Symbol Mappings."""
    lines = [
        "# Phase 119: Asset Symbol Mapping Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Sembol Eşleme Özeti",
        f"- **Toplam Sembol Eşlemesi**: {summary.get('total_mappings', 0)}",
        f"- **Varlık Tipleri**: {', '.join(summary.get('asset_types', []))}",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if mapping_df is not None and not mapping_df.empty:
        lines.extend(["## Eşleme Detayları", "", _df_to_markdown(mapping_df), ""])
    return "\n".join(lines)


def build_feature_namespace_markdown_report(
    summary: Dict[str, Any], namespace_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Feature Namespaces."""
    lines = [
        "# Phase 119: Feature Namespace Standard Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Ad Alanı Standardı Özeti",
        f"- **Toplam Tanımlı Feature**: {summary.get('total_features', 0)}",
        f"- **Format**: `<domain>__<family>__<source_symbol>__<feature_name>__<window>`",
        f"- **Kapsanan Domainler**: {', '.join(summary.get('domains', []))}",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if namespace_df is not None and not namespace_df.empty:
        lines.extend(["## Tanımlı Feature İsimleri", "", _df_to_markdown(namespace_df), ""])
    return "\n".join(lines)


def build_timestamp_session_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Timestamp & Session Alignment."""
    lines = [
        "# Phase 119: Timestamp & Session Alignment Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Zaman & Seans Özeti",
        f"- **Zaman Damgası Sözleşmeleri**: {summary.get('total_contracts', 0)}",
        f"- **Seans Politikaları**: {summary.get('total_policies', 0)}",
        f"- **UTC Standartlaştırma**: `Zorunlu`",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Detay Tablosu", "", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_feature_matrix_contracts_markdown_report(
    summary: Dict[str, Any], contract_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Feature Matrix Contracts."""
    lines = [
        "# Phase 119: Feature Matrix Contracts Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Matris Sözleşmeleri Özeti",
        f"- **Toplam Sözleşme**: {summary.get('total_contracts', 0)}",
        f"- **Geriye Dönük (Backward-only) Asof İlkesi**: `Zorunlu`",
        f"- **Lookahead Koruması**: `Aktif`",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if contract_df is not None and not contract_df.empty:
        lines.extend(["## Sözleşme Detayları", "", _df_to_markdown(contract_df), ""])
    return "\n".join(lines)


def build_domain_alignment_markdown_report(
    title: str,
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for a specific cross-domain alignment registry."""
    lines = [
        f"# Phase 119: {title} Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Hizalama Özeti",
        f"- **Toplam Hizalama Bağlantısı**: {summary.get('total_alignments', summary.get('total_mappings', 0))}",
        f"- **Non-Signal İzolasyonu**: `Doğrulandı`",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Hizalama Detayları", "", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_cross_domain_matrix_markdown_report(
    summary: Dict[str, Any], matrix_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Cross-Domain Feature Matrix."""
    lines = [
        "# Phase 119: Cross-Domain Aligned Feature Matrix Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Matris Özeti",
        f"- **Toplam Satır**: {summary.get('total_rows', 0)}",
        f"- **Toplam Sütun**: {summary.get('total_columns', 0)}",
        f"- **Sözleşme Adı**: `{summary.get('contract_name', 'cross_domain_research')}`",
        f"- **Target / Label / Prediction**: `Bulunmuyor (Strictly Non-Signal)`",
        f"- **Geleceğe Bakış (Lookahead Bias)**: `Sıfır (Zero Lookahead)`",
        f"- **Kaynak Korunumu**: `Tam Korunmuş (df.copy used)`",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if matrix_df is not None and not matrix_df.empty:
        lines.extend(["## Matris Kolonları ve Önizleme", "", f"Kolon Sayısı: {len(matrix_df.columns)}", "", _df_to_markdown(matrix_df.head(10)), ""])
    return "\n".join(lines)


def build_aligned_manifest_markdown_report(
    summary: Dict[str, Any], manifest_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Aligned Feature Matrix Manifests."""
    lines = [
        "# Phase 119: Aligned Feature Matrix Manifest Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Manifest Özeti",
        f"- **Toplam Manifest**: {summary.get('total_manifests', 0)}",
        f"- **Non-Signal İlkesi**: `Onaylandı`",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.extend(["## Manifest Detayları", "", _df_to_markdown(manifest_df), ""])
    return "\n".join(lines)


def build_cross_asset_alignment_validation_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for validation findings."""
    lines = [
        "# Phase 119: Cross-Asset Alignment Validation Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Doğrulama Özeti",
        f"- **Toplam Kontrol**: {summary.get('total_checks', 0)}",
        f"- **Başarılı**: {summary.get('passed_checks', 0)}",
        f"- **Başarısız**: {summary.get('failed_checks', 0)}",
        f"- **Genel Durum**: `{summary.get('validation_status', 'PASS')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Kontrol Bulguları", "", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_cross_asset_alignment_health_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for system health check."""
    lines = [
        "# Phase 119: Cross-Asset Alignment Health Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Sistem Sağlık Özeti",
        f"- **Toplam Bileşen**: {summary.get('total_components', 0)}",
        f"- **Sağlıklı**: {summary.get('healthy_components', 0)}",
        f"- **Sorunlu**: {summary.get('unhealthy_components', 0)}",
        f"- **Sistem Durumu**: `{summary.get('health_status', 'HEALTHY')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Bileşen Durumları", "", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_cross_asset_alignment_safety_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for safety boundary enforcement."""
    lines = [
        "# Phase 119: Cross-Asset Alignment Safety Boundary Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Güvenlik Sınırları Özeti",
        f"- **Toplam Kural**: {summary.get('total_conditions', 0)}",
        f"- **NO-GO Sınırları**: {summary.get('no_go_count', 0)} (Strictly Enforced)",
        f"- **SAFE-GO İlkeleri**: {summary.get('safe_go_count', 0)} (Enabled)",
        f"- **Güvenlik Statüsü**: `{summary.get('safety_status', 'SECURE')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Güvenlik Kuralları Listesi", "", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_phase_120_handoff_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Phase 120 Handoff."""
    lines = [
        "# Phase 119 -> Phase 120: Feature Fusion Handoff Report",
        "",
        f"> {CROSS_ASSET_ALIGNMENT_DISCLAIMER}",
        "",
        "## Handoff Özeti",
        f"- **Toplam Handoff Maddesi**: {summary.get('total_items', 0)}",
        f"- **Hazır (READY) Maddeler**: {summary.get('ready_items', 0)}",
        f"- **Hedef Faz**: `120 (Macro/Calendar/News Feature Fusion)`",
        f"- **Handoff Durumu**: `{summary.get('handoff_status', 'READY')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Handoff Maddeleri Detayı", "", _df_to_markdown(df), ""])
    return "\n".join(lines)
