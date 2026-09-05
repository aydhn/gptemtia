"""Unit tests for Phase 119 cross-asset alignment labels and validators."""

import pytest
from advanced_cross_asset_alignment.cross_asset_alignment_labels import (
    ALIGNMENT_DOMAINS,
    ALIGNMENT_FAMILIES,
    JOIN_POLICIES,
    ALIGNMENT_STATUS_LABELS,
    validate_alignment_domain,
    validate_alignment_family,
    validate_join_policy,
    validate_alignment_status_label,
)


def test_domain_validation():
    assert validate_alignment_domain("fx") is True
    assert validate_alignment_domain("commodity") is True
    assert validate_alignment_domain("macro") is True
    assert validate_alignment_domain("calendar") is True
    assert validate_alignment_domain("news") is True
    assert validate_alignment_domain("unsupported_domain") is False


def test_family_validation():
    assert validate_alignment_family("price_technical") is True
    assert validate_alignment_family("macro_interest_rate") is True
    assert validate_alignment_family("calendar_scheduled_event") is True
    assert validate_alignment_family("news_metadata_sentiment") is True
    assert validate_alignment_family("arbitrary_family") is False


def test_join_policy_validation():
    assert validate_join_policy("join_policy_asof_backward") is True
    assert validate_join_policy("join_policy_exact_timestamp") is True
    assert validate_join_policy("join_policy_forward_nearest") is False


def test_status_label_validation():
    assert validate_alignment_status_label("alignment_ready") is True
    assert validate_alignment_status_label("alignment_pending") is True
    assert validate_alignment_status_label("invalid_status") is False
