import glob

# Try self.project_root instead
for p in glob.glob("commodity_fx_signal_bot/scripts/run_*governance*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_artifact*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_provenance*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_lineage*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_audit*.py") + glob.glob("commodity_fx_signal_bot/scripts/run_dependency*.py"):
    with open(p, "r") as f:
        c = f.read()

    c = c.replace("paths.root_dir", "paths.project_root")

    with open(p, "w") as f:
        f.write(c)

print("Fixed scripts root dir")
