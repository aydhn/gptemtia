from typing import Tuple, Dict, Any, List
from pathlib import Path

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def build_review_template_sections(review_type: str, profile: LocalMaintenanceProfile) -> List[Dict[str, str]]:
    sections = [
        {"title": "Review Date & Operator", "content": "- Date: YYYY-MM-DD\n- Operator: [Name]"},
        {"title": "Scope", "content": f"- Type: {review_type.capitalize()} Review\n- Profile: {profile.name}"},
        {"title": "Safe Local Commands Executed", "content": "- `python -m scripts.run_system_healthcheck`\n- `python -m scripts.run_consistency_status`"},
        {"title": "Reports Reviewed", "content": "- Secrets Hygiene\n- Artifact Staleness"},
        {"title": "Gaps Identified", "content": "- [List any maintenance gaps here]"},
        {"title": "Manual Follow-ups", "content": "- [List manual actions to take]"},
        {"title": "Go / No-Go (Maintenance)", "content": "- [Is the system reasonably maintained?]"},
        {"title": "Next Review Note", "content": "- Target Date: YYYY-MM-DD"},
        {"title": "Limitations & Disclaimers", "content": "This is a manual local maintenance review. It is not a production sign-off, official audit, or investment advice."}
    ]
    return sections

def _build_template_string(title: str, sections: List[Dict[str, str]]) -> str:
    lines = [f"# {title}\n"]
    for sec in sections:
        lines.append(f"## {sec['title']}")
        lines.append(sec['content'])
        lines.append("")
    return "\n".join(lines)

def build_monthly_review_template(profile: LocalMaintenanceProfile) -> Tuple[str, Dict[str, Any]]:
    sections = build_review_template_sections("monthly", profile)
    content = _build_template_string("Monthly Operator Review Template", sections)
    return content, {"type": "monthly"}

def build_quarterly_review_template(profile: LocalMaintenanceProfile) -> Tuple[str, Dict[str, Any]]:
    sections = build_review_template_sections("quarterly", profile)
    content = _build_template_string("Quarterly Operator Review Template", sections)
    return content, {"type": "quarterly"}

def save_review_template(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
