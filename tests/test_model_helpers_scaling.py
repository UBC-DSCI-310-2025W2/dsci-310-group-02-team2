import pandas as pd
from src.model_helpers_scaling import scale_features
import pytest
import numpy as np

def test_scale_features_math():
    """Test if the mean is 0 and standard deviation is 1 after scaling."""
    train = pd.DataFrame({"A": [10, 20, 30], "B": [1, 2, 3]})
    test = pd.DataFrame({"A": [15], "B": [1.5]})
    
    train_scaled, test_scaled = scale_features(train, test)
    
    # Check training mean is approx 0 and std is approx 1
    assert np.allclose(train_scaled.mean(), 0)
    assert np.allclose(train_scaled.std(ddof=0), 1)
    # Check that it returned DataFrames
    assert isinstance(train_scaled, pd.DataFrame)
    assert list(train_scaled.columns) == ["A", "B"]

def test_scale_features_input_error():
    """Test that the function raises a TypeError if inputs are not DataFrames."""
    with pytest.raises(TypeError):
        scale_features([1, 2, 3], [4, 5, 6])

def test_scale_features_preserves_index():
    """Test if the original indices are preserved after scaling."""
    train = pd.DataFrame({"A": [10, 20]}, index=["row1", "row2"])
    test = pd.DataFrame({"A": [15]}, index=["row3"])
    
    train_scaled, test_scaled = scale_features(train, test)
    
    assert list(train_scaled.index) == ["row1", "row2"]
    assert list(test_scaled.index) == ["row3"]

def test_scale_features_mismatched_columns():
    """Test that it raises an error if test set has different columns than train set."""
    train = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    test = pd.DataFrame({"C": [5, 6]}) # 'C' instead of 'A' and 'B'
    
    # Scikit-learn's transform() will naturally raise a ValueError here
    with pytest.raises(ValueError):
        scale_features(train, test)

def test_scale_features_constant_column():
    """Test behavior when a column has zero variance (all same values)."""
    # Standard deviation will be 0, scaling usually results in 0s
    train = pd.DataFrame({"A": [10, 10, 10]}) 
    test = pd.DataFrame({"A": [10]})
    
    train_scaled, test_scaled = scale_features(train, test)
    
    assert np.all(train_scaled["A"] == 0)
    assert np.all(test_scaled["A"] == 0)