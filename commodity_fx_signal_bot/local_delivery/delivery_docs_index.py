import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_delivery_docs_index(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"doc_path": "README.md"}])
    return df, summarize_delivery_docs_index(df)

def summarize_delivery_docs_index(doc_df: pd.DataFrame) -> dict:
    return {"total_docs": len(doc_df)}
