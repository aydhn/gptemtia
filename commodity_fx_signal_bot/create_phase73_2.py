import os

with open("local_training/training_domain_registry.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from .training_config import LocalTrainingProfile
from .training_models import TrainingDomain, build_training_domain_id, training_domain_to_dict

def build_default_training_domains(profile: LocalTrainingProfile) -> list[TrainingDomain]:
    return [
        TrainingDomain(
            domain_id=build_training_domain_id("operator_training"),
            domain_name="operator_training",
            domain_label="operator_training",
            description="Operator training for local/offline usage",
            target_roles=["operator_role"],
            required_materials=["OPERATOR_MANUAL.md", "SAFE_USAGE_GUIDE.md"],
            warnings=["Bu domain resmi eğitim kapsamı değildir.", "Canlı işlem yetkisi vermez."]
        ),
        TrainingDomain(
            domain_id=build_training_domain_id("analyst_training"),
            domain_name="analyst_training",
            domain_label="analyst_training",
            description="Analyst training for local research",
            target_roles=["analyst_role"],
            required_materials=["ANALYST_HANDBOOK.md"],
            warnings=["Bu domain resmi eğitim kapsamı değildir.", "Yatırım tavsiyesi vermez."]
        ),
        TrainingDomain(
            domain_id=build_training_domain_id("developer_training"),
            domain_name="developer_training",
            domain_label="developer_training",
            description="Developer training for project maintenance",
            target_roles=["developer_role", "maintainer_role"],
            required_materials=["ARCHITECTURE.md", "README.md"],
            warnings=["Bu domain resmi eğitim kapsamı değildir."]
        ),
        TrainingDomain(
            domain_id=build_training_domain_id("safe_usage_training"),
            domain_name="safe_usage_training",
            domain_label="safe_usage_training",
            description="Safe usage guidelines for offline tool",
            target_roles=["operator_role", "analyst_role", "developer_role"],
            required_materials=["SAFE_USAGE_GUIDE.md"],
            warnings=["Bu domain resmi eğitim kapsamı değildir."]
        ),
        TrainingDomain(
            domain_id=build_training_domain_id("non_use_policy_training"),
            domain_name="non_use_policy_training",
            domain_label="non_use_policy_training",
            description="Non-use policy covering forbidden actions",
            target_roles=["operator_role", "analyst_role", "developer_role"],
            required_materials=["SAFE_USAGE_GUIDE.md"],
            warnings=["Bu domain resmi eğitim kapsamı değildir."]
        )
    ]

def build_training_domain_registry(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_training_domains(profile)
    df = pd.DataFrame([training_domain_to_dict(d) for d in domains])
    return df, summarize_training_domains(df)

def summarize_training_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df is None or domain_df.empty:
        return {"total_domains": 0}
    return {
        "total_domains": len(domain_df),
        "domain_labels": domain_df["domain_label"].tolist()
    }
''')

with open("local_training/onboarding_paths.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from .training_config import LocalTrainingProfile
from .training_models import OnboardingPath, build_onboarding_path_id, onboarding_path_to_dict

def build_operator_onboarding_path(profile: LocalTrainingProfile) -> OnboardingPath:
    return OnboardingPath(
        path_id=build_onboarding_path_id("operator_role", "Operator Path"),
        role_label="operator_role",
        path_name="Operator Path",
        description="Onboarding path for operators",
        modules=["güvenli kullanım", "kurulum okuma", "status komutları", "rapor okuma", "DataLake klasörleri", "no-go/safe-go sınırları", "DR/maintenance/archive statüleri"],
        expected_outcomes=["Can read reports", "Can run status commands"],
        warnings=["Onboarding path production authorization değildir.", "Finansal tavsiye eğitimi üretmez.", "Broker/live/deploy yok."]
    )

def build_analyst_onboarding_path(profile: LocalTrainingProfile) -> OnboardingPath:
    return OnboardingPath(
        path_id=build_onboarding_path_id("analyst_role", "Analyst Path"),
        role_label="analyst_role",
        path_name="Analyst Path",
        description="Onboarding path for analysts",
        modules=["araştırma raporları", "backtest/paper sınırları", "evidence/metadata cards", "scenario/regression outputs", "non-use policy", "yatırım tavsiyesi olmayan yorumlama"],
        expected_outcomes=["Can interpret research", "Understands limitations"],
        warnings=["Onboarding path production authorization değildir.", "Finansal tavsiye eğitimi üretmez.", "Broker/live/deploy yok."]
    )

def build_developer_onboarding_path(profile: LocalTrainingProfile) -> OnboardingPath:
    return OnboardingPath(
        path_id=build_onboarding_path_id("developer_role", "Developer Path"),
        role_label="developer_role",
        path_name="Developer Path",
        description="Onboarding path for developers",
        modules=["repo mimarisi", "scripts contract", "tests", "DataLake save/load", "local graph/timeline/consistency/readiness/maintenance/archive/DR modules", "safety boundaries"],
        expected_outcomes=["Can extend project locally"],
        warnings=["Onboarding path production authorization değildir.", "Broker/live/deploy yok."]
    )

def build_maintainer_onboarding_path(profile: LocalTrainingProfile) -> OnboardingPath:
    return OnboardingPath(
        path_id=build_onboarding_path_id("maintainer_role", "Maintainer Path"),
        role_label="maintainer_role",
        path_name="Maintainer Path",
        description="Onboarding path for maintainers",
        modules=["repo mimarisi", "safety boundaries", "maintenance outputs"],
        expected_outcomes=["Can review and maintain project locally"],
        warnings=["Onboarding path production authorization değildir."]
    )

def build_role_based_onboarding_paths(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    paths = [
        build_operator_onboarding_path(profile),
        build_analyst_onboarding_path(profile),
        build_developer_onboarding_path(profile),
        build_maintainer_onboarding_path(profile)
    ]
    df = pd.DataFrame([onboarding_path_to_dict(p) for p in paths])
    return df, summarize_onboarding_paths(df)

def summarize_onboarding_paths(path_df: pd.DataFrame) -> dict:
    if path_df is None or path_df.empty: return {"total_paths": 0}
    return {"total_paths": len(path_df), "roles": path_df["role_label"].tolist()}
''')

with open("local_training/operator_training_pack.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from .training_config import LocalTrainingProfile

def build_operator_training_sections(project_root: Path, profile: LocalTrainingProfile) -> list[dict]:
    return [
        {"title": "Projenin amacı", "content": "Offline araştırma ve analiz."},
        {"title": "Ne yapar/ne yapmaz?", "content": "Sinyal üretir ama canlı trade yapmaz."},
        {"title": "Güvenli ilk kullanım", "content": "Sadece okuma ve analiz yapın."},
        {"title": "Status komutlarını okuma", "content": "Status komutları raporları gösterir."},
        {"title": "Rapor klasörlerini okuma", "content": "reports/ altındaki verileri inceleyin."},
        {"title": "DataLake outputs", "content": "DataLake lake içindeki verilerdir."},
        {"title": "Final review/quality gates", "content": "Quality checks pass edilmelidir."},
        {"title": "Known gaps/manual review", "content": "Manuel inceleme gerektirir."},
        {"title": "Local DR, archive, maintenance outputs", "content": "Local recovery raporlarıdır."},
        {"title": "Yasaklar", "content": "Canlı emir, deployment, broker kullanımı yasaktır."}
    ]

def build_operator_training_pack(project_root: Path, profile: LocalTrainingProfile) -> tuple[str, dict]:
    sections = build_operator_training_sections(project_root, profile)
    text = "\\n\\n".join([f"### {s['title']}\\n{s['content']}" for s in sections])
    text += "\\n\\n> UYARI: Eğitim pack canlı işlem yetkisi vermez. Safe commands çalıştırılmaz. Yatırım tavsiyesi yok."
    return text, summarize_operator_training_pack(text)

def summarize_operator_training_pack(text: str) -> dict:
    return {"length": len(text), "sections": text.count("### ")}
''')

with open("local_training/analyst_training_pack.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from .training_config import LocalTrainingProfile

def build_analyst_training_sections(project_root: Path, profile: LocalTrainingProfile) -> list[dict]:
    return [
        {"title": "Araştırma raporlarını okuma", "content": "Raporlar analiz için üretilmiştir."},
        {"title": "Synthetic/demo/test verinin sınırları", "content": "Veriler sentetik olabilir."},
        {"title": "Backtest/paper outputlarını yorumlama sınırları", "content": "Geçmiş performans geleceği garanti etmez."},
        {"title": "Evidence ve metadata cards", "content": "Modeller hakkında bilgi verir."},
        {"title": "Scenario/regression reports", "content": "Test raporlarıdır."},
        {"title": "Graph/timeline/consistency outputs", "content": "Bağımlılık ve olay geçmişidir."},
        {"title": "“Yatırım tavsiyesi değildir” çerçevesi", "content": "Hiçbir rapor yatırım tavsiyesi değildir."},
        {"title": "Manual review notları", "content": "Analist incelemesi gerekir."}
    ]

def build_analyst_training_pack(project_root: Path, profile: LocalTrainingProfile) -> tuple[str, dict]:
    sections = build_analyst_training_sections(project_root, profile)
    text = "\\n\\n".join([f"### {s['title']}\\n{s['content']}" for s in sections])
    text += "\\n\\n> UYARI: Analist eğitimi yatırım danışmanlığı değildir. Kesin AL/SAT yorumlama yok. Canlı sinyal yok."
    return text, summarize_analyst_training_pack(text)

def summarize_analyst_training_pack(text: str) -> dict:
    return {"length": len(text), "sections": text.count("### ")}
''')

with open("local_training/developer_training_pack.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from .training_config import LocalTrainingProfile

def build_developer_training_sections(project_root: Path, profile: LocalTrainingProfile) -> list[dict]:
    return [
        {"title": "Repo yapısı", "content": "Ana klasörler ve amaçları."},
        {"title": "Config/settings/paths", "content": "Ayar dosyalarının yönetimi."},
        {"title": "DataLake save/load convention", "content": "Veri okuma yazma kuralları."},
        {"title": "FeatureStore load convention", "content": "ML özellikleri kuralları."},
        {"title": "Scripts contract", "content": "Betiklerin çalışma yapısı."},
        {"title": "Tests contract", "content": "Test standartları."},
        {"title": "Report builder convention", "content": "Rapor oluşturma kuralları."},
        {"title": "Safety boundary pattern", "content": "Güvenlik sınırları ve exceptionlar."},
        {"title": "New phase implementation checklist", "content": "Yeni faz ekleme adımları."},
        {"title": "Common anti-patterns", "content": "Yapılmaması gerekenler."}
    ]

def build_developer_training_pack(project_root: Path, profile: LocalTrainingProfile) -> tuple[str, dict]:
    sections = build_developer_training_sections(project_root, profile)
    text = "\\n\\n".join([f"### {s['title']}\\n{s['content']}" for s in sections])
    text += "\\n\\n> UYARI: Developer pack deployment instruction değildir. Auto-fix veya destructive command yok. External LLM/API kullanımını teşvik etmez."
    return text, summarize_developer_training_pack(text)

def summarize_developer_training_pack(text: str) -> dict:
    return {"length": len(text), "sections": text.count("### ")}
''')

