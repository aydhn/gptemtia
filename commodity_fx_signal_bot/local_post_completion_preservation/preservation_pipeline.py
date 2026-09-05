import pandas as pd
from pathlib import Path
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

class LocalPostCompletionPreservationPipeline:
    def __init__(self, data_lake, settings, project_root: Path, profile: LocalPostCompletionPreservationProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile

    def build_preservation_domain_registry(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df = pd.DataFrame([{"mock": 1}])
        if save:
            pass
        return {"registry": df}, {"mock": True}

    def build_archive_seal_rehearsal(self, save: bool = True) -> tuple[str, dict]:
        return "rehearsal", {"mock": True}

    def build_immutable_readme_rehearsal(self, save: bool = True) -> tuple[str, dict]:
        return "readme", {"mock": True}

    def build_evidence_vault_index(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df = pd.DataFrame([{"mock": 1}])
        return {"index": df}, {"mock": True}

    def build_final_knowledge_capsule(self, save: bool = True) -> tuple[str, dict]:
        return "capsule", {"mock": True}

    def build_post_completion_preservation_binder(self, save: bool = True) -> tuple[str, dict]:
        return "binder", {"mock": True}

    def build_preservation_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        return {"q": True}, {"mock": True}

    def build_preservation_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "ok"}])
        return df, {"mock": True}
