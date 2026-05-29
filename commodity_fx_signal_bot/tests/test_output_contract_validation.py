import pandas as pd
from pathlib import Path
from scenario_regression.output_contract_validation import validate_scenario_output_contracts
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_output_contract_validation(tmp_path):
    f = tmp_path / "test.csv"
    f.write_text("a,b\n1,2")
    prof = get_default_scenario_regression_profile()

    e_df = pd.DataFrame([{"scenario_id": "s1", "output_name": "n1", "output_path": str(f)}])
    df, summ = validate_scenario_output_contracts(e_df, Path("/"), prof)
    assert not df.empty
