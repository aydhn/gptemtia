# -*- coding: utf-8 -*-
"""Phase 160: Run Final Delivery Evidence Script.

Builds and persists acceptance, manifest, validation, safety, disabled execution,
manual review, runbook, and release candidate evidence registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_delivery.final_delivery_config import (
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_acceptance_evidence import (
    build_final_delivery_acceptance_evidence_registry,
)
from advanced_final_delivery.final_delivery_manifest_evidence import (
    build_final_delivery_manifest_evidence_registry,
)
from advanced_final_delivery.final_delivery_validation_evidence import (
    build_final_delivery_validation_evidence_registry,
)
from advanced_final_delivery.final_delivery_safety_evidence import (
    build_final_delivery_safety_evidence_registry,
)
from advanced_final_delivery.final_delivery_disabled_execution_evidence import (
    build_final_delivery_disabled_execution_evidence_registry,
)
from advanced_final_delivery.final_delivery_manual_review_evidence import (
    build_final_delivery_manual_review_evidence_registry,
)
from advanced_final_delivery.final_delivery_runbook_evidence import (
    build_final_delivery_runbook_evidence_registry,
)
from advanced_final_delivery.final_delivery_release_candidate_evidence import (
    build_final_delivery_release_candidate_evidence_registry,
)
from advanced_final_delivery.final_delivery_report_builder import (
    build_final_delivery_evidence_markdown_report,
)
from reports.report_builder import (
    build_final_delivery_evidence_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_delivery_profile()

    df_acc, s_acc = build_final_delivery_acceptance_evidence_registry(profile)
    df_mnf, s_mnf = build_final_delivery_manifest_evidence_registry(profile)
    df_val, s_val = build_final_delivery_validation_evidence_registry(profile)
    df_saf, s_saf = build_final_delivery_safety_evidence_registry(profile)
    df_dis, s_dis = build_final_delivery_disabled_execution_evidence_registry(profile)
    df_man, s_man = build_final_delivery_manual_review_evidence_registry(profile)
    df_run, s_run = build_final_delivery_runbook_evidence_registry(profile)
    df_rc, s_rc = build_final_delivery_release_candidate_evidence_registry(profile)

    if "--no-save" not in sys.argv and settings.final_delivery_save_reports:
        data_lake.save_final_delivery_acceptance_evidence_registry(df_acc, s_acc)
        data_lake.save_final_delivery_manifest_evidence_registry(df_mnf, s_mnf)
        data_lake.save_final_delivery_validation_evidence_registry(df_val, s_val)
        data_lake.save_final_delivery_safety_evidence_registry(df_saf, s_saf)
        data_lake.save_final_delivery_disabled_execution_evidence_registry(df_dis, s_dis)
        data_lake.save_final_delivery_manual_review_evidence_registry(df_man, s_man)
        data_lake.save_final_delivery_runbook_evidence_registry(df_run, s_run)
        data_lake.save_final_delivery_release_candidate_evidence_registry(df_rc, s_rc)

    out_dir = Path("reports/output/advanced_final_delivery")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_ev = build_final_delivery_evidence_markdown_report(s_acc, df_acc)
    txt_ev = build_final_delivery_evidence_text_report(s_acc, df_acc)

    if "--no-save" not in sys.argv:
        with open(out_dir / "evidence.md", "w", encoding="utf-8") as f:
            f.write(md_ev)
        with open(out_dir / "evidence.txt", "w", encoding="utf-8") as f:
            f.write(txt_ev)

    print("=" * 70)
    print("PHASE 160: FINAL DELIVERY EVIDENCE INITIALIZED")
    print("=" * 70)
    print(f"Acceptance Milestones: {s_acc['acceptance_milestone_count']}")
    print(f"Manifests: {s_mnf['manifest_evidence_count']} | Runbooks: {s_run['runbook_count']}")
    print(f"Status: {s_acc['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
