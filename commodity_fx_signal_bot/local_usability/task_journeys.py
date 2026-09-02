import pandas as pd
from .usability_config import LocalUsabilityProfile
from .usability_models import OperatorTaskJourney, build_operator_task_journey_id

def build_default_operator_task_journeys(profile: LocalUsabilityProfile) -> list[OperatorTaskJourney]:
    return [
        OperatorTaskJourney(
            journey_id=build_operator_task_journey_id("İlk kurulum sonrası güvenli kontrol"),
            journey_name="İlk kurulum sonrası güvenli kontrol",
            path_label="first_hour_path",
            steps=["README oku", "status check yap"],
            expected_outputs=["status reports"],
            manual_review_required=True,
            warnings=["Canlı operasyon prosedürü değildir."]
        )
    ]

def build_operator_task_journey_registry(profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_operator_task_journeys(profile)
    df = pd.DataFrame([i.__dict__ for i in items])
    return df, {"total_journeys": len(items)}

def summarize_operator_task_journeys(journey_df: pd.DataFrame) -> dict:
    return {"total": len(journey_df)}
