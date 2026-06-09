for f in commodity_fx_signal_bot/tests/test_evidence*.py commodity_fx_signal_bot/tests/test_artifact_inventory.py commodity_fx_signal_bot/tests/test_policy_registry.py commodity_fx_signal_bot/tests/test_control_registry.py commodity_fx_signal_bot/tests/test_control_mapping.py commodity_fx_signal_bot/tests/test_traceability_matrix.py; do
    sed -i 's/from evidence_governance/from evidence_governance/g' $f
done
