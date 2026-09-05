import pandas as pd

def build_completion_status() -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"status": "ok"}])
    return df, {}\n