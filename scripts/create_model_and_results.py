import argparse
import pandas as pd 
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

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
    
    # 2. FIX: Select only numeric columns so the Scaler doesn't hit strings like 'Nov'
    X = df.select_dtypes(include=['number'])
    
    # 3. FIX: Ensure 'revenue' is the target and not part of the features (X)
    if 'revenue' in X.columns:
        X = X.drop('revenue', axis=1)
    y = df['revenue']

    # Split dataset 
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale data 
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

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
    save_table(cr_df, f"{output_prefix}_classification_report.csv")
    print(f"Model results saved to {output_prefix}...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", help="File path for cleaned dataset")
    parser.add_argument("output_prefix", help="Output prefix for results")
    args = parser.parse_args()

    create_model_and_results(args.data_path, args.output_prefix)