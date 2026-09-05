import pandas as pd
from .__init__ import get_warning

def generate_handover_constitution() -> pd.DataFrame:
    return pd.DataFrame(columns=["constitution_id", "area", "title", "status", "warning"])
