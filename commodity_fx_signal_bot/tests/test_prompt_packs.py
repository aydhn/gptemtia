import pytest
from analyst_ux.ux_config import get_default_analyst_ux_profile
from analyst_ux.prompt_packs import (
    build_default_prompt_packs, prompt_packs_to_dataframe, build_prompt_pack_manifest
)

def test_prompt_packs():
    profile = get_default_analyst_ux_profile()
    packs = build_default_prompt_packs(profile)

    assert len(packs) > 0
    assert any(p.audience == "operator" for p in packs)
    assert any(p.audience == "analyst" for p in packs)
    assert any(p.audience == "codex" for p in packs)
    assert any(p.audience == "developer" for p in packs) # troubleshooting and regression

    manifest = build_prompt_pack_manifest(packs)
    assert manifest["total_packs"] == len(packs)
    assert "packs" in manifest

    for pack in packs:
        assert "Bu prompt pack sadece offline research içindir" in pack.warnings[0]
