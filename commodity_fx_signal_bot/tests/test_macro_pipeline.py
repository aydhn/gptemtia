from unittest.mock import MagicMock

import pandas as pd

from macro.macro_config import get_default_macro_profile
from macro.macro_pipeline import MacroPipeline


def test_macro_pipeline_mocked():
    lake_mock = MagicMock()
    settings_mock = MagicMock()
    settings_mock.evds_api_key = "fake"
    settings_mock.fred_api_key = "fake"
    settings_mock.save_macro_features = False
    settings_mock.save_macro_events = False

    p = get_default_macro_profile()
    pipeline = MacroPipeline(data_lake=lake_mock, settings=settings_mock, profile=p)

    # mock fetch
    pipeline.provider.fetch_many = MagicMock(
        return_value={
            "TR_CPI": pd.DataFrame(
                {"value": [100]}, index=[pd.to_datetime("2020-01-01")]
            )
        }
    )

    res, summ = pipeline.update_macro_data(save=False)
    assert "TR_CPI" in res
    assert "fetched_series" in summ

    lake_mock.load_macro_series.return_value = pd.DataFrame(
        {"value": [100]}, index=[pd.to_datetime("2020-01-01")]
    )

    f_res, f_summ = pipeline.build_macro_features(save=False)
    assert not f_res.empty

    b_res, b_summ = pipeline.build_benchmarks(save=False)
    assert not b_res.empty
