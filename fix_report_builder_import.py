import os
import glob

# The report_builder.py is just a module with functions, not a class
# So we shouldn't import ReportBuilder. Let's fix the scripts to just import the module

for p in glob.glob("commodity_fx_signal_bot/scripts/run_*governance*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_artifact*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_provenance*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_lineage*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_audit*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_dependency*.py"):
    with open(p, "r") as f:
        c = f.read()

    c = c.replace("from reports.report_builder import report_builder as ReportBuilder", "import reports.report_builder as rb")
    c = c.replace("rb = ReportBuilder(paths)", "")

    with open(p, "w") as f:
        f.write(c)

print("Fixed imports")
