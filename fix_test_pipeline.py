with open("commodity_fx_signal_bot/tests/test_level_pipeline.py", "r") as f:
    content = f.read()

content = content.replace("from pathlib import Path\nlake = DummyDataLake(Path(\"/tmp/lake\"))", "from pathlib import Path\n    lake = DummyDataLake(Path(\"/tmp/lake\"))")

with open("commodity_fx_signal_bot/tests/test_level_pipeline.py", "w") as f:
    f.write(content)
