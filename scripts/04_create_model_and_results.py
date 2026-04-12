import argparse
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    accuracy_score
)

from logreg_project_prep.split_data import split_data
from logreg_project_prep.scaling_helpers import scale_features

def create_model_and_results(data_path: str, output_prefix: str) -> None:
    """
    Loads cleaned data, trains logistic regression model,
    evaluates it, and saves results.
    """

    # Load dataset
    df = pd.read_csv(data_path)

    # Split data
    X_train, X_test, y_train, y_test = split_data(df, "revenue")

    # Scale features
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)

    # Train model
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)

    # --------------------------
    # Model evaluation
    # --------------------------

    # Predictions
    y_pred = model.predict(X_test_scaled)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    # Save metrics for Quarto
    metrics = pd.DataFrame({
        "accuracy": [accuracy],
        "true_negative": [tn],
        "false_positive": [fp],
        "false_negative": [fn],
        "true_positive": [tp]
    })

    metrics.to_csv(f"{output_prefix}_metrics.csv", index=False)

    # Confusion matrix plot
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Not Purchased", "Purchased"]
    )

    disp.plot()
    plt.title(f"Confusion Matrix (Accuracy = {accuracy:.3f})")

    plt.savefig(f"{output_prefix}_confusion_matrix.png")
    plt.close()

    # Classification report
    cr = classification_report(y_test, y_pred, output_dict=True)
    pd.DataFrame(cr).transpose().to_csv(
        f"{output_prefix}_classification_report.csv"
    )

    print(f"Model results saved to {output_prefix}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", help="File path for cleaned dataset")
    parser.add_argument("output_prefix", help="Output prefix for results")
    args = parser.parse_args()

    create_model_and_results(args.data_path, args.output_prefix)