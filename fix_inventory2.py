with open("commodity_fx_signal_bot/portable_packaging/dependency_inventory.py", "r") as f:
    inv = f.read()

import re
inv = inv.replace('return pd.DataFrame(columns=["package_name", "required_version", "source", "requirement_detected", "optional"])',
                  'return pd.DataFrame(columns=["package_name", "required_version", "source", "requirement_detected", "optional"]).astype(str)')
inv = inv.replace('imports_df = collect_imported_packages(project_root)',
                  'imports_df = collect_imported_packages(project_root)\n    if imports_df.empty:\n        imports_df = pd.DataFrame(columns=["package_name", "import_detected", "source"]).astype(str)')

with open("commodity_fx_signal_bot/portable_packaging/dependency_inventory.py", "w") as f:
    f.write(inv)
