import os
from pathlib import Path

def patch_paths():
    print("Patching config/paths.py")
    paths_path = Path("config/paths.py")
    with open(paths_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_paths = """
# Local Reuse Paths
LOCAL_REUSE_DIR = DATA_LAKE_DIR / "local_reuse"
LOCAL_REUSE_PROFILES_DIR = LOCAL_REUSE_DIR / "profiles"
LOCAL_REUSE_DOMAINS_DIR = LOCAL_REUSE_DIR / "domains"
LOCAL_REUSE_AUDIT_MEMORY_DIR = LOCAL_REUSE_DIR / "audit_memory"
LOCAL_REUSE_PHASE_CAPSULES_DIR = LOCAL_REUSE_DIR / "phase_capsules"
LOCAL_REUSE_TEMPLATE_CATALOG_DIR = LOCAL_REUSE_DIR / "template_catalog"
LOCAL_REUSE_PROMPT_TEMPLATES_DIR = LOCAL_REUSE_DIR / "prompt_templates"
LOCAL_REUSE_MODULE_BLUEPRINTS_DIR = LOCAL_REUSE_DIR / "module_blueprints"
LOCAL_REUSE_SCRIPT_PATTERNS_DIR = LOCAL_REUSE_DIR / "script_patterns"
LOCAL_REUSE_TEST_PATTERNS_DIR = LOCAL_REUSE_DIR / "test_patterns"
LOCAL_REUSE_DATALAKE_PATTERNS_DIR = LOCAL_REUSE_DIR / "datalake_patterns"
LOCAL_REUSE_REPORT_PATTERNS_DIR = LOCAL_REUSE_DIR / "report_patterns"
LOCAL_REUSE_SAFETY_PATTERNS_DIR = LOCAL_REUSE_DIR / "safety_patterns"
LOCAL_REUSE_DOCUMENTATION_PATTERNS_DIR = LOCAL_REUSE_DIR / "documentation_patterns"
LOCAL_REUSE_KNOWLEDGE_REUSE_KIT_DIR = LOCAL_REUSE_DIR / "knowledge_reuse_kit"
LOCAL_REUSE_PATTERN_EXTRACTION_DIR = LOCAL_REUSE_DIR / "pattern_extraction"
LOCAL_REUSE_V1_1_SEED_DIR = LOCAL_REUSE_DIR / "v1_1_seed"
LOCAL_REUSE_FUTURE_PROJECT_DIR = LOCAL_REUSE_DIR / "future_project"
LOCAL_REUSE_NO_GO_SAFE_GO_DIR = LOCAL_REUSE_DIR / "no_go_safe_go"
LOCAL_REUSE_EXCEPTIONS_DIR = LOCAL_REUSE_DIR / "exceptions"
LOCAL_REUSE_GAPS_DIR = LOCAL_REUSE_DIR / "gaps"
LOCAL_REUSE_RISKS_DIR = LOCAL_REUSE_DIR / "risks"
LOCAL_REUSE_SCORING_DIR = LOCAL_REUSE_DIR / "scoring"
LOCAL_REUSE_VALIDATION_DIR = LOCAL_REUSE_DIR / "validation"
LOCAL_REUSE_QUALITY_DIR = LOCAL_REUSE_DIR / "quality"

LOCAL_REUSE_REPORTS_DIR = REPORTS_OUTPUT_DIR / "local_reuse"
LOCAL_REUSE_REPORTS_CSV_DIR = LOCAL_REUSE_REPORTS_DIR / "csv"
LOCAL_REUSE_REPORTS_MD_DIR = LOCAL_REUSE_REPORTS_DIR / "markdown"
LOCAL_REUSE_REPORTS_TXT_DIR = LOCAL_REUSE_REPORTS_DIR / "txt"
LOCAL_REUSE_REPORTS_JSON_DIR = LOCAL_REUSE_REPORTS_DIR / "json"

LOCAL_REUSE_DOCS_DIR = DOCS_DIR / "generated" / "local_reuse"
"""
    new_dirs_to_ensure = """
    LOCAL_REUSE_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_PROFILES_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_DOMAINS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_AUDIT_MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_PHASE_CAPSULES_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_TEMPLATE_CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_PROMPT_TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_MODULE_BLUEPRINTS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_SCRIPT_PATTERNS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_TEST_PATTERNS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_DATALAKE_PATTERNS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_REPORT_PATTERNS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_SAFETY_PATTERNS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_DOCUMENTATION_PATTERNS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_KNOWLEDGE_REUSE_KIT_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_PATTERN_EXTRACTION_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_V1_1_SEED_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_FUTURE_PROJECT_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_NO_GO_SAFE_GO_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_EXCEPTIONS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_GAPS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_RISKS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_SCORING_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_VALIDATION_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_QUALITY_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_REPORTS_CSV_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_REPORTS_MD_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_REPORTS_TXT_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_REPORTS_JSON_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REUSE_DOCS_DIR.mkdir(parents=True, exist_ok=True)
"""
    if "LOCAL_REUSE_DIR" not in content:
        ensure_idx = content.find("def ensure_project_directories")
        if ensure_idx != -1:
            content = content[:ensure_idx] + new_paths + "\n" + content[ensure_idx:]
            
            # Re-find the index after modification
            ensure_idx = content.find("def ensure_project_directories")
            # find next function or end of file to insert inside ensure_project_directories
            insert_point = content.find("\n\n", ensure_idx)
            if insert_point == -1:
                insert_point = len(content)
            
            content = content[:insert_point] + "\n" + new_dirs_to_ensure + content[insert_point:]
            with open(paths_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully patched paths.py")
        else:
            print("Could not find ensure_project_directories")

if __name__ == "__main__":
    patch_paths()
