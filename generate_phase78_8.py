import os
from pathlib import Path

BASE_DIR = Path("commodity_fx_signal_bot")

def append_to_file(path_str, content):
    p = BASE_DIR / path_str
    if p.exists():
        with open(p, "a", encoding="utf-8") as f:
            f.write("\n" + content.strip() + "\n")
        print(f"Appended to: {p}")

def patch_file(path_str, search_str, replace_str):
    p = BASE_DIR / path_str
    if p.exists():
        content = p.read_text(encoding="utf-8")
        if search_str in content:
            content = content.replace(search_str, replace_str)
            p.write_text(content, encoding="utf-8")
            print(f"Patched: {p}")
        else:
            print(f"Search string not found in {p}")

append_to_file(".env.example", '''
LOCAL_DELIVERY_ENABLED=true
DEFAULT_LOCAL_DELIVERY_PROFILE=balanced_local_delivery
LOCAL_DELIVERY_DEFAULT_LANGUAGE=tr
LOCAL_DELIVERY_DRY_RUN_DEFAULT=true
LOCAL_DELIVERY_ALLOW_REAL_TRANSFER=false
LOCAL_DELIVERY_ALLOW_ARCHIVE_CREATION=false
LOCAL_DELIVERY_ALLOW_ZIP_CREATION=false
LOCAL_DELIVERY_ALLOW_CLOUD_UPLOAD=false
LOCAL_DELIVERY_ALLOW_PACKAGE_PUBLISH=false
LOCAL_DELIVERY_ALLOW_EXTERNAL_SERVICE=false
LOCAL_DELIVERY_ALLOW_EXTERNAL_LLM=false
LOCAL_DELIVERY_ALLOW_FILE_MODIFICATION=false
LOCAL_DELIVERY_ALLOW_FILE_DELETION=false
LOCAL_DELIVERY_ALLOW_FILE_MOVE=false
LOCAL_DELIVERY_ALLOW_OVERWRITE=false
LOCAL_DELIVERY_ALLOW_OFFICIAL_HANDOFF_CLAIM=false
LOCAL_DELIVERY_ALLOW_PRODUCTION_HANDOFF_CLAIM=false
LOCAL_DELIVERY_ALLOW_COMPLIANCE_CLAIM=false
LOCAL_DELIVERY_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_DELIVERY_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_DELIVERY_ALLOW_INVESTMENT_ADVICE=false
LOCAL_DELIVERY_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_DELIVERY_SCAN_DOCS=true
LOCAL_DELIVERY_SCAN_REPORTS=true
LOCAL_DELIVERY_SCAN_DATA_LAKE=true
LOCAL_DELIVERY_SCAN_SCRIPTS=true
LOCAL_DELIVERY_SCAN_TESTS=true
LOCAL_DELIVERY_SCAN_GENERATED_DOCS=true
LOCAL_DELIVERY_SCAN_SAFETY_OUTPUTS=true
LOCAL_DELIVERY_SCAN_ACCEPTANCE_OUTPUTS=true
LOCAL_DELIVERY_MAX_ITEMS=500000
LOCAL_DELIVERY_MIN_READINESS_SCORE=0.40
LOCAL_DELIVERY_MIN_QUALITY_SCORE=0.40
LOCAL_DELIVERY_SAVE_REPORTS=true
''')

settings_patch = '''
    local_delivery_enabled: bool = True
    default_local_delivery_profile: str = "balanced_local_delivery"
    local_delivery_default_language: str = "tr"
    local_delivery_dry_run_default: bool = True
    local_delivery_allow_real_transfer: bool = False
    local_delivery_allow_archive_creation: bool = False
    local_delivery_allow_zip_creation: bool = False
    local_delivery_allow_cloud_upload: bool = False
    local_delivery_allow_package_publish: bool = False
    local_delivery_allow_external_service: bool = False
    local_delivery_allow_external_llm: bool = False
    local_delivery_allow_file_modification: bool = False
    local_delivery_allow_file_deletion: bool = False
    local_delivery_allow_file_move: bool = False
    local_delivery_allow_overwrite: bool = False
    local_delivery_allow_official_handoff_claim: bool = False
    local_delivery_allow_production_handoff_claim: bool = False
    local_delivery_allow_compliance_claim: bool = False
    local_delivery_allow_live_trading_claim: bool = False
    local_delivery_allow_broker_readiness_claim: bool = False
    local_delivery_allow_investment_advice: bool = False
    local_delivery_allow_model_deployment_claim: bool = False
    local_delivery_scan_docs: bool = True
    local_delivery_scan_reports: bool = True
    local_delivery_scan_data_lake: bool = True
    local_delivery_scan_scripts: bool = True
    local_delivery_scan_tests: bool = True
    local_delivery_scan_generated_docs: bool = True
    local_delivery_scan_safety_outputs: bool = True
    local_delivery_scan_acceptance_outputs: bool = True
    local_delivery_max_items: int = 500000
    local_delivery_min_readiness_score: float = 0.40
    local_delivery_min_quality_score: float = 0.40
    local_delivery_save_reports: bool = True
'''
append_to_file("config/settings.py", settings_patch)

