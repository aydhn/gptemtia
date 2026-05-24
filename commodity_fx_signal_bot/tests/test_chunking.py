from knowledge_base.chunking import extract_symbols_from_text, extract_modules_from_text, split_text_into_chunks

def test_extract_symbols():
    syms = extract_symbols_from_text("We analyzed GC=F and CL=F today.")
    assert "GC=F" in syms
    assert "CL=F" in syms

def test_extract_modules():
    mods = extract_modules_from_text("This is from meta_research output.")
    assert "meta_research" in mods

def test_split_text():
    text = "A" * 2000
    chunks = split_text_into_chunks(text, 1200, 150)
    assert len(chunks) == 2
