import os

scripts = [
    "commodity_fx_signal_bot/scripts/run_level_candidate_preview.py",
    "commodity_fx_signal_bot/scripts/run_level_batch_build.py",
    "commodity_fx_signal_bot/scripts/run_reward_risk_preview.py",
    "commodity_fx_signal_bot/scripts/run_level_status.py"
]

# When I appended to report_builder.py earlier, I added methods to a class (implied by `self`) but then called them as module functions.
# Let's fix the report_builder.py to make them module functions

with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

content = content.replace("def build_level_candidate_preview_report(self,", "def build_level_candidate_preview_report(")
content = content.replace("def build_reward_risk_preview_report(self,", "def build_reward_risk_preview_report(")
content = content.replace("def build_level_batch_report(self,", "def build_level_batch_report(")
content = content.replace("def build_level_status_report(self,", "def build_level_status_report(")

with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
    f.write(content)
