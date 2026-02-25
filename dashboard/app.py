import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine(
    "postgresql+psycopg2://postgres:subarna29%40@127.0.0.1:5432/fraud_db"
)

df = pd.read_sql("SELECT * FROM fact_transactions", engine)

st.set_page_config(page_title="Fraud Dashboard", layout="wide")

st.title("🏦 Banking Transaction Fraud Detection Dashboard")

# --- Fraud Count ---
st.subheader("Fraud vs Non-Fraud Distribution")
fraud_counts = df["is_fraud"].value_counts()
st.bar_chart(fraud_counts)

# --- Fraud Percentage ---
fraud_percentage = (fraud_counts[1] / fraud_counts.sum()) * 100
st.metric("Fraud Percentage", f"{fraud_percentage:.4f}%")

# --- Top High Transactions ---
st.subheader("Top 10 Highest Transactions")
top_transactions = df.sort_values("Amount", ascending=False).head(10)
st.dataframe(top_transactions)

# --- Transaction Amount Distribution ---
st.subheader("Transaction Amount Distribution")
st.line_chart(df["Amount"].head(500))