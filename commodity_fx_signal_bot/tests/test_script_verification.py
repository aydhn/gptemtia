from portable_packaging.script_verification import (
    discover_safe_scripts,
    verify_script_main_guard,
    verify_script_importability,
    classify_script_safety
)

def test_script_verification(tmp_path):
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (scripts / "test_script.py").write_text("if __name__ == '__main__':\n    pass")

    df = discover_safe_scripts(tmp_path)
    assert not df.empty

    guard = verify_script_main_guard(scripts / "test_script.py")
    assert guard["has_main_guard"]

    imp = verify_script_importability(scripts / "test_script.py", tmp_path)
    assert imp["importable"]

    safe = classify_script_safety(scripts / "test_script.py")
    assert safe == "safe"

    unsafe = classify_script_safety(scripts / "live_trade.py")
    assert unsafe == "forbidden"
