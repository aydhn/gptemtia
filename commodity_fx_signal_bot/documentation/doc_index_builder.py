from pathlib import Path
import pandas as pd

from documentation.doc_templates import build_standard_disclaimer

def build_documentation_index(docs_df: pd.DataFrame, coverage_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Dokümantasyon İndeksi (Documentation Index)",
        build_standard_disclaimer(),
        "",
        "Bu indeks, sistemdeki tüm offline araştırma dokümanlarının bir haritasıdır.",
        "",
        "## Başlangıç Rehberleri",
        "- [Kullanıcı Kılavuzu](USER_GUIDE.md)",
        "- [Güvenli Kullanım Kılavuzu](SAFE_USAGE_GUIDE.md)",
        "",
        "## Rol Bazlı Kılavuzlar",
        "- [Operatör El Kitabı](OPERATOR_MANUAL.md)",
        "- [Analist El Kitabı](ANALYST_HANDBOOK.md)",
        "- [Geliştirici Kılavuzu](DEVELOPER_GUIDE.md)",
        "- [Codex Agent Kılavuzu](CODEX_AGENT_GUIDE.md)",
        "",
        "## Referanslar",
        "- [Modül Haritası](MODULE_MAP.md)",
        "- [Script Referansı](SCRIPT_REFERENCE.md)",
        "- [Çıktı Referansı](OUTPUT_REFERENCE.md)",
        "- [Güvenli Komut Referansı](SAFE_COMMAND_REFERENCE.md)",
        "- [Sözlük](GLOSSARY.md)",
        "- [SSS](FAQ.md)",
        "",
        "## Sorun Giderme",
        "- [Troubleshooting Cookbook](TROUBLESHOOTING_COOKBOOK.md)",
        ""
    ]
    return "\n".join(lines)

def build_script_reference(project_root: Path) -> str:
    lines = [
        "# Script Referansı (Script Reference)",
        build_standard_disclaimer(),
        "",
        "Sistemde bulunan ve çalıştırılabilir `scripts/` klasörü altındaki komutlar listelenmiştir.",
        "Hiçbir script canlı broker'a bağlanmaz veya emir göndermez.",
        "",
        "## Güvenli Komutlar"
    ]

    scripts_dir = project_root / "scripts"
    if scripts_dir.exists():
        for script in sorted(scripts_dir.glob("run_*.py")):
            lines.append(f"- `python -m scripts.{script.stem}`: Offline pipeline çalıştırır.")

    return "\n".join(lines)

def build_output_reference(project_root: Path) -> str:
    lines = [
        "# Çıktı Referansı (Output Reference)",
        build_standard_disclaimer(),
        "",
        "Sistemin ürettiği offline dosyaların dizin yapısı:",
        "",
        "## Data Lake (`data/lake/`)",
        "- `raw/`: Ham indirilen veriler.",
        "- `features/`: Hesaplanmış feature'lar.",
        "",
        "## Reports (`reports/output/`)",
        "- `markdown/`: İnsan okunabilir raporlar.",
        "- `csv/`: Tablo verileri.",
        "- `json/`: Metadata ve manifestolar.",
        ""
    ]
    return "\n".join(lines)

def build_safe_command_reference(project_root: Path) -> str:
    lines = [
        "# Güvenli Komut Referansı (Safe Command Reference)",
        build_standard_disclaimer(),
        "",
        "Bu komutlar sistemi güvenli bir şekilde (dry-run / offline modda) çalıştırır:",
        "",
        "- `make setup`: Ortamı kurar.",
        "- `make test`: Testleri çalıştırır.",
        "- `python main.py`: Offline sinyal adaylarını oluşturur.",
        "- `make dx`: Geliştirici kalite araçlarını çalıştırır.",
        ""
    ]
    return "\n".join(lines)

def build_module_map(project_root: Path) -> str:
    lines = [
        "# Modül Haritası (Module Map)",
        build_standard_disclaimer(),
        "",
        "Sistem Mimarisini oluşturan ana modüller:",
        "",
        "- `data/`: Veri indirme ve ön işleme.",
        "- `indicators/`, `features/`: Özellik mühendisliği.",
        "- `signals/`, `decisions/`: Aday oluşturma (canlı emir üretmez).",
        "- `ml/`: Çevrimdışı yapay zeka modelleri.",
        "- `reports/`: Sonuç raporlama.",
        ""
    ]
    return "\n".join(lines)
