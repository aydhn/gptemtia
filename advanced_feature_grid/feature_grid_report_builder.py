from typing import Dict, Any, Optional
import pandas as pd


FEATURE_GRID_DISCLAIMER = (
    "Bu çıktı Phase 118 Multi-Window Feature Grid raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, feature grid değerini trade sinyali "
    "olarak kullanma, strateji üretimi, backtest, optimizer, prediction/target/label üretimi, "
    "production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval değildir."
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


def build_feature_grid_disclaimer() -> str:
    return FEATURE_GRID_DISCLAIMER


def build_feature_grid_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Phase 118: Multi-Window Feature Grid Profile Report",
        "",
        f"> {FEATURE_GRID_DISCLAIMER}",
        "",
        "## Profile Özeti",
        f"- **Aktif Profil**: `{summary.get('active_profile', 'unknown')}`",
        f"- **Toplam Profil Sayısı**: {summary.get('total_profiles', 0)}",
        f"- **Mevcut Faz**: {summary.get('current_phase', 118)}",
        f"- **Hedef Faz**: {summary.get('target_final_phase', 160)}",
        f"- **Sonraki Faz**: {summary.get('next_phase', 119)}",
        f"- **Local Only / Research Only**: {summary.get('local_only', True)}",
        f"- **Non-Signal Güvencesi**: {summary.get('non_signal', True)}",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.extend(["## Profil Detayları", "", _df_to_markdown(profile_df), ""])
    return "\n".join(lines)


def build_window_grid_contract_markdown_report(
    summary: Dict[str, Any], contract_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Phase 118: Window Grid Contracts Report",
        "",
        f"> {FEATURE_GRID_DISCLAIMER}",
        "",
        "## Sözleşme Özeti",
        f"- **Toplam Sözleşme Sayısı**: {summary.get('total_contracts', 0)}",
        f"- **Toplam Aile Sayısı**: {summary.get('total_families', 0)}",
        f"- **Sözleşme Başına Ortalama Pencere**: {summary.get('avg_windows_per_contract', 0.0):.1f}",
        f"- **Tümü Geriye Dönük (No-Lookahead)**: {summary.get('all_strictly_backward_looking', True)}",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if contract_df is not None and not contract_df.empty:
        lines.extend(["## Sözleşme Listesi", "", _df_to_markdown(contract_df), ""])
    return "\n".join(lines)


def build_parameter_grid_markdown_report(
    summary: Dict[str, Any], parameter_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Phase 118: Indicator Parameter Grid Registry Report",
        "",
        f"> {FEATURE_GRID_DISCLAIMER}",
        "",
        "## Parametre Grid Özeti",
        f"- **Toplam Grid Sayısı**: {summary.get('total_grids', 0)}",
        f"- **Toplam Aile**: {summary.get('total_families', 0)}",
        f"- **Beklenen Toplam Feature Sayısı**: {summary.get('total_expected_features', 0)}",
        f"- **Non-Signal**: {summary.get('non_signal', True)}",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if parameter_df is not None and not parameter_df.empty:
        lines.extend(["## Parametre Gridleri", "", _df_to_markdown(parameter_df), ""])
    return "\n".join(lines)


def build_feature_grid_family_markdown_report(
    summary: Dict[str, Any], family_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Phase 118: Window Grid Family Report",
        "",
        f"> {FEATURE_GRID_DISCLAIMER}",
        "",
        "## Aile Özeti",
        f"- **Toplam Grid Feature**: {summary.get('total_grid_features', 0)}",
        f"- **Toplam İndikatör**: {summary.get('total_indicators', 0)}",
        f"- **Non-Signal**: {summary.get('non_signal', True)}",
        f"- **Durum**: `{summary.get('status', 'READY')}`",
        "",
    ]
    if family_df is not None and not family_df.empty:
        lines.extend(["## Grid Feature Listesi", "", _df_to_markdown(family_df), ""])
    return "\n".join(lines)


def build_feature_grid_rehearsal_markdown_report(
    summary: Dict[str, Any], rehearsal_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Phase 118: Feature Grid Computation Rehearsal Report",
        "",
        f"> {FEATURE_GRID_DISCLAIMER}",
        "",
        "## Prova ve Doğrulama Özeti",
        f"- **Toplam Prova Koşumu**: {summary.get('total_rehearsals', 0)}",
        f"- **Tüm Provalar Başarılı**: {summary.get('all_passed', True)}",
        f"- **In-Place Mutasyon Engellendi**: {summary.get('no_mutation_guaranteed', True)}",
        f"- **Üretilen Toplam Feature**: {summary.get('total_features_generated', 0)}",
        f"- **Non-Signal**: {summary.get('non_signal', True)}",
        f"- **Durum**: `{summary.get('status', 'PASS')}`",
        "",
    ]
    if rehearsal_df is not None and not rehearsal_df.empty:
        lines.extend(["## Prova Detayları", "", _df_to_markdown(rehearsal_df), ""])
    return "\n".join(lines)


def build_feature_grid_validation_markdown_report(
    summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Phase 118: Feature Grid Validation Report",
        "",
        f"> {FEATURE_GRID_DISCLAIMER}",
        "",
        "## Validasyon Özeti",
        f"- **Validasyon Durumu**: `{summary.get('validation_status', 'PASS')}`",
        f"- **Denetlenen Kural Sayısı**: {summary.get('rules_checked', 0)}",
        f"- **İhlal Sayısı**: {summary.get('violations_count', 0)}",
        f"- **Yasaklı İddia/Kolon Tespit Edilmedi**: {summary.get('no_forbidden_claims', True)}",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.extend(["## Validasyon Bulguları", "", _df_to_markdown(validation_df), ""])
    return "\n".join(lines)


def build_feature_grid_health_markdown_report(
    summary: Dict[str, Any], health_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Phase 118: Multi-Window Feature Grid Health Check Report",
        "",
        f"> {FEATURE_GRID_DISCLAIMER}",
        "",
        "## Sağlık Durumu Özeti",
        f"- **Genel Sağlık**: `{summary.get('health_status', 'HEALTHY')}`",
        f"- **Kontrol Edilen Bileşen Sayısı**: {summary.get('total_components', 0)}",
        f"- **Tüm Bileşenler Sağlıklı**: {summary.get('all_healthy', True)}",
        f"- **Phase 117 ve 116 Entegrasyonu**: {summary.get('prior_phases_healthy', True)}",
        "",
    ]
    if health_df is not None and not health_df.empty:
        lines.extend(["## Bileşen Sağlık Durumu", "", _df_to_markdown(health_df), ""])
    return "\n".join(lines)


def build_feature_grid_safety_markdown_report(
    summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Phase 118: Feature Grid Safety Boundary Report",
        "",
        f"> {FEATURE_GRID_DISCLAIMER}",
        "",
        "## Güvenlik Sınırları Özeti",
        f"- **Güvenlik Durumu**: `{summary.get('safety_status', 'ACTIVE')}`",
        f"- **No-Go Koşul Sayısı**: {summary.get('total_no_go', 0)}",
        f"- **Safe-Go Koşul Sayısı**: {summary.get('total_safe_go', 0)}",
        f"- **Kesin Yasaklar Aktif**: {summary.get('strict_boundaries_enforced', True)}",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.extend(["## Sınır Matrisi", "", _df_to_markdown(safety_df), ""])
    return "\n".join(lines)


def build_phase_119_handoff_markdown_report(
    summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Phase 118: Phase 119 Cross-Asset Feature Alignment Handoff Report",
        "",
        f"> {FEATURE_GRID_DISCLAIMER}",
        "",
        "## Handoff Özeti",
        f"- **Handoff Durumu**: `{summary.get('handoff_status', 'READY')}`",
        f"- **Aktarılan Madde Sayısı**: {summary.get('total_handoff_items', 0)}",
        f"- **Hedef Faz**: {summary.get('next_phase', 119)}",
        f"- **Nihai Hedef**: {summary.get('target_final_phase', 160)}",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.extend(["## Handoff Başlıkları", "", _df_to_markdown(handoff_df), ""])
    return "\n".join(lines)
