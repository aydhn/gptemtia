import pytest
from commodity_fx_signal_bot.ml.uncertainty import (
    calculate_probability_entropy,
    calculate_margin_confidence,
    calculate_ensemble_disagreement
)

def test_calculate_probability_entropy():
    assert calculate_probability_entropy({"up": 1.0, "down": 0.0}) == 0.0
    assert calculate_probability_entropy({"up": 0.5, "down": 0.5}) == 1.0

def test_calculate_margin_confidence():
    assert calculate_margin_confidence({"up": 0.8, "down": 0.2}) == 0.6
    assert calculate_margin_confidence({"up": 0.5, "down": 0.5}) == 0.0

def test_calculate_ensemble_disagreement():
    assert calculate_ensemble_disagreement([{"predicted_direction": "predicted_up"}]) == 0.0
    assert calculate_ensemble_disagreement([{"predicted_direction": "predicted_up"}, {"predicted_direction": "predicted_up"}]) == 0.0

    dis = calculate_ensemble_disagreement([
        {"predicted_direction": "predicted_up"},
        {"predicted_direction": "predicted_up"},
        {"predicted_direction": "predicted_down"}
    ])
    assert dis > 0.5
