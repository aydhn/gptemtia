import os
import re

# config/paths.py
with open("commodity_fx_signal_bot/config/paths.py", "r", encoding="utf-8") as f:
    content = f.read()

paths_addition = """
    # Phase 93
    "data/lake/local_project_atlas",
    "data/lake/local_project_atlas/profiles",
    "data/lake/local_project_atlas/domains",
    "data/lake/local_project_atlas/meta_index",
    "data/lake/local_project_atlas/navigation",
    "data/lake/local_project_atlas/lookup",
    "data/lake/local_project_atlas/semantic_toc",
    "data/lake/local_project_atlas/terminal_atlas",
    "data/lake/local_project_atlas/family_maps",
    "data/lake/local_project_atlas/phase_maps",
    "data/lake/local_project_atlas/route_maps",
    "data/lake/local_project_atlas/glossary",
    "data/lake/local_project_atlas/crosswalks",
    "data/lake/local_project_atlas/no_go_safe_go",
    "data/lake/local_project_atlas/exceptions",
    "data/lake/local_project_atlas/gaps",
    "data/lake/local_project_atlas/risks",
    "data/lake/local_project_atlas/scoring",
    "data/lake/local_project_atlas/validation",
    "data/lake/local_project_atlas/quality",
    "reports/output/local_project_atlas",
    "reports/output/local_project_atlas/csv",
    "reports/output/local_project_atlas/markdown",
    "reports/output/local_project_atlas/txt",
    "reports/output/local_project_atlas/json",
    "docs/generated/local_project_atlas",
"""

if "data/lake/local_project_atlas" not in content:
    content = content.replace("]  # End of required_dirs", paths_addition + "]  # End of required_dirs")
    with open("commodity_fx_signal_bot/config/paths.py", "w", encoding="utf-8") as f:
        f.write(content)

print("Paths patched")
