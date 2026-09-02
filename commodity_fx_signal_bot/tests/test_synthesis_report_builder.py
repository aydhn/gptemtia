import pytest
from local_synthesis.synthesis_report_builder import build_synthesis_profile_markdown_report

def test_build_synthesis_profile_markdown_report():
    report = build_synthesis_profile_markdown_report({})
    assert "yatırım tavsiyesi" in report
