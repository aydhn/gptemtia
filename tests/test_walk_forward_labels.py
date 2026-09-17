# -*- coding: utf-8 -*-
"""Unit tests for Phase 147: Walk-Forward Validation Labels."""

from advanced_walk_forward_validation.walk_forward_labels import (
    WALK_FORWARD_DOMAIN,
    WALK_FORWARD_PROFILE_DOMAIN,
    SPLIT_CONTRACT_DOMAIN,
    BENCHMARK_CONTRACT_DOMAIN,
    VALIDATION_CONTRACT_READY,
    EXECUTION_BLOCKED_NO_WALK_FORWARD,
    EXECUTION_BLOCKED_NO_BENCHMARK,
    DOMAIN_LABELS,
    STATUS_LABELS,
    EXECUTION_LABELS,
)


def test_walk_forward_labels():
    assert WALK_FORWARD_DOMAIN == "walk_forward_domain"
    assert WALK_FORWARD_PROFILE_DOMAIN == "walk_forward_profile_domain"
    assert SPLIT_CONTRACT_DOMAIN == "split_contract_domain"
    assert BENCHMARK_CONTRACT_DOMAIN == "benchmark_contract_domain"

    assert VALIDATION_CONTRACT_READY == "validation_contract_ready"
    assert EXECUTION_BLOCKED_NO_WALK_FORWARD == "execution_blocked_no_walk_forward"
    assert EXECUTION_BLOCKED_NO_BENCHMARK == "execution_blocked_no_benchmark"

    assert len(DOMAIN_LABELS) >= 30
    assert len(STATUS_LABELS) >= 5
    assert len(EXECUTION_LABELS) >= 8
