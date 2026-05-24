from pathlib import Path

# Update README.md
readme = Path("README.md")
readme_content = readme.read_text()

if "Adaptive Research Planning and Backlog" not in readme_content:
    readme_insert = """
## Adaptive Research Planning and Backlog (Phase 48)

The project includes an offline research planning layer that generates automated research tasks, priority scores, and next-best-experiment recommendations based on outputs from the governance, validation, observability, and other modules.

- Research planning is not a live scheduler.
- The backlog is a list of research tasks; it does not trigger automatic execution.
- Priority scores are not live trading priorities.
- Next-best-experiment recommendations do not automatically start experiments.
- Research debt indicates maintenance risks, not trade alarms.
- Roadmap health reflects offline research capacity, not production readiness.
- Outputs are saved in `data/lake/research_planning` and `reports/output/research_planning`.

### Generating Planning Reports

```bash
python -m scripts.run_research_backlog_report --timeframe 1d
python -m scripts.run_priority_scoring_report --timeframe 1d
python -m scripts.run_next_best_experiment_report --timeframe 1d
python -m scripts.run_research_debt_report --timeframe 1d
python -m scripts.run_roadmap_health_report --timeframe 1d
python -m scripts.run_research_planning_status
```
"""
    readme_content += readme_insert
    readme.write_text(readme_content)
    print("Updated README.md")

# Update ARCHITECTURE.md
arch = Path("docs/ARCHITECTURE.md")
arch_content = arch.read_text()

if "PlanningSignalCollector" not in arch_content:
    arch_insert = """
## Phase 48: Adaptive Research Planning

The architecture includes a comprehensive offline research planning pipeline:

Governance / Experiments / Meta / Factor / Synthetic Index / Portfolio / Regime / Validation / ML / Paper / Observability
→ `PlanningSignalCollector`
→ `BacklogBuilder`
→ `PriorityScoring`
→ `NextBestExperiment`
→ `ResearchDebt`
→ `ResearchOpportunities`
→ `RoadmapHealth`
→ `TaskDependencies`
→ `MilestoneTracking`
→ `OfflineTaskOrchestrationPlan`
→ `PlanningQuality`
→ Research Planning Reports
"""
    arch_content += arch_insert
    arch.write_text(arch_content)
    print("Updated ARCHITECTURE.md")

# Update PHASE_LOG.md
log = Path("docs/PHASE_LOG.md")
log_content = log.read_text()

if "Phase 48:" not in log_content:
    log_insert = """
### Phase 48: Adaptive Research Planning
- Research planning profile sistemi eklendi.
- Planning label registry eklendi.
- ResearchSignal, ResearchTask, NextBestExperiment ve RoadmapHealthSnapshot modelleri eklendi.
- PlanningSignalCollector eklendi.
- ResearchTaskRegistry eklendi.
- BacklogBuilder eklendi.
- PriorityScoring eklendi.
- Next-best-experiment öneri sistemi eklendi.
- ResearchDebt raporu eklendi.
- ResearchOpportunities raporu eklendi.
- RoadmapHealth snapshot eklendi.
- TaskDependencies eklendi.
- MilestoneTracking eklendi.
- Offline Task Orchestration Plan eklendi.
- PlanningQuality report eklendi.
- ResearchPlanningPipeline eklendi.
- DataLake research planning kayıt desteği aldı.
- Research planning scriptleri eklendi.
- Testler genişletildi.
"""
    log_content += log_insert
    log.write_text(log_content)
    print("Updated PHASE_LOG.md")
