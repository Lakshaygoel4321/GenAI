from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['HF_TOKEN'] = os.getenv("HF_TOKEN")

class RetrievalAgent:
    def __init__(self):
        self.name = "RetrievalAgent"
        self.embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2",
                                                     model_kwargs={"device": "cpu"})
        self.vectorstore = None

    def build_index(self, chunks):
        self.vectorstore = FAISS.from_documents(chunks, self.embedding_model)

    def query(self, query_text):
        retriever = self.vectorstore.as_retriever()
        return retriever.get_relevant_documents(query_text)

    def handle(self, mcp_msg):
        if mcp_msg.type == "DOC_CHUNKS":
            self.build_index(mcp_msg.payload["chunks"])
            return {
                "sender": self.name,
                "receiver": "LLMResponseAgent",
                "type": "READY",
                "trace_id": mcp_msg.trace_id,
                "payload": {}
            }

        elif mcp_msg.type == "QUERY":
            top_chunks = self.query(mcp_msg.payload["query"])
            return {
                "sender": self.name,
                "receiver": "LLMResponseAgent",
                "type": "CONTEXT_RESPONSE",
                "trace_id": mcp_msg.trace_id,
                "payload": {
                    "top_chunks": [doc.page_content for doc in top_chunks],
                    "query": mcp_msg.payload["query"]
                }
            }
