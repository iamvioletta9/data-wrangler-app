import streamlit as st
import pandas as pd

st.title("Dataset Upload")

file = st.file_uploader(
    "Upload dataset",
    type=["csv","xlsx","json"]
)

if file:

    if file.name.endswith("csv"):
        df = pd.read_csv(file)

    elif file.name.endswith("xlsx"):
        df = pd.read_excel(file)

    elif file.name.endswith("json"):
        df = pd.read_json(file)

    st.session_state["data"] = df

    st.success("Dataset loaded")

    st.subheader("Preview")

    st.dataframe(df.head())

    col1,col2,col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing values", df.isnull().sum().sum())

else:

    st.warning("Upload a dataset to begin.")