from devtools.dx_pipeline import DeveloperExperiencePipeline

def test_dx_pipeline_runs(tmp_path):
    pipeline = DeveloperExperiencePipeline(tmp_path)
    df, sum1 = pipeline.run_cli_catalog(save=False)
    assert isinstance(sum1, dict)
    df, sum2 = pipeline.run_cli_help_audit(save=False)
    assert isinstance(sum2, dict)
    df, sum3 = pipeline.run_import_smoke_test(save=False)
    assert isinstance(sum3, dict)
    df, sum4 = pipeline.run_test_matrix_report(save=False)
    assert isinstance(sum4, dict)
    df, sum5 = pipeline.run_full_dx_check(save=False)
    assert isinstance(sum5, dict)
