import re

# Fix conflict_resolver
with open("commodity_fx_signal_bot/tests/test_conflict_resolver.py", "r") as f:
    content = f.read()
content = content.replace('assert res["blocking_conflict"] is True', 'assert res["blocking_conflict"] == True')
with open("commodity_fx_signal_bot/tests/test_conflict_resolver.py", "w") as f:
    f.write(content)

# Fix directional_bias
with open("commodity_fx_signal_bot/tests/test_directional_bias.py", "r") as f:
    content = f.read()
content = content.replace('assert res["is_directional_conflict"] is True', 'assert res["is_directional_conflict"] == True')
with open("commodity_fx_signal_bot/tests/test_directional_bias.py", "w") as f:
    f.write(content)

# Fix neutral_filter
with open("commodity_fx_signal_bot/tests/test_neutral_filter.py", "r") as f:
    content = f.read()
content = content.replace('assert should_mark_neutral(0.6, 0.1, threshold=0.15) is True', 'assert should_mark_neutral(0.6, 0.1, neutral_zone_threshold=0.15) == True')
content = content.replace('assert should_mark_neutral(0.6, 0.2, threshold=0.15) is False', 'assert should_mark_neutral(0.6, 0.2, neutral_zone_threshold=0.15) == False')
with open("commodity_fx_signal_bot/tests/test_neutral_filter.py", "w") as f:
    f.write(content)
