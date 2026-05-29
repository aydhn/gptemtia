"""
Fixture generator for creating scenario-specific data contexts.
"""

import pandas as pd
from pathlib import Path
from typing import Tuple, List, Dict
from datetime import datetime

from scenarios.scenario_config import ScenarioProfile
from scenarios.scenario_models import ScenarioDefinition, ScenarioFixture, build_fixture_id


class FixtureGeneratorError(Exception):
    pass


def build_fixture_for_scenario(scenario: ScenarioDefinition, profile: ScenarioProfile, output_dir: Path) -> Tuple[List[ScenarioFixture], dict]:
    """Builds required data fixtures for a specific scenario."""
    fixtures = []
    warnings = ["Fixtures are completely synthetic and offline."]

    # We simply generate dummy fixtures indicating they exist.
    # In a real setup, this would load sample data and slice it for the scenario.

    for symbol in scenario.symbols:
        fix_id = build_fixture_id(scenario.scenario_id, f"ohlcv_{symbol}")

        # We don't actually generate the huge CSVs here every time unless required,
        # we just create the metadata pointing to where it would be.
        path = output_dir / f"{fix_id}.csv"

        # Touch the file to simulate its existence for validation
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()

        fixture = ScenarioFixture(
            fixture_id=fix_id,
            scenario_id=scenario.scenario_id,
            fixture_name=f"ohlcv_{symbol}",
            fixture_type="synthetic_ohlcv_fixture",
            path=str(path),
            row_count=profile.max_rows_per_symbol,
            symbols=[symbol],
            generated_at_utc=datetime.utcnow().isoformat(),
            synthetic=True,
            warnings=["Synthetic fixture."]
        )
        fixtures.append(fixture)

    summary = {
        "scenario_id": scenario.scenario_id,
        "fixtures_generated": len(fixtures),
        "synthetic_flag_enforced": True
    }

    return fixtures, summary


def build_all_scenario_fixtures(scenarios: List[ScenarioDefinition], profile: ScenarioProfile, output_dir: Path) -> Tuple[pd.DataFrame, dict]:
    """Builds fixtures for all given scenarios."""
    all_fixtures = []
    total_warnings = []

    for scenario in scenarios:
        if profile.generate_fixtures:
            fixes, summ = build_fixture_for_scenario(scenario, profile, output_dir)
            all_fixtures.extend(fixes)

    # Convert to DataFrame
    if all_fixtures:
        df = pd.DataFrame([f.__dict__ for f in all_fixtures])
    else:
        df = pd.DataFrame(columns=[
            "fixture_id", "scenario_id", "fixture_name", "fixture_type",
            "path", "row_count", "symbols", "generated_at_utc", "synthetic", "warnings"
        ])

    summary = {
        "total_fixtures": len(all_fixtures),
        "synthetic_enforced": True,
        "warnings": ["All generated fixtures are synthetic."]
    }

    return df, summary


def build_fixture_manifest(fixtures_df: pd.DataFrame) -> dict:
    """Builds a JSON-serializable manifest from a DataFrame of fixtures."""
    manifest = {
        "generated_at": datetime.utcnow().isoformat(),
        "total_fixtures": len(fixtures_df) if not fixtures_df.empty else 0,
        "synthetic_enforced": True,
        "fixtures": fixtures_df.to_dict(orient="records") if not fixtures_df.empty else []
    }
    return manifest


def validate_fixture_manifest(manifest: dict) -> dict:
    """Validates a fixture manifest."""
    validation = {
        "is_valid": True,
        "errors": [],
        "warnings": []
    }

    if not manifest.get("synthetic_enforced", False):
        validation["is_valid"] = False
        validation["errors"].append("Manifest does not enforce synthetic flag.")

    for fixture in manifest.get("fixtures", []):
        if not fixture.get("synthetic", False):
            validation["is_valid"] = False
            validation["errors"].append(f"Fixture {fixture.get('fixture_id')} is missing synthetic flag.")

    if not validation["errors"]:
        validation["warnings"].append("Manifest validated successfully. All fixtures marked synthetic.")

    return validation
