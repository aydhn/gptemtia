"""Phase 126: Run Regime Contracts and Dependencies Script.

Generates feature contracts, factor/val/qual dependencies, output schema, and namespace registry.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_foundation.regime_foundation_config import (
    get_default_regime_foundation_profile,
)
from advanced_regime_foundation.regime_input_feature_contracts import (
    build_regime_input_feature_contract_registry,
)
from advanced_regime_foundation.regime_factor_dependencies import (
    build_regime_factor_dependency_registry,
)
from advanced_regime_foundation.regime_validation_dependencies import (
    build_regime_validation_dependency_registry,
)
from advanced_regime_foundation.regime_quality_dependencies import (
    build_regime_quality_dependency_registry,
)
from advanced_regime_foundation.regime_state_output_schema import (
    build_regime_state_output_schema_registry,
)
from advanced_regime_foundation.regime_namespace_registry import (
    build_regime_namespace_registry,
)
from advanced_regime_foundation.regime_foundation_report_builder import (
    build_regime_contract_dependency_markdown_report,
)
from reports.report_builder import (
    build_regime_contract_dependency_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_foundation_profile()

    df_cont, s_cont = build_regime_input_feature_contract_registry(profile)
    df_fact, s_fact = build_regime_factor_dependency_registry(profile)
    df_val, s_val = build_regime_validation_dependency_registry(profile)
    df_qual, s_qual = build_regime_quality_dependency_registry(profile)
    df_schema, s_schema = build_regime_state_output_schema_registry(profile)
    df_ns, s_ns = build_regime_namespace_registry(profile)

    data_lake.save_regime_input_feature_contract_registry(df_cont, s_cont)
    data_lake.save_regime_factor_dependency_registry(df_fact, s_fact)
    data_lake.save_regime_validation_dependency_registry(df_val, s_val)
    data_lake.save_regime_quality_dependency_registry(df_qual, s_qual)
    data_lake.save_regime_state_output_schema_registry(df_schema, s_schema)
    data_lake.save_regime_namespace_registry(df_ns, s_ns)

    md_cont = build_regime_contract_dependency_markdown_report(s_cont, df_cont)
    md_fact = build_regime_contract_dependency_markdown_report(s_fact, df_fact)
    txt_cont = build_regime_contract_dependency_text_report(s_cont, df_cont)

    out_dir = Path("reports/output/advanced_regime_foundation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "input_feature_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_cont)
    with open(out_dir / "factor_dependencies.md", "w", encoding="utf-8") as f:
        f.write(md_fact)
    with open(out_dir / "contracts_dependencies.txt", "w", encoding="utf-8") as f:
        f.write(txt_cont)

    print("=" * 70)
    print("PHASE 126: REGIME CONTRACTS & DEPENDENCIES")
    print("=" * 70)
    print(f"Total Contracts: {s_cont['total_contracts']}")
    print(f"Factor Deps    : {s_fact['total_dependencies']}")
    print(f"Val Rules      : {s_val['total_rules']}")
    print(f"Qual Metrics   : {s_qual['total_metrics']}")
    print(f"Schema Fields  : {s_schema['total_fields']}")
    print(f"Namespaces     : {s_ns['total_namespaces']}")
    print(f"Non-Signal     : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
