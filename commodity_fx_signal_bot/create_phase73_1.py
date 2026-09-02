import os

os.makedirs("local_training", exist_ok=True)

with open("local_training/__init__.py", "w", encoding="utf-8") as f:
    f.write('"""Local Training module."""\n')

with open("local_training/training_config.py", "w", encoding="utf-8") as f:
    f.write('''from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalTrainingProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_cloud_upload: bool = False
    allow_external_training_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    allow_certification_claim: bool = False
    allow_investment_advice_training: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_data_lake: bool = True
    scan_cross_layer_outputs: bool = True
    scan_safety_docs: bool = True
    max_lessons: int = 10000
    max_walkthrough_steps: int = 5000
    min_training_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_training": LocalTrainingProfile(
        name="balanced_local_training",
        description="Genel amaçlı local/offline knowledge-transfer, onboarding ve handover education profili.",
        language="tr",
        dry_run_default=True,
        allow_cloud_upload=False,
        allow_external_training_service=False,
        allow_external_llm=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_file_move=False,
        allow_overwrite=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_certification_claim=False,
        allow_investment_advice_training=False,
        scan_docs=True,
        scan_reports=True,
        scan_scripts=True,
        scan_tests=True,
        scan_data_lake=True,
        scan_cross_layer_outputs=True,
        scan_safety_docs=True,
        max_lessons=10000,
        max_walkthrough_steps=5000,
        min_training_quality_score=0.40,
        enabled=True,
        notes="Genel amaçlı local/offline knowledge-transfer, onboarding ve handover education profili."
    ),
    "operator_onboarding_focus": LocalTrainingProfile(
        name="operator_onboarding_focus",
        description="Operatör onboarding odaklı profil.",
        language="tr",
        dry_run_default=True,
        scan_docs=True,
        scan_reports=True,
        scan_scripts=True,
        scan_tests=False,
        scan_data_lake=True,
        scan_cross_layer_outputs=True,
        scan_safety_docs=True,
        notes="Operatör onboarding, first-week curriculum ve safe command lessons odaklı profil."
    ),
    "developer_onboarding_focus": LocalTrainingProfile(
        name="developer_onboarding_focus",
        description="Geliştirici onboarding odaklı profil.",
        language="tr",
        dry_run_default=True,
        scan_docs=True,
        scan_reports=True,
        scan_scripts=True,
        scan_tests=True,
        scan_data_lake=True,
        scan_cross_layer_outputs=True,
        scan_safety_docs=True,
        notes="Geliştirici onboarding, repo yapısı, test contract ve modül mimarisi odaklı profil."
    ),
    "strict_training_safety": LocalTrainingProfile(
        name="strict_training_safety",
        description="Strict safety training profil.",
        language="tr",
        dry_run_default=True,
        max_lessons=7000,
        max_walkthrough_steps=3000,
        min_training_quality_score=0.60,
        notes="Non-use policy, canlı/broker/deploy yasakları ve eğitim güvenlik sınırlarını sıkılaştıran profil."
    )
}

def get_local_training_profile(name: str) -> LocalTrainingProfile:
    if name not in PROFILES:
        raise ConfigError(f"Bilinmeyen profil: {name}")
    return PROFILES[name]

def list_local_training_profiles(enabled_only: bool = True) -> list[LocalTrainingProfile]:
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())

def validate_local_training_profiles() -> None:
    for name, p in PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} must have a language.")
        if p.max_lessons <= 0:
            raise ConfigError(f"Profile {name} max_lessons must be positive.")
        if p.max_walkthrough_steps <= 0:
            raise ConfigError(f"Profile {name} max_walkthrough_steps must be positive.")
        if not (0 <= p.min_training_quality_score <= 1):
            raise ConfigError(f"Profile {name} min_training_quality_score must be between 0 and 1.")
        
        # Initial profiles checks
        if name in ["balanced_local_training", "operator_onboarding_focus", "developer_onboarding_focus", "strict_training_safety"]:
            if not p.dry_run_default:
                raise ConfigError(f"Profile {name} dry_run_default must be True.")
            if any([
                p.allow_cloud_upload, p.allow_external_training_service, p.allow_external_llm,
                p.allow_file_modification, p.allow_file_deletion, p.allow_file_move, p.allow_overwrite,
                p.allow_live_commands, p.allow_broker_commands, p.allow_deploy_commands,
                p.allow_background_daemons, p.allow_real_market_download, p.allow_certification_claim,
                p.allow_investment_advice_training
            ]):
                raise ConfigError(f"Profile {name} must have all allow flags as False.")

def get_default_local_training_profile() -> LocalTrainingProfile:
    return PROFILES["balanced_local_training"]
''')

