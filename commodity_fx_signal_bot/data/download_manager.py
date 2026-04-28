from typing import Dict, List, Optional, Tuple
from datetime import datetime, timezone
import pandas as pd

from core.logger import get_logger
from config.settings import Settings
from config.symbols import SymbolSpec
from data.data_pipeline import DataPipeline
from data.storage.data_lake import DataLake
from data.storage.download_journal import DownloadJournal, DownloadJournalEntry
from data.data_quality import build_data_quality_report, infer_quality_grade

logger = get_logger(__name__)


class DownloadManager:
    """Orchestrates data downloading, lake storage, and journaling."""

    def __init__(
        self,
        pipeline: DataPipeline,
        data_lake: DataLake,
        journal: DownloadJournal,
        settings: Settings,
    ):
        self.pipeline = pipeline
        self.data_lake = data_lake
        self.journal = journal
        self.settings = settings

    def download_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str,
        period: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        refresh: bool = False,
    ) -> Optional[pd.DataFrame]:
        """Download and store data for a specific symbol and timeframe."""
        if spec.data_source == "synthetic" and self.settings.skip_synthetic_downloads:
            logger.info(f"Skipping download for synthetic symbol {spec.symbol}")
            return None

        # Check macro rules
        if (
            spec.data_source in ("evds", "fred")
            and self.settings.skip_macro_downloads_in_ohlcv_pipeline
        ):
            logger.info(f"Skipping macro symbol {spec.symbol} in OHLCV pipeline")
            return None

        logger.info(f"Downloading {spec.symbol} ({timeframe})")

        entry = DownloadJournalEntry(
            timestamp_utc=datetime.now(timezone.utc).isoformat(),
            symbol=spec.symbol,
            requested_symbol=spec.symbol,
            resolved_symbol=None,
            asset_class=spec.asset_class,
            timeframe=timeframe,
            provider_interval="",  # Will update after fetch
            period=period,
            start=start,
            end=end,
            success=False,
            rows=0,
            used_cache=False,
            used_alias=False,
            saved_path=None,
            error="",
        )

        df = None
        try:
            df = self.pipeline.fetch_symbol_data(
                spec=spec,
                interval=timeframe,
                period=period,
                start=start,
                end=end,
                use_cache=self.settings.data_cache_enabled,
                refresh=refresh,
            )

            entry.resolved_symbol = df.attrs.get("resolved_symbol", spec.symbol)
            entry.used_alias = df.attrs.get("used_alias", False)
            entry.provider_interval = df.attrs.get("provider_interval", timeframe)
            entry.used_cache = df.attrs.get("source_provider") == "Cache"

            # Save to Data Lake
            saved_path = self.data_lake.save_ohlcv(spec, timeframe, df)

            # Update Metadata
            report = build_data_quality_report(df)
            grade = infer_quality_grade(report)

            metadata = self.data_lake.load_metadata(spec)
            if not metadata:
                metadata = {
                    "symbol": spec.symbol,
                    "name": spec.name,
                    "asset_class": spec.asset_class,
                    "sub_class": spec.sub_class,
                    "data_source": spec.data_source,
                    "row_counts_by_timeframe": {},
                    "first_timestamp_by_timeframe": {},
                    "last_timestamp_by_timeframe": {},
                    "quality_grades": {},
                }

            metadata["last_updated_utc"] = datetime.now(timezone.utc).isoformat()
            if "available_timeframes" not in metadata:
                metadata["available_timeframes"] = []
            if timeframe not in metadata["available_timeframes"]:
                metadata["available_timeframes"].append(timeframe)

            metadata["row_counts_by_timeframe"][timeframe] = report.get("rows", 0)
            metadata["first_timestamp_by_timeframe"][timeframe] = report.get("start")
            metadata["last_timestamp_by_timeframe"][timeframe] = report.get("end")
            metadata["quality_grades"][timeframe] = grade

            self.data_lake.save_metadata(spec, metadata)

            entry.success = True
            entry.rows = len(df)
            entry.saved_path = str(saved_path)

        except Exception as e:
            logger.error(f"Download failed for {spec.symbol} ({timeframe}): {e}")
            entry.error = str(e)

        finally:
            if self.settings.journal_enabled:
                self.journal.append(entry)

        return df

    def download_symbol_all_timeframes(
        self,
        spec: SymbolSpec,
        timeframes: Tuple[str, ...],
        period: Optional[str] = None,
        refresh: bool = False,
    ) -> Dict[str, pd.DataFrame]:
        """Download and store data for all allowed timeframes for a symbol."""
        results = {}
        for tf in timeframes:
            df = self.download_symbol_timeframe(
                spec, tf, period=period, refresh=refresh
            )
            if df is not None:
                results[tf] = df
        return results

    def download_universe(
        self,
        specs: List[SymbolSpec],
        timeframes_by_symbol: Dict[str, Tuple[str, ...]],
        period: Optional[str] = None,
        limit: Optional[int] = None,
        refresh: bool = False,
    ) -> Dict:
        """Download data for multiple symbols and timeframes."""
        total_attempts = 0
        success_count = 0
        failure_count = 0
        skipped_count = 0
        by_asset_class = {}
        by_timeframe = {}
        errors = []

        specs_to_process = specs[:limit] if limit else specs

        for spec in specs_to_process:
            if (
                spec.data_source == "synthetic"
                and self.settings.skip_synthetic_downloads
            ):
                skipped_count += 1
                continue

            if (
                spec.data_source in ("evds", "fred")
                and self.settings.skip_macro_downloads_in_ohlcv_pipeline
            ):
                skipped_count += 1
                continue

            allowed_tfs = timeframes_by_symbol.get(spec.symbol, tuple())
            for tf in allowed_tfs:
                total_attempts += 1
                try:
                    df = self.download_symbol_timeframe(
                        spec, tf, period=period, refresh=refresh
                    )
                    if df is not None and not df.empty:
                        success_count += 1
                        by_asset_class[spec.asset_class] = (
                            by_asset_class.get(spec.asset_class, 0) + 1
                        )
                        by_timeframe[tf] = by_timeframe.get(tf, 0) + 1
                    else:
                        failure_count += 1
                        # download_symbol_timeframe catches exceptions and returns None
                        errors.append(
                            f"{spec.symbol} ({tf}): Fetch failed or returned empty"
                        )
                except Exception as e:
                    failure_count += 1
                    errors.append(f"{spec.symbol} ({tf}): {e}")

        return {
            "total_attempts": total_attempts,
            "success_count": success_count,
            "failure_count": failure_count,
            "skipped_count": skipped_count,
            "by_asset_class": by_asset_class,
            "by_timeframe": by_timeframe,
            "errors": errors,
        }

    def repair_missing_data(
        self,
        specs: List[SymbolSpec],
        timeframes_by_symbol: Dict[str, Tuple[str, ...]],
        period: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        """Attempt to repair missing or poorly graded data."""
        repair_candidates = []

        for spec in specs:
            if spec.data_source == "synthetic" or spec.data_source in ("evds", "fred"):
                continue

            allowed_tfs = timeframes_by_symbol.get(spec.symbol, tuple())
            metadata = self.data_lake.load_metadata(spec)
            grades = metadata.get("quality_grades", {})

            for tf in allowed_tfs:
                exists = self.data_lake.has_ohlcv(spec, tf)
                grade = grades.get(tf, "N/A")

                if not exists or grade in ("D", "F", "N/A"):
                    repair_candidates.append((spec, tf))

        if limit:
            repair_candidates = repair_candidates[:limit]

        results = {"attempted": len(repair_candidates), "success": 0, "failed": 0}

        for spec, tf in repair_candidates:
            logger.info(f"Repairing {spec.symbol} ({tf})")
            df = self.download_symbol_timeframe(spec, tf, period=period, refresh=True)
            if df is not None and not df.empty:
                results["success"] += 1
            else:
                results["failed"] += 1

        return results
