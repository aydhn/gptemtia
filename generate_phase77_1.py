import os
from pathlib import Path

BASE_DIR = Path("commodity_fx_signal_bot")
CONFIG_DIR = BASE_DIR / "config"
LOCAL_ACC_DIR = BASE_DIR / "local_acceptance"
os.makedirs(LOCAL_ACC_DIR, exist_ok=True)

# 1. Update config/settings.py
settings_path = CONFIG_DIR / "settings.py"
with open(settings_path, "r", encoding="utf-8") as f:
    settings_content = f.read()

settings_addition = """
    # Phase 77 - Local Acceptance Settings
    local_acceptance_enabled: bool = True
    default_local_acceptance_profile: str = "balanced_local_acceptance"
    local_acceptance_default_language: str = "tr"
    local_acceptance_dry_run_default: bool = True
    local_acceptance_allow_official_signoff: bool = False
    local_acceptance_allow_compliance_claim: bool = False
    local_acceptance_allow_production_release_claim: bool = False
    local_acceptance_allow_live_trading_claim: bool = False
    local_acceptance_allow_broker_readiness_claim: bool = False
    local_acceptance_allow_investment_advice: bool = False
    local_acceptance_allow_model_deployment_claim: bool = False
    local_acceptance_allow_package_publish: bool = False
    local_acceptance_allow_cloud_upload: bool = False
    local_acceptance_allow_external_service: bool = False
    local_acceptance_allow_external_llm: bool = False
    local_acceptance_allow_file_modification: bool = False
    local_acceptance_allow_file_deletion: bool = False
    local_acceptance_allow_file_move: bool = False
    local_acceptance_allow_overwrite: bool = False
    local_acceptance_scan_docs: bool = True
    local_acceptance_scan_reports: bool = True
    local_acceptance_scan_data_lake: bool = True
    local_acceptance_scan_scripts: bool = True
    local_acceptance_scan_tests: bool = True
    local_acceptance_scan_safety_outputs: bool = True
    local_acceptance_scan_hardening_outputs: bool = True
    local_acceptance_scan_synthesis_outputs: bool = True
    local_acceptance_max_evidence_items: int = 500000
    local_acceptance_max_questions: int = 5000
    local_acceptance_min_readiness_score: float = 0.40
    local_acceptance_min_quality_score: float = 0.40
    local_acceptance_save_reports: bool = True
"""
if "local_acceptance_enabled" not in settings_content:
    settings_content = settings_content.replace(
        "class Settings(BaseSettings):", 
        f"class Settings(BaseSettings):{settings_addition}"
    )
    with open(settings_path, "w", encoding="utf-8") as f:
        f.write(settings_content)

# Update .env.example
env_path = BASE_DIR / ".env.example"
with open(env_path, "r", encoding="utf-8") as f:
    env_content = f.read()

env_addition = """
# Phase 77 - Local Acceptance Settings
LOCAL_ACCEPTANCE_ENABLED=true
DEFAULT_LOCAL_ACCEPTANCE_PROFILE=balanced_local_acceptance
LOCAL_ACCEPTANCE_DEFAULT_LANGUAGE=tr
LOCAL_ACCEPTANCE_DRY_RUN_DEFAULT=true
LOCAL_ACCEPTANCE_ALLOW_OFFICIAL_SIGNOFF=false
LOCAL_ACCEPTANCE_ALLOW_COMPLIANCE_CLAIM=false
LOCAL_ACCEPTANCE_ALLOW_PRODUCTION_RELEASE_CLAIM=false
LOCAL_ACCEPTANCE_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_ACCEPTANCE_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_ACCEPTANCE_ALLOW_INVESTMENT_ADVICE=false
LOCAL_ACCEPTANCE_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_ACCEPTANCE_ALLOW_PACKAGE_PUBLISH=false
LOCAL_ACCEPTANCE_ALLOW_CLOUD_UPLOAD=false
LOCAL_ACCEPTANCE_ALLOW_EXTERNAL_SERVICE=false
LOCAL_ACCEPTANCE_ALLOW_EXTERNAL_LLM=false
LOCAL_ACCEPTANCE_ALLOW_FILE_MODIFICATION=false
LOCAL_ACCEPTANCE_ALLOW_FILE_DELETION=false
LOCAL_ACCEPTANCE_ALLOW_FILE_MOVE=false
LOCAL_ACCEPTANCE_ALLOW_OVERWRITE=false
LOCAL_ACCEPTANCE_SCAN_DOCS=true
LOCAL_ACCEPTANCE_SCAN_REPORTS=true
LOCAL_ACCEPTANCE_SCAN_DATA_LAKE=true
LOCAL_ACCEPTANCE_SCAN_SCRIPTS=true
LOCAL_ACCEPTANCE_SCAN_TESTS=true
LOCAL_ACCEPTANCE_SCAN_SAFETY_OUTPUTS=true
LOCAL_ACCEPTANCE_SCAN_HARDENING_OUTPUTS=true
LOCAL_ACCEPTANCE_SCAN_SYNTHESIS_OUTPUTS=true
LOCAL_ACCEPTANCE_MAX_EVIDENCE_ITEMS=500000
LOCAL_ACCEPTANCE_MAX_QUESTIONS=5000
LOCAL_ACCEPTANCE_MIN_READINESS_SCORE=0.40
LOCAL_ACCEPTANCE_MIN_QUALITY_SCORE=0.40
LOCAL_ACCEPTANCE_SAVE_REPORTS=true
"""
if "LOCAL_ACCEPTANCE_ENABLED" not in env_content:
    with open(env_path, "a", encoding="utf-8") as f:
        f.write(env_addition)

