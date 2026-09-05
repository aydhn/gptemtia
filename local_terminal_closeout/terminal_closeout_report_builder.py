import pandas as pd
from .__init__ import get_warning

def generate_report_builder() -> pd.DataFrame:
    return pd.DataFrame(columns=["id", "area", "title", "status", "warning"])
