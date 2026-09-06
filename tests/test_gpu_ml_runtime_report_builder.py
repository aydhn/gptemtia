"""Test suite for Phase 136 GPU ML Runtime Report Builder."""

import pytest
from advanced_gpu_ml_runtime.gpu_ml_runtime_report_builder import (
    build_gpu_ml_runtime_disclaimer,
    build_gpu_ml_runtime_profile_markdown_report,
    build_local_hardware_discovery_markdown_report,
    build_gpu_capability_markdown_report,
    build_ml_runtime_safety_contract_markdown_report,
    build_gpu_ml_runtime_manifest_markdown_report,
    build_phase_137_handoff_markdown_report,
    _df_to_markdown,
)
import pandas as pd


def test_disclaimer_content():
    disc = build_gpu_ml_runtime_disclaimer()
    assert "Phase 136" in disc
    assert "GPU Acceleration and Advanced ML Runtime Foundation" in disc
    assert "kesin AL/SAT" in disc
    assert "yatırım tavsiyesi" in disc


def test_markdown_report_generation():
    summary = {"active_profile": "balanced_local_gpu_ml_runtime_foundation", "current_phase": 136, "target_final_phase": 160}
    md = build_gpu_ml_runtime_profile_markdown_report(summary)
    assert "# Phase 136: GPU ML Runtime Profile Registry Report" in md
    assert "Phase 136" in md


def test_df_to_markdown_fallback():
    df = pd.DataFrame([{"col1": "val1", "col2": "val2"}])
    res = _df_to_markdown(df)
    assert "col1" in res
    assert "val1" in res

    empty_res = _df_to_markdown(None)
    assert empty_res == "_Boş tablo_"
