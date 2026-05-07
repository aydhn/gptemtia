import os

scripts = [
    "commodity_fx_signal_bot/scripts/run_level_candidate_preview.py",
    "commodity_fx_signal_bot/scripts/run_level_batch_build.py",
    "commodity_fx_signal_bot/scripts/run_reward_risk_preview.py",
    "commodity_fx_signal_bot/scripts/run_level_status.py"
]

for script in scripts:
    with open(script, "r") as f:
        content = f.read()

    # We don't have a ReportBuilder class, these are module-level functions
    content = content.replace("from reports.report_builder import ReportBuilder", "import reports.report_builder as report_builder")
    content = content.replace("builder = ReportBuilder()", "")
    content = content.replace("builder.build_", "report_builder.build_")

    with open(script, "w") as f:
        f.write(content)
