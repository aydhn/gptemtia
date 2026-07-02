from pathlib import Path
import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile
from .archive_item_registry import build_archive_item_registry

def build_documentation_archive_index(project_root: Path, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    from .archive_domain_registry import build_default_archive_domains
    domains = build_default_archive_domains(profile)
    domain_df = pd.DataFrame([d.__dict__ for d in domains])
    item_df, _ = build_archive_item_registry(project_root, domain_df, profile)
    docs = []
    if not item_df.empty and 'domain_label' in item_df.columns:
        cand_df = item_df[(item_df['item_status'] == 'archive_candidate') & (item_df['domain_label'] == 'documentation_archive')]
        for _, row in cand_df.iterrows():
            name = Path(row['relative_path']).name
            role = "project_root" if name == "README.md" else ("operator_guide" if name == "OPERATOR_MANUAL.md" else "general_doc")
            docs.append({"item_id": row['item_id'], "relative_path": row['relative_path'], "doc_role": role})
    df = pd.DataFrame(docs)
    return df, {"total_docs_indexed": len(df)}
