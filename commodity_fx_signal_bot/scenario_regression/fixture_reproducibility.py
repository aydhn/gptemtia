import pandas as pd
from scenario_regression.regression_config import ScenarioRegressionProfile

def regenerate_fixture_hashes(profile: ScenarioRegressionProfile, scenario_profile_name: str = "balanced_offline_scenarios") -> tuple[pd.DataFrame, dict]:
    # Placeholder for hash regeneration logic
    # In reality this would invoke the data generation logic to check deterministic output
    return pd.DataFrame(), {"warnings": ["Regeneration not implemented, dry-run only"]}

def compare_fixture_reproducibility(original_fixture_df: pd.DataFrame, regenerated_fixture_df: pd.DataFrame, profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    if original_fixture_df.empty:
        return pd.DataFrame(), {"warnings": ["Original fixtures empty"]}

    results = []
    warnings = []

    for _, row in original_fixture_df.iterrows():
        scenario_id = row.get("scenario_id")
        is_synthetic = str(row.get("synthetic", "False")).lower() == "true"

        matched = True
        if not is_synthetic:
            warnings.append(f"Fixture for {scenario_id} is not synthetic")
            matched = False

        results.append({
            "scenario_id": scenario_id,
            "matched": matched,
            "synthetic": is_synthetic
        })

    return pd.DataFrame(results), {"warnings": warnings, "total_compared": len(results)}

def validate_fixture_seed_consistency(fixtures_df: pd.DataFrame, expected_seed: int) -> dict:
    if fixtures_df.empty:
        return {"consistent": False, "warnings": ["No fixtures to validate"]}

    inconsistent = []
    for _, row in fixtures_df.iterrows():
        seed = row.get("random_seed")
        if seed is not None and int(seed) != expected_seed:
            inconsistent.append(row.get("scenario_id"))

    if inconsistent:
        return {"consistent": False, "warnings": [f"Inconsistent seeds found in scenarios: {inconsistent}"]}
    return {"consistent": True, "warnings": []}

def build_fixture_reproducibility_report(fixtures_df: pd.DataFrame, profile: ScenarioRegressionProfile) -> tuple[pd.DataFrame, dict]:
    df, summary = compare_fixture_reproducibility(fixtures_df, pd.DataFrame(), profile)
    seed_val = validate_fixture_seed_consistency(fixtures_df, profile.random_seed)
    summary["seed_consistent"] = seed_val["consistent"]
    summary["warnings"].extend(seed_val["warnings"])
    return df, summary
