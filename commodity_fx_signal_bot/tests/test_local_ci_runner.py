from pathlib import Path
from quality_gates.quality_config import QualityGateProfile
from quality_gates.quality_models import QualityCheckResult
from quality_gates.local_ci_runner import LocalCIRunner

def test_local_ci_runner_methods():
    profile = QualityGateProfile(name="mock", description="mock")
    runner = LocalCIRunner(Path("."), profile)

    res = runner.run_test_health()
    assert isinstance(res, QualityCheckResult)

    res = runner.run_import_validation()
    assert isinstance(res, QualityCheckResult)

    res = runner.run_static_safety_scan()
    assert isinstance(res, QualityCheckResult)

    res = runner.run_repo_hygiene()
    assert isinstance(res, QualityCheckResult)

    res = runner.run_dependency_audit()
    assert isinstance(res, QualityCheckResult)

    res = runner.run_smoke_tests()
    assert isinstance(res, QualityCheckResult)

    res = runner.run_output_contracts()
    assert isinstance(res, QualityCheckResult)

    res = runner.run_documentation_coverage()
    assert isinstance(res, QualityCheckResult)

    results, summary = runner.run_all()
    assert isinstance(results, list)
    assert isinstance(summary, dict)
