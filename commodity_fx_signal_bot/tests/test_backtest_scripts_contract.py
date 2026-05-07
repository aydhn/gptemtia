import pytest
import sys
from pathlib import Path


def test_scripts_importable():
    sys.path.append(str(Path(__file__).parent.parent))
    import scripts.run_backtest_preview
    import scripts.run_backtest_batch
    import scripts.run_backtest_status
    import scripts.run_backtest_trade_ledger_preview

    assert True
