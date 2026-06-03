from portable_packaging.environment_snapshot import (
    collect_python_runtime_info,
    collect_platform_info,
    collect_memory_info,
    collect_installed_packages_snapshot
)
import pandas as pd

def test_environment_collections():
    assert isinstance(collect_python_runtime_info(), dict)
    assert isinstance(collect_platform_info(), dict)
    assert isinstance(collect_memory_info(), dict)

    df = collect_installed_packages_snapshot()
    assert isinstance(df, pd.DataFrame)
