#!/bin/bash
cat << 'PY' > fix_datalake.py
import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    dl_content = f.read()

# Instead of injecting below the class definition, we will inject at the very end of the file.
# Since it's a class we need to make sure indentation is correct. But DataLake is usually at the bottom.
# Let's just find a safe place.
dl_content = re.sub(r'class DataLake:.*?\n    # Phase 61:', 'class DataLake:', dl_content, flags=re.DOTALL)

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
    f.write(dl_content)

PY
python fix_datalake.py
