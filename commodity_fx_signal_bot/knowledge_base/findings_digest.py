import pandas as pd
from typing import Tuple, Dict
import datetime

FINDING_KEYWORDS = [
    "warning", "insufficient_data", "conflict", "uncertainty",
    "failed", "missing", "stale", "high_priority",
    "next_best_experiment", "quality_adjusted", "governance_warning", "research_debt"
]

def extract_recent_findings(documents_df: pd.DataFrame, chunks_df: pd.DataFrame, max_items: int = 50) -> pd.DataFrame:
    if chunks_df.empty:
        return pd.DataFrame()

    # Search for keywords
    pattern = "|".join(FINDING_KEYWORDS)
    mask = chunks_df['text'].str.lower().str.contains(pattern, na=False)
    findings = chunks_df[mask].copy()

    if findings.empty:
        return pd.DataFrame()

    # If we had dates, we'd sort by date. Here we just take head.
    return findings.head(max_items)

def extract_important_warnings(chunks_df: pd.DataFrame, max_items: int = 50) -> pd.DataFrame:
    if chunks_df.empty:
        return pd.DataFrame()

    mask = chunks_df['text'].str.lower().str.contains("warning", na=False)
    warnings = chunks_df[mask].copy()

    if warnings.empty:
        return pd.DataFrame()

    return warnings.head(max_items)

def build_recent_findings_digest(documents_df: pd.DataFrame, chunks_df: pd.DataFrame) -> Tuple[str, Dict]:
    findings_df = extract_recent_findings(documents_df, chunks_df)

    if findings_df.empty:
        return "No recent findings found.", {"matches": 0}

    lines = ["# Recent Findings Digest\n"]
    lines.append("*This is an offline digest of research outputs, not a list of trade opportunities.*\n")

    for _, row in findings_df.iterrows():
        doc_id = row.get('document_id', 'unknown')
        text = row.get('text', '')
        snippet = text[:150] + "..." if len(text) > 150 else text
        lines.append(f"- **Source**: {doc_id}")
        lines.append(f"  > {snippet}")

    return "\n".join(lines), summarize_findings_digest(findings_df)

def build_warning_digest(chunks_df: pd.DataFrame) -> Tuple[str, Dict]:
    warnings_df = extract_important_warnings(chunks_df)

    if warnings_df.empty:
        return "No important warnings found.", {"matches": 0}

    lines = ["# Important Warnings Digest\n"]
    lines.append("*This is not a live system alarm. These are offline governance/research warnings.*\n")

    for _, row in warnings_df.iterrows():
        doc_id = row.get('document_id', 'unknown')
        text = row.get('text', '')
        snippet = text[:150] + "..." if len(text) > 150 else text
        lines.append(f"- **Source**: {doc_id}")
        lines.append(f"  > {snippet}")

    return "\n".join(lines), {"matches": len(warnings_df)}

def summarize_findings_digest(findings_df: pd.DataFrame) -> Dict:
    return {
        "total_findings": len(findings_df) if not findings_df.empty else 0,
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }
