import pandas as pd
from pathlib import Path
from .completion_config import LocalProjectCompletionProfile

def classify_final_command(script_name: str) -> dict:
    if "live" in script_name or "deploy" in script_name:
        return {"status": "unsafe", "warning": "Unknown command warning."}
    return {"status": "safe", "warning": "None"}

def classify_final_output_path(path: Path, project_root: Path) -> dict:
    return {"status": "local", "warning": "None"}

def build_final_command_map(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"command": "mock_cmd", "class": classify_final_command("mock")}])
    return df, summarize_final_command_map(df)

def build_final_output_map(project_root: Path, profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"output": "mock_out", "class": classify_final_output_path(Path("mock"), project_root)}])
    return df, summarize_final_output_map(df)

def summarize_final_command_map(df: pd.DataFrame) -> dict:
    return {"commands": len(df), "note": "Command map does not run commands."}

def summarize_final_output_map(df: pd.DataFrame) -> dict:
    return {"outputs": len(df), "note": "Output map does not move/modify files."}
