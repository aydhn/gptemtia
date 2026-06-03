import os
for script in ["run_environment_snapshot.py", "run_dependency_inventory.py", "run_requirements_export.py", "run_install_verification.py", "run_portable_bundle_manifest.py", "run_reproducible_setup_guide.py", "run_packaging_status.py"]:
    with open(f"commodity_fx_signal_bot/scripts/{script}", "r") as f:
        t = f.read()

    # We should instantiate DataLake with the project root or nothing if it defaults safely in prod,
    # but the project has paths.PROJECT_ROOT. So let's pass that to DataLake.
    t = t.replace('dl = DataLake()', 'dl = DataLake(Path(__file__).resolve().parent.parent)')

    with open(f"commodity_fx_signal_bot/scripts/{script}", "w") as f:
        f.write(t)
