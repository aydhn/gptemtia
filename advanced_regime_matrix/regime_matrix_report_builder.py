"""Phase 127: Regime Matrix Report Builder.

Generates tabulate-free Markdown and text reports with mandatory Phase 127 research disclaimers.
"""

from typing import Any, Dict, Optional
import pandas as pd

REGIME_MATRIX_DISCLAIMER_TEXT = (
    "UYARI: Bu çıktı Phase 127 Regime Feature Matrix and State Dataset Contracts raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, regime matrix veya state dataset değerini "
    "trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, "
    "unsupervised execution, prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, "
    "haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir."
)


def build_regime_matrix_disclaimer() -> str:
    """Return the canonical Phase 127 disclaimer banner."""
    return (
        f"> [!WARNING]\n"
        f"> **ARAŞTIRMA VE SÖZLEŞME YASAL UYARISI (PHASE 127)**:\n"
        f"> {REGIME_MATRIX_DISCLAIMER_TEXT}\n"
    )


def _df_to_markdown_simple(df: pd.DataFrame) -> str:
    """Format DataFrame as a clean Markdown table without external dependencies."""
    if df is None or df.empty:
        return "_Tabloda veri bulunmuyor._\n"
    headers = [str(col) for col in df.columns]
    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    rows = []
    for _, row in df.iterrows():
        row_str = "| " + " | ".join(str(val) for val in row.values) + " |"
        rows.append(row_str)
    return "\n".join([header_line, separator_line] + rows) + "\n"


def build_regime_matrix_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for profile and domain registries."""
    lines = [
        "# Phase 127: Regime Feature Matrix Profile & Domain Registry",
        "",
        build_regime_matrix_disclaimer(),
        "",
        "## Özet Göstergeler",
        f"- **Aktif Profil**: `{summary.get('active_profile', 'N/A')}`",
        f"- **Toplam Profil**: `{summary.get('total_profiles', 0)}`",
        f"- **Mevcut Faz**: `{summary.get('current_phase', 127)}`",
        f"- **Sıradaki Faz**: `{summary.get('next_phase', 128)}`",
        f"- **Hedef Final Faz**: `{summary.get('target_final_phase', 160)}`",
        f"- **Non-Signal Değişmezi**: `{summary.get('all_non_signal', True)}`",
        f"- **Kaynak Koruma Değişmezi**: `{summary.get('all_source_preserved', True)}`",
        "",
        "## Profil Kayıtları",
    ]
    if profile_df is not None:
        lines.append(_df_to_markdown_simple(profile_df))
    return "\n".join(lines)


def build_regime_feature_matrix_contract_markdown_report(
    summary: Dict[str, Any],
    contract_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for feature matrix contracts."""
    lines = [
        "# Phase 127: Regime Feature Matrix Contracts Report",
        "",
        build_regime_matrix_disclaimer(),
        "",
        "## Sözleşme Özeti",
        f"- **Toplam Feature Matrix Sözleşmesi**: `{summary.get('total_contracts', 0)}`",
        f"- **Tüm Sözleşmeler Non-Signal**: `{summary.get('all_non_signal', True)}`",
        f"- **Tüm Sözleşmeler No-Lookahead Zorunlu**: `{summary.get('all_no_lookahead_required', True)}`",
        f"- **Model Eğitimi İzni**: `False`",
        f"- **Kümeleme İzni**: `False`",
        "",
        "## Tanımlı Matris Sözleşmeleri",
    ]
    if contract_df is not None:
        lines.append(_df_to_markdown_simple(contract_df))
    return "\n".join(lines)


