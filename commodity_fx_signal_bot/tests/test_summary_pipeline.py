import pytest
from pathlib import Path
from config.settings import settings
from report_summarization.summary_pipeline import ReportSummarizationPipeline
from report_summarization.summary_config import get_default_report_summary_profile
from data.storage.data_lake import DataLake

class MockDataLake(DataLake):
    pass

def test_summary_pipeline():
    profile = get_default_report_summary_profile()
    dl = MockDataLake(root_dir=Path('/tmp'))
    pipeline = ReportSummarizationPipeline(dl, settings, Path("/tmp"), profile)

    tables, summary = pipeline.build_report_summary_registry(save=False)
    assert isinstance(tables, dict)

    text, meta = pipeline.build_executive_summary_report(save=False)
    assert isinstance(text, str)
