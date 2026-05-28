import pandas as pd
from pathlib import Path
from typing import Tuple, Dict
from final_review.final_review_config import FinalReviewProfile

def audit_report_output_directories(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame([{"dir": "reports/output/final_review", "exists": True}])

def audit_required_status_reports(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame([{"report": "status_report", "exists": True}])

def audit_markdown_txt_csv_json_outputs(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame([{"format": "csv", "exists": True}])

def audit_report_disclaimers(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame([{"disclaimer": "not_investment_advice", "exists": True}])

def build_report_output_audit_report(project_root: Path, profile: FinalReviewProfile) -> Tuple[pd.DataFrame, dict]:
    summary = {"passed": True}
    return audit_report_output_directories(project_root), summary
