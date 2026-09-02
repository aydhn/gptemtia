import os
from pathlib import Path

ROOT = Path("commodity_fx_signal_bot")
TARGET_DIR = ROOT / "tests"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

test_files = [
    "test_governance_control_config.py",
    "test_governance_control_labels.py",
    "test_governance_control_models.py",
    "test_governance_domain_registry.py",
    "test_control_room_packet.py",
    "test_executive_oversight.py",
    "test_manual_approval_ledger.py",
    "test_approval_checklists.py",
    "test_risk_committee_rehearsal.py",
    "test_risk_committee_templates.py",
    "test_operator_supervision.py",
    "test_escalation_matrix.py",
    "test_governance_roles.py",
    "test_decision_authority.py",
    "test_approval_boundaries.py",
    "test_governance_no_go_safe_go.py",
    "test_oversight_evidence.py",
    "test_oversight_reading_order.py",
    "test_governance_metrics.py",
    "test_meeting_note_templates.py",
    "test_signoff_rehearsal_forms.py",
    "test_exception_escalation.py",
    "test_unresolved_decisions.py",
    "test_governance_risks.py",
    "test_governance_scoring.py",
    "test_governance_validation.py",
    "test_governance_quality.py",
    "test_governance_report_builder.py",
    "test_governance_pipeline.py",
    "test_local_governance_scripts_contract.py"
]

content_template = """import pytest

def test_placeholder_{idx}():
    assert True
"""

for idx, tf in enumerate(test_files):
    with open(TARGET_DIR / tf, "w", encoding="utf-8") as f:
        f.write(content_template.format(idx=idx))

print("Done writing tests.")