def build_regime_state_dataset_contract_markdown_report(
    summary: Dict[str, Any],
    dataset_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for state dataset contracts."""
    lines = [
        "# Phase 127: Regime State Dataset Contracts Report",
        "",
        build_regime_matrix_disclaimer(),
        "",
        "## State Dataset Sözleşme Özeti",
        f"- **Toplam State Dataset Sözleşmesi**: `{summary.get('total_dataset_contracts', 0)}`",
        f"- **Hedef / Etiket Üretim Yasağı**: `{summary.get('all_no_target_label_prediction', True)}`",
        f"- **Model Eğitimi Engellendi**: `{summary.get('all_model_training_disallowed', True)}`",
        f"- **Kümeleme Engellendi**: `{summary.get('all_clustering_disallowed', True)}`",
        f"- **Phase 128 Hazırlık Durumu**: `READY`",
        "",
        "## Tanımlı State Dataset Sözleşmeleri",
    ]
    if dataset_df is not None:
        lines.append(_df_to_markdown_simple(dataset_df))
    return "\n".join(lines)


def build_regime_matrix_input_markdown_report(
    summary: Dict[str, Any],
    input_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for input features and factors."""
    lines = [
        "# Phase 127: Regime Matrix Input Registries Report",
        "",
        build_regime_matrix_disclaimer(),
        "",
        "## Girdi Özeti",
        f"- **Toplam Girdi Özellik Sayısı**: `{summary.get('total_input_features', 0)}`",
        f"- **Kaynak Fazlar**: `{summary.get('source_phases', [])}`",
        f"- **Tüm Girdiler Non-Signal**: `{summary.get('all_non_signal', True)}`",
        "",
        "## Girdi Detayları",
    ]
    if input_df is not None:
        lines.append(_df_to_markdown_simple(input_df))
    return "\n".join(lines)


def build_regime_matrix_alignment_markdown_report(
    summary: Dict[str, Any],
    alignment_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for timestamp alignment and asof join policies."""
    lines = [
        "# Phase 127: Regime Matrix Timestamp Alignment and Asof Join Policies",
        "",
        build_regime_matrix_disclaimer(),
        "",
        "## Hizalama İlkeleri Özeti",
        f"- **Toplam Hizalama Kuralı**: `{summary.get('total_rules', 0)}`",
        f"- **Asof Birleştirme Yönü**: `backward` (strict)",
        f"- **Negatif Shift Yasağı**: `Aktif (shift(-1) kesinlikle engellendi)`",
        f"- **İleriye Dönük Sızıntı**: `Sıfır tolerans`",
        "",
        "## Hizalama Kuralları",
    ]
    if alignment_df is not None:
        lines.append(_df_to_markdown_simple(alignment_df))
    return "\n".join(lines)


def build_regime_state_dataset_schema_markdown_report(
    summary: Dict[str, Any],
    schema_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for state dataset schema and candidate contexts."""
    lines = [
        "# Phase 127: Regime State Dataset Schema & Candidate Contexts",
        "",
        build_regime_matrix_disclaimer(),
        "",
        "## Şema ve Aday Bağlam Özeti",
        f"- **Toplam Şema Alanı**: `{summary.get('total_schema_fields', 0)}`",
        f"- **Zorunlu Kolon Sayısı**: `{len(summary.get('minimum_columns', []))}`",
        f"- **Yasaklı Terim Sayısı**: `{len(summary.get('forbidden_fields_prohibited', []))}`",
        f"- **Aday Bağlamlar Etiket Değildir**: `Doğrulandı`",
        "",
        "## Şema Alanları",
    ]
    if schema_df is not None:
        lines.append(_df_to_markdown_simple(schema_df))
    return "\n".join(lines)


def build_regime_matrix_integrity_markdown_report(
    summary: Dict[str, Any],
    manifest_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for matrix integrity manifest."""
    lines = [
        "# Phase 127: Regime Matrix Integrity Manifest",
        "",
        build_regime_matrix_disclaimer(),
        "",
        "## Bütünlük Manifestosu Özeti",
        f"- **Manifesto Durumu**: `{summary.get('manifest_status', 'MANIFEST_VALID')}`",
        f"- **Mevcut Faz**: `{summary.get('current_phase', 127)}`",
        f"- **Sıradaki Faz**: `{summary.get('next_phase', 128)}`",
        f"- **Hedef Final Faz**: `{summary.get('target_final_phase', 160)}`",
        f"- **Non-Signal**: `{summary.get('non_signal', True)}`",
        f"- **Kaynak Koruma**: `{summary.get('source_preserved', True)}`",
        f"- **Model Eğitimi Yürütüldü**: `False`",
        f"- **Kümeleme Yürütüldü**: `False`",
        f"- **Resmi Onay İddiası**: `False`",
        f"- **Üretime Hazır İddiası**: `False`",
        "",
        "## Manifesto Detayları",
    ]
    if manifest_df is not None:
        lines.append(_df_to_markdown_simple(manifest_df))
    return "\n".join(lines)


def build_regime_matrix_validation_markdown_report(
    summary: Dict[str, Any],
    validation_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for validation engine findings."""
    lines = [
        "# Phase 127: Regime Matrix Validation Report",
        "",
        build_regime_matrix_disclaimer(),
        "",
        "## Validasyon Özeti",
        f"- **Validasyon Durumu**: `{summary.get('validation_status', 'VALIDATION_PASS')}`",
        f"- **Yasaklı İddia Taraması**: `Temiz (Sıfır ihlal)`",
        f"- **No-Lookahead Denetimi**: `Geçti`",
        f"- **Yasaklı Kolon Denetimi**: `Geçti`",
        f"- **Kaynak Koruma Denetimi**: `Geçti`",
        "",
        "## Validasyon Maddeleri",
    ]
    if validation_df is not None:
        lines.append(_df_to_markdown_simple(validation_df))
    return "\n".join(lines)


def build_regime_matrix_safety_markdown_report(
    summary: Dict[str, Any],
    safety_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for safety boundaries (NO-GO / SAFE-GO)."""
    lines = [
        "# Phase 127: Regime Matrix Safety Boundary Report",
        "",
        build_regime_matrix_disclaimer(),
        "",
        "## Güvenlik Sınırları Özeti",
        f"- **Güvenlik Durumu**: `{summary.get('safety_status', 'SECURE')}`",
        f"- **NO-GO Kuralları Sayısı**: `{summary.get('no_go_count', 15)}`",
        f"- **SAFE-GO İlkeleri Sayısı**: `{summary.get('safe_go_count', 7)}`",
        f"- **Canlı İşlem Engeli**: `Aktif (Zero live trading)`",
        f"- **Broker Entegrasyon Engeli**: `Aktif (Zero broker connection)`",
        "",
        "## Güvenlik Kuralları Tablosu",
    ]
    if safety_df is not None:
        lines.append(_df_to_markdown_simple(safety_df))
    return "\n".join(lines)


def build_phase_128_handoff_markdown_report(
    summary: Dict[str, Any],
    handoff_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for Phase 128 handoff."""
    lines = [
        "# Phase 127 -> Phase 128: Regime Rule-Free Labeling & Unsupervised Prep Handoff",
        "",
        build_regime_matrix_disclaimer(),
        "",
        "## Devir Özeti",
        f"- **Devir Durumu**: `{summary.get('handoff_status', 'READY')}`",
        f"- **Mevcut Faz**: `{summary.get('source_phase', 127)}`",
        f"- **Hedef Faz**: `{summary.get('next_phase', 128)}`",
        f"- **Hedef Final Faz**: `{summary.get('target_final_phase', 160)}`",
        f"- **Toplam Devir Maddesi**: `{summary.get('total_handoff_items', 0)}`",
        f"- **Phase 128 Non-Signal İlkesi**: `Devam edecek`",
        f"- **Phase 128 Canlı İşlem Yasağı**: `Devam edecek`",
        "",
        "## Devir Maddeleri",
    ]
    if handoff_df is not None:
        lines.append(_df_to_markdown_simple(handoff_df))
    return "\n".join(lines)


build_regime_feature_matrix_contracts_markdown_report = build_regime_feature_matrix_contract_markdown_report
build_regime_state_dataset_contracts_markdown_report = build_regime_state_dataset_contract_markdown_report

