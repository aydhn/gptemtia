"""Phase 135: Run Regime Acceptance Validation Report Script.

Validates all registries, gates, manifest, and safety rules, persisting results to DataLake.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_regime_acceptance.regime_acceptance_config import (
    get_default_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_profile_registry import (
    build_regime_acceptance_profile_registry,
)
from advanced_regime_acceptance.regime_block_inventory import (
    build_regime_block_inventory_report,
)
from advanced_regime_acceptance.regime_block_acceptance_gates import (
    build_regime_block_acceptance_gate_registry,
)
from advanced_regime_acceptance.phase_126_135_acceptance_manifest import (
    build_phase_126_135_acceptance_manifest,
)
from advanced_regime_acceptance.regime_acceptance_validation import (
    build_regime_acceptance_validation_report,
)
from advanced_regime_acceptance.regime_acceptance_report_builder import (
    build_regime_validation_markdown_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_regime_acceptance_profile()

    df_prof, _ = build_regime_acceptance_profile_registry(profile)
    df_inv, _ = build_regime_block_inventory_report(profile)
    df_gates, _ = build_regime_block_acceptance_gate_registry(profile)
    df_man, _ = build_phase_126_135_acceptance_manifest(profile)

    tables = {
        "profiles": df_prof,
        "inventory": df_inv,
        "gates": df_gates,
        "manifest": df_man,
    }

    df_val, s_val = build_regime_acceptance_validation_report(tables, profile)
    data_lake.save_regime_acceptance_validation_report(df_val, s_val)

    md_val = build_regime_validation_markdown_report(s_val, df_val)

    out_dir = Path("reports/output/advanced_regime_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "validation.md", "w", encoding="utf-8") as f:
        f.write(md_val)

    print("=" * 70)
    print("PHASE 135: REGIME ACCEPTANCE VALIDATION REPORT")
    print("=" * 70)
    print(f"Total Validations  : {s_val['total_validations']}")
    print(f"Passed Validations : {s_val['passed_validations']}")
    print(f"All Passed         : {s_val['all_passed']}")
    print(f"Status             : {s_val['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
