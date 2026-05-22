import pytest
from factor_research.factor_labels import validate_factor_type, list_factor_type_labels

def test_labels():
    labels = list_factor_type_labels()
    assert "trend_factor" in labels

    validate_factor_type("trend_factor")

    with pytest.raises(ValueError):
        validate_factor_type("invalid_label")
