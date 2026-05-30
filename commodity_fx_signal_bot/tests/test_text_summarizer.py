from report_summarization.text_summarizer import normalize_report_text, split_text_into_sentences, score_sentence_importance, build_rule_based_summary, mask_sensitive_summary_text

def test_normalize_report_text():
    text = "Line1\n\n\n\nLine2"
    assert normalize_report_text(text) == "Line1\n\nLine2"

def test_split_text_into_sentences():
    text = "Hello world. This is a test! Another sentence."
    sentences = split_text_into_sentences(text)
    assert len(sentences) == 3

def test_score_sentence_importance():
    score1 = score_sentence_importance("This is a normal sentence.")
    score2 = score_sentence_importance("This is a critical warning about a failed pipeline.")
    assert score2 > score1

def test_build_rule_based_summary():
    text = "Normal text. This is a critical gap. Another normal one. This is a warning."
    summary, bullets, meta = build_rule_based_summary(text, max_bullets=2)
    assert meta["status"] == "success"
    assert len(bullets) == 2

def test_mask_sensitive_summary_text():
    text = "API_KEY='12345' CANLI EMIR gonderildi. YATIRIM TAVSIYESIDIR."
    masked = mask_sensitive_summary_text(text)
    assert "12345" not in masked
    assert "CANLI EMIR" not in masked
    assert "YATIRIM TAVSIYESIDIR" not in masked
    assert "DETECTED_AS_TEXT" in masked
