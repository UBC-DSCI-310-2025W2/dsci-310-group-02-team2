import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the DataFrame with standardized column names.

    Standardization rules:
    - lowercase all column names
    - replace spaces with underscores
    - strip leading/trailing whitespace

    Args:
        df (pd.DataFrame): Input pandas DataFrame.

    Returns:
        pd.DataFrame: A new DataFrame with standardized column names.

    Raises:
        TypeError: If df is not a pandas DataFrame.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({"Column A": [1, 2], " Column B ": [3, 4]})
        >>> standardize_column_names(df).columns.tolist()
        ['column_a', 'column_b']
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    cleaned_columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df_cleaned = df.copy()
    df_cleaned.columns = cleaned_columns
    return df_cleaned
