import pandas as pd
from .ux_config import AnalystUXProfile
from .ux_models import PromptPack, build_prompt_pack_id

def _create_pack(title: str, label: str, audience: str, desc: str, prompts: list, commands: list) -> PromptPack:
    return PromptPack(
        prompt_pack_id=build_prompt_pack_id(title, label),
        title=title,
        prompt_pack_label=label,
        audience=audience,
        description=desc,
        prompts=prompts,
        related_commands=commands,
        warnings=["Bu prompt pack sadece offline research içindir. Canlı emir veya yatırım tavsiyesi istemeyin."]
    )

def build_operator_prompt_pack(profile: AnalystUXProfile) -> PromptPack:
    return _create_pack(
        "Operator Routine Pack", "operator_prompt_pack", "operator",
        "Routine health and status checks",
        [{"purpose": "Check system health", "prompt_text": "Lütfen sistem sağlık durumunu kontrol et.", "expected_safe_output": "Status report generated."}],
        ["status:final", "status:quality"]
    )

def build_analyst_prompt_pack(profile: AnalystUXProfile) -> PromptPack:
    return _create_pack(
        "Analyst Research Pack", "analyst_prompt_pack", "analyst",
        "Generate offline research reports",
        [{"purpose": "Run end to end demo", "prompt_text": "Demo raporunu üret", "expected_safe_output": "Offline report saved."}],
        ["demo:scenario", "report:final"]
    )

def build_codex_agent_prompt_pack(profile: AnalystUXProfile) -> PromptPack:
    return _create_pack(
        "Codex Productivity Pack", "codex_agent_prompt_pack", "codex",
        "Safe instructions for AI agents",
        [{"purpose": "Fix tests", "prompt_text": "Eksik testleri bul ve yalnızca test/kalite düzeltmeleri öner.", "expected_safe_output": "Test fix code proposed."}],
        ["quality:check", "report:safety"]
    )

def build_troubleshooting_prompt_pack(profile: AnalystUXProfile) -> PromptPack:
    return _create_pack(
        "Troubleshooting Pack", "troubleshooting_prompt_pack", "developer",
        "Diagnose errors",
        [{"purpose": "Analyze error", "prompt_text": "Son hatayı diagnostik et.", "expected_safe_output": "Error summary without live state details."}],
        ["status:quality"]
    )

def build_documentation_prompt_pack(profile: AnalystUXProfile) -> PromptPack:
    return _create_pack(
        "Docs Pack", "documentation_prompt_pack", "writer",
        "Generate documentation",
        [{"purpose": "Update docs", "prompt_text": "Dokümantasyonu yenile.", "expected_safe_output": "Docs updated."}],
        ["docs:pack"]
    )

def build_scenario_prompt_pack(profile: AnalystUXProfile) -> PromptPack:
    return _create_pack(
        "Scenario Pack", "scenario_prompt_pack", "analyst",
        "Run synthetic scenarios",
        [{"purpose": "Run scenario", "prompt_text": "Sentetik senaryoyu çalıştır.", "expected_safe_output": "Scenario demo executed."}],
        ["demo:scenario"]
    )

def build_regression_prompt_pack(profile: AnalystUXProfile) -> PromptPack:
    return _create_pack(
        "Regression Pack", "regression_prompt_pack", "developer",
        "Check regressions",
        [{"purpose": "Regression diff", "prompt_text": "Scenario regression snapshot farklarını kontrol et. Yatırım sinyali olarak yorumlama.", "expected_safe_output": "Regression diff displayed."}],
        ["regression:demo", "status:regression"]
    )

def build_final_review_prompt_pack(profile: AnalystUXProfile) -> PromptPack:
    return _create_pack(
        "Final Review Pack", "final_review_prompt_pack", "auditor",
        "Run final reviews",
        [{"purpose": "Run final review", "prompt_text": "Final review risklerini proje kalite/güvenlik riski olarak raporla.", "expected_safe_output": "Final review passed."}],
        ["report:final"]
    )

def build_default_prompt_packs(profile: AnalystUXProfile) -> list[PromptPack]:
    if not profile.generate_prompt_packs: return []
    return [
        build_operator_prompt_pack(profile),
        build_analyst_prompt_pack(profile),
        build_codex_agent_prompt_pack(profile),
        build_troubleshooting_prompt_pack(profile),
        build_documentation_prompt_pack(profile),
        build_scenario_prompt_pack(profile),
        build_regression_prompt_pack(profile),
        build_final_review_prompt_pack(profile)
    ]

def prompt_packs_to_dataframe(packs: list[PromptPack]) -> pd.DataFrame:
    if not packs: return pd.DataFrame()
    return pd.DataFrame([p.__dict__ for p in packs])

def build_prompt_pack_manifest(packs: list[PromptPack]) -> dict:
    if not packs: return {"packs": []}
    return {
        "manifest_version": "1.0",
        "total_packs": len(packs),
        "packs": [p.__dict__ for p in packs]
    }