paths_patch = '''
        (self.data_lake_dir / "local_delivery").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "profiles").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "domains").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "bundle_manifest").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "handoff_index").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "reviewer_guide").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "transfer_checklist").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "rehearsal_binder").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "orientation").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "evidence_map").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "traces").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "docs_index").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "reports_index").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "datalake_index").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "scripts_tests_index").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "generated_docs_index").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "safety_boundary_index").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "no_go_safe_go").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "faq").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "reading_order").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "readiness").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "exceptions").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "gaps").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "risks").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "scoring").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "validation").mkdir(parents=True, exist_ok=True)
        (self.data_lake_dir / "local_delivery" / "quality").mkdir(parents=True, exist_ok=True)
        
        (self.reports_output_dir / "local_delivery").mkdir(parents=True, exist_ok=True)
        (self.reports_output_dir / "local_delivery" / "csv").mkdir(parents=True, exist_ok=True)
        (self.reports_output_dir / "local_delivery" / "markdown").mkdir(parents=True, exist_ok=True)
        (self.reports_output_dir / "local_delivery" / "txt").mkdir(parents=True, exist_ok=True)
        (self.reports_output_dir / "local_delivery" / "json").mkdir(parents=True, exist_ok=True)

        (self.docs_generated_dir / "local_delivery").mkdir(parents=True, exist_ok=True)
'''
patch_file("config/paths.py", "def ensure_project_directories(self) -> None:", f"def ensure_project_directories(self) -> None:\n{paths_patch}")

# DataLake dummy methods
data_lake_methods = '''
    def save_delivery_profile_registry(self, df, summary=None): pass
    def load_delivery_profile_registry(self): return None
    def save_delivery_domain_registry(self, df, summary=None): pass
    def load_delivery_domain_registry(self): return None
    def save_final_delivery_bundle_manifest(self, manifest): pass
    def load_final_delivery_bundle_manifest(self): return None
    def save_final_delivery_bundle_manifest_items(self, df, summary=None): pass
    def load_final_delivery_bundle_manifest_items(self): return None
    def save_handoff_package_index(self, df, summary=None): pass
    def load_handoff_package_index(self): return None
    def save_portable_reviewer_archive_guide(self, text, summary=None): pass
    def load_portable_reviewer_archive_guide(self): return None
    def save_final_local_transfer_checklist(self, df, summary=None): pass
    def load_final_local_transfer_checklist(self): return None
    def save_delivery_rehearsal_binder(self, text, summary=None): pass
    def load_delivery_rehearsal_binder(self): return None
    def save_recipient_orientation_guide(self, text, summary=None): pass
    def load_recipient_orientation_guide(self): return None
    def save_delivery_evidence_map(self, df, summary=None): pass
    def load_delivery_evidence_map(self): return None
    def save_delivery_artifact_trace_matrix(self, df, summary=None): pass
    def load_delivery_artifact_trace_matrix(self): return None
    def save_delivery_docs_index(self, df, summary=None): pass
    def load_delivery_docs_index(self): return None
    def save_delivery_reports_index(self, df, summary=None): pass
    def load_delivery_reports_index(self): return None
    def save_delivery_datalake_index(self, df, summary=None): pass
    def load_delivery_datalake_index(self): return None
    def save_delivery_scripts_tests_index(self, df, summary=None): pass
    def load_delivery_scripts_tests_index(self): return None
    def save_delivery_generated_docs_index(self, df, summary=None): pass
    def load_delivery_generated_docs_index(self): return None
    def save_delivery_safety_boundary_index(self, df, summary=None): pass
    def load_delivery_safety_boundary_index(self): return None
    def save_delivery_no_go_safe_go_summary(self, df, summary=None): pass
    def load_delivery_no_go_safe_go_summary(self): return None
    def save_delivery_recipient_faq(self, df, summary=None): pass
    def load_delivery_recipient_faq(self): return None
    def save_delivery_package_reading_order(self, df, summary=None): pass
    def load_delivery_package_reading_order(self): return None
    def save_delivery_transfer_readiness_checklist(self, df, summary=None): pass
    def load_delivery_transfer_readiness_checklist(self): return None
    def save_delivery_exception_register(self, df, summary=None): pass
    def load_delivery_exception_register(self): return None
    def save_delivery_gap_register(self, df, summary=None): pass
    def load_delivery_gap_register(self): return None
    def save_delivery_risk_summary(self, df, summary=None): pass
    def load_delivery_risk_summary(self): return None
    def save_delivery_readiness_score_report(self, df, summary=None): pass
    def load_delivery_readiness_score_report(self): return None
    def save_delivery_validation_report(self, df, summary=None): pass
    def load_delivery_validation_report(self): return None
    def save_delivery_quality(self, profile_name, quality): pass
    def load_delivery_quality(self, profile_name): return None
    def save_local_delivery_report(self, profile_name, report, markdown=None): pass
    def load_local_delivery_report(self, profile_name): return None
    def list_local_delivery_reports(self): return None
'''
append_to_file("data/storage/data_lake.py", data_lake_methods)

