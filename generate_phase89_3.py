import os
from pathlib import Path

def create_files():
    base_dir = Path("commodity_fx_signal_bot/local_longterm_operations")
    
    workbook_template = '''"""{module_name}"""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_{func_prefix}_review_items(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {{"item": "sample", "status": "needs_review", "warnings": ["{warning_text}"]}}
    ])

def build_{func_prefix}_review_workbook(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_{func_prefix}_review_items(profile)
    return df, summarize_{func_prefix}_review_workbook(df)

def summarize_{func_prefix}_review_workbook(df: pd.DataFrame) -> dict:
    return {{"total_items": len(df)}}
'''
    
    files = [
        ("retention_review_workbooks.py", "longterm_output_retention", "Dosya silmez. Otomatik retention uygulamaz."),
        ("datalake_review_workbook.py", "longterm_datalake", "Dosya taşımaz."),
        ("generated_docs_review_workbook.py", "longterm_generated_docs", "Generated docs review."),
        ("quality_review_workbook.py", "longterm_quality", "Official certification değildir."),
        ("safety_review_workbook.py", "longterm_safety", "Official certification değildir."),
        ("incident_redteam_governance_review.py", "longterm_incident_redteam_governance", "Gerçek operasyon onayı değildir.")
    ]
    
    for filename, func_prefix, warning in files:
        with open(base_dir / filename, "w", encoding="utf-8") as f:
            f.write(workbook_template.format(module_name=filename, func_prefix=func_prefix, warning_text=warning))

if __name__ == "__main__":
    create_files()