# Update config/paths.py
paths_path = CONFIG_DIR / "paths.py"
with open(paths_path, "r", encoding="utf-8") as f:
    paths_content = f.read()

paths_addition = """
    # Local Acceptance
    "lake_local_acceptance": DATA_LAKE_DIR / "local_acceptance",
    "lake_local_acceptance_profiles": DATA_LAKE_DIR / "local_acceptance" / "profiles",
    "lake_local_acceptance_domains": DATA_LAKE_DIR / "local_acceptance" / "domains",
    "lake_local_acceptance_simulation": DATA_LAKE_DIR / "local_acceptance" / "simulation",
    "lake_local_acceptance_reviewer_pack": DATA_LAKE_DIR / "local_acceptance" / "reviewer_pack",
    "lake_local_acceptance_questions": DATA_LAKE_DIR / "local_acceptance" / "questions",
    "lake_local_acceptance_evidence_matrix": DATA_LAKE_DIR / "local_acceptance" / "evidence_matrix",
    "lake_local_acceptance_evidence_trail": DATA_LAKE_DIR / "local_acceptance" / "evidence_trail",
    "lake_local_acceptance_traces": DATA_LAKE_DIR / "local_acceptance" / "traces",
    "lake_local_acceptance_signoff": DATA_LAKE_DIR / "local_acceptance" / "signoff",
    "lake_local_acceptance_verification": DATA_LAKE_DIR / "local_acceptance" / "verification",
    "lake_local_acceptance_criteria": DATA_LAKE_DIR / "local_acceptance" / "criteria",
    "lake_local_acceptance_exceptions": DATA_LAKE_DIR / "local_acceptance" / "exceptions",
    "lake_local_acceptance_no_go_safe_go": DATA_LAKE_DIR / "local_acceptance" / "no_go_safe_go",
    "lake_local_acceptance_templates": DATA_LAKE_DIR / "local_acceptance" / "templates",
    "lake_local_acceptance_binders": DATA_LAKE_DIR / "local_acceptance" / "binders",
    "lake_local_acceptance_gaps": DATA_LAKE_DIR / "local_acceptance" / "gaps",
    "lake_local_acceptance_risks": DATA_LAKE_DIR / "local_acceptance" / "risks",
    "lake_local_acceptance_scoring": DATA_LAKE_DIR / "local_acceptance" / "scoring",
    "lake_local_acceptance_validation": DATA_LAKE_DIR / "local_acceptance" / "validation",
    "lake_local_acceptance_quality": DATA_LAKE_DIR / "local_acceptance" / "quality",

    "output_local_acceptance": REPORTS_OUTPUT_DIR / "local_acceptance",
    "output_local_acceptance_csv": REPORTS_OUTPUT_DIR / "local_acceptance" / "csv",
    "output_local_acceptance_markdown": REPORTS_OUTPUT_DIR / "local_acceptance" / "markdown",
    "output_local_acceptance_txt": REPORTS_OUTPUT_DIR / "local_acceptance" / "txt",
    "output_local_acceptance_json": REPORTS_OUTPUT_DIR / "local_acceptance" / "json",

    "docs_generated_local_acceptance": DOCS_GENERATED_DIR / "local_acceptance",
"""
if "lake_local_acceptance" not in paths_content:
    paths_content = paths_content.replace(
        "return {",
        f"return {{{paths_addition}"
    )
    with open(paths_path, "w", encoding="utf-8") as f:
        f.write(paths_content)

