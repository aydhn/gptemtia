"""Phase 130: Run State Transition Diagnostics Script.

Generates persistence, frequency, matrix placeholders, ambiguity, continuity, and stability diagnostics.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.state_persistence_diagnostics import (
    build_state_persistence_diagnostics_report,
)
from advanced_regime_transition.state_transition_frequency import (
    build_state_transition_frequency_report,
)
from advanced_regime_transition.state_transition_matrix_placeholders import (
    build_state_transition_matrix_placeholder_registry,
)
from advanced_regime_transition.state_transition_ambiguity import (
    build_state_transition_ambiguity_report,
)
from advanced_regime_transition.state_transition_continuity import (
    build_state_transition_continuity_report,
)
from advanced_regime_transition.state_transition_stability import (
    build_state_transition_stability_report,
)
from advanced_regime_transition.regime_transition_report_builder import (
    build_state_transition_diagnostics_markdown_report,
)
from reports.report_builder import build_state_transition_diagnostics_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_transition_profile()

    df_pers, s_pers = build_state_persistence_diagnostics_report(profile)
    df_freq, s_freq = build_state_transition_frequency_report(profile)
    df_mat, s_mat = build_state_transition_matrix_placeholder_registry(profile)
    df_amb, s_amb = build_state_transition_ambiguity_report(profile)
    df_cont, s_cont = build_state_transition_continuity_report(profile)
    df_stab, s_stab = build_state_transition_stability_report(profile)

    data_lake.save_state_persistence_diagnostics_report(df_pers, s_pers)
    data_lake.save_state_transition_frequency_report(df_freq, s_freq)
    data_lake.save_state_transition_matrix_placeholder_registry(df_mat, s_mat)
    data_lake.save_state_transition_ambiguity_report(df_amb, s_amb)
    data_lake.save_state_transition_continuity_report(df_cont, s_cont)
    data_lake.save_state_transition_stability_report(df_stab, s_stab)

    md_content = build_state_transition_diagnostics_markdown_report(s_pers, df_pers)
    txt_content = build_state_transition_diagnostics_text_report(s_pers, df_pers)

    out_dir = Path("reports/output/advanced_regime_transition")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "state_transition_diagnostics.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    with open(out_dir / "state_transition_diagnostics.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)

    print("=" * 70)
    print("PHASE 130: STATE TRANSITION & STABILITY DIAGNOSTICS")
    print("=" * 70)
    print(f"Persistence States : {s_pers.get('total_analyzed_states', len(df_pers))}")
    print(f"Transition Pairs   : {s_freq.get('total_transition_pairs', len(df_freq))}")
    print(f"Matrix Placeholders: {s_mat.get('total_matrix_entries', len(df_mat))}")
    print(f"Ambiguity Analyzed : {s_amb.get('total_ambiguity_records', len(df_amb))}")
    print(f"Continuity Score   : {s_cont.get('mean_continuity_score', 0.0):.4f}")
    print(f"Stability Score    : {s_stab.get('mean_stability_score', 0.0):.4f}")
    print(f"Non-Signal         : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
