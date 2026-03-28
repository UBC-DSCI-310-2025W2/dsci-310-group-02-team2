import pandas as pd

from src.data_cleaning import standardize_column_names


def test_standardize_column_names_basic():
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
