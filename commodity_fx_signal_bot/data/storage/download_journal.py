from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Optional

import pandas as pd

from core.logger import get_logger

logger = get_logger(__name__)


@dataclass
class DownloadJournalEntry:
    timestamp_utc: str
    symbol: str
    requested_symbol: str
    resolved_symbol: Optional[str]
    asset_class: str
    timeframe: str
    provider_interval: str
    period: Optional[str]
    start: Optional[str]
    end: Optional[str]
    success: bool
    rows: int
    used_cache: bool
    used_alias: bool
    saved_path: Optional[str]
    error: str = ""


class DownloadJournal:
    """Manages the history of data downloads."""

    def __init__(self, journal_path: Path):
        self.journal_path = journal_path

    def append(self, entry: DownloadJournalEntry) -> None:
        """Append an entry to the journal."""
        self.journal_path.parent.mkdir(parents=True, exist_ok=True)

        df_new = pd.DataFrame([asdict(entry)])

        try:
            if self.journal_path.exists():
                df_new.to_csv(self.journal_path, mode="a", header=False, index=False)
            else:
                df_new.to_csv(self.journal_path, mode="w", header=True, index=False)
        except Exception as e:
            logger.error(f"Failed to append to journal {self.journal_path}: {e}")

    def load(self) -> pd.DataFrame:
        """Load the entire journal as a DataFrame."""
        if not self.journal_path.exists():
            return pd.DataFrame()

        try:
            return pd.read_csv(self.journal_path)
        except Exception as e:
            logger.error(f"Failed to load journal {self.journal_path}: {e}")
            return pd.DataFrame()

    def tail(self, n: int = 20) -> pd.DataFrame:
        """Get the last n entries of the journal."""
        df = self.load()
        if df.empty:
            return df
        return df.tail(n)

    def summarize(self) -> Dict:
        """Provide a summary of the journal."""
        df = self.load()
        if df.empty:
            return {
                "total_entries": 0,
                "success_count": 0,
                "failure_count": 0,
                "success_rate": 0.0,
                "cache_hits": 0,
                "alias_used": 0,
                "recent_errors": [],
            }

        total = len(df)
        success = int(df["success"].sum())
        failure = total - success
        success_rate = success / total if total > 0 else 0.0
        cache_hits = int(df["used_cache"].sum())
        alias_used = int(df["used_alias"].sum())

        recent_errors = (
            df[df["error"].notna() & (df["error"] != "")]["error"].tail(5).tolist()
        )

        return {
            "total_entries": total,
            "success_count": success,
            "failure_count": failure,
            "success_rate": success_rate,
            "cache_hits": cache_hits,
            "alias_used": alias_used,
            "recent_errors": recent_errors,
        }
