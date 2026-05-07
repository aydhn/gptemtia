import pytest
from levels.level_candidate import build_level_id, build_level_candidate_from_evaluation
import pandas as pd


def test_build_level_id():
    lid = build_level_id("GC=F", "1d", "2023-01-01", "SIZ_123")
    assert lid.startswith("LVL_")


def test_build_from_eval():
    row = pd.Series({"directional_bias": "long_bias_candidate"})
    eval_d = {"latest_close": 100.0, "level_label": "level_approved_candidate"}
    cand = build_level_candidate_from_evaluation(row, eval_d, "GC=F", "1d")
    assert cand.symbol == "GC=F"
    assert cand.level_label == "level_approved_candidate"
