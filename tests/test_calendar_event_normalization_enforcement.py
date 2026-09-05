import pandas as pd
from advanced_data_normalization.calendar_event_normalization_enforcement import (
    normalize_calendar_event_value,
    normalize_calendar_event_dataframe,
    build_calendar_event_normalization_enforcement_report,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalize_calendar_event_value():
    assert normalize_calendar_event_value("FOMC") == "FOMC_RATE_DECISION"
    assert normalize_calendar_event_value("US CPI") == "US_CPI_RELEASE"
    assert normalize_calendar_event_value("NFP") == "US_NONFARM_PAYROLLS_RELEASE"
    assert normalize_calendar_event_value("CBRT") == "CBRT_RATE_DECISION"


def test_normalize_calendar_event_dataframe():
    raw_df = pd.DataFrame([{"canonical_event": "FOMC"}, {"canonical_event": "NFP"}])
    norm_df, findings = normalize_calendar_event_dataframe(raw_df, field="canonical_event")

    assert "normalized_event" in norm_df.columns
    assert norm_df["normalized_event"].iloc[0] == "FOMC_RATE_DECISION"
    assert norm_df["normalized_event"].iloc[1] == "US_NONFARM_PAYROLLS_RELEASE"


def test_calendar_event_report():
    prof = get_default_data_normalization_profile()
    df, summary = build_calendar_event_normalization_enforcement_report(prof)
    assert not df.empty
    assert summary["total_mappings"] >= 5
