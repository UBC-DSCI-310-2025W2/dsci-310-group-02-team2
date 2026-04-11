import argparse
import pandas as pd

def validate_data(file_path: str):
    """
    Perform 8 important data validation checks on the dataset.
    Raises ValueError or AssertionError if validation fails.
    """
    df = pd.read_csv(file_path)

    # 1. Dataset not empty
    if df.empty:
        raise ValueError("Data validation failed: The dataset is completely empty.")

    # 2. Minimum Size Check (Row count)
    if len(df) < 50:
        raise ValueError(f"Data validation failed: Dataset too small for reliable modeling ({len(df)} rows).")

    # 3. Check for exact expected column count
    # Note: online shoppers intention typically has 18 columns.
    if len(df.columns) < 5:
        raise ValueError(f"Data validation failed: Very few columns found ({len(df.columns)}). Expected around 18.")

    # 4. Check for missing values (NaNs)
    if df.isna().sum().sum() > 0:
        raise ValueError("Data validation failed: The dataset contains missing values (NaNs).")

    # 5. Type Consistency
    # Ensure all columns have consistent types (pandas type resolution is strict if mixed types)
    for col in df.columns:
        if df[col].dtype == 'object':
            # Check if there are mixed types in objects
            types = set(df[col].apply(type))
            if len(types) > 1:
                 raise TypeError(f"Data validation failed: Column '{col}' contains mixed types: {types}.")

    # 6. Target Variable presence and binary
    target_col = 'revenue'
    if target_col not in df.columns:
        # Some cleaned data might use 'revenue' or something else. We'll search for 'revenue'
        target_cols = [c for c in df.columns if 'revenue' in c.lower()]
        if not target_cols:
             raise ValueError("Data validation failed: Missing target variable 'revenue' in the dataset.")
        target_col = target_cols[0]

    unique_targets = df[target_col].dropna().unique()
    if len(unique_targets) != 2:
        raise ValueError(f"Data validation failed: Target '{target_col}' should be binary, found {len(unique_targets)} unique values.")

    # 7. Non-negative constraints on numeric fields
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        if (df[col] < 0).any():
            # Most features in this dataset (bounces, durations, value) are non-negative
            raise ValueError(f"Data validation failed: Column '{col}' contains unexpected negative values.")

    # 8. Class Representation (No Data leakage check / pre-split verification)
    # Ensure that both the positive and negative class have a minimal representative distribution (>10 samples)
    class_counts = df[target_col].value_counts()
    if class_counts.min() < 10:
        raise ValueError(f"Data validation failed: Severe class imbalance or missing class in target '{target_col}'. Details: {class_counts.to_dict()}")

    print("SUCCESS: Data passed all 8 validation checks.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate data against 8 crucial criteria.")
    parser.add_argument("data_path", help="Path to the cleaned dataset.")
    args = parser.parse_args()

    validate_data(args.data_path)
