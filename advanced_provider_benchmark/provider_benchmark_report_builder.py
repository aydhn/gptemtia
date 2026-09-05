from typing import Dict, Any, Optional
import pandas as pd


PROVIDER_BENCHMARK_DISCLAIMER_TEXT = (
    "Bu çıktı Phase 115 Data Provider Benchmark Report raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, "
    "benchmark score’u trade sinyali olarak kullanma, provider official approval, "
    "production-ready/broker-ready iddiası, production deployment, model deployment, "
    "scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, "
    "gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir."
)


def build_provider_benchmark_disclaimer() -> str:
    return f"> **UYARI VE SINIRLAR**:\n> {PROVIDER_BENCHMARK_DISCLAIMER_TEXT}\n"


def _df_to_markdown_table(df: Optional[pd.DataFrame]) -> str:
    if df is None or df.empty:
        return "_Kayıt bulunamadı._\n"
    try:
        return df.to_markdown(index=False) + "\n"
    except Exception:
        cols = list(df.columns)
        header = "| " + " | ".join(str(c) for c in cols) + " |"
        sep = "| " + " | ".join("---" for _ in cols) + " |"
        rows = []
        for _, row in df.iterrows():
            rows.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
        return "\n".join([header, sep] + rows) + "\n"



def build_provider_benchmark_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Benchmark Profile Registry",
        build_provider_benchmark_disclaimer(),
        f"- **Toplam Profil Sayısı**: {summary.get('total_profiles', 0)}",
        f"- **Yerel / Offline Zorunluluğu**: {summary.get('all_local_only', True)}",
        f"- **Production-Dışı**: {summary.get('all_non_production', True)}",
        f"- **Mevcut Faz**: {summary.get('current_phase', 115)} | **Hedef Faz**: {summary.get('target_final_phase', 160)}",
        "\n### Tanımlı Benchmark Profilleri",
        _df_to_markdown_table(profile_df),
    ]
    return "\n".join(md)


def build_provider_benchmark_metric_markdown_report(
    summary: Dict[str, Any], metric_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Benchmark Metric Registry",
        build_provider_benchmark_disclaimer(),
        f"- **Toplam Metrik Sayısı**: {summary.get('total_metrics', 0)}",
        f"- **Manuel İnceleme Gerektiren Metrik Sayısı**: {summary.get('manual_review_metrics_count', 0)}",
        "\n### Tanımlı Metrikler",
        _df_to_markdown_table(metric_df),
    ]
    return "\n".join(md)


def build_provider_coverage_markdown_report(
    summary: Dict[str, Any], coverage_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Coverage Benchmark Report",
        build_provider_benchmark_disclaimer(),
        f"- **Değerlendirilen Sağlayıcı Sayısı**: {summary.get('total_providers_evaluated', 0)}",
        f"- **Ortalama Kapsam Puanı**: {summary.get('mean_coverage_score', 0.0)}",
        f"- **Manuel İnceleme Sayısı**: {summary.get('manual_review_count', 0)}",
        "\n### Kapsam Değerlendirme Tablosu",
        _df_to_markdown_table(coverage_df),
    ]
    return "\n".join(md)


def build_provider_capability_markdown_report(
    summary: Dict[str, Any], capability_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Capability Benchmark Report",
        build_provider_benchmark_disclaimer(),
        f"- **Değerlendirilen Sağlayıcı Sayısı**: {summary.get('total_providers_evaluated', 0)}",
        f"- **Ortalama Yetenek Puanı**: {summary.get('mean_capability_score', 0.0)}",
        "\n### Yetenek Değerlendirme Tablosu",
        _df_to_markdown_table(capability_df),
    ]
    return "\n".join(md)


def build_provider_quality_markdown_report(
    summary: Dict[str, Any], quality_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Quality Benchmark Report",
        build_provider_benchmark_disclaimer(),
        f"- **Değerlendirilen Sağlayıcı Sayısı**: {summary.get('total_providers_evaluated', 0)}",
        f"- **Ortalama Kalite Puanı**: {summary.get('mean_quality_score', 0.0)}",
        "\n### Kalite Değerlendirme Tablosu",
        _df_to_markdown_table(quality_df),
    ]
    return "\n".join(md)


