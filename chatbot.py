import streamlit as st
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from utils import custom_prompt
from langchain_groq import ChatGroq
from langchain.schema import (
    SystemMessage,
    HumanMessage
    )

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

st.subheader('Chat with document')

collection = st.selectbox(
    "Choose a collection",
    ("safe_dev"),
)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name=collection,
    url="http://localhost:6333",
)

llama_3 = ChatGroq(temperature=0, model_name="llama-3.1-70b-versatile")


messages = [
    SystemMessage(content="You are a helpful assistant. You will answer the questions and give correct answer based on the context. After answering the question, give the context where you find it"),
]

query = st.text_area(label="Ask your question...")
    
btn_submit = st.button("Send")

if btn_submit:
    prompt = HumanMessage(
    content=custom_prompt(qdrant=qdrant, query=query)
    )
    messages.append(prompt)
    res = llama_3.invoke(messages)
    st.write(res.content)
