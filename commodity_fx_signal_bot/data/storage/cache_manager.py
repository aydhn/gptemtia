"""
Cache management for OHLCV data.
"""

import re
from pathlib import Path
from typing import Optional

import pandas as pd

from core.logger import get_logger

logger = get_logger(__name__)


class CacheManager:
    """Manager for caching downloaded data."""

    def __init__(self, cache_dir: Path):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _sanitize_symbol(self, symbol: str) -> str:
        """Sanitize symbol to be safe for filenames."""
        safe_symbol = symbol.replace("/", "_").replace("=", "")
        safe_symbol = re.sub(r"[^a-zA-Z0-9_-]", "", safe_symbol)
        return safe_symbol

    def build_cache_path(
        self,
        symbol: str,
        interval: str,
        period: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        format_ext: str = "parquet",
    ) -> Path:
        """Build a safe file path for caching."""
        safe_symbol = self._sanitize_symbol(symbol)

        if start and end:
            time_suffix = f"{start}_{end}"
        elif period:
            time_suffix = f"{period}"
        else:
            time_suffix = "default"

        filename = f"{safe_symbol}_{interval}_{time_suffix}.{format_ext}"
        return self.cache_dir / filename

    def exists(self, path: Path) -> bool:
        """Check if cache file exists."""
        return path.exists() and path.is_file()

    def save_dataframe(self, df: pd.DataFrame, path: Path) -> None:
        """Save a dataframe to cache."""
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            if path.suffix == ".parquet":
                df.to_parquet(path, engine="pyarrow")
            elif path.suffix == ".csv":
                df.to_csv(path)
            else:
                raise ValueError(f"Unsupported cache format: {path.suffix}")
            logger.debug(f"Saved dataframe to cache: {path}")
        except Exception as e:
            logger.error(f"Failed to save dataframe to cache at {path}: {e}")

    def load_dataframe(self, path: Path) -> pd.DataFrame:
        """Load a dataframe from cache."""
        try:
            if path.suffix == ".parquet":
                df = pd.read_parquet(path, engine="pyarrow")
            elif path.suffix == ".csv":
                df = pd.read_csv(path, index_col=0, parse_dates=True)
            else:
                raise ValueError(f"Unsupported cache format: {path.suffix}")

            # Ensure index is timezone-aware DatetimeIndex
            if isinstance(df.index, pd.DatetimeIndex) and df.index.tz is None:
                df.index = df.index.tz_localize("UTC")

            logger.debug(f"Loaded dataframe from cache: {path}")
            return df
        except Exception as e:
            logger.error(f"Failed to load dataframe from cache at {path}: {e}")
            raise

    def clear_cache(self) -> None:
        """Clear all files in the cache directory."""
        try:
            count = 0
            for file_path in self.cache_dir.glob("*"):
                if file_path.is_file():
                    file_path.unlink()
                    count += 1
            logger.info(f"Cleared {count} files from cache directory.")
        except Exception as e:
            logger.error(f"Failed to clear cache directory: {e}")
