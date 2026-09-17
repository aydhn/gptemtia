# -*- coding: utf-8 -*-
"""Unit tests for Phase 137 Dataset Contract Acceptance."""

import pytest
from advanced_ml_acceptance.phase_137_dataset_contract_acceptance import (
    build_phase_137_dataset_contract_acceptance_registry,
    summarize_phase_137_dataset_contract_acceptance,
)


def test_phase_137_acceptance():
    df, summary = build_phase_137_dataset_contract_acceptance_registry()
    assert not df.empty
    assert len(df) >= 7
    assert summary["phase_ref"] == "Phase 137"
    assert summary["all_passed"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "ACCEPTED"

    s = summarize_phase_137_dataset_contract_acceptance(df)
    assert s["check_count"] >= 7
    assert s["all_passed"] is True
