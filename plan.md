1. **Update Settings & Paths:**
    - Update `commodity_fx_signal_bot/config/settings.py` to include quality gate configurations.
    - Update `commodity_fx_signal_bot/.env.example` with the new environment variables.
    - Update `commodity_fx_signal_bot/config/paths.py` to add quality gate directories.

2. **Create Quality Gate Modules:**
    - `quality_gates/__init__.py`
    - `quality_gates/quality_config.py`: Data classes and profiles.
    - `quality_gates/quality_labels.py`: Controlled labels.
    - `quality_gates/quality_models.py`: Data models.
    - `quality_gates/test_discovery.py`: Test file discovery.
    - `quality_gates/test_health.py`: Test execution and summary.
    - `quality_gates/import_graph.py`: Import dependency parsing.
    - `quality_gates/static_safety_scan.py`: Forbidden term scanning.
    - `quality_gates/repo_hygiene.py`: Repo structure validation.
    - `quality_gates/dependency_audit.py`: Package dependency checking.
    - `quality_gates/smoke_tests.py`: Safe command running.
    - `quality_gates/output_contracts.py`: Output folder validation.
    - `quality_gates/documentation_coverage.py`: Documentation completeness.
    - `quality_gates/release_manifest.py`: Release candidate manifest.
    - `quality_gates/release_checklist.py`: Release checklist.
    - `quality_gates/release_notes.py`: Release notes draft generation.
    - `quality_gates/local_ci_runner.py`: Orchestrator for local CI.
    - `quality_gates/quality_report_builder.py`: Markdown report generator.
    - `quality_gates/quality_pipeline.py`: Main quality gate pipeline.

3. **Update Data Lake & Feature Store:**
    - Add quality gate load/save methods to `commodity_fx_signal_bot/data/storage/data_lake.py`.
    - Add load methods to `commodity_fx_signal_bot/ml/feature_store.py`.

4. **Update Report Builder:**
    - Update `commodity_fx_signal_bot/reports/report_builder.py` with text report functions for quality gates.

5. **Create Scripts:**
    - `scripts/run_local_ci_validation.py`
    - `scripts/run_test_health_report.py`
    - `scripts/run_import_graph_report.py`
    - `scripts/run_repo_hygiene_report.py`
    - `scripts/run_dependency_audit_report.py`
    - `scripts/run_static_safety_scan.py`
    - `scripts/run_smoke_test_report.py`
    - `scripts/run_release_candidate_report.py`
    - `scripts/run_release_quality_gate_status.py`

6. **Create Tests:**
    - Write unit tests for all new modules in `tests/test_quality_config.py` through `tests/test_quality_gate_scripts_contract.py`.

7. **Update Documentation:**
    - Update `commodity_fx_signal_bot/README.md`.
    - Update `commodity_fx_signal_bot/docs/ARCHITECTURE.md`.
    - Update `commodity_fx_signal_bot/docs/PHASE_LOG.md`.

8. **Pre-commit Instructions:**
    - Run pre-commit checks.

9. **Submit:**
    - Submit the changes.
