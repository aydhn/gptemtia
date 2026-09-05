"""Test presentation freeze."""
from pathlib import Path
from commodity_fx_signal_bot.local_documentation_export.presentation_freeze import build_archival_presentation_freeze_packet
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_presentation_freeze():
    p = get_default_local_documentation_export_profile()
    txt, s = build_archival_presentation_freeze_packet(Path("."), p)
    assert len(txt) > 0
