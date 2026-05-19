from pathlib import Path
import pandas as pd
from security.security_config import SecurityProfile
from security.security_models import SecurityFinding, build_security_finding_id
from security.secret_hygiene import detect_secret_like_value

class TokenLeakScanner:
    def __init__(self, profile: SecurityProfile):
        self.profile = profile
        self.exclude_dirs = [".git", "__pycache__", ".pytest_cache", "data/lake/ml/model_artifacts", ".venv", "venv"]

    def should_scan_file(self, path: Path) -> bool:
        if path.suffix not in self.profile.scan_text_extensions: return False
        if not path.exists(): return False
        try:
             if path.stat().st_size > self.profile.max_file_scan_mb * 1024 * 1024: return False
        except Exception: return False
        return True

    def scan_file(self, path: Path) -> tuple[list[SecurityFinding], dict]:
        findings = []
        if not self.should_scan_file(path): return findings, {}
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                for i, line in enumerate(f):
                    if "=" in line or ":" in line:
                        parts = line.split("=", 1) if "=" in line else line.split(":", 1)
                        det = detect_secret_like_value(parts[-1]) if len(parts) > 1 else {"is_secret": False}
                        if det.get("is_secret"):
                             if path.name == ".env.example": continue
                             findings.append(SecurityFinding(
                                finding_id=build_security_finding_id("token_leakage", f"leaked_token_{det['type']}", str(path), i+1),
                                category="token_leakage", severity="critical", status="security_failed",
                                title="Leaked Token Found", description=f"Found token of type {det['type']} in {path.name}",
                                file_path=str(path), line_number=i+1, blocking=self.profile.fail_on_secret_leak
                             ))
        except Exception: pass
        return findings, {}

    def scan_directory(self, root: Path, exclude_dirs: list[str] | None = None) -> tuple[pd.DataFrame, dict]:
        findings = []
        excludes = exclude_dirs or self.exclude_dirs
        for path in root.rglob("*"):
            if not path.is_file(): continue
            if any(ex in str(path) for ex in excludes): continue
            f, _ = self.scan_file(path)
            findings.extend(f)
        from security.security_models import security_finding_to_dict
        df = pd.DataFrame([security_finding_to_dict(f) for f in findings]) if findings else pd.DataFrame(columns=["finding_id"])
        return df, {"total_findings": len(findings)}
