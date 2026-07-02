import pytest
import pandas as pd
from local_archive.archive_report_builder import (
    build_archive_domain_registry_markdown_report,
    build_archive_disclaimer
)

def test_archive_disclaimer():
    disc = build_archive_disclaimer()
    assert "Cloud backup" in disc
    assert "yatırım tavsiyesi değildir" in disc

def test_markdown_report():
    df = pd.DataFrame([{"A": 1}])
    rep = build_archive_domain_registry_markdown_report({"total_domains": 1}, df)

    assert "Archive Domain Registry Report" in rep
    assert "yatırım tavsiyesi değildir" in rep
    assert "A" in rep
    assert "1" in rep
