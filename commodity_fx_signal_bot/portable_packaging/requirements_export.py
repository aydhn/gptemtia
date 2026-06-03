from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any, Optional

def build_requirements_export(dependency_df: pd.DataFrame, installed_df: Optional[pd.DataFrame] = None) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    # Unused placeholder mapping to the overall process
    return dependency_df, {"exported": True}

def build_requirements_minimal_export(dependency_df: pd.DataFrame) -> Tuple[str, Dict[str, Any]]:
    required = dependency_df[dependency_df["requirement_detected"] == True]
    lines = []
    for _, row in required.iterrows():
        if not pd.isna(row["required_version"]) and row["required_version"]:
            lines.append(f"{row['package_name']}=={row['required_version']}")
        else:
            lines.append(f"{row['package_name']}")

    text = "\n".join(sorted(lines)) + "\n"
    return text, {"type": "minimal", "count": len(lines)}

def build_requirements_frozen_export(installed_df: pd.DataFrame) -> Tuple[str, Dict[str, Any]]:
    lines = []
    for _, row in installed_df.iterrows():
        if not pd.isna(row["installed_version"]) and row["installed_version"]:
            lines.append(f"{row['package_name']}=={row['installed_version']}")
        else:
            lines.append(f"{row['package_name']}")

    text = "# LOCAL ENVIRONMENT SNAPSHOT\n# Bu dosya mevcut lokal ortamin dondurulmus halidir, her makinede calisma garantisi yoktur.\n\n"
    text += "\n".join(sorted(lines)) + "\n"
    return text, {"type": "frozen_local", "count": len(lines)}

def build_optional_dependencies_note(dependency_df: pd.DataFrame) -> str:
    optional = dependency_df[dependency_df["optional"] == True]
    text = "# Optional Dependencies\n\n"
    if optional.empty:
        text += "No optional dependencies detected.\n"
    else:
        for _, row in optional.iterrows():
            text += f"- {row['package_name']}\n"
    return text

def save_requirements_exports(output_dir: Path, exports: Dict[str, str]) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    output_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for name, content in exports.items():
        path = output_dir / name
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        records.append({"filename": name, "size_bytes": len(content)})

    df = pd.DataFrame(records)
    summary = {"files_created": len(records)}
    return df, summary
