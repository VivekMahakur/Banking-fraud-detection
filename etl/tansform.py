import pandas as pd
import os


def transform_data():

    # Project base path
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    input_path = os.path.join(BASE_DIR,
                              "data", "raw", "creditcard.csv")

    output_path = os.path.join(BASE_DIR,
                               "data", "processed",
                               "clean_transactions.csv")

    # Load data
    df = pd.read_csv(input_path)

    print("Original Shape:", df.shape)

    # -----------------------
    # Data Cleaning
    # -----------------------

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Normalize Amount column
    df["Amount"] = (
        df["Amount"] - df["Amount"].mean()
    ) / df["Amount"].std()

    print("Cleaned Shape:", df.shape)

    # Save processed data
    df.to_csv(output_path, index=False)

    print("Processed data saved")


if __name__ == "__main__":
    transform_data()