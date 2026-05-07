import re

with open("commodity_fx_signal_bot/sizing/sizing_filters.py", "r") as f:
    content = f.read()

content = content.replace("from typing import Tuple, List, Dict, Any", "from typing import Tuple, List, Dict, Any, Optional")

with open("commodity_fx_signal_bot/sizing/sizing_filters.py", "w") as f:
    f.write(content)
