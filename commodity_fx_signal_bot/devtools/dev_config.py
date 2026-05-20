from dataclasses import dataclass

@dataclass(frozen=True)
class DevExperienceProfile:
    name: str
    description: str
    required_python_min: str = "3.10"
    required_docs: tuple[str, ...] = (
        "README.md",
        "docs/DEVELOPER_SETUP.md",
        "docs/CLI_COMMANDS.md",
        "docs/TEST_MATRIX.md",
        "docs/TROUBLESHOOTING.md",
        "docs/LOCAL_RUNBOOK.md",
        "docs/MAINTENANCE_CHECKLIST.md",
    )
    required_project_files: tuple[str, ...] = (
        "pyproject.toml",
        "requirements.txt",
        "requirements-dev.txt",
        ".env.example",
        ".gitignore",
        "pytest.ini",
    )
    require_makefile: bool = True
    require_cli_help: bool = True
    require_main_guard_for_scripts: bool = True
    require_script_parse_args: bool = True
    max_cli_help_failures: int = 0
    enabled: bool = True
    notes: str = ""

def get_dev_experience_profile(name: str) -> DevExperienceProfile:
    profiles = {p.name: p for p in list_dev_experience_profiles()}
    if name not in profiles:
        raise ValueError(f"Unknown profile: {name}")
    return profiles[name]

def list_dev_experience_profiles(enabled_only: bool = True) -> list[DevExperienceProfile]:
    profiles = [
        DevExperienceProfile(
            name="balanced_dev_experience",
            description="Genel amaçlı geliştirici deneyimi kalite profili.",
            required_python_min="3.10",
            require_makefile=True,
            require_cli_help=True,
            require_main_guard_for_scripts=True,
            notes="Genel amaçlı geliştirici deneyimi kalite profili.",
        ),
        DevExperienceProfile(
            name="strict_dev_experience",
            description="CLI ve repo hijyeni için daha sıkı profil.",
            max_cli_help_failures=0,
            require_script_parse_args=True,
            require_main_guard_for_scripts=True,
            notes="CLI ve repo hijyeni için daha sıkı profil.",
        ),
        DevExperienceProfile(
            name="light_dev_experience",
            description="Hafif kontrol ve hızlı geliştirme için.",
            require_makefile=False,
            max_cli_help_failures=5,
            notes="Hafif kontrol ve hızlı geliştirme için.",
        ),
    ]
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def validate_dev_experience_profiles() -> None:
    for p in list_dev_experience_profiles(enabled_only=False):
        if not p.required_python_min:
            raise ValueError("required_python_min cannot be empty")
        if not p.required_docs:
            raise ValueError("required_docs cannot be empty")
        if not p.required_project_files:
            raise ValueError("required_project_files cannot be empty")
        if p.max_cli_help_failures < 0:
            raise ValueError("max_cli_help_failures cannot be negative")

def get_default_dev_experience_profile() -> DevExperienceProfile:
    return get_dev_experience_profile("balanced_dev_experience")
