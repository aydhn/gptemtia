# -*- coding: utf-8 -*-
"""Phase 151: Run Benchmark Evaluation Profile Registry Script.

Builds and persists Phase 151 benchmark evaluation profile, domain, and scope registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_profile_registry import (
    build_benchmark_evaluation_profile_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_domain_registry import (
    build_benchmark_evaluation_domain_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_scope_registry import (
    build_benchmark_evaluation_scope_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_report_builder import (
    build_benchmark_evaluation_profile_markdown_report,
)
from reports.report_builder import (
    build_benchmark_evaluation_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_benchmark_evaluation_profile()

    df_prof, s_prof = build_benchmark_evaluation_profile_registry(profile)
    df_dom, s_dom = build_benchmark_evaluation_domain_registry(profile)
    df_scope, s_scope = build_benchmark_evaluation_scope_registry(profile)

    data_lake.save_benchmark_evaluation_profile_registry(df_prof, s_prof)
    data_lake.save_benchmark_evaluation_domain_registry(df_dom, s_dom)
    data_lake.save_benchmark_evaluation_scope_registry(df_scope, s_scope)

    out_dir = Path("reports/output/advanced_benchmark_evaluation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "profiles.md", "w", encoding="utf-8") as f:
        f.write(build_benchmark_evaluation_profile_markdown_report(s_prof, df_prof))
    with open(out_dir / "profiles.txt", "w", encoding="utf-8") as f:
        f.write(build_benchmark_evaluation_text_report(s_prof, df_prof))

    print("Phase 151 benchmark evaluation profiles, domains, and scopes successfully built.")


if __name__ == "__main__":
    main()
