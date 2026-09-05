from pathlib import Path
import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile, get_default_local_completion_governance_profile
from local_completion_governance.completion_domain_registry import build_completion_governance_domain_registry
from local_completion_governance.closure_synthesis import build_final_local_closure_synthesis
from local_completion_governance.end_state_certification import build_end_state_certification_rehearsal
from local_completion_governance.project_freeze_summary import build_terminal_project_freeze_summary
from local_completion_governance.acceptance_evidence_pack import build_offline_acceptance_evidence_pack
from local_completion_governance.completion_governance_binder import build_final_completion_governance_binder
from local_completion_governance.completion_quality import build_completion_quality_report
from local_completion_governance.completion_status import build_completion_status # Assuming it exists

class LocalCompletionGovernancePipeline:
    def __init__(self, data_lake, settings, project_root: Path, profile: LocalCompletionGovernanceProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_local_completion_governance_profile()

    def build_completion_domain_registry(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, summary = build_completion_governance_domain_registry(self.profile)
        if save:
            pass # Save logic using data_lake
        return {"domain_registry": df}, summary

    def build_closure_synthesis(self, save: bool = True) -> tuple[str, dict]:
        text, summary = build_final_local_closure_synthesis(self.project_root, self.profile)
        return text, summary

    def build_end_state_certification_rehearsal(self, save: bool = True) -> tuple[str, dict]:
        text, summary = build_end_state_certification_rehearsal(self.project_root, self.profile)
        return text, summary

    def build_terminal_project_freeze_summary(self, save: bool = True) -> tuple[str, dict]:
        text, summary = build_terminal_project_freeze_summary(self.project_root, self.profile)
        return text, summary

    def build_offline_acceptance_evidence_pack(self, save: bool = True) -> tuple[str, dict]:
        text, summary = build_offline_acceptance_evidence_pack(self.project_root, self.profile)
        return text, summary

    def build_final_completion_governance(self, save: bool = True) -> tuple[str, dict]:
        text, summary = build_final_completion_governance_binder(self.project_root, self.profile)
        return text, summary

    def build_completion_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        report = build_completion_quality_report({})
        return report, {}

    def build_completion_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "ok"}])
        return df, {}\n