with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

# Remove the indentation for these functions so they become module-level functions
content = content.replace("    def build_level_candidate_preview_report", "def build_level_candidate_preview_report")
content = content.replace("    def build_reward_risk_preview_report", "def build_reward_risk_preview_report")
content = content.replace("    def build_level_batch_report", "def build_level_batch_report")
content = content.replace("    def build_level_status_report", "def build_level_status_report")

with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
    f.write(content)
