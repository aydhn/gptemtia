from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class DocumentationProfile:
    name: str
    description: str
    language: str = "tr"
    generate_user_guide: bool = True
    generate_operator_manual: bool = True
    generate_analyst_handbook: bool = True
    generate_developer_guide: bool = True
    generate_codex_agent_guide: bool = True
    generate_safe_usage_guide: bool = True
    generate_troubleshooting: bool = True
    generate_references: bool = True
    check_internal_links: bool = True
    check_safety_language: bool = True
    check_consistency: bool = True
    require_disclaimers: bool = True
    require_no_investment_advice: bool = True
    require_no_live_trading_language: bool = True
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_profiles: dict[str, DocumentationProfile] = {
    "balanced_documentation_pack": DocumentationProfile(
        name="balanced_documentation_pack",
        description="Balanced Documentation Pack",
        language="tr",
        notes="Genel amaçlı Türkçe user/operator/analyst dokümantasyon paketi."
    ),
    "operator_focused_documentation": DocumentationProfile(
        name="operator_focused_documentation",
        description="Operator Focused Documentation",
        generate_analyst_handbook=False,
        generate_developer_guide=False,
        notes="Operatör, Codex ajanı ve güvenli çalışma akışlarına odaklı dokümantasyon profili."
    ),
    "analyst_focused_documentation": DocumentationProfile(
        name="analyst_focused_documentation",
        description="Analyst Focused Documentation",
        generate_operator_manual=False,
        generate_developer_guide=False,
        generate_codex_agent_guide=False,
        notes="Analist çalışma alanı, raporlar, knowledge base ve araştırma workflow'larına odaklı profil."
    ),
    "developer_focused_documentation": DocumentationProfile(
        name="developer_focused_documentation",
        description="Developer Focused Documentation",
        generate_user_guide=False,
        generate_analyst_handbook=False,
        min_quality_score=0.55,
        notes="Kod ajanı, geliştirici rehberi, modül haritası ve script referanslarına odaklı profil."
    )
}

def get_documentation_profile(name: str) -> DocumentationProfile:
    if name not in _profiles:
        raise ConfigError(f"Bilinmeyen profile: {name}")
    return _profiles[name]

def list_documentation_profiles(enabled_only: bool = True) -> list[DocumentationProfile]:
    if enabled_only:
        return [p for p in _profiles.values() if p.enabled]
    return list(_profiles.values())

def validate_documentation_profiles() -> None:
    for name, profile in _profiles.items():
        if not profile.language:
            raise ConfigError(f"Profil {name} için language boş olamaz.")
        if not 0.0 <= profile.min_quality_score <= 1.0:
            raise ConfigError(f"Profil {name} için min_quality_score 0-1 aralığında olmalı.")
        if not any([
            profile.generate_user_guide,
            profile.generate_operator_manual,
            profile.generate_analyst_handbook,
            profile.generate_developer_guide,
            profile.generate_codex_agent_guide,
            profile.generate_safe_usage_guide,
            profile.generate_troubleshooting,
            profile.generate_references
        ]):
            raise ConfigError(f"Profil {name} için en az bir generate flag True olmalı.")

def get_default_documentation_profile() -> DocumentationProfile:
    return _profiles["balanced_documentation_pack"]
