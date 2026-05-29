import pandas as pd
from pathlib import Path
from typing import Optional
from scenario_regression.regression_models import ScenarioRegressionDefinition, scenario_regression_definition_to_dict
from scenario_regression.regression_config import ScenarioRegressionProfile

class ScenarioRegressionRegistry:
    def __init__(self, registry_dir: Path):
        self.registry_dir = registry_dir
        self.registry_dir.mkdir(parents=True, exist_ok=True)
        self.registry_file = self.registry_dir / "regression_registry.csv"

    def add_regression_definition(self, definition: ScenarioRegressionDefinition) -> Path:
        df = self.load_regression_definitions()
        row = scenario_regression_definition_to_dict(definition)
        if not df.empty and definition.regression_id in df["regression_id"].values:
            df.loc[df["regression_id"] == definition.regression_id] = pd.Series(row)
        else:
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        df.to_csv(self.registry_file, index=False)
        return self.registry_file

    def load_regression_definitions(self) -> pd.DataFrame:
        if self.registry_file.exists():
            return pd.read_csv(self.registry_file)
        return pd.DataFrame()

    def get_regression_definition(self, regression_id: str) -> Optional[dict]:
        df = self.load_regression_definitions()
        if not df.empty and regression_id in df["regression_id"].values:
            return df[df["regression_id"] == regression_id].iloc[0].to_dict()
        return None

    def list_by_scenario(self, scenario_id: str) -> pd.DataFrame:
        df = self.load_regression_definitions()
        if not df.empty:
            return df[df["scenario_id"] == scenario_id]
        return df

    def list_by_type(self, regression_type: str) -> pd.DataFrame:
        df = self.load_regression_definitions()
        if not df.empty:
            return df[df["regression_type"] == regression_type]
        return df

    def summarize(self) -> dict:
        df = self.load_regression_definitions()
        if df.empty:
            return {"total_definitions": 0}
        return {
            "total_definitions": len(df),
            "by_type": df["regression_type"].value_counts().to_dict() if "regression_type" in df else {},
            "by_scenario": df["scenario_id"].value_counts().to_dict() if "scenario_id" in df else {},
        }

def build_default_regression_definitions(scenarios_df: pd.DataFrame, profile: ScenarioRegressionProfile) -> list[ScenarioRegressionDefinition]:
    from scenario_regression.regression_models import build_regression_id
    from scenario_regression.regression_labels import list_regression_type_labels

    definitions = []
    if scenarios_df.empty:
        return definitions

    types = [
        "golden_output_regression",
        "snapshot_regression",
        "deterministic_replay_regression",
        "fixture_reproducibility_regression",
        "output_contract_regression",
        "demo_workflow_regression",
        "end_to_end_acceptance_regression"
    ]

    for _, row in scenarios_df.iterrows():
        scenario_id = row.get("scenario_id", "unknown")
        for t in types:
            reg_id = build_regression_id(scenario_id, t)
            definitions.append(
                ScenarioRegressionDefinition(
                    regression_id=reg_id,
                    scenario_id=scenario_id,
                    regression_type=t,
                    name=f"{scenario_id} {t}",
                    description=f"Auto-generated definition for {scenario_id} ({t})",
                    expected_outputs=[],
                    golden_output_ids=[],
                    snapshot_ids=[],
                    required=True,
                    warnings=[],
                )
            )
    return definitions

def regression_definitions_to_dataframe(definitions: list[ScenarioRegressionDefinition]) -> pd.DataFrame:
    if not definitions:
        return pd.DataFrame()
    return pd.DataFrame([scenario_regression_definition_to_dict(d) for d in definitions])
