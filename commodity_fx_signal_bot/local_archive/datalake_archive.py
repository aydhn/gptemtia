from pathlib import Path
import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile
from .archive_item_registry import build_archive_item_registry

def build_datalake_archive_index(project_root: Path, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    from .archive_domain_registry import build_default_archive_domains
    domains = build_default_archive_domains(profile)
    domain_df = pd.DataFrame([d.__dict__ for d in domains])
    item_df, _ = build_archive_item_registry(project_root, domain_df, profile)
    lake = []
    if not item_df.empty and 'domain_label' in item_df.columns:
        cand_df = item_df[(item_df['item_status'] == 'archive_candidate') & (item_df['domain_label'] == 'datalake_archive')]
        for _, row in cand_df.iterrows():
            try:
                rel = row['relative_path']
                domain = Path(rel).parts[2] if "data/lake" in rel and len(Path(rel).parts) > 2 else "general_data"
            except: domain = "general_data"
            lake.append({"item_id": row['item_id'], "relative_path": row['relative_path'], "datalake_domain": domain})
    df = pd.DataFrame(lake)
    return df, {"total_files_indexed": len(df)}
