import streamlit as st
import pandas as pd
import json

st.title("Export & Report")

if "data" not in st.session_state:
    st.warning("Upload data first.")
    st.stop()

df = st.session_state["data"]

st.subheader("Download Clean Dataset")

csv = df.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    "clean_dataset.csv",
    "text/csv"
)

st.subheader("Transformation Report")

log = st.session_state.get("transform_log", [])

st.write(log)

report = json.dumps(log, indent=2)

st.download_button(
    "Download Report",
    report,
    "transform_report.json"
)