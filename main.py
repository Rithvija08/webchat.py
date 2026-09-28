import streamlit as st
from ollama import chat

st.title("My AI Bot: Synora")
name = "Rithvija"
st.write("Welcome, ",name)
question = st.text_input("Ask a question")
if st.button("Ask"):
    st.write("you asked: ",question)
    response = chat(model = "gemma3:1b",messages=[
        {
             "role": "system", 
             "content": "You are a friendly tutor. you explain concepts in avery simple way. explain concepts in a very simple way Explain in 50 words max."
        },
        {
            "role": "user",
            "content": question
        }
    ])
    answer = response.message.content
    st.write(answer)