import streamlit as st
from groq import Groq

st.title("AI Hackathon Chatbot 🤖")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# input box
user_input = st.chat_input("Type a message...")

# only run when user types something
if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)
