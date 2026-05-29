import pandas as pd
from scenario_regression.regression_config import ScenarioRegressionProfile

def validate_demo_workflow_steps(workflow_df: pd.DataFrame, profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    if workflow_df is None or workflow_df.empty:
        return pd.DataFrame(), {"warnings": ["Workflow dataframe is empty"]}

    results = []
    warnings = []

    for _, row in workflow_df.iterrows():
        step_num = row.get("step_number")
        if pd.isna(step_num):
            warnings.append("Missing step_number")
            continue

        is_valid = True
        cmd = str(row.get("command", "")).lower()

        if "live" in cmd or "broker" in cmd or "deploy" in cmd:
            warnings.append(f"Unsafe command in step {step_num}")
            is_valid = False

        results.append({
            "step_number": step_num,
            "workflow_id": row.get("workflow_id", "unknown"),
            "is_valid": is_valid
        })

    return pd.DataFrame(results), {"warnings": warnings, "total_steps": len(results)}

def validate_demo_command_sequences(command_df: pd.DataFrame, profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    if command_df is None or command_df.empty:
        return pd.DataFrame(), {"warnings": ["Command dataframe is empty"]}

    results = []
    warnings = []

    for _, row in command_df.iterrows():
        cmd = str(row.get("command", "")).lower()
        is_safe = "live" not in cmd and "broker" not in cmd and "deploy" not in cmd and "daemon" not in cmd
        if not is_safe:
            warnings.append(f"Unsafe command found: {cmd}")

        results.append({
            "command": row.get("command"),
            "is_safe": is_safe
        })

    return pd.DataFrame(results), {"warnings": warnings}

def validate_module_demo_flows(flow_df: pd.DataFrame, profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    if flow_df is None or flow_df.empty:
        return pd.DataFrame(), {"warnings": ["Flow dataframe is empty"]}

    results = []
    warnings = []

    for _, row in flow_df.iterrows():
        module = row.get("module")
        has_offline = str(row.get("offline_supported", "False")).lower() == "true"

        if not has_offline:
            warnings.append(f"Module {module} does not declare offline support")

        results.append({
            "module": module,
            "is_valid": has_offline
        })

    return pd.DataFrame(results), {"warnings": warnings}

def build_demo_workflow_regression_report(workflow_df: pd.DataFrame | None, command_df: pd.DataFrame | None, flow_df: pd.DataFrame | None, profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    w_df, w_meta = validate_demo_workflow_steps(workflow_df if workflow_df is not None else pd.DataFrame(), profile)
    c_df, c_meta = validate_demo_command_sequences(command_df if command_df is not None else pd.DataFrame(), profile)
    f_df, f_meta = validate_module_demo_flows(flow_df if flow_df is not None else pd.DataFrame(), profile)

    warnings = w_meta.get("warnings", []) + c_meta.get("warnings", []) + f_meta.get("warnings", [])

    # Compile a summary dataframe
    summary_data = {
        "workflow_valid": w_df["is_valid"].all() if not w_df.empty else False,
        "commands_safe": c_df["is_safe"].all() if not c_df.empty else False,
        "modules_offline": f_df["is_valid"].all() if not f_df.empty else False,
    }
    df = pd.DataFrame([summary_data])

    return df, {"warnings": warnings, "summary": summary_data}
