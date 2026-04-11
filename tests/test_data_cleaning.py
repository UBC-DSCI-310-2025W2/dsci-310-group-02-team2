import pandas as pd
import pytest

from src.data_cleaning import standardize_column_names


def test_standardize_column_names_basic():
    """Test that column names are standardized and original DataFrame is unchanged."""
    df = pd.DataFrame(
        {
            "Administrative Duration": [1, 2],
            "ProductRelated": [3, 4],
            "  Special Day ": [5, 6],
        }
    )

    result = standardize_column_names(df)

    assert list(result.columns) == [
        "administrative_duration",
        "productrelated",
        "special_day",
    ]
    assert result.iloc[1, 2] == 6
    assert list(df.columns) == [
        "Administrative Duration",
        "ProductRelated",
        "  Special Day ",
    ]


def test_standardize_column_names_type_error():
    """Test that function raises TypeError when input is not a DataFrame."""
    with pytest.raises(TypeError):
        standardize_column_names([1, 2, 3])