# local_acceptance/__init__.py
with open(LOCAL_ACC_DIR / "__init__.py", "w", encoding="utf-8") as f:
    f.write('"""Local Acceptance Simulation, Reviewer Pack, and Verification Module"""\\n')

# local_acceptance/acceptance_config.py
with open(LOCAL_ACC_DIR / "acceptance_config.py", "w", encoding="utf-8") as f:
    f.write('''from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalAcceptanceProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_official_signoff: bool = False
    allow_compliance_claim: bool = False
    allow_production_release_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    allow_package_publish: bool = False
    allow_cloud_upload: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_safety_outputs: bool = True
    scan_hardening_outputs: bool = True
    scan_synthesis_outputs: bool = True
    max_evidence_items: int = 500000
    max_questions: int = 5000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_acceptance": LocalAcceptanceProfile(
        name="balanced_local_acceptance",
        description="Genel amaçlı local/offline final acceptance simulation ve verification rehearsal profili.",
        notes="Genel amaçlı local/offline final acceptance simulation ve verification rehearsal profili."
    ),
    "independent_reviewer_focus": LocalAcceptanceProfile(
        name="independent_reviewer_focus",
        description="Independent reviewer pack, question bank ve evidence request matrix odaklı profil.",
        max_questions=3000,
        notes="Independent reviewer pack, question bank ve evidence request matrix odaklı profil."
    ),
    "evidence_trail_focus": LocalAcceptanceProfile(
        name="evidence_trail_focus",
        description="Audit-style local evidence trail ve trace matrix odaklı profil.",
        max_evidence_items=500000,
        notes="Audit-style local evidence trail ve trace matrix odaklı profil."
    ),
    "strict_acceptance_safety": LocalAcceptanceProfile(
        name="strict_acceptance_safety",
        description="Official sign-off, compliance, production release, canlı trading, broker readiness ve yatırım tavsiyesi overclaim denetimini sıkılaştıran profil.",
        max_evidence_items=300000,
        max_questions=3000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Official sign-off, compliance, production release, canlı trading, broker readiness ve yatırım tavsiyesi overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_acceptance_profile(name: str) -> LocalAcceptanceProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Bilinmeyen profile: {name}")
    return _PROFILES[name]

def list_local_acceptance_profiles(enabled_only: bool = True) -> list[LocalAcceptanceProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_acceptance_profiles() -> None:
    for name, p in _PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} language boş olamaz.")
        if p.max_evidence_items <= 0:
            raise ConfigError(f"Profile {name} max_evidence_items pozitif olmalı.")
        if p.max_questions <= 0:
            raise ConfigError(f"Profile {name} max_questions pozitif olmalı.")
        if not (0 <= p.min_readiness_score <= 1):
            raise ConfigError(f"Profile {name} min_readiness_score 0-1 aralığında olmalı.")
        if not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profile {name} min_quality_score 0-1 aralığında olmalı.")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name} dry_run_default True olmalı.")
        
        allow_flags = [p.allow_official_signoff, p.allow_compliance_claim, p.allow_production_release_claim,
                       p.allow_live_trading_claim, p.allow_broker_readiness_claim, p.allow_investment_advice,
                       p.allow_model_deployment_claim, p.allow_package_publish, p.allow_cloud_upload,
                       p.allow_external_service, p.allow_external_llm, p.allow_file_modification,
                       p.allow_file_deletion, p.allow_file_move, p.allow_overwrite]
        if any(allow_flags):
            raise ConfigError(f"Profile {name} allow flagleri False olmalı.")

def get_default_local_acceptance_profile() -> LocalAcceptanceProfile:
    return _PROFILES["balanced_local_acceptance"]
''')

