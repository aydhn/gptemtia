import pandas as pd
from pathlib import Path
from .runtime_config import AdvancedRuntimeProfile, get_default_advanced_runtime_profile

class AdvancedRuntimePipeline:
    def __init__(self, data_lake, settings, project_root: Path, profile: AdvancedRuntimeProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_advanced_runtime_profile()
        
    def build_runtime_profile_registry(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        from .runtime_profile_registry import build_advanced_runtime_profile_registry
        df, sum_d = build_advanced_runtime_profile_registry(self.profile)
        if save:
            try: self.data_lake.save_advanced_runtime_profile_registry(df, sum_d)
            except: pass
        return df, sum_d

    def build_unified_runtime_context(self, save: bool = True) -> tuple[str, dict]:
        from .runtime_context import build_unified_runtime_context
        txt, sum_d = build_unified_runtime_context(self.project_root, self.profile)
        if save:
            try: self.data_lake.save_unified_runtime_context(txt, sum_d)
            except: pass
        return txt, sum_d

    def build_runtime_capabilities(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        from .runtime_capabilities import build_runtime_capability_registry
        df, sum_d = build_runtime_capability_registry(self.profile)
        if save:
            try: self.data_lake.save_runtime_capability_registry(df, sum_d)
            except: pass
        return df, sum_d

    def build_runtime_contracts(self, save: bool = True) -> tuple[dict, dict]:
        from .runtime_execution_contract import build_runtime_execution_contract
        from .runtime_command_contract import build_runtime_dry_run_command_contract
        from .runtime_output_contract import build_runtime_output_contract
        from .runtime_datalake_contract import build_runtime_datalake_contract
        from .runtime_featurestore_contract import build_runtime_featurestore_contract
        from .runtime_report_contract import build_runtime_report_contract
        from .runtime_safety_boundary import build_runtime_safety_boundary
        
        df1, _ = build_runtime_execution_contract(self.profile)
        df2, _ = build_runtime_dry_run_command_contract(self.profile)
        df3, _ = build_runtime_output_contract(self.profile)
        df4, _ = build_runtime_datalake_contract(self.profile)
        df5, _ = build_runtime_featurestore_contract(self.profile)
        df6, _ = build_runtime_report_contract(self.profile)
        df7, _ = build_runtime_safety_boundary(self.profile)
        
        d = {"exec": df1, "cmd": df2, "out": df3, "dl": df4, "fs": df5, "rep": df6, "safe": df7}
        return d, {"status": "ok"}

    def build_runtime_health_check(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        from .runtime_health import build_runtime_health_check
        df, sum_d = build_runtime_health_check(self.project_root, self.profile)
        if save:
            try: self.data_lake.save_runtime_health_check(df, sum_d)
            except: pass
        return df, sum_d

    def build_runtime_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        from .runtime_quality import build_runtime_quality_report
        rep = build_runtime_quality_report({}, None, None)
        if save:
            try: self.data_lake.save_runtime_quality_report(self.profile.name, rep)
            except: pass
        return rep, {"status": "ok"}

    def build_runtime_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "ok"}])
        return df, {"status": "ok"}
