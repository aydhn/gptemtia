from knowledge_base.text_extraction import mask_sensitive_text, estimate_token_count

def test_masking():
    t = "This is a token: '12345' and secret='abc'"
    m = mask_sensitive_text(t)
    assert "[MASKED_TOKEN]" in m
    assert "[MASKED_SECRET]" in m
    assert "12345" not in m

def test_token_count():
    assert estimate_token_count("hello world.") == 3