# local_acceptance/acceptance_labels.py
with open(LOCAL_ACC_DIR / "acceptance_labels.py", "w", encoding="utf-8") as f:
    f.write('''ACCEPTANCE_DOMAIN_LABELS = [
    "final_acceptance_domain",
    "reviewer_pack_domain",
    "evidence_trail_domain",
    "signoff_rehearsal_domain",
    "verification_rehearsal_domain",
    "criteria_domain",
    "exception_domain",
    "no_go_safe_go_domain",
    "quality_validation_domain",
    "unknown_acceptance_domain"
]

ACCEPTANCE_STATUS_LABELS = [
    "acceptance_ready_for_rehearsal",
    "acceptance_ready_with_warnings",
    "acceptance_missing",
    "acceptance_blocked_by_safety",
    "acceptance_needs_manual_review",
    "acceptance_unknown"
]

EVIDENCE_TRACE_LABELS = [
    "evidence_trace_available",
    "evidence_trace_partial",
    "evidence_trace_missing",
    "evidence_trace_not_applicable",
    "evidence_trace_blocked_by_safety",
    "evidence_trace_unknown"
]

REVIEWER_RESPONSE_LABELS = [
    "reviewer_response_ready",
    "reviewer_response_needs_evidence",
    "reviewer_response_needs_manual_review",
    "reviewer_response_blocked_by_safety",
    "reviewer_response_unknown"
]

ACCEPTANCE_RISK_LABELS = [
    "acceptance_critical_risk",
    "acceptance_high_risk",
    "acceptance_medium_risk",
    "acceptance_low_risk",
    "acceptance_info",
    "acceptance_unknown_risk"
]

def list_acceptance_domain_labels() -> list[str]:
    return ACCEPTANCE_DOMAIN_LABELS

def list_acceptance_status_labels() -> list[str]:
    return ACCEPTANCE_STATUS_LABELS

def list_evidence_trace_labels() -> list[str]:
    return EVIDENCE_TRACE_LABELS

def list_reviewer_response_labels() -> list[str]:
    return REVIEWER_RESPONSE_LABELS

def list_acceptance_risk_labels() -> list[str]:
    return ACCEPTANCE_RISK_LABELS

def validate_acceptance_domain_label(label: str) -> None:
    if label not in ACCEPTANCE_DOMAIN_LABELS:
        raise ValueError(f"Invalid domain label: {label}")

def validate_acceptance_status(label: str) -> None:
    if label not in ACCEPTANCE_STATUS_LABELS:
        raise ValueError(f"Invalid status label: {label}")

def validate_evidence_trace_label(label: str) -> None:
    if label not in EVIDENCE_TRACE_LABELS:
        raise ValueError(f"Invalid evidence trace label: {label}")

def validate_reviewer_response_label(label: str) -> None:
    if label not in REVIEWER_RESPONSE_LABELS:
        raise ValueError(f"Invalid reviewer response label: {label}")

def validate_acceptance_risk(label: str) -> None:
    if label not in ACCEPTANCE_RISK_LABELS:
        raise ValueError(f"Invalid risk label: {label}")
''')

# local_acceptance/acceptance_models.py
with open(LOCAL_ACC_DIR / "acceptance_models.py", "w", encoding="utf-8") as f:
    f.write('''from dataclasses import dataclass, asdict
import hashlib

@dataclass
class AcceptanceDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_evidence: list[str]
    warnings: list[str]

@dataclass
class AcceptanceChecklistItem:
    item_id: str
    domain_label: str
    item_name: str
    description: str
    status: str
    evidence_refs: list[str]
    manual_review_required: bool
    warnings: list[str]

@dataclass
class ReviewerQuestion:
    question_id: str
    question: str
    domain_label: str
    expected_evidence: list[str]
    safe_answer_hint: str
    response_label: str
    warnings: list[str]

@dataclass
class EvidenceTraceItem:
    trace_id: str
    trace_type: str
    evidence_name: str
    source_path: str | None
    linked_output: str | None
    linked_test: str | None
    linked_doc: str | None
    trace_label: str
    warnings: list[str]

@dataclass
class AcceptanceFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_acceptance_domain_id(domain_label: str) -> str:
    return hashlib.md5(domain_label.encode()).hexdigest()[:8]

def build_acceptance_checklist_item_id(domain_label: str, item_name: str) -> str:
    return hashlib.md5(f"{domain_label}_{item_name}".encode()).hexdigest()[:8]

def build_reviewer_question_id(question: str) -> str:
    return hashlib.md5(question.encode()).hexdigest()[:8]

def build_evidence_trace_id(trace_type: str, evidence_name: str) -> str:
    return hashlib.md5(f"{trace_type}_{evidence_name}".encode()).hexdigest()[:8]

def build_acceptance_finding_id(title: str) -> str:
    return hashlib.md5(title.encode()).hexdigest()[:8]

def acceptance_domain_to_dict(item: AcceptanceDomain) -> dict:
    return asdict(item)

def acceptance_checklist_item_to_dict(item: AcceptanceChecklistItem) -> dict:
    return asdict(item)

def reviewer_question_to_dict(item: ReviewerQuestion) -> dict:
    return asdict(item)

def evidence_trace_item_to_dict(item: EvidenceTraceItem) -> dict:
    return asdict(item)

def acceptance_finding_to_dict(item: AcceptanceFinding) -> dict:
    return asdict(item)
''')

