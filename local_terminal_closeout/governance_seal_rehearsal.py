import pandas as pd
from .__init__ import get_warning

def generate_seal_rehearsal() -> pd.DataFrame:
    return pd.DataFrame(columns=["seal_id", "area", "title", "status", "warning"])
