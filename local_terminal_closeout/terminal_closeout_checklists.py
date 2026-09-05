import pandas as pd
from .__init__ import get_warning

def generate_checklists() -> pd.DataFrame:
    return pd.DataFrame(columns=["checklist_id", "area", "title", "status", "warning"])
