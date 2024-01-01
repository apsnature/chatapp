import google.generativeai as genai
import streamlit as st
# from dotenv import load_dotenv
import os


# load_dotenv()
st.markdown("""
<style>
    .centered {
        text-align: center;
            font-weight: bold;
            font-size:24px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="centered">AI-Powered Chat Companion by Shahid</div>', unsafe_allow_html=True)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How I can assist you today?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.markdown(prompt)

# Assistant message one time
    # response = model.generate_content(prompt)
    # with st.chat_message("assistant"):
    #     st.session_state.messages.append({"role": "assistant", "content": response.text})
    #     st.markdown(response.text)
        

# Assistant message stream (in chunks)
    try:
        response = model.generate_content(prompt, stream=True)
        with st.chat_message("assistant"):
            fullresponse = ""
            for chunk in response:
                fullresponse += chunk.text
                st.markdown(chunk.text)

        st.session_state.messages.append({"role": "assistant", "content": fullresponse})
    
    except:
        st.subheader("Oh My Bad! Please try again! :500")
