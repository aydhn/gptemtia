"""Phase 130: Run Regime Transition Validation Report Script.

Performs schema, contract, no-lookahead, and safety validation for Phase 130.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_profile_registry import (
    build_regime_transition_profile_registry,
)
from advanced_regime_transition.regime_state_sequence_contracts import (
    build_regime_state_sequence_contract_registry,
)
from advanced_regime_transition.regime_transition_metric_registry import (
    build_regime_transition_metric_registry,
)
from advanced_regime_transition.transition_diagnostics_manifest import (
    build_transition_diagnostics_manifest,
)
from advanced_regime_transition.regime_transition_validation import (
    build_regime_transition_validation_report,
)
from advanced_regime_transition.regime_transition_safety_boundary import (
    build_regime_transition_safety_boundary,
)
from advanced_regime_transition.phase_131_handoff import (
    build_phase_131_cross_asset_regime_context_handoff_report,
)
from advanced_regime_transition.regime_transition_report_builder import (
    build_regime_transition_validation_markdown_report,
    build_regime_transition_safety_markdown_report,
    build_phase_131_handoff_markdown_report,
)
from reports.report_builder import build_regime_transition_validation_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_transition_profile()

    df_prof, _ = build_regime_transition_profile_registry(profile)
    df_cont, _ = build_regime_state_sequence_contract_registry(profile)
    df_tmet, _ = build_regime_transition_metric_registry(profile)
    df_man, _ = build_transition_diagnostics_manifest(profile)

    tables = {
        "profiles": df_prof,
        "contracts": df_cont,
        "metrics": df_tmet,
        "manifest": df_man,
    }

    df_val, s_val = build_regime_transition_validation_report(tables, profile)
    df_sft, s_sft = build_regime_transition_safety_boundary(profile)
    df_han, s_han = build_phase_131_cross_asset_regime_context_handoff_report(profile)

    data_lake.save_regime_transition_validation_report(df_val, s_val)
    data_lake.save_regime_transition_safety_boundary(df_sft, s_sft)
    data_lake.save_phase_131_cross_asset_regime_context_handoff_report(df_han, s_han)

    md_val = build_regime_transition_validation_markdown_report(s_val, df_val)
    md_sft = build_regime_transition_safety_markdown_report(s_sft, df_sft)
    md_han = build_phase_131_handoff_markdown_report(s_han, df_han)
    combined_md = f"{md_val}\n\n---\n\n{md_sft}\n\n---\n\n{md_han}"
    txt_content = build_regime_transition_validation_text_report(s_val, df_val)

    out_dir = Path("reports/output/advanced_regime_transition")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "regime_transition_validation.md", "w", encoding="utf-8") as f:
        f.write(combined_md)
    with open(out_dir / "regime_transition_validation.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)

    print("=" * 70)
    print("PHASE 130: REGIME TRANSITION VALIDATION & SAFETY REPORT")
    print("=" * 70)
    print(f"Validation Status: {s_val.get('validation_status')}")
    print(f"Total Checks     : {s_val.get('total_checks')}")
    print(f"Passed Checks    : {s_val.get('passed_checks')}")
    print(f"Failed Checks    : {s_val.get('failed_checks')}")
    print(f"Safety Status    : {s_sft.get('safety_status')}")
    print(f"Handoff Status   : {s_han.get('handoff_status')}")
    print(f"Next Phase       : {s_han.get('next_phase')}")
    print(f"Non-Signal       : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
