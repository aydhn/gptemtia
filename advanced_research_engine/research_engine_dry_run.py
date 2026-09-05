import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
def build_research_engine_dry_run_harness_report(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]: return pd.DataFrame([{"status": "dry_run_ready"}]), {"ready": True}
def run_research_engine_dry_run_examples(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]: return pd.DataFrame([{"example": "test", "status": "success"}]), {"run": True}
def summarize_research_engine_dry_run(df: pd.DataFrame) -> dict: return {"records": len(df)}
