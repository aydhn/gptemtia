import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e)
        sys.exit(1)

run_command("git add .")
run_command("git commit -m 'feat: complete phase 11 volume/liquidity feature set'")
