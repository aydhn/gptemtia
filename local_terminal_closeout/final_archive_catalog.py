import pandas as pd
from .__init__ import get_warning

def generate_archive_catalog() -> pd.DataFrame:
    return pd.DataFrame(columns=["catalog_id", "area", "title", "status", "warning"])
