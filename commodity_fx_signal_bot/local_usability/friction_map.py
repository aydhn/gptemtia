import pandas as pd
from pathlib import Path
from .usability_config import LocalUsabilityProfile
from .usability_models import OperatorFrictionItem, build_operator_friction_id

def classify_friction_level(description: str, profile: LocalUsabilityProfile) -> str:
    return "friction_medium"

def detect_operator_friction_items(project_root: Path, profile: LocalUsabilityProfile) -> list[OperatorFrictionItem]:
    return [
        OperatorFrictionItem(
            friction_id=build_operator_friction_id("çok fazla script", "scripts"),
            friction_area="çok fazla script",
            source_layer="scripts",
            friction_label="friction_high",
            description="Çok fazla script var.",
            recommended_manual_action="Command discoverability guide okuyun.",
            warnings=["Gerçek kullanıcı testi değildir."]
        )
    ]

def build_operator_friction_map(project_root: Path, profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    items = detect_operator_friction_items(project_root, profile)
    df = pd.DataFrame([i.__dict__ for i in items])
    return df, {"total_friction_items": len(items)}

def summarize_operator_friction_map(friction_df: pd.DataFrame) -> dict:
    return {"total": len(friction_df)}
