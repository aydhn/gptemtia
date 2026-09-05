from typing import Dict, Any, Optional
import pandas as pd

DISCLAIMER_TEXT = (
    "Bu çıktı Phase 117 Technical Indicator Expansion raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, indicator/feature "
    "değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, "
    "prediction/target/label üretimi, production deployment, model deployment, "
    "scraping, gerçek provider API çağrısı veya official approval değildir."
)


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


def build_technical_indicator_disclaimer() -> str:
    return DISCLAIMER_TEXT


def build_technical_indicator_profile_markdown_report(summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 117 Technical Indicator Profile Registry Report",
        "",
        f"> **Yasal Uyarı / Sınır:** {DISCLAIMER_TEXT}",
        "",
        "## Özet",
        f"- **Toplam Profil Sayısı:** {summary.get('total_profiles', 0)}",
        f"- **Mevcut Faz:** {summary.get('current_phase', 117)}",
        f"- **Hedef Final Faz:** {summary.get('target_final_phase', 160)}",
        f"- **Sıradaki Faz:** {summary.get('next_phase', 118)}",
        f"- **Varsayılan Profil:** `{summary.get('default_profile', 'balanced_local_technical_indicators')}`",
        f"- **Non-Signal Güvencesi:** `{summary.get('non_signal_guaranteed', True)}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        md.append("## Kayıtlı Profiller")
        md.append(_df_to_markdown(profile_df))
        md.append("")
    return "\n".join(md)


def build_technical_indicator_catalog_markdown_report(summary: Dict[str, Any], catalog_df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 117 Technical Indicator Catalog Expansion Report",
        "",
        f"> **Yasal Uyarı / Sınır:** {DISCLAIMER_TEXT}",
        "",
        "## Özet",
        f"- **Toplam İndikatör Sayısı:** {summary.get('total_indicators', 0)}",
        f"- **Toplam İndikatör Ailesi:** {summary.get('total_families', 0)}",
        f"- **Durum:** `{summary.get('status', 'READY')}`",
        "",
    ]
    if catalog_df is not None and not catalog_df.empty:
        md.append("## İndikatör Kataloğu")
        cols = ["indicator_name", "indicator_family", "required_fields", "output_fields", "warmup_policy", "status_label"]
        available_cols = [c for c in cols if c in catalog_df.columns]
        md.append(_df_to_markdown(catalog_df[available_cols]))
        md.append("")
    return "\n".join(md)


def build_indicator_family_markdown_report(summary: Dict[str, Any], family_df: Optional[pd.DataFrame] = None) -> str:
    md = [
        f"# Phase 117 Indicator Family Report: {summary.get('family', 'Indicator Family')}",
        "",
        f"> **Yasal Uyarı / Sınır:** {DISCLAIMER_TEXT}",
        "",
        f"- **İndikatör Sayısı:** {summary.get('total_indicators', 0)}",
        f"- **Non-Signal Durumu:** `{summary.get('non_signal', True)}`",
        "",
    ]
    if family_df is not None and not family_df.empty:
        md.append("## Göstergeler")
        md.append(_df_to_markdown(family_df))
        md.append("")
    return "\n".join(md)


def build_indicator_parameter_contract_markdown_report(summary: Dict[str, Any], parameter_df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 117 Indicator Parameter Contracts Report",
        "",
        f"> **Yasal Uyarı / Sınır:** {DISCLAIMER_TEXT}",
        "",
        f"- **Toplam Kontrat:** {summary.get('total_parameter_contracts', 0)}",
        f"- **Kapsanan İndikatör Sayısı:** {summary.get('total_indicators_covered', 0)}",
        "",
    ]
    if parameter_df is not None and not parameter_df.empty:
        md.append("## Parametre Kontratları")
        md.append(_df_to_markdown(parameter_df))
        md.append("")
    return "\n".join(md)


def build_indicator_output_schema_markdown_report(summary: Dict[str, Any], schema_df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 117 Indicator Output Schema Registry Report",
        "",
        f"> **Yasal Uyarı / Sınır:** {DISCLAIMER_TEXT}",
        "",
        f"- **Toplam Şema:** {summary.get('total_schemas', 0)}",
        f"- **Yasaklı Kolon Kontrolü:** `{summary.get('forbidden_check_active', True)}`",
        "",
    ]
    if schema_df is not None and not schema_df.empty:
        md.append("## Çıktı Şemaları")
        md.append(_df_to_markdown(schema_df))
        md.append("")
    return "\n".join(md)


def build_indicator_rehearsal_markdown_report(summary: Dict[str, Any], rehearsal_df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 117 Indicator Computation Rehearsal Report",
        "",
        f"> **Yasal Uyarı / Sınır:** {DISCLAIMER_TEXT}",
        "",
        f"- **Toplam Prova Sayısı:** {summary.get('total_rehearsals', 0)}",
        f"- **Tüm Provalar Başarılı:** `{summary.get('all_passed', True)}`",
        f"- **Input Mutation-Free:** `{summary.get('no_mutation_guaranteed', True)}`",
        f"- **Non-Signal Çıktı:** `{summary.get('non_signal', True)}`",
        "",
    ]
    if rehearsal_df is not None and not rehearsal_df.empty:
        md.append("## Prova Sonuçları")
        md.append(_df_to_markdown(rehearsal_df))
        md.append("")
    return "\n".join(md)


def build_indicator_validation_markdown_report(summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 117 Technical Indicator Validation Report",
        "",
        f"> **Yasal Uyarı / Sınır:** {DISCLAIMER_TEXT}",
        "",
        f"- **Doğrulama Durumu:** `{summary.get('validation_status', 'PASS')}`",
        f"- **Toplam Kural:** {summary.get('total_rules_checked', 0)}",
        f"- **Hata Sayısı:** {summary.get('total_violations', 0)}",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        md.append("## Doğrulama Detayları")
        md.append(_df_to_markdown(validation_df))
        md.append("")
    return "\n".join(md)


def build_technical_indicator_health_markdown_report(summary: Dict[str, Any], health_df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 117 Technical Indicator Health Check Report",
        "",
        f"> **Yasal Uyarı / Sınır:** {DISCLAIMER_TEXT}",
        "",
        f"- **Genel Sağlık Durumu:** `{summary.get('health_status', 'HEALTHY')}`",
        f"- **Kontrol Edilen Bileşenler:** {summary.get('total_checks', 0)}",
        "",
    ]
    if health_df is not None and not health_df.empty:
        md.append("## Sağlık Kontrol Tablosu")
        md.append(_df_to_markdown(health_df))
        md.append("")
    return "\n".join(md)


def build_technical_indicator_safety_markdown_report(summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 117 Technical Indicator Safety Boundary Report",
        "",
        f"> **Yasal Uyarı / Sınır:** {DISCLAIMER_TEXT}",
        "",
        f"- **Güvenlik Durumu:** `{summary.get('safety_status', 'ACTIVE')}`",
        f"- **No-Go Kuralları:** {summary.get('total_no_go', 0)}",
        f"- **Safe-Go Kuralları:** {summary.get('total_safe_go', 0)}",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        md.append("## Güvenlik Sınırları Tablosu")
        md.append(_df_to_markdown(safety_df))
        md.append("")
    return "\n".join(md)


def build_phase_118_handoff_markdown_report(summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 117 to Phase 118 Multi-Window Feature Grid Handoff Report",
        "",
        f"> **Yasal Uyarı / Sınır:** {DISCLAIMER_TEXT}",
        "",
        f"- **Devir Durumu:** `{summary.get('handoff_status', 'READY')}`",
        f"- **Hedef Faz:** {summary.get('next_phase', 118)}",
        f"- **Devir Edilen Maddeler:** {summary.get('total_handoff_items', 0)}",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        md.append("## Devir Maddeleri")
        md.append(_df_to_markdown(handoff_df))
        md.append("")
    return "\n".join(md)
