import pytest
import pandas as pd
from local_maintenance.maintenance_report_builder import (
    build_maintenance_domain_registry_markdown_report,
    build_maintenance_disclaimer
)

def test_maintenance_report_builder():
    df = pd.DataFrame([{"a": 1}])
    md = build_maintenance_domain_registry_markdown_report({}, df)

    assert "Maintenance Domain Registry" in md
    assert "yatırım tavsiyesi değildir" in md
    assert "a" in md
