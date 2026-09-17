# -*- coding: utf-8 -*-
"""Phase 155: Exposure Attribution Contracts Registry."""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import ExposureAttributionContract


DEFAULT_EXPOSURE_ATTRIBUTION_CONTRACTS = [
    {
        "contract_name": "gross_exposure_attribution_contract",
        "exposure_family": "gross_exposure",
        "description": "Portfoy toplam mutlak pozisyon buyuklugu exposure attribution sozlesmesi",
        "mathematical_formulation": "Gross Exposure = sum(|w_i|) * NAV",
        "is_placeholder": True,
        "exposure_calculated": False,
        "allows_execution": False,
    },
    {
        "contract_name": "net_exposure_attribution_contract",
        "exposure_family": "net_exposure",
        "description": "Portfoy net yonlu pozisyon dengesi exposure attribution sozlesmesi",
        "mathematical_formulation": "Net Exposure = sum(w_i) * NAV",
        "is_placeholder": True,
        "exposure_calculated": False,
        "allows_execution": False,
    },
    {
        "contract_name": "currency_exposure_attribution_contract",
        "exposure_family": "currency_exposure",
        "description": "Doviz cinsi bazinda risk ve pozisyon dagilimi sozlesmesi",
        "mathematical_formulation": "Currency Exposure_c = sum_{i in c}(w_i) * NAV",
        "is_placeholder": True,
        "exposure_calculated": False,
        "allows_execution": False,
    },
    {
        "contract_name": "cross_asset_exposure_attribution_contract",
        "exposure_family": "cross_asset_exposure",
        "description": "Emtia ve doviz siniflari arasi risk dagilimi sozlesmesi",
        "mathematical_formulation": "CrossAsset Exposure_a = sum_{i in a}(|w_i|) / Gross",
        "is_placeholder": True,
        "exposure_calculated": False,
        "allows_execution": False,
    },
    {
        "contract_name": "concentration_exposure_attribution_contract",
        "exposure_family": "concentration_exposure",
        "description": "Konsantrasyon ve agirlik yogunlasma attribution sozlesmesi",
        "mathematical_formulation": "HHI = sum(w_i^2), Top-K weight ratio = sum_{k}(|w_k|)",
        "is_placeholder": True,
        "exposure_calculated": False,
        "allows_execution": False,
    },
    {
        "contract_name": "liquidity_exposure_attribution_contract",
        "exposure_family": "liquidity_exposure",
        "description": "Pozisyon tasfiye edilebilirlik ve likidite riski sozlesmesi",
        "mathematical_formulation": "Liquidity Exposure = Days to Liquidate = |Position_i| / (ADV_i * Liquidity_Cap)",
        "is_placeholder": True,
        "exposure_calculated": False,
        "allows_execution": False,
    },
    {
        "contract_name": "leverage_margin_exposure_attribution_contract",
        "exposure_family": "leverage_margin_exposure",
        "description": "Kaldirac ve teminat kullanim dagilimi sozlesmesi",
        "mathematical_formulation": "Leverage = Gross / NAV, Margin Utilization = Initial Margin / Equity",
        "is_placeholder": True,
        "exposure_calculated": False,
        "allows_execution": False,
    },
    {
        "contract_name": "regime_exposure_attribution_contract",
        "exposure_family": "regime_exposure",
        "description": "Piyasa rejimi kosullarina gore pozisyon duyarliligi sozlesmesi",
        "mathematical_formulation": "Regime Exposure_r = sum_{i}(w_i * RegimeSensitivity_{i,r})",
        "is_placeholder": True,
        "exposure_calculated": False,
        "allows_execution": False,
    },
    {
        "contract_name": "strategy_exposure_attribution_contract",
        "exposure_family": "strategy_exposure",
        "description": "Alt stratejiler bazinda pozisyon paylasimi sozlesmesi",
        "mathematical_formulation": "Strategy Exposure_s = sum_{i in s}(|w_i|)",
        "is_placeholder": True,
        "exposure_calculated": False,
        "allows_execution": False,
    },
    {
        "contract_name": "asset_level_exposure_attribution_contract",
        "exposure_family": "asset_exposure",
        "description": "Varlik duzeyinde net ve brut pozisyon dökümü sozlesmesi",
        "mathematical_formulation": "Asset Exposure_i = w_i * NAV",
        "is_placeholder": True,
        "exposure_calculated": False,
        "allows_execution": False,
    },
]


def build_exposure_attribution_contract_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of exposure attribution contracts."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for c in DEFAULT_EXPOSURE_ATTRIBUTION_CONTRACTS:
        model = ExposureAttributionContract(**c)
        data = model.model_dump()
        data["current_phase"] = profile.current_phase
        data["target_final_phase"] = profile.target_final_phase
        data["next_phase"] = profile.next_phase
        rows.append(data)

    df = pd.DataFrame(rows)
    summary = summarize_exposure_attribution_contracts(df)
    return df, summary


def validate_exposure_attribution_contract(contract: dict) -> dict:
    """Validate that an exposure attribution contract satisfies safety invariants."""
    violations = []
    if contract.get("exposure_calculated", False) is True:
        violations.append("exposure_calculated must be False")
    if contract.get("allows_execution", False) is True:
        violations.append("allows_execution must be False")
    if contract.get("is_placeholder", True) is not True:
        violations.append("is_placeholder must be True")
    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": len(violations) == 0,
        "violations": violations,
    }


def summarize_exposure_attribution_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Produce summary dictionary for exposure attribution contracts."""
    return {
        "contract_count": len(df),
        "total_contracts": len(df),
        "all_contracts_placeholder": bool(df["is_placeholder"].all()) if not df.empty else True,
        "zero_exposure_calculated": bool((df["exposure_calculated"] == False).all()) if not df.empty else True,
        "zero_execution_allowed": bool((df["allows_execution"] == False).all()) if not df.empty else True,
    }
