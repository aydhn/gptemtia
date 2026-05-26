import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd
from documentation.documentation_config import get_default_documentation_profile
from documentation.doc_quality import (
    check_documentation_inventory_quality,
    check_documentation_coverage_quality,
    check_documentation_link_quality,
    check_documentation_safety_quality,
    build_documentation_quality_report
)

def test_check_inventory_quality():
    profile = get_default_documentation_profile()

    q1 = check_documentation_inventory_quality(pd.DataFrame(), profile)
    assert q1["passed"] is False

    df = pd.DataFrame([{"has_disclaimer": True}])
    q2 = check_documentation_inventory_quality(df, profile)
    assert q2["passed"] is True

def test_check_coverage_quality():
    profile = get_default_documentation_profile()
    df = pd.DataFrame([{"status": "covered"}])
    q = check_documentation_coverage_quality(df, profile)
    assert q["passed"] is True

def test_build_documentation_quality_report():
    report = build_documentation_quality_report({})
    assert "passed" in report
    assert "warning_count" in report
