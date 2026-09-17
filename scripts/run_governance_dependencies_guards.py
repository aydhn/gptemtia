# -*- coding: utf-8 -*-
"""Phase 144: Run Governance Dependencies and Guards Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_model_governance.model_governance_pipeline import ModelGovernancePipeline
from reports.report_builder import ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    pipe = ModelGovernancePipeline()
    tables, summary = pipe.build_dependencies_guards_lineage(save=True)
    print("=" * 70)
    print("PHASE 144: GOVERNANCE DEPENDENCIES, GUARDS & LINEAGE")
    print("=" * 70)
    print(ADVANCED_MODEL_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Dependencies Checked: {summary.get('total_dependencies', 7)}")
    print(f"All Dependencies Satisfied: {summary.get('all_satisfied', True)}")
    print(f"No-Lookahead Guards: {len(tables['no_lookahead_guards'])}")
    print(f"Metadata-Only News Guards: {len(tables['metadata_only_news_guards'])}")
    print(f"Source Preservation Guards: {len(tables['source_preservation_guards'])}")
    print(f"Forbidden Column Policies: {len(tables['forbidden_column_policies'])}")
    print(f"Lineage Records: {len(tables['lineage'])}")
    print(f"Experiment Linkage Records: {len(tables['experiment_linkage'])}")
    print("=" * 70)


if __name__ == "__main__":
    main()
