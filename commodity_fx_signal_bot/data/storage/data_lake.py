import json
import re
from pathlib import Path
from typing import Optional, List, Dict
import pandas as pd

from core.logger import get_logger
from config.symbols import SymbolSpec
from data.data_quality import validate_ohlcv_dataframe, DataQualityError

logger = get_logger(__name__)


class DataLake:
    """Manager for the local Data Lake."""

    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.ohlcv_dir = self.root_dir / "ohlcv"

    @staticmethod
    def safe_symbol_name(symbol: str) -> str:
        """Sanitize symbol to be safe for filenames and directories."""
        safe_symbol = symbol.replace("/", "_").replace("=", "_")
        safe_symbol = re.sub(r"[^a-zA-Z0-9_-]", "", safe_symbol)
        return safe_symbol

    def get_symbol_dir(self, spec: SymbolSpec) -> Path:
        """Get the directory path for a specific symbol."""
        source = spec.data_source
        sub_class = spec.sub_class.lower().replace(" ", "_")
        safe_sym = self.safe_symbol_name(spec.symbol)
        return self.ohlcv_dir / source / sub_class / safe_sym

    def get_ohlcv_path(self, spec: SymbolSpec, timeframe: str) -> Path:
        """Get the file path for OHLCV data of a specific timeframe."""
        symbol_dir = self.get_symbol_dir(spec)
        return symbol_dir / f"{timeframe}.parquet"

    def get_metadata_path(self, spec: SymbolSpec) -> Path:
        """Get the file path for the symbol's metadata."""
        symbol_dir = self.get_symbol_dir(spec)
        return symbol_dir / "metadata.json"

    def save_ohlcv(self, spec: SymbolSpec, timeframe: str, df: pd.DataFrame) -> Path:
        """Save an OHLCV DataFrame to the Data Lake."""
        if df is None or df.empty:
            logger.warning(
                f"Attempted to save empty DataFrame for {spec.symbol} ({timeframe})"
            )
            return self.get_ohlcv_path(spec, timeframe)

        try:
            validate_ohlcv_dataframe(df)
        except DataQualityError as e:
            logger.warning(
                f"Data validation failed for {spec.symbol} ({timeframe}): {e}"
            )
            raise

        path = self.get_ohlcv_path(spec, timeframe)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            logger.debug(f"Saved OHLCV to Data Lake: {path}")
        except ImportError:
            logger.error("pyarrow is required to save parquet files.")
            raise
        except Exception as e:
            logger.error(f"Failed to save OHLCV for {spec.symbol} ({timeframe}): {e}")
            raise

        return path

    def load_ohlcv(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        """Load an OHLCV DataFrame from the Data Lake."""
        path = self.get_ohlcv_path(spec, timeframe)
        if not path.exists():
            raise FileNotFoundError(f"OHLCV data not found at {path}")

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            if isinstance(df.index, pd.DatetimeIndex) and df.index.tz is None:
                df.index = df.index.tz_localize("UTC")
            return df
        except ImportError:
            logger.error("pyarrow is required to read parquet files.")
            raise
        except Exception as e:
            logger.error(f"Failed to load OHLCV for {spec.symbol} ({timeframe}): {e}")
            raise

    def has_ohlcv(self, spec: SymbolSpec, timeframe: str) -> bool:
        """Check if OHLCV data exists for a given timeframe."""
        path = self.get_ohlcv_path(spec, timeframe)
        return path.exists() and path.is_file()

    def save_metadata(self, spec: SymbolSpec, metadata: dict) -> Path:
        """Save metadata for a symbol."""
        path = self.get_metadata_path(spec)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=4)
            return path
        except Exception as e:
            logger.error(f"Failed to save metadata for {spec.symbol}: {e}")
            raise

    def load_metadata(self, spec: SymbolSpec) -> dict:
        """Load metadata for a symbol."""
        path = self.get_metadata_path(spec)
        if not path.exists():
            return {}
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load metadata for {spec.symbol}: {e}")
            return {}

    def list_available_timeframes(self, spec: SymbolSpec) -> list[str]:
        """List all available OHLCV timeframes for a symbol."""
        symbol_dir = self.get_symbol_dir(spec)
        if not symbol_dir.exists():
            return []

        timeframes = []
        for file in symbol_dir.glob("*.parquet"):
            timeframe = file.stem
            timeframes.append(timeframe)

        return sorted(timeframes)

    def delete_ohlcv(self, spec: SymbolSpec, timeframe: str) -> None:
        """Delete OHLCV data for a specific timeframe."""
        path = self.get_ohlcv_path(spec, timeframe)
        if path.exists():
            try:
                path.unlink()
                logger.debug(f"Deleted OHLCV from Data Lake: {path}")
            except Exception as e:
                logger.error(
                    f"Failed to delete OHLCV for {spec.symbol} ({timeframe}): {e}"
                )
