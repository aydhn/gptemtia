from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from typing import Optional

class ResearchDataCollector:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def collect_symbol_inputs(
        self,
        spec: SymbolSpec,
        timeframe: str,
    ) -> tuple[dict, dict]:
        """
        Collects all required inputs for a symbol from the DataLake.
        Returns (inputs: dict, metadata: dict)
        """
        inputs = {}
        missing_sources = []
        warnings = []

        # Latest Price/OHLCV
        try:
            ohlcv = self.data_lake.load_processed_ohlcv(spec.symbol, timeframe)
            if not ohlcv.empty:
               inputs['ohlcv'] = ohlcv
            else:
                missing_sources.append('ohlcv')
        except Exception as e:
             missing_sources.append('ohlcv')
             warnings.append(f"Could not load ohlcv: {e}")

        # Technical Features
        try:
            inputs['technical_features'] = self.data_lake.load_technical_features(spec.symbol, timeframe)
        except Exception as e:
            missing_sources.append('technical_features')

        # Candidates (Signal, Decision, Strategy, Risk, Sizing, Level)
        try:
            inputs['signal_candidates'] = self.data_lake.load_signal_candidates(spec.symbol, timeframe)
        except Exception:
            missing_sources.append('signal_candidates')

        try:
            inputs['decision_candidates'] = self.data_lake.load_decision_candidates(spec.symbol, timeframe)
        except Exception:
             missing_sources.append('decision_candidates')

        try:
            inputs['strategy_candidates'] = self.data_lake.load_strategy_candidates(spec.symbol, timeframe)
        except Exception:
             missing_sources.append('strategy_candidates')

        try:
            inputs['risk_candidates'] = self.data_lake.load_risk_candidates(spec.symbol, timeframe)
        except Exception:
             missing_sources.append('risk_candidates')

        try:
             inputs['sizing_candidates'] = self.data_lake.load_sizing_candidates(spec.symbol, timeframe)
        except Exception:
             missing_sources.append('sizing_candidates')

        try:
             inputs['level_candidates'] = self.data_lake.load_level_candidates(spec.symbol, timeframe)
        except Exception:
             missing_sources.append('level_candidates')


        # Summaries and Reports (Backtest, Performance, Validation, ML, Paper, Quality, Security, Orchestration)
        try:
            inputs['backtest_report'] = self.data_lake.load_backtest_report(spec.symbol, timeframe)
        except Exception:
            missing_sources.append('backtest_report')

        try:
             # Just load some generic ml metadata for now
             inputs['ml_metadata'] = self.data_lake.load_ml_metadata(spec.symbol, timeframe)
        except Exception:
             missing_sources.append('ml_metadata')

        try:
             inputs['paper_portfolio'] = self.data_lake.load_paper_portfolio(spec.symbol, timeframe)
        except Exception:
             missing_sources.append('paper_portfolio')

        try:
            inputs['quality_report'] = self.data_lake.load_observability_quality(spec.symbol, timeframe)
        except Exception:
            missing_sources.append('quality_report')

        try:
             inputs['security_readiness'] = self.data_lake.load_security_readiness(spec.symbol, timeframe)
        except Exception:
             missing_sources.append('security_readiness')

        # Just stubbing some to prevent crashes if missing

        metadata = {
            "missing_sources": missing_sources,
            "warnings": warnings,
            "data_available": len(inputs) > 0
        }
        return inputs, metadata


    def collect_universe_inputs(
        self,
        specs: list[SymbolSpec],
        timeframe: str,
        limit: Optional[int] = None,
    ) -> tuple[dict[str, dict], dict]:
        universe_inputs = {}
        missing_sources = []
        warnings = []

        specs_to_process = specs[:limit] if limit else specs

        for spec in specs_to_process:
            try:
                inputs, metadata = self.collect_symbol_inputs(spec, timeframe)
                universe_inputs[spec.symbol] = {
                    "inputs": inputs,
                    "metadata": metadata
                }
            except Exception as e:
                warnings.append(f"Failed to collect inputs for {spec.symbol}: {e}")

        metadata = {
            "missing_sources": missing_sources,
            "warnings": warnings,
            "symbols_collected": len(universe_inputs)
        }
        return universe_inputs, metadata
