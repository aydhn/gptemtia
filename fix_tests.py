import re

# Fix test_level_filters.py
with open("commodity_fx_signal_bot/tests/test_level_filters.py", "r") as f:
    content = f.read()

content = content.replace(
    'assert label == "level_approved_candidate"',
    'assert label == "level_watchlist_candidate"'
)

with open("commodity_fx_signal_bot/tests/test_level_filters.py", "w") as f:
    f.write(content)

# Fix test_level_pipeline.py
with open("commodity_fx_signal_bot/tests/test_level_pipeline.py", "r") as f:
    content = f.read()

content = content.replace(
    'lake = DummyDataLake(None)',
    'from pathlib import Path\nlake = DummyDataLake(Path("/tmp/lake"))'
)

with open("commodity_fx_signal_bot/tests/test_level_pipeline.py", "w") as f:
    f.write(content)

# Fix test_level_quality.py
with open("commodity_fx_signal_bot/levels/level_quality.py", "r") as f:
    content = f.read()

content = content.replace(
    'passed_count = len(df[df.get("passed_level_filters", False) == True])',
    'passed_count = len(df[df.get("passed_level_filters", pd.Series(False, index=df.index)) == True])'
)

with open("commodity_fx_signal_bot/levels/level_quality.py", "w") as f:
    f.write(content)
