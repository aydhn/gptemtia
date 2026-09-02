"""Mock reusable_template_catalog.py"""
import pandas as pd
def get_mock_df(): return pd.DataFrame([{"mock": 1}])
def get_mock_dict(): return {"status": "ok"}
def get_mock_str(): return "Mock content"
