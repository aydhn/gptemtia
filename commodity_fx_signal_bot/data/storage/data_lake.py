import json
import re
from pathlib import Path

import pandas as pd
from config.paths import LAKE_FEATURES_GROUP_FEATURES_DIR

from config.symbols import SymbolSpec
from core.logger import get_logger
from data.data_quality import DataQualityError, validate_ohlcv_dataframe

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

    def get_signal_pool_path(self, timeframe: str, profile_name: str) -> Path:
        """Get path for signal pool features."""
        from config.paths import LAKE_FEATURES_SIGNAL_POOL_DIR

        filename = f"signal_pool_{timeframe}_{profile_name}.parquet"
        return LAKE_FEATURES_SIGNAL_POOL_DIR / filename

    def save_signal_pool(
        self, timeframe: str, df: pd.DataFrame, profile_name: str
    ) -> Path:
        """Save a signal pool DataFrame to the Data Lake."""
        if df is None or df.empty:
            return self.get_signal_pool_path(timeframe, profile_name)

        path = self.get_signal_pool_path(timeframe, profile_name)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            import logging

            logging.getLogger(__name__).debug(f"Saved signal pool to Data Lake: {path}")
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to save signal pool ({timeframe}, {profile_name}): {e}"
            )
            raise

        return path

    def load_signal_pool(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        """Load a signal pool DataFrame from the Data Lake."""
        path = self.get_signal_pool_path(timeframe, profile_name)
        if not path.exists():
            return pd.DataFrame()

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            return df
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to load signal pool ({timeframe}, {profile_name}): {e}"
            )
            raise

    def has_signal_pool(self, timeframe: str, profile_name: str) -> bool:
        """Check if signal pool exists."""
        return self.get_signal_pool_path(timeframe, profile_name).exists()

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

    # Processed Data Methods
    def get_processed_symbol_dir(self, spec: SymbolSpec) -> Path:
        """Get the directory path for a specific symbol in the processed area."""
        source = spec.data_source
        sub_class = spec.sub_class.lower().replace(" ", "_")
        safe_sym = self.safe_symbol_name(spec.symbol)
        return self.root_dir / "processed" / "ohlcv" / source / sub_class / safe_sym

    def get_processed_ohlcv_path(self, spec: SymbolSpec, timeframe: str) -> Path:
        """Get the file path for processed OHLCV data of a specific timeframe."""
        symbol_dir = self.get_processed_symbol_dir(spec)
        return symbol_dir / f"{timeframe}.parquet"

    def save_processed_ohlcv(
        self, spec: SymbolSpec, timeframe: str, df: pd.DataFrame
    ) -> Path:
        """Save a cleaned/processed OHLCV DataFrame to the Data Lake."""
        if df is None or df.empty:
            logger.warning(
                f"Attempted to save empty processed DataFrame for {spec.symbol} ({timeframe})"
            )
            return self.get_processed_ohlcv_path(spec, timeframe)

        try:
            # We skip standard validation here or you could add a softer validation
            # since processed data might have extra columns
            pass
        except Exception as e:
            logger.warning(
                f"Processed data validation failed for {spec.symbol} ({timeframe}): {e}"
            )

        path = self.get_processed_ohlcv_path(spec, timeframe)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            logger.debug(f"Saved processed OHLCV to Data Lake: {path}")
        except ImportError:
            logger.error("pyarrow is required to save parquet files.")
            raise
        except Exception as e:
            logger.error(
                f"Failed to save processed OHLCV for {spec.symbol} ({timeframe}): {e}"
            )
            raise

        return path

    def load_processed_ohlcv(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        """Load a processed OHLCV DataFrame from the Data Lake."""
        path = self.get_processed_ohlcv_path(spec, timeframe)
        if not path.exists():
            raise FileNotFoundError(f"Processed OHLCV data not found at {path}")

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            if isinstance(df.index, pd.DatetimeIndex) and df.index.tz is None:
                df.index = df.index.tz_localize("UTC")
            return df
        except ImportError:
            logger.error("pyarrow is required to read parquet files.")
            raise
        except Exception as e:
            logger.error(
                f"Failed to load processed OHLCV for {spec.symbol} ({timeframe}): {e}"
            )
            raise

    def has_processed_ohlcv(self, spec: SymbolSpec, timeframe: str) -> bool:
        """Check if processed OHLCV data exists for a given timeframe."""
        path = self.get_processed_ohlcv_path(spec, timeframe)
        return path.exists() and path.is_file()

    def save_quality_report(
        self, spec: SymbolSpec, timeframe: str, report: dict
    ) -> Path:
        """Save a quality report."""
        safe_sym = self.safe_symbol_name(spec.symbol)
        filename = f"{safe_sym}_{timeframe}_quality.json"
        path = self.root_dir / "processed" / "quality_reports" / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=4)
            return path
        except Exception as e:
            logger.error(f"Failed to save quality report for {spec.symbol}: {e}")
            raise

    def load_quality_report(self, spec: SymbolSpec, timeframe: str) -> dict:
        """Load a quality report."""
        safe_sym = self.safe_symbol_name(spec.symbol)
        filename = f"{safe_sym}_{timeframe}_quality.json"
        path = self.root_dir / "processed" / "quality_reports" / filename
        if not path.exists():
            return {}
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load quality report for {spec.symbol}: {e}")
            return {}

    def save_cleaning_report(
        self, spec: SymbolSpec, timeframe: str, report: dict
    ) -> Path:
        """Save a cleaning report."""
        safe_sym = self.safe_symbol_name(spec.symbol)
        filename = f"{safe_sym}_{timeframe}_cleaning.json"
        path = self.root_dir / "processed" / "cleaning_reports" / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=4)
            return path
        except Exception as e:
            logger.error(f"Failed to save cleaning report for {spec.symbol}: {e}")
            raise

    def load_cleaning_report(self, spec: SymbolSpec, timeframe: str) -> dict:
        """Load a cleaning report."""
        safe_sym = self.safe_symbol_name(spec.symbol)
        filename = f"{safe_sym}_{timeframe}_cleaning.json"
        path = self.root_dir / "processed" / "cleaning_reports" / filename
        if not path.exists():
            return {}
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load cleaning report for {spec.symbol}: {e}")
            return {}

    # Feature Data Methods
    def get_feature_path(
        self, spec: SymbolSpec, timeframe: str, feature_set_name: str = "technical"
    ) -> Path:
        """Get the file path for feature data."""
        source = spec.data_source
        sub_class = spec.sub_class.lower().replace(" ", "_")
        safe_sym = self.safe_symbol_name(spec.symbol)

        from config.paths import (
            LAKE_FEATURES_ASSET_PROFILES_DIR,
            LAKE_FEATURES_ASSET_PROFILE_EVENTS_DIR,
            LAKE_FEATURES_GROUP_FEATURES_DIR,
            LAKE_FEATURES_ASSET_PROFILES_DIR,
            LAKE_FEATURES_ASSET_PROFILE_EVENTS_DIR,
            LAKE_FEATURES_GROUP_FEATURES_DIR,
            LAKE_MACRO_RAW_DIR,
            LAKE_MACRO_PROCESSED_DIR,
            LAKE_FEATURES_REGIME_DIR,
            LAKE_FEATURES_REGIME_EVENTS_DIR,
            LAKE_FEATURES_MTF_DIR,
            LAKE_FEATURES_MTF_EVENTS_DIR,
            LAKE_FEATURES_DIR,
            LAKE_FEATURES_DIVERGENCE_DIR,
            LAKE_FEATURES_DIVERGENCE_EVENTS_DIR,
        )

        symbol_dir = (
            LAKE_FEATURES_DIR / feature_set_name / source / sub_class / safe_sym
        )
        return symbol_dir / f"{timeframe}.parquet"

    def save_features(
        self,
        spec: SymbolSpec,
        timeframe: str,
        df: pd.DataFrame,
        feature_set_name: str = "technical",
    ) -> Path:
        """Save a feature DataFrame to the Data Lake."""
        if df is None or df.empty:
            logger.warning(
                f"Attempted to save empty feature DataFrame for {spec.symbol} ({timeframe})"
            )
            return self.get_feature_path(spec, timeframe, feature_set_name)

        path = self.get_feature_path(spec, timeframe, feature_set_name)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            logger.debug(f"Saved {feature_set_name} features to Data Lake: {path}")
        except Exception as e:
            logger.error(
                f"Failed to save {feature_set_name} features for {spec.symbol} ({timeframe}): {e}"
            )
            raise

        return path

    def load_features(
        self, spec: SymbolSpec, timeframe: str, feature_set_name: str = "technical"
    ) -> pd.DataFrame:
        """Load a feature DataFrame from the Data Lake."""
        path = self.get_feature_path(spec, timeframe, feature_set_name)
        if not path.exists():
            raise FileNotFoundError(f"Feature data not found at {path}")

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            if isinstance(df.index, pd.DatetimeIndex) and df.index.tz is None:
                df.index = df.index.tz_localize("UTC")
            return df
        except Exception as e:
            logger.error(
                f"Failed to load {feature_set_name} features for {spec.symbol} ({timeframe}): {e}"
            )
            raise

    def has_features(
        self, spec: SymbolSpec, timeframe: str, feature_set_name: str = "technical"
    ) -> bool:
        """Check if feature data exists."""
        path = self.get_feature_path(spec, timeframe, feature_set_name)
        return path.exists() and path.is_file()

    def list_feature_timeframes(
        self, spec: SymbolSpec, feature_set_name: str = "technical"
    ) -> list[str]:
        """List all available feature timeframes for a symbol."""
        path = self.get_feature_path(spec, "dummy", feature_set_name)
        symbol_dir = path.parent

        if not symbol_dir.exists():
            return []

        return sorted([f.stem for f in symbol_dir.glob("*.parquet")])

    def save_macro_series(
        self, code: str, df: pd.DataFrame, processed: bool = False
    ) -> Path:
        """Save macro series data to lake."""
        if df.empty:
            logger.warning("Attempted to save empty macro series for %s", code)
            from config.paths import LAKE_MACRO_PROCESSED_DIR, LAKE_MACRO_RAW_DIR
            return (
                LAKE_MACRO_PROCESSED_DIR if processed else LAKE_MACRO_RAW_DIR
            ) / f"{code}.parquet"

        from config.paths import LAKE_MACRO_PROCESSED_DIR, LAKE_MACRO_RAW_DIR
        target_dir = LAKE_MACRO_PROCESSED_DIR if processed else LAKE_MACRO_RAW_DIR
        filepath = target_dir / f"{code}.parquet"

        try:
            df.to_parquet(filepath, index=True)
            logger.debug("Saved macro series %s to %s", code, filepath)
            return filepath
        except Exception as e:
            logger.error("Error saving macro series %s: %s", code, str(e))
            from core.exceptions import DataStorageError

            raise DataStorageError(f"Failed to save macro series {code}: {str(e)}")

    def load_macro_series(self, code: str, processed: bool = False) -> pd.DataFrame:
        """Load macro series data from lake."""
        from config.paths import LAKE_MACRO_PROCESSED_DIR, LAKE_MACRO_RAW_DIR
        target_dir = LAKE_MACRO_PROCESSED_DIR if processed else LAKE_MACRO_RAW_DIR
        filepath = target_dir / f"{code}.parquet"

        if not filepath.exists():
            logger.debug("Macro series not found: %s", filepath)
            return pd.DataFrame()

        try:
            df = pd.read_parquet(filepath)
            return df
        except Exception as e:
            logger.error("Error loading macro series %s: %s", code, str(e))
            from core.exceptions import DataStorageError

            raise DataStorageError(f"Failed to load macro series {code}: {str(e)}")

    def has_macro_series(self, code: str, processed: bool = False) -> bool:
        """Check if macro series exists in lake."""
        from config.paths import LAKE_MACRO_PROCESSED_DIR, LAKE_MACRO_RAW_DIR
        target_dir = LAKE_MACRO_PROCESSED_DIR if processed else LAKE_MACRO_RAW_DIR
        filepath = target_dir / f"{code}.parquet"
        return filepath.exists()

    def get_group_feature_path(self, asset_class: str, timeframe: str) -> Path:
        """Get path for group features."""
        filename = f"group_features_{asset_class}_{timeframe}.{'parquet'}"
        return LAKE_FEATURES_GROUP_FEATURES_DIR / filename

    def save_group_features(
        self, asset_class: str, timeframe: str, df: pd.DataFrame
    ) -> Path:
        """Save a group feature DataFrame to the Data Lake."""
        if df is None or df.empty:
            return self.get_group_feature_path(asset_class, timeframe)

        path = self.get_group_feature_path(asset_class, timeframe)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            logger.debug(f"Saved group features to Data Lake: {path}")
        except Exception as e:
            logger.error(
                f"Failed to save group features for {asset_class} ({timeframe}): {e}"
            )
            raise

        return path

    def load_group_features(self, asset_class: str, timeframe: str) -> pd.DataFrame:
        """Load a group feature DataFrame from the Data Lake."""
        path = self.get_group_feature_path(asset_class, timeframe)
        if not path.exists():
            raise FileNotFoundError(f"Group feature data not found at {path}")

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            if isinstance(df.index, pd.DatetimeIndex) and df.index.tz is None:
                df.index = df.index.tz_localize("UTC")
            return df
        except Exception as e:
            logger.error(
                f"Failed to load group features for {asset_class} ({timeframe}): {e}"
            )
            raise

    def has_group_features(self, asset_class: str, timeframe: str) -> bool:
        """Check if group features exist."""
        return self.get_group_feature_path(asset_class, timeframe).exists()

    def list_group_feature_timeframes(self, asset_class: str) -> list[str]:
        """List all timeframes with group features for a specific asset class."""
        dir_path = LAKE_FEATURES_GROUP_FEATURES_DIR
        if not dir_path.exists():
            return []

        prefix = f"group_features_{asset_class}_"
        suffix = f".{'parquet'}"

        timeframes = []
        for file_path in dir_path.glob(f"{prefix}*{suffix}"):
            try:
                tf_part = file_path.name[len(prefix) : -len(suffix)]
                timeframes.append(tf_part)
            except Exception:
                continue

        return sorted(timeframes)

    def get_signal_pool_path(self, timeframe: str, profile_name: str) -> Path:
        """Get path for signal pool features."""
        from config.paths import LAKE_FEATURES_SIGNAL_POOL_DIR

        filename = f"signal_pool_{timeframe}_{profile_name}.parquet"
        return LAKE_FEATURES_SIGNAL_POOL_DIR / filename

    def save_signal_pool(
        self, timeframe: str, df: pd.DataFrame, profile_name: str
    ) -> Path:
        """Save a signal pool DataFrame to the Data Lake."""
        if df is None or df.empty:
            return self.get_signal_pool_path(timeframe, profile_name)

        path = self.get_signal_pool_path(timeframe, profile_name)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            import logging

            logging.getLogger(__name__).debug(f"Saved signal pool to Data Lake: {path}")
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to save signal pool ({timeframe}, {profile_name}): {e}"
            )
            raise

        return path

    def load_signal_pool(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        """Load a signal pool DataFrame from the Data Lake."""
        path = self.get_signal_pool_path(timeframe, profile_name)
        if not path.exists():
            return pd.DataFrame()

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            return df
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to load signal pool ({timeframe}, {profile_name}): {e}"
            )
            raise

    def has_signal_pool(self, timeframe: str, profile_name: str) -> bool:
        """Check if signal pool exists."""
        return self.get_signal_pool_path(timeframe, profile_name).exists()

    def get_decision_pool_path(self, timeframe: str, profile_name: str) -> Path:
        """Get path for decision pool features."""
        from config.paths import LAKE_FEATURES_DECISION_POOL_DIR

        filename = f"decision_pool_{timeframe}_{profile_name}.parquet"
        return LAKE_FEATURES_DECISION_POOL_DIR / filename

    def save_decision_pool(
        self, timeframe: str, df: pd.DataFrame, profile_name: str
    ) -> Path:
        """Save a decision pool DataFrame to the Data Lake."""
        if df is None or df.empty:
            return self.get_decision_pool_path(timeframe, profile_name)

        path = self.get_decision_pool_path(timeframe, profile_name)
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df.to_parquet(path, engine="pyarrow")
            import logging

            logging.getLogger(__name__).debug(
                f"Saved decision pool to Data Lake: {path}"
            )
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to save decision pool ({timeframe}, {profile_name}): {e}"
            )
            raise

        return path

    def load_decision_pool(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        """Load a decision pool DataFrame from the Data Lake."""
        path = self.get_decision_pool_path(timeframe, profile_name)
        if not path.exists():
            return pd.DataFrame()

        try:
            df = pd.read_parquet(path, engine="pyarrow")
            return df
        except Exception as e:
            import logging

            logging.getLogger(__name__).error(
                f"Failed to load decision pool ({timeframe}, {profile_name}): {e}"
            )
            raise

    def has_decision_pool(self, timeframe: str, profile_name: str) -> bool:
        """Check if decision pool exists."""
        return self.get_decision_pool_path(timeframe, profile_name).exists()
