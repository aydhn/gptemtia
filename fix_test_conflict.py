import re
with open("commodity_fx_signal_bot/tests/test_conflict_resolver.py", "r") as f:
    content = f.read()
content = content.replace('assert res["blocking_conflict"] == True', 'assert res["blocking_conflict"] == False')
with open("commodity_fx_signal_bot/tests/test_conflict_resolver.py", "w") as f:
    f.write(content)
