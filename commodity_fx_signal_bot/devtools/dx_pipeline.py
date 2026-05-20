from pathlib import Path
import pandas as pd
from .dev_config import DevExperienceProfile, get_default_dev_experience_profile
from .cli_catalog import build_cli_command_catalog, export_cli_catalog_markdown
from .cli_help_audit import audit_cli_help, build_cli_help_audit_report
from .import_smoke import run_import_smoke_test, build_import_smoke_report, list_project_packages
from .test_matrix import build_test_matrix, export_test_matrix_markdown
from .package_audit import build_package_audit_report
from .repo_hygiene import build_repo_hygiene_report
from .docs_audit import build_docs_audit_report
from .dx_quality import build_dx_quality_report

class DeveloperExperiencePipeline:
    def __init__(
        self,
        project_root: Path,
        profile: DevExperienceProfile | None = None,
    ):
        self.project_root = project_root
        self.profile = profile or get_default_dev_experience_profile()

    def run_cli_catalog(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        return build_cli_command_catalog(self.project_root)

    def run_cli_help_audit(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        return audit_cli_help(self.project_root)

    def run_import_smoke_test(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        packages = list_project_packages(self.project_root)
        return run_import_smoke_test(packages)

    def run_test_matrix_report(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        return build_test_matrix(self.project_root)

    def run_package_audit(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        return build_package_audit_report(self.project_root, self.profile)

    def run_repo_hygiene_check(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        return build_repo_hygiene_report(self.project_root, self.profile)

    def run_docs_audit(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        return build_docs_audit_report(self.project_root, self.profile)

    def run_full_dx_check(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df1, _ = self.run_package_audit(save=False)
        df2, _ = self.run_repo_hygiene_check(save=False)
        df3, _ = self.run_docs_audit(save=False)

        all_findings = pd.concat([df1, df2, df3], ignore_index=True) if not all(x.empty for x in [df1, df2, df3]) else pd.DataFrame()
        summary = build_dx_quality_report(all_findings, {})

        return all_findings, summary
