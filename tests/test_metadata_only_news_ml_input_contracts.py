"""Test suite for Phase 136 Metadata-Only News ML Input Contracts."""

import pytest
from advanced_gpu_ml_runtime.metadata_only_news_ml_input_contracts import (
    build_metadata_only_news_ml_input_contract_registry,
)


def test_build_metadata_only_news_ml_input_contracts():
    df, summary = build_metadata_only_news_ml_input_contract_registry()
    assert not df.empty
    assert summary["metadata_only_guaranteed"] is True
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
