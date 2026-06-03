with open("commodity_fx_signal_bot/portable_packaging/dependency_inventory.py", "r") as f:
    inv = f.read()

import re
inv = inv.replace('row["source"]', 'row.get("source_x", row.get("source_y", "unknown"))')

with open("commodity_fx_signal_bot/portable_packaging/dependency_inventory.py", "w") as f:
    f.write(inv)
