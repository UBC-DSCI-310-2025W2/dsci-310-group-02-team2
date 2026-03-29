import pandas as pd
from sklearn.preprocessing import StandardScaler
from typing import Tuple

def scale_features(train_df: pd.DataFrame, test_df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Applies standard scaling to training and testing datasets.
    
    The scaler is fit only on the training data to prevent data leakage,
    then applied to both the training and testing sets.

    Parameters
    ----------
    train_df : pd.DataFrame
        The training feature set.
    test_df : pd.DataFrame
        The testing feature set.

    Returns
    -------
    Tuple[pd.DataFrame, pd.DataFrame]
        A tuple containing (scaled_train_df, scaled_test_df) as DataFrames 
        with original column names and indices.
        
    Examples
    --------
    >>> train, test = scale_features(train_data, test_data)
    """
    if not isinstance(train_df, pd.DataFrame) or not isinstance(test_df, pd.DataFrame):
        raise TypeError("Inputs must be pandas DataFrames")
        
    scaler = StandardScaler()
    
    # Fit and transform
    train_scaled = scaler.fit_transform(train_df)
    test_scaled = scaler.transform(test_df)
    
    # Convert back to DataFrame to preserve metadata (better for DS workflows)
    train_scaled_df = pd.DataFrame(train_scaled, columns=train_df.columns, index=train_df.index)
    test_scaled_df = pd.DataFrame(test_scaled, columns=test_df.columns, index=test_df.index)
    
    return train_scaled_df, test_scaled_df