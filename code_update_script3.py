import os

def update_file(filename, search_pattern, replace_text):
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return
    with open(filename, "r") as f:
        content = f.read()

    new_content = content.replace(search_pattern, replace_text)

    if new_content != content:
        with open(filename, "w") as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes made to {filename}")

update_file("commodity_fx_signal_bot/config/paths.py",
"""LAKE_ML_METADATA_DIR = LAKE_ML_DIR / "metadata"
LAKE_ML_QUALITY_DIR = LAKE_ML_DIR / "quality"
""",
"""LAKE_ML_METADATA_DIR = LAKE_ML_DIR / "metadata"
LAKE_ML_QUALITY_DIR = LAKE_ML_DIR / "quality"

# ML Training Directories
LAKE_ML_MODELS_DIR = LAKE_ML_DIR / "models"
LAKE_ML_MODEL_ARTIFACTS_DIR = LAKE_ML_DIR / "model_artifacts"
LAKE_ML_MODEL_REGISTRY_DIR = LAKE_ML_DIR / "model_registry"
LAKE_ML_MODEL_EVALUATIONS_DIR = LAKE_ML_DIR / "model_evaluations"
LAKE_ML_MODEL_CV_DIR = LAKE_ML_DIR / "model_cv"
LAKE_ML_MODEL_QUALITY_DIR = LAKE_ML_DIR / "model_quality"

REPORTS_ML_TRAINING_REPORTS_DIR = REPORTS_DIR / "ml_training_reports"
""")

update_file("commodity_fx_signal_bot/config/paths.py",
"""        LAKE_ML_SPLITS_DIR,
        LAKE_ML_METADATA_DIR,
        LAKE_ML_QUALITY_DIR,
    ]""",
"""        LAKE_ML_SPLITS_DIR,
        LAKE_ML_METADATA_DIR,
        LAKE_ML_QUALITY_DIR,
        LAKE_ML_MODELS_DIR,
        LAKE_ML_MODEL_ARTIFACTS_DIR,
        LAKE_ML_MODEL_REGISTRY_DIR,
        LAKE_ML_MODEL_EVALUATIONS_DIR,
        LAKE_ML_MODEL_CV_DIR,
        LAKE_ML_MODEL_QUALITY_DIR,
        REPORTS_ML_TRAINING_REPORTS_DIR,
    ]""")

update_file("commodity_fx_signal_bot/config/paths.py",
"""        self.ml_metadata = LAKE_ML_METADATA_DIR
        self.ml_quality = LAKE_ML_QUALITY_DIR""",
"""        self.ml_metadata = LAKE_ML_METADATA_DIR
        self.ml_quality = LAKE_ML_QUALITY_DIR
        self.ml_models = LAKE_ML_MODELS_DIR
        self.ml_model_artifacts = LAKE_ML_MODEL_ARTIFACTS_DIR
        self.ml_model_registry = LAKE_ML_MODEL_REGISTRY_DIR
        self.ml_model_evaluations = LAKE_ML_MODEL_EVALUATIONS_DIR
        self.ml_model_cv = LAKE_ML_MODEL_CV_DIR
        self.ml_model_quality = LAKE_ML_MODEL_QUALITY_DIR
        self.ml_training_reports = REPORTS_ML_TRAINING_REPORTS_DIR""")
