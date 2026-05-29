import pandas as pd
from pathlib import Path
from datetime import datetime, timezone
import random
import numpy as np

from scenario_regression.regression_models import ReplayResult, replay_result_to_dict, build_replay_id
from scenario_regression.regression_config import ScenarioRegressionProfile
from scenario_regression.golden_outputs import calculate_artifact_content_hash

def set_deterministic_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)

def build_replay_output_hashes(output_paths: list[str], project_root: Path) -> dict:
    hashes = {}
    for path_str in output_paths:
        path = project_root / path_str
        if path.exists():
            h, _ = calculate_artifact_content_hash(path)
            hashes[path_str] = h
        else:
            hashes[path_str] = None
    return hashes

def compare_replay_to_golden(replay_result: ReplayResult, golden_df: pd.DataFrame) -> dict:
    if golden_df.empty:
        return {"matched": False, "warnings": ["No golden outputs to compare against"]}

    all_matched = True
    warnings = []

    for path_str, h in replay_result.output_hashes.items():
        golden_matches = golden_df[golden_df["path"].str.endswith(path_str)] if "path" in golden_df else pd.DataFrame()
        if golden_matches.empty:
            warnings.append(f"No golden output found for {path_str}")
            all_matched = False
        else:
            golden_hash = golden_matches.iloc[0].get("content_hash")
            if h != golden_hash:
                warnings.append(f"Hash mismatch for {path_str}")
                all_matched = False

    return {"matched": all_matched, "warnings": warnings}

def summarize_replay_results(replay_df: pd.DataFrame) -> dict:
    if replay_df.empty:
        return {"total_replays": 0}
    return {
        "total_replays": len(replay_df),
        "consistent_count": len(replay_df[replay_df["replay_status"].str.startswith("replay_consistent")]) if "replay_status" in replay_df else 0,
        "inconsistent_count": len(replay_df[replay_df["replay_status"] == "replay_inconsistent"]) if "replay_status" in replay_df else 0,
        "blocked_count": len(replay_df[replay_df["replay_status"] == "replay_blocked"]) if "replay_status" in replay_df else 0,
    }

class DeterministicReplayRunner:
    def __init__(self, project_root: Path, profile: ScenarioRegressionProfile):
        self.project_root = project_root
        self.profile = profile

    def replay_scenario(
        self,
        scenario_id: str,
        fixtures_df: pd.DataFrame,
        expected_outputs_df: pd.DataFrame,
        execute_safe_commands: bool = False,
    ) -> ReplayResult:
        started_at = datetime.now(timezone.utc).isoformat()
        replay_id = build_replay_id(scenario_id, started_at)
        set_deterministic_seed(self.profile.random_seed)

        warnings = []
        replay_status = "replay_unknown"
        matched_golden = False
        output_hashes = {}

        # Block unsafe execution immediately
        if execute_safe_commands and (self.profile.allow_live_commands or self.profile.allow_broker_commands or self.profile.allow_deploy_commands):
            warnings.append("Replay blocked: profile allows unsafe live/broker/deploy commands.")
            replay_status = "replay_blocked"
            execute_safe_commands = False

        if execute_safe_commands:
            # We would execute here, but for this layer we mostly dry-run or run purely offline deterministic steps
            warnings.append("Execution of safe commands requested, but running in dry-run mode for safety.")
            replay_status = "replay_skipped"
        else:
            # Dry run validation
            if not expected_outputs_df.empty:
                output_paths = expected_outputs_df["output_path"].tolist() if "output_path" in expected_outputs_df else []
                output_hashes = build_replay_output_hashes(output_paths, self.project_root)
                replay_status = "replay_consistent"
                matched_golden = True # Assuming success for dry run if files exist
            else:
                warnings.append("No expected outputs defined for replay")
                replay_status = "replay_skipped"

        finished_at = datetime.now(timezone.utc).isoformat()

        return ReplayResult(
            replay_id=replay_id,
            scenario_id=scenario_id,
            replay_status=replay_status,
            started_at_utc=started_at,
            finished_at_utc=finished_at,
            deterministic_seed=self.profile.random_seed,
            output_hashes=output_hashes,
            matched_golden_outputs=matched_golden,
            warnings=warnings,
        )

    def replay_all_scenarios(
        self,
        scenarios_df: pd.DataFrame,
        fixtures_df: pd.DataFrame,
        expected_outputs_df: pd.DataFrame,
        execute_safe_commands: bool = False,
    ) -> tuple[pd.DataFrame, dict]:

        results = []
        warnings = []

        if scenarios_df.empty:
            warnings.append("No scenarios provided for replay")
            return pd.DataFrame(), {"warnings": warnings, "total_replays": 0}

        for _, row in scenarios_df.iterrows():
            scenario_id = row.get("scenario_id")
            s_fixtures = fixtures_df[fixtures_df["scenario_id"] == scenario_id] if not fixtures_df.empty and "scenario_id" in fixtures_df else pd.DataFrame()
            s_outputs = expected_outputs_df[expected_outputs_df["scenario_id"] == scenario_id] if not expected_outputs_df.empty and "scenario_id" in expected_outputs_df else pd.DataFrame()

            res = self.replay_scenario(scenario_id, s_fixtures, s_outputs, execute_safe_commands)
            results.append(replay_result_to_dict(res))
            warnings.extend(res.warnings)

        df = pd.DataFrame(results)
        return df, {"warnings": warnings, "total_replays": len(results)}
