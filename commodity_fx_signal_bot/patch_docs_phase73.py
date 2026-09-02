import os

readme_add = '''
## Local Knowledge Transfer and Operator Onboarding

- Local training layer resmi sertifika değildir.
- Onboarding paths canlı işlem yetkisi vermez.
- Guided walkthrough komut çalıştırmaz; read-only/manual öğrenme adımları sağlar.
- Safe command lessons canlı/broker/deploy/destructive komut içermez.
- Analyst training pack yatırım tavsiyesi öğretmez.
- Handover binder local/offline proje devri içindir.
- Çıktılar data/lake/local_training ve reports/output/local_training altında oluşur.

Komutlar:
python -m scripts.run_training_domain_registry
python -m scripts.run_onboarding_curriculum
python -m scripts.run_guided_walkthroughs
python -m scripts.run_training_packs
python -m scripts.run_handover_education_binder
python -m scripts.run_training_quality_report
python -m scripts.run_training_status
'''
with open("README.md", "a", encoding="utf-8") as f: f.write(readme_add)

architecture_add = '''
## Phase 73: Local Training Layer
Docs / Reports / Scripts / Tests / DataLake / Safety Docs / Evidence / Metadata / Graph / Timeline / Consistency / Readiness / Maintenance / Archive / DR
-> TrainingDomainRegistry
-> RoleBasedOnboardingPaths
-> OperatorTrainingPack
-> AnalystTrainingPack
-> DeveloperTrainingPack
-> SafeUsageTraining
-> NonUsePolicyTraining
-> GuidedWalkthroughRegistry
-> LocalWalkthroughLessons
-> CommandLessons
-> ReportLessons
-> DataLakeLessons
-> CrossLayerLessons
-> TroubleshootingLessons
-> Glossary
-> ConceptMap
-> FAQ
-> FirstWeekCurriculum
-> KnowledgeTransferChecklist
-> HandoverEducationBinder
-> TrainingAssessment
-> TrainingGaps
-> TrainingRisks
-> TrainingValidation
-> TrainingQuality
-> Local Training Outputs
'''
with open("docs/ARCHITECTURE.md", "a", encoding="utf-8") as f: f.write(architecture_add)

phase_log_add = '''
## Phase 73
- Local training profile sistemi eklendi.
- Training label registry eklendi.
- TrainingDomain, OnboardingPath, TrainingLesson, TrainingFAQ ve TrainingFinding modelleri eklendi.
- Training domain registry eklendi.
- Role-based onboarding paths eklendi.
- Operator/analyst/developer training pack eklendi.
- Safe usage ve non-use policy training pack eklendi.
- Guided walkthrough registry eklendi.
- Local walkthrough lessons eklendi.
- Safe command lesson registry eklendi.
- Report/DataLake/cross-layer lesson registries eklendi.
- Troubleshooting lesson registry eklendi.
- Glossary ve concept map eklendi.
- FAQ registry eklendi.
- First-week operator curriculum eklendi.
- Knowledge-transfer checklist eklendi.
- Training assessment dry-run eklendi.
- Handover education binder eklendi.
- Training gap register ve risk summary eklendi.
- Training validation ve quality report eklendi.
- LocalTrainingPipeline eklendi.
- DataLake local training kayıt desteği aldı.
- Local training scriptleri eklendi.
- Testler genişletildi.
'''
with open("docs/PHASE_LOG.md", "a", encoding="utf-8") as f: f.write(phase_log_add)

common_docs_add = '''
## Local Training and Onboarding

- **Onboarding Paths:** Hangi rolün hangi konularda eğitim alacağını belirtir.
- **Training Packs:** Operatör, analist ve developer için detaylı kılavuzlar.
- **Guided Walkthrough:** Adım adım çevrimdışı rehberler, read-only/manual öğrenme adımları sağlar.
- **Safe Command Lessons:** Sadece okuma veya dry-run komutlarını öğretir, canlı/broker/deploy/destructive komut içermez.
- **Non-use Policy Training:** Yapılmaması gereken eylemleri net bir şekilde sınırlar.
- **Handover Binder:** Proje devri için tüm gerekli belgeleri ve checklistleri içerir.
- **Training Assessment:** Dry-run olarak bilginizi sınar, resmi bir sertifika değildir.

> **UYARI**: Bu modül canlı emir, broker execution, deployment, yatırım tavsiyesi, cloud upload veya resmi sertifika onaylarını İÇERMEZ. Sistem offline knowledge-transfer aracıdır.
'''

for doc in ["OPERATOR_MANUAL.md", "ANALYST_HANDBOOK.md", "CODEX_AGENT_GUIDE.md", "SAFE_USAGE_GUIDE.md", "INSTALLATION.md", "CONFIGURATION.md"]:
    p = os.path.join("docs", doc)
    if os.path.exists(p):
        with open(p, "a", encoding="utf-8") as f: f.write(common_docs_add)
    else:
        with open(p, "w", encoding="utf-8") as f: f.write(common_docs_add)

