import pandas as pd


def create_feature_overview(df: pd.DataFrame) -> pd.DataFrame:
    """Create a summary table of DataFrame feature metadata.

    The summary includes each feature name, its data type, non-null count,
    missing value count, and number of unique values.

    Args:
        df: Input pandas DataFrame.

    Returns:
        A pandas DataFrame with one row per input feature.
    """
    overview = pd.DataFrame(
        {
            "Features": df.columns,
            "Data Types": df.dtypes.astype(str).values,
            "Non-null Values": df.notnull().sum().values,
            "Missing Values": df.isnull().sum().values,
            "Unique Values": df.nunique().values,
        }
    )
    return overview
