import pandas as pd
import pytest

from src.data_splitting import split_data


def test_data_splitting():
    """Test correct train/test split, types, and structure of outputs."""
    
    df = pd.DataFrame({
        'revenue': [True, True, False, False, False, True, True, True, False, False],
        'month': ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct'],
        'productrelated': [0.0, 0.2, 1, 4, 2, 1, 2, 0, 1, 0.3],
        'administrative': [1, 0, 0, 2, 4, 3, 1, 2, 0, 1]
    })

    X_train, X_test, y_train, y_test = split_data(df, 'revenue')

    assert len(X_train) == 8
    assert len(X_test) == 2

    assert 'revenue' not in X_train.columns
    assert 'revenue' not in X_test.columns

    assert len(X_train.select_dtypes(include='number').columns) == len(X_train.columns)

    assert len(y_train) == 8
    assert len(y_test) == 2

    assert y_train.dtype == bool
    assert y_test.dtype == bool

    assert y_train.sum() == 4
    assert y_test.sum() == 1


def test_split_data_type_errors():
    """Test that split_data raises errors for invalid inputs."""
    df = pd.DataFrame({"a": [1, 2], "target": [0, 1]})

    with pytest.raises(TypeError):
        split_data([1, 2, 3], "target")

    with pytest.raises(TypeError):
        split_data(df, 123)


def test_split_data_missing_target():
    """Test that split_data raises ValueError when target column is missing."""
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})

    with pytest.raises(ValueError):
        split_data(df, "target")