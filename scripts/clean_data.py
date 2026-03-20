import argparse
import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)

    df.columns = df.columns.str.lower().str.replace(" ", "_")

    df = df.drop_duplicates()

    df.to_csv(output_path, index=False)

    print(f"Cleaned data saved to {output_path}")

parser = argparse.ArgumentParser()
parser.add_argument("input_path")
parser.add_argument("output_path")
args = parser.parse_args()

clean_data(args.input_path, args.output_path)