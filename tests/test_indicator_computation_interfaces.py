from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.indicator_computation_interfaces import (
    BaseTechnicalIndicatorComputer,
    build_indicator_computation_interface_contract,
)


def test_indicator_computation_interfaces():
    prof = get_default_technical_indicator_profile()
    df, summary = build_indicator_computation_interface_contract(prof)
    assert not df.empty
    assert summary["interface_ready"] is True
