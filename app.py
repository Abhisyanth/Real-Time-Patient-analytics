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

# Build a summary to feed the AI
context = f"""
The user is looking at the {selected_icu} department.
- Total Patients: {len(filtered_df)}
- Mortality Rate: {mortality:.2f}%
- Average Wait Time: {wait:.2f} days
"""
# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat history from the list
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# The Clear Conversation button
if st.sidebar.button(" Clear Conversation"):
    st.session_state.messages = []
    
    st.rerun()

# Capture new user input
if user_question := st.chat_input("Ask a question about this ICU department..."):

 
    # Add user message to history and display it
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    # Process the response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_placeholder.markdown(" *Analyzing ICU metrics...*")
        
        # Build the prompt with context
        full_prompt = f"""
        You are a professional medical data analyst.   
        
        Current ICU Statistics for reference:
        {context}

        Conversation History:
        {st.session_state.messages[-3:]} 

        User Question: {user_question}
        
        Instruction: If the user is just saying thanks or greeting you, respond naturally. 
        If they ask about data, use the statistics above to provide a concise, data-driven answer.
        """
        
        try:
            # This creates a stream instead of a single block
            full_response = ""
            for chunk in llm.stream(full_prompt):
                full_response += chunk.content
                response_placeholder.markdown(full_response + "▌")
            
            # Final clean display
            response_placeholder.markdown(full_response)
            
            # Add assistant message to history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Connection Error: {e}")

