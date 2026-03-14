import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Visualization Builder")

if "data" not in st.session_state:
    st.warning("Upload a dataset first.")
    st.stop()

df = st.session_state["data"]

numeric_cols = df.select_dtypes(include=np.number).columns

chart = st.selectbox(
    "Chart type",
    ["Histogram", "Scatter", "Line", "Box"]
)

if chart == "Histogram":

    col = st.selectbox("Column", numeric_cols)

    fig, ax = plt.subplots()
    ax.hist(df[col].dropna())

    st.pyplot(fig)

elif chart == "Scatter":

    x = st.selectbox("X", numeric_cols)
    y = st.selectbox("Y", numeric_cols)

    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y])

    st.pyplot(fig)

elif chart == "Line":

    x = st.selectbox("X", df.columns)
    y = st.selectbox("Y", numeric_cols)

    fig, ax = plt.subplots()
    ax.plot(df[x], df[y])

    st.pyplot(fig)

elif chart == "Box":

    col = st.selectbox("Column", numeric_cols)

    fig, ax = plt.subplots()
    ax.boxplot(df[col].dropna())

    st.pyplot(fig)