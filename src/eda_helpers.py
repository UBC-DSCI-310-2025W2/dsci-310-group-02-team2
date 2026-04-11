import pandas as pd


def create_feature_overview(df: pd.DataFrame) -> pd.DataFrame:
    """Create a summary table of DataFrame feature metadata.

    The summary includes each feature name, its data type, non-null count,
    missing value count, and number of unique values.

    Args:
        df (pd.DataFrame): Input pandas DataFrame.

    Returns:
        pd.DataFrame: A summary DataFrame with one row per feature.

    Raises:
        TypeError: If df is not a pandas DataFrame.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({"A": [1, 2, None], "B": ["x", "y", "y"]})
        >>> overview = create_feature_overview(df)
        >>> "Missing Values" in overview.columns
        True
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

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