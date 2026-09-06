"""Test suite for Phase 136 GPU ML Runtime Data Models."""

import pytest
from advanced_gpu_ml_runtime.gpu_ml_runtime_models import (
    HardwareDiscoveryItem,
    GpuCapabilityItem,
    CpuCapabilityItem,
    MemoryCapabilityItem,
    RuntimeDependencyCapabilityItem,
    AcceleratorBackendItem,
    MlRuntimeSafetyContract,
    MlExperimentPermissionPolicy,
    MlInputContract,
    MlRuntimeFinding,
    MlRuntimeReadinessScore,
)


def test_models_instantiation():
    hw = HardwareDiscoveryItem(
        item_id="hw_os",
        category="os",
        property_name="system",
        property_value="Windows",
        status_label="runtime_ready",
    )
    assert hw.item_id == "hw_os"
    assert hw.non_signal is True

    gpu = GpuCapabilityItem(
        gpu_id="gpu_0",
        gpu_name="NVIDIA GeForce",
        cuda_available=True,
        device_count=1,
        memory_total_mb=8192.0,
        capability_status="runtime_ready",
    )
    assert gpu.gpu_id == "gpu_0"
    assert gpu.cuda_available is True

    contract = MlRuntimeSafetyContract(
        contract_id="SC-01",
        topic="no_live_trading",
        enforced=True,
        prohibition_rule="PROHIBIT_LIVE",
    )
    assert contract.contract_id == "SC-01"
    assert contract.enforced is True

    inp = MlInputContract(
        contract_id="IC-01",
        source_component="regime",
        source_phase=126,
        dataset_entity="macro_regime",
        accepted_reference_required=True,
        no_lookahead_accepted_required=True,
        metadata_only_news_accepted_required=True,
        source_preserved_required=True,
        non_signal_required=True,
    )
    assert inp.contract_id == "IC-01"
    assert inp.model_training_allowed is False
