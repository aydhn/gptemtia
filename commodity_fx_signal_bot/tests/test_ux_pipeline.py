import pytest
from pathlib import Path
import pandas as pd
from analyst_ux.ux_pipeline import AnalystUXPipeline
from analyst_ux.ux_config import get_default_analyst_ux_profile
from config.settings import settings

class MockDataLake:
    def save_command_alias_registry(self, df, summary): pass
    def save_safe_command_suggestions(self, df, summary): pass
    def save_prompt_pack_registry(self, df, summary): pass
    def save_prompt_pack_manifest(self, manifest): pass
    def save_productivity_checklist(self, df, summary): pass
    def save_analyst_task_board(self, df, summary): pass
    def save_ux_report(self, name, summary, md): pass

@pytest.fixture
def project_root():
    return Path(__file__).resolve().parent.parent

def test_pipeline_methods(project_root):
    dl = MockDataLake()
    profile = get_default_analyst_ux_profile()
    pipeline = AnalystUXPipeline(dl, settings, project_root, profile)

    df, summary = pipeline.build_ux_alias_report(save=True)
    assert not df.empty

    df, summary = pipeline.build_safe_command_suggestions("final review durumunu kontrol et")
    assert not df.empty

    df, summary = pipeline.build_prompt_pack_report()
    assert not df.empty

    df, summary = pipeline.build_productivity_checklist()
    assert not df.empty

    df, summary = pipeline.build_analyst_task_board()
    assert not df.empty

    df, summary = pipeline.build_operator_productivity_status()
    assert not df.empty
