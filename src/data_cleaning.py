import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the DataFrame with standardized column names.

    Standardization rules:
    - lowercase all column names
    - replace spaces with underscores
    - strip leading/trailing whitespace

    Args:
        df: Input pandas DataFrame.

    Returns:
        A new DataFrame with standardized column names.
    """
    cleaned_columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df_cleaned = df.copy()
    df_cleaned.columns = cleaned_columns
    return df_cleaned
