import pandas as pd
from pathlib import Path
from quality_gates.quality_pipeline import QualityGatePipeline

class MockDataLake:
    pass

class MockSettings:
    pass

def test_quality_pipeline():
    lake = MockDataLake()
    settings = MockSettings()
    pipeline = QualityGatePipeline(lake, settings, Path("."))

    df, summary = pipeline.build_local_ci_validation_report(save=False)
    assert isinstance(df, pd.DataFrame)

    df, summary = pipeline.build_test_health_report(save=False)
    assert isinstance(df, pd.DataFrame)

    tables, summary = pipeline.build_import_graph_report(save=False)
    assert isinstance(tables, dict)

    df, summary = pipeline.build_repo_hygiene_report(save=False)
    assert isinstance(df, pd.DataFrame)

    tables, summary = pipeline.build_dependency_audit_report(save=False)
    assert isinstance(tables, dict)

    df, summary = pipeline.build_static_safety_scan_report(save=False)
    assert isinstance(df, pd.DataFrame)

    df, summary = pipeline.build_smoke_test_report(save=False)
    assert isinstance(df, pd.DataFrame)

    report, summary = pipeline.build_release_candidate_report(save=False)
    assert isinstance(report, dict)
