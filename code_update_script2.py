import os

def append_to_file(filename, text):
    with open(filename, "a") as f:
        f.write(text)

append_to_file("commodity_fx_signal_bot/.env.example", """
# Phase 30: ML Training Baseline
ML_TRAINING_ENABLED=true
ML_BASELINE_MODELS_ENABLED=true
ML_MODEL_REGISTRY_ENABLED=true
DEFAULT_ML_TRAINING_PROFILE=balanced_baseline_training
DEFAULT_ML_TRAINING_TIMEFRAME=1d
DEFAULT_ML_TRAINING_DATASET_PROFILE=balanced_supervised_dataset
DEFAULT_ML_TARGET_COLUMN=target_direction_class_5
ML_TRAINING_TASK_TYPE=classification
ML_ALLOWED_MODEL_FAMILIES=dummy,logistic_regression,random_forest,hist_gradient_boosting
ML_DEFAULT_MODEL_FAMILY=random_forest
ML_CV_N_SPLITS=5
ML_CV_EMBARGO_BARS=5
ML_MIN_TRAIN_ROWS=300
ML_MIN_TEST_ROWS=50
ML_MAX_FEATURE_NAN_RATIO_FOR_TRAINING=0.35
ML_DROP_HIGH_NAN_FEATURES=true
ML_ENABLE_BASIC_IMPUTATION=true
ML_ENABLE_BASIC_SCALING=true
ML_SAVE_MODEL_ARTIFACTS=true
ML_SAVE_MODEL_REGISTRY_ENTRIES=true
ML_SAVE_MODEL_EVALUATION_REPORTS=true
""")
