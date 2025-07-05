import streamlit as st
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent
from agents.mcp import MCPMessage
import os

st.set_page_config("Agentic RAG with MCP", "🤖")

st.title("📄 Agentic RAG Chatbot with MCP")
uploaded_files = st.file_uploader("Upload docs", type=["pdf", "csv", "docx", "pptx", "txt", "md"], accept_multiple_files=True)

if "agents_initialized" not in st.session_state:
    st.session_state.ingestion = IngestionAgent()
    st.session_state.retrieval = RetrievalAgent()
    st.session_state.llm = LLMResponseAgent()
    st.session_state.agents_initialized = True

if uploaded_files:
    file_paths = []
    os.makedirs("temp", exist_ok=True)
    for file in uploaded_files:
        path = f"./temp/{file.name}"
        with open(path, "wb") as f:
            f.write(file.getbuffer())
        file_paths.append(path)

    msg = MCPMessage("UI", "IngestionAgent", "UPLOAD", {"files": file_paths})
    chunks_msg = st.session_state.ingestion.handle(msg)
    ready_msg = st.session_state.retrieval.handle(MCPMessage.from_dict(chunks_msg))
    st.success("✅ Files embedded and vector store is ready.")

user_query = st.text_input("Ask a question from your document")
if st.button("Ask"):
    if user_query:
        query_msg = MCPMessage("UI", "RetrievalAgent", "QUERY", {"query": user_query})
        context_msg = st.session_state.retrieval.handle(query_msg)
        answer_msg = st.session_state.llm.handle(MCPMessage.from_dict(context_msg))

        st.subheader("💬 Answer:")
        st.write(answer_msg["payload"]["answer"])

        st.subheader("🔍 Source Context:")
        for c in answer_msg["payload"]["context"]:
            st.info(c)
