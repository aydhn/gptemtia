
import pytest
from commodity_fx_signal_bot.local_hardening.hardening_report_builder import build_hardening_domain_registry_markdown_report, build_dead_code_review_markdown_report, build_hardening_disclaimer

def test_hardening_report_builder():
    disc = build_hardening_disclaimer()
    assert "Production release" in disc
    assert "yatirim tavsiyesi degildir" in disc
    rep = build_hardening_domain_registry_markdown_report({})
    assert "Domains" in rep
