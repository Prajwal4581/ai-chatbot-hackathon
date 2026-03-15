import streamlit as st
from groq import Groq
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

st.title("AI Document Chatbot 🤖")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

# store vector db so we don't recompute every question
if "db" not in st.session_state:
    st.session_state.db = None

if uploaded_file and st.session_state.db is None:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(pages)

    embeddings = HuggingFaceEmbeddings()

    st.session_state.db = FAISS.from_documents(docs, embeddings)

    st.success("PDF processed successfully!")

query = st.chat_input("Ask something about the document")

if query and st.session_state.db:

    with st.chat_message("user"):
        st.write(query)

    results = st.session_state.db.similarity_search(query, k=3)

    context = " ".join([doc.page_content for doc in results])

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.write(answer)
