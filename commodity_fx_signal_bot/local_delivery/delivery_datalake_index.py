import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_delivery_datalake_index(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"datalake_path": "data/lake/dummy.csv"}])
    return df, summarize_delivery_datalake_index(df)

def summarize_delivery_datalake_index(dl_df: pd.DataFrame) -> dict:
    return {"total_datalake_items": len(dl_df)}
