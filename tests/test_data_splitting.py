import pandas as pd

from src.data_splitting import split_data


def test_data_splitting():
    
    # create fake dataframe
    df = pd.DataFrame({
        'revenue': [True, True, False, False, False, True, True, True, False, False],
        'month': ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct'],
        'productrelated': [0.0, 0.2, 1, 4, 2, 1, 2, 0, 1, 0.3],
        'administrative': [1, 0, 0, 2, 4, 3, 1, 2, 0, 1]
    })

    # call split_data function
    X_train, X_test, y_train, y_test = split_data(df, 'revenue')

    # check X split size
    assert len(X_train) == 8, f"expected 8 rows in X_train, got {len(X_train)}"
    assert len(X_test) == 2, f"expected 2 row in X_test, got {len(X_test)}"

    # check target variable not in X
    assert 'revenue' not in X_train.columns, "unexpected revenue column found in X_train"
    assert 'revenue' not in X_test.columns, "unexpected revenue column found in X_test"

    # check X values are numeric
    assert len(X_train.select_dtypes(include='number').columns) == len(X_train.columns), "Values in X sets are not numeric"

    # check y split size
    assert len(y_train) == 8, f"expected 8 values in y_train, got {len(y_train)}"
    assert len(y_test) == 2, f"expected 2 value in y_test, got {len(y_test)}"

    # check y dtype
    assert y_train.dtype == bool, f"expected boolean dtype, got {y_train.dtype}"
    assert y_test.dtype == bool, f"expected boolean dtype, got {y_test.dtype}"

    # check y values
    assert y_train.sum() == 4, f"expected 2, got {y_train.sum()}"
    assert y_test.sum() == 1, f"expected 1, got {y_test.sum()}"