import os

scripts_to_patch = [
    "run_hypothesis_registry_report.py",
    "run_experiment_tracking_report.py",
    "run_research_version_report.py",
    "run_ablation_study_report.py",
    "run_experiment_comparison_report.py",
    "run_experiment_leaderboard.py",
    "run_experiment_status.py"
]

for script in scripts_to_patch:
    path = f"commodity_fx_signal_bot/scripts/{script}"
    if not os.path.exists(path):
        continue
    with open(path, "r") as f:
        content = f.read()

    content = content.replace("from reports.report_builder import ReportBuilder", "from reports.report_builder import ReportBuilder")
    content = content.replace("report_builder_inst = ReportBuilder(paths)\n    txt_content = report_builder_inst", "report_builder_inst = ReportBuilder()\n    txt_content = report_builder_inst")

    with open(path, "w") as f:
        f.write(content)
