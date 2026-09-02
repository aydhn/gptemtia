import os
from pathlib import Path

def create_local_reuse_files():
    base_dir = Path("local_reuse")
    base_dir.mkdir(exist_ok=True)
    
    files = [
        "__init__.py",
        "reuse_config.py",
        "reuse_labels.py",
        "reuse_models.py",
        "reuse_domain_registry.py",
        "audit_memory_pack.py",
        "phase_memory_capsules.py",
        "reusable_template_catalog.py",
        "prompt_template_library.py",
        "module_blueprints.py",
        "script_patterns.py",
        "test_patterns.py",
        "datalake_contract_patterns.py",
        "report_patterns.py",
        "safety_boundary_patterns.py",
        "documentation_patterns.py",
        "knowledge_reuse_kit.py",
        "pattern_extraction.py",
        "architecture_pattern_extraction.py",
        "safety_pattern_extraction.py",
        "validation_quality_patterns.py",
        "handoff_delivery_closure_patterns.py",
        "v1_1_planning_seed.py",
        "v1_1_backlog_seed.py",
        "v1_1_safety_seed.py",
        "future_project_starter.py",
        "future_project_blueprints.py",
        "reuse_no_go_safe_go.py",
        "reuse_exceptions.py",
        "reuse_gaps.py",
        "reuse_risks.py",
        "reuse_scoring.py",
        "reuse_validation.py",
        "reuse_quality.py",
        "reuse_report_builder.py",
        "reuse_pipeline.py"
    ]
    
    for f in files:
        file_path = base_dir / f
        if not file_path.exists():
            with open(file_path, "w", encoding="utf-8") as file:
                file.write('"""\nLocal reuse module: ' + f + '\n"""\n')
            print(f"Created {file_path}")

def create_scripts():
    scripts_dir = Path("scripts")
    scripts_dir.mkdir(exist_ok=True)
    scripts = [
        "run_reuse_domain_registry.py",
        "run_final_audit_memory_pack.py",
        "run_reusable_template_catalog.py",
        "run_local_knowledge_reuse_kit.py",
        "run_v1_1_planning_seed.py",
        "run_reuse_quality_report.py",
        "run_reuse_status.py"
    ]
    
    for s in scripts:
        script_path = scripts_dir / s
        if not script_path.exists():
            with open(script_path, "w", encoding="utf-8") as file:
                file.write('"""\nScript: ' + s + '\n"""\n')
            print(f"Created {script_path}")

def create_tests():
    tests_dir = Path("tests")
    tests_dir.mkdir(exist_ok=True)
    tests = [
        "test_reuse_config.py",
        "test_reuse_labels.py",
        "test_reuse_models.py",
        "test_reuse_domain_registry.py",
        "test_audit_memory_pack.py",
        "test_phase_memory_capsules.py",
        "test_reusable_template_catalog.py",
        "test_prompt_template_library.py",
        "test_module_blueprints.py",
        "test_script_patterns.py",
        "test_test_patterns.py",
        "test_datalake_contract_patterns.py",
        "test_report_patterns.py",
        "test_safety_boundary_patterns.py",
        "test_documentation_patterns.py",
        "test_knowledge_reuse_kit.py",
        "test_pattern_extraction.py",
        "test_architecture_pattern_extraction.py",
        "test_safety_pattern_extraction.py",
        "test_validation_quality_patterns.py",
        "test_handoff_delivery_closure_patterns.py",
        "test_v1_1_planning_seed.py",
        "test_v1_1_backlog_seed.py",
        "test_v1_1_safety_seed.py",
        "test_future_project_starter.py",
        "test_future_project_blueprints.py",
        "test_reuse_no_go_safe_go.py",
        "test_reuse_exceptions.py",
        "test_reuse_gaps.py",
        "test_reuse_risks.py",
        "test_reuse_scoring.py",
        "test_reuse_validation.py",
        "test_reuse_quality.py",
        "test_reuse_report_builder.py",
        "test_reuse_pipeline.py",
        "test_local_reuse_scripts_contract.py"
    ]
    
    for t in tests:
        test_path = tests_dir / t
        if not test_path.exists():
            with open(test_path, "w", encoding="utf-8") as file:
                file.write('"""\nTest: ' + t + '\n"""\n')
            print(f"Created {test_path}")

if __name__ == "__main__":
    create_local_reuse_files()
    create_scripts()
    create_tests()
