import streamlit as st
from vega_datasets import data
import matplotlib.pyplot as plt

source = data.cars()



if st.button("Call API"):
    st.balloons()

st.header("Visualization")

st.subheader("Matplotlib")

plt.figure(figsize=(12,8))
plt.scatter(source['Horsepower'], source['Miles_per_Gallon'])
st.pyplot(plt)