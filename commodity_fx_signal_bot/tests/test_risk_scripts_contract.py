def test_risk_scripts_import():
    try:
        import scripts.run_risk_precheck_preview
        import scripts.run_risk_batch_build
        import scripts.run_risk_pool_preview
        import scripts.run_risk_status
    except Exception as e:
        assert False, f"Failed to import risk scripts: {e}"
