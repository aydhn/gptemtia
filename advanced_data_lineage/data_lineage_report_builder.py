from typing import Dict, Any, Optional
import pandas as pd


DATA_LINEAGE_DISCLAIMER_TEXT = (
    "Bu çıktı Phase 114 Data Lineage and Provenance raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, "
    "lineage/traceability score’u trade sinyali olarak kullanma, official approval, "
    "production deployment, model deployment, scraping, haber tam metni toplama, "
    "telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, "
    "source overwrite veya destructive cleaning değildir."
)


def build_data_lineage_disclaimer() -> str:
    return f"> **YASAL UYARI VE FERAGATNAME**\n> {DATA_LINEAGE_DISCLAIMER_TEXT}\n"


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


def build_data_lineage_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Data Lineage Profile Registry Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Profil Sayısı**: {summary.get('total_profiles', 0)}",
        f"- **Mevcut Faz**: {summary.get('current_phase', 114)}",
        f"- **Hedef Final Faz**: {summary.get('target_final_phase', 160)}",
        f"- **Tümü Local-Only**: {summary.get('all_local_only', True)}",
        f"- **Tümü Non-Destructive**: {summary.get('all_non_destructive', True)}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        md.append(_df_to_markdown(profile_df))
    return "\n".join(md)


def build_provenance_source_markdown_report(
    summary: Dict[str, Any], source_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Provenance Source Registry Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Kaynak Sayısı**: {summary.get('total_sources', 0)}",
        f"- **Kaynak Tipleri**: {', '.join(summary.get('source_types', []))}",
        f"- **Manuel İnceleme Gereken**: {summary.get('manual_review_count', 0)}",
        f"- **Tümü No-Scraping**: {summary.get('all_no_scraping', True)}",
        "",
    ]
    if source_df is not None and not source_df.empty:
        md.append(_df_to_markdown(source_df))
    return "\n".join(md)


def build_provider_provenance_markdown_report(
    summary: Dict[str, Any], provider_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Provider Provenance Registry Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Sağlayıcı Sayısı**: {summary.get('total_providers', 0)}",
        f"- **Yüksek Güvenilirlikli Sağlayıcı**: {summary.get('high_confidence_count', 0)}",
        f"- **Manuel İnceleme Gereken**: {summary.get('manual_review_count', 0)}",
        "",
    ]
    if provider_df is not None and not provider_df.empty:
        md.append(_df_to_markdown(provider_df))
    return "\n".join(md)


def build_dataset_provenance_markdown_report(
    summary: Dict[str, Any], dataset_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Dataset Provenance Registry Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Veri Seti Sayısı**: {summary.get('total_datasets', 0)}",
        f"- **Tüm Kaynaklar Korundu**: {summary.get('all_source_preserved', True)}",
        f"- **Manuel İnceleme Sayısı**: {summary.get('manual_review_count', 0)}",
        "",
    ]
    if dataset_df is not None and not dataset_df.empty:
        md.append(_df_to_markdown(dataset_df))
    return "\n".join(md)


def build_transformation_provenance_markdown_report(
    summary: Dict[str, Any], transform_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Transformation Provenance Registry Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Dönüşüm Sayısı**: {summary.get('total_transformations', 0)}",
        f"- **Tüm Kaynaklar Korundu**: {summary.get('all_source_preserved', True)}",
        f"- **Sıfır Yıkıcı Eylem**: {summary.get('zero_destructive_actions', True)}",
        "",
    ]
    if transform_df is not None and not transform_df.empty:
        md.append(_df_to_markdown(transform_df))
    return "\n".join(md)


def build_domain_lineage_markdown_report(
    summary: Dict[str, Any], domain_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Domain Lineage Registry Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Domain Sayısı**: {summary.get('total_domains', 0)}",
        f"- **Gerekli Çıktı Sayısı**: {summary.get('required_output_count', 0)}",
        "",
    ]
    if domain_df is not None and not domain_df.empty:
        md.append(_df_to_markdown(domain_df))
    return "\n".join(md)


def build_license_copyright_markdown_report(
    summary: Dict[str, Any], license_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# License & Copyright Provenance Boundary Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Lisans Kaydı**: {summary.get('total_license_records', 0)}",
        f"- **Sıfır Serbest Yeniden Dağıtım**: {summary.get('zero_unrestricted_redistribution', True)}",
        f"- **Manuel İnceleme Sayısı**: {summary.get('manual_review_count', 0)}",
        "",
    ]
    if license_df is not None and not license_df.empty:
        md.append(_df_to_markdown(license_df))
    return "\n".join(md)


