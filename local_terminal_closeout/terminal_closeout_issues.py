import pandas as pd
from .__init__ import get_warning

def generate_issues() -> pd.DataFrame:
    return pd.DataFrame(columns=["issue_id", "area", "title", "status", "warning"])
