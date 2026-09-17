# -*- coding: utf-8 -*-
"""Unit tests for Phase 160 Markdown Report Builder."""

import pandas as pd
from advanced_final_delivery.final_delivery_report_builder import (
    build_final_delivery_disclaimer,
    build_final_delivery_full_markdown_report,
    build_final_160_phase_completion_markdown_report,
    build_final_system_summary_markdown_report,
    build_final_operator_handover_markdown_report,
)


def test_final_delivery_disclaimer():
    disc = build_final_delivery_disclaimer()
    assert "YATIRIM TAVSIYESI DEGILDIR" in disc
    assert "OFFLINE RESEARCH ONLY" in disc
    assert "NO LIVE TRADING" in disc


def test_final_delivery_reports():
    df = pd.DataFrame([{"key": "test_metric", "val": 100}])
    summary = {"phase": 160, "status": "COMPLETED"}

    rep = build_final_160_phase_completion_markdown_report(summary, df)
    assert "Phase 160" in rep
    assert "160 Fazlık Plan" in rep

    sys_rep = build_final_system_summary_markdown_report(summary, df)
    assert "Final System Summary" in sys_rep

    op_rep = build_final_operator_handover_markdown_report(summary, df)
    assert "Final Operator Handover" in op_rep
