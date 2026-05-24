import pandas as pd
from knowledge_base.memory_cards import build_symbol_memory_card, build_warning_memory_cards

def test_symbol_memory_card():
    c_df = pd.DataFrame({"symbols": [["GC=F"]], "text": ["found gold"], "document_id": ["d1"]})
    card = build_symbol_memory_card("GC=F", pd.DataFrame(), c_df)
    assert card.symbol == "GC=F"

def test_warning_cards():
    c_df = pd.DataFrame({"text": ["warning: failed"], "document_id": ["d1"], "chunk_id": ["c1"]})
    cards = build_warning_memory_cards(c_df)
    assert len(cards) == 1
