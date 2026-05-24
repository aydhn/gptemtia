import glob

# Replace paths.PROJECT_ROOT with paths.PROJECT_DIR

for p in glob.glob("commodity_fx_signal_bot/scripts/run_*governance*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_artifact*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_provenance*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_lineage*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_audit*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_dependency*.py"):
    with open(p, "r") as f:
        c = f.read()

    c = c.replace("paths.PROJECT_ROOT", "paths.PROJECT_DIR")

    with open(p, "w") as f:
        f.write(c)

print("Fixed scripts project root")
