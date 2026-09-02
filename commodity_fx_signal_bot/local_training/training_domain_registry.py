import pandas as pd
from .training_config import LocalTrainingProfile
from .training_models import TrainingDomain, build_training_domain_id, training_domain_to_dict

def build_default_training_domains(profile: LocalTrainingProfile) -> list[TrainingDomain]:
    return [
        TrainingDomain(
            domain_id=build_training_domain_id("operator_training"),
            domain_name="operator_training",
            domain_label="operator_training",
            description="Operator training for local/offline usage",
            target_roles=["operator_role"],
            required_materials=["OPERATOR_MANUAL.md", "SAFE_USAGE_GUIDE.md"],
            warnings=["Bu domain resmi eğitim kapsamı değildir.", "Canlı işlem yetkisi vermez."]
        ),
        TrainingDomain(
            domain_id=build_training_domain_id("analyst_training"),
            domain_name="analyst_training",
            domain_label="analyst_training",
            description="Analyst training for local research",
            target_roles=["analyst_role"],
            required_materials=["ANALYST_HANDBOOK.md"],
            warnings=["Bu domain resmi eğitim kapsamı değildir.", "Yatırım tavsiyesi vermez."]
        ),
        TrainingDomain(
            domain_id=build_training_domain_id("developer_training"),
            domain_name="developer_training",
            domain_label="developer_training",
            description="Developer training for project maintenance",
            target_roles=["developer_role", "maintainer_role"],
            required_materials=["ARCHITECTURE.md", "README.md"],
            warnings=["Bu domain resmi eğitim kapsamı değildir."]
        ),
        TrainingDomain(
            domain_id=build_training_domain_id("safe_usage_training"),
            domain_name="safe_usage_training",
            domain_label="safe_usage_training",
            description="Safe usage guidelines for offline tool",
            target_roles=["operator_role", "analyst_role", "developer_role"],
            required_materials=["SAFE_USAGE_GUIDE.md"],
            warnings=["Bu domain resmi eğitim kapsamı değildir."]
        ),
        TrainingDomain(
            domain_id=build_training_domain_id("non_use_policy_training"),
            domain_name="non_use_policy_training",
            domain_label="non_use_policy_training",
            description="Non-use policy covering forbidden actions",
            target_roles=["operator_role", "analyst_role", "developer_role"],
            required_materials=["SAFE_USAGE_GUIDE.md"],
            warnings=["Bu domain resmi eğitim kapsamı değildir."]
        )
    ]

def build_training_domain_registry(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_training_domains(profile)
    df = pd.DataFrame([training_domain_to_dict(d) for d in domains])
    return df, summarize_training_domains(df)

def summarize_training_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df is None or domain_df.empty:
        return {"total_domains": 0}
    return {
        "total_domains": len(domain_df),
        "domain_labels": domain_df["domain_label"].tolist()
    }
