
import importlib
def test_scripts():
    scripts = [
        "scripts.run_review_domain_registry",
        "scripts.run_human_review_cockpit",
        "scripts.run_manual_approval_ledger",
        "scripts.run_expert_review_workbook",
        "scripts.run_offline_reviewer_console",
        "scripts.run_terminal_review_governance",
        "scripts.run_review_quality_report",
        "scripts.run_review_status"
    ]
    for s in scripts:
        mod = importlib.import_module(s)
        assert hasattr(mod, "main")
