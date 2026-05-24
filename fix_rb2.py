path = "commodity_fx_signal_bot/reports/report_builder.py"
with open(path, "r") as f:
    content = f.read()

# Fix literal parsing for \n in the replacement block
# The issue is that the python script interpreted \n as actual newlines and un-escaped them. Let's fix that.
# Find the broken part and just re-write it correctly using open/write or a literal patch script.
lines = content.split("\n")
for i, line in enumerate(lines):
    if line.startswith("def build_artifact_inventory_text_report"):
        idx = i
        break

# Actually, it's easier to just append after the class ReportBuilder.
# Let's restore the original using git if possible, or just fix the end of the file.