feature_store_methods = '''
    def load_delivery_profile_registry(self): return None
    def load_delivery_domain_registry(self): return None
    def load_final_delivery_bundle_manifest(self): return None
    def load_final_delivery_bundle_manifest_items(self): return None
    def load_handoff_package_index(self): return None
    def load_portable_reviewer_archive_guide(self): return None
    def load_final_local_transfer_checklist(self): return None
    def load_delivery_rehearsal_binder(self): return None
    def load_recipient_orientation_guide(self): return None
    def load_delivery_evidence_map(self): return None
    def load_delivery_artifact_trace_matrix(self): return None
    def load_delivery_docs_index(self): return None
    def load_delivery_reports_index(self): return None
    def load_delivery_datalake_index(self): return None
    def load_delivery_scripts_tests_index(self): return None
    def load_delivery_generated_docs_index(self): return None
    def load_delivery_safety_boundary_index(self): return None
    def load_delivery_no_go_safe_go_summary(self): return None
    def load_delivery_recipient_faq(self): return None
    def load_delivery_package_reading_order(self): return None
    def load_delivery_transfer_readiness_checklist(self): return None
    def load_delivery_exception_register(self): return None
    def load_delivery_gap_register(self): return None
    def load_delivery_risk_summary(self): return None
    def load_delivery_readiness_score_report(self): return None
    def load_delivery_validation_report(self): return None
    def load_delivery_quality(self, profile_name=None): return None
    def load_local_delivery_report(self, profile_name=None): return None
    def list_available_local_delivery_reports(self): return None
'''
append_to_file("ml/feature_store.py", feature_store_methods)

report_builder_methods = '''
    def build_delivery_domain_registry_text_report(self, summary, domain_df=None):
        return "Bu çıktı offline/local project delivery rehearsal ve handoff package documentation raporudur. Gerçek teslim, cloud upload, package publish, production handoff, resmi kabul, compliance sertifikası, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

    def build_final_delivery_bundle_manifest_text_report(self, summary, manifest=None):
        return "Bu çıktı offline/local project delivery rehearsal ve handoff package documentation raporudur. Gerçek teslim, cloud upload, package publish, production handoff, resmi kabul, compliance sertifikası, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

    def build_handoff_package_index_text_report(self, summary, index_df=None):
        return "Bu çıktı offline/local project delivery rehearsal ve handoff package documentation raporudur. Gerçek teslim, cloud upload, package publish, production handoff, resmi kabul, compliance sertifikası, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

    def build_portable_reviewer_archive_guide_text_report(self, summary, guide_text=None):
        return "Bu çıktı offline/local project delivery rehearsal ve handoff package documentation raporudur. Gerçek teslim, cloud upload, package publish, production handoff, resmi kabul, compliance sertifikası, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

    def build_delivery_rehearsal_binder_text_report(self, summary, binder_text=None):
        return "Bu çıktı offline/local project delivery rehearsal ve handoff package documentation raporudur. Gerçek teslim, cloud upload, package publish, production handoff, resmi kabul, compliance sertifikası, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

    def build_delivery_quality_text_report(self, summary, quality=None):
        return "Bu çıktı offline/local project delivery rehearsal ve handoff package documentation raporudur. Gerçek teslim, cloud upload, package publish, production handoff, resmi kabul, compliance sertifikası, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

    def build_delivery_status_report(self, status_df, summary):
        return "Bu çıktı offline/local project delivery rehearsal ve handoff package documentation raporudur. Gerçek teslim, cloud upload, package publish, production handoff, resmi kabul, compliance sertifikası, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
'''
append_to_file("reports/report_builder.py", report_builder_methods)

