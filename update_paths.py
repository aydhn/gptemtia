import re

with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

ml_paths_code = """
# Phase 29: ML Dataset Preparation
LAKE_ML_DIR = LAKE_DIR / "ml"
LAKE_ML_FEATURES_DIR = LAKE_ML_DIR / "features"
LAKE_ML_TARGETS_DIR = LAKE_ML_DIR / "targets"
LAKE_ML_DATASETS_DIR = LAKE_ML_DIR / "datasets"
LAKE_ML_SPLITS_DIR = LAKE_ML_DIR / "splits"
LAKE_ML_METADATA_DIR = LAKE_ML_DIR / "metadata"
LAKE_ML_QUALITY_DIR = LAKE_ML_DIR / "quality"
REPORTS_ML_REPORTS_DIR = REPORTS_DIR / "ml_reports"

def ensure_project_directories() -> None:
"""

content = content.replace("def ensure_project_directories() -> None:", ml_paths_code)

ensure_paths_add = """        LAKE_DIR / "backtests" / "audits",
        REPORTS_DIR / "backtest_reports",
        LAKE_ML_DIR,
        LAKE_ML_FEATURES_DIR,
        LAKE_ML_TARGETS_DIR,
        LAKE_ML_DATASETS_DIR,
        LAKE_ML_SPLITS_DIR,
        LAKE_ML_METADATA_DIR,
        LAKE_ML_QUALITY_DIR,
        REPORTS_ML_REPORTS_DIR,
    ]"""

content = content.replace("""        LAKE_DIR / "backtests" / "audits",
        REPORTS_DIR / "backtest_reports",
    ]""", ensure_paths_add)

project_paths_add = """        self.backtest_audits = self.backtests / "audits"
        self.backtest_reports = REPORTS_DIR / "backtest_reports"
        self.ml_dir = LAKE_ML_DIR
        self.ml_features = LAKE_ML_FEATURES_DIR
        self.ml_targets = LAKE_ML_TARGETS_DIR
        self.ml_datasets = LAKE_ML_DATASETS_DIR
        self.ml_splits = LAKE_ML_SPLITS_DIR
        self.ml_metadata = LAKE_ML_METADATA_DIR
        self.ml_quality = LAKE_ML_QUALITY_DIR
        self.ml_reports = REPORTS_ML_REPORTS_DIR"""

content = content.replace("""        self.backtest_audits = self.backtests / "audits"
        self.backtest_reports = REPORTS_DIR / "backtest_reports\"""", project_paths_add)


with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
    f.write(content)
