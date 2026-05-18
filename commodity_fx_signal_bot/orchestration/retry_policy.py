"""
Defines retry logic for failed jobs in the pipeline.
"""

from dataclasses import dataclass
from typing import List, Tuple
import time
import logging
from orchestration.orchestration_config import OrchestrationProfile
from orchestration.orchestration_models import JobExecutionResult

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class RetryPolicy:
    enabled: bool
    max_retries: int
    delay_seconds: float
    retryable_statuses: Tuple[str, ...] = ("job_failed",)

def build_retry_policy(profile: OrchestrationProfile) -> RetryPolicy:
    return RetryPolicy(
        enabled=profile.retry_failed_jobs,
        max_retries=profile.max_retries,
        delay_seconds=profile.retry_delay_seconds
    )

def should_retry_job(result: JobExecutionResult, policy: RetryPolicy) -> bool:
    if not policy.enabled:
        return False
    if result.status not in policy.retryable_statuses:
        return False
    if result.attempts > policy.max_retries:
        return False
    return True

def apply_retry_delay(policy: RetryPolicy) -> None:
    if policy.delay_seconds > 0:
        logger.info(f"Applying retry delay of {policy.delay_seconds} seconds")
        time.sleep(policy.delay_seconds)

def summarize_retry_plan(results: List[JobExecutionResult], policy: RetryPolicy) -> dict:
    retry_candidates = [r for r in results if should_retry_job(r, policy)]
    return {
        "policy_enabled": policy.enabled,
        "max_retries": policy.max_retries,
        "candidate_count": len(retry_candidates),
        "candidates": [{"job_id": r.job_id, "symbol": r.symbol} for r in retry_candidates]
    }
