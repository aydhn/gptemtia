import pandas as pd
from pathlib import Path
from scenario_regression.regression_config import ScenarioRegressionProfile

def validate_contract_file_exists(contract_row: pd.Series, project_root: Path) -> dict:
    path_str = contract_row.get("output_path", "")
    if not path_str:
        return {"valid": False, "error": "No output path defined"}
    path = project_root / path_str
    return {"valid": path.exists(), "error": None if path.exists() else "File does not exist"}

def validate_contract_non_empty(contract_row: pd.Series, project_root: Path) -> dict:
    path_str = contract_row.get("output_path", "")
    path = project_root / path_str
    if not path.exists():
        return {"valid": False, "error": "File does not exist"}
    if path.stat().st_size == 0:
        return {"valid": False, "error": "File is empty"}
    return {"valid": True, "error": None}

def validate_contract_disclaimer(contract_row: pd.Series, project_root: Path) -> dict:
    path_str = contract_row.get("output_path", "")
    path = project_root / path_str
    if not path.exists() or path.suffix not in [".txt", ".md"]:
        return {"valid": True, "error": None} # Skip for non-text
    try:
        content = path.read_text(encoding="utf-8").lower()
        if "yatırım tavsiyesi" not in content and "offline" not in content and "not investment advice" not in content:
            return {"valid": False, "error": "Disclaimer missing"}
    except Exception:
        pass
    return {"valid": True, "error": None}

def validate_contract_synthetic_label(contract_row: pd.Series, project_root: Path) -> dict:
    path_str = contract_row.get("output_path", "")
    path = project_root / path_str
    if not path.exists() or path.suffix not in [".txt", ".md", ".csv"]:
        return {"valid": True, "error": None}
    try:
        content = path.read_text(encoding="utf-8").lower()
        if "synthetic" not in content:
            return {"valid": False, "error": "Synthetic label missing"}
    except Exception:
        pass
    return {"valid": True, "error": None}

def validate_contract_expected_columns(contract_row: pd.Series, project_root: Path) -> dict:
    path_str = contract_row.get("output_path", "")
    expected_cols = contract_row.get("expected_columns", "")
    if not expected_cols or not isinstance(expected_cols, str):
        return {"valid": True, "error": None}

    path = project_root / path_str
    if not path.exists() or path.suffix != ".csv":
        return {"valid": False, "error": "Cannot validate columns, invalid file"}

    try:
        df = pd.read_csv(path, nrows=1)
        expected = [c.strip() for c in expected_cols.split(",")]
        missing = [c for c in expected if c not in df.columns]
        if missing:
            return {"valid": False, "error": f"Missing columns: {missing}"}
    except Exception as e:
        return {"valid": False, "error": str(e)}

    return {"valid": True, "error": None}

def validate_scenario_output_contracts(expected_df: pd.DataFrame, project_root: Path, profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    if expected_df.empty:
        return pd.DataFrame(), {"warnings": ["No expected outputs to validate"]}

    results = []
    warnings = []

    for _, row in expected_df.iterrows():
        scenario_id = row.get("scenario_id")
        output_name = row.get("output_name")

        exists_val = validate_contract_file_exists(row, project_root)
        empty_val = validate_contract_non_empty(row, project_root)
        disclaimer_val = validate_contract_disclaimer(row, project_root)
        synthetic_val = validate_contract_synthetic_label(row, project_root)
        cols_val = validate_contract_expected_columns(row, project_root)

        is_valid = exists_val["valid"] and empty_val["valid"] and (disclaimer_val["valid"] or not row.get("required", True))

        if not is_valid:
            warnings.append(f"Validation failed for {scenario_id} - {output_name}")

        results.append({
            "scenario_id": scenario_id,
            "output_name": output_name,
            "is_valid": is_valid,
            "exists": exists_val["valid"],
            "non_empty": empty_val["valid"],
            "has_disclaimer": disclaimer_val["valid"],
            "has_synthetic_label": synthetic_val["valid"],
            "has_expected_columns": cols_val["valid"],
        })

    df = pd.DataFrame(results)
    return df, {"warnings": warnings, "total_validated": len(results)}

def summarize_output_contract_validation(validation_df: pd.DataFrame) -> dict:
    if validation_df.empty:
        return {"total_contracts": 0}
    return {
        "total_contracts": len(validation_df),
        "valid_count": len(validation_df[validation_df["is_valid"]]) if "is_valid" in validation_df else 0,
        "invalid_count": len(validation_df[~validation_df["is_valid"]]) if "is_valid" in validation_df else 0,
    }
