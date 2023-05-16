%%writefile app.py
import streamlit as st

x = st.sliider("Select a value")
st.write(x, "squared is", x * x)
