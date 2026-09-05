import pandas as pd
from advanced_feature_grid.feature_grid_computation_interfaces import (
    BaseFeatureGridComputer,
    build_feature_grid_computation_interface_contract,
)
from advanced_feature_grid.feature_grid_models import FeatureGridComputationResult


class DummyComputer(BaseFeatureGridComputer):
    def compute_grid(self, df, grid_name, parameter_grid=None):
        out = df.copy()
        out["dummy_feat"] = 1.0
        res = FeatureGridComputationResult(
            result_id="dummy_res",
            grid_name=grid_name,
            indicator_family="dummy",
            dataset_type="ohlcv",
            provider_name="dummy",
            output_fields=["dummy_feat"],
            row_count=len(df),
            output_feature_count=1,
            non_signal=True,
        )
        return out, res


def test_feature_grid_computation_interfaces():
    df, summary = build_feature_grid_computation_interface_contract()
    assert not df.empty
    assert summary["in_place_mutation_prevented"] is True
    assert summary["non_signal"] is True

    computer = DummyComputer()
    df_test = pd.DataFrame({"close": [10.0, 20.0]})
    val = computer.validate_input(df_test, ["close"])
    assert val["valid"] is True

    out, res = computer.compute_grid(df_test, "dummy_grid")
    assert "dummy_feat" in out.columns
    assert "dummy_feat" not in df_test.columns  # No mutation
    assert res.non_signal is True
