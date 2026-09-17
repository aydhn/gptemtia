# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Model Report Builder."""

from advanced_ensemble_model_registry.ensemble_model_manifest import build_ensemble_model_manifest
from advanced_ensemble_model_registry.ensemble_findings import build_ensemble_findings
from advanced_ensemble_model_registry.ensemble_manual_review import build_ensemble_manual_review_queue
from advanced_ensemble_model_registry.ensemble_model_report_builder import (
    build_ensemble_model_text_report,
    build_ensemble_model_markdown_report,
    ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER,
)


def test_ensemble_model_report_builder():
    manifest = build_ensemble_model_manifest()
    findings = build_ensemble_findings()
    review = build_ensemble_manual_review_queue()

    txt = build_ensemble_model_text_report(manifest, findings, review)
    assert "FAZ 140" in txt
    assert "YASAL UYARI" in txt
    assert "Sıfır model eğitimi" in txt

    md = build_ensemble_model_markdown_report(manifest, findings, review)
    assert "# Faz 140" in md
    assert "YASAL UYARI" in md
    assert "Faz 141 Devir Hazırlığı" in md
