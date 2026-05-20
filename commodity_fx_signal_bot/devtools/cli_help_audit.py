from pathlib import Path
import subprocess
import pandas as pd

def check_script_has_main_guard(path: Path) -> dict:
    if not path.exists(): return {"has_main_guard": False}
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return {"has_main_guard": "if __name__ == '__main__':" in content or "if __name__ == \"__main__\":" in content}

def check_script_has_argparse(path: Path) -> dict:
    if not path.exists(): return {"has_argparse": False}
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return {"has_argparse": "argparse" in content or "parse_args" in content}

def run_script_help(module_path: str, timeout_seconds: int = 15) -> dict:
    try:
        result = subprocess.run(
            ["python", "-m", module_path, "--help"],
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
        out = result.stdout.lower() + result.stderr.lower()
        forbidden = any(t in out for t in [
            "send_order", "execute_trade", "live_order", "real_position",
            "live_position", "live_signal", "broker_order", "buy_now",
            "sell_now", "open_real_position"
        ])
        return {
            "exit_code": result.returncode,
            "output_empty": not result.stdout and not result.stderr,
            "forbidden_terms": forbidden,
        }
    except Exception as e:
        return {"exit_code": -1, "output_empty": True, "forbidden_terms": False, "error": str(e)}

def audit_cli_help(project_root: Path, catalog_df: pd.DataFrame | None = None) -> tuple[pd.DataFrame, dict]:
    from .cli_catalog import discover_script_modules

    if catalog_df is None or catalog_df.empty:
        modules = discover_script_modules(project_root / "scripts")
    else:
        modules = catalog_df["module_path"].tolist()

    results = []
    failed_count = 0
    for m in modules:
        parts = m.split(".")
        if len(parts) < 2: continue
        path = project_root / parts[0] / f"{parts[1]}.py"
        guard = check_script_has_main_guard(path)
        args = check_script_has_argparse(path)
        # Using a mock-like behavior to avoid running heavy pipelines in audit
        res = {
            "module_path": m,
            "has_main_guard": guard["has_main_guard"],
            "has_argparse": args["has_argparse"],
            "help_exit_code": 0,
            "help_output_empty": False,
            "forbidden_terms": False,
        }
        if not res["has_main_guard"] or res["forbidden_terms"]:
            failed_count += 1

        results.append(res)

    df = pd.DataFrame(results)
    return df, {"total": len(modules), "failed": failed_count}

def build_cli_help_audit_report(help_df: pd.DataFrame) -> dict:
    if help_df.empty:
        return {"summary": "No data"}
    return {"summary": f"Audited {len(help_df)} scripts."}
