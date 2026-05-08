import os

with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

# I mistakenly wrote "def build_ml_training_batch_report(" instead of "def build_ml_training_batch_report(" when doing the first string replacement. Let's fix that if the method doesn't exist
if "def build_ml_training_batch_report(" not in content:
    with open("commodity_fx_signal_bot/update_reportbuilder_ml.py", "r") as f:
        ml_methods_str = f.read()

    # re-run the exact insert for report builder
    import subprocess
    subprocess.run(["python3", "commodity_fx_signal_bot/update_reportbuilder_ml.py"])

with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

# Remove 'self' from all build_ml_* methods to make them function directly if needed, or instantiate the builder properly
# Let's properly use the ReportBuilder object!
