from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, List
from .archive_config import LocalArchiveProfile
from .archive_item_registry import build_archive_item_registry

def classify_archive_candidate_priority(path: Path, project_root: Path) -> str:
    try:
        rel = str(path.relative_to(project_root)).lower()
    except ValueError:
        rel = str(path).lower()
    if "readme" in rel or "architecture" in rel or "docs/" in rel: return "high"
    if "reports/" in rel and (".pdf" in rel or ".md" in rel): return "high"
    if "data/lake" in rel and ".json" in rel: return "medium"
    if "config/" in rel: return "high"
    if "tests/" in rel: return "medium"
    return "low"

def detect_archive_candidate_reasons(path: Path, project_root: Path) -> List[str]:
    try:
        rel = str(path.relative_to(project_root)).lower()
    except ValueError:
        rel = str(path).lower()
    reasons = []
    if "docs/" in rel or "readme" in rel: reasons.append("docs_required")
    if "reports/" in rel: reasons.append("generated_report")
    if "data/lake" in rel: reasons.append("datalake_manifest")
    if "operator_manual" in rel: reasons.append("operator_manual")
    if "evidence" in rel: reasons.append("evidence_output")
    if "metadata" in rel: reasons.append("metadata_output")
    return reasons

def build_archive_candidate_inventory(project_root: Path, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    from .archive_domain_registry import build_default_archive_domains
    domains = build_default_archive_domains(profile)
    domain_df = pd.DataFrame([d.__dict__ for d in domains])
    item_df, _ = build_archive_item_registry(project_root, domain_df, profile)
    candidates = []
    if not item_df.empty and 'item_status' in item_df.columns:
        cand_df = item_df[item_df['item_status'] == 'archive_candidate'].copy()
        for _, row in cand_df.iterrows():
            path = project_root / row['relative_path']
            priority = classify_archive_candidate_priority(path, project_root)
            reasons = detect_archive_candidate_reasons(path, project_root)
            candidates.append({
                "item_id": row['item_id'],
                "relative_path": row['relative_path'],
                "priority": priority,
                "reasons": ", ".join(reasons)
            })
    df = pd.DataFrame(candidates)
    summary = summarize_archive_candidates(df)
    return df, summary

def summarize_archive_candidates(candidate_df: pd.DataFrame) -> Dict:
    if candidate_df.empty: return {"total": 0}
    high = int((candidate_df['priority'] == 'high').sum()) if 'priority' in candidate_df.columns else 0
    return {
        "total_candidates": len(candidate_df),
        "high_priority": high,
        "notice": "Candidates are flagged for manual review, no auto-archive will happen."
    }
