from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any, Optional
import json

from data.storage.data_lake import DataLake
from config.settings import Settings
from documentation.documentation_config import DocumentationProfile, get_default_documentation_profile
from documentation.doc_generation import DocumentationGenerator
from documentation.doc_inventory import discover_documentation_files, summarize_documentation_inventory
from documentation.doc_coverage import build_documentation_coverage_report
from documentation.doc_link_checker import build_documentation_link_check_report
from documentation.doc_safety_scan import build_documentation_safety_scan_report
from documentation.doc_consistency import build_documentation_consistency_report
from documentation.doc_pack_manifest import build_documentation_pack_manifest, build_documentation_pack_manifest_json, summarize_documentation_pack_manifest
from documentation.doc_index_builder import build_documentation_index, build_script_reference, build_output_reference, build_safe_command_reference, build_module_map
from documentation.doc_quality import build_documentation_quality_report
from documentation.doc_report_builder import (
    build_documentation_pack_markdown_report,
    build_documentation_quality_markdown_report,
    build_safe_usage_docs_markdown_report,
    build_script_reference_markdown_report,
    build_output_reference_markdown_report,
    build_documentation_status_markdown_report
)

class DocumentationPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[DocumentationProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_documentation_profile()
        self.generator = DocumentationGenerator(self.project_root, self.profile)

    def _generate_templates(self) -> None:
        docs_dir = self.project_root / "docs"
        docs_dir.mkdir(parents=True, exist_ok=True)

        ug, _ = self.generator.generate_user_guide()
        self.generator.write_document("docs/USER_GUIDE.md", ug, overwrite=False)

        om, _ = self.generator.generate_operator_manual()
        self.generator.write_document("docs/OPERATOR_MANUAL.md", om, overwrite=False)

        ah, _ = self.generator.generate_analyst_handbook()
        self.generator.write_document("docs/ANALYST_HANDBOOK.md", ah, overwrite=False)

        dg, _ = self.generator.generate_developer_guide()
        self.generator.write_document("docs/DEVELOPER_GUIDE.md", dg, overwrite=False)

        cg, _ = self.generator.generate_codex_agent_guide()
        self.generator.write_document("docs/CODEX_AGENT_GUIDE.md", cg, overwrite=False)

        sg, _ = self.generator.generate_safe_usage_guide()
        self.generator.write_document("docs/SAFE_USAGE_GUIDE.md", sg, overwrite=False)

        tc, _ = self.generator.generate_troubleshooting_cookbook()
        self.generator.write_document("docs/TROUBLESHOOTING_COOKBOOK.md", tc, overwrite=False)

        refs, _ = self.generator.generate_faq_and_glossary()
        self.generator.write_document("docs/FAQ.md", refs.get("faq", ""), overwrite=False)
        self.generator.write_document("docs/GLOSSARY.md", refs.get("glossary", ""), overwrite=False)

        if self.profile.generate_references:
            self.generator.write_document("docs/DOCUMENTATION_INDEX.md", build_documentation_index(pd.DataFrame()), overwrite=True)
            self.generator.write_document("docs/SCRIPT_REFERENCE.md", build_script_reference(self.project_root), overwrite=True)
            self.generator.write_document("docs/OUTPUT_REFERENCE.md", build_output_reference(self.project_root), overwrite=True)
            self.generator.write_document("docs/SAFE_COMMAND_REFERENCE.md", build_safe_command_reference(self.project_root), overwrite=True)
            self.generator.write_document("docs/MODULE_MAP.md", build_module_map(self.project_root), overwrite=True)

    def build_documentation_pack_report(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:

        if self.settings.documentation_pack_enabled is False:
             return {}, {"status": "disabled"}

        self._generate_templates()

        docs_df = discover_documentation_files(self.project_root)
        inv_summary = summarize_documentation_inventory(docs_df)

        cov_df, cov_summary = build_documentation_coverage_report(self.project_root)
        safety_df, saf_summary = build_documentation_safety_scan_report(self.project_root)

        manifest = build_documentation_pack_manifest(self.profile, docs_df, cov_df, safety_df)
        manifest_json = build_documentation_pack_manifest_json(manifest, docs_df)
        manifest_summary = summarize_documentation_pack_manifest(manifest_json)

        if save:
            try:
                self.data_lake.save_documentation_inventory(docs_df, inv_summary)
                self.data_lake.save_documentation_coverage(cov_df, cov_summary)
                self.data_lake.save_documentation_pack_manifest(manifest.manifest_id, manifest_json)
            except AttributeError:
                pass

        return {"inventory": docs_df, "coverage": cov_df}, manifest_summary

    def build_documentation_quality_report(
        self,
        save: bool = True,
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:

        if self.settings.documentation_pack_enabled is False:
             return {}, {"status": "disabled"}

        docs_df = discover_documentation_files(self.project_root)
        cov_df, _ = build_documentation_coverage_report(self.project_root)
        lnk_df, _ = build_documentation_link_check_report(self.project_root)
        saf_df, _ = build_documentation_safety_scan_report(self.project_root)
        con_df, _ = build_documentation_consistency_report(self.project_root)

        quality = build_documentation_quality_report(
             {}, docs_df, cov_df, saf_df, lnk_df, con_df, self.profile
        )

        if save:
            try:
                self.data_lake.save_documentation_quality(self.profile.name, quality)
            except AttributeError:
                pass

        return quality, quality

    def build_safe_usage_docs_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        saf_df, saf_summary = build_documentation_safety_scan_report(self.project_root)
        return saf_df, saf_summary

    def build_script_reference_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        return pd.DataFrame(), {}

    def build_output_reference_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        return pd.DataFrame(), {}

    def build_documentation_status(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        return pd.DataFrame(), {}
