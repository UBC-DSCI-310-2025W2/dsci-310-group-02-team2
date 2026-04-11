import argparse
import pandas as pd 
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
from logreg_project_prep.split_data import split_data
from logreg_project_prep.scaling_helpers import scale_features

def save_table(df: pd.DataFrame, path: str) -> None: 
    """
    Save table (pandas dataframe) into CSV file
    """
    df.to_csv(path, index=True)

def create_model_and_results(data_path: str, output_prefix: str) -> None:
    """
    Takes in a csv file path, performs data splitting on inputted data which is then used for fitting 
    and testing a logistic regression model. Model results are then saved with `output_prefix`.
    NOTE: ensure the dataset is clean before using this function.
    """
    # 1. Load cleaned dataset
    df = pd.read_csv(data_path)
    
    # Split dataset using function
    X_train, X_test, y_train, y_test = split_data(df, 'revenue')

    # Scale data using function 
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)

    # Create and fit model
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)

    #__________________#
    # Model evaluation #
    #__________________#

    score = model.score(X_test_scaled, y_test)
    y_pred = model.predict(X_test_scaled)

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Not Purchased", "Purchased"])
    disp.plot()
    plt.title(f"The validation score is approximately {round(score, 3)}")
    
    # 4. FIX: Removed .pyplot (it's just plt.show and plt.savefig)
    plt.savefig(f"{output_prefix}_confusion_matrix.png")
    plt.close()

    # Classification report
    cr = classification_report(y_test, y_pred, output_dict=True)
    cr_df = pd.DataFrame(cr).transpose()
    cr_df.to_csv(f"{output_prefix}_classification_report.csv", index=True)
    print(f"Model results saved to {output_prefix}...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", help="File path for cleaned dataset")
    parser.add_argument("output_prefix", help="Output prefix for results")
    args = parser.parse_args()

    create_model_and_results(args.data_path, args.output_prefix)