def build_audit_trail_markdown_report(
    summary: Dict[str, Any], audit_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Audit Trail Event Registry Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Denetim Olayı**: {summary.get('total_audit_events', 0)}",
        f"- **Sıfır Yıkıcı Eylem**: {summary.get('zero_destructive_actions', True)}",
        f"- **Manuel İnceleme Olayları**: {summary.get('manual_review_count', 0)}",
        "",
    ]
    if audit_df is not None and not audit_df.empty:
        md.append(_df_to_markdown(audit_df))
    return "\n".join(md)


def build_lineage_finding_markdown_report(
    summary: Dict[str, Any], finding_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Lineage Finding Registry Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Soy Kütüğü Bulgusu**: {summary.get('total_lineage_findings', 0)}",
        f"- **Manuel İnceleme Gereksinimi**: {summary.get('manual_review_count', 0)}",
        "",
    ]
    if finding_df is not None and not finding_df.empty:
        md.append(_df_to_markdown(finding_df))
    return "\n".join(md)


def build_traceability_score_markdown_report(
    summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Traceability Score Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam İzlenen Varlık**: {summary.get('total_traceability_records', 0)}",
        f"- **Ortalama İzlenebilirlik Skoru**: {summary.get('mean_traceability_score', 0.0)}",
        f"- **Minimum İzlenebilirlik Skoru**: {summary.get('min_traceability_score', 0.0)}",
        f"- **Tam Soy Kütüğüne Sahip Varlıklar**: {summary.get('complete_lineage_count', 0)}",
        "",
    ]
    if score_df is not None and not score_df.empty:
        md.append(_df_to_markdown(score_df))
    return "\n".join(md)


def build_cross_domain_provenance_markdown_report(
    summary: Dict[str, Any], map_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Cross-Domain Provenance Map Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Çapraz Eşleme**: {summary.get('total_cross_domain_mappings', 0)}",
        f"- **Tüm Kaynaklar Korundu**: {summary.get('all_source_preserved', True)}",
        "",
    ]
    if map_df is not None and not map_df.empty:
        md.append(_df_to_markdown(map_df))
    return "\n".join(md)


def build_data_lineage_health_markdown_report(
    summary: Dict[str, Any], health_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Data Lineage Health Check Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Sağlık Denetimi**: {summary.get('total_checks', 0)}",
        f"- **Geçen Denetimler**: {summary.get('passed_checks', 0)}",
        f"- **Genel Durum**: {summary.get('overall_status', 'PASS')}",
        "",
    ]
    if health_df is not None and not health_df.empty:
        md.append(_df_to_markdown(health_df))
    return "\n".join(md)


def build_data_lineage_validation_markdown_report(
    summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Data Lineage Validation Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Doğrulama Kuralı**: {summary.get('total_rules', 0)}",
        f"- **Doğrulama Sonucu**: {summary.get('validation_status', 'PASS')}",
        f"- **Yasaklı İddia Tespiti**: {summary.get('forbidden_claims_found', 0)}",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        md.append(_df_to_markdown(validation_df))
    return "\n".join(md)


def build_data_lineage_safety_markdown_report(
    summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Data Lineage Safety Boundary Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam No-Go Kuralı**: {summary.get('total_no_go', 0)}",
        f"- **Toplam Safe-Go Kuralı**: {summary.get('total_safe_go', 0)}",
        f"- **Güvenlik Durumu**: {summary.get('safety_status', 'ACTIVE_ENFORCED')}",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        md.append(_df_to_markdown(safety_df))
    return "\n".join(md)


def build_phase_115_handoff_markdown_report(
    summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115 Data Provider Benchmark Handoff Report",
        build_data_lineage_disclaimer(),
        f"- **Toplam Devir Maddesi**: {summary.get('total_handoff_items', 0)}",
        f"- **Hedef Faz**: {summary.get('target_phase', 115)} ({summary.get('target_phase_name', 'Data Provider Benchmark Report')})",
        f"- **Manuel İnceleme Sayısı**: {summary.get('manual_review_count', 0)}",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        md.append(_df_to_markdown(handoff_df))
    return "\n".join(md)
