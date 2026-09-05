import pandas as pd
from .__init__ import get_warning

def generate_master_closeout() -> pd.DataFrame:
    return pd.DataFrame(columns=["closeout_id", "area", "title", "status", "warning"])
