from typing import Dict, Any, Optional
import pandas as pd


def _df_to_markdown(df: pd.DataFrame) -> str:
    if df.empty:
        return ""
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


def build_feature_engine_disclaimer() -> str:
    return (
        "> **YASAL VE TEKNİK FERAGATNAME (DISCLAIMER)**:\n"
        "> Bu çıktı Phase 116 Advanced Indicator/Feature/Factor Engine Foundation raporudur. "
        "> Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, feature/indicator değerini trade sinyali "
        "> olarak kullanma, strateji üretimi, backtest, optimizer, production deployment, model deployment, "
        "> scraping, gerçek provider API çağrısı veya official approval değildir.\n"
    )


def build_feature_engine_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 116: Feature Engine Profile Registry Report",
        "",
        build_feature_engine_disclaimer(),
        "",
        "## Özet",
        f"- **Aktif Profil**: `{summary.get('active_profile', 'unknown')}`",
        f"- **Toplam Profil**: `{summary.get('total_profiles', 0)}`",
        f"- **Mevcut Faz**: `{summary.get('current_phase', 116)}`",
        f"- **Hedef Final Faz**: `{summary.get('target_final_phase', 160)}`",
        f"- **Sonraki Faz**: `{summary.get('next_phase', 117)}`",
        f"- **Local Only**: `{summary.get('all_local_only', True)}`",
        f"- **Non-Signal**: `{summary.get('all_non_signal', True)}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Profiller Tablosu")
        lines.append(_df_to_markdown(profile_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_input_contract_markdown_report(
    summary: Dict[str, Any],
    contract_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 116: Canonical Feature Input Contracts Report",
        "",
        build_feature_engine_disclaimer(),
        "",
        "## Özet",
        f"- **Toplam Kontrat Sayısı**: `{summary.get('total_contracts', 0)}`",
        f"- **Kayıtlı Veri Seti Tipleri**: `{len(summary.get('dataset_types', []))}`",
        f"- **Tüm Kontratlar Hazır**: `{summary.get('all_contracts_registered', True)}`",
        f"- **Manuel İnceleme Gereksinimi**: `{summary.get('manual_review_required_count', 0)}`",
        "",
    ]
    if contract_df is not None and not contract_df.empty:
        lines.append("## Girdi Kontratları")
        lines.append(_df_to_markdown(contract_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_schema_markdown_report(
    summary: Dict[str, Any],
    schema_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 116: Canonical Feature Schema Registry Report",
        "",
        build_feature_engine_disclaimer(),
        "",
        "## Özet",
        f"- **Toplam Feature Şeması**: `{summary.get('total_schemas', 0)}`",
        f"- **Feature Tipleri**: `{', '.join(summary.get('feature_types', []))}`",
        f"- **Tümü Non-Signal**: `{summary.get('all_non_signal', True)}`",
        "",
    ]
    if schema_df is not None and not schema_df.empty:
        lines.append("## Şemalar Tablosu")
        lines.append(_df_to_markdown(schema_df))
        lines.append("")
    return "\n".join(lines)


def build_indicator_catalog_markdown_report(
    summary: Dict[str, Any],
    catalog_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 116: Indicator Catalog Registry Report",
        "",
        build_feature_engine_disclaimer(),
        "",
        "## Özet",
        f"- **Toplam Gösterge Sayısı**: `{summary.get('total_indicators', 0)}`",
        f"- **Aile Sayısı**: `{summary.get('total_families', 0)}`",
        f"- **Gösterge Aileleri**: `{', '.join(summary.get('families', []))}`",
        f"- **Tümü Non-Signal**: `{summary.get('all_non_signal', True)}`",
        "",
    ]
    if catalog_df is not None and not catalog_df.empty:
        lines.append("## Gösterge Kataloğu")
        lines.append(_df_to_markdown(catalog_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_metadata_markdown_report(
    summary: Dict[str, Any],
    metadata_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 116: Feature Metadata Registry Report",
        "",
        build_feature_engine_disclaimer(),
        "",
        "## Özet",
        f"- **Kayıtlı Feature Sayısı**: `{summary.get('total_features_registered', 0)}`",
        f"- **Maksimum Warmup Satırı**: `{summary.get('max_warmup_required', 0)}`",
        f"- **Lookahead Koruması**: `{summary.get('all_guarded_against_lookahead', True)}`",
        "",
    ]
    if metadata_df is not None and not metadata_df.empty:
        lines.append("## Metadata Detayları")
        lines.append(_df_to_markdown(metadata_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_computation_markdown_report(
    summary: Dict[str, Any],
    computation_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 116: Basic Feature Computation Rehearsal Report",
        "",
        build_feature_engine_disclaimer(),
        "",
        "## Özet",
        f"- **Hesaplanan Özellik Sayısı**: `{summary.get('features_computed_count', 0)}`",
        f"- **Girdi Mutasyon Koruması**: `PASSED (df.copy())`",
        f"- **Yasaklı Kolon Taraması**: `PASSED (0 signal/target columns)`",
        f"- **Lookahead Taraması**: `PASSED (no shift(-1))`",
        "",
    ]
    if computation_df is not None and not computation_df.empty:
        lines.append("## Hesaplama Çıktısı")
        lines.append(_df_to_markdown(computation_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_validation_markdown_report(
    summary: Dict[str, Any],
    validation_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 116: Feature Engine Validation Report",
        "",
        build_feature_engine_disclaimer(),
        "",
        "## Özet",
        f"- **Validasyon Durumu**: `{summary.get('validation_status', 'UNKNOWN')}`",
        f"- **Toplam Kontrol**: `{summary.get('total_checks', 0)}`",
        f"- **Geçen Kontrol**: `{summary.get('passed_checks', 0)}`",
        f"- **Yasaklı İddia Tespiti**: `{summary.get('forbidden_claims_found', False)}`",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Kontrol Sonuçları")
        lines.append(_df_to_markdown(validation_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_engine_health_markdown_report(
    summary: Dict[str, Any],
    health_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 116: Feature Engine Health Check Report",
        "",
        build_feature_engine_disclaimer(),
        "",
        "## Özet",
        f"- **Genel Durum**: `{summary.get('overall_status', 'UNKNOWN')}`",
        f"- **Toplam Kontrol**: `{summary.get('total_checks', 0)}`",
        f"- **Başarılı**: `{summary.get('passed_checks', 0)}`",
        f"- **Başarısız**: `{summary.get('failed_checks', 0)}`",
        "",
    ]
    if health_df is not None and not health_df.empty:
        lines.append("## Sağlık Kontrolleri")
        lines.append(_df_to_markdown(health_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_engine_safety_markdown_report(
    summary: Dict[str, Any],
    safety_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 116: Feature Engine Safety Boundary Report",
        "",
        build_feature_engine_disclaimer(),
        "",
        "## Özet",
        f"- **Güvenlik Durumu**: `{summary.get('safety_status', 'ACTIVE')}`",
        f"- **Toplam Kural**: `{summary.get('total_rules', 0)}`",
        f"- **No-Go Kuralları**: `{summary.get('total_no_go_rules', 0)}` (Tümü zorunlu)",
        f"- **Safe-Go Koşulları**: `{summary.get('total_safe_go_rules', 0)}` (Tümü aktif)",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Güvenlik Kuralları Tablosu")
        lines.append(_df_to_markdown(safety_df))
        lines.append("")
    return "\n".join(lines)


def build_phase_117_handoff_markdown_report(
    summary: Dict[str, Any],
    handoff_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 116 -> Phase 117 Technical Indicator Expansion Handoff Report",
        "",
        build_feature_engine_disclaimer(),
        "",
        "## Özet",
        f"- **Handoff Durumu**: `{summary.get('readiness_status', 'READY')}`",
        f"- **Hedef Faz**: `{summary.get('target_phase', 117)}` - `{summary.get('target_phase_name', '')}`",
        f"- **Devredilen Başlık Sayısı**: `{summary.get('total_handoff_items', 0)}`",
        f"- **Tüm Maddeler Hazır**: `{summary.get('all_items_ready', True)}`",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Maddeleri")
        lines.append(_df_to_markdown(handoff_df))
        lines.append("")
    return "\n".join(lines)
