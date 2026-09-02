import pandas as pd
from pathlib import Path
from local_release_candidate.release_candidate_config import LocalReleaseCandidateProfile

class LocalReleaseCandidatePipeline:
    def __init__(
        self,
        data_lake,
        settings,
        project_root: Path,
        profile: LocalReleaseCandidateProfile | None = None,
    ):
        pass

    def build_release_candidate_domain_registry(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        return {}, {}

    def build_final_local_release_candidate(self, save: bool = True) -> tuple[str, dict]:
        return "mock", {}

    def build_frozen_baseline_snapshot(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        return {}, {}

    def build_final_acceptance_rehearsal(self, save: bool = True) -> tuple[dict[str, pd.DataFrame] | str, dict]:
        return "mock", {}

    def build_v1_offline_release_dossier(self, save: bool = True) -> tuple[str, dict]:
        return "mock", {}

    def build_release_candidate_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        return {}, {}

    def build_release_candidate_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        return pd.DataFrame(), {}
