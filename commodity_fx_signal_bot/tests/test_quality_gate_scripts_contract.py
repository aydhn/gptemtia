import sys

def test_quality_gate_scripts_importable():
    # Attempt importing the scripts to ensure syntax correctness
    try:
        import scripts.run_local_ci_validation
        import scripts.run_test_health_report
        import scripts.run_import_graph_report
        import scripts.run_repo_hygiene_report
        import scripts.run_dependency_audit_report
        import scripts.run_static_safety_scan
        import scripts.run_smoke_test_report
        import scripts.run_release_candidate_report
        import scripts.run_release_quality_gate_status
    except Exception as e:
        assert False, f"Script import failed: {e}"
