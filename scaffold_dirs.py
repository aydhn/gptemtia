import os
from pathlib import Path

# Create directories
paths = [
    "data/lake/advanced_economic_calendar/profiles",
    "data/lake/advanced_economic_calendar/domains",
    "data/lake/advanced_economic_calendar/events",
    "data/lake/advanced_economic_calendar/categories",
    "data/lake/advanced_economic_calendar/importance",
    "data/lake/advanced_economic_calendar/mapping",
    "data/lake/advanced_economic_calendar/schemas",
    "data/lake/advanced_economic_calendar/surprise",
    "data/lake/advanced_economic_calendar/time_normalization",
    "data/lake/advanced_economic_calendar/revision_handling",
    "data/lake/advanced_economic_calendar/capabilities",
    "data/lake/advanced_economic_calendar/metadata",
    "data/lake/advanced_economic_calendar/request_response",
    "data/lake/advanced_economic_calendar/contracts",
    "data/lake/advanced_economic_calendar/registry",
    "data/lake/advanced_economic_calendar/resolver",
    "data/lake/advanced_economic_calendar/preferences",
    "data/lake/advanced_economic_calendar/matcher",
    "data/lake/advanced_economic_calendar/dry_run",
    "data/lake/advanced_economic_calendar/placeholders",
    "data/lake/advanced_economic_calendar/output_validation",
    "data/lake/advanced_economic_calendar/safety",
    "data/lake/advanced_economic_calendar/health",
    "data/lake/advanced_economic_calendar/scoring",
    "data/lake/advanced_economic_calendar/validation",
    "data/lake/advanced_economic_calendar/quality",
    "reports/output/advanced_economic_calendar/csv",
    "reports/output/advanced_economic_calendar/markdown",
    "reports/output/advanced_economic_calendar/txt",
    "reports/output/advanced_economic_calendar/json",
    "docs/generated/advanced_economic_calendar/registry",
    "docs/generated/advanced_economic_calendar/events",
    "docs/generated/advanced_economic_calendar/contracts",
    "docs/generated/advanced_economic_calendar/dry_run",
    "docs/generated/advanced_economic_calendar/health",
    "docs/generated/advanced_economic_calendar/quality",
    "docs/generated/advanced_economic_calendar/handoff",
    "advanced_economic_calendar",
    "scripts",
    "tests"
]

for p in paths:
    Path(p).mkdir(parents=True, exist_ok=True)

# Append to config/paths.py
with open("config/paths.py", "a", encoding="utf-8") as f:
    f.write("\n\n# Phase 110 Paths\n")
    f.write("def ensure_project_directories():\n")
    f.write("    pass\n")
    for p in paths:
        f.write(f"    # {p}\n")

print("Directories created.")
