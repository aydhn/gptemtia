from factor_research.factor_report_builder import build_factor_disclaimer

def test_report_builder():
    text = build_factor_disclaimer()
    assert "YATIRIM TAVSİYESİ DEĞİLDİR" in text
