import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from orchestration.pipeline_orchestrator import PipelineOrchestrator
from orchestration.orchestration_config import get_default_orchestration_profile
from unittest.mock import MagicMock

def test_pipeline_orchestrator():
    mock_lake = MagicMock()
    mock_settings = MagicMock()

    orch = PipelineOrchestrator(mock_lake, mock_settings)

    manifest, summary = orch.run_workflow("healthcheck_workflow", [], "1d", dry_run=True, save=False)
    assert manifest.run_id is not None
    assert summary["status"] == "workflow_dry_run"
