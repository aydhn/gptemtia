"""Test printable binder."""
from pathlib import Path
from commodity_fx_signal_bot.local_documentation_export.printable_binder import build_printable_binder_packet
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_printable_binder():
    p = get_default_local_documentation_export_profile()
    txt, s = build_printable_binder_packet(Path("."), p)
    assert len(txt) > 0
