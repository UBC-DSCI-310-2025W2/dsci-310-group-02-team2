import argparse
import shutil
from pathlib import Path
from urllib.request import urlopen


def load_data(input_path, output_path):
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    if input_path.startswith("http://") or input_path.startswith("https://"):
        with urlopen(input_path) as response, open(output_file, "wb") as f:
            shutil.copyfileobj(response, f)
    else:
        shutil.copy(input_path, output_file)


parser = argparse.ArgumentParser()
parser.add_argument("input_path")
parser.add_argument("output_path")
args = parser.parse_args()

load_data(args.input_path, args.output_path)
print(f"Saved file to {args.output_path}")