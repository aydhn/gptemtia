"""Test pipeline."""
from pathlib import Path
from commodity_fx_signal_bot.local_documentation_export.documentation_export_pipeline import LocalDocumentationExportPipeline
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

class MockSettings:
    pass

def test_pipeline():
    p = get_default_local_documentation_export_profile()
    pipe = LocalDocumentationExportPipeline(None, MockSettings(), Path("."), p)
    df, s = pipe.build_documentation_export_domain_registry(save=False)
    assert isinstance(s, dict)
