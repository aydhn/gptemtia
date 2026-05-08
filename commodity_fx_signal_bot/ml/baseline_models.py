from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, HistGradientBoostingClassifier, HistGradientBoostingRegressor
from .model_labels import MODEL_FAMILY_DUMMY, MODEL_FAMILY_LOGISTIC_REGRESSION, MODEL_FAMILY_RANDOM_FOREST, MODEL_FAMILY_HIST_GRADIENT_BOOSTING, is_classification_task

def create_dummy_model(task_type: str):
    if is_classification_task(task_type):
        return DummyClassifier(strategy="prior")
    return DummyRegressor(strategy="mean")

def create_logistic_regression_model():
    return LogisticRegression(random_state=42, max_iter=1000, n_jobs=-1)

def create_random_forest_model(task_type: str, random_state: int = 42):
    if is_classification_task(task_type):
        return RandomForestClassifier(n_estimators=100, max_depth=5, min_samples_leaf=5, random_state=random_state, n_jobs=-1)
    return RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_leaf=5, random_state=random_state, n_jobs=-1)

def create_hist_gradient_boosting_model(task_type: str, random_state: int = 42):
    if is_classification_task(task_type):
        return HistGradientBoostingClassifier(max_iter=100, max_depth=5, min_samples_leaf=5, random_state=random_state)
    return HistGradientBoostingRegressor(max_iter=100, max_depth=5, min_samples_leaf=5, random_state=random_state)

def create_baseline_model(model_family: str, task_type: str, random_state: int = 42):
    if model_family == MODEL_FAMILY_DUMMY:
        return create_dummy_model(task_type)
    elif model_family == MODEL_FAMILY_LOGISTIC_REGRESSION:
        if not is_classification_task(task_type):
            raise ValueError("Logistic regression is only supported for classification tasks.")
        return create_logistic_regression_model()
    elif model_family == MODEL_FAMILY_RANDOM_FOREST:
        return create_random_forest_model(task_type, random_state)
    elif model_family == MODEL_FAMILY_HIST_GRADIENT_BOOSTING:
        return create_hist_gradient_boosting_model(task_type, random_state)
    else:
        raise ValueError(f"Unknown model family: {model_family}")

def list_supported_baseline_models(task_type: str) -> list[str]:
    models = [MODEL_FAMILY_DUMMY, MODEL_FAMILY_RANDOM_FOREST, MODEL_FAMILY_HIST_GRADIENT_BOOSTING]
    if is_classification_task(task_type):
        models.append(MODEL_FAMILY_LOGISTIC_REGRESSION)
    return models
