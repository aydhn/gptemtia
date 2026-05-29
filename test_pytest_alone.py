import subprocess
print(subprocess.run(["python3", "-m", "pytest", "commodity_fx_signal_bot/tests/test_regression_pipeline.py"], capture_output=True).stderr.decode())
