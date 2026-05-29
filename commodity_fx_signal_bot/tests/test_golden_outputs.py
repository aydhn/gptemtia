import pandas as pd
from pathlib import Path
from scenario_regression.golden_outputs import build_golden_outputs_for_scenario

def test_golden_output_generation(tmp_path):
    f = tmp_path / "test.csv"
    f.write_text("a,b\n1,2")

    expected_df = pd.DataFrame([{"scenario_id": "scen1", "output_name": "test", "output_path": str(f)}])

    # We pass the root as / so it uses absolute paths we passed
    df, summary = build_golden_outputs_for_scenario("scen1", expected_df, Path("/"))
    assert not df.empty
    assert "test" in df.iloc[0]["output_name"]
    assert bool(df.iloc[0]["synthetic_only"]) is True
