import pandas as pd
from scenario_regression.fixture_reproducibility import compare_fixture_reproducibility, validate_fixture_seed_consistency
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_fixture_reproducibility():
    prof = get_default_scenario_regression_profile()
    f_df = pd.DataFrame([{"scenario_id": "s1", "synthetic": True, "random_seed": 42}])
    df, summ = compare_fixture_reproducibility(f_df, pd.DataFrame(), prof)
    assert not df.empty

    seed_res = validate_fixture_seed_consistency(f_df, 42)
    assert seed_res["consistent"] is True
