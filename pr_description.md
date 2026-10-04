🧹 Fix empty exception handling in data quality rules

🎯 **What:** Modified three files in `advanced_data_quality` (`timestamp_integrity_rules.py`, `event_release_consistency_rules.py`, `data_quality_report_builder.py`) to properly handle exceptions in `try/except Exception:` blocks.

💡 **Why:** Previous implementation contained blind `except Exception: pass` blocks which swallowed unexpected errors during critical data quality checks and markdown report rendering. The new implementation correctly logs exceptions by creating explicit `QualityFinding` objects on failure so issues can be audited and corrected (Phase 113). In `data_quality_report_builder`, the exception variable was captured explicitly as `exc` but continues to gracefully fallback to manual string joining since it is used as a fallback for missing tabulate package. These changes improve observability and maintainability by surfacing silent errors.

✅ **Verification:** Ran `python -m pytest tests/test_timestamp_integrity_rules.py`, `tests/test_advanced_data_quality_scripts_contract.py`, and other advanced data quality tests. Formatted the updated files with `ruff` and ran `pre-commit` steps.

✨ **Result:** Better error tracking and visibility when processing dirty data frames, and overall improved system resilience without crashing during pipeline checks.
