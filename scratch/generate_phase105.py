import os
from pathlib import Path

# Paths
ROOT_DIR = Path("C:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia")
ADV_DIR = ROOT_DIR / "advanced_gap_closure"
SCRIPTS_DIR = ROOT_DIR / "scripts"
TESTS_DIR = ROOT_DIR / "tests"

# Create directories
os.makedirs(ADV_DIR, exist_ok=True)
os.makedirs(SCRIPTS_DIR, exist_ok=True)
os.makedirs(TESTS_DIR, exist_ok=True)

# Files to create in advanced_gap_closure
adv_files = [
    "__init__.py",
    "gap_closure_config.py",
    "gap_closure_labels.py",
    "gap_closure_models.py",
    "gap_closure_profile_registry.py",
    "readiness_reconciliation.py",
    "mvp_to_v2_closure_matrix.py",
    "foundation_audit.py",
    "dependency_closure_map.py",
    "missing_functionality_register.py",
    "implementation_backlog.py",
    "phase_106_handoff.py",
    "data_provider_requirements.py",
    "no_scraping_boundary.py",
    "provider_interface_readiness.py",
    "data_quality_readiness.py",
    "profile_data_requirement_map.py",
    "runtime_provider_handoff.py",
    "research_engine_provider_handoff.py",
    "config_provider_handoff.py",
    "functional_no_go_safe_go.py",
    "functional_gap_risks.py",
    "functional_gap_scoring.py",
    "functional_gap_validation.py",
    "functional_gap_quality.py",
    "functional_gap_report_builder.py",
    "functional_gap_pipeline.py"
]

for f in adv_files:
    (ADV_DIR / f).touch()

# Files to create in scripts
scripts_files = [
    "run_functional_gap_closure_profile_registry.py",
    "run_advanced_readiness_reconciliation.py",
    "run_mvp_to_v2_closure_matrix.py",
    "run_phase_101_104_foundation_audit.py",
    "run_phase_106_data_foundation_handoff.py",
    "run_functional_gap_quality_report.py",
    "run_functional_gap_status.py"
]

for f in scripts_files:
    (SCRIPTS_DIR / f).touch()

# Files to create in tests
tests_files = [
    "test_gap_closure_config.py",
    "test_gap_closure_labels.py",
    "test_gap_closure_models.py",
    "test_gap_closure_profile_registry.py",
    "test_readiness_reconciliation.py",
    "test_mvp_to_v2_closure_matrix.py",
    "test_foundation_audit.py",
    "test_dependency_closure_map.py",
    "test_missing_functionality_register.py",
    "test_implementation_backlog.py",
    "test_phase_106_handoff.py",
    "test_data_provider_requirements.py",
    "test_no_scraping_boundary.py",
    "test_provider_interface_readiness.py",
    "test_data_quality_readiness.py",
    "test_profile_data_requirement_map.py",
    "test_runtime_provider_handoff.py",
    "test_research_engine_provider_handoff.py",
    "test_config_provider_handoff.py",
    "test_functional_no_go_safe_go.py",
    "test_functional_gap_risks.py",
    "test_functional_gap_scoring.py",
    "test_functional_gap_validation.py",
    "test_functional_gap_quality.py",
    "test_functional_gap_report_builder.py",
    "test_functional_gap_pipeline.py",
    "test_functional_gap_scripts_contract.py"
]

for f in tests_files:
    (TESTS_DIR / f).touch()

print("Files created successfully.")
