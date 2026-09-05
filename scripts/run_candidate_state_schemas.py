"""Phase 128: Run Candidate State Schemas Script.

Generates candidate state schema, pseudo-state schema, and namespace registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_rule_free.regime_rule_free_config import (
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.candidate_state_schema import (
    build_candidate_state_schema_registry,
)
from advanced_regime_rule_free.pseudo_state_schema import (
    build_pseudo_state_schema_registry,
)
from advanced_regime_rule_free.regime_candidate_state_namespace import (
    build_regime_candidate_state_namespace_registry,
)
from advanced_regime_rule_free.regime_rule_free_report_builder import (
    build_candidate_state_schema_markdown_report,
)
from reports.report_builder import build_candidate_state_schema_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_rule_free_profile()

    df_cs, s_cs = build_candidate_state_schema_registry(profile)
    df_ps, s_ps = build_pseudo_state_schema_registry(profile)
    df_ns, s_ns = build_regime_candidate_state_namespace_registry(profile)

    data_lake.save_candidate_state_schema_registry(df_cs, s_cs)
    data_lake.save_pseudo_state_schema_registry(df_ps, s_ps)
    data_lake.save_regime_candidate_state_namespace_registry(df_ns, s_ns)

    md_cs = build_candidate_state_schema_markdown_report(s_cs, df_cs)
    txt_cs = build_candidate_state_schema_text_report(s_cs, df_cs)

    out_dir = Path("reports/output/advanced_regime_rule_free")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "candidate_state_schema.md", "w", encoding="utf-8") as f:
        f.write(md_cs)
    with open(out_dir / "candidate_state_schema.txt", "w", encoding="utf-8") as f:
        f.write(txt_cs)

    print("=" * 70)
    print("PHASE 128: CANDIDATE & PSEUDO-STATE SCHEMAS")
    print("=" * 70)
    print(f"Total Schema Fields: {s_cs['total_schema_fields']}")
    print(f"Schema Status      : {s_cs['schema_status']}")
    print(f"Total Pseudo States: {s_ps['total_pseudo_states']}")
    print(f"Pseudo Status      : {s_ps['schema_status']}")
    print(f"Namespace Rules    : {s_ns['total_namespace_rules']}")
    print(f"All Non-Signal     : {s_cs['all_non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
