# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_feature_store_inventory."""

from advanced_final_delivery.final_delivery_feature_store_inventory import build_final_delivery_feature_store_inventory_registry


def test_build_final_delivery_feature_store_inventory_registry():
    df, summary = build_final_delivery_feature_store_inventory_registry()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
