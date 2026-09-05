"""Test offline HTML pages."""
from commodity_fx_signal_bot.local_documentation_export.offline_html_pages import build_offline_html_index_page
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_html_pages():
    p = get_default_local_documentation_export_profile()
    txt, s = build_offline_html_index_page(p)
    assert len(txt) > 0
