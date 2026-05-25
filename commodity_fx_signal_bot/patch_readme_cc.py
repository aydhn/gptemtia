import re

with open("commodity_fx_signal_bot/README.md", "r") as f:
    content = f.read()

cc_section = """
## Offline Analyst Command Center (Phase 50)

The Offline Analyst Command Center aggregates all offline research, reporting, knowledge base, governance, experiment, and planning layers into safe command catalogs, guided workflows, safe runbooks, dry-run plans, project status, module health, script discovery, phase coverage, and project consolidation reports.

**Important Note:** The Command Center is NOT a live trading terminal.
- Safe command catalogs only list offline report, status, and query commands.
- Guided workflows do not auto-execute commands.
- Runbooks do not contain live execution or deployment instructions.
- Dry-run plans do not run commands; they only produce safe plans.
- Project consolidation is not production readiness.
- Analyst command queries only suggest safe offline commands.
- Outputs are saved under `data/lake/command_center` and `reports/output/command_center`.

**Available Commands:**
```bash
python -m scripts.run_command_catalog_report
python -m scripts.run_guided_workflow_report
python -m scripts.run_safe_runbook_report
python -m scripts.run_project_status_report
python -m scripts.run_project_consolidation_report
python -m scripts.run_analyst_command_query --query "GC=F için hangi raporları çalıştırmalıyım?"
python -m scripts.run_command_center_status
```
"""

content = content + "\n\n" + cc_section

with open("commodity_fx_signal_bot/README.md", "w") as f:
    f.write(content)
