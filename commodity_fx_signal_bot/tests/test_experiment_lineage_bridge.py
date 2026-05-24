import pandas as pd

from governance.experiment_lineage_bridge import link_experiment_runs_to_artifacts


def test_link_experiment():
    exp_df = pd.DataFrame([{"run_id": "run1", "experiment_id": "exp1"}])
    inv_df = pd.DataFrame([{"artifact_id": "a1", "artifact_type": "type", "relative_path": "path/run1/data.csv"}])

    links = link_experiment_runs_to_artifacts(exp_df, inv_df)
    assert not links.empty
    assert links.iloc[0]["run_id"] == "run1"
    assert links.iloc[0]["artifact_id"] == "a1"
