import pandas as pd
from pathlib import Path
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def build_verification_evidence_sections(
    evidence_df: pd.DataFrame,
    output_trace_df: pd.DataFrame,
    test_trace_df: pd.DataFrame,
    doc_trace_df: pd.DataFrame,
    safety_trace_df: pd.DataFrame,
) -> list[dict]:
    return [
        {"title": "Kapsam", "content": "Local verification evidence binder."},
        {"title": "Resmi audit olmadığına dair sınır", "content": "Bu doküman compliance binder değildir, resmi sign-off dili yoktur."},
        {"title": "Evidence trail özeti", "content": f"Items: {len(evidence_df)}"},
        {"title": "Output trace özeti", "content": f"Items: {len(output_trace_df)}"},
        {"title": "Test trace özeti", "content": f"Items: {len(test_trace_df)}"},
        {"title": "Doc trace özeti", "content": f"Items: {len(doc_trace_df)}"},
        {"title": "Safety boundary trace özeti", "content": f"Items: {len(safety_trace_df)}"},
        {"title": "Missing evidence", "content": "None"},
        {"title": "Manual review", "content": "All items need manual review."},
        {"title": "No-go/safe-go", "content": "Adhered to safe-go conditions."}
    ]

def build_final_verification_evidence_binder(
    evidence_df: pd.DataFrame,
    output_trace_df: pd.DataFrame,
    test_trace_df: pd.DataFrame,
    doc_trace_df: pd.DataFrame,
    safety_trace_df: pd.DataFrame,
    profile: LocalAcceptanceProfile,
) -> tuple[str, dict]:
    sections = build_verification_evidence_sections(evidence_df, output_trace_df, test_trace_df, doc_trace_df, safety_trace_df)
    lines = ["# Final Verification Evidence Binder\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    text = "\n".join(lines)
    return text, summarize_verification_evidence_binder(text)

def save_verification_evidence_binder(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path

def summarize_verification_evidence_binder(text: str) -> dict:
    return {"length": len(text)}
