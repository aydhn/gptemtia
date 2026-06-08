
from pathlib import Path
import pandas as pd
from typing import Tuple, Optional
from secrets_hygiene.secrets_config import SecretsHygieneProfile
from secrets_hygiene.secrets_models import EnvTemplateAuditItem, build_env_template_item_id

def parse_env_template(path: Path) -> pd.DataFrame:
    items = []
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        items.append({"variable_name": k.strip(), "value": v.strip()})
        except Exception: pass
    return pd.DataFrame(items)

def classify_env_variable_safety(name: str, value: str | None) -> dict:
    if not value: return {"has_placeholder": True, "has_realistic_secret_value": False, "status": "safe"}
    v_lower = value.lower()
    if any(p in v_lower for p in ["your_", "changeme", "placeholder", "xxx", "dummy", "<", "123"]):
        return {"has_placeholder": True, "has_realistic_secret_value": False, "status": "safe"}
    if v_lower in ["true", "false", "1", "0", "yes", "no"]:
        return {"has_placeholder": False, "has_realistic_secret_value": False, "status": "safe"}
    if any(x in name.lower() for x in ["api", "secret", "key", "token"]) and len(value) > 12:
        return {"has_placeholder": False, "has_realistic_secret_value": True, "status": "warning"}
    return {"has_placeholder": False, "has_realistic_secret_value": False, "status": "info"}

def audit_env_template(project_root: Path, profile: SecretsHygieneProfile) -> Tuple[pd.DataFrame, dict]:
    parsed_df = parse_env_template(project_root / ".env.example")
    if parsed_df.empty: return pd.DataFrame(), {"error": "No .env.example found"}
    audit_items = []
    for _, row in parsed_df.iterrows():
        safety = classify_env_variable_safety(row["variable_name"], row["value"])
        audit_items.append(EnvTemplateAuditItem(
            item_id=build_env_template_item_id(row["variable_name"], ".env.example"),
            variable_name=row["variable_name"], template_path=".env.example",
            status=safety["status"], has_placeholder=safety["has_placeholder"],
            has_realistic_secret_value=safety["has_realistic_secret_value"],
            recommendation="Replace real-looking secret with a placeholder" if safety["has_realistic_secret_value"] else "No action needed.",
            warnings=[]
        ))
    df = pd.DataFrame([item.__dict__ for item in audit_items])
    return df, {"total_variables": len(df), "realistic_secrets_found": len(df[df["has_realistic_secret_value"]]), "placeholders_used": len(df[df["has_placeholder"]])}

def build_env_template_recommendations(audit_df: pd.DataFrame) -> pd.DataFrame:
    if audit_df.empty: return pd.DataFrame()
    return audit_df[audit_df["has_realistic_secret_value"]].copy()[["variable_name", "template_path", "recommendation"]]
