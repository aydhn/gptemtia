from pathlib import Path
from typing import Tuple, Dict, Any

from documentation.documentation_config import DocumentationProfile
from documentation.doc_templates import (
    build_user_guide_template,
    build_operator_manual_template,
    build_analyst_handbook_template,
    build_developer_guide_template,
    build_codex_agent_guide_template,
    build_safe_usage_guide_template,
    build_troubleshooting_template,
    build_faq_template,
    build_glossary_template
)

class DocumentationGenerator:
    def __init__(self, project_root: Path, profile: DocumentationProfile):
        self.project_root = project_root
        self.profile = profile

    def _prepare_content(self, template_func) -> Tuple[str, Dict[str, Any]]:
        content = template_func()
        metadata = {
            "profile_used": self.profile.name,
            "language": self.profile.language,
            "generated_with_disclaimer": self.profile.require_disclaimers
        }
        return content, metadata

    def generate_user_guide(self) -> Tuple[str, Dict[str, Any]]:
        if not self.profile.generate_user_guide:
            return "", {}
        return self._prepare_content(build_user_guide_template)

    def generate_operator_manual(self) -> Tuple[str, Dict[str, Any]]:
        if not self.profile.generate_operator_manual:
            return "", {}
        return self._prepare_content(build_operator_manual_template)

    def generate_analyst_handbook(self) -> Tuple[str, Dict[str, Any]]:
        if not self.profile.generate_analyst_handbook:
            return "", {}
        return self._prepare_content(build_analyst_handbook_template)

    def generate_developer_guide(self) -> Tuple[str, Dict[str, Any]]:
        if not self.profile.generate_developer_guide:
            return "", {}
        return self._prepare_content(build_developer_guide_template)

    def generate_codex_agent_guide(self) -> Tuple[str, Dict[str, Any]]:
        if not self.profile.generate_codex_agent_guide:
            return "", {}
        return self._prepare_content(build_codex_agent_guide_template)

    def generate_safe_usage_guide(self) -> Tuple[str, Dict[str, Any]]:
        if not self.profile.generate_safe_usage_guide:
            return "", {}
        return self._prepare_content(build_safe_usage_guide_template)

    def generate_troubleshooting_cookbook(self) -> Tuple[str, Dict[str, Any]]:
        if not self.profile.generate_troubleshooting:
            return "", {}
        return self._prepare_content(build_troubleshooting_template)

    def generate_faq_and_glossary(self) -> Tuple[Dict[str, str], Dict[str, Any]]:
        results = {}
        metadata = {
             "profile_used": self.profile.name,
             "language": self.profile.language,
        }
        if self.profile.generate_references:
            results["faq"] = build_faq_template()
            results["glossary"] = build_glossary_template()
        return results, metadata

    def write_document(self, relative_path: str, content: str, overwrite: bool = True) -> Path:
        if not content:
            return self.project_root / relative_path

        full_path = self.project_root / relative_path
        full_path.parent.mkdir(parents=True, exist_ok=True)

        if full_path.exists() and not overwrite:
            return full_path

        # Protect manual content if possible (simple marker approach)
        existing_content = ""
        if full_path.exists():
            with open(full_path, "r", encoding="utf-8") as f:
                existing_content = f.read()

        manual_section = ""
        if "<!-- AUTO-GENERATED SECTION END -->" in existing_content:
             parts = existing_content.split("<!-- AUTO-GENERATED SECTION END -->")
             if len(parts) > 1:
                 manual_section = parts[1]

        final_content = "<!-- AUTO-GENERATED SECTION START -->\n" + content + "\n<!-- AUTO-GENERATED SECTION END -->\n" + manual_section

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(final_content)

        return full_path
