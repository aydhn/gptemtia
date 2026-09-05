from typing import Dict, Any, Optional
import pandas as pd


def build_data_normalization_disclaimer() -> str:
    return (
        "> [!IMPORTANT]\n"
        "> **YASAL UYARI VE GÜVENLİK SINIRI**:\n"
        "> Bu çıktı Phase 113 Data Normalization Layer raporudur. "
        "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, "
        "normalized data’yı trade sinyali olarak kullanma, official approval, "
        "production deployment, model deployment, scraping, haber tam metni toplama, "
        "telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, "
        "source overwrite veya destructive cleaning değildir.\n"
    )


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    if df is None or df.empty:
        return ""
    try:
        return df.to_markdown(index=False)
    except Exception:
        cols = list(df.columns)
        header = "| " + " | ".join(str(c) for c in cols) + " |"
        sep = "| " + " | ".join("---" for _ in cols) + " |"
        rows = []
        for _, row in df.iterrows():
            rows.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
        return "\n".join([header, sep] + rows)


def build_data_normalization_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Data Normalization Profile Registry Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Profil Özeti",
        f"- **Toplam Profil Sayısı**: {summary.get('total_profiles', 0)}",
        f"- **Non-Destructive Politika**: {summary.get('all_non_destructive', True)}",
        f"- **Dry-Run Modu**: {summary.get('all_dry_run', True)}",
        f"- **Mevcut Faz**: {summary.get('current_phase', 113)} / Hedef: {summary.get('target_final_phase', 160)}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Kayıtlı Profiller")
        lines.append(_df_to_markdown(profile_df))
        lines.append("")
    return "\n".join(lines)


def build_normalization_rule_registry_markdown_report(
    summary: Dict[str, Any],
    rules_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Normalization Rule Registry Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Kural Kataloğu Özeti",
        f"- **Toplam Kural Sayısı**: {summary.get('total_rules', 0)}",
        f"- **Kapsanan Alanlar**: {', '.join(summary.get('domains', []))}",
        f"- **Manuel İnceleme Gerektiren Kural Sayısı**: {summary.get('manual_review_count', 0)}",
        f"- **Non-Destructive Garanti**: {summary.get('all_non_destructive', True)}",
        "",
    ]
    if rules_df is not None and not rules_df.empty:
        lines.append("## Kurallar Listesi")
        lines.append(_df_to_markdown(rules_df))
        lines.append("")
    return "\n".join(lines)


def build_canonical_schema_markdown_report(
    summary: Dict[str, Any],
    schema_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Canonical Schema Registry Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Şema Özeti",
        f"- **Toplam Kanonik Şema Sayısı**: {summary.get('total_schemas', 0)}",
        f"- **Veri Seti Tipleri**: {', '.join(summary.get('dataset_types', []))}",
        "",
    ]
    if schema_df is not None and not schema_df.empty:
        lines.append("## Şemalar")
        lines.append(_df_to_markdown(schema_df))
        lines.append("")
    return "\n".join(lines)


def build_symbol_normalization_markdown_report(
    summary: Dict[str, Any],
    symbol_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Symbol & Indicator Normalization Enforcement Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Sembol ve Gösterge Dönüşüm Özeti",
        f"- **Toplam Eşleme Sayısı**: {summary.get('total_rules', summary.get('total_mappings', 0))}",
        "",
    ]
    if symbol_df is not None and not symbol_df.empty:
        lines.append("## Eşleme Detayları")
        lines.append(_df_to_markdown(symbol_df))
        lines.append("")
    return "\n".join(lines)


