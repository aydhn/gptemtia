import datetime
from typing import Dict, Tuple

import pandas as pd

FINDING_KEYWORDS = [
    "warning",
    "insufficient_data",
    "conflict",
    "uncertainty",
    "failed",
    "missing",
    "stale",
    "high_priority",
    "next_best_experiment",
    "quality_adjusted",
    "governance_warning",
    "research_debt",
]


def extract_recent_findings(
    documents_df: pd.DataFrame, chunks_df: pd.DataFrame, max_items: int = 50
) -> pd.DataFrame:
    if chunks_df.empty:
        return pd.DataFrame()

    # Search for keywords
    pattern = "|".join(FINDING_KEYWORDS)
    mask = chunks_df["text"].str.lower().str.contains(pattern, na=False)
    findings = chunks_df[mask].copy()

    if findings.empty:
        return pd.DataFrame()

    # If we had dates, we'd sort by date. Here we just take head.
    return findings.head(max_items)


def extract_important_warnings(chunks_df: pd.DataFrame, max_items: int = 50) -> pd.DataFrame:
    if chunks_df.empty:
        return pd.DataFrame()

    mask = chunks_df["text"].str.lower().str.contains("warning", na=False)
    warnings = chunks_df[mask].copy()

    if warnings.empty:
        return pd.DataFrame()

    return warnings.head(max_items)


def build_recent_findings_digest(
    documents_df: pd.DataFrame, chunks_df: pd.DataFrame
) -> Tuple[str, Dict]:
    findings_df = extract_recent_findings(documents_df, chunks_df)

    if findings_df.empty:
        return "No recent findings found.", {"matches": 0}

    lines = ["# Recent Findings Digest\n"]
    lines.append(
        "*This is an offline digest of research outputs, not a list of trade opportunities.*\n"
    )

    doc_ids = (
        findings_df["document_id"]
        if "document_id" in findings_df
        else ["unknown"] * len(findings_df)
    )
    texts = findings_df["text"] if "text" in findings_df else [""] * len(findings_df)

    for doc_id, text in zip(doc_ids, texts, strict=False):
        doc_id_val = "unknown" if pd.isna(doc_id) else doc_id
        text_val = "" if pd.isna(text) else str(text)
        snippet = text_val[:150] + "..." if len(text_val) > 150 else text_val
        lines.append(f"- **Source**: {doc_id_val}")
        lines.append(f"  > {snippet}")

    return "\n".join(lines), summarize_findings_digest(findings_df)


def build_warning_digest(chunks_df: pd.DataFrame) -> Tuple[str, Dict]:
    warnings_df = extract_important_warnings(chunks_df)

    if warnings_df.empty:
        return "No important warnings found.", {"matches": 0}

    lines = ["# Important Warnings Digest\n"]
    lines.append(
        "*This is not a live system alarm. These are offline governance/research warnings.*\n"
    )

    doc_ids = (
        warnings_df["document_id"]
        if "document_id" in warnings_df
        else ["unknown"] * len(warnings_df)
    )
    texts = warnings_df["text"] if "text" in warnings_df else [""] * len(warnings_df)

    for doc_id, text in zip(doc_ids, texts, strict=False):
        doc_id_val = "unknown" if pd.isna(doc_id) else doc_id
        text_val = "" if pd.isna(text) else str(text)
        snippet = text_val[:150] + "..." if len(text_val) > 150 else text_val
        lines.append(f"- **Source**: {doc_id_val}")
        lines.append(f"  > {snippet}")

    return "\n".join(lines), {"matches": len(warnings_df)}


def summarize_findings_digest(findings_df: pd.DataFrame) -> Dict:
    return {
        "total_findings": len(findings_df) if not findings_df.empty else 0,
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
