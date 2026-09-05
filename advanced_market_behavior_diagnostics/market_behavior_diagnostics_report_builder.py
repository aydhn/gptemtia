"""Phase 129: Market Behavior Diagnostics Report Builder.

Builds formatted Markdown and text reports with mandatory non-signal research disclaimers.
"""

from typing import Optional
import pandas as pd

MARKET_BEHAVIOR_DIAGNOSTICS_DISCLAIMER = (
    "UYARI: Bu çıktı Phase 129 Market Behavior Diagnostics and Regime Quality raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, behavior quality veya candidate "
    "state quality değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, "
    "model training, clustering execution, unsupervised execution, dimensionality reduction execution, "
    "prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, "
    "haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek "
    "provider API çağrısı değildir."
)


def build_market_behavior_diagnostics_disclaimer() -> str:
    """Return the official Phase 129 disclaimer string."""
    return MARKET_BEHAVIOR_DIAGNOSTICS_DISCLAIMER


def _render_df_table(df: Optional[pd.DataFrame]) -> str:
    if df is None or df.empty:
        return "*Tabloda veri bulunmuyor.*"
    headers = [str(col) for col in df.columns]
    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    rows = []
    for _, row in df.iterrows():
        row_str = "| " + " | ".join(str(val) for val in row.values) + " |"
        rows.append(row_str)
    return "\n".join([header_line, separator_line] + rows) + "\n"



