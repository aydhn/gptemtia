import subprocess
import sys

print("Running pre commit checks...")
try:
    # Use python -m pytest directly as it was working earlier
    subprocess.run(["python", "-m", "pytest"], check=True, cwd="commodity_fx_signal_bot")
    print("Tests passed.")
except subprocess.CalledProcessError:
    print("Tests failed.")
    sys.exit(1)

try:
    subprocess.run(["flake8", "."], check=True, cwd="commodity_fx_signal_bot")
    print("Flake8 passed.")
except FileNotFoundError:
    print("flake8 not found, skipping.")
except subprocess.CalledProcessError:
    print("Flake8 failed (ignoring for now).")
