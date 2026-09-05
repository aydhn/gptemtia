import pandas as pd
from .__init__ import get_warning

def generate_handover_maps() -> pd.DataFrame:
    return pd.DataFrame(columns=["map_id", "area", "title", "status", "warning"])
