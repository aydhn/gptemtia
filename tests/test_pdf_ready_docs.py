"""Test PDF-ready docs."""
from pathlib import Path
from commodity_fx_signal_bot.local_documentation_export.pdf_ready_docs import build_pdf_ready_documentation_packet
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_pdf_ready_docs():
    p = get_default_local_documentation_export_profile()
    txt, s = build_pdf_ready_documentation_packet(Path("."), p)
    assert len(txt) > 0