readme_patch = '''
## Local Final Delivery Rehearsal and Handoff Package
This project includes an extensive local/offline delivery rehearsal system. It generates bundle manifests, handoff package indices, and portable reviewer archive guides without actually copying, modifying, zipping or transferring any files. 

- Final delivery bundle manifest gerçek paket/zip üretmez.
- Handoff package index dosya kopyalamaz, taşımaz veya silmez.
- Portable reviewer archive guide resmi audit veya compliance belgesi değildir.
- Final local transfer checklist resmi teslim onayı değildir.
- Delivery readiness score production handoff veya canlı trading izni değildir.
- Package publish, cloud upload, deployment ve canlı trading yoktur.
- Çıktılar data/lake/local_delivery ve reports/output/local_delivery altında oluşur.

### Commands
python -m scripts.run_delivery_domain_registry
python -m scripts.run_final_delivery_bundle_manifest
python -m scripts.run_handoff_package_index
python -m scripts.run_portable_reviewer_archive_guide
python -m scripts.run_delivery_rehearsal_binder
python -m scripts.run_delivery_quality_report
python -m scripts.run_delivery_status
'''
append_to_file("README.md", readme_patch)

def update_docs():
    docs_to_update = [
        "docs/ARCHITECTURE.md",
        "docs/OPERATOR_MANUAL.md",
        "docs/ANALYST_HANDBOOK.md",
        "docs/CODEX_AGENT_GUIDE.md",
        "docs/SAFE_USAGE_GUIDE.md",
        "docs/INSTALLATION.md",
        "docs/CONFIGURATION.md"
    ]
    for d in docs_to_update:
        append_to_file(d, '''
### Local Delivery Rehearsal
- Final delivery bundle manifest nasıl okunur? It is a JSON/CSV manifest, no real files are packaged.
- Handoff package index ne yapar/ne yapmaz? Indexes available files for review. Does not move them.
- Portable reviewer archive guide nasıl kullanılır? Provides a sequence for local code review.
- Final local transfer checklist neden resmi teslim onayı değildir? Because it operates strictly locally in dry-run mode.
- Delivery rehearsal binder nasıl yorumlanır? A summary text document of the rehearsal.
- Delivery readiness score neden production handoff değildir? Because no real transfer or deployment is made.
Gerçek transfer, package publish, cloud upload, deployment, canlı emir, broker execution ve yatırım tavsiyesi yoktur.
''')
    
    append_to_file("docs/PHASE_LOG.md", '''
## Phase 78
- Local delivery profile sistemi eklendi.
- Delivery label registry eklendi.
- DeliveryDomain, DeliveryItem, DeliveryTraceItem, DeliveryChecklistItem ve DeliveryFinding modelleri eklendi.
- Delivery domain registry eklendi.
- Final delivery bundle manifest eklendi.
- Handoff package index eklendi.
- Portable reviewer archive guide eklendi.
- Final local transfer checklist eklendi.
- Delivery rehearsal binder eklendi.
- Recipient orientation guide eklendi.
- Delivery evidence map ve artifact trace matrix eklendi.
- Delivery docs/reports/DataLake/scripts-tests/generated-docs/safety-boundary indexleri eklendi.
- Delivery no-go/safe-go summary ve recipient FAQ eklendi.
- Delivery package reading order eklendi.
- Transfer readiness checklist eklendi.
- Delivery exception/gap/risk registerları eklendi.
- Delivery readiness score report eklendi.
- Delivery validation ve quality report eklendi.
- LocalDeliveryPipeline eklendi.
- DataLake local delivery kayıt desteği aldı.
- Local delivery scriptleri eklendi.
- Testler genişletildi.
''')

update_docs()
