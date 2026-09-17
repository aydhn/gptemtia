# -*- coding: utf-8 -*-
"""Unit tests for baseline model source preservation guards."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_model_source_preservation_guards import (
    SOURCE_PRESERVATION_GUARDS,
    build_baseline_model_source_preservation_guard_registry,
    summarize_baseline_model_source_preservation_guards,
    validate_baseline_model_source_preservation_action,
)


def test_build_baseline_model_source_preservation_guard_registry():
    df, summary = build_baseline_model_source_preservation_guard_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(SOURCE_PRESERVATION_GUARDS)
    assert len(df) == 4
    assert summary["total_guards"] == 4
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
    assert (df["enforced"] == True).all()


def test_validate_baseline_model_source_preservation_action():
    assert validate_baseline_model_source_preservation_action("read_catalog_metadata")["valid"] is True
    assert validate_baseline_model_source_preservation_action("load_snapshot")["valid"] is True

    assert validate_baseline_model_source_preservation_action("overwrite_raw_file")["valid"] is False
    assert validate_baseline_model_source_preservation_action("delete_dataset_partition")["valid"] is False
    assert validate_baseline_model_source_preservation_action("auto_impute_missing_values")["valid"] is False
