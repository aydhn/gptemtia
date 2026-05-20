from pathlib import Path
import pandas as pd
from .dev_models import CLICommandInfo

def discover_script_modules(scripts_dir: Path) -> list[str]:
    if not scripts_dir.exists():
        return []
    return [
        f"scripts.{f.stem}"
        for f in scripts_dir.glob("run_*.py")
        if f.is_file() and not f.name.startswith("__")
    ]

def infer_command_group(module_path: str) -> str:
    name = module_path.split(".")[-1]
    if name.startswith("run_data_"): return "data"
    if name.startswith("run_feature_"): return "features"
    if any(x in name for x in ["run_signal", "run_decision", "run_strategy"]): return "candidates"
    if any(x in name for x in ["run_risk", "run_sizing", "run_level"]): return "risk_sizing_level"
    if "run_backtest" in name: return "backtest"
    if "run_performance" in name: return "performance"
    if any(x in name for x in ["run_validation", "walk_forward", "optimizer"]): return "validation"
    if name.startswith("run_ml_"): return "ml"
    if name.startswith("run_paper_"): return "paper"
    if any(x in name for x in ["run_telegram", "run_notification"]): return "notifications"
    if any(x in name for x in ["run_workflow", "run_dependency", "run_daily", "run_full"]): return "orchestration"
    if any(x in name for x in ["run_system_health", "run_observability"]): return "observability"
    if any(x in name for x in ["run_security", "run_secret", "run_config_hardening"]): return "security"
    if any(x in name for x in ["run_cli", "run_import", "run_test_matrix", "run_dx", "run_local_dev"]): return "devtools"
    return "unknown_group"

def infer_command_description(module_path: str) -> str:
    return f"Runs the {module_path.split('.')[-1]} script."

def build_command_example(module_path: str, group: str) -> str:
    return f"python -m {module_path}"

def build_cli_command_catalog(project_root: Path) -> tuple[pd.DataFrame, dict]:
    scripts_dir = project_root / "scripts"
    modules = discover_script_modules(scripts_dir)
    infos = []
    for m in modules:
        group = infer_command_group(m)
        infos.append(
            CLICommandInfo(
                command_name=m.split(".")[-1],
                module_path=m,
                group=group,
                description=infer_command_description(m),
                example=build_command_example(m, group),
                supports_help=True,
                supports_dry_run=True,
                requires_symbol=False,
                requires_timeframe=False,
                output_report=None,
                warnings=[],
            )
        )
    df = pd.DataFrame([info.__dict__ for info in infos])
    summary = {"total_commands": len(infos)}
    return df, summary

def export_cli_catalog_markdown(catalog_df: pd.DataFrame) -> str:
    if catalog_df.empty:
        return "No commands found."
    return catalog_df.to_markdown(index=False)
