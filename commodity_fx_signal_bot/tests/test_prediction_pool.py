import pytest
import math
from ml.prediction_candidate import MLPredictionCandidate
from ml.prediction_pool import MLPredictionCandidatePool

def test_prediction_pool():
    pool = MLPredictionCandidatePool()

    cand1 = MLPredictionCandidate("BTC", "1d", "2020", "id1", "m1", "rf", "cls", "t", "ready", "up", "sup", None, None, 0.8, 0.8, 0.8, 0.1, 0.8, 0.8, 0.1, True, True, [])
    cand2 = MLPredictionCandidate("ETH", "1d", "2020", "id2", "m2", "rf", "cls", "t", "ready", "down", "sup", None, None, 0.9, 0.9, 0.9, 0.05, 0.8, 0.8, 0.1, True, True, [])

    pool.add(cand1)
    pool.add(cand2)

    df = pool.to_dataframe()
    assert len(df) == 2

    ranked = pool.rank()
    assert ranked[0].symbol == "ETH" # higher confidence

    summ = pool.summarize()
    assert summ["total_prediction_candidates"] == 2
    assert math.isclose(summ["average_confidence_score"], 0.85, rel_tol=1e-9)
