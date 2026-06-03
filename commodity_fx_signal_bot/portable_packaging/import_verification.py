import importlib
import sys
from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any, List

def build_core_module_list() -> List[str]:
    return [
        "data", "features", "candidates", "risk", "backtest", "validation", "ml",
        "paper", "orchestration", "observability", "security", "research_reports",
        "report_exports", "portfolio_research", "portfolio_regime", "synthetic_indices",
        "factor_research", "meta_research", "experiments", "governance", "research_planning",
        "knowledge_base", "command_center", "quality_gates", "performance", "maintenance",
        "documentation", "final_review", "scenarios", "scenario_regression", "analyst_ux",
        "report_summarization", "master_orchestration", "portable_packaging"
    ]

def verify_module_import(module_name: str, project_root: Path) -> Dict[str, Any]:
    # Temporarily add project root to path
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    try:
        importlib.import_module(module_name)
        return {"module_name": module_name, "importable": True, "error": None}
    except Exception as e:
        return {"module_name": module_name, "importable": False, "error": str(e)}
    finally:
        if str(project_root) in sys.path:
            sys.path.remove(str(project_root))

def verify_core_module_imports(project_root: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    core_modules = build_core_module_list()
    results = []

    for mod in core_modules:
        # Check if directory exists before importing to avoid noise
        if (project_root / mod).exists():
            results.append(verify_module_import(mod, project_root))
        else:
            results.append({"module_name": mod, "importable": False, "error": "Module directory not found"})

    df = pd.DataFrame(results)
    return df, summarize_import_verification(df)

def verify_pipeline_imports(project_root: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    # Just reusing core imports logic for pipeline for now
    return verify_core_module_imports(project_root)

def summarize_import_verification(import_df: pd.DataFrame) -> Dict[str, Any]:
    if import_df.empty:
        return {"total_modules": 0, "successful_imports": 0, "failed_imports": 0}

    return {
        "total_modules": len(import_df),
        "successful_imports": int(import_df["importable"].sum()),
        "failed_imports": len(import_df) - int(import_df["importable"].sum()),
    }
