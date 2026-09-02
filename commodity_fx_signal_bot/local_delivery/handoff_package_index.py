import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile
from local_delivery.delivery_models import DeliveryItem, build_delivery_item_id, delivery_item_to_dict

def classify_handoff_item_label(path: Path, project_root: Path) -> str:
    parts = path.parts
    if "docs" in parts:
        return "delivery_doc_item"
    if "reports" in parts:
        return "delivery_report_item"
    if "data" in parts and "lake" in parts:
        return "delivery_datalake_item"
    if "scripts" in parts:
        return "delivery_script_item"
    if "tests" in parts:
        return "delivery_test_item"
    return "delivery_unknown_item"

def classify_handoff_source_layer(path: Path, project_root: Path) -> str:
    return str(path.parent.name) if path.parent.name else "root"

def build_handoff_package_index(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    # Placeholder
    items = []
    df = pd.DataFrame([delivery_item_to_dict(i) for i in items]) if items else pd.DataFrame(columns=["item_id", "item_label", "relative_path", "source_layer", "item_status", "size_bytes", "modified_at_utc", "delivery_notes", "warnings"])
    return df, summarize_handoff_package_index(df)

def summarize_handoff_package_index(index_df: pd.DataFrame) -> dict:
    return {"total_items_in_index": len(index_df)}
