import os
import subprocess
from pathlib import Path

def test_scripts():
    scripts = [
        "commodity_fx_signal_bot.scripts.run_performance_domain_registry",
        "commodity_fx_signal_bot.scripts.run_final_local_performance_budget",
        "commodity_fx_signal_bot.scripts.run_resource_footprint_rehearsal",
        "commodity_fx_signal_bot.scripts.run_maintenance_cost_estimate",
        "commodity_fx_signal_bot.scripts.run_offline_efficiency_plan",
        "commodity_fx_signal_bot.scripts.run_performance_quality_report",
        "commodity_fx_signal_bot.scripts.run_performance_status"
    ]
    
    for s in scripts:
        print(f"Running {s}...")
        res = subprocess.run(["python", "-m", s], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Error running {s}: {res.stderr}")
        else:
            print(f"Success: {s}")

if __name__ == "__main__":
    test_scripts()
