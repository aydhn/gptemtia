from pathlib import Path
import pandas as pd
from security.security_config import SecurityProfile
from security.security_models import SecurityFinding, build_security_finding_id

_DISALLOWED_IMPORTS = ["selenium", "playwright", "bs4", "beautifulsoup", "scrapy", "pyautogui", "keyboard", "pynput"]
_NETWORK_IMPORTS = ["requests", "urllib", "httpx", "aiohttp"]

def list_imported_modules(project_root: Path) -> tuple[pd.DataFrame, dict]: return pd.DataFrame(), {}
def check_requirements_safety(requirements_path: Path | None = None) -> tuple[list[SecurityFinding], dict]: return [], {}

def detect_disallowed_imports(project_root: Path) -> tuple[list[SecurityFinding], dict]:
    findings = []
    req_path = project_root / "requirements.txt"
    if req_path.exists():
        with open(req_path, "r", encoding="utf-8") as f:
            content = f.read().lower()
            for pkg in _DISALLOWED_IMPORTS:
                if pkg in content:
                    findings.append(SecurityFinding(
                        finding_id=build_security_finding_id("dependency_security", f"disallowed_import_{pkg}"),
                        category="dependency_security", severity="critical", status="security_failed",
                        title=f"Disallowed import found: {pkg}", description=f"Package {pkg} is disallowed.", blocking=True
                    ))
    return findings, {}

def detect_network_related_imports(project_root: Path) -> tuple[list[SecurityFinding], dict]:
    findings = []
    req_path = project_root / "requirements.txt"
    if req_path.exists():
        with open(req_path, "r", encoding="utf-8") as f:
            content = f.read().lower()
            for pkg in _NETWORK_IMPORTS:
                if pkg in content:
                    findings.append(SecurityFinding(
                        finding_id=build_security_finding_id("dependency_security", f"network_import_{pkg}"),
                        category="dependency_security", severity="info", status="security_passed",
                        title=f"Network import found: {pkg}", description=f"Package {pkg} is a network surface.", blocking=False
                    ))
    return findings, {}

def build_dependency_security_report(project_root: Path, profile: SecurityProfile) -> tuple[pd.DataFrame, dict]:
    findings = []
    f1, _ = detect_disallowed_imports(project_root)
    f2, _ = detect_network_related_imports(project_root)
    findings.extend(f1); findings.extend(f2)
    from security.security_models import security_finding_to_dict
    df = pd.DataFrame([security_finding_to_dict(f) for f in findings]) if findings else pd.DataFrame(columns=["finding_id"])
    return df, {"total_findings": len(findings)}