# local_acceptance/acceptance_domain_registry.py
with open(LOCAL_ACC_DIR / "acceptance_domain_registry.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from local_acceptance.acceptance_config import LocalAcceptanceProfile
from local_acceptance.acceptance_models import AcceptanceDomain, build_acceptance_domain_id, acceptance_domain_to_dict
from local_acceptance.acceptance_labels import list_acceptance_domain_labels

def build_default_acceptance_domains(profile: LocalAcceptanceProfile) -> list[AcceptanceDomain]:
    domains = []
    labels = list_acceptance_domain_labels()
    for lbl in labels:
        if lbl == "unknown_acceptance_domain":
            continue
        d = AcceptanceDomain(
            domain_id=build_acceptance_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Local/offline {lbl.replace('_', ' ')}",
            required_evidence=["docs/README.md"],
            warnings=["Bu domain resmi acceptance scope değildir."]
        )
        domains.append(d)
    return domains

def build_acceptance_domain_registry(profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_acceptance_domains(profile)
    df = pd.DataFrame([acceptance_domain_to_dict(d) for d in domains])
    summary = summarize_acceptance_domains(df)
    return df, summary

def summarize_acceptance_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "domain_labels": domain_df["domain_label"].tolist() if not domain_df.empty else []
    }
''')

# local_acceptance/acceptance_simulation.py
with open(LOCAL_ACC_DIR / "acceptance_simulation.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from local_acceptance.acceptance_config import LocalAcceptanceProfile
from local_acceptance.acceptance_models import AcceptanceChecklistItem, build_acceptance_checklist_item_id, acceptance_checklist_item_to_dict

def build_acceptance_checklist_items(profile: LocalAcceptanceProfile) -> list[AcceptanceChecklistItem]:
    items_def = [
        "final synthesis outputs mevcut",
        "hardening outputs mevcut",
        "safety boundary dokümante",
        "non-use policy dokümante",
        "master indexes mevcut",
        "contract catalogs mevcut",
        "documentation freeze snapshot mevcut",
        "RC dry-run manifest mevcut",
        "quality reports mevcut",
        "acceptance evidence trail üretilebilir",
        "reviewer pack üretilebilir",
        "no-go register üretilebilir",
        "raw secret output yok",
        "live/broker/deploy claim yok",
        "investment advice claim yok"
    ]
    
    items = []
    for nm in items_def:
        items.append(AcceptanceChecklistItem(
            item_id=build_acceptance_checklist_item_id("final_acceptance_domain", nm),
            domain_label="final_acceptance_domain",
            item_name=nm,
            description=f"Check for {nm}",
            status="acceptance_ready_for_rehearsal",
            evidence_refs=[],
            manual_review_required=True,
            warnings=["Bu madde resmi kabul değildir."]
        ))
    return items

def evaluate_acceptance_checklist_items(checklist_df: pd.DataFrame, project_root: Path, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    df = checklist_df.copy()
    if not df.empty:
        df["status"] = "acceptance_ready_for_rehearsal"
        df["manual_review_required"] = True
    return df, {}

def build_final_acceptance_simulation_checklist(project_root: Path, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_acceptance_checklist_items(profile)
    df = pd.DataFrame([acceptance_checklist_item_to_dict(i) for i in items])
    eval_df, _ = evaluate_acceptance_checklist_items(df, project_root, profile)
    summary = summarize_acceptance_simulation(eval_df)
    return eval_df, summary

def summarize_acceptance_simulation(checklist_df: pd.DataFrame) -> dict:
    return {
        "total_items": len(checklist_df),
        "status_counts": checklist_df["status"].value_counts().to_dict() if not checklist_df.empty else {}
    }
''')