with open("local_training/training_labels.py", "w", encoding="utf-8") as f:
    f.write('''
TRAINING_DOMAIN_LABELS = [
    "operator_training",
    "analyst_training",
    "developer_training",
    "safe_usage_training",
    "non_use_policy_training",
    "command_training",
    "report_training",
    "datalake_training",
    "cross_layer_training",
    "troubleshooting_training",
    "handover_training",
    "unknown_training"
]

TRAINING_LESSON_STATUS_LABELS = [
    "lesson_ready",
    "lesson_ready_with_warnings",
    "lesson_missing",
    "lesson_blocked_by_safety",
    "lesson_needs_manual_review",
    "lesson_unknown"
]

ONBOARDING_ROLE_LABELS = [
    "operator_role",
    "analyst_role",
    "developer_role",
    "maintainer_role",
    "reviewer_role",
    "unknown_role"
]

ASSESSMENT_STATUS_LABELS = [
    "assessment_dry_run_ready",
    "assessment_needs_manual_review",
    "assessment_blocked_by_safety",
    "assessment_not_applicable",
    "assessment_unknown"
]

TRAINING_RISK_LABELS = [
    "training_critical_risk",
    "training_high_risk",
    "training_medium_risk",
    "training_low_risk",
    "training_info",
    "training_unknown_risk"
]

def list_training_domain_labels() -> list[str]: return TRAINING_DOMAIN_LABELS
def list_training_lesson_status_labels() -> list[str]: return TRAINING_LESSON_STATUS_LABELS
def list_onboarding_role_labels() -> list[str]: return ONBOARDING_ROLE_LABELS
def list_assessment_status_labels() -> list[str]: return ASSESSMENT_STATUS_LABELS
def list_training_risk_labels() -> list[str]: return TRAINING_RISK_LABELS

def validate_training_domain_label(label: str) -> None:
    if label not in TRAINING_DOMAIN_LABELS: raise ValueError(f"Invalid domain label: {label}")
def validate_training_lesson_status(label: str) -> None:
    if label not in TRAINING_LESSON_STATUS_LABELS: raise ValueError(f"Invalid lesson status: {label}")
def validate_onboarding_role(label: str) -> None:
    if label not in ONBOARDING_ROLE_LABELS: raise ValueError(f"Invalid role label: {label}")
def validate_assessment_status(label: str) -> None:
    if label not in ASSESSMENT_STATUS_LABELS: raise ValueError(f"Invalid assessment status: {label}")
def validate_training_risk(label: str) -> None:
    if label not in TRAINING_RISK_LABELS: raise ValueError(f"Invalid risk label: {label}")
''')

with open("local_training/training_models.py", "w", encoding="utf-8") as f:
    f.write('''from dataclasses import dataclass
import hashlib

@dataclass
class TrainingDomain:
    domain_id: str
    domain_name: str
    domain_label: str
    description: str
    target_roles: list[str]
    required_materials: list[str]
    warnings: list[str]

@dataclass
class OnboardingPath:
    path_id: str
    role_label: str
    path_name: str
    description: str
    modules: list[str]
    expected_outcomes: list[str]
    warnings: list[str]

@dataclass
class TrainingLesson:
    lesson_id: str
    lesson_name: str
    domain_label: str
    role_label: str
    objective: str
    steps: list[str]
    safe_commands: list[str]
    expected_outputs: list[str]
    status: str
    warnings: list[str]

@dataclass
class TrainingFAQ:
    faq_id: str
    question: str
    answer: str
    domain_label: str
    warnings: list[str]

@dataclass
class TrainingFinding:
    finding_id: str
    domain_label: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def _md5(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()

def build_training_domain_id(domain_name: str) -> str: return f"domain_{_md5(domain_name)}"
def build_onboarding_path_id(role_label: str, path_name: str) -> str: return f"path_{_md5(role_label + path_name)}"
def build_training_lesson_id(domain_label: str, lesson_name: str) -> str: return f"lesson_{_md5(domain_label + lesson_name)}"
def build_training_faq_id(question: str) -> str: return f"faq_{_md5(question)}"
def build_training_finding_id(domain_label: str, title: str) -> str: return f"finding_{_md5(domain_label + title)}"

def training_domain_to_dict(item: TrainingDomain) -> dict: return item.__dict__
def onboarding_path_to_dict(item: OnboardingPath) -> dict: return item.__dict__
def training_lesson_to_dict(item: TrainingLesson) -> dict: return item.__dict__
def training_faq_to_dict(item: TrainingFAQ) -> dict: return item.__dict__
def training_finding_to_dict(item: TrainingFinding) -> dict: return item.__dict__
''')
