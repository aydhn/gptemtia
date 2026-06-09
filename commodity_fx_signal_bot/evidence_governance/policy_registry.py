import pandas as pd
from evidence_governance.evidence_config import EvidenceGovernanceProfile
from evidence_governance.evidence_models import PolicyItem, build_policy_id

def build_default_policy_registry(profile: EvidenceGovernanceProfile) -> list[PolicyItem]:
    policies = [
        ("Offline-only operation policy", "operational", "Tüm süreçler offline/local çalışmalıdır.", ["operational_controls"]),
        ("No live order policy", "safety", "Sistem canlı emir gönderemez.", ["safety_controls"]),
        ("No broker execution policy", "safety", "Broker entegrasyonu ve talimatı yasaktır.", ["safety_controls"]),
        ("No investment advice policy", "safety", "Üretilen raporlar yatırım tavsiyesi içeremez.", ["safety_controls", "documentation_controls"]),
        ("No external LLM/API policy", "safety", "Harici LLM veya API çağrısı yapılamaz.", ["safety_controls"]),
        ("No web scraping policy", "operational", "Web scraping araçları kullanılamaz.", ["operational_controls"]),
        ("Secrets redaction policy", "secrets", "Raporlarda secret değerleri maskelenmelidir.", ["secrets_controls"]),
        ("Env template hygiene policy", "secrets", ".env.example dosyası template standartlarına uymalıdır.", ["secrets_controls"]),
        ("Backup/restore dry-run policy", "backup", "Backup ve restore işlemleri dry-run olarak doğrulanabilmelidir.", ["backup_recovery_controls"]),
        ("Packaging manifest-only policy", "packaging", "Packaging sadece manifest üretmeli, payload export etmemelidir.", ["packaging_controls"]),
        ("Quality gate evidence policy", "quality", "Her modül quality gate sonuçlarını kaydetmelidir.", ["quality_controls"]),
        ("Scenario regression evidence policy", "scenario", "Senaryo regresyon testleri kanıt üretmelidir.", ["scenario_regression_controls"]),
        ("Final review evidence policy", "review", "Final review işlemleri kanıtlanmalıdır.", ["final_review_controls"]),
        ("Documentation traceability policy", "documentation", "Dokümantasyon çıktıları güncel olmalıdır.", ["documentation_controls"]),
        ("Master orchestration dry-run policy", "orchestration", "Master pipeline dry-run plan üretmelidir.", ["master_orchestration_controls"]),
    ]

    registry = []
    for name, domain, desc, controls in policies:
        pol_id = build_policy_id(name, domain)
        registry.append(PolicyItem(
            policy_id=pol_id,
            policy_name=name,
            policy_domain=domain,
            description=desc,
            local_only=True,
            official_compliance_claim=False,
            controls=controls,
            warnings=[]
        ))

    return registry

def policy_registry_to_dataframe(policies: list[PolicyItem]) -> pd.DataFrame:
    from evidence_governance.evidence_models import policy_item_to_dict
    if not policies:
        return pd.DataFrame()
    return pd.DataFrame([policy_item_to_dict(p) for p in policies])

def validate_policy_registry(policy_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> dict:
    if policy_df is None or policy_df.empty:
        return {"passed": False, "warnings": ["Empty policy registry"]}

    warnings = []
    passed = True

    if "official_compliance_claim" in policy_df.columns:
        if policy_df["official_compliance_claim"].any():
            passed = False
            warnings.append("Found official_compliance_claim=True in policies")

    return {"passed": passed, "warnings": warnings}

def summarize_policy_registry(policy_df: pd.DataFrame) -> dict:
    if policy_df is None or policy_df.empty:
        return {"total_policies": 0}

    return {
        "total_policies": len(policy_df),
        "domains": policy_df["policy_domain"].value_counts().to_dict() if "policy_domain" in policy_df.columns else {}
    }
