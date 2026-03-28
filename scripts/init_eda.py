import argparse
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from pathlib import Path

from src.eda_helpers import create_feature_overview

def save_table(df: pd.DataFrame, path: str) -> None: 
    """
    Save table (pandas dataframe) into CSV file
    """
    df.to_csv(path, index=True)


def init_eda(data_path: str, output_prefix: str) -> None: 
    """
    Takes cleaned dataset file path and performs EDA (see comments below for details). Also 
    takes a prefix string as 2nd argument to append to output file after EDA is performed. The 
    EDA performed is specific to the `online_shoppers` dataset.
    z
    """
    #load cleaned dataset
    df = pd.read_csv(data_path)

    #ensure output path exists 
    ouput_prefix_path = Path(output_prefix)
    ouput_prefix_path.parent.mkdir(parents=True, exist_ok=True)

    # Basic dataset overview
    overview = create_feature_overview(df)
    save_table(overview, f"{output_prefix}_overview.csv")

    #revenue count: 
    rev_count_table = df["revenue"].value_counts().reset_index()
    rev_count_table.columns = ["revenue", "Count"]
    save_table(rev_count_table, f"{output_prefix}_revenue_count.csv")

    #Bar graph: revenue count per customer 
    rev_count_by_customer = df.groupby('visitortype')['revenue'].value_counts().unstack()
    rev_count_by_customer.plot(kind="bar", stacked=True, figsize=(8, 5))

    plt.xlabel("Vistor Type")
    plt.ylabel("Count")
    plt.title("Revenue Distribution by Visitor Type")
    plt.show()
    plt.savefig(f"{output_prefix}_revenue_by_visitor_type.png")
    plt.close()

    #correlation map of features 
    feature_correlation = df.corr(numeric_only=True) 
    plt.figure(figsize=(10, 8))
    sns.heatmap(feature_correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Online Shoppers Intention Correlation Heatmap")
    plt.show()
    plt.savefig(f"{output_prefix}_correlation_heatmap.png")
    plt.close()

    print(f"EDA complete. Files written with prefix: {output_prefix}")

parser = argparse.ArgumentParser()
parser.add_argument("data_path", help="File path for cleaned dataset, please input a csv file")
parser.add_argument("output_prefix", help="Output prefix for prefix and figures, please use results/xxx")
args = parser.parse_args()

init_eda(args.data_path, args.output_prefix)







