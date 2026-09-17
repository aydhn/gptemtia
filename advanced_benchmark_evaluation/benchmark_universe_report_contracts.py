# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Universe Report Contracts Module.

Defines benchmark reference universes for Commodities and Foreign Exchange (FX) assets.
Ensures zero live market connectivity and zero automated order routing.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_BENCHMARK_UNIVERSE_REPORT_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

BENCHMARK_UNIVERSES: List[Dict[str, Any]] = [
    {
        "universe_id": "UNIV_COMMODITY_ENERGY",
        "asset_class": "commodity",
        "sub_class": "energy",
        "universe_name": "Commodity Energy Benchmark Universe",
        "symbols": ["BRENT", "WTI", "NATGAS"],
        "primary_benchmark": "BRENT_CRUDE_CONTINUOUS",
        "description": "Ham petrol ve doğal gaz gösterge evreni.",
    },
    {
        "universe_id": "UNIV_COMMODITY_METALS_PRECIOUS",
        "asset_class": "commodity",
        "sub_class": "precious_metals",
        "universe_name": "Precious Metals Benchmark Universe",
        "symbols": ["XAU_USD", "XAG_USD", "PLATINUM"],
        "primary_benchmark": "GOLD_USD_SPOT",
        "description": "Altın ve gümüş değerli maden gösterge evreni.",
    },
    {
        "universe_id": "UNIV_COMMODITY_METALS_BASE",
        "asset_class": "commodity",
        "sub_class": "industrial_metals",
        "universe_name": "Industrial Metals Benchmark Universe",
        "symbols": ["COPPER", "ALUMINUM", "ZINC"],
        "primary_benchmark": "LME_COPPER_CASH",
        "description": "Endüstriyel baz metaller gösterge evreni.",
    },
    {
        "universe_id": "UNIV_FX_MAJORS",
        "asset_class": "fx",
        "sub_class": "major_pairs",
        "universe_name": "FX Major Pairs Benchmark Universe",
        "symbols": ["EUR_USD", "GBP_USD", "USD_JPY", "USD_CHF"],
        "primary_benchmark": "DXY_DOLLAR_INDEX",
        "description": "Başlıca döviz çiftleri ve dolar endeksi gösterge evreni.",
    },
    {
        "universe_id": "UNIV_FX_COMMODITY_CURRENCIES",
        "asset_class": "fx",
        "sub_class": "commodity_currencies",
        "universe_name": "FX Commodity Currencies Benchmark Universe",
        "symbols": ["AUD_USD", "USD_CAD", "NZD_USD", "USD_NOK"],
        "primary_benchmark": "EQUAL_WEIGHT_COMMODITY_FX_BASKET",
        "description": "Emtia bağlantılı para birimleri gösterge evreni.",
    },
]


def build_benchmark_universe_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of all benchmark universe contracts."""
    rows: List[Dict[str, Any]] = []

    for u in BENCHMARK_UNIVERSES:
        rows.append(
            {
                "universe_id": u["universe_id"],
                "asset_class": u["asset_class"],
                "sub_class": u["sub_class"],
                "universe_name": u["universe_name"],
                "symbol_count": len(u["symbols"]),
                "symbols_str": ",".join(u["symbols"]),
                "primary_benchmark": u["primary_benchmark"],
                "description": u["description"],
                "execution_allowed": False,
                "trading_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_BENCHMARK_UNIVERSE_REPORT_DOMAIN,
        "total_universes": len(df),
        "total_symbols_covered": sum(u["symbol_count"] for u in rows) if rows else 0,
        "all_execution_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