def build_time_frequency_unit_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Time, Frequency & Unit Normalization Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Zaman, Frekans ve Birim Standartlaştırması",
        f"- **Kanonik Zaman Dilimi**: UTC (ISO 8601)",
        f"- **Kaynak Korundu**: True",
        f"- **Birim Değer Dönüşümü**: Ertelendi (Yalnızca sözlük standartlaştırıldı)",
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_normalization_findings_markdown_report(
    summary: Dict[str, Any],
    findings_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Normalization Findings Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Bulgu Özeti",
        f"- **Toplam Bulgu Sayısı**: {summary.get('total_findings', 0)}",
        f"- **Uygulanan Normalizasyon**: {summary.get('applied_count', 0)}",
        f"- **Manuel İnceleme Gerektiren**: {summary.get('manual_review_count_total', summary.get('manual_review_required_count', 0))}",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        lines.append("## Bulgular Listesi")
        lines.append(_df_to_markdown(findings_df))
        lines.append("")
    return "\n".join(lines)


def build_manual_review_normalization_markdown_report(
    summary: Dict[str, Any],
    review_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Manual Review Normalization Queue Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## İnceleme Kuyruğu Özeti",
        f"- **Kuyruktaki Kayıt Sayısı**: {summary.get('total_queued_items', 0)}",
        f"- **Yıkıcı Eylem Engellendi**: {summary.get('destructive_actions_prevented', True)}",
        f"- **Kaynak Korundu**: {summary.get('source_preserved_all', True)}",
        "",
    ]
    if review_df is not None and not review_df.empty:
        lines.append("## Kuyruk Kayıtları")
        lines.append(_df_to_markdown(review_df))
        lines.append("")
    return "\n".join(lines)


def build_normalized_output_manifest_markdown_report(
    summary: Dict[str, Any],
    manifest_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Normalized Output Manifest Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Çıktı Manifestosu Özeti",
        f"- **Toplam Görünüm Kaydı**: {summary.get('total_manifest_entries', 0)}",
        f"- **Kaynak Korundu**: {summary.get('source_preserved_all', True)}",
        f"- **Yıkıcı Eylem İzni**: {summary.get('destructive_action_allowed_zero', True)}",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Manifest Detayları")
        lines.append(_df_to_markdown(manifest_df))
        lines.append("")
    return "\n".join(lines)


def build_normalization_score_markdown_report(
    summary: Dict[str, Any],
    score_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Normalization Score Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Skor Özeti",
        f"- **Puanlanan Veri Seti**: {summary.get('total_scored_datasets', 0)}",
        f"- **Ortalama Normalizasyon Skoru**: {summary.get('mean_score', 1.0)}",
        f"- **Min / Max**: {summary.get('min_score', 1.0)} / {summary.get('max_score', 1.0)}",
        f"- **Ticaret Sinyali Mi?**: HAYIR ({summary.get('is_trading_signal', False)})",
        f"- **Resmi Onay Mı?**: HAYIR ({summary.get('is_official_approval', False)})",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Skor Detayları")
        lines.append(_df_to_markdown(score_df))
        lines.append("")
    return "\n".join(lines)


def build_cross_domain_mapping_markdown_report(
    summary: Dict[str, Any],
    mapping_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Cross-Domain Normalized Mapping Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Çapraz Alan Eşleme Özeti",
        f"- **Toplam Çapraz Eşleme**: {summary.get('total_mappings', 0)}",
        f"- **Manuel İnceleme Sayısı**: {summary.get('manual_review_count', 0)}",
        "",
    ]
    if mapping_df is not None and not mapping_df.empty:
        lines.append("## Çapraz Eşlemeler")
        lines.append(_df_to_markdown(mapping_df))
        lines.append("")
    return "\n".join(lines)


def build_data_normalization_health_markdown_report(
    summary: Dict[str, Any],
    health_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Data Normalization Health Check Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Sistem Sağlık Özeti",
        f"- **Toplam Kontrol Sayısı**: {summary.get('total_checks', 0)}",
        f"- **Başarılı**: {summary.get('pass_count', 0)}",
        f"- **Başarısız**: {summary.get('fail_count', 0)}",
        f"- **Genel Durum**: {summary.get('overall_status', 'PASS')}",
        "",
    ]
    if health_df is not None and not health_df.empty:
        lines.append("## Sağlık Kontrolleri")
        lines.append(_df_to_markdown(health_df))
        lines.append("")
    return "\n".join(lines)


def build_data_normalization_validation_markdown_report(
    summary: Dict[str, Any],
    validation_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Data Normalization Validation Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Doğrulama Özeti",
        f"- **Toplam Doğrulama Maddesi**: {summary.get('total_validations', 0)}",
        f"- **Tüm Sözleşmeler Uyumlu**: {summary.get('all_passed', True)}",
        f"- **Yasaklı İddia Tespiti**: {summary.get('forbidden_claims_found', 0)}",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Doğrulama Sonuçları")
        lines.append(_df_to_markdown(validation_df))
        lines.append("")
    return "\n".join(lines)


def build_data_normalization_safety_markdown_report(
    summary: Dict[str, Any],
    safety_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Data Normalization Safety Boundary Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Güvenlik Sınırı Özeti",
        f"- **Toplam No-Go Maddesi**: {summary.get('total_no_go', 0)}",
        f"- **Toplam Safe-Go Maddesi**: {summary.get('total_safe_go', 0)}",
        f"- **Kaynak Koruma Garantisi**: {summary.get('source_overwrite_forbidden', True)}",
        f"- **Yıkıcı Temizleme Yasağı**: {summary.get('destructive_cleaning_forbidden', True)}",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Güvenlik Kuralları")
        lines.append(_df_to_markdown(safety_df))
        lines.append("")
    return "\n".join(lines)


def build_phase_114_handoff_markdown_report(
    summary: Dict[str, Any],
    handoff_df: Optional[pd.DataFrame] = None,
) -> str:
    lines = [
        "# Phase 113 — Phase 114 Lineage & Provenance Handoff Report",
        "",
        build_data_normalization_disclaimer(),
        "",
        "## Devir Özeti",
        f"- **Hedef Faz**: Phase 114 (Data Lineage and Provenance)",
        f"- **Devredilen Soy Kütüğü Alanları**: {summary.get('total_handoff_items', 0)}",
        f"- **Manuel İnceleme Gerektiren Alanlar**: {summary.get('manual_review_count', 0)}",
        f"- **Yıkıcı Eylem**: {summary.get('destructive_actions', False)}",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Devir Maddeleri")
        lines.append(_df_to_markdown(handoff_df))
        lines.append("")
    return "\n".join(lines)
