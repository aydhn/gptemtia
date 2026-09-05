"""Phase 128: Run Regime Rule-Free Validation Report Script.

Executes validation suites across Phase 128 tables and generates safety and validation reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_rule_free.regime_rule_free_config import (
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_pipeline import (
    RegimeRuleFreePipeline,
)
from advanced_regime_rule_free.regime_rule_free_report_builder import (
    build_regime_rule_free_validation_markdown_report,
    build_regime_rule_free_safety_markdown_report,
)
from reports.report_builder import (
    build_regime_rule_free_validation_text_report,
    build_regime_rule_free_safety_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_rule_free_profile()
    pipeline = RegimeRuleFreePipeline(data_lake=data_lake, profile=profile)

    tables, summaries = pipeline.build_health_validation_safety_handoff(save=True)

    df_val = tables["validation"]
    s_val = summaries["validation"]
    df_safe = tables["safety"]
    s_safe = summaries["safety"]

    md_val = build_regime_rule_free_validation_markdown_report(s_val, df_val)
    txt_val = build_regime_rule_free_validation_text_report(s_val, df_val)
    md_safe = build_regime_rule_free_safety_markdown_report(s_safe, df_safe)
    txt_safe = build_regime_rule_free_safety_text_report(s_safe, df_safe)

    out_dir = Path("reports/output/advanced_regime_rule_free")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "validation_report.md", "w", encoding="utf-8") as f:
        f.write(md_val)
    with open(out_dir / "validation_report.txt", "w", encoding="utf-8") as f:
        f.write(txt_val)
    with open(out_dir / "safety_boundary.md", "w", encoding="utf-8") as f:
        f.write(md_safe)
    with open(out_dir / "safety_boundary.txt", "w", encoding="utf-8") as f:
        f.write(txt_safe)

    print("=" * 70)
    print("PHASE 128: VALIDATION & SAFETY BOUNDARY REPORT")
    print("=" * 70)
    print(f"Validation Status: {s_val['validation_status']}")
    print(f"Passed Checks    : {s_val['passed_checks']}/{s_val['total_checks']}")
    print(f"Forbidden Clean  : {s_val['forbidden_claims_clean']}")
    print(f"Safety Status    : {s_safe['safety_status']}")
    print(f"NO-GO Rules      : {s_safe['no_go_count']}")
    print(f"SAFE-GO Rules    : {s_safe['safe_go_count']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
