import pytest
from pathlib import Path
import pandas as pd
from final_review.final_review_pipeline import FinalReviewPipeline
from final_review.final_review_config import get_default_final_review_profile
from config.settings import settings

class MockDataLake:
    def __init__(self, root):
        self.root = root
    def save_architecture_audit(self, df, summary=None): pass
    def save_safety_audit(self, df, summary=None): pass
    def save_integration_audit(self, df, summary=None): pass
    def save_command_audit(self, df, summary=None): pass
    def save_datalake_contract_audit(self, df, summary=None): pass
    def save_report_output_audit(self, df, summary=None): pass
    def save_documentation_audit(self, df, summary=None): pass
    def save_quality_gate_audit(self, df, summary=None): pass
    def save_readiness_audit(self, df, summary=None): pass
    def save_final_risk_register(self, df, summary=None): pass
    def save_final_gap_register(self, df, summary=None): pass
    def save_final_acceptance_checklist(self, df, summary=None): pass
    def save_final_acceptance_snapshot(self, snapshot): pass
    def save_release_readiness_dry_run(self, df, summary=None): pass
    def save_phase_1_55_consolidation_audit(self, name, df, summary=None): pass
    def save_final_review_quality(self, name, quality): pass
    def save_final_review_report(self, name, report, md): pass

@pytest.fixture
def project_root():
    return Path(__file__).resolve().parent.parent

def test_final_review_pipeline(project_root):
    profile = get_default_final_review_profile()
    dl = MockDataLake(project_root)
    pipeline = FinalReviewPipeline(dl, settings, project_root, profile)

    tables, summary = pipeline.build_final_system_review(save=True)
    assert "architecture" in tables
    assert summary["passed"] is not None
