import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(df, target_variable):
    """Return training and testing datasets: X_train, X_test, y_train, y_test.

    Splits dataset into training and testing datasets into an 80-20 ratio and separates 
    X values from y values. Also ensures that values in X is numeric for scaling purposes.

    Args:
        df: Input pandas DataFrame.
        target_variable: single target variable

    Returns:
        4 datasets: X_train, X_test, y_train, y_test
    """
    y = df[target_variable]
    X = df.drop(columns=target_variable).select_dtypes(include='number')
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    return X_train, X_test, y_train, y_test