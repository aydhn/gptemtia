"""Test labels."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_labels import (
    list_reproducibility_domain_labels, list_reproducibility_status_labels, list_environment_replay_labels,
    list_determinism_labels, list_reproducibility_risk_labels,
    validate_reproducibility_domain_label, validate_reproducibility_status, validate_environment_replay_label,
    validate_determinism_label, validate_reproducibility_risk
)

def test_labels():
    assert list_reproducibility_domain_labels()
    assert list_reproducibility_status_labels()
    assert list_environment_replay_labels()
    assert list_determinism_labels()
    assert list_reproducibility_risk_labels()
    
    validate_reproducibility_domain_label(list_reproducibility_domain_labels()[0])
    validate_determinism_label(list_determinism_labels()[0])
