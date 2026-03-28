import pandas as pd

from src.eda_helpers import create_feature_overview


def test_create_feature_overview_counts():
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
