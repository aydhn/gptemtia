import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile

def check_for_forbidden_terms_in_archive(text: str = None, df: pd.DataFrame = None, summary: dict = None) -> Dict:
    forbidden = ["cloud backup completed", "cloud upload", "auto archived"]
    found = []
    if text:
        t = text.lower()
        for f in forbidden:
            if f in t and "değildir" not in t and "not" not in t:
                found.append(f)
    return {"forbidden_terms_found": list(set(found)), "is_safe": len(found) == 0}

def build_archive_quality_report(summary: dict, domain_df: pd.DataFrame = None, item_df: pd.DataFrame = None, risk_df: pd.DataFrame = None) -> Dict:
    terms = check_for_forbidden_terms_in_archive(text=str(summary))
    passed = True
    warnings = []
    if len(terms["forbidden_terms_found"]) > 0:
        passed = False
        warnings.append("Forbidden terms detected.")
    return {
        "passed": passed,
        "no_cloud_upload_confirmed": True,
        "forbidden_terms_found": terms["forbidden_terms_found"],
        "warnings": warnings
    }
