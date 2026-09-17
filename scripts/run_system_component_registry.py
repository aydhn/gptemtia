# -*- coding: utf-8 -*-
"""Phase 158: Run System Component Registry Script.

Builds and persists component, dependency, and checkpoint registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_component_registry import (
    build_system_component_registry,
)
from advanced_full_system_integration.system_component_dependencies import (
    build_system_component_dependency_registry,
)
from advanced_full_system_integration.system_component_checkpoints import (
    build_system_component_checkpoint_registry,
)
from advanced_full_system_integration.full_system_integration_report_builder import (
    build_system_component_markdown_report,
    build_system_dependency_markdown_report,
)
from reports.report_builder import (
    build_system_component_text_report,
    build_system_dependency_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_full_system_integration_profile()

    df_cmp, s_cmp = build_system_component_registry(profile)
    df_dep, s_dep = build_system_component_dependency_registry(profile)
    df_chk, s_chk = build_system_component_checkpoint_registry(profile)

    data_lake.save_system_component_registry(df_cmp, s_cmp)
    data_lake.save_system_component_dependency_registry(df_dep, s_dep)
    data_lake.save_system_component_checkpoint_registry(df_chk, s_chk)

    out_dir = Path("reports/output/advanced_full_system_integration")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_cmp = build_system_component_markdown_report(s_cmp, df_cmp)
    txt_cmp = build_system_component_text_report(s_cmp, df_cmp)
    md_dep = build_system_dependency_markdown_report(s_dep, df_dep)
    txt_dep = build_system_dependency_text_report(s_dep, df_dep)

    with open(out_dir / "components.md", "w", encoding="utf-8") as f:
        f.write(md_cmp)
    with open(out_dir / "components.txt", "w", encoding="utf-8") as f:
        f.write(txt_cmp)
    with open(out_dir / "dependencies.md", "w", encoding="utf-8") as f:
        f.write(md_dep)
    with open(out_dir / "dependencies.txt", "w", encoding="utf-8") as f:
        f.write(txt_dep)

    print("=" * 70)
    print("PHASE 158: SYSTEM COMPONENTS & DEPENDENCY GRAPH INITIALIZED")
    print("=" * 70)
    print(f"Total Components    : {s_cmp['total_components']}")
    print(f"Total Dependencies  : {s_dep['total_dependencies']}")
    print(f"Hard Dependencies   : {s_dep['hard_dependencies']}")
    print(f"Total Checkpoints   : {s_chk['total_checkpoints']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
