import os
from pathlib import Path

base_dir = Path("c:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/commodity_fx_signal_bot")
paths_path = base_dir / "config" / "paths.py"

with open(paths_path, "r", encoding="utf-8") as f:
    content = f.read()

if "LAKE_DIR / 'local_synthesis'" not in content:
    new_dirs = """
    # Phase 75: Local Synthesis
    ls_lake = LAKE_DIR / 'local_synthesis'
    ls_reps = REPORTS_DIR / 'output' / 'local_synthesis'
    ls_docs = DOCS_DIR / 'generated' / 'local_synthesis'
    
    directories.extend([
        ls_lake,
        ls_lake / 'profiles',
        ls_lake / 'phase_families',
        ls_lake / 'master_indexes',
        ls_lake / 'final_maps',
        ls_lake / 'capabilities',
        ls_lake / 'boundaries',
        ls_lake / 'dependencies',
        ls_lake / 'catalogs',
        ls_lake / 'dossiers',
        ls_lake / 'binders',
        ls_lake / 'statements',
        ls_lake / 'limitations',
        ls_lake / 'manual_review',
        ls_lake / 'no_go_safe_go',
        ls_lake / 'navigation',
        ls_lake / 'checklists',
        ls_lake / 'validation',
        ls_lake / 'quality',
        ls_reps,
        ls_reps / 'csv',
        ls_reps / 'markdown',
        ls_reps / 'txt',
        ls_reps / 'json',
        ls_docs
    ])

    for directory in directories:
"""
    content = content.replace("    for directory in directories:\n", new_dirs)
    
    # Check if we also need to add properties to ProjectPaths
    if "def local_synthesis_dir(self):" not in content:
        props = """
    @property
    def local_synthesis_dir(self): return self.data_lake_dir / "local_synthesis"
    @property
    def local_synthesis_reports_dir(self): return self.reports_dir / "output" / "local_synthesis"
    @property
    def local_synthesis_docs_dir(self): return self.docs_dir / "generated" / "local_synthesis"
"""
        content = content.replace("class ProjectPaths:\n", "class ProjectPaths:\n" + props)

    with open(paths_path, "w", encoding="utf-8") as f:
        f.write(content)