def build_provider_normalization_markdown_report(
    summary: Dict[str, Any], normalization_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Normalization Benchmark Report",
        build_provider_benchmark_disclaimer(),
        f"- **Değerlendirilen Sağlayıcı Sayısı**: {summary.get('total_providers_evaluated', 0)}",
        f"- **Ortalama Normalizasyon Puanı**: {summary.get('mean_normalization_score', 0.0)}",
        "\n### Normalizasyon Değerlendirme Tablosu",
        _df_to_markdown_table(normalization_df),
    ]
    return "\n".join(md)


def build_provider_traceability_markdown_report(
    summary: Dict[str, Any], traceability_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Traceability Benchmark Report",
        build_provider_benchmark_disclaimer(),
        f"- **Değerlendirilen Sağlayıcı Sayısı**: {summary.get('total_providers_evaluated', 0)}",
        f"- **Ortalama İzlenebilirlik Puanı**: {summary.get('mean_traceability_score', 0.0)}",
        "\n### İzlenebilirlik Değerlendirme Tablosu",
        _df_to_markdown_table(traceability_df),
    ]
    return "\n".join(md)


def build_provider_compliance_markdown_report(
    summary: Dict[str, Any], compliance_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Compliance Benchmark Report (No-Scraping & Metadata-Only)",
        build_provider_benchmark_disclaimer(),
        f"- **Tüm Sağlayıcılar No-Scraping Uyumlu**: {summary.get('all_no_scraping_compliant', True)}",
        f"- **Tüm Sağlayıcılar Metadata-Only Uyumlu**: {summary.get('all_zero_full_text', True)}",
        "\n### Uyum Değerlendirme Tablosu",
        _df_to_markdown_table(compliance_df),
    ]
    return "\n".join(md)


def build_domain_provider_benchmark_markdown_report(
    summary: Dict[str, Any], domain_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        f"# Phase 115: {summary.get('domain', 'Domain')} Provider Benchmark Report",
        build_provider_benchmark_disclaimer(),
        f"- **Domain**: {summary.get('domain', 'N/A')}",
        f"- **Değerlendirilen Metrik Sayısı**: {summary.get('total_metrics_evaluated', 0)}",
        f"- **Ortalama Domain Puanı**: {summary.get('mean_domain_score', 0.0)}",
        "\n### Alan Bazlı Değerlendirme Tablosu",
        _df_to_markdown_table(domain_df),
    ]
    return "\n".join(md)


def build_cross_domain_provider_benchmark_markdown_report(
    summary: Dict[str, Any], cross_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Cross-Domain Provider Benchmark Report",
        build_provider_benchmark_disclaimer(),
        f"- **Değerlendirme Sayısı**: {summary.get('total_cross_domain_evaluations', 0)}",
        f"- **Ortalama Uyum Puanı**: {summary.get('mean_cross_domain_score', 0.0)}",
        f"- **Tüm Eşleşmeler Başarılı**: {summary.get('all_alignments_pass', True)}",
        "\n### Çapraz Alan Eşleşme Tablosu",
        _df_to_markdown_table(cross_df),
    ]
    return "\n".join(md)


def build_provider_benchmark_score_markdown_report(
    summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Benchmark Score Report",
        build_provider_benchmark_disclaimer(),
        f"- **Toplam Puanlanan Sağlayıcı**: {summary.get('total_providers_scored', 0)}",
        f"- **Ortalama Benchmark Skoru**: {summary.get('mean_benchmark_score', 0.0)}",
        f"- **En Yüksek Skor**: {summary.get('max_benchmark_score', 0.0)}",
        f"- **En Düşük Skor**: {summary.get('min_benchmark_score', 0.0)}",
        f"- **Official Approval Garantisi**: {summary.get('official_approval_guarantee', False)}",
        f"- **Production/Live Ready Garantisi**: {summary.get('production_ready_guarantee', False)}",
        "\n### Sağlayıcı Benchmark Puanları",
        _df_to_markdown_table(score_df),
    ]
    return "\n".join(md)