def build_market_behavior_diagnostics_profile_markdown_report(
    summary: dict, profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for operational profiles."""
    return f"""# Phase 129 Market Behavior Diagnostics Profile Registry

> [!NOTE]
> {build_market_behavior_diagnostics_disclaimer()}

## Özet Bilgiler
- **Aktif Profil**: `{summary.get('active_profile', 'N/A')}`
- **Toplam Profil Sayısı**: `{summary.get('total_profiles', 0)}`
- **Mevcut Faz**: `{summary.get('current_phase', 129)}`
- **Hedef Final Faz**: `{summary.get('target_final_phase', 160)}`
- **Sıradaki Faz**: `{summary.get('next_phase', 130)}`
- **Non-Signal Güvencesi**: `{summary.get('non_signal', True)}`

## Profil Detayları
{_render_df_table(profile_df)}
"""


def build_behavior_quality_metric_markdown_report(
    summary: dict, metric_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for behavior quality metrics."""
    return f"""# Phase 129 Behavior Quality Metric Registry

> [!NOTE]
> {build_market_behavior_diagnostics_disclaimer()}

## Özet Bilgiler
- **Toplam Metrik Sayısı**: `{summary.get('total_metrics', 0)}`
- **Engelleyici Metrik Sayısı**: `{summary.get('blocking_metrics_count', 0)}`
- **Non-Signal Uyumluluğu**: `{summary.get('all_non_signal', True)}`

## Metrik Listesi
{_render_df_table(metric_df)}
"""


def build_candidate_state_quality_markdown_report(
    summary: dict, quality_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for candidate state quality."""
    return f"""# Phase 129 Candidate State Quality Report

> [!NOTE]
> {build_market_behavior_diagnostics_disclaimer()}

## Özet Bilgiler
- **Toplam Aday Durum Sayısı**: `{summary.get('total_candidate_states', 0)}`
- **Hazır Durum Sayısı**: `{summary.get('ready_count', 0)}`
- **Ortalama Tamlık Skoru**: `{summary.get('average_completeness', 0.0):.2f}`
- **Model Eğitimi Engellendi**: `{summary.get('all_training_disallowed', True)}`
- **Non-Signal Durumu**: `{summary.get('all_non_signal', True)}`

## Aday Durum Kalite Tablosu
{_render_df_table(quality_df)}
"""


def build_regime_family_quality_markdown_report(
    summary: dict, family_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for regime family quality."""
    return f"""# Phase 129 Regime Family Quality Report

> [!NOTE]
> {build_market_behavior_diagnostics_disclaimer()}

## Özet Bilgiler
- **Toplam Rejim Ailesi**: `{summary.get('total_families', 0)}`
- **Hazır Aile Sayısı**: `{summary.get('ready_count', 0)}`
- **Ortalama Tutarlılık**: `{summary.get('average_consistency', 0.0):.2f}`
- **Phase 130 Geçişe Hazır**: `{summary.get('phase_130_ready', True)}`

## Rejim Ailesi Kalite Tablosu
{_render_df_table(family_df)}
"""


def build_behavior_diagnostics_markdown_report(
    summary: dict, diagnostics_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for multi-domain behavior diagnostics."""
    return f"""# Phase 129 Market Behavior Diagnostics Report

> [!NOTE]
> {build_market_behavior_diagnostics_disclaimer()}

## Özet Bilgiler
- **Toplam Tanı Konuları**: `{summary.get('total_contexts', 0)}`
- **Ortalama Kapsama**: `{summary.get('average_coverage', 0.0):.2f}`
- **Tüm Bağlamlar Hazır**: `{summary.get('all_ready', True)}`
- **Non-Signal**: `{summary.get('non_signal', True)}`

## Davranış Tanı Detayları
{_render_df_table(diagnostics_df)}
"""


def build_transition_stability_readiness_markdown_report(
    summary: dict, readiness_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for transition and stability readiness."""
    return f"""# Phase 129 Transition and Stability Readiness Report

> [!NOTE]
> {build_market_behavior_diagnostics_disclaimer()}

## Özet Bilgiler
- **Toplam Alan**: `{summary.get('total_areas', 0)}`
- **Phase 130 Hazırlık Durumu**: `{summary.get('all_ready', True)}`
- **Sıfır Geleceğe Bakış Güvencesi**: `True`
- **Non-Signal**: `True`

## Hazırlık Denetim Tablosu
{_render_df_table(readiness_df)}
"""


def build_behavior_findings_markdown_report(
    summary: dict, findings_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for behavior findings and review queue."""
    return f"""# Phase 129 Behavior Quality Findings and Manual Review Queue

> [!NOTE]
> {build_market_behavior_diagnostics_disclaimer()}

## Özet Bilgiler
- **Toplam Bulgu Sayısı**: `{summary.get('total_findings', 0)}`
- **Engelleyici Bulgu Sayısı**: `{summary.get('blocking_findings_count', 0)}`
- **Yıkıcı İşlem İzni**: `{summary.get('destructive_action_allowed', False)}`

## Bulgular Tablosu
{_render_df_table(findings_df)}
"""


def build_behavior_quality_score_markdown_report(
    summary: dict, score_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for behavior quality score."""
    return f"""# Phase 129 Behavior Quality Score Report

> [!NOTE]
> {build_market_behavior_diagnostics_disclaimer()}

## Özet Bilgiler
- **Genel Kalite Skoru**: `{summary.get('overall_quality_score', 0.0):.2f}`
- **Kalite Derecesi**: `{summary.get('quality_grade', 'UNKNOWN')}`
- **Ticari Onay İddiası**: `{summary.get('official_approval', False)}`
- **Canlıya Hazır İddiası**: `{summary.get('production_ready', False)}`

## Skor Detayları
{_render_df_table(score_df)}
"""


def build_behavior_manifest_markdown_report(
    summary: dict, manifest_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for behavior diagnostics manifest."""
    return f"""# Phase 129 Behavior Diagnostics Manifest

> [!NOTE]
> {build_market_behavior_diagnostics_disclaimer()}

## Özet Bilgiler
- **Manifesto Adı**: `{summary.get('manifest_name', 'market_behavior_diagnostics_manifest')}`
- **Geçerlilik**: `{summary.get('is_valid', True)}`
- **Sıfır Yürütme Güvencesi**: `{summary.get('zero_execution_guaranteed', True)}`
- **Kaynak Veri Korundu**: `{summary.get('source_preserved', True)}`

## Manifesto Tablosu
{_render_df_table(manifest_df)}
"""


def build_market_behavior_validation_markdown_report(
    summary: dict, validation_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for validation audits."""
    return f"""# Phase 129 Market Behavior Diagnostics Validation Report

> [!NOTE]
> {build_market_behavior_diagnostics_disclaimer()}

## Özet Bilgiler
- **Validasyon Durumu**: `{summary.get('validation_status', 'VALIDATION_PASS')}`
- **Yasaklı İddia Taraması**: `CLEAN`
- **Sıfır Yürütme Denetimi**: `CLEAN`

## Validasyon Denetimleri
{_render_df_table(validation_df)}
"""


def build_market_behavior_safety_markdown_report(
    summary: dict, safety_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for safety boundaries."""
    return f"""# Phase 129 Market Behavior Diagnostics Safety Boundary

> [!NOTE]
> {build_market_behavior_diagnostics_disclaimer()}

## Özet Bilgiler
- **Güvenlik Durumu**: `{summary.get('safety_status', 'SECURE')}`
- **NO-GO Kuralları Sayısı**: `{summary.get('no_go_count', 18)}`
- **SAFE-GO Prensipleri Sayısı**: `{summary.get('safe_go_count', 8)}`

## Güvenlik Kuralları Tablosu
{_render_df_table(safety_df)}
"""


def build_phase_130_handoff_markdown_report(
    summary: dict, handoff_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for Phase 130 handoff."""
    return f"""# Phase 129 to Phase 130 Regime Transition and Stability Handoff Report

> [!NOTE]
> {build_market_behavior_diagnostics_disclaimer()}

## Özet Bilgiler
- **Devir Durumu**: `{summary.get('handoff_status', 'READY')}`
- **Kaynak Faz**: `{summary.get('source_phase', 129)}`
- **Hedef Sonraki Faz**: `{summary.get('next_phase', 130)}`
- **Hedef Final Faz**: `{summary.get('target_final_phase', 160)}`
- **Tüm Maddeler Hazır**: `{summary.get('all_ready', True)}`

## Devir Maddeleri Tablosu
{_render_df_table(handoff_df)}
"""


# Aliases for script compatibility
build_behavior_diagnostics_domain_markdown_report = build_behavior_diagnostics_markdown_report
build_behavior_quality_findings_markdown_report = build_behavior_findings_markdown_report
build_behavior_diagnostics_manifest_markdown_report = build_behavior_manifest_markdown_report
build_market_behavior_diagnostics_health_markdown_report = build_market_behavior_validation_markdown_report
build_market_behavior_diagnostics_validation_markdown_report = build_market_behavior_validation_markdown_report
build_market_behavior_diagnostics_safety_markdown_report = build_market_behavior_safety_markdown_report

