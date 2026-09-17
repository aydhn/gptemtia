# -*- coding: utf-8 -*-
"""Phase 150: Run Backtest Governance Guards Script.

Builds and persists source preservation, metadata-only news, and forbidden column policy registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_source_preservation_guards import (
    build_backtest_source_preservation_guard_registry,
)
from advanced_backtest_governance.backtest_metadata_only_news_guards import (
    build_backtest_metadata_only_news_guard_registry,
)
from advanced_backtest_governance.backtest_forbidden_column_policies import (
    build_backtest_forbidden_column_policy_registry,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_governance_profile()

    df_src, s_src = build_backtest_source_preservation_guard_registry(profile)
    df_news, s_news = build_backtest_metadata_only_news_guard_registry(profile)
    df_forb, s_forb = build_backtest_forbidden_column_policy_registry(profile)

    data_lake.save_backtest_source_preservation_guards(df_src, s_src)
    data_lake.save_backtest_metadata_only_news_guards(df_news, s_news)
    data_lake.save_backtest_forbidden_column_policies(df_forb, s_forb)

    print("Phase 150 governance guards successfully built and saved.")


if __name__ == "__main__":
    main()
