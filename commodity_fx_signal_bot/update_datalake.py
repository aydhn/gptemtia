import re

file_path = "commodity_fx_signal_bot/data/storage/data_lake.py"

with open(file_path, "r") as f:
    content = f.read()

addition = """
    # ARTIFACT METADATA METHODS
    def save_research_artifact_inventory(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_INVENTORY_DIR, "research_artifact_inventory")

    def load_research_artifact_inventory(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_INVENTORY_DIR / "research_artifact_inventory.parquet")

    def save_research_artifact_metadata_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_REGISTRY_DIR, "research_artifact_metadata_registry")

    def load_research_artifact_metadata_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_REGISTRY_DIR / "research_artifact_metadata_registry.parquet")

    def save_model_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_MODEL_CARDS_DIR, "model_card_registry")

    def load_model_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_MODEL_CARDS_DIR / "model_card_registry.parquet")

    def save_dataset_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_DATASET_CARDS_DIR, "dataset_card_registry")

    def load_dataset_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_DATASET_CARDS_DIR / "dataset_card_registry.parquet")

    def save_experiment_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_EXPERIMENT_CARDS_DIR, "experiment_card_registry")

    def load_experiment_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_EXPERIMENT_CARDS_DIR / "experiment_card_registry.parquet")

    def save_reproducibility_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_REPRODUCIBILITY_CARDS_DIR, "reproducibility_card_registry")

    def load_reproducibility_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_REPRODUCIBILITY_CARDS_DIR / "reproducibility_card_registry.parquet")

    def save_backtest_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_BACKTEST_CARDS_DIR, "backtest_card_registry")

    def load_backtest_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_BACKTEST_CARDS_DIR / "backtest_card_registry.parquet")

    def save_scenario_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_SCENARIO_CARDS_DIR, "scenario_card_registry")

    def load_scenario_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_SCENARIO_CARDS_DIR / "scenario_card_registry.parquet")

    def save_regression_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_REGRESSION_CARDS_DIR, "regression_card_registry")

    def load_regression_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_REGRESSION_CARDS_DIR / "regression_card_registry.parquet")

    def save_feature_set_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_FEATURE_SET_CARDS_DIR, "feature_set_card_registry")

    def load_feature_set_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_FEATURE_SET_CARDS_DIR / "feature_set_card_registry.parquet")

    def save_synthetic_data_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_SYNTHETIC_DATA_CARDS_DIR, "synthetic_data_card_registry")

    def load_synthetic_data_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_SYNTHETIC_DATA_CARDS_DIR / "synthetic_data_card_registry.parquet")

    def save_research_report_card_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_RESEARCH_REPORT_CARDS_DIR, "research_report_card_registry")

    def load_research_report_card_registry(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_RESEARCH_REPORT_CARDS_DIR / "research_report_card_registry.parquet")

    def save_artifact_lineage_cards(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_LINEAGE_CARDS_DIR, "artifact_lineage_cards")

    def load_artifact_lineage_cards(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_LINEAGE_CARDS_DIR / "artifact_lineage_cards.parquet")

    def save_artifact_limitation_cards(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_LIMITATION_CARDS_DIR, "artifact_limitation_cards")

    def load_artifact_limitation_cards(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_LIMITATION_CARDS_DIR / "artifact_limitation_cards.parquet")

    def save_intended_use_cards(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_INTENDED_USE_CARDS_DIR, "intended_use_cards")

    def load_intended_use_cards(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_INTENDED_USE_CARDS_DIR / "intended_use_cards.parquet")

    def save_non_use_policy_cards(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_NON_USE_POLICY_CARDS_DIR, "non_use_policy_cards")

    def load_non_use_policy_cards(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_NON_USE_POLICY_CARDS_DIR / "non_use_policy_cards.parquet")

    def save_reproducibility_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_REPRODUCIBILITY_CARDS_DIR, "reproducibility_checklist")

    def load_reproducibility_checklist(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_REPRODUCIBILITY_CARDS_DIR / "reproducibility_checklist.parquet")

    def save_metadata_completeness_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_SCORING_DIR, "metadata_completeness_report")

    def load_metadata_completeness_report(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_SCORING_DIR / "metadata_completeness_report.parquet")

    def save_metadata_freshness_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_SCORING_DIR, "metadata_freshness_report")

    def load_metadata_freshness_report(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_SCORING_DIR / "metadata_freshness_report.parquet")

    def save_card_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, DATA_LAKE_ARTIFACT_METADATA_VALIDATION_DIR, "card_validation_report")

    def load_card_validation_report(self) -> pd.DataFrame:
        return self._load_parquet(DATA_LAKE_ARTIFACT_METADATA_VALIDATION_DIR / "card_validation_report.parquet")

    def save_metadata_quality(self, profile_name: str, quality: dict) -> Path:
        path = DATA_LAKE_ARTIFACT_METADATA_QUALITY_DIR / f"metadata_quality_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=4)
        return path

    def load_metadata_quality(self, profile_name: str) -> dict:
        path = DATA_LAKE_ARTIFACT_METADATA_QUALITY_DIR / f"metadata_quality_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_research_artifact_metadata_export(self, manifest: dict) -> Path:
        path = DATA_LAKE_ARTIFACT_METADATA_EXPORTS_DIR / "research_artifact_metadata_export.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=4)
        return path

    def load_research_artifact_metadata_export(self) -> dict:
        path = DATA_LAKE_ARTIFACT_METADATA_EXPORTS_DIR / "research_artifact_metadata_export.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_artifact_metadata_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        path = DATA_LAKE_ARTIFACT_METADATA_EXPORTS_DIR / f"artifact_metadata_report_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        return path

    def load_artifact_metadata_report(self, profile_name: str) -> dict:
        path = DATA_LAKE_ARTIFACT_METADATA_EXPORTS_DIR / f"artifact_metadata_report_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_artifact_metadata_reports(self) -> pd.DataFrame:
        return pd.DataFrame()
"""

imports_to_add = """from config.paths import (
    DATA_LAKE_ARTIFACT_METADATA_DIR,
    DATA_LAKE_ARTIFACT_METADATA_INVENTORY_DIR,
    DATA_LAKE_ARTIFACT_METADATA_REGISTRY_DIR,
    DATA_LAKE_ARTIFACT_METADATA_MODEL_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_DATASET_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_EXPERIMENT_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_REPRODUCIBILITY_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_BACKTEST_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_SCENARIO_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_REGRESSION_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_FEATURE_SET_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_SYNTHETIC_DATA_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_RESEARCH_REPORT_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_LINEAGE_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_LIMITATION_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_INTENDED_USE_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_NON_USE_POLICY_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_SCORING_DIR,
    DATA_LAKE_ARTIFACT_METADATA_VALIDATION_DIR,
    DATA_LAKE_ARTIFACT_METADATA_QUALITY_DIR,
    DATA_LAKE_ARTIFACT_METADATA_EXPORTS_DIR
)
"""

if "save_research_artifact_inventory" not in content:
    content = content.replace("class DataLake:", "class DataLake:\n" + addition)

if "DATA_LAKE_ARTIFACT_METADATA_DIR" not in content:
    content = content.replace("from config.paths import (", imports_to_add + "from config.paths import (")

with open(file_path, "w") as f:
    f.write(content)
