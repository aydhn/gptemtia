import pandas as pd
from .__init__ import get_warning

def generate_ledgers() -> pd.DataFrame:
    return pd.DataFrame(columns=["ledger_id", "area", "title", "status", "warning"])
