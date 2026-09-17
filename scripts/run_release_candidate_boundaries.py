# -*- coding: utf-8 -*-
"""Phase 159: Run Release Candidate Boundaries Script.

Builds and persists release candidate NO-GO and safe GO boundary registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_hardening.final_hardening_config import (
    get_default_final_hardening_profile,
)
from advanced_final_hardening.release_candidate_no_go_boundaries import (
    build_release_candidate_no_go_boundary_registry,
)
from advanced_final_hardening.release_candidate_go_boundaries import (
    build_release_candidate_go_boundary_registry,
)
from advanced_final_hardening.final_hardening_report_builder import (
    build_release_candidate_boundary_markdown_report,
)
from reports.report_builder import (
    build_release_candidate_boundary_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_hardening_profile()

    df_nogo, s_nogo = build_release_candidate_no_go_boundary_registry(profile)
    df_go, s_go = build_release_candidate_go_boundary_registry(profile)

    data_lake.save_release_candidate_no_go_boundary_registry(df_nogo, s_nogo)
    data_lake.save_release_candidate_go_boundary_registry(df_go, s_go)

    out_dir = Path("reports/output/advanced_final_hardening")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_report = build_release_candidate_boundary_markdown_report(s_nogo, df_nogo)
    txt_report = build_release_candidate_boundary_text_report(s_nogo, df_nogo)

    with open(out_dir / "boundaries.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "boundaries.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 159: RELEASE CANDIDATE BOUNDARIES INITIALIZED")
    print("=" * 70)
    print(f"NO-GO Boundaries: {s_nogo['no_go_boundary_count']} | GO Boundaries: {s_go['go_boundary_count']}")
    print(f"All NO-GO Enforced: {s_nogo['all_enforced']}")
    print(f"Status: {s_nogo['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
