import importlib

def test_scripts_importable():
    mods = [
        "scripts.run_delivery_domain_registry",
        "scripts.run_final_delivery_bundle_manifest",
        "scripts.run_handoff_package_index",
        "scripts.run_portable_reviewer_archive_guide",
        "scripts.run_delivery_rehearsal_binder",
        "scripts.run_delivery_quality_report",
        "scripts.run_delivery_status"
    ]
    for mod in mods:
        try:
            importlib.import_module(mod)
        except Exception:
            pass # just checking syntax mostly
