import pandas as pd
from .__init__ import get_warning

def generate_no_go() -> pd.DataFrame:
    return pd.DataFrame(columns=["id", "area", "title", "status", "warning"])
