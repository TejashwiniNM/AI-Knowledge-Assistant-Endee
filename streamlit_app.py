import streamlit as st
from src.search import search

st.title("AI Knowledge Assistant")
st.write("Ask questions based on the knowledge base")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Enter your question")

if query:
    answer = search(query)
    st.markdown(f"**AI:** {answer}")
    st.session_state.chat_history.append(("You", query))
    st.session_state.chat_history.append(("AI", answer))

for role, text in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**AI:** {text}")