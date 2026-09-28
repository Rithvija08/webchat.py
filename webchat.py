import streamlit as st
from ollama import chat

st.title("My AI Chatbot:")
#messages = []
system_messages = "you are a shakespearean tutor. Answer in a sentence of 50 words max."
#messages.append(
#  {
#       "role": "system",
#       "content":system_messages
#   }
#)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": system_messages          
        }
]  

#Display previous messages
for message in st.session_state.messages:
    #Don't display system message
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

question = st.chat_input("Ask a something...")
if question:
    with st.chat_message("user"):
        st.write(question)
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })
    with st.spinner("Thinking..."):
        response = chat(model = "gemma3:1b",messages=st.session_state.messages)
        answer = response.message.content
        with st.chat_message("assistant"):
            st.write(answer)
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )