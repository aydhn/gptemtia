import pandas as pd
from pathlib import Path
from typing import Tuple, Dict
from final_review.final_review_config import FinalReviewProfile

def audit_module_importability(project_root: Path) -> pd.DataFrame:
    # Mock for offline research
    return pd.DataFrame([{"module": "data", "importable": True}])

def audit_pipeline_class_availability(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame([{"module": "data", "pipeline_class": "DataPipeline", "available": True}])

def audit_script_to_pipeline_mapping(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame([{"script": "run_data_pipeline.py", "pipeline": "DataPipeline", "mapped": True}])

def audit_tests_to_modules_mapping(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame([{"module": "data", "has_tests": True}])

def build_integration_audit_report(project_root: Path, profile: FinalReviewProfile) -> Tuple[pd.DataFrame, dict]:
    dfs = {
        "importability": audit_module_importability(project_root),
        "pipeline_classes": audit_pipeline_class_availability(project_root),
        "script_mapping": audit_script_to_pipeline_mapping(project_root),
        "test_mapping": audit_tests_to_modules_mapping(project_root)
    }

    summary = {
        "passed": True,
        "warnings": 0
    }

    # Combine or just return one for simplicity in the mock
    return dfs["importability"], summary
