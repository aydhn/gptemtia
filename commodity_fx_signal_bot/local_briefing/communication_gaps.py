import pandas as pd
from .briefing_config import LocalBriefingProfile

def detect_missing_audience_materials(audience_df: pd.DataFrame, section_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing materials", "description": "Check if materials align with audiences."}])

def detect_missing_faq_coverage(faq_df: pd.DataFrame) -> pd.DataFrame:
    if faq_df is None or faq_df.empty:
        return pd.DataFrame([{"gap": "FAQ missing", "description": "No FAQ found."}])
    return pd.DataFrame()

def detect_missing_boundary_language(section_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def build_communication_gap_register(
    audience_df: pd.DataFrame,
    section_df: pd.DataFrame,
    faq_df: pd.DataFrame,
    template_df: pd.DataFrame,
    profile: LocalBriefingProfile,
) -> tuple[pd.DataFrame, dict]:
    g1 = detect_missing_audience_materials(audience_df, section_df)
    g2 = detect_missing_faq_coverage(faq_df)
    g3 = detect_missing_boundary_language(section_df)
    
    df = pd.concat([g1, g2, g3], ignore_index=True) if not all(x.empty for x in [g1, g2, g3]) else pd.DataFrame(columns=["gap", "description"])
    return df, summarize_communication_gaps(df)

def summarize_communication_gaps(gap_df: pd.DataFrame) -> dict:
    if gap_df is None or gap_df.empty:
        return {"total_gaps": 0}
    return {"total_gaps": len(gap_df)}
