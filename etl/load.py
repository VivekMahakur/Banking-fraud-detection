import pandas as pd
from sqlalchemy import create_engine


def load_data():

    # -----------------------------
    # 1. Load Dataset
    from pathlib import Path
    import pandas as pd

    BASE_DIR = Path(__file__).resolve().parent.parent
    file_path = BASE_DIR / "data" / "raw" / "creditcard.csv"

    df = pd.read_csv(file_path)
    print("Dataset Loaded ✅")
    print(f"Rows: {len(df)}")

    # -----------------------------
    # 2. PostgreSQL Connection
    # -----------------------------
    engine = create_engine(
        "postgresql+psycopg2://postgres@127.0.0.1:5432/fraud_db",
        connect_args={
            "password": "subarna29@"   # ✅ safe password handling
        }
    )

    print("Loading data into PostgreSQL...")

    # -----------------------------
    # 3. Load into PostgreSQL
    # -----------------------------
    df.to_sql(
        name="transactions",
        con=engine,
        if_exists="replace",   # change to 'append' later
        index=False,
        chunksize=5000,        # ✅ faster loading
        method="multi"
    )

    print("Data Loaded Successfully ✅")


if __name__ == "__main__":
    load_data()