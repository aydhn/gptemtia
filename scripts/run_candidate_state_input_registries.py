"""Phase 128: Run Candidate State Input Registries Script.

Generates candidate feature sets, context, metadata, and dependencies.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_rule_free.regime_rule_free_config import (
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_candidate_feature_sets import (
    build_regime_candidate_feature_set_registry,
)
from advanced_regime_rule_free.regime_candidate_state_context import (
    build_regime_candidate_state_context_registry,
)
from advanced_regime_rule_free.regime_candidate_state_metadata import (
    build_regime_candidate_state_metadata_registry,
)
from advanced_regime_rule_free.regime_candidate_state_quality_dependencies import (
    build_regime_candidate_state_quality_dependency_registry,
)
from advanced_regime_rule_free.regime_candidate_state_validation_dependencies import (
    build_regime_candidate_state_validation_dependency_registry,
)
from advanced_regime_rule_free.regime_rule_free_report_builder import (
    build_candidate_state_metadata_markdown_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_rule_free_profile()

    df_cfs, s_cfs = build_regime_candidate_feature_set_registry(profile)
    df_ctx, s_ctx = build_regime_candidate_state_context_registry(profile)
    df_meta, s_meta = build_regime_candidate_state_metadata_registry(profile)
    df_qd, s_qd = build_regime_candidate_state_quality_dependency_registry(profile)
    df_vd, s_vd = build_regime_candidate_state_validation_dependency_registry(profile)

    data_lake.save_regime_candidate_feature_set_registry(df_cfs, s_cfs)
    data_lake.save_regime_candidate_state_context_registry(df_ctx, s_ctx)
    data_lake.save_regime_candidate_state_metadata_registry(df_meta, s_meta)
    data_lake.save_regime_candidate_state_quality_dependency_registry(df_qd, s_qd)
    data_lake.save_regime_candidate_state_validation_dependency_registry(df_vd, s_vd)

    md_meta = build_candidate_state_metadata_markdown_report(s_meta, df_meta)

    out_dir = Path("reports/output/advanced_regime_rule_free")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "candidate_state_metadata.md", "w", encoding="utf-8") as f:
        f.write(md_meta)

    print("=" * 70)
    print("PHASE 128: CANDIDATE FEATURE SETS & STATE METADATA")
    print("=" * 70)
    print(f"Total Feature Sets     : {s_cfs['total_feature_sets']}")
    print(f"Total Candidate Features: {s_cfs['total_candidate_features']}")
    print(f"Total State Contexts   : {s_ctx['total_candidate_contexts']}")
    print(f"Total Metadata Records : {s_meta['total_candidate_metadata_records']}")
    print(f"Quality Dependencies   : {s_qd['total_quality_dependencies']}")
    print(f"Validation Dependencies: {s_vd['total_validation_dependencies']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
