import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import random
import time

st.set_page_config(page_title='chatbot', page_icon='🤖')
st.markdown("# Robot ")
st.sidebar.markdown("# Robot ")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"]) 
        
# Streamed response emulator
def response_generator():
    response = random.choice(
        ["Hello there! How can I assist you today?",
        "Hi! Is there anything I can help you with?",
        "Do you need help?",])
    for word in response.split():
        yield word + " "
        time.sleep(random.randint(5,15)/1000)

prompt = st.chat_input("Say something")
if prompt:
    response_generator()

@st.cache_data
def load_data(url):
    df = pd.read_csv(url) # Download the data
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)
