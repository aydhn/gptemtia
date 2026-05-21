from dataclasses import dataclass, field
from config.settings import settings

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class ReportExportProfile:
    name: str
    description: str
    language: str = "tr"
    include_html: bool = True
    include_pdf: bool = True
    include_csv_bundle: bool = True
    archive_enabled: bool = True
    comparison_enabled: bool = True
    periodic_tracking_enabled: bool = True
    max_archive_records: int = 5000
    max_comparison_rows: int = 100
    pdf_engine: str = "auto"
    html_theme: str = "clean_research"
    require_disclaimer: bool = True
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

    def __post_init__(self):
        if self.max_archive_records <= 0:
            raise ConfigError("max_archive_records must be positive")
        if self.max_comparison_rows <= 0:
            raise ConfigError("max_comparison_rows must be positive")
        if not (0.0 <= self.min_quality_score <= 1.0):
            raise ConfigError("min_quality_score must be between 0.0 and 1.0")
        if self.pdf_engine not in ["auto", "weasyprint", "reportlab", "none"]:
            raise ConfigError("pdf_engine must be 'auto', 'weasyprint', 'reportlab', or 'none'")
        if not self.html_theme:
            raise ConfigError("html_theme cannot be empty")


_EXPORT_PROFILES = {
    "balanced_report_export": ReportExportProfile(
        name="balanced_report_export",
        description="General purpose HTML/PDF/CSV packaging and archiving profile.",
        include_html=True,
        include_pdf=True,
        include_csv_bundle=True,
        archive_enabled=True,
        comparison_enabled=True,
        periodic_tracking_enabled=True,
        pdf_engine="auto",
        html_theme="clean_research",
        notes="Genel amaçlı HTML/PDF/CSV paketleme ve arşiv profili."
    ),
    "html_only_report_export": ReportExportProfile(
        name="html_only_report_export",
        description="Produces HTML and CSV bundle without PDF dependency.",
        include_html=True,
        include_pdf=False,
        include_csv_bundle=True,
        archive_enabled=True,
        comparison_enabled=True,
        periodic_tracking_enabled=True,
        notes="PDF bağımlılığı olmadan HTML ve CSV rapor paketi üretir."
    ),
    "pdf_focused_report_export": ReportExportProfile(
        name="pdf_focused_report_export",
        description="Focused on producing PDF outputs for professional sharing.",
        include_html=True,
        include_pdf=True,
        include_csv_bundle=True,
        pdf_engine="auto",
        notes="Profesyonel paylaşım için PDF çıktıya odaklı profil."
    ),
    "archive_only_report_export": ReportExportProfile(
        name="archive_only_report_export",
        description="Produces only archive, manifest, comparisons and periodic tracking.",
        include_html=False,
        include_pdf=False,
        include_csv_bundle=False,
        archive_enabled=True,
        comparison_enabled=True,
        periodic_tracking_enabled=True,
        notes="Sadece rapor arşiv, manifest, karşılaştırma ve dönemsel takip üretir."
    ),
}

def get_report_export_profile(name: str) -> ReportExportProfile:
    if name not in _EXPORT_PROFILES:
        raise ConfigError(f"Unknown ReportExportProfile: {name}")
    return _EXPORT_PROFILES[name]

def list_report_export_profiles(enabled_only: bool = True) -> list[ReportExportProfile]:
    profiles = list(_EXPORT_PROFILES.values())
    if enabled_only:
        profiles = [p for p in profiles if p.enabled]
    return profiles

def validate_report_export_profiles() -> None:
    for profile in _EXPORT_PROFILES.values():
        if profile.max_archive_records <= 0:
            raise ConfigError("max_archive_records must be positive")
        if profile.max_comparison_rows <= 0:
            raise ConfigError("max_comparison_rows must be positive")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ConfigError("min_quality_score must be between 0.0 and 1.0")
        if profile.pdf_engine not in ["auto", "weasyprint", "reportlab", "none"]:
            raise ConfigError("pdf_engine must be 'auto', 'weasyprint', 'reportlab', or 'none'")
        if not profile.html_theme:
            raise ConfigError("html_theme cannot be empty")

def get_default_report_export_profile() -> ReportExportProfile:
    try:
        return get_report_export_profile(settings.default_report_export_profile)
    except ConfigError:
        return get_report_export_profile("balanced_report_export")
