import pytest
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_report_builder import (
    build_benchmark_evaluation_disclaimer,
    build_summary_placeholder_markdown_report,
    build_metric_placeholder_markdown_report,
    build_evaluation_guard_markdown_report,
    build_evaluation_disabled_execution_markdown_report,
    build_benchmark_evaluation_findings_markdown_report,
    build_benchmark_evaluation_readiness_score_markdown_report,
    build_benchmark_evaluation_manifest_markdown_report,
    build_benchmark_evaluation_validation_markdown_report,
    build_benchmark_evaluation_safety_markdown_report,
    build_phase_152_handoff_markdown_report,
    build_benchmark_evaluation_health_markdown_report
)

def test_build_benchmark_evaluation_disclaimer():
    disclaimer = build_benchmark_evaluation_disclaimer()
    assert "> [!WARNING]" in disclaimer
    assert "> **YASAL UYARI VE GÜVENLİK SINIRI:**" in disclaimer
    assert "Bu çıktı Phase 151 Benchmark Comparison and Strategy Evaluation Reports raporudur." in disclaimer
    assert "Canlı emir, broker talimatı, kesin AL/SAT" in disclaimer

def test_build_summary_placeholder_markdown_report():
    summary = {"total_placeholders": 5, "all_uncalculated": True, "status": "OK"}
    df = pd.DataFrame([{"col1": "A", "col2": "B"}])
    report = build_summary_placeholder_markdown_report(summary, df)

    assert "# Phase 151: Summary Placeholders Report" in report
    assert "## Summary" in report
    assert "- **Total Placeholders:** 5" in report
    assert "- **All Uncalculated:** True" in report
    assert "- **Status:** OK" in report
    assert "## Summary Placeholders Registry" in report
    assert "| col1" in report
    assert "| col2" in report

def test_build_summary_placeholder_markdown_report_empty_df():
    summary = {"total_placeholders": 0}
    report = build_summary_placeholder_markdown_report(summary)

    assert "# Phase 151: Summary Placeholders Report" in report
    assert "## Summary" in report
    assert "## Summary Placeholders Registry" not in report

def test_build_metric_placeholder_markdown_report():
    summary = {"total_metrics": 10, "all_uncalculated": True, "all_claims_blocked": True, "status": "READY"}
    report = build_metric_placeholder_markdown_report(summary)

    assert "# Phase 151: Uncalculated Metric Placeholders Report" in report
    assert "- **Total Metrics:** 10" in report
    assert "- **Claims Blocked:** True" in report

def test_build_evaluation_guard_markdown_report():
    summary = {"total_guards": 3, "all_active": True, "status": "ACTIVE"}
    report = build_evaluation_guard_markdown_report(summary)

    assert "# Phase 151: Evaluation Guards and Boundary Report" in report
    assert "- **Total Guards:** 3" in report
    assert "- **All Active:** True" in report

def test_build_evaluation_disabled_execution_markdown_report():
    summary = {"operation": "trade", "is_disabled": True, "status": "SECURE"}
    report = build_evaluation_disabled_execution_markdown_report(summary)

    assert "# Phase 151: Disabled Execution Enforcements Report" in report
    assert "- **Operation:** trade" in report
    assert "- **Is Disabled:** True" in report

def test_build_benchmark_evaluation_findings_markdown_report():
    summary = {"total_findings": 2, "critical_count": 0, "blocker_count": 0, "status": "CLEAN"}
    report = build_benchmark_evaluation_findings_markdown_report(summary)

    assert "# Phase 151: Diagnostic Findings and Review Gates Report" in report
    assert "- **Total Findings:** 2" in report
    assert "- **Critical Count:** 0" in report
    assert "- **Blocker Count:** 0" in report

def test_build_benchmark_evaluation_readiness_score_markdown_report():
    summary = {"score": 0.85, "classification": "HIGH", "meets_threshold": True, "status": "READY"}
    report = build_benchmark_evaluation_readiness_score_markdown_report(summary)

    assert "# Phase 151: Benchmark Evaluation Readiness Score Report" in report
    assert "- **Readiness Score:** 0.85" in report
    assert "- **Classification:** HIGH" in report
    assert "- **Meets Minimum Threshold:** True" in report

def test_build_benchmark_evaluation_manifest_markdown_report():
    summary = {"manifest_id": "MAN-001", "current_phase": 151, "next_phase": 152, "all_negative_invariants_satisfied": True, "phase_152_handoff_ready": True, "status": "READY"}
    report = build_benchmark_evaluation_manifest_markdown_report(summary)

    assert "# Phase 151: Master Benchmark Evaluation Manifest Report" in report
    assert "- **Manifest ID:** MAN-001" in report
    assert "- **Current Phase:** 151" in report
    assert "- **Next Phase:** 152" in report

def test_build_benchmark_evaluation_validation_markdown_report():
    summary = {"validation_status": "PASS", "total_checks": 10, "all_passed": True}
    report = build_benchmark_evaluation_validation_markdown_report(summary)

    assert "# Phase 151: Validation Report" in report
    assert "- **Validation Status:** PASS" in report
    assert "- **Total Checks:** 10" in report
    assert "- **All Passed:** True" in report
    assert "- **Forbidden Claims Clean:** True" in report

def test_build_benchmark_evaluation_safety_markdown_report():
    summary = {"safety_status": "SECURE", "no_go_count": 5, "safe_go_count": 3}
    report = build_benchmark_evaluation_safety_markdown_report(summary)

    assert "# Phase 151: Safety Boundary Report" in report
    assert "- **Safety Status:** SECURE" in report
    assert "- **NO-GO Rules Enforced:** 5" in report
    assert "- **SAFE-GO Principles Active:** 3" in report
    assert "- **Live Trading Prohibited:** True" in report

def test_build_phase_152_handoff_markdown_report():
    summary = {"handoff_status": "READY", "source_phase": 151, "next_phase": 152, "next_phase_name": "Phase 152", "total_prerequisites": 5, "all_prerequisites_satisfied": True}
    report = build_phase_152_handoff_markdown_report(summary)

    assert "# Phase 151 to Phase 152 Handoff Report" in report
    assert "- **Handoff Status:** READY" in report
    assert "- **Source Phase:** 151" in report
    assert "- **Next Phase:** 152" in report

def test_build_benchmark_evaluation_health_markdown_report():
    summary = {"status": "HEALTHY", "total_checks": 10, "passed_checks": 10, "failed_checks": 0, "all_passed": True}
    report = build_benchmark_evaluation_health_markdown_report(summary)

    assert "# Phase 151: Benchmark Evaluation Health Check Report" in report
    assert "- **Health Status:** HEALTHY" in report
    assert "- **Total Checks:** 10" in report
    assert "- **Passed Checks:** 10" in report
    assert "- **Failed Checks:** 0" in report
