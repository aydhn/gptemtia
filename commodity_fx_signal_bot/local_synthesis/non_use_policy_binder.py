from typing import Tuple, Dict, List
from .synthesis_config import LocalSynthesisProfile

def build_non_use_policy_sections(profile: LocalSynthesisProfile) -> List[Dict]:
    return []

def build_final_non_use_policy_binder(profile: LocalSynthesisProfile) -> Tuple[str, Dict]:
    text = "# Non-Use Policy Binder\nOffline/local only. No investment advice."
    return text, summarize_non_use_policy_binder(text)

def summarize_non_use_policy_binder(text: str) -> Dict:
    return {"length": len(text)}
