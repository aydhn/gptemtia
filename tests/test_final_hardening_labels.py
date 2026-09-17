# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Hardening Labels."""

from advanced_final_hardening.final_hardening_labels import (
    ALL_FINAL_HARDENING_DOMAINS,
    ALL_FINAL_HARDENING_PROFILES,
    ALL_FINAL_HARDENING_METRICS,
    ALL_FINAL_HARDENING_STATUSES,
    ALL_OPERATOR_RUNBOOK_NAMES,
    ALL_OPERATOR_RUNBOOK_DOMAINS,
    ALL_RELEASE_CANDIDATE_CHECKLIST_NAMES,
    ALL_RELEASE_CANDIDATE_GATES,
    ALL_RELEASE_CANDIDATE_NO_GO_BOUNDARIES,
    ALL_RELEASE_CANDIDATE_GO_BOUNDARIES,
    FINAL_HARDENING_DISCLAIMER,
)


def test_labels_domains_and_profiles():
    assert len(ALL_FINAL_HARDENING_DOMAINS) == 12
    assert len(ALL_FINAL_HARDENING_PROFILES) == 3
    assert len(ALL_FINAL_HARDENING_METRICS) >= 10
    assert len(ALL_FINAL_HARDENING_STATUSES) >= 4


def test_operator_runbook_labels():
    assert len(ALL_OPERATOR_RUNBOOK_NAMES) == 16
    assert len(ALL_OPERATOR_RUNBOOK_DOMAINS) == 8


def test_release_candidate_labels():
    assert len(ALL_RELEASE_CANDIDATE_CHECKLIST_NAMES) == 16
    assert len(ALL_RELEASE_CANDIDATE_GATES) == 8
    assert len(ALL_RELEASE_CANDIDATE_NO_GO_BOUNDARIES) == 16
    assert len(ALL_RELEASE_CANDIDATE_GO_BOUNDARIES) == 16


def test_disclaimer():
    assert "PHASE 159" in FINAL_HARDENING_DISCLAIMER
    assert "YASAL VE GÜVENLİK FERAGATNAMESİ" in FINAL_HARDENING_DISCLAIMER

