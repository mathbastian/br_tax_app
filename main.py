import streamlit as st
import pandas as pd

data = pd.read_csv("./data/brazilian_tax_revenue.csv", delimiter=";")
filtered_data = data[data["State"].isin(['RS', 'SC', 'PR'])]

st.set_page_config("Brazilian tax",layout="wide")
st.title("Brazilian tax")

st.header("Individual Income Tax over the years:", divider=True)
st.bar_chart(data=filtered_data, x="Year", y="Individual Income Tax", color="State", stack="layered")