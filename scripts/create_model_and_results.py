import argparse
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

from logreg_project_prep.split_data import split_data
from logreg_project_prep.scaling_helpers import scale_features


def save_table(df: pd.DataFrame, path: str) -> None:
    """
    Save pandas DataFrame to CSV file.
    """
    df.to_csv(path, index=True)


def create_model_and_results(data_path: str, output_prefix: str) -> None:
    """
    Loads cleaned dataset, trains logistic regression model,
    evaluates it, and saves results (metrics + plots + reports).
    """

    # --------------------------
    # 1. Load data
    # --------------------------
    df = pd.read_csv(data_path)

    # --------------------------
    # 2. Split data
    # --------------------------
    X_train, X_test, y_train, y_test = split_data(df, "revenue")

    # --------------------------
    # 3. Scale features
    # --------------------------
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)

    # --------------------------
    # 4. Train model
    # --------------------------
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)

    # --------------------------
    # 5. Predictions & metrics
    # --------------------------
    y_pred = model.predict(X_test_scaled)

    accuracy = model.score(X_test_scaled, y_test)
    cm = confusion_matrix(y_test, y_pred)

    tn, fp, fn, tp = cm.ravel()

    # --------------------------
    # 6. Save METRICS (IMPORTANT for QMD)
    # --------------------------
    metrics_df = pd.DataFrame({
        "accuracy": [accuracy],
        "true_negative": [tn],
        "false_positive": [fp],
        "false_negative": [fn],
        "true_positive": [tp]
    })

    metrics_df.to_csv(f"{output_prefix}_metrics.csv", index=False)

    # --------------------------
    # 7. Confusion matrix plot
    # --------------------------
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Not Purchased", "Purchased"]
    )

    disp.plot()
    plt.title(f"Validation Accuracy = {accuracy:.3f}")
    plt.savefig(f"{output_prefix}_confusion_matrix.png")
    plt.close()

    # --------------------------
    # 8. Classification report
    # --------------------------
    cr = classification_report(y_test, y_pred, output_dict=True)
    cr_df = pd.DataFrame(cr).transpose()

    cr_df.to_csv(f"{output_prefix}_classification_report.csv", index=True)

    print(f"Model results saved to {output_prefix}")


# --------------------------
# CLI entry point
# --------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", help="File path for cleaned dataset")
    parser.add_argument("output_prefix", help="Output prefix for results")

    args = parser.parse_args()

    create_model_and_results(args.data_path, args.output_prefix)