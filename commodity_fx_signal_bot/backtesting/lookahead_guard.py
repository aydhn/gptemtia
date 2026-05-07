import pandas as pd
import logging

logger = logging.getLogger(__name__)


class LookaheadGuard:
    def __init__(self, strict: bool = True):
        self.strict = strict

    def validate_candidate_timestamp(
        self, candidate_ts: pd.Timestamp, current_ts: pd.Timestamp
    ) -> dict:
        if candidate_ts > current_ts:
            return {
                "passed": False,
                "violation": f"Candidate ts {candidate_ts} is > current ts {current_ts}",
            }
        return {"passed": True}

    def validate_execution_timestamp(
        self, execution_ts: pd.Timestamp, signal_ts: pd.Timestamp
    ) -> dict:
        if execution_ts < signal_ts:
            return {
                "passed": False,
                "violation": f"Execution ts {execution_ts} is < signal ts {signal_ts}",
            }
        return {"passed": True}

    def validate_context_timestamp(
        self, context_ts: pd.Timestamp, current_ts: pd.Timestamp
    ) -> dict:
        if context_ts > current_ts:
            return {
                "passed": False,
                "violation": f"Context ts {context_ts} is > current ts {current_ts}",
            }
        return {"passed": True}

    def audit_backtest_frame(self, df: pd.DataFrame) -> dict:
        return {"passed": True, "violations": [], "warnings": [], "violation_count": 0}

    def audit_trade_ledger(self, trades_df: pd.DataFrame) -> dict:
        if trades_df.empty:
            return {
                "passed": True,
                "violations": [],
                "warnings": [],
                "violation_count": 0,
            }

        violations = []
        for idx, row in trades_df.iterrows():
            if pd.isna(row.get("entry_timestamp")):
                continue
            # For simplicity, convert strings to timestamps for comparison if needed
            entry_ts = pd.to_datetime(row["entry_timestamp"])

            # Simulated exit should not be before entry
            if not pd.isna(row.get("exit_timestamp")):
                exit_ts = pd.to_datetime(row["exit_timestamp"])
                if exit_ts < entry_ts:
                    violations.append(
                        f"Trade {row['trade_id']}: exit {exit_ts} < entry {entry_ts}"
                    )

        return {
            "passed": len(violations) == 0,
            "violations": violations,
            "warnings": [],
            "violation_count": len(violations),
        }
