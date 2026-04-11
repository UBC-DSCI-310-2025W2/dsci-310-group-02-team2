import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(df: pd.DataFrame, target_variable: str):
    """Split dataset into training and testing sets.

    Performs an 80-20 split and separates features (X) from target (y).
    Only numeric columns are kept in X.

    Args:
        df (pd.DataFrame): Input dataset.
        target_variable (str): Name of the target column.

    Returns:
        tuple:
            X_train (pd.DataFrame)
            X_test (pd.DataFrame)
            y_train (pd.Series)
            y_test (pd.Series)

    Raises:
        TypeError: If df is not a DataFrame or target_variable is not a string.
        ValueError: If target_variable is not in df.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({
        ...     "feature1": [1, 2, 3, 4],
        ...     "feature2": [5, 6, 7, 8],
        ...     "target": [0, 1, 0, 1]
        ... })
        >>> X_train, X_test, y_train, y_test = split_data(df, "target")
        >>> len(X_train) + len(X_test) == len(df)
        True
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if not isinstance(target_variable, str):
        raise TypeError("target_variable must be a string")
    if target_variable not in df.columns:
        raise ValueError(f"{target_variable} not found in DataFrame")

    y = df[target_variable]
    X = df.drop(columns=target_variable).select_dtypes(include="number")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    return X_train, X_test, y_train, y_test