with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

# Make sure all offline experiment tracking methods are INSIDE ReportBuilder class
# Find the ReportBuilder class definition
import re

# Remove any existing definition outside
content = re.sub(r'def build_hypothesis_registry_text_report.*?return report\s+', '', content, flags=re.DOTALL)

with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
    f.write(content)
