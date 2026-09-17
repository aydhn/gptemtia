# -*- coding: utf-8 -*-
"""Phase 159: Run Release Candidate Checklists Script.

Builds and persists release candidate checklists and checkpoints.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_hardening.final_hardening_config import (
    get_default_final_hardening_profile,
)
from advanced_final_hardening.release_candidate_checklists import (
    build_release_candidate_checklist_registry,
)
from advanced_final_hardening.release_candidate_component_checkpoints import (
    build_release_candidate_component_checkpoint_registry,
)
from advanced_final_hardening.release_candidate_dependency_checkpoints import (
    build_release_candidate_dependency_checkpoint_registry,
)
from advanced_final_hardening.release_candidate_validation_checkpoints import (
    build_release_candidate_validation_checkpoint_registry,
)
from advanced_final_hardening.release_candidate_safety_checkpoints import (
    build_release_candidate_safety_checkpoint_registry,
)
from advanced_final_hardening.final_hardening_report_builder import (
    build_release_candidate_checkpoint_markdown_report,
)
from reports.report_builder import (
    build_release_candidate_checkpoint_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_hardening_profile()

    df_chk, s_chk = build_release_candidate_checklist_registry(profile)
    df_cmp, s_cmp = build_release_candidate_component_checkpoint_registry(profile)
    df_dep, s_dep = build_release_candidate_dependency_checkpoint_registry(profile)
    df_val, s_val = build_release_candidate_validation_checkpoint_registry(profile)
    df_sf, s_sf = build_release_candidate_safety_checkpoint_registry(profile)

    data_lake.save_release_candidate_checklist_registry(df_chk, s_chk)
    data_lake.save_release_candidate_component_checkpoint_registry(df_cmp, s_cmp)
    data_lake.save_release_candidate_dependency_checkpoint_registry(df_dep, s_dep)
    data_lake.save_release_candidate_validation_checkpoint_registry(df_val, s_val)
    data_lake.save_release_candidate_safety_checkpoint_registry(df_sf, s_sf)

    out_dir = Path("reports/output/advanced_final_hardening")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_report = build_release_candidate_checkpoint_markdown_report(s_chk, df_chk)
    txt_report = build_release_candidate_checkpoint_text_report(s_chk, df_chk)

    with open(out_dir / "checklists.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "checklists.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 159: RELEASE CANDIDATE CHECKLISTS & CHECKPOINTS INITIALIZED")
    print("=" * 70)
    print(f"Checklist Items: {s_chk['checklist_item_count']} | All Passed: {s_chk['all_passed']}")
    print(f"Components: {s_cmp['checkpoint_count']} | Dependencies: {s_dep['checkpoint_count']}")
    print(f"Status: {s_chk['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
