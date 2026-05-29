import os

scripts = [
    "commodity_fx_signal_bot/scripts/run_ux_alias_report.py",
    "commodity_fx_signal_bot/scripts/run_safe_command_suggestions.py",
    "commodity_fx_signal_bot/scripts/run_prompt_pack_report.py",
    "commodity_fx_signal_bot/scripts/run_productivity_checklist.py",
    "commodity_fx_signal_bot/scripts/run_analyst_task_board.py",
    "commodity_fx_signal_bot/scripts/run_operator_productivity_status.py"
]

for script in scripts:
    with open(script, "r") as f:
        content = f.read()

    # Change 'from reports.report_builder import ReportBuilder' to 'from reports.report_builder import build_ux_alias_text_report' or similar based on usage
    if "from reports.report_builder import ReportBuilder" in content:
        content = content.replace("from reports.report_builder import ReportBuilder", "from reports.report_builder import *")
        content = content.replace("ReportBuilder.build_ux_alias_text_report", "build_ux_alias_text_report")
        content = content.replace("ReportBuilder.build_safe_command_suggestion_text_report", "build_safe_command_suggestion_text_report")
        content = content.replace("ReportBuilder.build_prompt_pack_text_report", "build_prompt_pack_text_report")
        content = content.replace("ReportBuilder.build_productivity_checklist_text_report", "build_productivity_checklist_text_report")
        content = content.replace("ReportBuilder.build_analyst_task_board_text_report", "build_analyst_task_board_text_report")
        content = content.replace("ReportBuilder.build_operator_productivity_status_report", "build_operator_productivity_status_report")

        with open(script, "w") as f:
            f.write(content)
