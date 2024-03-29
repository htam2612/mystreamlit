import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("Map")
df = pd.DataFrame(np.random.randn(500, 2) / [50 / 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
