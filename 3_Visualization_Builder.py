import streamlit as st
import plotly.express as px

st.title("Visualization Builder")

if "data" not in st.session_state:
    st.warning("Upload dataset first")
    st.stop()

df = st.session_state["data"]

chart = st.selectbox(
    "Select visualization",
    [
        "Histogram",
        "Scatter",
        "Box Plot",
        "Line Chart",
        "Bar Chart",
        "Correlation Heatmap"
    ]
)

num = df.select_dtypes("number").columns

if chart == "Histogram":

    col = st.selectbox("Variable", num)

    fig = px.histogram(df, x=col)

    st.plotly_chart(fig, use_container_width=True)


elif chart == "Scatter":

    x = st.selectbox("X", num)
    y = st.selectbox("Y", num)

    fig = px.scatter(df, x=x, y=y)

    st.plotly_chart(fig, use_container_width=True)


elif chart == "Box Plot":

    col = st.selectbox("Variable", num)

    fig = px.box(df, y=col)

    st.plotly_chart(fig, use_container_width=True)


elif chart == "Line Chart":

    x = st.selectbox("X axis", df.columns)
    y = st.selectbox("Y axis", num)

    fig = px.line(df, x=x, y=y)

    st.plotly_chart(fig, use_container_width=True)


elif chart == "Bar Chart":

    x = st.selectbox("Category", df.columns)
    y = st.selectbox("Value", num)

    fig = px.bar(df, x=x, y=y)

    st.plotly_chart(fig, use_container_width=True)


elif chart == "Correlation Heatmap":

    fig = px.imshow(df.corr())

    st.plotly_chart(fig, use_container_width=True)