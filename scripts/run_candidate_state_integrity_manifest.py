"""Phase 128: Run Candidate State Integrity Manifest Script.

Generates candidate state integrity contracts, guards, policies, manifest, and Phase 129 handoff.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_rule_free.regime_rule_free_config import (
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_candidate_state_integrity_contracts import (
    build_regime_candidate_state_integrity_contract_registry,
)
from advanced_regime_rule_free.regime_candidate_state_integrity_manifest import (
    build_regime_candidate_state_integrity_manifest,
)
from advanced_regime_rule_free.regime_candidate_state_no_lookahead_guard import (
    build_regime_candidate_state_no_lookahead_guard_registry,
)
from advanced_regime_rule_free.regime_candidate_state_timestamp_policies import (
    build_regime_candidate_state_timestamp_policy_registry,
)
from advanced_regime_rule_free.regime_candidate_state_manual_review import (
    build_regime_candidate_state_manual_review_queue,
)
from advanced_regime_rule_free.regime_rule_free_non_signal_policies import (
    build_regime_rule_free_non_signal_policy_registry,
)
from advanced_regime_rule_free.regime_rule_free_forbidden_claims import (
    build_regime_rule_free_forbidden_claim_registry,
)
from advanced_regime_rule_free.regime_rule_free_source_preservation_policies import (
    build_regime_rule_free_source_preservation_policy_registry,
)
from advanced_regime_rule_free.phase_129_handoff import (
    build_phase_129_market_behavior_diagnostics_handoff_report,
)
from advanced_regime_rule_free.regime_rule_free_report_builder import (
    build_candidate_state_integrity_markdown_report,
    build_phase_129_handoff_markdown_report,
)
from reports.report_builder import (
    build_candidate_state_integrity_text_report,
    build_phase_129_handoff_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_rule_free_profile()

    df_ic, s_ic = build_regime_candidate_state_integrity_contract_registry(profile)
    df_nolook, s_nolook = build_regime_candidate_state_no_lookahead_guard_registry(profile)
    df_ts, s_ts = build_regime_candidate_state_timestamp_policy_registry(profile)
    df_rev, s_rev = build_regime_candidate_state_manual_review_queue(profile)
    df_nsp, s_nsp = build_regime_rule_free_non_signal_policy_registry(profile)
    df_fc, s_fc = build_regime_rule_free_forbidden_claim_registry(profile)
    df_sp, s_sp = build_regime_rule_free_source_preservation_policy_registry(profile)
    df_man, s_man = build_regime_candidate_state_integrity_manifest(profile)
    df_h129, s_h129 = build_phase_129_market_behavior_diagnostics_handoff_report(profile)

    data_lake.save_regime_candidate_state_integrity_contract_registry(df_ic, s_ic)
    data_lake.save_regime_candidate_state_no_lookahead_guard_registry(df_nolook, s_nolook)
    data_lake.save_regime_candidate_state_timestamp_policy_registry(df_ts, s_ts)
    data_lake.save_regime_candidate_state_manual_review_queue(df_rev, s_rev)
    data_lake.save_regime_rule_free_non_signal_policy_registry(df_nsp, s_nsp)
    data_lake.save_regime_rule_free_forbidden_claim_registry(df_fc, s_fc)
    data_lake.save_regime_rule_free_source_preservation_policy_registry(df_sp, s_sp)
    data_lake.save_regime_candidate_state_integrity_manifest(df_man, s_man)
    data_lake.save_phase_129_market_behavior_diagnostics_handoff_report(df_h129, s_h129)

    md_man = build_candidate_state_integrity_markdown_report(s_man, df_man)
    txt_man = build_candidate_state_integrity_text_report(s_man, df_man)
    md_h129 = build_phase_129_handoff_markdown_report(s_h129, df_h129)
    txt_h129 = build_phase_129_handoff_text_report(s_h129, df_h129)

    out_dir = Path("reports/output/advanced_regime_rule_free")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "integrity_manifest.md", "w", encoding="utf-8") as f:
        f.write(md_man)
    with open(out_dir / "integrity_manifest.txt", "w", encoding="utf-8") as f:
        f.write(txt_man)
    with open(out_dir / "phase_129_handoff.md", "w", encoding="utf-8") as f:
        f.write(md_h129)
    with open(out_dir / "phase_129_handoff.txt", "w", encoding="utf-8") as f:
        f.write(txt_h129)

    print("=" * 70)
    print("PHASE 128: INTEGRITY MANIFEST & PHASE 129 HANDOFF")
    print("=" * 70)
    print(f"Integrity Rules   : {s_ic['total_integrity_rules']}")
    print(f"Manifest Status   : {s_man['manifest_status']}")
    print(f"No-Lookahead Guard: {s_nolook['guard_status']}")
    print(f"Manual Review Q   : {s_rev['total_queued_items']} queued")
    print(f"Phase 129 Handoff : {s_h129['handoff_status']} ({s_h129['verified_items']}/{s_h129['total_items']})")
    print(f"Non-Signal Mandate: {s_man['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
