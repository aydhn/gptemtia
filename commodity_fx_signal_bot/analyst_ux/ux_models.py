from dataclasses import dataclass, asdict
import hashlib

@dataclass
class CommandAlias:
    alias_id: str
    alias_name: str
    alias_type: str
    command: str
    description: str
    module_name: str
    safety_label: str
    example_queries: list[str]
    warnings: list[str]

@dataclass
class AnalystIntent:
    intent_id: str
    query_text: str
    intent_label: str
    confidence: float
    matched_keywords: list[str]
    related_modules: list[str]
    warnings: list[str]

@dataclass
class SafeCommandSuggestion:
    suggestion_id: str
    query_text: str
    intent_label: str
    command_alias_id: str | None
    command: str
    description: str
    safety_label: str
    rank: int
    confidence: float
    warnings: list[str]

@dataclass
class PromptPack:
    prompt_pack_id: str
    title: str
    prompt_pack_label: str
    audience: str
    description: str
    prompts: list[dict]
    related_commands: list[str]
    warnings: list[str]

@dataclass
class AnalystTask:
    task_id: str
    title: str
    task_type: str
    description: str
    suggested_aliases: list[str]
    suggested_commands: list[str]
    status: str
    priority: str
    warnings: list[str]

def build_command_alias_id(alias_name: str, module_name: str) -> str:
    s = f"alias_{alias_name}_{module_name}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def build_intent_id(query_text: str) -> str:
    s = f"intent_{query_text}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def build_safe_command_suggestion_id(query_text: str, command: str) -> str:
    s = f"sugg_{query_text}_{command}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def build_prompt_pack_id(title: str, label: str) -> str:
    s = f"pack_{title}_{label}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def build_analyst_task_id(title: str, task_type: str) -> str:
    s = f"task_{title}_{task_type}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def command_alias_to_dict(alias: CommandAlias) -> dict:
    return asdict(alias)

def analyst_intent_to_dict(intent: AnalystIntent) -> dict:
    return asdict(intent)

def safe_command_suggestion_to_dict(suggestion: SafeCommandSuggestion) -> dict:
    return asdict(suggestion)

def prompt_pack_to_dict(pack: PromptPack) -> dict:
    return asdict(pack)

def analyst_task_to_dict(task: AnalystTask) -> dict:
    return asdict(task)
