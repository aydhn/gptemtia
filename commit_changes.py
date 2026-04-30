import subprocess
import sys

def run_cmd(cmd, cwd=None):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    return True

cwd = "commodity_fx_signal_bot"

# Add changes
if not run_cmd(["git", "add", "."], cwd=cwd):
    sys.exit(1)

# Commit changes
if not run_cmd(["git", "commit", "-m", "feat: implement phase 9 trend features and events"], cwd=cwd):
    # Might already be committed or nothing to commit
    print("Nothing to commit or commit failed.")

print("Done.")
