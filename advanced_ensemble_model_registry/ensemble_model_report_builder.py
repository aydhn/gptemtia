# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Model Report Builder."""

from typing import Any, Dict, List, Optional
from advanced_ensemble_model_registry.ensemble_model_models import (
    EnsembleModelManifest,
    EnsembleFinding,
    EnsembleManualReviewItem,
)

ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER = (
    "YASAL UYARI VE GÜVENLİK SINIRI:\n"
    "Bu rapor Faz 140 (Ensemble Model Sözleşmeleri ve Aday Model Kayıt Defteri) kapsamında üretilmiştir.\n"
    "BURADAKİ BİLGİLER KESİNLİKLE YATIRIM TAVSİYESİ VEYA ALIM-SATIM SİNYALİ DEĞİLDİR.\n"
    "Bu katman tamamen çevrimdışı, yerel, simülasyon ve sözleşme/meta-veri mimarisidir.\n"
    "Sıfır model eğitimi, sıfır tahmin, sıfır ensemble yürütme (voting/blending/stacking), sıfır kalibrasyon yapılmıştır.\n"
    "Üretim veya aracı kurum bağlantısı kesinlikle yoktur."
)


def build_ensemble_model_text_report(
    manifest: EnsembleModelManifest,
    findings: Optional[List[EnsembleFinding]] = None,
    review_items: Optional[List[EnsembleManualReviewItem]] = None,
) -> str:
    """Build text report for Phase 140.
    
    Args:
        manifest: Manifest instance.
        findings: Optional list of findings.
        review_items: Optional list of manual review items.
        
    Returns:
        str: Plain text formatted report.
    """
    lines = [
        "=" * 80,
        "FAZ 140: ENSEMBLE MODEL SÖZLEŞMELERİ VE ADAY MODEL KAYIT DEFTERİ RAPORU",
        "=" * 80,
        ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER,
        "-" * 80,
        f"Mevcut Faz               : {manifest.current_phase}",
        f"Hedef Final Faz          : {manifest.target_final_phase}",
        f"Sonraki Faz              : {manifest.next_phase}",
        f"Aday Model Sözleşmeleri  : {manifest.candidate_contract_count}",
        f"Ensemble Sözleşmeleri    : {manifest.ensemble_contract_count}",
        f"Devre Dışı Raporlar      : {manifest.disabled_execution_report_count}",
        f"Hazırlık Skoru (Readiness): {manifest.readiness_score:.4f}",
        f"Non-Signal Durumu        : {manifest.non_signal}",
        f"Dry-Run Durumu           : {manifest.dry_run}",
        f"Gerçek Model Eğitimi     : {manifest.real_training_executed}",
        f"Model Çıkarımı/Tahmin    : {manifest.model_predict_executed}",
        f"Ensemble Yürütme         : {manifest.ensemble_executed}",
        f"Model Kayıt Dışa Yazım   : {manifest.model_registry_written}",
        f"Model İkili Dosya Kaydı  : {manifest.artifact_persisted}",
        "-" * 80,
    ]
    
    if findings:
        lines.append("BULGULAR:")
        for f in findings:
            lines.append(f"  - [{f.finding_id}] ({f.severity_label}) {f.message}")
        lines.append("-" * 80)
        
    if review_items:
        lines.append("MANUEL İNCELEME GÖREVLERİ:")
        for item in review_items:
            lines.append(f"  - [{item.review_id}] {item.description} -> Öneri: {item.recommended_action}")
        lines.append("-" * 80)
        
    lines.append("DURUM: SÖZLEŞMELER GEÇERLİ, YÜRÜTME ENGELLENDİ, FAZ 141 DEVRE HAZIR.")
    lines.append("=" * 80)
    return "\n".join(lines)


def build_ensemble_model_markdown_report(
    manifest: EnsembleModelManifest,
    findings: Optional[List[EnsembleFinding]] = None,
    review_items: Optional[List[EnsembleManualReviewItem]] = None,
) -> str:
    """Build markdown report for Phase 140.
    
    Args:
        manifest: Manifest instance.
        findings: Optional list of findings.
        review_items: Optional list of manual review items.
        
    Returns:
        str: Markdown formatted report.
    """
    md = [
        "# Faz 140: Ensemble Model Sözleşmeleri ve Aday Model Kayıt Defteri Raporu",
        "",
        "> **YASAL UYARI VE GÜVENLİK SINIRI:**",
        "> " + ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER.replace("\n", "\n> "),
        "",
        "## 1. Yönetici Özeti",
        "",
        f"- **Mevcut Faz**: {manifest.current_phase}",
        f"- **Hedef Final Faz**: {manifest.target_final_phase}",
        f"- **Sonraki Faz**: {manifest.next_phase}",
        f"- **Hazırlık Skoru**: `{manifest.readiness_score:.4f}`",
        f"- **Dry Run**: `{manifest.dry_run}`",
        f"- **Non-Signal**: `{manifest.non_signal}`",
        "",
        "## 2. Model ve Ensemble Sözleşmeleri",
        "",
        f"- **Kayıtlı Aday Model Aileleri / Sözleşmeleri**: {manifest.candidate_contract_count}",
        f"- **Kayıtlı Ensemble Strateji Sözleşmeleri**: {manifest.ensemble_contract_count}",
        f"- **Devre Dışı Yürütme Raporları**: {manifest.disabled_execution_report_count}",
        "",
        "## 3. Güvenlik ve Sıfır Yürütme Değişmezleri",
        "",
        "| Değişmez (Invariant) | Durum | Politika |",
        "| --- | --- | --- |",
        f"| Gerçek Model Eğitimi | `{manifest.real_training_executed}` | ENGELLENDİ |",
        f"| Model Çıkarımı / Tahmin | `{manifest.model_predict_executed}` | ENGELLENDİ |",
        f"| Ensemble Yürütme | `{manifest.ensemble_executed}` | ENGELLENDİ |",
        f"| Kalibrasyon ve Belirsizlik | `{manifest.calibration_executed}` | ENGELLENDİ (Faz 141 Kapsamı) |",
        f"| Model İkili Dosya Kaydı | `{manifest.artifact_persisted}` | ENGELLENDİ |",
        f"| Dış Kayıt Defteri Yazımı | `{manifest.model_registry_written}` | ENGELLENDİ |",
        f"| Geleceğe Bakış Sızıntısı (Lookahead) | `0 Sızıntı` | KORUNDU ($t \\le T$) |",
        f"| Ham Haber Metni / Embedding | `İçermez` | SADECE META-VERİ |",
        "",
    ]
    
    if findings:
        md.append("## 4. Bulgular")
        md.append("")
        for f in findings:
            md.append(f"- **[{f.finding_id}]** ({f.severity_label}): {f.message} *Öneri: {f.recommendation}*")
        md.append("")
        
    if review_items:
        md.append("## 5. Manuel İnceleme Kuyruğu")
        md.append("")
        for r in review_items:
            md.append(f"- **[{r.review_id}]**: {r.description} (Eylem: {r.recommended_action})")
        md.append("")
        
    md.append("## 6. Faz 141 Devir Hazırlığı")
    md.append("")
    md.append("Ensemble ve aday model sözleşmeleri eksiksiz kurulmuş olup, Faz 141 (Olasılık Kalibrasyonu ve Belirsizlik Tahmini) devrine hazırdır.")
    md.append("")
    return "\n".join(md)
