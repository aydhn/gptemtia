import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile
from local_simplification.simplification_models import ComplexityItem, build_complexity_item_id, complexity_item_to_dict
from local_simplification.simplification_labels import validate_complexity_level

def classify_complexity_level(metric_value: int | float | None, metric_name: str) -> str:
    if metric_value is None:
        return "complexity_unknown"
    
    if metric_name == "folder_depth":
        if metric_value > 5: return "complexity_very_high"
        elif metric_value > 3: return "complexity_high"
        elif metric_value > 1: return "complexity_medium"
        else: return "complexity_low"
    elif metric_name == "file_count":
        if metric_value > 100: return "complexity_very_high"
        elif metric_value > 50: return "complexity_high"
        elif metric_value > 20: return "complexity_medium"
        else: return "complexity_low"
    elif metric_name == "function_count":
        if metric_value > 20: return "complexity_very_high"
        elif metric_value > 10: return "complexity_high"
        elif metric_value > 5: return "complexity_medium"
        else: return "complexity_low"
    
    return "complexity_unknown"

def build_final_modular_complexity_map(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    items = []
    
    # Just a placeholder for the final map, normally we'd aggregate from the other modules.
    df = pd.DataFrame(items)
    summary = summarize_modular_complexity_map(df)
    return df, summary

def summarize_modular_complexity_map(complexity_df: pd.DataFrame) -> dict:
    return {
        "total_items": len(complexity_df) if complexity_df is not None else 0,
        "warnings": ["Bu rapor official architecture assessment degildir."]
    }
