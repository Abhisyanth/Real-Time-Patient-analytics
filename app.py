import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

st.set_page_config(layout = "wide", page_title = "Patient Analytics Pro", page_icon = "🏥", initial_sidebar_state = "expanded")

from langchain_groq import ChatGroq

load_dotenv()

my_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key = my_key,
    model_name = "llama-3.3-70b-versatile"
)

@st.cache_data
def load_data():
    df = pd.read_csv("dataset.csv")
    return df

st.title("Real-Time Patient Analysis")
st.markdown("------------------")

df = load_data()

st.sidebar.title("Dashboard Controls")
selected_icu = st.sidebar.selectbox("Choose ICU Department", df['icu_type'].unique())

filtered_df = df[df['icu_type'] == selected_icu]

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Patients in Dept", len(filtered_df))
with col2:
    mortality = filtered_df['hospital_death'].mean() * 100
    st.metric("Dept. Mortality Rate", f"{mortality:.2f}%")
with col3:
    wait = filtered_df['pre_icu_los_days'].mean()
    st.metric("Avg Wait (Days)", f"{wait:.2f}")


st.subheader(f"Raw Data for {selected_icu}")
st.dataframe(filtered_df.head(10))