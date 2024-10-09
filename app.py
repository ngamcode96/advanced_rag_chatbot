import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.title("Advanced RAG App Multi sources")
st.subheader("PDF, Web page, Video, Audio, txt, ...")
pg = st.navigation([st.Page("add_documents.py", title="Add document", icon="1️⃣"), st.Page("chatbot.py", title="Chat with documents", icon="2️⃣")])
pg.run()
