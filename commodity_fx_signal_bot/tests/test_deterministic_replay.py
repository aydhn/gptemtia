import pandas as pd
from pathlib import Path
from scenario_regression.deterministic_replay import DeterministicReplayRunner
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_replay_runner():
    prof = get_default_scenario_regression_profile()
    runner = DeterministicReplayRunner(Path("/"), prof)
    res = runner.replay_scenario("scen1", pd.DataFrame(), pd.DataFrame())
    assert res.replay_status == "replay_skipped"
