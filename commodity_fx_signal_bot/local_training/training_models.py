from dataclasses import dataclass
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
