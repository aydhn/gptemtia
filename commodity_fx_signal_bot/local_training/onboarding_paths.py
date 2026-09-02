import pandas as pd
from .training_config import LocalTrainingProfile
from .training_models import OnboardingPath, build_onboarding_path_id, onboarding_path_to_dict

def build_operator_onboarding_path(profile: LocalTrainingProfile) -> OnboardingPath:
    return OnboardingPath(
        path_id=build_onboarding_path_id("operator_role", "Operator Path"),
        role_label="operator_role",
        path_name="Operator Path",
        description="Onboarding path for operators",
        modules=["güvenli kullanım", "kurulum okuma", "status komutları", "rapor okuma", "DataLake klasörleri", "no-go/safe-go sınırları", "DR/maintenance/archive statüleri"],
        expected_outcomes=["Can read reports", "Can run status commands"],
        warnings=["Onboarding path production authorization değildir.", "Finansal tavsiye eğitimi üretmez.", "Broker/live/deploy yok."]
    )

def build_analyst_onboarding_path(profile: LocalTrainingProfile) -> OnboardingPath:
    return OnboardingPath(
        path_id=build_onboarding_path_id("analyst_role", "Analyst Path"),
        role_label="analyst_role",
        path_name="Analyst Path",
        description="Onboarding path for analysts",
        modules=["araştırma raporları", "backtest/paper sınırları", "evidence/metadata cards", "scenario/regression outputs", "non-use policy", "yatırım tavsiyesi olmayan yorumlama"],
        expected_outcomes=["Can interpret research", "Understands limitations"],
        warnings=["Onboarding path production authorization değildir.", "Finansal tavsiye eğitimi üretmez.", "Broker/live/deploy yok."]
    )

def build_developer_onboarding_path(profile: LocalTrainingProfile) -> OnboardingPath:
    return OnboardingPath(
        path_id=build_onboarding_path_id("developer_role", "Developer Path"),
        role_label="developer_role",
        path_name="Developer Path",
        description="Onboarding path for developers",
        modules=["repo mimarisi", "scripts contract", "tests", "DataLake save/load", "local graph/timeline/consistency/readiness/maintenance/archive/DR modules", "safety boundaries"],
        expected_outcomes=["Can extend project locally"],
        warnings=["Onboarding path production authorization değildir.", "Broker/live/deploy yok."]
    )

def build_maintainer_onboarding_path(profile: LocalTrainingProfile) -> OnboardingPath:
    return OnboardingPath(
        path_id=build_onboarding_path_id("maintainer_role", "Maintainer Path"),
        role_label="maintainer_role",
        path_name="Maintainer Path",
        description="Onboarding path for maintainers",
        modules=["repo mimarisi", "safety boundaries", "maintenance outputs"],
        expected_outcomes=["Can review and maintain project locally"],
        warnings=["Onboarding path production authorization değildir."]
    )

def build_role_based_onboarding_paths(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    paths = [
        build_operator_onboarding_path(profile),
        build_analyst_onboarding_path(profile),
        build_developer_onboarding_path(profile),
        build_maintainer_onboarding_path(profile)
    ]
    df = pd.DataFrame([onboarding_path_to_dict(p) for p in paths])
    return df, summarize_onboarding_paths(df)

def summarize_onboarding_paths(path_df: pd.DataFrame) -> dict:
    if path_df is None or path_df.empty: return {"total_paths": 0}
    return {"total_paths": len(path_df), "roles": path_df["role_label"].tolist()}
