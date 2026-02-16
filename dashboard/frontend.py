import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

# Page settings
st.set_page_config(page_title="ACME Governance System", page_icon="🛡️")

# Header
st.title("🛡️ NM Company Governance System")
st.caption("AI Compliance Assistant ")

st.divider()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(msg)

# Input box
user_input = st.chat_input("Ask a company policy question...")

if user_input:

    # Show user message
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Thinking indicator
    with st.chat_message("assistant"):
        with st.spinner("Analyzing company policy..."):
            try:
                response = requests.post(API_URL, json={"message": user_input})
                reply = response.json()["reply"]
            except Exception:
                reply = "Backend connection failed. Is FastAPI running?"

            st.markdown(reply)

    st.session_state.messages.append(("assistant", reply))
