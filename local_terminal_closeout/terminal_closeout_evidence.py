import pandas as pd
from .__init__ import get_warning

def generate_evidence() -> pd.DataFrame:
    return pd.DataFrame(columns=["evidence_id", "area", "title", "status", "warning"])
