import pandas as pd
from .runtime_config import AdvancedRuntimeProfile

def build_runtime_report_contract(profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    reports = [
        "markdown reports", "txt reports", "csv reports", "json reports",
        "status reports", "quality reports", "validation reports", "phase preparation reports"
    ]
    data = [{"report_type": r, "disclaimer": "Bu rapor local/offline advanced runtime consolidation çıktısıdır; canlı emir, broker talimatı, yatırım tavsiyesi, deployment, scraping veya official approval değildir."} for r in reports]
    df = pd.DataFrame(data)
    return df, summarize_runtime_report_contract(df)

def summarize_runtime_report_contract(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total_reports": len(df)}
