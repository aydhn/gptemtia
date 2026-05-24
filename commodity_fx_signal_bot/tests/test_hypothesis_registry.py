import pytest
from pathlib import Path
from experiments.hypothesis_registry import HypothesisRegistry, build_default_hypotheses
from experiments.experiment_models import ResearchHypothesis

def test_build_default_hypotheses():
    hyps = build_default_hypotheses()
    assert len(hyps) > 0
    assert isinstance(hyps[0], ResearchHypothesis)

def test_hypothesis_registry(tmp_path):
    registry = HypothesisRegistry(tmp_path)
    hyps = build_default_hypotheses()

    for h in hyps:
        registry.add_hypothesis(h)

    df = registry.load_hypotheses()
    assert len(df) == len(hyps)

    h_id = hyps[0].hypothesis_id
    h_dict = registry.get_hypothesis(h_id)
    assert h_dict is not None
    assert h_dict["title"] == hyps[0].title

    updated = registry.update_hypothesis_status(h_id, "hypothesis_supported", "Looks good")
    assert updated["hypothesis_status"] == "hypothesis_supported"

    summary = registry.summarize()
    assert summary["total_hypotheses"] == len(hyps)
    assert "hypothesis_supported" in summary["by_status"]
