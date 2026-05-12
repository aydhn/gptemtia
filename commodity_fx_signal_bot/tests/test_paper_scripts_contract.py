import pytest
import importlib

def test_paper_trading_preview_script():
    module = importlib.import_module("scripts.run_paper_trading_preview")
    assert hasattr(module, "main")

def test_paper_order_book_preview_script():
    module = importlib.import_module("scripts.run_paper_order_book_preview")
    assert hasattr(module, "main")

def test_paper_portfolio_preview_script():
    module = importlib.import_module("scripts.run_paper_portfolio_preview")
    assert hasattr(module, "main")

def test_paper_batch_script():
    module = importlib.import_module("scripts.run_paper_batch")
    assert hasattr(module, "main")

def test_paper_status_script():
    module = importlib.import_module("scripts.run_paper_status")
    assert hasattr(module, "main")
