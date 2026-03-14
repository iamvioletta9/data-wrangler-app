import streamlit as st
import pandas as pd

st.title("Upload & Overview")

uploaded_file = st.file_uploader(
    "Upload dataset",
    type=["csv", "xlsx", "json"]
)

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    elif uploaded_file.name.endswith(".json"):
        df = pd.read_json(uploaded_file)

    # sanitize object columns to avoid Arrow issues
    df = df.convert_dtypes()

    st.session_state["data"] = df

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.write("Shape:", df.shape)

    st.subheader("Column Types")
    st.write(df.dtypes)

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    st.subheader("Duplicate Rows")
    st.write(df.duplicated().sum())