import os
from pathlib import Path

ROOT_DIR = Path("C:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia")

paths_content = """
# Phase 105 Paths
data/lake/advanced_gap_closure/
data/lake/advanced_gap_closure/profiles/
data/lake/advanced_gap_closure/reconciliation/
data/lake/advanced_gap_closure/closure_matrix/
data/lake/advanced_gap_closure/foundation_audit/
data/lake/advanced_gap_closure/dependency_closure/
data/lake/advanced_gap_closure/missing_functionality/
data/lake/advanced_gap_closure/backlog/
data/lake/advanced_gap_closure/phase_106_handoff/
data/lake/advanced_gap_closure/data_provider_requirements/
data/lake/advanced_gap_closure/no_scraping_boundary/
data/lake/advanced_gap_closure/provider_interface_readiness/
data/lake/advanced_gap_closure/data_quality_readiness/
data/lake/advanced_gap_closure/profile_data_requirements/
data/lake/advanced_gap_closure/contract_handoff/
data/lake/advanced_gap_closure/no_go_safe_go/
data/lake/advanced_gap_closure/risks/
data/lake/advanced_gap_closure/scoring/
data/lake/advanced_gap_closure/validation/
data/lake/advanced_gap_closure/quality/

reports/output/advanced_gap_closure/
reports/output/advanced_gap_closure/csv/
reports/output/advanced_gap_closure/markdown/
reports/output/advanced_gap_closure/txt/
reports/output/advanced_gap_closure/json/

docs/generated/advanced_gap_closure/
docs/generated/advanced_gap_closure/reconciliation/
docs/generated/advanced_gap_closure/closure_matrix/
docs/generated/advanced_gap_closure/audit/
docs/generated/advanced_gap_closure/handoff/
docs/generated/advanced_gap_closure/quality/

def ensure_project_directories():
    pass
"""

with open(ROOT_DIR / "config/paths.py", "a", encoding="utf-8") as f:
    f.write("\n" + paths_content + "\n")

print("Appended paths to paths.py")
