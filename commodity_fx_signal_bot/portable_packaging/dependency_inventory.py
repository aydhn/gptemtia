import ast
import os
from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any, Optional

from portable_packaging.packaging_models import DependencyRecord, build_dependency_id

def parse_requirements_files(project_root: Path) -> pd.DataFrame:
    data = []
    for req_file in ["requirements.txt", "requirements-dev.txt"]:
        path = project_root / req_file
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue

                    # Very basic parsing
                    parts = line.split("==")
                    name = parts[0].strip().split(">")[0].split("<")[0].split("~")[0]
                    version = parts[1].strip() if len(parts) > 1 else None

                    data.append({
                        "package_name": name.lower(),
                        "required_version": version,
                        "source": req_file,
                        "requirement_detected": True,
                        "optional": req_file == "requirements-dev.txt"
                    })
    return pd.DataFrame(data)

def parse_pyproject_dependencies(project_root: Path) -> pd.DataFrame:
    # Not using tomli to avoid adding dependencies, very basic parsing or skip
    return pd.DataFrame(columns=["package_name", "required_version", "source", "requirement_detected", "optional"]).astype(str)

def collect_imported_packages(project_root: Path) -> pd.DataFrame:
    imports = set()
    for root, _, files in os.walk(project_root):
        for file in files:
            if file.endswith(".py"):
                path = Path(root) / file
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        tree = ast.parse(f.read())
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Import):
                                for alias in node.names:
                                    imports.add(alias.name.split(".")[0])
                            elif isinstance(node, ast.ImportFrom) and node.module:
                                imports.add(node.module.split(".")[0])
                except Exception:
                    pass

    # Filter stdlib roughly
    import sys
    stdlib = set(sys.stdlib_module_names) if hasattr(sys, "stdlib_module_names") else set()
    imports = imports - stdlib

    data = [
        {"package_name": imp.lower(), "import_detected": True, "source": "ast"}
        for imp in imports
    ]
    return pd.DataFrame(data)

def build_dependency_inventory(project_root: Path, installed_packages_df: Optional[pd.DataFrame] = None) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    req_df = parse_requirements_files(project_root)
    pyproj_df = parse_pyproject_dependencies(project_root)
    reqs = pd.concat([req_df, pyproj_df], ignore_index=True)

    imports_df = collect_imported_packages(project_root)
    if imports_df.empty:
        imports_df = pd.DataFrame(columns=["package_name", "import_detected", "source"]).astype(str)

    merged = pd.merge(reqs, imports_df, on="package_name", how="outer").fillna(
        {"requirement_detected": False, "import_detected": False, "optional": False, "source": "unknown"}
    )

    if installed_packages_df is not None and not installed_packages_df.empty:
        merged = pd.merge(merged, installed_packages_df, on="package_name", how="left")
    else:
        merged["installed_version"] = None

    records = []
    for _, row in merged.iterrows():
        warnings = []
        if row["requirement_detected"] and not row["import_detected"]:
            warnings.append("Required but not imported.")
        if row["import_detected"] and not row["requirement_detected"]:
            warnings.append("Imported but not required.")

        record = DependencyRecord(
            dependency_id=build_dependency_id(row["package_name"], row.get("source_x", row.get("source_y", "unknown"))),
            package_name=row["package_name"],
            installed_version=row["installed_version"],
            required_version=row.get("required_version"),
            source=row.get("source_x", row.get("source_y", "unknown")),
            import_detected=bool(row["import_detected"]),
            requirement_detected=bool(row["requirement_detected"]),
            optional=bool(row["optional"]),
            warnings=warnings
        )
        records.append(record)

    df = pd.DataFrame([r.__dict__ for r in records])
    summary = summarize_dependency_inventory(df)

    return df, summary

def compare_required_vs_installed(dependency_df: pd.DataFrame) -> pd.DataFrame:
    mismatches = dependency_df[
        (dependency_df["required_version"].notnull()) &
        (dependency_df["installed_version"].notnull()) &
        (dependency_df["required_version"] != dependency_df["installed_version"])
    ]
    return mismatches

def summarize_dependency_inventory(dependency_df: pd.DataFrame) -> Dict[str, Any]:
    if dependency_df.empty:
        return {"total_packages": 0}

    return {
        "total_packages": len(dependency_df),
        "required_packages": int(dependency_df["requirement_detected"].sum()),
        "imported_packages": int(dependency_df["import_detected"].sum()),
        "missing_requirements": int((~dependency_df["requirement_detected"] & dependency_df["import_detected"]).sum()),
    }
