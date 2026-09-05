"""Reproducibility pipeline."""
import pandas as pd
from pathlib import Path
from .reproducibility_config import LocalReproducibilityGovernanceProfile, get_default_local_reproducibility_governance_profile
from .reproducibility_domain_registry import build_reproducibility_domain_registry
from .reproducibility_dossier import build_final_local_reproducibility_dossier
from .environment_replay_manifest import build_environment_replay_manifest
from .deterministic_runbook import build_deterministic_runbook
from .build_free_reproduction import build_build_free_reproduction_manifest
from .reproducibility_governance_binder import build_terminal_reproducibility_governance_binder
from .reproducibility_quality import build_reproducibility_quality_report

class LocalReproducibilityGovernancePipeline:
    def __init__(
        self,
        data_lake,
        settings,
        project_root: Path,
        profile: LocalReproducibilityGovernanceProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_local_reproducibility_governance_profile()

    def build_reproducibility_domain_registry(
        self,
        save: bool = True,
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        df, summary = build_reproducibility_domain_registry(self.profile)
        if save:
            try:
                self.data_lake.save_reproducibility_domain_registry(df, summary)
            except AttributeError:
                pass
        return {"domain_registry": df}, summary

    def build_reproducibility_dossier(
        self,
        save: bool = True,
    ) -> tuple[str, dict]:
        text, summary = build_final_local_reproducibility_dossier(self.project_root, self.profile)
        if save:
            try:
                self.data_lake.save_final_local_reproducibility_dossier(text, summary)
            except AttributeError:
                pass
        return text, summary

    def build_environment_replay_manifest(
        self,
        save: bool = True,
    ) -> tuple[str, dict]:
        text, summary = build_environment_replay_manifest(self.project_root, self.profile)
        if save:
            try:
                self.data_lake.save_environment_replay_manifest(text, summary)
            except AttributeError:
                pass
        return text, summary

    def build_deterministic_runbook(
        self,
        save: bool = True,
    ) -> tuple[str, dict]:
        text, summary = build_deterministic_runbook(self.project_root, self.profile)
        if save:
            try:
                self.data_lake.save_deterministic_runbook(text, summary)
            except AttributeError:
                pass
        return text, summary

    def build_build_free_reproduction_layer(
        self,
        save: bool = True,
    ) -> tuple[str, dict]:
        text, summary = build_build_free_reproduction_manifest(self.project_root, self.profile)
        if save:
            try:
                self.data_lake.save_build_free_reproduction_manifest(text, summary)
            except AttributeError:
                pass
        return text, summary

    def build_terminal_reproducibility_governance(
        self,
        save: bool = True,
    ) -> tuple[str, dict]:
        text, summary = build_terminal_reproducibility_governance_binder(self.project_root, self.profile)
        if save:
            try:
                self.data_lake.save_terminal_reproducibility_governance_binder(text, summary)
            except AttributeError:
                pass
        return text, summary

    def build_reproducibility_quality_report(
        self,
        save: bool = True,
    ) -> tuple[dict, dict]:
        q = build_reproducibility_quality_report({})
        if save:
            try:
                self.data_lake.save_reproducibility_quality(self.profile.name, q)
            except AttributeError:
                pass
        return q, {}

    def build_reproducibility_status(
        self,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "ok"}])
        return df, {}
