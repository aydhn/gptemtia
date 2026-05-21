from report_exports.html_renderer import (
    markdown_to_basic_html,
    build_html_document,
    render_markdown_report_to_html
)
from report_exports.export_config import get_default_report_export_profile

def test_markdown_to_basic_html():
    res = markdown_to_basic_html("**bold**")
    assert "<strong>bold</strong>" in res or "<b>bold</b>" in res or "<strong>" in res.lower()

def test_render_markdown_report_to_html():
    profile = get_default_report_export_profile()
    html, summary = render_markdown_report_to_html("# Test", "Title", profile)
    assert "Title" in html
    assert "Test" in html
    assert "offline araştırma raporu" in html
    assert "script" not in html.lower()
