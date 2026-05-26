import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from documentation.documentation_config import get_default_documentation_profile
from documentation.doc_generation import DocumentationGenerator
from pathlib import Path

def test_generator_methods(tmp_path):
    profile = get_default_documentation_profile()
    gen = DocumentationGenerator(tmp_path, profile)

    ug, _ = gen.generate_user_guide()
    assert len(ug) > 0

    om, _ = gen.generate_operator_manual()
    assert len(om) > 0

    ah, _ = gen.generate_analyst_handbook()
    assert len(ah) > 0

    dg, _ = gen.generate_developer_guide()
    assert len(dg) > 0

    cg, _ = gen.generate_codex_agent_guide()
    assert len(cg) > 0

def test_write_document(tmp_path):
    profile = get_default_documentation_profile()
    gen = DocumentationGenerator(tmp_path, profile)

    path = gen.write_document("test.md", "Test Content")
    assert path.exists()

    content = path.read_text(encoding="utf-8")
    assert "<!-- AUTO-GENERATED SECTION START -->" in content
    assert "Test Content" in content
