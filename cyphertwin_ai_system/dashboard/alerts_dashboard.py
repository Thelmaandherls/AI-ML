# Displays high-risk issues
import streamlit as st 
import json 

st.title("Cyber Alerts")

with open("alerts.json") as f:
    alerts = json.load(f)

for alert in alerts:
    st.error(f"{alerts['severity'].upper()}: {alert['msg']}")