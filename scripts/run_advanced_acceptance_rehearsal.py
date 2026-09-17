# -*- coding: utf-8 -*-
"""Phase 158: Run Advanced Acceptance Rehearsal Script.

Executes acceptance rehearsal checklist verification without live executions.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.advanced_acceptance_rehearsal import (
    build_advanced_acceptance_rehearsal_registry,
)
from advanced_full_system_integration.advanced_acceptance_rehearsal_checkpoints import (
    build_advanced_acceptance_rehearsal_checkpoint_registry,
)
from advanced_full_system_integration.advanced_acceptance_rehearsal_scripts import (
    build_advanced_acceptance_rehearsal_script_registry,
)
from advanced_full_system_integration.advanced_acceptance_rehearsal_documentation import (
    build_advanced_acceptance_rehearsal_documentation_registry,
)
from advanced_full_system_integration.full_system_integration_report_builder import (
    build_advanced_acceptance_rehearsal_markdown_report,
)
from reports.report_builder import (
    build_advanced_acceptance_rehearsal_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_full_system_integration_profile()

    df_reh, s_reh = build_advanced_acceptance_rehearsal_registry(profile)
    df_rcp, s_rcp = build_advanced_acceptance_rehearsal_checkpoint_registry(profile)
    df_rsc, s_rsc = build_advanced_acceptance_rehearsal_script_registry(profile)
    df_rdc, s_rdc = build_advanced_acceptance_rehearsal_documentation_registry(profile)

    data_lake.save_advanced_acceptance_rehearsal_registry(df_reh, s_reh)
    data_lake.save_advanced_acceptance_rehearsal_checkpoint_registry(df_rcp, s_rcp)

    out_dir = Path("reports/output/advanced_full_system_integration")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_reh = build_advanced_acceptance_rehearsal_markdown_report(s_reh, df_reh)
    txt_reh = build_advanced_acceptance_rehearsal_text_report(s_reh, df_reh)

    with open(out_dir / "rehearsal.md", "w", encoding="utf-8") as f:
        f.write(md_reh)
    with open(out_dir / "rehearsal.txt", "w", encoding="utf-8") as f:
        f.write(txt_reh)

    print("=" * 70)
    print("PHASE 158: ADVANCED ACCEPTANCE REHEARSAL VERIFIED")
    print("=" * 70)
    print(f"Total Rehearsals      : {s_reh['total_rehearsals']}")
    print(f"Satisfied Count       : {s_reh['satisfied_count']}")
    print(f"Rehearsal Checkpoints : {s_rcp['total_checkpoints']}")
    print(f"Rehearsal Scripts     : {s_rsc['total_scripts']}")
    print(f"Documentation Items   : {s_rdc['total_documents']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
