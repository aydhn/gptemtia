import pandas as pd

from strategies.strategy_config import get_default_strategy_selection_profile
from strategies.strategy_mapper import CandidateToStrategyMapper


def test_map_decision_to_families():
    profile = get_default_strategy_selection_profile()
    mapper = CandidateToStrategyMapper(profile)

    row = pd.Series(
        {"decision_label": "long_bias_candidate", "candidate_type": "trend_following"}
    )
    families, summary = mapper.map_decision_to_families(row)

    assert "trend_following" in families


def test_map_no_trade_decision():
    profile = get_default_strategy_selection_profile()
    mapper = CandidateToStrategyMapper(profile)

    row = pd.Series({"decision_label": "no_trade_candidate"})
    families, summary = mapper.map_decision_to_families(row)

    assert families == ["no_trade"]


def test_build_family_fit_table():
    profile = get_default_strategy_selection_profile()
    mapper = CandidateToStrategyMapper(profile)

    row = pd.Series(
        {"decision_label": "long_bias_candidate", "candidate_type": "trend_following"}
    )
    context = {}

    df, summary = mapper.build_family_fit_table(row, context)
    assert not df.empty
    assert "family" in df.columns