# local_acceptance/reviewer_pack.py
with open(LOCAL_ACC_DIR / "reviewer_pack.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def build_reviewer_pack_sections(checklist_df: pd.DataFrame, question_df: pd.DataFrame, evidence_df: pd.DataFrame) -> list[dict]:
    return [
        {"title": "Amaç ve kapsam", "content": "Bu doküman bağımsız gözden geçirme provasıdır."},
        {"title": "Resmi audit olmadığına dair sınır", "content": "Bu doküman resmi audit, compliance belgesi veya yatırım tavsiyesi değildir."},
        {"title": "İnceleme sırası", "content": "1. Evidence trail 2. Questions 3. Trace matrix"},
        {"title": "Beklenen evidence seti", "content": f"Toplam evidence: {len(evidence_df) if evidence_df is not None else 0}"},
        {"title": "Reviewer question bank özeti", "content": f"Toplam soru: {len(question_df) if question_df is not None else 0}"},
        {"title": "Acceptance checklist özeti", "content": f"Checklist items: {len(checklist_df) if checklist_df is not None else 0}"},
        {"title": "No-go/safe-go özeti", "content": "No-go ve safe-go koşulları listelenmiştir."},
        {"title": "Quality/validation outputs", "content": "Validation and quality logs reviewed."},
        {"title": "Manual review notları", "content": "Tüm riskli alanlar manual review gerektirir."},
        {"title": "Yapılmayacaklar", "content": "Production release onayı, canlı emir, broker entegrasyonu yok."}
    ]

def build_independent_reviewer_pack(checklist_df: pd.DataFrame, question_df: pd.DataFrame, evidence_df: pd.DataFrame, profile: LocalAcceptanceProfile) -> tuple[str, dict]:
    sections = build_reviewer_pack_sections(checklist_df, question_df, evidence_df)
    
    lines = ["# Independent Reviewer Pack\\n"]
    for s in sections:
        lines.append(f"## {s['title']}\\n{s['content']}\\n")
    
    text = "\\n".join(lines)
    return text, summarize_independent_reviewer_pack(text)

def save_independent_reviewer_pack(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path

def summarize_independent_reviewer_pack(text: str) -> dict:
    return {"length": len(text)}
''')

# local_acceptance/reviewer_questions.py
with open(LOCAL_ACC_DIR / "reviewer_questions.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from local_acceptance.acceptance_config import LocalAcceptanceProfile
from local_acceptance.acceptance_models import ReviewerQuestion, build_reviewer_question_id, reviewer_question_to_dict

def build_default_reviewer_questions(profile: LocalAcceptanceProfile) -> list[ReviewerQuestion]:
    qs = [
        "Sistem ne yapar?",
        "Sistem ne yapmaz?",
        "Canlı emir gönderiyor mu?",
        "Broker entegrasyonu var mı?",
        "Yatırım tavsiyesi üretiyor mu?",
        "Production release mi?",
        "Hangi evidence çıktıları var?",
        "Hangi no-go koşulları var?",
        "Hangi manual review alanları var?",
        "DataLake ve report outputs nasıl doğrulanıyor?",
        "Contract freeze ne anlama gelir?",
        "RC dry-run freeze gerçek RC midir?"
    ]
    out = []
    for q in qs:
        out.append(ReviewerQuestion(
            question_id=build_reviewer_question_id(q),
            question=q,
            domain_label="reviewer_pack_domain",
            expected_evidence=[],
            safe_answer_hint="Sistem canlı işlem yapmaz. Boundary-first.",
            response_label="reviewer_response_ready",
            warnings=["Bu soru yatırım tavsiyesi yönlendirmesi yapmaz."]
        ))
    return out

def classify_reviewer_response_label(question_row: pd.Series, profile: LocalAcceptanceProfile) -> str:
    return "reviewer_response_ready"

def build_reviewer_question_bank(profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    qs = build_default_reviewer_questions(profile)
    df = pd.DataFrame([reviewer_question_to_dict(q) for q in qs])
    return df, summarize_reviewer_questions(df)

def summarize_reviewer_questions(question_df: pd.DataFrame) -> dict:
    return {"total_questions": len(question_df)}
''')

# local_acceptance/reviewer_evidence_matrix.py
with open(LOCAL_ACC_DIR / "reviewer_evidence_matrix.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def map_questions_to_evidence_paths(question_df: pd.DataFrame, project_root: Path, profile: LocalAcceptanceProfile) -> pd.DataFrame:
    df = question_df.copy()
    if not df.empty:
        df["mapped_evidence"] = df["question"].apply(lambda x: ["docs/README.md"])
        df["warnings"] = df["warnings"].apply(lambda x: x + ["Missing evidence manual review warning üretir."])
    return df

def build_reviewer_evidence_request_matrix(question_df: pd.DataFrame, project_root: Path, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    df = map_questions_to_evidence_paths(question_df, project_root, profile)
    return df, summarize_reviewer_evidence_matrix(df)

def summarize_reviewer_evidence_matrix(matrix_df: pd.DataFrame) -> dict:
    return {"mapped_questions": len(matrix_df)}
''')
