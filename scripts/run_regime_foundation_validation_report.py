"""Phase 126: Run Regime Foundation Validation and Safety Report Script.

Generates validation and safety boundary compliance reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_foundation.regime_foundation_config import (
    get_default_regime_foundation_profile,
)
from advanced_regime_foundation.regime_foundation_safety_boundary import (
    build_regime_foundation_safety_boundary,
)
from advanced_regime_foundation.regime_foundation_validation import (
    build_regime_foundation_validation_report,
)
from advanced_regime_foundation.regime_foundation_pipeline import (
    RegimeFoundationPipeline,
)
from advanced_regime_foundation.regime_foundation_report_builder import (
    build_regime_validation_markdown_report,
    build_regime_safety_markdown_report,
)
from reports.report_builder import (
    build_regime_validation_text_report,
    build_regime_safety_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_foundation_profile()
    pipeline = RegimeFoundationPipeline(data_lake=data_lake, profile=profile)

    df_safety, s_safety = build_regime_foundation_safety_boundary(profile)
    data_lake.save_regime_foundation_safety_boundary(df_safety, s_safety)

    t_prof, _ = pipeline.build_profiles_domains_taxonomy(save=False)
    t_fam, _ = pipeline.build_regime_families(save=False)
    t_man, _ = pipeline.build_manifest_policies(save=False)
    val_inputs = {**t_prof, **t_fam, **t_man}

    df_val, s_val = build_regime_foundation_validation_report(val_inputs, profile)
    data_lake.save_regime_foundation_validation_report(df_val, s_val)

    md_safety = build_regime_safety_markdown_report(s_safety, df_safety)
    md_val = build_regime_validation_markdown_report(s_val, df_val)
    txt_safety = build_regime_safety_text_report(s_safety, df_safety)
    txt_val = build_regime_validation_text_report(s_val, df_val)

    out_dir = Path("reports/output/advanced_regime_foundation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "safety_boundary_report.md", "w", encoding="utf-8") as f:
        f.write(md_safety)
    with open(out_dir / "safety_boundary_report.txt", "w", encoding="utf-8") as f:
        f.write(txt_safety)
    with open(out_dir / "validation_report.md", "w", encoding="utf-8") as f:
        f.write(md_val)
    with open(out_dir / "validation_report.txt", "w", encoding="utf-8") as f:
        f.write(txt_val)

    print("=" * 70)
    print("PHASE 126: VALIDATION & SAFETY BOUNDARY REPORT")
    print("=" * 70)
    print(f"Validation Stat: {s_val['validation_status']}")
    print(f"Passed Rules   : {s_val['passed_rules']}/{s_val['total_rules']}")
    print(f"Claims Clean   : {s_val['forbidden_claims_clean']}")
    print(f"Safety Status  : {s_safety['safety_status']}")
    print(f"NO-GO Rules    : {s_safety['no_go_count']}")
    print(f"SAFE-GO Rules  : {s_safety['safe_go_count']}")
    print(f"Non-Signal     : {s_val['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
