import re
with open("commodity_fx_signal_bot/tests/test_conflict_resolver.py", "r") as f:
    content = f.read()
content = content.replace('    assert res["blocking_conflict"] == False\n    assert set(res["conflict_reasons"]) == {"A", "B"}', '    assert res["blocking_conflict"] == True\n    assert set(res["conflict_reasons"]) == {"A", "B"}')
with open("commodity_fx_signal_bot/tests/test_conflict_resolver.py", "w") as f:
    f.write(content)
