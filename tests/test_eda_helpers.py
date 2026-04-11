import pandas as pd
import pytest

from src.eda_helpers import create_feature_overview


def test_create_feature_overview_counts():
    """Test that feature overview computes correct summary statistics."""
    df = pd.DataFrame(
        {
            "A": [1, 2, None],
            "B": ["x", "x", "y"],
        }
    )

    overview = create_feature_overview(df)

    assert list(overview.columns) == [
        "Features",
        "Data Types",
        "Non-null Values",
        "Missing Values",
        "Unique Values",
    ]
    assert overview.loc[overview["Features"] == "A", "Non-null Values"].iloc[0] == 2
    assert overview.loc[overview["Features"] == "A", "Missing Values"].iloc[0] == 1
    assert overview.loc[overview["Features"] == "B", "Unique Values"].iloc[0] == 2


def test_create_feature_overview_type_error():
    """Test that function raises TypeError when input is not a DataFrame."""
    with pytest.raises(TypeError):
        create_feature_overview("not a dataframe")