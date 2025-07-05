# 🦜 Agentic RAG Chatbot for Multi-Format Document QA

A powerful Retrieval-Augmented Generation (RAG) chatbot with an **Agentic Architecture** using **Model Context Protocol (MCP)** for clean, modular agent communication.  

This project lets you upload documents in multiple formats, embed them, and interactively ask questions—all powered by modern embeddings and LLMs.

---

## 🚀 Features

✅ **Multi-format Document Ingestion**
- PDF
- DOCX
- CSV
- PPTX
- TXT / Markdown

✅ **Agentic Architecture**
- **IngestionAgent**: Parses and splits documents.
- **RetrievalAgent**: Embeds and retrieves chunks semantically.
- **LLMResponseAgent**: Generates context-aware answers.

✅ **Model Context Protocol (MCP)**
- Standardized message passing between agents.

✅ **Streamlit User Interface**
- Upload and embed documents.
- Ask multi-turn questions.
- View answers and their context.

✅ **Vector Store & Embeddings**
- FAISS as the vector database.
- HuggingFace Sentence Transformers for embeddings.

---

## 📂 Project Structure

.
├── app.py # Main Streamlit app
├── .env # Environment variables
├── agents/
│ ├── init.py
│ ├── ingestion_agent.py # Document parsing
│ ├── retrieval_agent.py # Embeddings and retrieval
│ ├── llm_response_agent.py # LLM answer generation
│ └── mcp.py # Model Context Protocol classes
├── temp/ # Uploaded files


---

## 🛠️ Installation

**1️⃣ Clone this repository**

```bash
git clone https://github.com/yourusername/agentic-rag-chatbot.git
cd agentic-rag-chatbot

** 2️⃣ Create a virtual environment
python -m venv .venv
# Activate:
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

**3️⃣ Install dependencies
pip install -r requirements.txt

**🔑 Environment Variables
Create a .env file in your project root:
HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_GROQ_api_key_if_needed

🏃 Usage
Run the app locally:
streamlit run app.py
