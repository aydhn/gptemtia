import pandas as pd

from governance.source_attribution import (
    build_data_source_attribution_table,
    infer_data_source_from_artifact,
)


def test_infer_source():
    assert infer_data_source_from_artifact("raw/yahoo/data.csv") == "yahoo_finance_library"
    assert infer_data_source_from_artifact("reports/r.txt") == "report_generated"

def test_build_table():
    inv_df = pd.DataFrame([{"artifact_id": "a1", "artifact_type": "raw", "relative_path": "raw/yahoo/data.csv"}])
    df = build_data_source_attribution_table(inv_df)
    assert not df.empty
    assert df.iloc[0]["source"] == "yahoo_finance_library"
