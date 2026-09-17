# -*- coding: utf-8 -*-
"""Phase 144: Run Model Governance Profile Registry Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_model_governance.model_governance_pipeline import ModelGovernancePipeline
from reports.report_builder import ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    pipe = ModelGovernancePipeline()
    tables, summary = pipe.build_profiles_domains(save=True)
    print("=" * 70)
    print("PHASE 144: MODEL GOVERNANCE PROFILE & DOMAIN REGISTRY")
    print("=" * 70)
    print(ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Profiles: {summary['profiles_summary']['total_profiles']}")
    print(f"Total Domains: {summary['domains_summary']['total_domains']}")
    print(f"Active Profile: {summary['profiles_summary']['active_profile']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
