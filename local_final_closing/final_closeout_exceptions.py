import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def detect_final_closeout_exceptions(lock_df: pd.DataFrame, constitution_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    exceptions = []
    if no_go_df is not None and not no_go_df.empty:
        triggered = no_go_df[no_go_df.get("triggered", pd.Series(dtype=bool)) == True]
        for _, row in triggered.iterrows():
            exceptions.append({"type": "no_go_triggered", "detail": row.get("condition", "unknown")})
    return pd.DataFrame(exceptions)

def build_final_closeout_exception_register(lock_df: pd.DataFrame, constitution_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_final_closeout_exceptions(lock_df, constitution_df, no_go_df)
    return df, summarize_final_closeout_exceptions(df)

def summarize_final_closeout_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"total_exceptions": len(exception_df) if exception_df is not None else 0}
