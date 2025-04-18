import os
import json
import streamlit as st
import openai


## config open ai api

working_dir=os.path.dirname(os.path.abspath(__file__))
config_data=json.load(open(f"{working_dir}/config.json"))

OPEN_AI_KEY=config_data["OPEN_AI_API_KEY"]
openai.api_key=OPEN_AI_KEY


## config streamlit page

st.set_page_config(
    page_title="ChaDbot",
    page_icon="🌚",
    layout="centered",
)

## initialize the chat session in streamlit if not present

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


