import pandas as pd
from pathlib import Path
from typing import Tuple, Dict

_MODULES = [
    "data", "features", "candidates", "risk", "backtest", "validation", "ml",
    "paper", "notifications", "orchestration", "observability", "security",
    "research_reports", "report_exports", "portfolio_research", "portfolio_regime",
    "synthetic_indices", "factor_research", "meta_research", "experiments",
    "governance", "research_planning", "knowledge_base", "command_center",
    "quality_gates", "performance", "maintenance", "documentation", "final_review"
]

def build_module_inventory(project_root: Path) -> pd.DataFrame:
    rows = []
    for mod in _MODULES:
        mod_path = project_root / mod
        exists = mod_path.exists() and mod_path.is_dir()
        init_exists = (mod_path / "__init__.py").exists() if exists else False
        rows.append({
            "module": mod,
            "exists": exists,
            "has_init": init_exists,
            "status": "ok" if exists and init_exists else "missing"
        })
    return pd.DataFrame(rows)

def build_script_inventory(project_root: Path) -> pd.DataFrame:
    scripts_dir = project_root / "scripts"
    if not scripts_dir.exists():
        return pd.DataFrame(columns=["script_name", "path", "status"])

    rows = []
    for script in scripts_dir.glob("*.py"):
        rows.append({
            "script_name": script.name,
            "path": str(script.relative_to(project_root)),
            "status": "ok"
        })
    return pd.DataFrame(rows)

def build_test_inventory(project_root: Path) -> pd.DataFrame:
    tests_dir = project_root / "tests"
    if not tests_dir.exists():
        return pd.DataFrame(columns=["test_name", "path", "status"])

    rows = []
    for test in tests_dir.rglob("test_*.py"):
        rows.append({
            "test_name": test.name,
            "path": str(test.relative_to(project_root)),
            "status": "ok"
        })
    return pd.DataFrame(rows)

def build_report_inventory(project_root: Path) -> pd.DataFrame:
    reports_dir = project_root / "reports" / "output"
    if not reports_dir.exists():
        return pd.DataFrame(columns=["report_type", "path", "exists"])

    rows = []
    for p in ["csv", "markdown", "txt", "json", "html"]:
        path = reports_dir / p
        rows.append({
            "report_type": p,
            "path": str(path.relative_to(project_root)) if path.exists() else f"reports/output/{p}",
            "exists": path.exists()
        })
    return pd.DataFrame(rows)

def build_datalake_inventory(project_root: Path) -> pd.DataFrame:
    lake_dir = project_root / "data" / "lake"
    if not lake_dir.exists():
        return pd.DataFrame(columns=["folder_name", "path", "exists"])

    rows = []
    for folder in lake_dir.iterdir():
        if folder.is_dir():
            rows.append({
                "folder_name": folder.name,
                "path": str(folder.relative_to(project_root)),
                "exists": True
            })
    return pd.DataFrame(rows)

def build_docs_inventory(project_root: Path) -> pd.DataFrame:
    docs_dir = project_root / "docs"
    if not docs_dir.exists():
        return pd.DataFrame(columns=["doc_name", "path", "exists"])

    rows = []
    for doc in docs_dir.glob("*.md"):
        rows.append({
            "doc_name": doc.name,
            "path": str(doc.relative_to(project_root)),
            "exists": True
        })
    return pd.DataFrame(rows)

def build_full_system_inventory(project_root: Path) -> Tuple[Dict[str, pd.DataFrame], dict]:
    tables = {
        "modules": build_module_inventory(project_root),
        "scripts": build_script_inventory(project_root),
        "tests": build_test_inventory(project_root),
        "reports": build_report_inventory(project_root),
        "datalake": build_datalake_inventory(project_root),
        "docs": build_docs_inventory(project_root),
    }

    missing_modules = tables["modules"][tables["modules"]["status"] != "ok"]["module"].tolist()

    summary = {
        "module_count": len(tables["modules"]),
        "missing_modules": len(missing_modules),
        "missing_module_list": missing_modules,
        "script_count": len(tables["scripts"]),
        "test_count": len(tables["tests"]),
        "report_folder_count": len(tables["reports"]),
        "datalake_folder_count": len(tables["datalake"]),
        "doc_count": len(tables["docs"])
    }

    return tables, summary
