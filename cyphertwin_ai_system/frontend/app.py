# Streamlit app: GPT UI and dashbaords 
# Ask natural questions (e.g., “Show servers with outdated patches”)
# Render insights from Memgraph
# Display daily agent summary

import streamlit as st 
import requests 

st.title("CypherTwin AI - Ask GPT")

token = st.text_input("Auth Token", type="password")
question = st.text_input("Ask a question about your cyber assets: ")

if st.button("Submit"):
    response = requests.post("https://localhost:800/ask"), json={"question" : question, "token" : token}
    st.write(response.json)