def build_continuity_command_interpretation_guide(profile) -> tuple[str, dict]:
    return "guide", {"len": 5}
def build_continuity_output_interpretation_guide(profile) -> tuple[str, dict]:
    return "guide", {"len": 5}
def summarize_continuity_interpretation_guides(cmd: str, out: str) -> dict:
    return {"cmd_len": len(cmd), "out_len": len(out)}