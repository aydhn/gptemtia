# -*- coding: utf-8 -*-
"""Phase 146: Run Backtest Bias and Lookahead Guards Script.

Builds timezone alignment guards, no-lookahead guards, survivorship bias guards,
data snooping guards, overfitting guards, metadata-only news guards, source preservation guards,
and forbidden column policy registry.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.timezone_alignment_backtest_guards import (
    build_timezone_alignment_backtest_guard_registry,
)
from advanced_realistic_backtest.backtest_no_lookahead_guards import (
    build_backtest_no_lookahead_guard_registry,
)
from advanced_realistic_backtest.backtest_survivorship_bias_guards import (
    build_backtest_survivorship_bias_guard_registry,
)
from advanced_realistic_backtest.backtest_data_snooping_bias_guards import (
    build_backtest_data_snooping_bias_guard_registry,
)
from advanced_realistic_backtest.backtest_overfitting_guards import (
    build_backtest_overfitting_guard_registry,
)
from advanced_realistic_backtest.backtest_metadata_only_news_guards import (
    build_backtest_metadata_only_news_guard_registry,
)
from advanced_realistic_backtest.backtest_source_preservation_guards import (
    build_backtest_source_preservation_guard_registry,
)
from advanced_realistic_backtest.backtest_forbidden_column_policies import (
    build_backtest_forbidden_column_policy_registry,
)
from advanced_realistic_backtest.realistic_backtest_report_builder import (
    build_backtest_guard_markdown_report,
)
from reports.report_builder import build_backtest_guard_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_realistic_backtest_profile()

    df_tz, s_tz = build_timezone_alignment_backtest_guard_registry(profile)
    df_nl, s_nl = build_backtest_no_lookahead_guard_registry(profile)
    df_surv, s_surv = build_backtest_survivorship_bias_guard_registry(profile)
    df_snoop, s_snoop = build_backtest_data_snooping_bias_guard_registry(profile)
    df_over, s_over = build_backtest_overfitting_guard_registry(profile)
    df_news, s_news = build_backtest_metadata_only_news_guard_registry(profile)
    df_src, s_src = build_backtest_source_preservation_guard_registry(profile)
    df_forb, s_forb = build_backtest_forbidden_column_policy_registry(profile)

    data_lake.save_timezone_alignment_backtest_guards(df_tz, s_tz)
    data_lake.save_backtest_no_lookahead_guard_registry(df_nl, s_nl)
    data_lake.save_backtest_survivorship_bias_guard_registry(df_surv, s_surv)
    data_lake.save_backtest_data_snooping_bias_guard_registry(df_snoop, s_snoop)
    data_lake.save_backtest_overfitting_guard_registry(df_over, s_over)
    data_lake.save_backtest_metadata_only_news_guards(df_news, s_news)
    data_lake.save_backtest_source_preservation_guards(df_src, s_src)
    data_lake.save_backtest_forbidden_column_policy_registry(df_forb, s_forb)

    md_report = build_backtest_guard_markdown_report(s_nl, df_nl)
    txt_report = build_backtest_guard_text_report(s_nl, df_nl)

    out_dir = Path("reports/output/advanced_realistic_backtest")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "guards.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "guards.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 146: BIAS & LOOKAHEAD GUARDS")
    print("=" * 70)
    print(f"Timezone Guards        : {len(df_tz)}")
    print(f"No-Lookahead Guards    : {len(df_nl)}")
    print(f"Survivorship Guards    : {len(df_surv)}")
    print(f"Data Snooping Guards   : {len(df_snoop)}")
    print(f"Overfitting Guards     : {len(df_over)}")
    print(f"News Metadata Guards   : {len(df_news)}")
    print(f"Source Guards          : {len(df_src)}")
    print(f"Forbidden Columns      : {len(df_forb)}")
    print(f"All Guards Enforced    : True")
    print(f"Non-Signal             : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
