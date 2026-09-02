import os
from pathlib import Path

# Paths
base_dir = Path("c:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/commodity_fx_signal_bot")
settings_path = base_dir / "config" / "settings.py"
env_example_path = base_dir / ".env.example"
paths_path = base_dir / "config" / "paths.py"

def update_settings():
    with open(settings_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "local_synthesis_enabled" not in content:
        new_settings = """    # Phase 75 - Local Synthesis Settings
    local_synthesis_enabled: bool = True
    default_local_synthesis_profile: str = "balanced_local_synthesis"
    local_synthesis_default_language: str = "tr"
    local_synthesis_dry_run_default: bool = True
    local_synthesis_allow_investment_advice: bool = False
    local_synthesis_allow_live_trading_claim: bool = False
    local_synthesis_allow_broker_readiness_claim: bool = False
    local_synthesis_allow_production_release_claim: bool = False
    local_synthesis_allow_model_deployment_claim: bool = False
    local_synthesis_allow_official_completion_claim: bool = False
    local_synthesis_allow_official_compliance_claim: bool = False
    local_synthesis_allow_cloud_upload: bool = False
    local_synthesis_allow_external_service: bool = False
    local_synthesis_allow_external_llm: bool = False
    local_synthesis_allow_file_modification: bool = False
    local_synthesis_allow_file_deletion: bool = False
    local_synthesis_allow_file_move: bool = False
    local_synthesis_allow_overwrite: bool = False
    local_synthesis_scan_docs: bool = True
    local_synthesis_scan_reports: bool = True
    local_synthesis_scan_data_lake: bool = True
    local_synthesis_scan_scripts: bool = True
    local_synthesis_scan_tests: bool = True
    local_synthesis_scan_cross_layer_outputs: bool = True
    local_synthesis_scan_safety_outputs: bool = True
    local_synthesis_max_index_items: int = 500000
    local_synthesis_max_sections: int = 10000
    local_synthesis_min_quality_score: float = 0.40
    local_synthesis_save_reports: bool = True

"""
        # Find where to insert
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if "class Settings(BaseSettings):" in line:
                lines.insert(i + 1, new_settings)
                break
        
        with open(settings_path, "w", encoding="utf-8") as f:
            f.write('\n'.join(lines))
    print("settings.py updated.")

def update_env_example():
    with open(env_example_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "LOCAL_SYNTHESIS_ENABLED" not in content:
        new_env = """
# Local Synthesis Settings (Phase 75)
LOCAL_SYNTHESIS_ENABLED=true
DEFAULT_LOCAL_SYNTHESIS_PROFILE=balanced_local_synthesis
LOCAL_SYNTHESIS_DEFAULT_LANGUAGE=tr
LOCAL_SYNTHESIS_DRY_RUN_DEFAULT=true
LOCAL_SYNTHESIS_ALLOW_INVESTMENT_ADVICE=false
LOCAL_SYNTHESIS_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_SYNTHESIS_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_SYNTHESIS_ALLOW_PRODUCTION_RELEASE_CLAIM=false
LOCAL_SYNTHESIS_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_SYNTHESIS_ALLOW_OFFICIAL_COMPLETION_CLAIM=false
LOCAL_SYNTHESIS_ALLOW_OFFICIAL_COMPLIANCE_CLAIM=false
LOCAL_SYNTHESIS_ALLOW_CLOUD_UPLOAD=false
LOCAL_SYNTHESIS_ALLOW_EXTERNAL_SERVICE=false
LOCAL_SYNTHESIS_ALLOW_EXTERNAL_LLM=false
LOCAL_SYNTHESIS_ALLOW_FILE_MODIFICATION=false
LOCAL_SYNTHESIS_ALLOW_FILE_DELETION=false
LOCAL_SYNTHESIS_ALLOW_FILE_MOVE=false
LOCAL_SYNTHESIS_ALLOW_OVERWRITE=false
LOCAL_SYNTHESIS_SCAN_DOCS=true
LOCAL_SYNTHESIS_SCAN_REPORTS=true
LOCAL_SYNTHESIS_SCAN_DATA_LAKE=true
LOCAL_SYNTHESIS_SCAN_SCRIPTS=true
LOCAL_SYNTHESIS_SCAN_TESTS=true
LOCAL_SYNTHESIS_SCAN_CROSS_LAYER_OUTPUTS=true
LOCAL_SYNTHESIS_SCAN_SAFETY_OUTPUTS=true
LOCAL_SYNTHESIS_MAX_INDEX_ITEMS=500000
LOCAL_SYNTHESIS_MAX_SECTIONS=10000
LOCAL_SYNTHESIS_MIN_QUALITY_SCORE=0.40
LOCAL_SYNTHESIS_SAVE_REPORTS=true
"""
        with open(env_example_path, "a", encoding="utf-8") as f:
            f.write(new_env)
    print(".env.example updated.")

def update_paths():
    with open(paths_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "local_synthesis" not in content:
        content = content.replace(
            "        self.dirs = [",
            """        self.dirs = [
            self.data_lake_dir / "local_synthesis",
            self.data_lake_dir / "local_synthesis" / "profiles",
            self.data_lake_dir / "local_synthesis" / "phase_families",
            self.data_lake_dir / "local_synthesis" / "master_indexes",
            self.data_lake_dir / "local_synthesis" / "final_maps",
            self.data_lake_dir / "local_synthesis" / "capabilities",
            self.data_lake_dir / "local_synthesis" / "boundaries",
            self.data_lake_dir / "local_synthesis" / "dependencies",
            self.data_lake_dir / "local_synthesis" / "catalogs",
            self.data_lake_dir / "local_synthesis" / "dossiers",
            self.data_lake_dir / "local_synthesis" / "binders",
            self.data_lake_dir / "local_synthesis" / "statements",
            self.data_lake_dir / "local_synthesis" / "limitations",
            self.data_lake_dir / "local_synthesis" / "manual_review",
            self.data_lake_dir / "local_synthesis" / "no_go_safe_go",
            self.data_lake_dir / "local_synthesis" / "navigation",
            self.data_lake_dir / "local_synthesis" / "checklists",
            self.data_lake_dir / "local_synthesis" / "validation",
            self.data_lake_dir / "local_synthesis" / "quality",
            self.reports_output_dir / "local_synthesis",
            self.reports_output_dir / "local_synthesis" / "csv",
            self.reports_output_dir / "local_synthesis" / "markdown",
            self.reports_output_dir / "local_synthesis" / "txt",
            self.reports_output_dir / "local_synthesis" / "json",
            self.docs_generated_dir / "local_synthesis","""
        )
        with open(paths_path, "w", encoding="utf-8") as f:
            f.write(content)
    print("paths.py updated.")

if __name__ == "__main__":
    update_settings()
    update_env_example()
    update_paths()
    print("Config files updated.")
