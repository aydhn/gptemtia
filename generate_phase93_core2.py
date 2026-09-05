import os
from pathlib import Path

base_dir = Path("commodity_fx_signal_bot/local_project_atlas")

with open(base_dir / "cross_phase_lookup.py", "w", encoding="utf-8") as f:
    f.write('''"""Cross-phase lookup engine module."""
import pandas as pd
from pathlib import Path
from .atlas_config import LocalProjectAtlasProfile
from .atlas_models import LookupItem, build_lookup_item_id, lookup_item_to_dict

def build_cross_phase_lookup_engine(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[str, dict]:
    doc = """# Cross-Phase Lookup Engine
This is an offline lookup engine. It is NOT an enterprise search, vector DB, or embedding system.
It maps keywords to script/report families purely based on string matching.
"""
    return doc, {"type": "offline_lookup_doc"}

def build_cross_phase_lookup_registry(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    items = []
    # Sample items
    keys = ["data", "report", "docs", "scripts", "tests", "models", "features"]
    for k in keys:
        item = LookupItem(
            lookup_id=build_lookup_item_id(k, "lookup_docs", f"docs/{k}.md"),
            lookup_key=k,
            lookup_family="lookup_docs",
            source_ref="keyword",
            target_ref=f"docs/{k}.md",
            relation_type="keyword_match",
            warnings=["Not semantic search"]
        )
        items.append(lookup_item_to_dict(item))
    
    df = pd.DataFrame(items)
    return df, summarize_cross_phase_lookup_registry(df)

def query_cross_phase_lookup(registry_df: pd.DataFrame, query_text: str, limit: int = 25) -> pd.DataFrame:
    if registry_df.empty:
        return registry_df
    mask = registry_df["lookup_key"].str.contains(query_text, case=False, na=False)
    return registry_df[mask].head(limit)

def summarize_cross_phase_lookup_registry(df: pd.DataFrame) -> dict:
    return {
        "total_lookups": len(df),
        "families": df["lookup_family"].unique().tolist() if not df.empty else []
    }
''')

with open(base_dir / "cross_phase_tables.py", "w", encoding="utf-8") as f:
    f.write('''"""Cross-phase lookup tables module."""
import pandas as pd
from pathlib import Path
from .atlas_config import LocalProjectAtlasProfile

def _build_dummy_table(name: str) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"id": f"dummy_{name}", "note": f"{name} placeholder"}])
    return df, summarize_cross_phase_table(df)

def build_cross_phase_output_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("output")

def build_cross_phase_script_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("script")

def build_cross_phase_docs_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("docs")

def build_cross_phase_datalake_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("datalake")

def build_cross_phase_report_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("report")

def build_cross_phase_generated_docs_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("generated_docs")

def build_cross_phase_safety_boundary_lookup_table(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_table("safety_boundary")

def summarize_cross_phase_table(df: pd.DataFrame) -> dict:
    return {"total_rows": len(df)}
''')

with open(base_dir / "semantic_toc.py", "w", encoding="utf-8") as f:
    f.write('''"""Offline semantic table of contents module."""
import pandas as pd
from pathlib import Path
from .atlas_config import LocalProjectAtlasProfile

def build_offline_semantic_table_of_contents(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[str, dict]:
    doc = """# Offline Semantic Table of Contents
This is a documented map of the project structure. It is NOT vector/embedding search.
## Modül Aileleri
- core
- ml
- data
- reports
## Rapor Aileleri
- output
## Manuel Review Noktaları
- Her phase geçişi
"""
    return doc, summarize_semantic_toc(doc)

def build_semantic_toc_sections(profile: LocalProjectAtlasProfile) -> list[dict]:
    return [{"section": "Modüller"}, {"section": "Raporlar"}]

def build_semantic_toc_registry(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame(build_semantic_toc_sections(profile))
    return df, summarize_semantic_toc_registry(df)

def summarize_semantic_toc(text: str) -> dict:
    return {"length": len(text)}

def summarize_semantic_toc_registry(df: pd.DataFrame) -> dict:
    return {"sections": len(df)}
''')

with open(base_dir / "terminal_project_atlas.py", "w", encoding="utf-8") as f:
    f.write('''"""Terminal project atlas module."""
import pandas as pd
from pathlib import Path
from .atlas_config import LocalProjectAtlasProfile

def build_terminal_project_atlas(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[str, dict]:
    doc = """# Terminal Project Atlas
Bu atlas offline bir dokümantasyon katmanıdır. Legal evidence, compliance, production approval, live trading veya yatırım tavsiyesi DEGILDIR.

## Phase 1-93 Haritası
Tüm fazların birleşik görünümü.

## Final Boundary Statement
No real deployment, no real broker execution, no investment advice.
"""
    return doc, summarize_terminal_project_atlas(doc)

def build_terminal_project_atlas_sections(project_root: Path, profile: LocalProjectAtlasProfile) -> list[dict]:
    return [{"title": "Ana Hatlar"}]

def summarize_terminal_project_atlas(text: str) -> dict:
    return {"length": len(text)}

def save_terminal_project_atlas(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
''')

with open(base_dir / "atlas_family_maps.py", "w", encoding="utf-8") as f:
    f.write('''"""Atlas family maps module."""
import pandas as pd
from pathlib import Path
from .atlas_config import LocalProjectAtlasProfile

def _build_dummy_map(name: str) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"family": name, "status": "mapped"}])
    return df, summarize_atlas_family_map(df)

def build_atlas_module_family_map(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_map("module")

def build_atlas_script_family_map(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_map("script")

def build_atlas_report_family_map(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_map("report")

def build_atlas_datalake_family_map(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_map("datalake")

def build_atlas_docs_family_map(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_map("docs")

def build_atlas_generated_docs_family_map(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_dummy_map("generated_docs")

def summarize_atlas_family_map(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
''')

print("Created core2")
