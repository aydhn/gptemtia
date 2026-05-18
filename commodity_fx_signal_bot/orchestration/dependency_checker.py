"""
Checks job and workflow dependencies in the DataLake.
"""

from typing import List, Tuple, Dict, Optional
import pandas as pd
from data.storage.data_lake import DataLake
from orchestration.orchestration_models import PipelineJob

class DependencyChecker:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def _check_dependency_exists(self, dep_name: str, symbol: Optional[str], timeframe: str) -> bool:
        """
        Check if a logical dependency exists in DataLake/Storage.
        This is a simplified check based on expected output names.
        """
        # Data Lake checks mapping
        # These are abstract names that jobs output/depend on
        # You'd map these to specific DataLake functions or file paths

        # Example mapping logic (simplified for stub)
        if dep_name == "processed_ohlcv":
             if symbol:
                 return self.data_lake.has_processed_data(symbol, timeframe)
             return False # Unlikely to require processed_ohlcv without symbol
        elif dep_name == "technical_features":
             if symbol:
                 return self.data_lake.has_feature_data(symbol, timeframe, "technical")
             return False
        # Add other mappings as needed. For now, default to True if we don't have a specific check
        # This allows the orchestration to proceed without blocking on every unknown dependency during initial development.

        return True

    def check_job_dependencies(
        self,
        job: PipelineJob,
        symbol: Optional[str],
        timeframe: str,
    ) -> dict:

        missing_req = []
        missing_opt = []

        for dep in job.dependencies:
             if not self._check_dependency_exists(dep, symbol, timeframe):
                  missing_req.append(dep)

        for dep in job.optional_dependencies:
             if not self._check_dependency_exists(dep, symbol, timeframe):
                  missing_opt.append(dep)

        status = "dependency_available"
        if missing_req:
             status = "dependency_missing"
        elif missing_opt:
             status = "dependency_optional_missing"

        return {
             "job_id": job.job_id,
             "symbol": symbol,
             "status": status,
             "missing_required": missing_req,
             "missing_optional": missing_opt
        }

    def check_workflow_dependencies(
        self,
        jobs: List[PipelineJob],
        symbols: List[str],
        timeframe: str,
    ) -> Tuple[pd.DataFrame, dict]:

        results = []

        for job in jobs:
            # Check for each symbol if it's a symbol-level job
            # We assume a job needs symbols if it's not a universe job
            # For simplicity in this checker, we check all provided symbols

            # If no symbols provided (e.g. universe level), check with None
            if not symbols:
                 res = self.check_job_dependencies(job, None, timeframe)
                 results.append(res)
            else:
                 for symbol in symbols:
                      res = self.check_job_dependencies(job, symbol, timeframe)
                      results.append(res)

        if not results:
             df = pd.DataFrame(columns=["job_id", "symbol", "status", "missing_required", "missing_optional"])
        else:
             df = pd.DataFrame(results)

        summary = {
            "total_checks": len(results),
            "missing_count": len([r for r in results if r["status"] == "dependency_missing"]),
            "optional_missing_count": len([r for r in results if r["status"] == "dependency_optional_missing"]),
            "available_count": len([r for r in results if r["status"] == "dependency_available"])
        }

        return df, summary

    def check_expected_outputs(
        self,
        job: PipelineJob,
        symbol: Optional[str],
        timeframe: str,
    ) -> dict:

        missing_outputs = []
        for out in job.expected_outputs:
             if not self._check_dependency_exists(out, symbol, timeframe):
                  missing_outputs.append(out)

        return {
            "job_id": job.job_id,
            "symbol": symbol,
            "all_outputs_present": len(missing_outputs) == 0,
            "missing_outputs": missing_outputs
        }
