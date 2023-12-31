import streamlit as st
import random
import time
st.sidebar.success("User Input History")
st.write("<h4 style='text-align: center; border-radius: 10px; background-color:lightgray;'>Simple User Input Bot</h4>", unsafe_allow_html=True)




prompt = st.chat_input("How can i help you?")

# Initialize the data list in session state
if 'data' not in st.session_state:
    st.session_state.data = []

if 'messages' not in st.session_state:
    st.session_state.messages = []




if 'count' not in st.session_state:
    st.session_state.count = 1


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


    


# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.session_state.data.append(f"👤: {prompt}")
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.sidebar.write(st.session_state.data)


