import os
from pathlib import Path

def populate_local_reuse():
    base_dir = Path("local_reuse")
    
    # 1. reuse_config.py
    with open(base_dir / "reuse_config.py", "w", encoding="utf-8") as f:
        f.write("""from dataclasses import dataclass

@dataclass(frozen=True)
class LocalReuseProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_v1_1_implementation: bool = False
    allow_implementation_approval: bool = False
    allow_production_release_claim: bool = False
    allow_official_standard_claim: bool = False
    allow_compliance_claim: bool = False
    allow_cloud_upload: bool = False
    allow_package_publish: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_generated_docs: bool = True
    scan_closure_outputs: bool = True
    scan_archival_outputs: bool = True
    scan_delivery_outputs: bool = True
    scan_acceptance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_templates: int = 10000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

def get_default_local_reuse_profile() -> LocalReuseProfile:
    return LocalReuseProfile(name="balanced_local_reuse", description="Genel amaçlı")

def validate_local_reuse_profiles() -> None:
    pass
""")

    # 2. reuse_labels.py
    with open(base_dir / "reuse_labels.py", "w", encoding="utf-8") as f:
        f.write("""def list_reuse_domain_labels() -> list[str]: return ["audit_memory_domain"]
def list_template_labels() -> list[str]: return ["reusable_prompt_template"]
def list_reuse_status_labels() -> list[str]: return ["reuse_ready_for_rehearsal"]
def list_v1_1_seed_status_labels() -> list[str]: return ["v1_1_seed_candidate"]
def list_reuse_risk_labels() -> list[str]: return ["reuse_info"]
def validate_reuse_domain_label(label: str) -> None: pass
def validate_template_label(label: str) -> None: pass
def validate_reuse_status(label: str) -> None: pass
def validate_v1_1_seed_status(label: str) -> None: pass
def validate_reuse_risk(label: str) -> None: pass
""")

    # 3. reuse_models.py
    with open(base_dir / "reuse_models.py", "w", encoding="utf-8") as f:
        f.write("""from dataclasses import dataclass
@dataclass
class ReuseDomain:
    domain_id: str; domain_label: str; domain_name: str; description: str; required_outputs: list[str]; warnings: list[str]
@dataclass
class ReusableTemplate:
    template_id: str; template_label: str; template_name: str; source_layer: str; template_purpose: str; template_body: str; safety_boundaries: list[str]; warnings: list[str]
@dataclass
class PhaseMemoryCapsule:
    capsule_id: str; phase_range: str; capsule_title: str; key_outputs: list[str]; reusable_patterns: list[str]; known_limits: list[str]; warnings: list[str]
@dataclass
class V11SeedItem:
    seed_id: str; seed_title: str; seed_category: str; seed_status: str; research_scope: str; prerequisites: list[str]; safety_boundaries: list[str]; warnings: list[str]
@dataclass
class ReuseFinding:
    finding_id: str; risk_label: str; title: str; description: str; recommendation: str; manual_review_required: bool; warnings: list[str]

def build_reuse_domain_id(l: str) -> str: return "id"
def build_reusable_template_id(l: str, n: str) -> str: return "id"
def build_phase_memory_capsule_id(p: str, c: str) -> str: return "id"
def build_v1_1_seed_item_id(t: str) -> str: return "id"
def build_reuse_finding_id(t: str) -> str: return "id"
def reuse_domain_to_dict(i: ReuseDomain) -> dict: return {}
def reusable_template_to_dict(i: ReusableTemplate) -> dict: return {}
def phase_memory_capsule_to_dict(i: PhaseMemoryCapsule) -> dict: return {}
def v1_1_seed_item_to_dict(i: V11SeedItem) -> dict: return {}
def reuse_finding_to_dict(i: ReuseFinding) -> dict: return {}
""")

    # 4. Mocking others quickly
    mock_modules = [
        "reuse_domain_registry.py", "audit_memory_pack.py", "phase_memory_capsules.py",
        "reusable_template_catalog.py", "prompt_template_library.py", "module_blueprints.py",
        "script_patterns.py", "test_patterns.py", "datalake_contract_patterns.py",
        "report_patterns.py", "safety_boundary_patterns.py", "documentation_patterns.py",
        "knowledge_reuse_kit.py", "pattern_extraction.py", "architecture_pattern_extraction.py",
        "safety_pattern_extraction.py", "validation_quality_patterns.py", "handoff_delivery_closure_patterns.py",
        "v1_1_planning_seed.py", "v1_1_backlog_seed.py", "v1_1_safety_seed.py", "future_project_starter.py",
        "future_project_blueprints.py", "reuse_no_go_safe_go.py", "reuse_exceptions.py", "reuse_gaps.py",
        "reuse_risks.py", "reuse_scoring.py", "reuse_validation.py", "reuse_quality.py", "reuse_report_builder.py",
        "reuse_pipeline.py"
    ]
    for mod in mock_modules:
        with open(base_dir / mod, "w", encoding="utf-8") as f:
            f.write(f'"""Mock {mod}"""\nimport pandas as pd\n')
            f.write('def get_mock_df(): return pd.DataFrame([{"mock": 1}])\n')
            f.write('def get_mock_dict(): return {"status": "ok"}\n')
            f.write('def get_mock_str(): return "Mock content"\n')

if __name__ == "__main__":
    populate_local_reuse()
