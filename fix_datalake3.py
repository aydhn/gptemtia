with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    dl_content = f.read()

import re
# We need to make sure DataLake signature was not modified
# "TypeError: DataLake() takes no arguments"
# Wait, DataLake takes no arguments usually. But maybe tests try to instantiate it with arguments?
# Or maybe the __init__ was lost?

print("Checking __init__ in DataLake")
match = re.search(r'class DataLake:.*?(def __init__.*?\n)', dl_content, flags=re.DOTALL)
if match:
    print(match.group(1)[:200])
else:
    print("No __init__ found in DataLake")
