import re

with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

content = content.replace("rep = \"*** DISCLAIMER ***\\n\"", "rep = \"*** DISCLAIMER ***\\n\"")
# The previous patch script wrote `rep = "*** DISCLAIMER ***\n"` but maybe without properly escaping the slash.
# Let's fix the report builder.
