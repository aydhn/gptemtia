import pandas as pd
from pathlib import Path
from local_acceptance.acceptance_config import LocalAcceptanceProfile
from local_acceptance.acceptance_models import EvidenceTraceItem, build_evidence_trace_id, evidence_trace_item_to_dict

def classify_evidence_domain(path: Path, project_root: Path) -> str:
    path_str = str(path.relative_to(project_root)).lower()
    if "docs" in path_str: return "docs"
    if "reports" in path_str: return "reports"
    if "data/lake" in path_str: return "DataLake"
    if "tests" in path_str: return "tests"
    if "scripts" in path_str: return "scripts"
    if "safety" in path_str: return "safety"
    if "metadata" in path_str: return "metadata"
    if "evidence_governance" in path_str: return "evidence_governance"
    if "synthesis" in path_str: return "synthesis"
    if "hardening" in path_str: return "hardening"
    if "local_acceptance" in path_str: return "acceptance"
    return "unknown"

def classify_evidence_trace_label(path: Path, project_root: Path, profile: LocalAcceptanceProfile) -> str:
    return "evidence_trace_available"

def discover_local_evidence_items(project_root: Path, profile: LocalAcceptanceProfile) -> pd.DataFrame:
    # Dummy discovery for simulation
    items = []
    sample_files = ["docs/README.md", "reports/output/test.csv"]
    for sf in sample_files:
        items.append(EvidenceTraceItem(
            trace_id=build_evidence_trace_id("file", sf),
            trace_type="file",
            evidence_name=sf,
            source_path=sf,
            linked_output=None,
            linked_test=None,
            linked_doc=None,
            trace_label="evidence_trace_available",
            warnings=["Raw secret okunmaz."]
        ))
    return pd.DataFrame([evidence_trace_item_to_dict(i) for i in items])

def build_audit_style_local_evidence_trail(project_root: Path, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_local_evidence_items(project_root, profile)
    return df, summarize_evidence_trail(df)

def summarize_evidence_trail(evidence_df: pd.DataFrame) -> dict:
    return {"total_evidence_items": len(evidence_df)}
