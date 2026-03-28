import pandas as pd

from src.data_splitting import split_data


def test_data_splitting():
    
    # create fake dataframe
    df = pd.DataFrame({
        'revenue': [True, True, False, False, False],
        'month': ['jan', 'feb', 'mar', 'apr', 'jun'],
        'productrelated': [0.0, 0.2, 1, 4, 2],
        'administrative': [1, 0, 0, 2, 4]
    })

    # call split_data function
    X_train, X_test, y_train, y_test = split_data(df, 'revenue')

    # check test results
    assert len(X_train) == 4, "split size is incorrect"
    assert len(X_test) == 1, "split size is incorrect"
    assert len(y_train) == 4, "split size is incorrect"
    assert len(y_test) == 1, "split size is incorrect"
    
    assert 'revenue' not in X_train.columns, "target variable found in X_train"
    assert 'revenue' not in X_test.columns, "target variable found in X_test"
    
    assert len(X_train.select_dtypes(include='number').columns) == len(X_train.columns), "Values in X sets are not numeric"