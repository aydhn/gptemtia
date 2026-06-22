import pandas as pd
from typing import Tuple, Dict, Any
from pathlib import Path
import re
from datetime import datetime, timezone

from local_maintenance.maintenance_config import LocalMaintenanceProfile
from local_maintenance.maintenance_models import DependencyWatchItem, build_dependency_watch_id, dependency_watch_item_to_dict

def discover_dependency_files(project_root: Path) -> pd.DataFrame:
    files = []

    req_txt = project_root / "requirements.txt"
    if req_txt.exists():
        files.append({"file_name": "requirements.txt", "type": "requirements", "path": str(req_txt)})

    req_dev_txt = project_root / "requirements-dev.txt"
    if req_dev_txt.exists():
        files.append({"file_name": "requirements-dev.txt", "type": "requirements", "path": str(req_dev_txt)})

    pyproject = project_root / "pyproject.toml"
    if pyproject.exists():
        files.append({"file_name": "pyproject.toml", "type": "pyproject", "path": str(pyproject)})

    return pd.DataFrame(files)

def parse_requirements_file(path: Path) -> pd.DataFrame:
    deps = []
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    # Basic parse, splitting by ==, >=, etc.
                    match = re.split(r'[=><!~]+', line)
                    if match:
                        dep_name = match[0].strip()
                        version_spec = line[len(dep_name):].strip() if len(match) > 1 else None
                        deps.append({
                            "dependency_name": dep_name,
                            "source_file": path.name,
                            "version_spec": version_spec
                        })
    return pd.DataFrame(deps)

def parse_pyproject_dependencies(path: Path) -> pd.DataFrame:
    deps = []
    if path.exists():
        # A simple fallback parser. A real parser would use `tomli` or similar.
        in_deps_section = False
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("[") and line.endswith("]"):
                    in_deps_section = "dependencies" in line.lower()
                    continue

                if in_deps_section and line and not line.startswith("#"):
                    if "=" in line:
                        dep_name, version = line.split("=", 1)
                        deps.append({
                            "dependency_name": dep_name.strip().strip('"').strip("'"),
                            "source_file": path.name,
                            "version_spec": version.strip().strip('"').strip("'")
                        })
    return pd.DataFrame(deps)

def parse_imports_from_source(project_root: Path) -> pd.DataFrame:
    # A rudimentary import parser
    imports = set()
    for py_file in project_root.rglob("*.py"):
        if "site-packages" in str(py_file) or ".venv" in str(py_file):
            continue
        try:
            with open(py_file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("import ") or line.startswith("from "):
                        parts = line.split()
                        if len(parts) > 1:
                            mod = parts[1].split('.')[0]
                            imports.add(mod)
        except Exception:
            pass

    data = [{"dependency_name": mod, "source_file": "source_imports", "version_spec": None} for mod in imports]
    return pd.DataFrame(data)

def classify_dependency_status(row: pd.Series, profile: LocalMaintenanceProfile) -> str:
    # For this offline/local watch, we base status mostly on metadata presence.
    # No internet connection is made to check current versions.
    if pd.isna(row.get("version_spec")) or not str(row.get("version_spec")).strip():
        return "dependency_missing_metadata"

    return "dependency_current"

def build_dependency_aging_watch_report(project_root: Path, profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if not profile.scan_requirements:
        return pd.DataFrame(), {"status": "skipped", "reason": "scan_requirements is False"}

    files_df = discover_dependency_files(project_root)
    all_deps = []

    for _, row in files_df.iterrows():
        path = Path(row["path"])
        if row["type"] == "requirements":
            df = parse_requirements_file(path)
        elif row["type"] == "pyproject":
            df = parse_pyproject_dependencies(path)
        else:
            df = pd.DataFrame()

        if not df.empty:
            all_deps.append(df)

    if all_deps:
        combined_df = pd.concat(all_deps, ignore_index=True)
    else:
        combined_df = pd.DataFrame()

    items = []
    for _, row in combined_df.iterrows():
        status = classify_dependency_status(row, profile)
        item = DependencyWatchItem(
            dependency_id=build_dependency_watch_id(row["dependency_name"], row["source_file"]),
            dependency_name=row["dependency_name"],
            source_file=row["source_file"],
            version_spec=row["version_spec"],
            status=status,
            review_reason="Offline metadata check.",
            recommendation="Review manually if update is needed. Do not use automatic update scripts.",
            warnings=["No internet version check performed."]
        )
        items.append(item)

    res_df = pd.DataFrame([dependency_watch_item_to_dict(i) for i in items])
    summary = summarize_dependency_aging(res_df)
    return res_df, summary

def summarize_dependency_aging(dep_df: pd.DataFrame) -> Dict[str, Any]:
    if dep_df is None or dep_df.empty:
        return {"total_dependencies": 0}

    return {
        "total_dependencies": len(dep_df),
        "status_counts": dep_df["status"].value_counts().to_dict(),
        "disclaimer": "This report relies on local file timestamp and version pin presence only. No external cloud or internet connection is used. Automatic upgrades are strictly forbidden."
    }
