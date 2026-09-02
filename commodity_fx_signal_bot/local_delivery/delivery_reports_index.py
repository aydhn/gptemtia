import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_delivery_reports_index(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"report_path": "reports/dummy_report.csv"}])
    return df, summarize_delivery_reports_index(df)

def summarize_delivery_reports_index(report_df: pd.DataFrame) -> dict:
    return {"total_reports": len(report_df)}
