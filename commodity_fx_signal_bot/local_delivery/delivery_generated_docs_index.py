import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_delivery_generated_docs_index(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"generated_doc_path": "docs/generated/dummy.md"}])
    return df, summarize_delivery_generated_docs_index(df)

def summarize_delivery_generated_docs_index(gdoc_df: pd.DataFrame) -> dict:
    return {"total_generated_docs": len(gdoc_df)}
