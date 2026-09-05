import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .data_access_interface import build_data_access_interface_contract
from .feature_interface import build_feature_interface_contract
from .regime_interface import build_regime_interface_contract
from .ml_interface import build_ml_interface_contract
from .backtest_interface import build_backtest_interface_contract
from .portfolio_interface import build_portfolio_interface_contract
from .report_interface import build_report_interface_contract
from .signal_research_interface import build_signal_research_interface_contract

def build_research_engine_interface_contract(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    dfs = []
    dfs.append(build_data_access_interface_contract(profile)[0])
    dfs.append(build_feature_interface_contract(profile)[0])
    dfs.append(build_regime_interface_contract(profile)[0])
    dfs.append(build_ml_interface_contract(profile)[0])
    dfs.append(build_backtest_interface_contract(profile)[0])
    dfs.append(build_portfolio_interface_contract(profile)[0])
    dfs.append(build_report_interface_contract(profile)[0])
    dfs.append(build_signal_research_interface_contract(profile)[0])
    combined = pd.concat(dfs, ignore_index=True)
    return combined, {"total_contracts": len(combined)}

def build_all_research_interface_contracts(profile: AdvancedResearchEngineProfile) -> tuple[dict[str, pd.DataFrame], dict]:
    contracts = {
        "data_access": build_data_access_interface_contract(profile)[0],
        "feature": build_feature_interface_contract(profile)[0],
        "regime": build_regime_interface_contract(profile)[0],
        "ml": build_ml_interface_contract(profile)[0],
        "backtest": build_backtest_interface_contract(profile)[0],
        "portfolio": build_portfolio_interface_contract(profile)[0],
        "report": build_report_interface_contract(profile)[0],
        "signal_research": build_signal_research_interface_contract(profile)[0],
    }
    return contracts, {"loaded": len(contracts)}
