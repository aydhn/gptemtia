import pytest
import pandas as pd
from unittest.mock import MagicMock
from decisions.decision_inputs import DecisionInputLoader


def test_load_signal_candidates():
    dl_mock = MagicMock()
    dl_mock.has_features.return_value = True
    dl_mock.load_features.return_value = pd.DataFrame({"a": [1]})

    loader = DecisionInputLoader(dl_mock)
    spec_mock = MagicMock()
    df, summary = loader.load_signal_candidates(spec_mock, "1d")

    assert not df.empty
    assert summary["loaded"] is True


def test_load_decision_context():
    dl_mock = MagicMock()
    dl_mock.has_features.return_value = False
    dl_mock.load_feature_set.side_effect = Exception("Not found")

    loader = DecisionInputLoader(dl_mock)
    spec_mock = MagicMock()
    ctx, summary = loader.load_decision_context(spec_mock, "1d")

    assert len(summary["missing_frames"]) > 0
