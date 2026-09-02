
import pytest
from commodity_fx_signal_bot.local_hardening.hardening_labels import list_hardening_domain_labels, list_dead_code_labels, list_contract_labels, list_freeze_status_labels, list_hardening_risk_labels, validate_hardening_domain_label, validate_freeze_status

def test_labels():
    assert len(list_hardening_domain_labels()) > 0
    assert len(list_dead_code_labels()) > 0
    assert len(list_contract_labels()) > 0
    assert len(list_freeze_status_labels()) > 0
    assert len(list_hardening_risk_labels()) > 0
    validate_hardening_domain_label("source_hardening")
    validate_freeze_status("freeze_ready")
    assert "production_release" not in list_freeze_status_labels()
