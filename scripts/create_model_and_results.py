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
    #load cleaned dataset, create X and y 
    df = pd.read_csv(data_path)
    X = df.drop('Revenue', axis=1)
    y = df['Revenue']

    #split dataset 
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
    )

    #scale data 
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    #create and fit model
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)

    #__________________#
    # Model evaluation #
    #__________________#

    score = model.score(X_test_scaled, y_test)
    y_pred = model.predict(X_test_scaled)

    #confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Not Purchased", "Purchased"])
    disp.plot()
    plt.title(f"The validation score of our logistic regression model is approximately {round(score, 3)}")
    plt.pyplot.show()
    plt.savefig(f"{output_prefix}_confusion_matrix.png")
    plt.close()

    #classification report
    cr = classification_report(y_test, y_pred, output_dict=True)
    cr_df = pd.DataFrame(cr).transpose()
    save_table(cr_df, f"{output_prefix}_classification_report.csv")

parser = argparse.ArgumentParser()
parser.add_argument("data_path", help="File path for cleaned dataset, please input a csv file")
parser.add_argument("output_prefix", help="Output prefix for prefix and figures, please use results/xxx")
args = parser.parse_args()

create_model_and_results(args.data_path, args.output_prefix)