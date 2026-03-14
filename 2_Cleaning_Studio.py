import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler

st.title("Cleaning Studio")

if "data" not in st.session_state:
    st.warning("Upload data first")
    st.stop()

df = st.session_state["data"]

st.subheader("Current dataset")

st.dataframe(df.head())

st.markdown("---")

option = st.selectbox(
    "Choose cleaning operation",
    [
        "Handle missing values",
        "Drop column",
        "Rename column",
        "Scale numeric feature"
    ]
)

if option == "Handle missing values":

    method = st.selectbox(
        "Method",
        ["Drop rows","Fill mean","Fill median"]
    )

    if st.button("Apply"):

        if method == "Drop rows":
            df = df.dropna()

        elif method == "Fill mean":
            df = df.fillna(df.mean(numeric_only=True))

        elif method == "Fill median":
            df = df.fillna(df.median(numeric_only=True))

        st.session_state["data"] = df
        st.success("Missing values processed")


elif option == "Drop column":

    col = st.selectbox("Column", df.columns)

    if st.button("Drop column"):

        df = df.drop(columns=[col])

        st.session_state["data"] = df

elif option == "Rename column":

    col = st.selectbox("Column", df.columns)

    new = st.text_input("New name")

    if st.button("Rename"):

        df.rename(columns={col:new}, inplace=True)

        st.session_state["data"] = df


elif option == "Scale numeric feature":

    numeric = df.select_dtypes("number").columns

    col = st.selectbox("Feature", numeric)

    if st.button("Scale"):

        scaler = StandardScaler()

        df[col] = scaler.fit_transform(df[[col]])

        st.session_state["data"] = df


st.markdown("---")

st.subheader("Updated dataset")

st.dataframe(df.head())