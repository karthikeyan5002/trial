import streamlit as st
import pandas as pd

st.title("Welcome to Streamlit")

df = pd.read_csv("./water_potability.csv")

st.dataframe(df)