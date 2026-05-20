import pandas as pd
from devtools.dx_quality import check_dx_findings_dataframe, check_cli_catalog_quality, check_cli_help_quality, check_import_smoke_quality, check_for_forbidden_live_terms_in_dx, build_dx_quality_report

def test_dx_quality_functions():
    df = pd.DataFrame([{"finding_id": "1", "status": "dx_failed"}])
    assert check_dx_findings_dataframe(df)["valid"] is True
    assert check_cli_catalog_quality(df)["valid"] is True
    assert check_cli_help_quality(df)["valid"] is True
    assert check_import_smoke_quality(df)["valid"] is True
    assert check_for_forbidden_live_terms_in_dx()["found"] is False
    rep = build_dx_quality_report(df, {})
    assert rep["failed_count"] == 1