def build_provider_ranking_research_markdown_report(
    summary: Dict[str, Any], ranking_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Ranking Research Report",
        build_provider_benchmark_disclaimer(),
        "> **ÖNEMLİ NOT**: Bu sıralama yalnızca araştırma amaçlıdır; resmi onay, broker talimatı veya al/sat sinyali niteliği taşımaz.",
        f"- **Sıralanan Sağlayıcı Sayısı**: {summary.get('total_providers_ranked', 0)}",
        f"- **En Yüksek Uygunluk Puanına Sahip**: {summary.get('top_ranked_provider', 'none')}",
        "\n### Araştırma Sıralama Tablosu",
        _df_to_markdown_table(ranking_df),
    ]
    return "\n".join(md)


def build_provider_benchmark_findings_markdown_report(
    summary: Dict[str, Any], findings_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Benchmark Findings Registry",
        build_provider_benchmark_disclaimer(),
        f"- **Toplam Bulgu Sayısı**: {summary.get('total_findings', 0)}",
        f"- **Yüksek Önem Derecesine Sahip Bulgular**: {summary.get('high_severity_count', 0)}",
        f"- **Manuel İnceleme Gerektirenler**: {summary.get('manual_review_required_count', 0)}",
        "\n### Bulgu Kayıtları",
        _df_to_markdown_table(findings_df),
    ]
    return "\n".join(md)


def build_provider_benchmark_manual_review_markdown_report(
    summary: Dict[str, Any], review_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Benchmark Manual Review Queue",
        build_provider_benchmark_disclaimer(),
        f"- **Kuyruktaki İnceleme Kalemi Sayısı**: {summary.get('total_manual_review_items', 0)}",
        f"- **Yıkıcı İşlem İzni (Destructive Action Allowed)**: {summary.get('destructive_actions_prevented', True)} (Strictly False)",
        "\n### Manuel İnceleme Kuyruğu",
        _df_to_markdown_table(review_df),
    ]
    return "\n".join(md)


def build_provider_benchmark_health_markdown_report(
    summary: Dict[str, Any], health_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Benchmark Health Check",
        build_provider_benchmark_disclaimer(),
        f"- **Genel Durum**: {summary.get('overall_status', 'PASS')}",
        f"- **Toplam Kontrol Sayısı**: {summary.get('total_checks', 0)}",
        f"- **Başarılı Kontroller**: {summary.get('passed_checks', 0)}",
        f"- **Başarısız Kontroller**: {summary.get('failed_checks', 0)}",
        "\n### Sağlık Kontrol Detayları",
        _df_to_markdown_table(health_df),
    ]
    return "\n".join(md)


def build_provider_benchmark_validation_markdown_report(
    summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Benchmark Validation Report",
        build_provider_benchmark_disclaimer(),
        f"- **Doğrulama Durumu**: {summary.get('validation_status', 'VALID')}",
        f"- **Yasaklı İddia Taraması**: {summary.get('forbidden_claims_found', False)}",
        f"- **Geçerli Puan Sınırları [0.0, 1.0]**: {summary.get('scores_valid', True)}",
        "\n### Doğrulama Detayları",
        _df_to_markdown_table(validation_df),
    ]
    return "\n".join(md)


def build_provider_benchmark_safety_markdown_report(
    summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115: Provider Benchmark Safety Boundary Report",
        build_provider_benchmark_disclaimer(),
        f"- **Tanımlı No-Go Kural Sayısı**: {summary.get('total_no_go_rules', 0)}",
        f"- **Tanımlı Safe-Go Kural Sayısı**: {summary.get('total_safe_go_rules', 0)}",
        f"- **Güvenlik Sınırı Durumu**: {summary.get('safety_status', 'ACTIVE')}",
        "\n### Güvenlik Sınırı Tablosu",
        _df_to_markdown_table(safety_df),
    ]
    return "\n".join(md)


def build_phase_116_handoff_markdown_report(
    summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None
) -> str:
    md = [
        "# Phase 115 to Phase 116 Handoff Report: Indicator/Feature/Factor Engine",
        build_provider_benchmark_disclaimer(),
        f"- **Toplam Handoff Kalemi**: {summary.get('total_handoff_items', 0)}",
        f"- **Hedef Faz**: Phase 116 (Advanced Indicator/Feature/Factor Engine)",
        f"- **Özellik/Faktör Hazırlık Durumu**: {summary.get('readiness_status', 'READY')}",
        "\n### Handoff Matrisi",
        _df_to_markdown_table(handoff_df),
    ]
    return "\n".join(md)
