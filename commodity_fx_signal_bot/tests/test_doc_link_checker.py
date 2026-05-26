import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pytest
from pathlib import Path
from documentation.doc_link_checker import (
    extract_markdown_links,
    check_local_markdown_link
)

def test_extract_markdown_links():
    text = "Here is a [link](some_file.md) and another [one](http://example.com)."
    links = extract_markdown_links(text)
    assert len(links) == 2
    assert links[0]["target"] == "some_file.md"
    assert links[1]["target"] == "http://example.com"

def test_check_local_markdown_link(tmp_path):
    source = tmp_path / "docs" / "source.md"
    source.parent.mkdir()
    source.write_text("dummy")

    # External link
    check = check_local_markdown_link(source, "http://example.com", tmp_path)
    assert check.link_type == "external"
    assert check.status == "ok"

    # Anchor
    check = check_local_markdown_link(source, "#some-section", tmp_path)
    assert check.link_type == "anchor"
    assert check.status == "ok"

    # Broken local
    check = check_local_markdown_link(source, "nonexistent.md", tmp_path)
    assert check.link_type == "local_file"
    assert check.status == "broken"
    assert len(check.warnings) == 1
