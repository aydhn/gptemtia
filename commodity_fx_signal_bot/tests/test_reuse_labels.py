"""
Test: test_reuse_labels.py
"""

import pytest
from commodity_fx_signal_bot.local_reuse.reuse_labels import (
    list_reuse_domain_labels,
    list_reuse_risk_labels,
    list_reuse_status_labels,
    list_template_labels,
    list_v1_1_seed_status_labels,
    validate_reuse_domain_label,
    validate_reuse_risk,
    validate_reuse_status,
    validate_template_label,
    validate_v1_1_seed_status,
)


def test_validate_reuse_domain_label():
    for label in list_reuse_domain_labels():
        validate_reuse_domain_label(label)  # Should not raise
    with pytest.raises(ValueError):
        validate_reuse_domain_label("invalid_label")


def test_validate_template_label():
    for label in list_template_labels():
        validate_template_label(label)
    with pytest.raises(ValueError):
        validate_template_label("invalid_label")


def test_validate_reuse_status():
    for label in list_reuse_status_labels():
        validate_reuse_status(label)
    with pytest.raises(ValueError):
        validate_reuse_status("invalid_label")


def test_validate_v1_1_seed_status():
    for label in list_v1_1_seed_status_labels():
        validate_v1_1_seed_status(label)
    with pytest.raises(ValueError):
        validate_v1_1_seed_status("invalid_label")


def test_validate_reuse_risk():
    for label in list_reuse_risk_labels():
        validate_reuse_risk(label)
    with pytest.raises(ValueError):
        validate_reuse_risk("invalid_label")
