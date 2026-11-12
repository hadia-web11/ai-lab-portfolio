"""Lab 01 home assignment: one compact inspection report for any CSV."""
import os
import sys

# This file is named inspect.py (as the manual requires), which would shadow
# Python's built-in "inspect" module when the script is run directly.
# Remove this folder from sys.path before importing pandas.
_here = os.path.dirname(os.path.abspath(__file__))
sys.path = [p for p in sys.path if os.path.abspath(p or ".") != _here]

import pandas as pd


def inspect(path_or_url):
    df = pd.read_csv(path_or_url)
    print("=" * 60)
    print(f"SOURCE : {path_or_url}")
    print(f"SHAPE  : {df.shape[0]} rows x {df.shape[1]} columns")
    print("\nDTYPES:")
    print(df.dtypes.to_string())
    print("\nMISSING VALUES (count, percent):")
    miss = pd.DataFrame({"missing": df.isnull().sum(),
                         "percent": (df.isnull().mean() * 100).round(2)})
    print(miss.to_string())
    print("\nNUMERIC SUMMARY:")
    print(df.describe().T.to_string())
    print("=" * 60)
    return df


if __name__ == "__main__":
    for p in sys.argv[1:]:
        inspect(p)
