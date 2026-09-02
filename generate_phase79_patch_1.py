import os
from pathlib import Path
import re

base_dir = Path(r"c:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\commodity_fx_signal_bot")

# 1. Patch config/settings.py
settings_path = base_dir / "config" / "settings.py"
with open(settings_path, 'r', encoding='utf-8') as f:
    content = f.read()

archival_settings = """
    # Local Archival Settings
    local_archival_enabled: bool = True
    default_local_archival_profile: str = "balanced_local_archival"
    local_archival_default_language: str = "tr"
    local_archival_dry_run_default: bool = True
    local_archival_hash_algorithm: str = "sha256"
    local_archival_allow_real_immutable_lock: bool = False
    local_archival_allow_chmod_lock: bool = False
    local_archival_allow_file_permission_change: bool = False
    local_archival_allow_legal_hold_claim: bool = False
    local_archival_allow_compliance_claim: bool = False
    local_archival_allow_blockchain_notarization: bool = False
    local_archival_allow_timestamp_authority: bool = False
    local_archival_allow_cloud_archive: bool = False
    local_archival_allow_cloud_upload: bool = False
    local_archival_allow_package_publish: bool = False
    local_archival_allow_external_service: bool = False
    local_archival_allow_external_llm: bool = False
    local_archival_allow_file_modification: bool = False
    local_archival_allow_file_deletion: bool = False
    local_archival_allow_file_move: bool = False
    local_archival_allow_overwrite: bool = False
    local_archival_allow_live_trading_claim: bool = False
    local_archival_allow_broker_readiness_claim: bool = False
    local_archival_allow_investment_advice: bool = False
    local_archival_allow_model_deployment_claim: bool = False
    local_archival_scan_docs: bool = True
    local_archival_scan_reports: bool = True
    local_archival_scan_data_lake: bool = True
    local_archival_scan_scripts: bool = True
    local_archival_scan_tests: bool = True
    local_archival_scan_generated_docs: bool = True
    local_archival_scan_delivery_outputs: bool = True
    local_archival_scan_acceptance_outputs: bool = True
    local_archival_scan_safety_outputs: bool = True
    local_archival_max_hash_items: int = 500000
    local_archival_max_file_size_mb_for_hash: int = 250
    local_archival_min_readiness_score: float = 0.40
    local_archival_min_quality_score: float = 0.40
    local_archival_save_reports: bool = True
"""
if "local_archival_enabled" not in content:
    content = content.replace("class Settings(BaseSettings):", f"class Settings(BaseSettings):\\n{archival_settings}")
    with open(settings_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Patch .env.example
env_path = base_dir / ".env.example"
with open(env_path, 'a', encoding='utf-8') as f:
    f.write('''
# Local Archival Settings
LOCAL_ARCHIVAL_ENABLED=true
DEFAULT_LOCAL_ARCHIVAL_PROFILE=balanced_local_archival
LOCAL_ARCHIVAL_DEFAULT_LANGUAGE=tr
LOCAL_ARCHIVAL_DRY_RUN_DEFAULT=true
LOCAL_ARCHIVAL_HASH_ALGORITHM=sha256
LOCAL_ARCHIVAL_ALLOW_REAL_IMMUTABLE_LOCK=false
LOCAL_ARCHIVAL_ALLOW_CHMOD_LOCK=false
LOCAL_ARCHIVAL_ALLOW_FILE_PERMISSION_CHANGE=false
LOCAL_ARCHIVAL_ALLOW_LEGAL_HOLD_CLAIM=false
LOCAL_ARCHIVAL_ALLOW_COMPLIANCE_CLAIM=false
LOCAL_ARCHIVAL_ALLOW_BLOCKCHAIN_NOTARIZATION=false
LOCAL_ARCHIVAL_ALLOW_TIMESTAMP_AUTHORITY=false
LOCAL_ARCHIVAL_ALLOW_CLOUD_ARCHIVE=false
LOCAL_ARCHIVAL_ALLOW_CLOUD_UPLOAD=false
LOCAL_ARCHIVAL_ALLOW_PACKAGE_PUBLISH=false
LOCAL_ARCHIVAL_ALLOW_EXTERNAL_SERVICE=false
LOCAL_ARCHIVAL_ALLOW_EXTERNAL_LLM=false
LOCAL_ARCHIVAL_ALLOW_FILE_MODIFICATION=false
LOCAL_ARCHIVAL_ALLOW_FILE_DELETION=false
LOCAL_ARCHIVAL_ALLOW_FILE_MOVE=false
LOCAL_ARCHIVAL_ALLOW_OVERWRITE=false
LOCAL_ARCHIVAL_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_ARCHIVAL_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_ARCHIVAL_ALLOW_INVESTMENT_ADVICE=false
LOCAL_ARCHIVAL_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_ARCHIVAL_SCAN_DOCS=true
LOCAL_ARCHIVAL_SCAN_REPORTS=true
LOCAL_ARCHIVAL_SCAN_DATA_LAKE=true
LOCAL_ARCHIVAL_SCAN_SCRIPTS=true
LOCAL_ARCHIVAL_SCAN_TESTS=true
LOCAL_ARCHIVAL_SCAN_GENERATED_DOCS=true
LOCAL_ARCHIVAL_SCAN_DELIVERY_OUTPUTS=true
LOCAL_ARCHIVAL_SCAN_ACCEPTANCE_OUTPUTS=true
LOCAL_ARCHIVAL_SCAN_SAFETY_OUTPUTS=true
LOCAL_ARCHIVAL_MAX_HASH_ITEMS=500000
LOCAL_ARCHIVAL_MAX_FILE_SIZE_MB_FOR_HASH=250
LOCAL_ARCHIVAL_MIN_READINESS_SCORE=0.40
LOCAL_ARCHIVAL_MIN_QUALITY_SCORE=0.40
LOCAL_ARCHIVAL_SAVE_REPORTS=true
''')

# 3. Patch config/paths.py
paths_path = base_dir / "config" / "paths.py"
with open(paths_path, 'r', encoding='utf-8') as f:
    content = f.read()

paths_archival = """
    "lake_local_archival": DATA_LAKE_DIR / "local_archival",
    "lake_local_archival_profiles": DATA_LAKE_DIR / "local_archival" / "profiles",
    "lake_local_archival_domains": DATA_LAKE_DIR / "local_archival" / "domains",
    "lake_local_archival_seal_manifest": DATA_LAKE_DIR / "local_archival" / "seal_manifest",
    "lake_local_archival_immutable_manifest": DATA_LAKE_DIR / "local_archival" / "immutable_manifest",
    "lake_local_archival_provenance_lockfile": DATA_LAKE_DIR / "local_archival" / "provenance_lockfile",
    "lake_local_archival_hash_catalogs": DATA_LAKE_DIR / "local_archival" / "hash_catalogs",
    "lake_local_archival_hash_of_hashes": DATA_LAKE_DIR / "local_archival" / "hash_of_hashes",
    "lake_local_archival_policies": DATA_LAKE_DIR / "local_archival" / "policies",
    "lake_local_archival_exclusions": DATA_LAKE_DIR / "local_archival" / "exclusions",
    "lake_local_archival_archive_inventory": DATA_LAKE_DIR / "local_archival" / "archive_inventory",
    "lake_local_archival_hash_rehearsals": DATA_LAKE_DIR / "local_archival" / "hash_rehearsals",
    "lake_local_archival_custody": DATA_LAKE_DIR / "local_archival" / "custody",
    "lake_local_archival_retention": DATA_LAKE_DIR / "local_archival" / "retention",
    "lake_local_archival_tamper_evidence": DATA_LAKE_DIR / "local_archival" / "tamper_evidence",
    "lake_local_archival_reproducibility": DATA_LAKE_DIR / "local_archival" / "reproducibility",
    "lake_local_archival_provenance_traces": DATA_LAKE_DIR / "local_archival" / "provenance_traces",
    "lake_local_archival_no_go_safe_go": DATA_LAKE_DIR / "local_archival" / "no_go_safe_go",
    "lake_local_archival_exceptions": DATA_LAKE_DIR / "local_archival" / "exceptions",
    "lake_local_archival_gaps": DATA_LAKE_DIR / "local_archival" / "gaps",
    "lake_local_archival_risks": DATA_LAKE_DIR / "local_archival" / "risks",
    "lake_local_archival_scoring": DATA_LAKE_DIR / "local_archival" / "scoring",
    "lake_local_archival_validation": DATA_LAKE_DIR / "local_archival" / "validation",
    "lake_local_archival_quality": DATA_LAKE_DIR / "local_archival" / "quality",
    "reports_local_archival": REPORTS_OUTPUT_DIR / "local_archival",
    "reports_local_archival_csv": REPORTS_OUTPUT_DIR / "local_archival" / "csv",
    "reports_local_archival_markdown": REPORTS_OUTPUT_DIR / "local_archival" / "markdown",
    "reports_local_archival_txt": REPORTS_OUTPUT_DIR / "local_archival" / "txt",
    "reports_local_archival_json": REPORTS_OUTPUT_DIR / "local_archival" / "json",
    "docs_generated_local_archival": DOCS_GENERATED_DIR / "local_archival",
"""
if "lake_local_archival" not in content:
    content = content.replace("PROJECT_DIRS = {", f"PROJECT_DIRS = {{\\n{paths_archival}")
    with open(paths_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("generate_phase79_patch_1.py created.")
