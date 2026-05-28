import pandas as pd
from typing import Dict, List, Optional
from final_review.final_review_models import FinalGap, build_final_gap_id

def classify_gap_category(row: pd.Series) -> str:
    return "unknown_gap"

def calculate_gap_priority(row: pd.Series) -> float:
    return 0.5

def build_gaps_from_audit_results(audit_tables: Dict[str, pd.DataFrame], summaries: Optional[dict] = None) -> List[FinalGap]:
    gaps = []

    if summaries and "documentation" in summaries:
        doc_summary = summaries["documentation"]
        if "missing_docs" in doc_summary:
            for doc in doc_summary["missing_docs"]:
                gaps.append(FinalGap(
                    gap_id=build_final_gap_id("documentation", "missing_doc"),
                    category="documentation_gap",
                    title=f"Missing Document: {doc}",
                    description=f"The required document {doc} is missing.",
                    affected_modules=["documentation"],
                    priority_score=0.8,
                    recommended_follow_up="Create the missing markdown document.",
                    warnings=[]
                ))

    return gaps

def gaps_to_dataframe(gaps: List[FinalGap]) -> pd.DataFrame:
    if not gaps:
        return pd.DataFrame(columns=[
            "gap_id", "category", "title", "description",
            "affected_modules", "priority_score", "recommended_follow_up", "warnings"
        ])
    return pd.DataFrame([g.__dict__ for g in gaps])

def summarize_final_gaps(gap_df: pd.DataFrame) -> dict:
    if gap_df.empty:
        return {"total_gaps": 0}
    return {"total_gaps": len(gap_df)}
