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

## stramlit page title

st.title(" 🥂 HomeMaded AI Chatbot")
##display chat history 

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
       st.markdown(message['content'])


## input field for user message

user_prompt=st.chat_input("ASK GPT-4o....")
if user_prompt:
    ## add user msh to chat history and display it

    st.chat_message('user').markdown(user_prompt)
    st.session_state.chat_history.append({'role':'user','content':user_prompt})



    #send user msg to gpt and get msg
    response=openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"system","content":"you are an expert annd a helpful assistant"},
            *st.session_state.chat_history
        ]
    )



    assistant_response=response.choices[0].message.content
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})

    ## display response

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
    