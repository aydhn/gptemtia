from pathlib import Path

def fix():
    # Mypy issues:
    # chunking.py:73: Need type annotation for freq
    p = Path("commodity_fx_signal_bot/knowledge_base/chunking.py")
    if p.exists():
        c = p.read_text()
        c = c.replace("freq = {}", "freq: dict[str, int] = {}")
        p.write_text(c)

    # tfidf_retrieval.py:73: Need type annotation for results
    p2 = Path("commodity_fx_signal_bot/knowledge_base/tfidf_retrieval.py")
    if p2.exists():
        c = p2.read_text()
        c = c.replace("results = []", "results: List[RetrievalResult] = []")
        p2.write_text(c)

fix()
