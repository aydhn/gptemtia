# -*- coding: utf-8 -*-
"""Unit tests for Phase 147: Evidence, Review Queue, Findings, Scoring, and Manifest."""

from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.validation_evidence import (
    build_validation_evidence_registry,
)
from advanced_walk_forward_validation.walk_forward_manual_review import (
    build_walk_forward_manual_review_queue,
)
from advanced_walk_forward_validation.walk_forward_findings import (
    build_walk_forward_findings_registry,
)
from advanced_walk_forward_validation.walk_forward_readiness_scoring import (
    build_walk_forward_readiness_score_report,
    calculate_walk_forward_readiness_score,
)
from advanced_walk_forward_validation.walk_forward_manifest import (
    build_walk_forward_manifest,
)


def test_evidence_review_findings_scoring_manifest():
    prof = get_default_walk_forward_profile()

    df_ev, s_ev = build_validation_evidence_registry(prof)
    assert not df_ev.empty
    assert s_ev["all_verified"] is True

    df_rev, s_rev = build_walk_forward_manual_review_queue(prof)
    assert not df_rev.empty
    assert s_rev["zero_destructive_actions"] is True

    df_fnd, s_fnd = build_walk_forward_findings_registry(prof)
    assert not df_fnd.empty
    assert s_fnd["has_critical_blockers"] is False

    df_scr, s_scr = build_walk_forward_readiness_score_report(prof)
    assert not df_scr.empty
    assert s_scr["score"] >= 0.80
    assert s_scr["meets_threshold"] is True
    assert s_scr["classification"] == "walk_forward_oos_contract_ready_non_production"

    score_obj = calculate_walk_forward_readiness_score(df_fnd, prof)
    assert score_obj.score >= 0.80
    assert score_obj.classification == "walk_forward_oos_contract_ready_non_production"

    df_man, s_man = build_walk_forward_manifest(prof)
    assert not df_man.empty
    assert s_man["current_phase"] == 147
    assert s_man["next_phase"] == 148
    assert s_man["target_final_phase"] == 160
    assert s_man["walk_forward_executed"] is False
    assert s_man["oos_benchmark_executed"] is False
    assert s_man["live_trading_ready"] is False
    assert s_man["phase_148_handoff_ready"] is True
