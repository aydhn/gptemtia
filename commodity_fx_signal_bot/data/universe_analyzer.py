"""
Universe Analyzer module.
Measures data reliability and quality for a given universe of symbols.
"""
from dataclasses import dataclass
from typing import List, Dict, Optional, Any
import pandas as pd

from core.logger import get_logger
from config.settings import Settings
from config.symbols import SymbolSpec
from data.data_pipeline import DataPipeline
from data.data_quality import build_data_quality_report

logger = get_logger(__name__)

@dataclass
class SymbolReliabilityResult:
    """Result of analyzing a single symbol."""
    symbol: str
    requested_symbol: str
    resolved_symbol: Optional[str]
    name: str
    asset_class: str
    sub_class: str
    data_source: str
    success: bool
    rows: int
    start: Optional[str]
    end: Optional[str]
    last_close: Optional[float]
    missing_close_ratio: Optional[float]
    duplicate_index_count: int
    negative_price_count: int
    high_low_error_count: int
    used_alias: bool
    error: str
    reliability_score: float
    reliability_grade: str


class UniverseAnalyzer:
    """Analyzes a symbol universe to produce reliability metrics."""

    def __init__(self, pipeline: DataPipeline, settings: Settings):
        self.pipeline = pipeline
        self.settings = settings

    def analyze_symbol(
        self,
        spec: SymbolSpec,
        interval: str,
        period: str,
        refresh: bool = False,
    ) -> SymbolReliabilityResult:
        """
        Analyze a single symbol.
        """
        error_msg = ""
        success = False
        df = None

        # We don't try to download synthetic symbols typically, but if we do, skip actual download
        if spec.data_source == "synthetic":
            # For synthetic, we fake a perfect score
            return SymbolReliabilityResult(
                symbol=spec.symbol,
                requested_symbol=spec.symbol,
                resolved_symbol=spec.symbol,
                name=spec.name,
                asset_class=spec.asset_class,
                sub_class=spec.sub_class,
                data_source=spec.data_source,
                success=True,
                rows=self.settings.min_ohlcv_rows + 1,
                start=None,
                end=None,
                last_close=1.0,
                missing_close_ratio=0.0,
                duplicate_index_count=0,
                negative_price_count=0,
                high_low_error_count=0,
                used_alias=False,
                error="",
                reliability_score=100.0,
                reliability_grade="SYNTHETIC"
            )

        try:
            df = self.pipeline.fetch_symbol_data(
                spec=spec,
                interval=interval,
                period=period,
                refresh=refresh
            )
            success = True
        except Exception as e:
            error_msg = str(e)
            logger.debug(f"Failed to fetch data for {spec.symbol}: {e}")

        # Basic parsing of metadata
        resolved_symbol = None
        used_alias = False
        if df is not None and not df.empty:
            resolved_symbol = df.attrs.get("resolved_symbol")
            used_alias = df.attrs.get("used_alias", False)

        report = build_data_quality_report(df if success else pd.DataFrame(), raise_on_empty=False)

        score = 100.0

        if not success or report["rows"] == 0:
            score = 0.0
        else:
            if report["rows"] < self.settings.min_ohlcv_rows:
                score -= 30
            if report.get("close_missing_ratio", 0) is not None and report.get("close_missing_ratio", 0) > 0.05:
                score -= 20
            if report.get("duplicate_index_count", 0) > 0:
                score -= 15
            if report.get("negative_price_count", 0) > 0:
                score -= 30
            if report.get("high_low_error_count", 0) > 0:
                score -= 30
            if used_alias:
                score -= 5
            if report.get("last_close") is None:
                score -= 20

        score = max(0.0, min(100.0, score))

        grade = "F"
        if score >= 90:
            grade = "A"
        elif score >= 75:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 40:
            grade = "D"

        return SymbolReliabilityResult(
            symbol=spec.symbol,
            requested_symbol=spec.symbol,
            resolved_symbol=resolved_symbol,
            name=spec.name,
            asset_class=spec.asset_class,
            sub_class=spec.sub_class,
            data_source=spec.data_source,
            success=success and report["rows"] > 0,
            rows=report["rows"],
            start=report.get("start"),
            end=report.get("end"),
            last_close=report.get("last_close"),
            missing_close_ratio=report.get("close_missing_ratio"),
            duplicate_index_count=report.get("duplicate_index_count", 0),
            negative_price_count=report.get("negative_price_count", 0),
            high_low_error_count=report.get("high_low_error_count", 0),
            used_alias=used_alias,
            error=error_msg,
            reliability_score=score,
            reliability_grade=grade
        )

    def analyze_many(
        self,
        specs: List[SymbolSpec],
        interval: str,
        period: str,
        limit: Optional[int] = None,
        refresh: bool = False,
    ) -> List[SymbolReliabilityResult]:
        """
        Analyze multiple symbols.
        """
        results = []
        specs_to_run = specs[:limit] if limit else specs

        for spec in specs_to_run:
            logger.info(f"Analyzing symbol: {spec.symbol}...")
            res = self.analyze_symbol(spec, interval=interval, period=period, refresh=refresh)
            results.append(res)

        return results

    @staticmethod
    def results_to_dataframe(results: List[SymbolReliabilityResult]) -> pd.DataFrame:
        """
        Convert list of SymbolReliabilityResult to a pandas DataFrame.
        """
        data = [
            {
                "symbol": r.symbol,
                "requested_symbol": r.requested_symbol,
                "resolved_symbol": r.resolved_symbol,
                "name": r.name,
                "asset_class": r.asset_class,
                "sub_class": r.sub_class,
                "data_source": r.data_source,
                "success": r.success,
                "rows": r.rows,
                "start": r.start,
                "end": r.end,
                "last_close": r.last_close,
                "missing_close_ratio": r.missing_close_ratio,
                "duplicate_index_count": r.duplicate_index_count,
                "negative_price_count": r.negative_price_count,
                "high_low_error_count": r.high_low_error_count,
                "used_alias": r.used_alias,
                "error": r.error,
                "reliability_score": r.reliability_score,
                "reliability_grade": r.reliability_grade
            }
            for r in results
        ]
        return pd.DataFrame(data)

    @staticmethod
    def summarize_results(results: List[SymbolReliabilityResult]) -> Dict[str, Any]:
        """
        Produce a summary of the analysis results.
        """
        if not results:
            return {}

        df = UniverseAnalyzer.results_to_dataframe(results)

        total = len(df)
        success_count = int(df["success"].sum())
        fail_count = total - success_count

        avg_score = float(df["reliability_score"].mean()) if total > 0 else 0.0

        grade_dist = df["reliability_grade"].value_counts().to_dict()

        ac_success = df.groupby("asset_class")["success"].mean().to_dict()

        best = df.sort_values(by="reliability_score", ascending=False).head(10)[["symbol", "reliability_score", "reliability_grade"]].to_dict('records')
        worst = df.sort_values(by="reliability_score", ascending=True).head(10)[["symbol", "reliability_score", "reliability_grade", "error"]].to_dict('records')

        used_alias_symbols = df[df["used_alias"] == True]["symbol"].tolist()
        error_symbols = df[df["error"] != ""][["symbol", "error"]].to_dict('records')

        return {
            "total_analyzed": total,
            "success_count": success_count,
            "fail_count": fail_count,
            "avg_score": avg_score,
            "grade_distribution": grade_dist,
            "asset_class_success_rate": ac_success,
            "best_10": best,
            "worst_10": worst,
            "used_alias_symbols": used_alias_symbols,
            "error_symbols": error_symbols
        }
