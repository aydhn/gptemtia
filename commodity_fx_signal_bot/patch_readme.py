def update_readme():
    file_path = "README.md"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    readme_insertion = """
## Long-Term Local Maintenance and Sustainability Planning

This project includes a local offline maintenance planner and sustainability review cadence.

**IMPORTANT:**
- The local maintenance planner is **NOT** a production scheduler.
- The periodic review calendar does **NOT** automatically run tasks; it provides a manual review plan for operators.
- The dependency aging watch does **NOT** check for updates over the internet and does **NOT** automatically upgrade dependencies.
- The refresh cadence reports provide a **manual/dry-run** refresh plan.
- The sustainability score is **NOT** an official SLA or health score.
- The maintenance runbook is **NOT** an automatic operation instruction.
- Raw secrets and private data are **never** included in outputs.
- All outputs are saved under `data/lake/local_maintenance` and `reports/output/local_maintenance`.

### Maintenance Commands

```bash
python -m scripts.run_maintenance_domain_registry
python -m scripts.run_periodic_review_calendar
python -m scripts.run_refresh_cadence_report
python -m scripts.run_dependency_aging_watch
python -m scripts.run_maintenance_sustainability_report
python -m scripts.run_maintenance_quality_report
python -m scripts.run_maintenance_status
```
"""

    if "## Long-Term Local Maintenance and Sustainability Planning" not in content:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(readme_insertion)

update_readme()
