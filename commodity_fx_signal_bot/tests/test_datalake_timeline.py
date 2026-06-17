import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
from local_timeline.datalake_timeline import classify_datalake_domain, build_datalake_domain_activity_summary

def test_classify_datalake_domain():
    assert classify_datalake_domain(Path("data/lake/test_domain/a.parquet"), Path(".")) == "test_domain"
    assert classify_datalake_domain(Path("other/a.parquet"), Path(".")) == "unknown_domain"

def test_build_datalake_domain_activity_summary():
    df = pd.DataFrame([{"relative_path": "data/lake/domainA/1.parquet"}, {"relative_path": "data/lake/domainA/2.parquet"}])
    summary_df = build_datalake_domain_activity_summary(df)
    assert not summary_df.empty
    assert summary_df.iloc[0]['domain'] == "domainA"
    assert summary_df.iloc[0]['event_count'] == 2
