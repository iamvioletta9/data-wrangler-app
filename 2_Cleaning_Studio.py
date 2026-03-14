import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

st.title("Cleaning & Preparation Studio")

if "data" not in st.session_state:
    st.warning("Upload a dataset first.")
    st.stop()

df = st.session_state["data"].copy()

# initialize log
if "transform_log" not in st.session_state:
    st.session_state["transform_log"] = []

log = st.session_state["transform_log"]

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.write(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")

# ------------------
# Missing values
# ------------------

st.header("Missing Values")

st.write(df.isnull().sum())

column = st.selectbox("Column", df.columns)

method = st.selectbox(
    "Method",
    ["Drop rows", "Fill mean", "Fill median", "Fill mode"]
)

if st.button("Apply Missing Value Fix"):

    if method == "Drop rows":
        df = df.dropna(subset=[column])

    elif method == "Fill mean":
        df[column] = pd.to_numeric(df[column], errors="coerce")
        df[column] = df[column].fillna(df[column].mean())

    elif method == "Fill median":
        df[column] = pd.to_numeric(df[column], errors="coerce")
        df[column] = df[column].fillna(df[column].median())

    elif method == "Fill mode":
        df[column] = df[column].fillna(df[column].mode()[0])

    st.session_state["data"] = df
    log.append(f"Handled missing values in {column}")

    st.success("Done")

# ------------------
# Duplicates
# ------------------

st.header("Duplicates")

dup_count = df.duplicated().sum()
st.write("Duplicates:", dup_count)

if st.button("Remove duplicates"):

    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    st.session_state["data"] = df
    log.append(f"Removed {before-after} duplicates")

    st.success("Duplicates removed")

# ------------------
# Scaling
# ------------------

st.header("Scaling")

numeric_cols = df.select_dtypes(include=np.number).columns

scale_cols = st.multiselect("Columns", numeric_cols)

scale_type = st.selectbox(
    "Scaling method",
    ["MinMax", "Z-score"]
)

if st.button("Apply scaling"):

    if len(scale_cols) > 0:

        if scale_type == "MinMax":
            scaler = MinMaxScaler()
        else:
            scaler = StandardScaler()

        df[scale_cols] = scaler.fit_transform(df[scale_cols])

        st.session_state["data"] = df
        log.append(f"{scale_type} scaling applied to {scale_cols}")

        st.success("Scaling applied")

# ------------------
# Rename column
# ------------------

st.header("Rename Column")

old = st.selectbox("Column to rename", df.columns)
new = st.text_input("New name")

if st.button("Rename"):

    if new.strip() != "":
        df = df.rename(columns={old: new})

        st.session_state["data"] = df
        log.append(f"Renamed {old} to {new}")

        st.success("Renamed")

# ------------------
# Transformation log
# ------------------

st.header("Transformation Log")

if len(log) > 0:
    st.write(log)
else:
    st.write("No transformations yet.")