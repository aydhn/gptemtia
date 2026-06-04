from pathlib import Path

root = Path("commodity_fx_signal_bot")

readme_path = root / "README.md"
readme_content = readme_path.read_text(encoding="utf-8")
new_readme_section = """
## Secrets Hygiene, Credential Boundary and Private Data Protection
* The secrets hygiene layer does not report real secret values.
* The scanner does not modify files, delete secrets, or perform overwrites.
* The `.env` file is never read; `.env.example` is audited instead.
* Findings are masked and intended for manual review.
* There is no cloud vault or external scanner integration.
* Backup/packaging manifests are checked for secret exclusions.
* Private data scanning provides warnings but is not a legal compliance guarantee.
* Outputs are generated under `data/lake/secrets_hygiene` and `reports/output/secrets_hygiene`.

```bash
python -m scripts.run_sensitive_file_scan
python -m scripts.run_env_template_audit
python -m scripts.run_credential_boundary_report
python -m scripts.run_private_data_protection_report
python -m scripts.run_secret_remediation_report
python -m scripts.run_secrets_quality_report
python -m scripts.run_secrets_hygiene_status
```
"""
if "Secrets Hygiene, Credential Boundary" not in readme_content:
    with open(readme_path, "a", encoding="utf-8") as f:
        f.write("\n" + new_readme_section)

arch_path = root / "docs" / "ARCHITECTURE.md"
if arch_path.exists():
    arch_content = arch_path.read_text(encoding="utf-8")
    new_arch = """
### Secrets Hygiene Flow
Project Files / Config Templates / Docs / Reports / DataLake / Backup-Packaging Manifests
-> SensitiveFileScanner
-> SecretPatterns
-> EntropyDetector
-> Redaction
-> EnvTemplateAuditor
-> CredentialBoundary
-> PrivateDataScanner
-> GitignoreAuditor
-> ConfigBoundaryAuditor
-> LeakageScanner
-> Source/Test/Docs Secret Auditors
-> BackupPackagingBoundary
-> RemediationRecommendations
-> SecretHygieneRunbook
-> SecretsSafety
-> SecretsQuality
-> Secrets Hygiene Outputs
"""
    if "Secrets Hygiene Flow" not in arch_content:
        with open(arch_path, "a", encoding="utf-8") as f:
            f.write("\n" + new_arch)

phase_log = root / "docs" / "PHASE_LOG.md"
if phase_log.exists():
    phase_content = phase_log.read_text(encoding="utf-8")
    new_phase = """
### Phase 63
- Secrets hygiene profile sistemi eklendi.
- Secret label registry eklendi.
- SensitiveFileRecord, SecretFinding, CredentialBoundaryResult, EnvTemplateAuditItem ve SecretRemediationRecommendation modelleri eklendi.
- Redaction utilities eklendi.
- Secret pattern scanner eklendi.
- High entropy detector eklendi.
- Sensitive file scanner eklendi.
- Env template auditor eklendi.
- Credential boundary audit eklendi.
- Private data scanner eklendi.
- Gitignore hygiene auditor eklendi.
- Config boundary auditor eklendi.
- Log/report/generated output leakage scanner eklendi.
- Source/test/docs secret scanners eklendi.
- Backup/packaging secret boundary eklendi.
- Remediation recommendation report eklendi.
- Secret hygiene runbook eklendi.
- Secrets safety ve quality report eklendi.
- SecretsHygienePipeline eklendi.
- DataLake secrets hygiene kayıt desteği aldı.
- Secrets hygiene scriptleri eklendi.
- Testler genişletildi.
"""
    if "Phase 63" not in phase_content:
        with open(phase_log, "a", encoding="utf-8") as f:
            f.write("\n" + new_phase)

for doc in ["CONFIGURATION.md", "OPERATOR_MANUAL.md", "CODEX_AGENT_GUIDE.md", "SAFE_USAGE_GUIDE.md"]:
    p = root / "docs" / doc
    if p.exists():
        content = p.read_text(encoding="utf-8")
        if "Secrets Hygiene" not in content:
            new_content = """
## Secrets Hygiene
- **.env vs .env.example:** Real secrets live in `.env` (which is ignored). `.env.example` must only contain placeholders.
- **Reporting:** Secret values are never written to reports to prevent leaks.
- **Masked Findings:** Findings display masked representations (e.g. `abc****xyz`) for safe review.
- **Credential Boundary:** Checks ensure secrets don't bleed into source code, tests, docs, or reports.
- **Private Data Scanner:** Flags potential personal data (emails, phones) but is not a substitute for formal compliance.
- **Backup/Packaging:** Manifests are checked to ensure sensitive files like `.env` are excluded.
- **No Automatic Operations:** The tool will not automatically delete files, overwrite secrets, or integrate with cloud vaults.
"""
            with open(p, "a", encoding="utf-8") as f:
                f.write("\n" + new_content)

gitignore = root / ".gitignore"
if gitignore.exists():
    with open(gitignore, "a", encoding="utf-8") as f:
        f.write("\n# Secrets Hygiene Outputs\n")
        f.write("data/lake/secrets_hygiene/\n")
        f.write("reports/output/secrets_hygiene/\n")
        f.write("docs/generated/secrets_hygiene/\n")
