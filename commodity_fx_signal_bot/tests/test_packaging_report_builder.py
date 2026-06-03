from portable_packaging.packaging_report_builder import (
    build_packaging_disclaimer,
    build_environment_snapshot_markdown_report,
    build_dependency_inventory_markdown_report,
    build_requirements_export_markdown_report,
    build_install_verification_markdown_report,
    build_portable_bundle_manifest_markdown_report,
    build_packaging_quality_markdown_report,
    build_packaging_status_markdown_report
)

def test_report_builder():
    disc = build_packaging_disclaimer()
    assert "UYARI" in disc
    assert "gerçek emir" in disc

    md = build_environment_snapshot_markdown_report({})
    assert "Environment Snapshot Report" in md

    md = build_dependency_inventory_markdown_report({})
    assert "Dependency Inventory Report" in md

    md = build_requirements_export_markdown_report({})
    assert "Requirements Export Report" in md

    md = build_install_verification_markdown_report({})
    assert "Install Verification Report" in md

    md = build_portable_bundle_manifest_markdown_report({})
    assert "Portable Bundle Manifest Report" in md

    md = build_packaging_quality_markdown_report({}, {})
    assert "Packaging Quality Report" in md

    md = build_packaging_status_markdown_report({})
    assert "Packaging Status Report" in md
