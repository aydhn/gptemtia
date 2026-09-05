from .completion_config import LocalProjectCompletionProfile

def build_terminal_readme_map(profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    return "README map", {"note": "Manual review vurgusu zorunlu."}

def build_terminal_architecture_map(profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    return "Architecture map", {"note": "Manual review vurgusu zorunlu."}

def build_terminal_phase_map(profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    return "Phase map", {"note": "Manual review vurgusu zorunlu."}

def build_terminal_safety_boundary_map(profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    return "Safety boundary map", {"note": "Manual review vurgusu zorunlu."}

def build_terminal_maintenance_map(profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    return "Maintenance map", {"note": "Manual review vurgusu zorunlu."}

def summarize_terminal_maps(maps: dict[str, str]) -> dict:
    return {"maps": len(maps), "note": "Terminal maps official documentation freeze değildir."}
