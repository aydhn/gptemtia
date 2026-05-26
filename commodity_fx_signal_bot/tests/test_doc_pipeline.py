import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pytest
from pathlib import Path
from documentation.doc_pipeline import DocumentationPipeline
from config.settings import Settings

class MockDataLake:
    def __init__(self):
        class MockPaths:
            pass
        self.paths = MockPaths()
    def save_documentation_inventory(self, *args, **kwargs): pass
    def save_documentation_coverage(self, *args, **kwargs): pass
    def save_documentation_pack_manifest(self, *args, **kwargs): pass
    def save_documentation_quality(self, *args, **kwargs): pass

def test_doc_pipeline_methods(tmp_path):
    dl = MockDataLake()
    settings = Settings()
    pipeline = DocumentationPipeline(dl, settings, tmp_path)

    dfs, summary = pipeline.build_documentation_pack_report(save=False)
    assert isinstance(dfs, dict)
    assert isinstance(summary, dict)

    quality, _ = pipeline.build_documentation_quality_report(save=False)
    assert isinstance(quality, dict)

    saf_df, _ = pipeline.build_safe_usage_docs_report(save=False)
    assert saf_df is not None

    scr_df, _ = pipeline.build_script_reference_report(save=False)
    assert scr_df.empty

    out_df, _ = pipeline.build_output_reference_report(save=False)
    assert out_df.empty

    stat_df, _ = pipeline.build_documentation_status(save=False)
    assert stat_df.empty
