"""Test PDF-ready maps."""
from commodity_fx_signal_bot.local_documentation_export.pdf_ready_maps import build_pdf_ready_print_checklist
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_pdf_ready_maps():
    p = get_default_local_documentation_export_profile()
    df, s = build_pdf_ready_print_checklist(p)
    assert not df.empty
