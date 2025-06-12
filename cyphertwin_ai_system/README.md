# CyberTwin AI

A secure, AI-driven cyber health check and Digital Twin insight tool using GPT, Langflow, and Memgraph.

## Features
- Langflow-powered autonomous agent
- Streamlit GPT UI to ask security questions
- Alerts for risky findings
- Secure design principles

## Tech
Python · FastAPI · Streamlit · Memgraph · Langflow · JWT

## Run
streamlit run frontend/app.py
uvicorn backend.api:app --reload

## Auth
Use JWT token: `{"username": "analyst", "role": "read"}`