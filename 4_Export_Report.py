import streamlit as st
import pandas as pd

st.title("Export Processed Data")

if "data" not in st.session_state:

    st.warning("No dataset available.")

else:

    df = st.session_state["data"]

    st.subheader("Preview")

    st.dataframe(df.head())

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Clean Dataset",
        data=csv,
        file_name="clean_dataset.csv",
        mime="text/csv"
    )

    st.success("Dataset ready for export")