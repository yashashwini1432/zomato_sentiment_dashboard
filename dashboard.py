
import streamlit as st
import pandas as pd

st.title("Zomato Review Sentiment Dashboard")

# Load dataset
df = pd.read_csv("zomato_reviews.csv")

# Display data
st.subheader("Customer Reviews Dataset")
st.dataframe(df)

# Show sentiment distribution
st.subheader("Sentiment Distribution")
st.bar_chart(df["Sentiment"].value_counts())
