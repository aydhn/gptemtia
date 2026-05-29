import pytest
from analyst_ux.ux_models import (
    CommandAlias, AnalystIntent, SafeCommandSuggestion, PromptPack, AnalystTask,
    build_command_alias_id, build_intent_id, build_safe_command_suggestion_id,
    build_prompt_pack_id, build_analyst_task_id,
    command_alias_to_dict, analyst_intent_to_dict, safe_command_suggestion_to_dict,
    prompt_pack_to_dict, analyst_task_to_dict
)

def test_build_ids_deterministic():
    id1 = build_command_alias_id("name", "mod")
    id2 = build_command_alias_id("name", "mod")
    assert id1 == id2
    assert len(id1) == 12

    assert build_intent_id("query") == build_intent_id("query")
    assert build_safe_command_suggestion_id("query", "cmd") == build_safe_command_suggestion_id("query", "cmd")
    assert build_prompt_pack_id("title", "label") == build_prompt_pack_id("title", "label")
    assert build_analyst_task_id("title", "type") == build_analyst_task_id("title", "type")

def test_model_to_dict():
    alias = CommandAlias("id", "name", "type", "cmd", "desc", "mod", "safe", [], [])
    d = command_alias_to_dict(alias)
    assert d["alias_id"] == "id"
    assert d["command"] == "cmd"
