import pandas as pd
from typing import Tuple, Dict
from .synthesis_config import LocalSynthesisProfile

def build_local_only_statement_table(profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame(columns=["item", "status"])
    return df, {"count": 0}

def build_final_local_only_statement(profile: LocalSynthesisProfile) -> Tuple[str, Dict]:
    text = "# Local Only Statement\nNo cloud/external service claim."
    df, summary = build_local_only_statement_table(profile)
    return text, summarize_local_only_statement(text, df)

def summarize_local_only_statement(text: str, statement_df: pd.DataFrame) -> Dict:
    return {"length": len(text)}
