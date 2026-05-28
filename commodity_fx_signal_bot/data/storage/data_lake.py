import os
from typing import Optional
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

    # Phase 50: Command Center Methods
    def save_command_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_REGISTRY_DIR / "command_registry.parquet", summary)

    def load_command_registry(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_REGISTRY_DIR / "command_registry.parquet")

    def save_guided_workflows(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_WORKFLOWS_DIR / "guided_workflows.parquet", summary)

    def load_guided_workflows(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_WORKFLOWS_DIR / "guided_workflows.parquet")

    def save_safe_runbooks(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_RUNBOOKS_DIR / "safe_runbooks.parquet", summary)

    def load_safe_runbooks(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_RUNBOOKS_DIR / "safe_runbooks.parquet")

    def save_command_dry_run_plan(self, plan_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_DRY_RUN_PLANS_DIR / f"{plan_name}.parquet", summary)

    def load_command_dry_run_plan(self, plan_name: str) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_DRY_RUN_PLANS_DIR / f"{plan_name}.parquet")

    def save_interactive_query_flow(self, flow_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_QUERY_FLOWS_DIR / f"{flow_name}.parquet", summary)

    def load_interactive_query_flow(self, flow_name: str) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_QUERY_FLOWS_DIR / f"{flow_name}.parquet")

    def save_project_status(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_PROJECT_STATUS_DIR / "project_status.parquet", summary)

    def load_project_status(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_PROJECT_STATUS_DIR / "project_status.parquet")

    def save_module_health(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_MODULE_HEALTH_DIR / "module_health.parquet", summary)

    def load_module_health(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_MODULE_HEALTH_DIR / "module_health.parquet")

    def save_script_availability_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_SCRIPT_DISCOVERY_DIR / "script_availability_matrix.parquet", summary)

    def load_script_availability_matrix(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_SCRIPT_DISCOVERY_DIR / "script_availability_matrix.parquet")

    def save_phase_coverage_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_PHASE_COVERAGE_DIR / "phase_coverage_matrix.parquet", summary)

    def load_phase_coverage_matrix(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_PHASE_COVERAGE_DIR / "phase_coverage_matrix.parquet")

    def save_project_consolidation_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        path = self.paths.LAKE_COMMAND_CENTER_CONSOLIDATION_DIR / f"{profile_name}_consolidation.json"
        with open(path, "w", encoding="utf-8") as f:
            json.update(report) if hasattr(json, "update") else json.dump(report, f, indent=4)
        return path

    def load_project_consolidation_report(self, profile_name: str) -> dict:
        path = self.paths.LAKE_COMMAND_CENTER_CONSOLIDATION_DIR / f"{profile_name}_consolidation.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_command_center_quality(self, profile_name: str, quality: dict) -> Path:
        path = self.paths.LAKE_COMMAND_CENTER_QUALITY_DIR / f"{profile_name}_quality.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=4)
        return path

    def load_command_center_quality(self, profile_name: str) -> dict:
        path = self.paths.LAKE_COMMAND_CENTER_QUALITY_DIR / f"{profile_name}_quality.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_command_center_status(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_DIR / "command_center_status.parquet", summary)

    def load_command_center_status(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_DIR / "command_center_status.parquet")

    def list_command_center_reports(self) -> pd.DataFrame:
        data = []
        for p in self.paths.LAKE_COMMAND_CENTER_DIR.rglob("*.parquet"):
            data.append({"path": str(p), "type": "parquet"})
        for p in self.paths.LAKE_COMMAND_CENTER_DIR.rglob("*.json"):
            data.append({"path": str(p), "type": "json"})
        return pd.DataFrame(data)



    # Phase 47 Governance Methods
    def save_artifact_inventory(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "inventory" / "artifact_inventory.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_artifact_inventory(self) -> pd.DataFrame:
        p = self.governance_dir / "inventory" / "artifact_inventory.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_artifact_fingerprints(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "fingerprints" / "artifact_fingerprints.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_artifact_fingerprints(self) -> pd.DataFrame:
        p = self.governance_dir / "fingerprints" / "artifact_fingerprints.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_provenance_records(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "provenance" / "provenance_records.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_provenance_records(self) -> pd.DataFrame:
        p = self.governance_dir / "provenance" / "provenance_records.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_lineage_nodes(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "lineage" / "lineage_nodes.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_lineage_nodes(self) -> pd.DataFrame:
        p = self.governance_dir / "lineage" / "lineage_nodes.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_lineage_edges(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "lineage" / "lineage_edges.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_lineage_edges(self) -> pd.DataFrame:
        p = self.governance_dir / "lineage" / "lineage_edges.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_dependency_trace(self, trace_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "dependencies" / f"{trace_name}_trace.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_dependency_trace(self, trace_name: str) -> pd.DataFrame:
        p = self.governance_dir / "dependencies" / f"{trace_name}_trace.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_audit_trail(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "audit" / "audit_trail.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_audit_trail(self) -> pd.DataFrame:
        p = self.governance_dir / "audit" / "audit_trail.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_source_attribution(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "source_attribution" / "source_attribution.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_source_attribution(self) -> pd.DataFrame:
        p = self.governance_dir / "source_attribution" / "source_attribution.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_governance_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.governance_dir / "checklists" / "governance_checklist.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_governance_checklist(self) -> pd.DataFrame:
        p = self.governance_dir / "checklists" / "governance_checklist.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_governance_quality(self, profile_name: str, quality: dict) -> Path: # type: ignore
        import json
        p = self.governance_dir / "quality" / f"{profile_name}_quality.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            json.dump(quality, f, indent=2)
        return p

    def load_governance_quality(self, profile_name: str) -> dict: # type: ignore
        import json
        p = self.governance_dir / "quality" / f"{profile_name}_quality.json"
        if not p.exists(): return {}
        with open(p, "r") as f:
            return json.load(f)

    def save_research_governance_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        import json
        p = self.governance_dir / f"{profile_name}_report.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            json.dump(report, f, indent=2)
        return p

    def load_research_governance_report(self, profile_name: str) -> dict: # type: ignore
        import json
        p = self.governance_dir / f"{profile_name}_report.json"
        if not p.exists(): return {}
        with open(p, "r") as f:
            return json.load(f)

    def list_governance_reports(self) -> pd.DataFrame:
        reports = []
        for p in self.governance_dir.glob("*_report.json"):
            reports.append({"report_name": p.stem, "path": str(p)})
        return pd.DataFrame(reports)


    """Manager for the local Data Lake."""

    def __init__(self, root_dir):
        if hasattr(root_dir, "lake_dir"):
            self.paths = root_dir
            self.root_dir = root_dir.lake_dir
        else:
            self.root_dir = Path(root_dir)
            from config.paths import ProjectPaths

            self.paths = ProjectPaths()

        self.ohlcv_dir = self.root_dir / "ohlcv"
        self.governance_dir = self.root_dir / "governance"

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

    def save_ohlcv(self, spec: SymbolSpec, timeframe: str, df: pd.DataFrame) -> Path: # type: ignore
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

    def save_metadata(self, spec: SymbolSpec, metadata: dict) -> Path: # type: ignore
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

    def load_metadata(self, spec: SymbolSpec) -> dict: # type: ignore
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

    def load_quality_report(self, spec: SymbolSpec, timeframe: str) -> dict: # type: ignore
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

    def load_cleaning_report(self, spec: SymbolSpec, timeframe: str) -> dict: # type: ignore
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

    def save_sizing_pool(
        self, timeframe: str, df: pd.DataFrame, profile_name: str
    ) -> Path:
        """Saves the global universe-level sizing candidate pool."""
        if df.empty:
            logger.warning(
                f"Empty sizing pool dataframe for {timeframe} {profile_name}. Skipping save."
            )
            return (
                paths.LAKE_FEATURES_SIZING_POOL_DIR
                / f"sizing_pool_{timeframe}_{profile_name}.parquet"
            )
        file_path = (
            paths.LAKE_FEATURES_SIZING_POOL_DIR
            / f"sizing_pool_{timeframe}_{profile_name}.parquet"
        )
        self._write_parquet(df, file_path)
        logger.info(f"Saved sizing pool to {file_path}")
        return file_path

    def load_sizing_pool(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        """Loads the global universe-level sizing candidate pool."""
        file_path = (
            paths.LAKE_FEATURES_SIZING_POOL_DIR
            / f"sizing_pool_{timeframe}_{profile_name}.parquet"
        )
        if not file_path.exists():
            raise FileNotFoundError(f"Sizing pool not found: {file_path}")
        return self._read_parquet(file_path)

    def has_sizing_pool(self, timeframe: str, profile_name: str) -> bool:
        """Checks if the global universe-level sizing candidate pool exists."""
        file_path = (
            paths.LAKE_FEATURES_SIZING_POOL_DIR
            / f"sizing_pool_{timeframe}_{profile_name}.parquet"
        )
        return file_path.exists()

    def save_backtest_trades(
        self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame
    ) -> Path:
        path = (
            self.paths.backtest_trades
            / f"backtest_trades_{symbol}_{timeframe}_{profile_name}.parquet"
        )
        df.to_parquet(path)
        return path

    def load_backtest_trades(
        self, symbol: str, timeframe: str, profile_name: str
    ) -> pd.DataFrame:
        path = (
            self.paths.backtest_trades
            / f"backtest_trades_{symbol}_{timeframe}_{profile_name}.parquet"
        )
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_backtest_equity_curve(
        self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame
    ) -> Path:
        path = (
            self.paths.backtest_equity_curves
            / f"backtest_equity_{symbol}_{timeframe}_{profile_name}.parquet"
        )
        df.to_parquet(path)
        return path

    def load_backtest_equity_curve(
        self, symbol: str, timeframe: str, profile_name: str
    ) -> pd.DataFrame:
        path = (
            self.paths.backtest_equity_curves
            / f"backtest_equity_{symbol}_{timeframe}_{profile_name}.parquet"
        )
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_backtest_summary(
        self, symbol: str, timeframe: str, profile_name: str, summary: dict
    ) -> Path:
        path = (
            self.paths.backtest_runs
            / f"backtest_summary_{symbol}_{timeframe}_{profile_name}.json"
        )
        import json

        with open(path, "w") as f:
            json.dump(summary, f, indent=2, default=str)
        return path

    def load_backtest_summary(
        self, symbol: str, timeframe: str, profile_name: str
    ) -> dict:
        path = (
            self.paths.backtest_runs
            / f"backtest_summary_{symbol}_{timeframe}_{profile_name}.json"
        )
        if path.exists():
            import json

            with open(path, "r") as f:
                return json.load(f)
        return {}

    def list_backtest_runs(self) -> pd.DataFrame:
        runs = []
        import json

        for file in self.paths.backtest_runs.glob("*.json"):
            try:
                with open(file, "r") as f:
                    data = json.load(f)
                runs.append(
                    {
                        "symbol": data.get("symbol", ""),
                        "timeframe": data.get("timeframe", ""),
                        "profile": data.get("profile", ""),
                        "trade_count": data.get("performance", {}).get(
                            "trade_count", 0
                        ),
                        "win_rate": data.get("performance", {}).get("win_rate", 0),
                        "total_return_pct": data.get("performance", {}).get(
                            "total_return_pct", 0
                        ),
                        "file_path": str(file),
                    }
                )
            except Exception as e:
                pass
        return pd.DataFrame(runs)

    # --- ML DATASET PHASE ---
    def save_ml_feature_matrix(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.ml_features / f"{symbol}_{timeframe}_{profile_name}_features.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_feature_matrix(self, symbol: str, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.ml_features / f"{symbol}_{timeframe}_{profile_name}_features.parquet"
        return self._load_parquet(path)

    def save_ml_target_frame(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.ml_targets / f"{symbol}_{timeframe}_{profile_name}_targets.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_target_frame(self, symbol: str, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.ml_targets / f"{symbol}_{timeframe}_{profile_name}_targets.parquet"
        return self._load_parquet(path)

    def save_ml_supervised_dataset(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.ml_datasets / f"{symbol}_{timeframe}_{profile_name}_dataset.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_supervised_dataset(self, symbol: str, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.ml_datasets / f"{symbol}_{timeframe}_{profile_name}_dataset.parquet"
        return self._load_parquet(path)

    def save_ml_split_manifest(self, symbol: str, timeframe: str, profile_name: str, manifest: dict) -> Path: # type: ignore
        path = self.paths.ml_splits / f"{symbol}_{timeframe}_{profile_name}_split.json"
        import json
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            if hasattr(manifest, '__dataclass_fields__'):
                from dataclasses import asdict
                json.dump(asdict(manifest), f, indent=4)
            else:
                json.dump(manifest, f, indent=4)

        return path

    def load_ml_split_manifest(self, symbol: str, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.ml_splits / f"{symbol}_{timeframe}_{profile_name}_split.json"
        return self._load_json(path) or {}

    def save_ml_dataset_metadata(self, symbol: str, timeframe: str, profile_name: str, metadata: dict) -> Path: # type: ignore
        path = self.paths.ml_metadata / f"{symbol}_{timeframe}_{profile_name}_metadata.json"
        self._save_json(metadata, path)
        return path

    def load_ml_dataset_metadata(self, symbol: str, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.ml_metadata / f"{symbol}_{timeframe}_{profile_name}_metadata.json"
        return self._load_json(path) or {}

    def save_ml_dataset_quality(self, symbol: str, timeframe: str, profile_name: str, quality: dict) -> Path: # type: ignore
        path = self.paths.ml_quality / f"{symbol}_{timeframe}_{profile_name}_quality.json"
        self._save_json(quality, path)
        return path

    def load_ml_dataset_quality(self, symbol: str, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.ml_quality / f"{symbol}_{timeframe}_{profile_name}_quality.json"
        return self._load_json(path) or {}

    def list_ml_datasets(self) -> pd.DataFrame:
        data = []
        for file_path in self.paths.ml_metadata.glob("*.json"):
            metadata = self._load_json(file_path)
            if metadata:
                data.append(metadata)
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data)

    def save_ml_model_evaluation(self, symbol: str, timeframe: str, profile_name: str, model_id: str, evaluation: dict) -> Path: # type: ignore
        path = self.paths.ml_model_evaluations / f"{model_id}_evaluation.json"
        self._save_json(evaluation, path)
        return path

    def load_ml_model_evaluation(self, symbol: str, timeframe: str, profile_name: str, model_id: str) -> dict: # type: ignore
        path = self.paths.ml_model_evaluations / f"{model_id}_evaluation.json"
        return self._load_json(path) or {}

    def save_ml_cv_results(self, symbol: str, timeframe: str, profile_name: str, model_id: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.ml_model_cv / f"{model_id}_cv.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_cv_results(self, symbol: str, timeframe: str, profile_name: str, model_id: str) -> pd.DataFrame:
        path = self.paths.ml_model_cv / f"{model_id}_cv.parquet"
        return self._load_parquet(path)

    def save_ml_model_quality(self, symbol: str, timeframe: str, profile_name: str, model_id: str, quality: dict) -> Path: # type: ignore
        path = self.paths.ml_model_quality / f"{model_id}_quality.json"
        self._save_json(quality, path)
        return path

    def load_ml_model_quality(self, symbol: str, timeframe: str, profile_name: str, model_id: str) -> dict: # type: ignore
        path = self.paths.ml_model_quality / f"{model_id}_quality.json"
        return self._load_json(path) or {}

    def save_ml_registry_entry(self, entry: dict) -> Path: # type: ignore
        model_id = entry.get("model_id", "unknown")
        path = self.paths.ml_model_registry / f"{model_id}_registry.json"
        self._save_json(entry, path)
        return path

    def list_ml_model_registry(self) -> pd.DataFrame:
        data = []
        for file_path in self.paths.ml_model_registry.glob("*.json"):
            metadata = self._load_json(file_path)
            if metadata:
                data.append(metadata)
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data)


    # --- PHASE 32: ML CONTEXT INTEGRATION ---
    def save_ml_integration_features(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame, layer: str) -> Path: # type: ignore
        path = self.paths.ml_integration_features / f"{symbol}_{timeframe}_{layer}_{profile_name}_features.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_integration_features(self, symbol: str, timeframe: str, profile_name: str, layer: str) -> pd.DataFrame:
        path = self.paths.ml_integration_features / f"{symbol}_{timeframe}_{layer}_{profile_name}_features.parquet"
        return self._load_parquet(path)

    def save_ml_alignment_report(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame, layer: str) -> Path: # type: ignore
        path = self.paths.ml_integration_alignment / f"{symbol}_{timeframe}_{layer}_{profile_name}_alignment.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_alignment_report(self, symbol: str, timeframe: str, profile_name: str, layer: str) -> pd.DataFrame:
        path = self.paths.ml_integration_alignment / f"{symbol}_{timeframe}_{layer}_{profile_name}_alignment.parquet"
        return self._load_parquet(path)

    def save_ml_conflict_report(self, symbol: str, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.ml_integration_conflicts / f"{symbol}_{timeframe}_{profile_name}_conflicts.parquet"
        self._save_parquet(df, path)
        return path

    def load_ml_conflict_report(self, symbol: str, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.ml_integration_conflicts / f"{symbol}_{timeframe}_{profile_name}_conflicts.parquet"
        return self._load_parquet(path)

    def save_ml_integration_quality(self, symbol: str, timeframe: str, profile_name: str, quality: dict) -> Path: # type: ignore
        path = self.paths.ml_integration_quality / f"{symbol}_{timeframe}_{profile_name}_quality.json"
        self._save_json(quality, path)
        return path

    def load_ml_integration_quality(self, symbol: str, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.ml_integration_quality / f"{symbol}_{timeframe}_{profile_name}_quality.json"
        return self._load_json(path) or {}

    def list_ml_integration_reports(self) -> pd.DataFrame:
        data = []
        for path in self.paths.ml_integration_alignment.glob("*_alignment.parquet"):
            parts = path.stem.split("_")
            if len(parts) >= 4:
                # symbol_timeframe_layer_profile_alignment
                symbol = parts[0]
                timeframe = parts[1]
                layer = parts[2]
                profile = "_".join(parts[3:-1])
                data.append({
                    "symbol": symbol,
                    "timeframe": timeframe,
                    "layer": layer,
                    "profile": profile,
                    "type": "alignment",
                    "path": str(path)
                })
        return pd.DataFrame(data)


    # --- Notifications Specific ---
    def save_notification_message(self, message: dict): # type: ignore
        import json
        message_id = message.get("message_id", "unknown_id")
        file_path = self.paths.LAKE_NOTIFICATIONS_MESSAGES_DIR / f"{message_id}.json"

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(message, f, indent=4, ensure_ascii=False)
            logger.info(f"Saved notification message to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error saving notification message {message_id}: {e}")
            return None

    def load_notification_message(self, message_id: str) -> dict: # type: ignore
        import json
        file_path = self.paths.LAKE_NOTIFICATIONS_MESSAGES_DIR / f"{message_id}.json"

        try:
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            else:
                logger.warning(f"Notification message file not found: {file_path}")
                return {}
        except Exception as e:
            logger.error(f"Error loading notification message {message_id}: {e}")
            return {}

    def save_notification_delivery_log(self, profile_name: str, df: pd.DataFrame): # type: ignore
        if df is None or df.empty:
            logger.warning(f"Empty delivery log dataframe for {profile_name}. Not saving.")
            return None

        file_path = self.paths.LAKE_NOTIFICATIONS_DELIVERY_LOGS_DIR / f"{profile_name}_delivery_log.parquet"
        df.astype(str).to_parquet(file_path, index=False)
        logger.info(f"Saved notification delivery log to {file_path}")
        return file_path

    def load_notification_delivery_log(self, profile_name: str) -> pd.DataFrame | None:
        file_path = self.paths.LAKE_NOTIFICATIONS_DELIVERY_LOGS_DIR / f"{profile_name}_delivery_log.parquet"
        return pd.read_parquet(file_path) if file_path.exists() else None

    def save_notification_delivery_audit(self, profile_name: str, audit: dict): # type: ignore
        import json
        from datetime import datetime; timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
        file_path = self.paths.LAKE_NOTIFICATIONS_AUDITS_DIR / f"{profile_name}_{timestamp}_audit.json"

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(audit, f, indent=4, ensure_ascii=False)
            logger.info(f"Saved notification delivery audit to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error saving notification delivery audit {profile_name}: {e}")
            return None

    def load_notification_delivery_audit(self, profile_name: str) -> dict: # type: ignore
        import json
        pattern = f"{profile_name}_*_audit.json"
        files = list(self.paths.LAKE_NOTIFICATIONS_AUDITS_DIR.glob(pattern))

        if not files:
            logger.warning(f"No delivery audit found for profile: {profile_name}")
            return {}

        latest_file = sorted(files)[-1]
        try:
            with open(latest_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading notification delivery audit from {latest_file}: {e}")
            return {}

    def save_notification_quality(self, message_id: str, quality: dict): # type: ignore
        import json
        file_path = self.paths.LAKE_NOTIFICATIONS_QUALITY_DIR / f"{message_id}_quality.json"

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(quality, f, indent=4, ensure_ascii=False)
            logger.info(f"Saved notification quality to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error saving notification quality {message_id}: {e}")
            return None

    def load_notification_quality(self, message_id: str) -> dict: # type: ignore
        import json
        file_path = self.paths.LAKE_NOTIFICATIONS_QUALITY_DIR / f"{message_id}_quality.json"

        try:
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            else:
                logger.warning(f"Notification quality file not found: {file_path}")
                return {}
        except Exception as e:
            logger.error(f"Error loading notification quality {message_id}: {e}")
            return {}

    def list_notification_messages(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_NOTIFICATIONS_MESSAGES_DIR.glob("*.json"))
        data = []
        for f in files:
            try:
                import json
                with open(f, "r", encoding="utf-8") as file:
                    msg = json.load(file)
                    data.append({
                        "message_id": msg.get("message_id"),
                        "notification_type": msg.get("notification_type"),
                        "severity": msg.get("severity"),
                        "created_at_utc": msg.get("created_at_utc"),
                        "profile_name": msg.get("profile_name"),
                        "file_path": str(f)
                    })
            except Exception:
                pass

        return pd.DataFrame(data)


    # -------------------------------------------------------------------------
    # Orchestration Support
    # -------------------------------------------------------------------------

    def save_orchestration_run_manifest(self, run_id: str, manifest: dict) -> 'Path':
        """Save orchestration run manifest."""
        from config.paths import LAKE_ORCHESTRATION_MANIFESTS_DIR
        path = LAKE_ORCHESTRATION_MANIFESTS_DIR / f"{run_id}_manifest.json"
        import json
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            if hasattr(manifest, '__dataclass_fields__'):
                from dataclasses import asdict
                json.dump(asdict(manifest), f, indent=4)
            else:
                json.dump(manifest, f, indent=4)

        return path

    def load_orchestration_run_manifest(self, run_id: str) -> dict: # type: ignore
        """Load orchestration run manifest."""
        from config.paths import LAKE_ORCHESTRATION_MANIFESTS_DIR
        path = LAKE_ORCHESTRATION_MANIFESTS_DIR / f"{run_id}_manifest.json"
        return self._load_json(path)

    def save_orchestration_execution_plan(self, run_id: str, df: 'pd.DataFrame', summary: dict | None = None) -> 'Path':
        """Save orchestration execution plan."""
        from config.paths import LAKE_ORCHESTRATION_EXECUTION_PLANS_DIR
        path = LAKE_ORCHESTRATION_EXECUTION_PLANS_DIR / f"{run_id}_plan.parquet"
        self._save_parquet(df, path)
        if summary:
            summary_path = LAKE_ORCHESTRATION_EXECUTION_PLANS_DIR / f"{run_id}_plan_summary.json"
            self._save_json(summary, summary_path)
        return path

    def load_orchestration_execution_plan(self, run_id: str) -> 'pd.DataFrame':
        """Load orchestration execution plan."""
        from config.paths import LAKE_ORCHESTRATION_EXECUTION_PLANS_DIR
        path = LAKE_ORCHESTRATION_EXECUTION_PLANS_DIR / f"{run_id}_plan.parquet"
        return self._load_parquet(path)

    def save_orchestration_dependency_graph(self, run_id: str, df: 'pd.DataFrame', summary: dict | None = None) -> 'Path':
        """Save orchestration dependency graph."""
        from config.paths import LAKE_ORCHESTRATION_DEPENDENCY_GRAPHS_DIR
        path = LAKE_ORCHESTRATION_DEPENDENCY_GRAPHS_DIR / f"{run_id}_graph.parquet"
        self._save_parquet(df, path)
        if summary:
            summary_path = LAKE_ORCHESTRATION_DEPENDENCY_GRAPHS_DIR / f"{run_id}_graph_summary.json"
            self._save_json(summary, summary_path)
        return path

    def load_orchestration_dependency_graph(self, run_id: str) -> 'pd.DataFrame':
        """Load orchestration dependency graph."""
        from config.paths import LAKE_ORCHESTRATION_DEPENDENCY_GRAPHS_DIR
        path = LAKE_ORCHESTRATION_DEPENDENCY_GRAPHS_DIR / f"{run_id}_graph.parquet"
        return self._load_parquet(path)

    def save_orchestration_job_log(self, run_id: str, df: 'pd.DataFrame') -> 'Path':
        """Save orchestration job log."""
        from config.paths import LAKE_ORCHESTRATION_JOB_LOGS_DIR
        path = LAKE_ORCHESTRATION_JOB_LOGS_DIR / f"{run_id}_jobs.parquet"
        self._save_parquet(df, path)
        return path

    def load_orchestration_job_log(self, run_id: str) -> 'pd.DataFrame':
        """Load orchestration job log."""
        from config.paths import LAKE_ORCHESTRATION_JOB_LOGS_DIR
        path = LAKE_ORCHESTRATION_JOB_LOGS_DIR / f"{run_id}_jobs.parquet"
        return self._load_parquet(path)

    def save_orchestration_quality(self, run_id: str, quality: dict) -> 'Path':
        """Save orchestration quality report."""
        from config.paths import LAKE_ORCHESTRATION_QUALITY_DIR
        path = LAKE_ORCHESTRATION_QUALITY_DIR / f"{run_id}_quality.json"
        self._save_json(quality, path)
        return path

    def load_orchestration_quality(self, run_id: str) -> dict: # type: ignore
        """Load orchestration quality report."""
        from config.paths import LAKE_ORCHESTRATION_QUALITY_DIR
        path = LAKE_ORCHESTRATION_QUALITY_DIR / f"{run_id}_quality.json"
        return self._load_json(path)

    def list_orchestration_runs(self) -> 'pd.DataFrame':
        """List all available orchestration runs."""
        from config.paths import LAKE_ORCHESTRATION_MANIFESTS_DIR

        if not LAKE_ORCHESTRATION_MANIFESTS_DIR.exists():
             return pd.DataFrame()

        runs = []
        for p in LAKE_ORCHESTRATION_MANIFESTS_DIR.glob("*_manifest.json"):
             try:
                 manifest = self._load_json(p)
                 runs.append({
                     "run_id": manifest.get("run_id", p.stem.replace("_manifest", "")),
                     "workflow_name": manifest.get("workflow_name", "unknown"),
                     "profile_name": manifest.get("profile_name", "unknown"),
                     "timeframe": manifest.get("timeframe", "unknown"),
                     "started_at": manifest.get("started_at_utc", ""),
                     "status": manifest.get("workflow_status", "unknown"),
                     "job_count": manifest.get("job_count", 0),
                     "success_count": manifest.get("success_count", 0),
                     "failed_count": manifest.get("failed_count", 0),
                     "dry_run": manifest.get("dry_run", True)
                 })
             except Exception:
                 continue

        if not runs:
            return pd.DataFrame()

        df = pd.DataFrame(runs)
        if "started_at" in df.columns:
            df = df.sort_values("started_at", ascending=False).reset_index(drop=True)
        return df

    def list_notification_delivery_logs(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_NOTIFICATIONS_DELIVERY_LOGS_DIR.glob("*.parquet"))
        data = []
        for f in files:
            try:
                parts = f.stem.split("_")
                profile = parts[0] if len(parts) > 0 else "unknown"
                date_str = parts[-2] if len(parts) >= 2 else "unknown"
                data.append({
                    "profile_name": profile,
                    "date": date_str,
                    "file_path": str(f)
                })
            except Exception:
                pass

        return pd.DataFrame(data)

    # --- Observability Reports Save/Load ---
    def save_observability_health_report(self, report_name: str, df: pd.DataFrame, summary: dict) -> Path: # type: ignore
        """Save a health report to the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_HEALTH_DIR', self.root_dir / 'observability' / 'health')
        target_dir.mkdir(parents=True, exist_ok=True)

        csv_path = target_dir / f"{report_name}.csv"
        json_path = target_dir / f"{report_name}_summary.json"

        if not df.empty:
            df.to_csv(csv_path, index=False)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return csv_path

    def load_observability_health_report(self, report_name: str) -> pd.DataFrame:
        """Load a health report from the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_HEALTH_DIR', self.root_dir / 'observability' / 'health')
        csv_path = target_dir / f"{report_name}.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        return pd.DataFrame()

    def save_runtime_metrics(self, report_name: str, df: pd.DataFrame, summary: dict) -> Path: # type: ignore
        """Save runtime metrics to the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_RUNTIME_METRICS_DIR', self.root_dir / 'observability' / 'runtime_metrics')
        target_dir.mkdir(parents=True, exist_ok=True)

        csv_path = target_dir / f"{report_name}.csv"
        json_path = target_dir / f"{report_name}_summary.json"

        if not df.empty:
            df.to_csv(csv_path, index=False)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return csv_path

    def load_runtime_metrics(self, report_name: str) -> pd.DataFrame:
        """Load runtime metrics from the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_RUNTIME_METRICS_DIR', self.root_dir / 'observability' / 'runtime_metrics')
        csv_path = target_dir / f"{report_name}.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        return pd.DataFrame()

    def save_diagnostics_report(self, report_name: str, summary: dict) -> Path: # type: ignore
        """Save self-diagnostics summary to the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_DIAGNOSTICS_DIR', self.root_dir / 'observability' / 'diagnostics')
        target_dir.mkdir(parents=True, exist_ok=True)

        json_path = target_dir / f"{report_name}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return json_path

    def load_diagnostics_report(self, report_name: str) -> dict: # type: ignore
        """Load self-diagnostics summary from the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_DIAGNOSTICS_DIR', self.root_dir / 'observability' / 'diagnostics')
        json_path = target_dir / f"{report_name}.json"
        if json_path.exists():
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_error_taxonomy_report(self, df: pd.DataFrame, summary: dict) -> Path: # type: ignore
        """Save error taxonomy to the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_ERROR_TAXONOMY_DIR', self.root_dir / 'observability' / 'error_taxonomy')
        target_dir.mkdir(parents=True, exist_ok=True)

        csv_path = target_dir / "error_taxonomy.csv"
        json_path = target_dir / "error_taxonomy_summary.json"

        if not df.empty:
            df.to_csv(csv_path, index=False)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return csv_path

    def load_error_taxonomy_report(self) -> pd.DataFrame:
        """Load error taxonomy from the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_ERROR_TAXONOMY_DIR', self.root_dir / 'observability' / 'error_taxonomy')
        csv_path = target_dir / "error_taxonomy.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        return pd.DataFrame()

    def save_data_freshness_report(self, df: pd.DataFrame, summary: dict) -> Path: # type: ignore
        """Save data freshness report to the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_DATA_FRESHNESS_DIR', self.root_dir / 'observability' / 'data_freshness')
        target_dir.mkdir(parents=True, exist_ok=True)

        csv_path = target_dir / "data_freshness.csv"
        json_path = target_dir / "data_freshness_summary.json"

        if not df.empty:
            df.to_csv(csv_path, index=False)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return csv_path

    def load_data_freshness_report(self) -> pd.DataFrame:
        """Load data freshness report from the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_DATA_FRESHNESS_DIR', self.root_dir / 'observability' / 'data_freshness')
        csv_path = target_dir / "data_freshness.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        return pd.DataFrame()

    def save_artifact_integrity_report(self, df: pd.DataFrame, summary: dict) -> Path: # type: ignore
        """Save artifact integrity report to the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_ARTIFACT_INTEGRITY_DIR', self.root_dir / 'observability' / 'artifact_integrity')
        target_dir.mkdir(parents=True, exist_ok=True)

        csv_path = target_dir / "artifact_integrity.csv"
        json_path = target_dir / "artifact_integrity_summary.json"

        if not df.empty:
            df.to_csv(csv_path, index=False)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return csv_path

    def load_artifact_integrity_report(self) -> pd.DataFrame:
        """Load artifact integrity report from the observability lake."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_ARTIFACT_INTEGRITY_DIR', self.root_dir / 'observability' / 'artifact_integrity')
        csv_path = target_dir / "artifact_integrity.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        return pd.DataFrame()

    def save_observability_quality(self, report_name: str, quality: dict) -> Path: # type: ignore
        """Save observability quality check results."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_QUALITY_DIR', self.root_dir / 'observability' / 'quality')
        target_dir.mkdir(parents=True, exist_ok=True)

        json_path = target_dir / f"{report_name}_quality.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(quality, f, indent=2, ensure_ascii=False)

        return json_path

    def load_observability_quality(self, report_name: str) -> dict: # type: ignore
        """Load observability quality check results."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_QUALITY_DIR', self.root_dir / 'observability' / 'quality')
        json_path = target_dir / f"{report_name}_quality.json"
        if json_path.exists():
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def list_observability_reports(self) -> pd.DataFrame:
        """List all available observability reports."""
        target_dir = getattr(self.paths, 'LAKE_OBSERVABILITY_DIR', self.root_dir / 'observability')

        if not target_dir.exists():
            return pd.DataFrame()

        rows = []
        for file in target_dir.rglob("*"):
            if file.is_file() and file.suffix in ['.csv', '.json']:
                report_type = file.parent.name
                rows.append({
                    "report_type": report_type,
                    "filename": file.name,
                    "modified_time": pd.Timestamp(file.stat().st_mtime, unit='s'),
                    "path": str(file)
                })

        if not rows:
            return pd.DataFrame()

        df = pd.DataFrame(rows)
        return df.sort_values(by="modified_time", ascending=False)

    # --- Phase 37: Security ---
    def save_security_audit_report(self, report_name: str, df: pd.DataFrame, summary: dict) -> Path: # type: ignore
        self.paths.security_audits.mkdir(parents=True, exist_ok=True)
        csv_path = self.paths.security_audits / f"{report_name}.csv"
        json_path = self.paths.security_audits / f"{report_name}.json"
        if not df.empty:
            df.to_csv(csv_path, index=False)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
        return csv_path

    def load_security_audit_report(self, report_name: str) -> pd.DataFrame:
        csv_path = self.paths.security_audits / f"{report_name}.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        return pd.DataFrame()

    def save_secret_hygiene_report(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("secret_hygiene", df, summary)
    def load_secret_hygiene_report(self) -> pd.DataFrame:
        return self.load_security_audit_report("secret_hygiene")
    def save_config_hardening_report(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("config_hardening", df, summary)
    def load_config_hardening_report(self) -> pd.DataFrame:
        return self.load_security_audit_report("config_hardening")
    def save_safe_defaults_report(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("safe_defaults", df, summary)
    def load_safe_defaults_report(self) -> pd.DataFrame:
        return self.load_security_audit_report("safe_defaults")
    def save_permission_boundary_report(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("permission_boundaries", df, summary)
    def load_permission_boundary_report(self) -> pd.DataFrame:
        return self.load_security_audit_report("permission_boundaries")
    def save_path_safety_report(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("path_safety", df, summary)
    def save_token_scan_report(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("token_scan", df, summary)
    def load_token_scan_report(self) -> pd.DataFrame:
        return self.load_security_audit_report("token_scan")
    def save_readiness_audit(self, df: pd.DataFrame, summary: dict) -> Path:
        return self.save_security_audit_report("readiness_audit", df, summary)
    def load_readiness_audit(self) -> pd.DataFrame:
        return self.load_security_audit_report("readiness_audit")

    def save_security_quality(self, report_name: str, quality: dict) -> Path: # type: ignore
        self.paths.security_quality.mkdir(parents=True, exist_ok=True)
        json_path = self.paths.security_quality / f"{report_name}_quality.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=2)
        return json_path

    def load_security_quality(self, report_name: str) -> dict: # type: ignore
        json_path = self.paths.security_quality / f"{report_name}_quality.json"
        if json_path.exists():
            with open(json_path, "r", encoding="utf-8") as f: return json.load(f)
        return {}

    def list_security_reports(self) -> pd.DataFrame: return pd.DataFrame()


    # Phase 42: Portfolio Regime Research
    def save_portfolio_regimes(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_df(df, self.paths.portfolio_regime_regimes / f"regimes_{timeframe}_{profile_name}.parquet")

    def load_portfolio_regimes(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_regimes / f"regimes_{timeframe}_{profile_name}.parquet")

    def save_regime_conditioned_returns(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_df(df, self.paths.portfolio_regime_conditioned_returns / f"conditioned_returns_{timeframe}_{profile_name}.parquet")

    def load_regime_conditioned_returns(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_conditioned_returns / f"conditioned_returns_{timeframe}_{profile_name}.parquet")

    def save_regime_correlation_summary(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_df(df, self.paths.portfolio_regime_correlation / f"correlation_{timeframe}_{profile_name}.parquet")

    def load_regime_correlation_summary(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_correlation / f"correlation_{timeframe}_{profile_name}.parquet")

    def save_macro_scenario_sensitivity(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_df(df, self.paths.portfolio_regime_scenarios / f"scenario_sensitivity_{timeframe}_{profile_name}.parquet")

    def load_macro_scenario_sensitivity(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_scenarios / f"scenario_sensitivity_{timeframe}_{profile_name}.parquet")

    def save_basket_stress_test_results(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_df(df, self.paths.portfolio_regime_stress_tests / f"stress_test_{timeframe}_{profile_name}.parquet")

    def load_basket_stress_test_results(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_stress_tests / f"stress_test_{timeframe}_{profile_name}.parquet")

    def save_drawdown_clusters(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_df(df, self.paths.portfolio_regime_drawdowns / f"drawdown_clusters_{timeframe}_{profile_name}.parquet")

    def load_drawdown_clusters(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_drawdowns / f"drawdown_clusters_{timeframe}_{profile_name}.parquet")

    def save_recovery_analysis(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_df(df, self.paths.portfolio_regime_recovery / f"recovery_analysis_{timeframe}_{profile_name}.parquet")

    def load_recovery_analysis(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_recovery / f"recovery_analysis_{timeframe}_{profile_name}.parquet")

    def save_tail_risk_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_df(df, self.paths.portfolio_regime_tail_risk / f"tail_risk_{timeframe}_{profile_name}.parquet")

    def load_tail_risk_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_tail_risk / f"tail_risk_{timeframe}_{profile_name}.parquet")

    def save_risk_regime_exposure(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        return self._save_df(df, self.paths.portfolio_regime_exposure / f"exposure_{timeframe}_{profile_name}.parquet")

    def load_risk_regime_exposure(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        return self._load_df(self.paths.portfolio_regime_exposure / f"exposure_{timeframe}_{profile_name}.parquet")

    def save_portfolio_regime_report(self, timeframe: str, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        import json
        path = self.paths.portfolio_regime_reports / f"regime_report_{timeframe}_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        if markdown:
            md_path = self.paths.portfolio_regime_reports / f"regime_report_{timeframe}_{profile_name}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown)
        return path

    def load_portfolio_regime_report(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        import json
        path = self.paths.portfolio_regime_reports / f"regime_report_{timeframe}_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_portfolio_regime_quality(self, timeframe: str, profile_name: str, quality: dict) -> Path: # type: ignore
        import json
        path = self.paths.portfolio_regime_quality / f"quality_{timeframe}_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=2)
        return path

    def load_portfolio_regime_quality(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        import json
        path = self.paths.portfolio_regime_quality / f"quality_{timeframe}_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_portfolio_regime_reports(self) -> pd.DataFrame:
        return pd.DataFrame()

    # Phase 43: Synthetic Indices
    def save_synthetic_index_definitions(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_definitions / f"definitions_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_index_definitions(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_definitions / f"definitions_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_index_levels(self, index_id: str, timeframe: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_levels / f"{index_id}_{timeframe}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_index_levels(self, index_id: str, timeframe: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_levels / f"{index_id}_{timeframe}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_index_returns(self, index_id: str, timeframe: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_returns / f"{index_id}_{timeframe}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_index_returns(self, index_id: str, timeframe: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_returns / f"{index_id}_{timeframe}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_relative_strength_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_relative_strength / f"relative_strength_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_relative_strength_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_relative_strength / f"relative_strength_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_relative_momentum_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_relative_momentum / f"relative_momentum_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_relative_momentum_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_relative_momentum / f"relative_momentum_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_universe_rotation_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_rotation / f"universe_rotation_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_universe_rotation_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_rotation / f"universe_rotation_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_leadership_laggard_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_leadership / f"leadership_laggard_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_leadership_laggard_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_leadership / f"leadership_laggard_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_benchmark_comparison(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_comparisons / f"benchmark_comparison_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_benchmark_comparison(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_comparisons / f"benchmark_comparison_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_index_performance(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        path = self.paths.synthetic_indices_performance / f"index_performance_{timeframe}_{profile_name}.parquet"
        if not df.empty:
            df.to_parquet(path)
        return path

    def load_synthetic_index_performance(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.synthetic_indices_performance / f"index_performance_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_synthetic_index_quality(self, timeframe: str, profile_name: str, quality: dict) -> Path: # type: ignore
        path = self.paths.synthetic_indices_quality / f"quality_{timeframe}_{profile_name}.json"
        import json
        with open(path, "w") as f:
            json.dump(quality, f, indent=2)
        return path

    def load_synthetic_index_quality(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.synthetic_indices_quality / f"quality_{timeframe}_{profile_name}.json"
        if path.exists():
            import json
            with open(path, "r") as f:
                return json.load(f)
        return {}

    def save_synthetic_index_report(self, timeframe: str, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        path = self.paths.synthetic_indices_reports / f"report_{timeframe}_{profile_name}.json"
        import json
        with open(path, "w") as f:
            json.dump(report, f, indent=2)

        if markdown:
             md_path = self.paths.synthetic_indices_reports_markdown / f"report_{timeframe}_{profile_name}.md"
             with open(md_path, "w") as f:
                 f.write(markdown)

        return path

    def load_synthetic_index_report(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.synthetic_indices_reports / f"report_{timeframe}_{profile_name}.json"
        if path.exists():
            import json
            with open(path, "r") as f:
                return json.load(f)
        return {}

    def list_synthetic_index_reports(self) -> pd.DataFrame:
        records = []
        if self.paths.synthetic_indices_reports.exists():
            import json
            for path in self.paths.synthetic_indices_reports.glob("*.json"):
                try:
                    with open(path, "r") as f:
                        data = json.load(f)
                        records.append({
                            "file": path.name,
                            "timeframe": data.get("timeframe"),
                            "profile": data.get("profile"),
                            "timestamp": data.get("timestamp")
                        })
                except Exception:
                    pass
        return pd.DataFrame(records)

    # --- Phase 45: Meta Research ---

    def save_meta_evidence_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_EVIDENCE_DIR / f"evidence_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_evidence_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_EVIDENCE_DIR / f"evidence_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_source_reliability(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_RELIABILITY_DIR / f"reliability_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_source_reliability(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_RELIABILITY_DIR / f"reliability_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_consensus_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_CONSENSUS_DIR / f"consensus_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_consensus_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_CONSENSUS_DIR / f"consensus_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_conflict_report(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_CONFLICTS_DIR / f"conflicts_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_conflict_report(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_CONFLICTS_DIR / f"conflicts_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_uncertainty_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_UNCERTAINTY_DIR / f"uncertainty_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_uncertainty_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_UNCERTAINTY_DIR / f"uncertainty_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_ensemble_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_ENSEMBLE_DIR / f"ensemble_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_ensemble_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_ENSEMBLE_DIR / f"ensemble_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_quality_adjusted_ranking(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_RANKINGS_DIR / f"ranking_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_quality_adjusted_ranking(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_RANKINGS_DIR / f"ranking_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_symbol_snapshot(self, symbol: str, timeframe: str, profile_name: str, snapshot: dict) -> Path: # type: ignore
        path = self.paths.LAKE_META_RESEARCH_SNAPSHOTS_DIR / f"snapshot_{symbol}_{timeframe}_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            import json
            json.dump(snapshot, f, indent=2, ensure_ascii=False)
        return path

    def load_meta_symbol_snapshot(self, symbol: str, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.LAKE_META_RESEARCH_SNAPSHOTS_DIR / f"snapshot_{symbol}_{timeframe}_{profile_name}.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                import json
                return json.load(f)
        return {}

    def save_meta_quality(self, timeframe: str, profile_name: str, quality: dict) -> Path: # type: ignore
        path = self.paths.LAKE_META_RESEARCH_QUALITY_DIR / f"quality_{timeframe}_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            import json
            json.dump(quality, f, indent=2, ensure_ascii=False)
        return path

    def load_meta_quality(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.LAKE_META_RESEARCH_QUALITY_DIR / f"quality_{timeframe}_{profile_name}.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                import json
                return json.load(f)
        return {}


    # Phase 46: Experiment Tracking Load/Save
    def save_hypothesis_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        out_file = self.paths.experiments_hypotheses / "hypothesis_registry.jsonl"
        # Not implementing full save here to keep the patch small, assuming managed by HypothesisRegistry
        return out_file

    def load_hypothesis_registry(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_definitions(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        return self.paths.experiments_definitions / "definitions.csv"

    def load_experiment_definitions(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_run_manifest(self, run_id: str, manifest: dict) -> Path: # type: ignore
        out_file = self.paths.experiments_runs / f"run_{run_id}.json"
        self._save_json(out_file, manifest)
        return out_file

    def load_experiment_run_manifest(self, run_id: str) -> dict: # type: ignore
        return {}

    def save_experiment_artifact_manifest(self, run_id: str, manifest: dict) -> Path: # type: ignore
        out_file = self.paths.experiments_artifacts / f"artifacts_{run_id}.json"
        self._save_json(out_file, manifest)
        return out_file

    def load_experiment_artifact_manifest(self, run_id: str) -> dict: # type: ignore
        return {}

    def save_reproducibility_manifest(self, run_id: str, manifest: dict) -> Path: # type: ignore
        out_file = self.paths.experiments_reproducibility / f"repro_{run_id}.json"
        self._save_json(out_file, manifest)
        return out_file

    def load_reproducibility_manifest(self, run_id: str) -> dict: # type: ignore
        return {}

    def save_research_version_record(self, version_id: str, record: dict) -> Path: # type: ignore
        out_file = self.paths.experiments_versions / f"version_{version_id}.json"
        self._save_json(out_file, record)
        return out_file

    def load_research_version_record(self, version_id: str) -> dict: # type: ignore
        return {}

    def save_ablation_study_results(self, study_id: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        out_file = self.paths.experiments_ablation / f"{study_id}.csv"
        df.to_csv(out_file, index=False)
        return out_file

    def load_ablation_study_results(self, study_id: str) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_comparison_table(self, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        out_file = self.paths.experiments_comparisons / f"{profile_name}_comparisons.csv"
        df.to_csv(out_file, index=False)
        return out_file

    def load_experiment_comparison_table(self, profile_name: str) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_leaderboard(self, profile_name: str, df: pd.DataFrame) -> Path: # type: ignore
        out_file = self.paths.experiments_leaderboards / f"{profile_name}_leaderboard.csv"
        df.to_csv(out_file, index=False)
        return out_file

    def load_experiment_leaderboard(self, profile_name: str) -> pd.DataFrame:
        return pd.DataFrame()

    def save_experiment_quality(self, run_id_or_profile: str, quality: dict) -> Path: # type: ignore
        out_file = self.paths.experiments_quality / f"{run_id_or_profile}_quality.json"
        self._save_json(out_file, quality)
        return out_file

    def load_experiment_quality(self, run_id_or_profile: str) -> dict: # type: ignore
        return {}

    def save_experiment_tracking_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        out_file = self.paths.experiments_reports_json / f"{profile_name}_report.json"
        self._save_json(out_file, report)
        return out_file

    def load_experiment_tracking_report(self, profile_name: str) -> dict: # type: ignore
        return {}

    def list_experiment_runs(self) -> pd.DataFrame:
        return pd.DataFrame()

    def list_experiment_reports(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_meta_research_report(self, timeframe: str, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        json_path = self.paths.LAKE_META_RESEARCH_REPORTS_DIR / f"report_{timeframe}_{profile_name}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            import json
            json.dump(report, f, indent=2, ensure_ascii=False)

        if markdown:
            md_path = self.paths.REPORTS_META_RESEARCH_MD_DIR / f"meta_research_{timeframe}_{profile_name}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown)

        return json_path

    def load_meta_research_report(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        path = self.paths.LAKE_META_RESEARCH_REPORTS_DIR / f"report_{timeframe}_{profile_name}.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                import json
                return json.load(f)
        return {}

    def list_meta_research_reports(self) -> pd.DataFrame:
        rows = []
        for p in self.paths.LAKE_META_RESEARCH_REPORTS_DIR.glob("report_*.json"):
            parts = p.stem.split("_", 2)
            if len(parts) >= 3:
                timeframe = parts[1]
                profile = parts[2]
                rows.append({
                    "timeframe": timeframe,
                    "profile": profile,
                    "path": str(p),
                    "size": p.stat().st_size
                })
        return pd.DataFrame(rows) if rows else pd.DataFrame(columns=["timeframe", "profile", "path", "size"])


    # Phase 48: Research Planning
    def save_research_planning_signals(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_SIGNALS_DIR / f"signals_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_research_planning_signals(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_SIGNALS_DIR / f"signals_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_task_registry(self, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_TASKS_DIR / f"tasks_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_research_task_registry(self, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_TASKS_DIR / f"tasks_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_backlog(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_BACKLOG_DIR / f"backlog_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_research_backlog(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_BACKLOG_DIR / f"backlog_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_priority_scores(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_PRIORITIES_DIR / f"priorities_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_research_priority_scores(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_PRIORITIES_DIR / f"priorities_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_next_best_experiments(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_NEXT_BEST_DIR / f"next_best_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_next_best_experiments(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_NEXT_BEST_DIR / f"next_best_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_debt_report(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_DEBT_DIR / f"debt_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_research_debt_report(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_DEBT_DIR / f"debt_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_opportunity_report(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_OPPORTUNITIES_DIR / f"opportunities_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_research_opportunity_report(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_OPPORTUNITIES_DIR / f"opportunities_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_roadmap_health_snapshot(self, timeframe: str, profile_name: str, snapshot: dict) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_ROADMAP_DIR / f"roadmap_{timeframe}_{profile_name}.json"
        self._save_json(snapshot, filepath)
        return filepath

    def load_roadmap_health_snapshot(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_ROADMAP_DIR / f"roadmap_{timeframe}_{profile_name}.json"
        return self._load_json(filepath)

    def save_task_dependency_table(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_DEPENDENCIES_DIR / f"dependencies_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_task_dependency_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_DEPENDENCIES_DIR / f"dependencies_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_milestone_tracking_table(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_MILESTONES_DIR / f"milestones_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_milestone_tracking_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_MILESTONES_DIR / f"milestones_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_task_orchestration_plan(self, timeframe: str, profile_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_ORCHESTRATION_DIR / f"orchestration_{timeframe}_{profile_name}.parquet"
        self._save_parquet(df, filepath)
        if summary:
            self._save_json(summary, filepath.with_suffix(".json"))
        return filepath

    def load_task_orchestration_plan(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        filepath = self.paths.LAKE_RESEARCH_PLANNING_ORCHESTRATION_DIR / f"orchestration_{timeframe}_{profile_name}.parquet"
        return self._load_parquet(filepath)

    def save_research_planning_quality(self, timeframe: str, profile_name: str, quality: dict) -> Path: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_QUALITY_DIR / f"quality_{timeframe}_{profile_name}.json"
        self._save_json(quality, filepath)
        return filepath

    def load_research_planning_quality(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        filepath = self.paths.LAKE_RESEARCH_PLANNING_QUALITY_DIR / f"quality_{timeframe}_{profile_name}.json"
        return self._load_json(filepath)

    def save_research_planning_report(self, timeframe: str, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        filepath = self.paths.REPORTS_RESEARCH_PLANNING_JSON_DIR / f"report_{timeframe}_{profile_name}.json"
        self._save_json(report, filepath)
        if markdown:
            md_path = self.paths.REPORTS_RESEARCH_PLANNING_MARKDOWN_DIR / f"report_{timeframe}_{profile_name}.md"
            self._save_text(markdown, md_path)
        return filepath

    def load_research_planning_report(self, timeframe: str, profile_name: str) -> dict: # type: ignore
        filepath = self.paths.REPORTS_RESEARCH_PLANNING_JSON_DIR / f"report_{timeframe}_{profile_name}.json"
        return self._load_json(filepath)

    def list_research_planning_reports(self) -> pd.DataFrame:
        files = list(self.paths.REPORTS_RESEARCH_PLANNING_JSON_DIR.glob("*.json"))
        data = []
        for f in files:
            parts = f.stem.split("_")
            if len(parts) >= 3:
                data.append({"timeframe": parts[1], "profile": "_".join(parts[2:]), "file": f.name})
        return pd.DataFrame(data)


    # Phase 49 Knowledge Base Methods
    def save_knowledge_documents(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_DOCUMENTS_DIR / "documents.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_DOCUMENTS_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_knowledge_documents(self) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_DOCUMENTS_DIR / "documents.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_knowledge_chunks(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_CHUNKS_DIR / "chunks.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_CHUNKS_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_knowledge_chunks(self) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_CHUNKS_DIR / "chunks.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_knowledge_index_summary(self, summary: dict) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_INDEXES_DIR / "index_summary.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        return p

    def load_knowledge_index_summary(self) -> dict: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_INDEXES_DIR / "index_summary.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_retrieval_results(self, query_id: str, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_RETRIEVAL_DIR / f"results_{query_id}.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_RETRIEVAL_DIR / f"summary_{query_id}.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_retrieval_results(self, query_id: str) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_RETRIEVAL_DIR / f"results_{query_id}.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_memory_cards(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / "memory_cards.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_memory_cards(self) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / "memory_cards.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_symbol_memory_card(self, symbol: str, card: dict) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / f"card_{symbol}.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(card, f, indent=2)
        return p

    def load_symbol_memory_card(self, symbol: str) -> dict: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_MEMORY_CARDS_DIR / f"card_{symbol}.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_decision_journal(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_DECISION_JOURNAL_DIR / "decision_journal.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_DECISION_JOURNAL_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_decision_journal(self) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_DECISION_JOURNAL_DIR / "decision_journal.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_analyst_notes(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_ANALYST_NOTES_DIR / "analyst_notes.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_ANALYST_NOTES_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_analyst_notes(self) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_ANALYST_NOTES_DIR / "analyst_notes.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_recent_findings_digest(self, df: pd.DataFrame, summary: dict | None = None) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_FINDINGS_DIR / "recent_findings.parquet"
        if not df.empty:
            df.to_parquet(p)
        if summary:
            s_path = self.paths.LAKE_KNOWLEDGE_BASE_FINDINGS_DIR / "summary.json"
            with open(s_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
        return p

    def load_recent_findings_digest(self) -> pd.DataFrame:
        p = self.paths.LAKE_KNOWLEDGE_BASE_FINDINGS_DIR / "recent_findings.parquet"
        if p.exists():
            return pd.read_parquet(p)
        return pd.DataFrame()

    def save_workspace_summary(self, summary: dict) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_WORKSPACE_DIR / "workspace_summary.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        return p

    def load_workspace_summary(self) -> dict: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_WORKSPACE_DIR / "workspace_summary.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_kb_quality(self, profile_name: str, quality: dict) -> Path: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_QUALITY_DIR / f"quality_{profile_name}.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(quality, f, indent=2)
        return p

    def load_kb_quality(self, profile_name: str) -> dict: # type: ignore
        p = self.paths.LAKE_KNOWLEDGE_BASE_QUALITY_DIR / f"quality_{profile_name}.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_knowledge_base_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path: # type: ignore
        p = self.paths.REPORTS_KNOWLEDGE_BASE_JSON_DIR / f"report_{profile_name}.json"
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)

        if markdown:
            md_p = self.paths.REPORTS_KNOWLEDGE_BASE_MARKDOWN_DIR / f"report_{profile_name}.md"
            with open(md_p, 'w', encoding='utf-8') as f:
                f.write(markdown)

            txt_p = self.paths.REPORTS_KNOWLEDGE_BASE_TXT_DIR / f"report_{profile_name}.txt"
            with open(txt_p, 'w', encoding='utf-8') as f:
                f.write(markdown) # Use markdown as text for now

        return p

    def load_knowledge_base_report(self, profile_name: str) -> dict: # type: ignore
        p = self.paths.REPORTS_KNOWLEDGE_BASE_JSON_DIR / f"report_{profile_name}.json"
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def list_knowledge_base_reports(self) -> pd.DataFrame:
        d = self.paths.REPORTS_KNOWLEDGE_BASE_JSON_DIR
        reports = []
        if d.exists():
            for p in d.glob("report_*.json"):
                profile_name = p.stem.replace("report_", "")
                with open(p, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        reports.append({
                            "profile_name": profile_name,
                            "file": p.name
                        })
                    except Exception:
                        pass
        return pd.DataFrame(reports)

    def save_runtime_profiles(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_RUNTIME.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_RUNTIME / f"runtime_profiles_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_runtime_profiles(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_RUNTIME.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_memory_profiles(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_MEMORY.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_MEMORY / f"memory_profiles_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_memory_profiles(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_MEMORY.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_cpu_gpu_awareness(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_CPU_GPU.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CPU_GPU / f"cpu_gpu_awareness_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_cpu_gpu_awareness(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_CPU_GPU.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_resource_budgets(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_BUDGET.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_BUDGET / f"resource_budgets_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_resource_budgets(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_BUDGET.glob("resource_budgets_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_resource_budget_violations(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_BUDGET.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_BUDGET / f"violations_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_resource_budget_violations(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_BUDGET.glob("violations_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_cache_inventory(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_CACHE.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CACHE / f"inventory_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_cache_inventory(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_CACHE.glob("inventory_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_cache_strategy(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_CACHE.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CACHE / f"strategy_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_cache_strategy(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_CACHE.glob("strategy_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_cache_hit_miss_report(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_CACHE.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CACHE / f"hit_miss_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_cache_hit_miss_report(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_CACHE.glob("hit_miss_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_batch_plans(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_BATCH_PLANS.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_BATCH_PLANS / f"batch_plans_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_batch_plans(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_BATCH_PLANS.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_checkpoint_manifest(self, manifest_name: str, manifest: dict) -> Path:
        self.paths.LAKE_PERFORMANCE_CHECKPOINTS.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CHECKPOINTS / f"{manifest_name}.json"
        import json
        with open(path, "w") as f:
            json.dump(manifest, f)
        return path

    def load_checkpoint_manifest(self, manifest_name: str) -> dict:
        path = self.paths.LAKE_PERFORMANCE_CHECKPOINTS / f"{manifest_name}.json"
        if not path.exists(): return {}
        import json
        with open(path, "r") as f:
            return json.load(f)

    def save_large_run_stability_report(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_STABILITY.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_STABILITY / f"stability_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_large_run_stability_report(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_STABILITY.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_bottleneck_report(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_BOTTLENECKS.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_BOTTLENECKS / f"bottleneck_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_bottleneck_report(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_BOTTLENECKS.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_optimization_recommendations(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_OPTIMIZATION.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_OPTIMIZATION / f"optimization_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_optimization_recommendations(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_OPTIMIZATION.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_performance_quality(self, profile_name: str, quality: dict) -> Path:
        self.paths.LAKE_PERFORMANCE_QUALITY.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_QUALITY / f"{profile_name}_quality_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json"
        import json
        with open(path, "w") as f:
            json.dump(quality, f)
        return path

    def load_performance_quality(self, profile_name: str) -> dict:
        files = list(self.paths.LAKE_PERFORMANCE_QUALITY.glob(f"{profile_name}_quality_*.json"))
        if not files: return {}
        latest = max(files, key=os.path.getctime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def save_performance_report(self, profile_name: str, report: dict, markdown: Optional[str] = None) -> Path:
        self.paths.REPORTS_PERFORMANCE_JSON.mkdir(parents=True, exist_ok=True)
        path = self.paths.REPORTS_PERFORMANCE_JSON / f"{profile_name}_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json"
        import json
        with open(path, "w") as f:
            json.dump(report, f)

        if markdown:
            self.paths.REPORTS_PERFORMANCE_MARKDOWN.mkdir(parents=True, exist_ok=True)
            md_path = self.paths.REPORTS_PERFORMANCE_MARKDOWN / f"{profile_name}_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.md"
            with open(md_path, "w") as f:
                f.write(markdown)

        return path

    def load_performance_report(self, profile_name: str) -> dict:
        files = list(self.paths.REPORTS_PERFORMANCE_JSON.glob(f"{profile_name}_report_*.json"))
        if not files: return {}
        latest = max(files, key=os.path.getctime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def list_performance_reports(self) -> pd.DataFrame:
        files = list(self.paths.REPORTS_PERFORMANCE_JSON.glob("*.json"))
        if not files: return pd.DataFrame()
        records = []
        for f in files:
            records.append({
                "name": f.stem,
                "path": str(f),
                "created_at": datetime.fromtimestamp(os.path.getctime(f)).isoformat()
            })
        return pd.DataFrame(records)


    # --- MAINTENANCE SUPPORT ---
    def save_storage_inventory(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_INVENTORY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "inventory")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"storage_inventory_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_inventory(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_INVENTORY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "inventory")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_retention_policies(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_POLICIES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "policies")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"retention_policies_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_retention_policies(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_POLICIES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "policies")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cleanup_candidates(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cleanup_candidates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cleanup_candidates(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cleanup_candidates_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cleanup_dry_run_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cleanup_plan_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cleanup_dry_run_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cleanup_plan_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_archive_candidates(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"archive_candidates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_archive_candidates(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("archive_candidates_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_archive_manifest(self, archive_id: str, manifest: dict) -> Path:
        out_dir = getattr(self.paths, "ARCHIVES_MANIFESTS_DIR", self.paths.PROJECT_ROOT / "archives" / "manifests")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"{archive_id}.json"
        with open(path, "w") as f:
            json.dump(manifest, f, indent=2)
        return path

    def load_archive_manifest(self, archive_id: str) -> dict:
        import json
        out_dir = getattr(self.paths, "ARCHIVES_MANIFESTS_DIR", self.paths.PROJECT_ROOT / "archives" / "manifests")
        path = out_dir / f"{archive_id}.json"
        if not path.exists():
            return {}
        with open(path, "r") as f:
            return json.load(f)

    def save_archive_dry_run_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"archive_plan_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_archive_dry_run_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("archive_plan_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_report_rotation_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"report_rotation_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_report_rotation_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("report_rotation_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_log_rotation_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"log_rotation_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_log_rotation_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("log_rotation_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cache_pruning_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cache_pruning_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cache_pruning_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cache_pruning_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_duplicate_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_DUPLICATES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "duplicates")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"duplicates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_duplicate_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_DUPLICATES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "duplicates")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_stale_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_STALE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "stale")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"stale_artifacts_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_stale_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_STALE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "stale")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_large_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_LARGE_ARTIFACTS_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "large_artifacts")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"large_artifacts_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_large_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_LARGE_ARTIFACTS_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "large_artifacts")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_storage_growth_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"storage_growth_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_growth_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("storage_growth_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_storage_growth_snapshot(self, snapshot: dict) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"snapshot_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(snapshot, f)
        return path

    def load_storage_growth_snapshots(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("snapshot_*.json"))
        if not files:
            return pd.DataFrame()
        import json
        data = []
        for f in files:
            with open(f, "r") as fp:
                data.append(json.load(fp))
        return pd.DataFrame(data)

    def save_storage_lifecycle_health(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_LIFECYCLE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "lifecycle")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"lifecycle_health_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_lifecycle_health(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_LIFECYCLE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "lifecycle")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_maintenance_quality(self, profile_name: str, quality: dict) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_QUALITY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "quality")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"quality_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(quality, f, indent=2)
        return path

    def load_maintenance_quality(self, profile_name: str) -> dict:
        out_dir = getattr(self.paths, "MAINTENANCE_QUALITY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "quality")
        if not out_dir.exists():
            return {}
        files = list(out_dir.glob(f"quality_{profile_name}_*.json"))
        if not files:
            return {}
        latest = max(files, key=lambda f: f.stat().st_mtime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def save_maintenance_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"maintenance_report_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(report, f, indent=2)

        if markdown:
            md_dir = getattr(self.paths, "REPORTS_MAINTENANCE_MARKDOWN_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "markdown")
            md_dir.mkdir(parents=True, exist_ok=True)
            md_path = md_dir / f"maintenance_report_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.md"
            with open(md_path, "w") as f:
                f.write(markdown)

        return path

    def load_maintenance_report(self, profile_name: str) -> dict:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        if not out_dir.exists():
            return {}
        files = list(out_dir.glob(f"maintenance_report_{profile_name}_*.json"))
        if not files:
            return {}
        latest = max(files, key=lambda f: f.stat().st_mtime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def list_maintenance_reports(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.json"))
        records = []
        for f in files:
            records.append({
                "file_name": f.name,
                "modified_at": datetime.fromtimestamp(f.stat().st_mtime).isoformat()
            })
        return pd.DataFrame(records)



    # --- MAINTENANCE SUPPORT ---
    def save_storage_inventory(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_INVENTORY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "inventory")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"storage_inventory_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_inventory(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_INVENTORY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "inventory")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_retention_policies(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_POLICIES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "policies")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"retention_policies_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_retention_policies(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_POLICIES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "policies")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cleanup_candidates(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cleanup_candidates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cleanup_candidates(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cleanup_candidates_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cleanup_dry_run_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cleanup_plan_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cleanup_dry_run_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cleanup_plan_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_archive_candidates(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"archive_candidates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_archive_candidates(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("archive_candidates_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_archive_manifest(self, archive_id: str, manifest: dict) -> Path:
        out_dir = getattr(self.paths, "ARCHIVES_MANIFESTS_DIR", self.paths.PROJECT_ROOT / "archives" / "manifests")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"{archive_id}.json"
        with open(path, "w") as f:
            json.dump(manifest, f, indent=2)
        return path

    def load_archive_manifest(self, archive_id: str) -> dict:
        import json
        out_dir = getattr(self.paths, "ARCHIVES_MANIFESTS_DIR", self.paths.PROJECT_ROOT / "archives" / "manifests")
        path = out_dir / f"{archive_id}.json"
        if not path.exists():
            return {}
        with open(path, "r") as f:
            return json.load(f)

    def save_archive_dry_run_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"archive_plan_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_archive_dry_run_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("archive_plan_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_report_rotation_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"report_rotation_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_report_rotation_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("report_rotation_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_log_rotation_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"log_rotation_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_log_rotation_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("log_rotation_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cache_pruning_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cache_pruning_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cache_pruning_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cache_pruning_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_duplicate_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_DUPLICATES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "duplicates")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"duplicates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_duplicate_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_DUPLICATES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "duplicates")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_stale_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_STALE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "stale")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"stale_artifacts_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_stale_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_STALE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "stale")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_large_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_LARGE_ARTIFACTS_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "large_artifacts")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"large_artifacts_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_large_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_LARGE_ARTIFACTS_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "large_artifacts")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_storage_growth_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"storage_growth_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_growth_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("storage_growth_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_storage_growth_snapshot(self, snapshot: dict) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"snapshot_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(snapshot, f)
        return path

    def load_storage_growth_snapshots(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("snapshot_*.json"))
        if not files:
            return pd.DataFrame()
        import json
        data = []
        for f in files:
            with open(f, "r") as fp:
                data.append(json.load(fp))
        return pd.DataFrame(data)

    def save_storage_lifecycle_health(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_LIFECYCLE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "lifecycle")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"lifecycle_health_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_lifecycle_health(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_LIFECYCLE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "lifecycle")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_maintenance_quality(self, profile_name: str, quality: dict) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_QUALITY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "quality")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"quality_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(quality, f, indent=2)
        return path

    def load_maintenance_quality(self, profile_name: str) -> dict:
        out_dir = getattr(self.paths, "MAINTENANCE_QUALITY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "quality")
        if not out_dir.exists():
            return {}
        files = list(out_dir.glob(f"quality_{profile_name}_*.json"))
        if not files:
            return {}
        latest = max(files, key=lambda f: f.stat().st_mtime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def save_maintenance_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"maintenance_report_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(report, f, indent=2)

        if markdown:
            md_dir = getattr(self.paths, "REPORTS_MAINTENANCE_MARKDOWN_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "markdown")
            md_dir.mkdir(parents=True, exist_ok=True)
            md_path = md_dir / f"maintenance_report_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.md"
            with open(md_path, "w") as f:
                f.write(markdown)

        return path

    def load_maintenance_report(self, profile_name: str) -> dict:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        if not out_dir.exists():
            return {}
        files = list(out_dir.glob(f"maintenance_report_{profile_name}_*.json"))
        if not files:
            return {}
        latest = max(files, key=lambda f: f.stat().st_mtime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def list_maintenance_reports(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.json"))
        records = []
        for f in files:
            records.append({
                "file_name": f.name,
                "modified_at": datetime.fromtimestamp(f.stat().st_mtime).isoformat()
            })
        return pd.DataFrame(records)

    # --- Final Review Methods ---
    def save_final_system_inventory(self, report_name: str, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        base_path = ProjectPaths.FINAL_REVIEW_SYSTEM_INVENTORY
        return self._save_report_data(base_path, report_name, df, summary)

    def load_final_system_inventory(self, report_name: str) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_SYSTEM_INVENTORY / f"{report_name}.parquet")

    def save_architecture_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_ARCHITECTURE, "architecture_audit", df, summary)

    def load_architecture_audit(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_ARCHITECTURE / "architecture_audit.parquet")

    def save_safety_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_SAFETY, "safety_audit", df, summary)

    def load_safety_audit(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_SAFETY / "safety_audit.parquet")

    def save_integration_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_INTEGRATION, "integration_audit", df, summary)

    def load_integration_audit(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_INTEGRATION / "integration_audit.parquet")

    def save_command_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_COMMANDS, "command_audit", df, summary)

    def load_command_audit(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_COMMANDS / "command_audit.parquet")

    def save_datalake_contract_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_DATALAKE, "datalake_contract_audit", df, summary)

    def load_datalake_contract_audit(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_DATALAKE / "datalake_contract_audit.parquet")

    def save_report_output_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_REPORT_OUTPUTS, "report_output_audit", df, summary)

    def load_report_output_audit(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_REPORT_OUTPUTS / "report_output_audit.parquet")

    def save_documentation_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_DOCUMENTATION, "documentation_audit", df, summary)

    def load_documentation_audit(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_DOCUMENTATION / "documentation_audit.parquet")

    def save_quality_gate_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_QUALITY_GATES, "quality_gate_audit", df, summary)

    def load_quality_gate_audit(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_QUALITY_GATES / "quality_gate_audit.parquet")

    def save_readiness_audit(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_READINESS, "readiness_audit", df, summary)

    def load_readiness_audit(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_READINESS / "readiness_audit.parquet")

    def save_final_risk_register(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_RISKS, "final_risk_register", df, summary)

    def load_final_risk_register(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_RISKS / "final_risk_register.parquet")

    def save_final_gap_register(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_GAPS, "final_gap_register", df, summary)

    def load_final_gap_register(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_GAPS / "final_gap_register.parquet")

    def save_final_acceptance_checklist(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_ACCEPTANCE, "final_acceptance_checklist", df, summary)

    def load_final_acceptance_checklist(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_ACCEPTANCE / "final_acceptance_checklist.parquet")

    def save_final_acceptance_snapshot(self, snapshot: dict) -> Path:
        path = ProjectPaths.FINAL_REVIEW_ACCEPTANCE / "final_acceptance_snapshot.json"
        self._save_json(snapshot, path)
        return path

    def load_final_acceptance_snapshot(self) -> dict:
        return self._load_json(ProjectPaths.FINAL_REVIEW_ACCEPTANCE / "final_acceptance_snapshot.json")

    def save_release_readiness_dry_run(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_READINESS, "release_readiness_dry_run", df, summary)

    def load_release_readiness_dry_run(self) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_READINESS / "release_readiness_dry_run.parquet")

    def save_phase_1_55_consolidation_audit(self, report_name: str, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_report_data(ProjectPaths.FINAL_REVIEW_CONSOLIDATION, report_name, df, summary)

    def load_phase_1_55_consolidation_audit(self, report_name: str) -> pd.DataFrame:
        return self._load_parquet(ProjectPaths.FINAL_REVIEW_CONSOLIDATION / f"{report_name}.parquet")

    def save_final_review_quality(self, profile_name: str, quality: dict) -> Path:
        path = ProjectPaths.FINAL_REVIEW_QUALITY / f"{profile_name}_quality.json"
        self._save_json(quality, path)
        return path

    def load_final_review_quality(self, profile_name: str) -> dict:
        return self._load_json(ProjectPaths.FINAL_REVIEW_QUALITY / f"{profile_name}_quality.json")

    def save_final_review_report(self, profile_name: str, report: dict, markdown: Optional[str] = None) -> Path:
        path = ProjectPaths.FINAL_REVIEW_REPORTS_JSON / f"{profile_name}_report.json"
        self._save_json(report, path)
        if markdown:
            md_path = ProjectPaths.FINAL_REVIEW_REPORTS_MARKDOWN / f"{profile_name}_report.md"
            with open(md_path, "w") as f:
                f.write(markdown)
        return path

    def load_final_review_report(self, profile_name: str) -> dict:
        return self._load_json(ProjectPaths.FINAL_REVIEW_REPORTS_JSON / f"{profile_name}_report.json")

    def list_final_review_reports(self) -> pd.DataFrame:
        rows = []
        for p in ProjectPaths.FINAL_REVIEW_REPORTS_JSON.glob("*_report.json"):
            rows.append({"report": p.stem, "path": str(p)})
        return pd.DataFrame(rows)
