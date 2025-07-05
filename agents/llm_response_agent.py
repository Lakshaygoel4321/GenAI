from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq
from langchain_core.documents import Document

from dotenv import load_dotenv
import os

load_dotenv()

class LLMResponseAgent:
    def __init__(self):
        self.name = "LLMResponseAgent"
        self.llm = ChatGroq(model="Gemma2-9b-it",api_key=os.getenv("GROQ_API_KEY"))
        self.prompt = ChatPromptTemplate.from_template("""
        🧠 Use the context below to answer the question:
        <context>
        {context}
        </context>
        Question: {input}
        """)

    def handle(self, mcp_msg):
    
        context = mcp_msg.payload["top_chunks"]
        query = mcp_msg.payload["query"]

        
        documents = [Document(page_content=chunk) for chunk in context]

        chain = create_stuff_documents_chain(self.llm, self.prompt)

    
        answer_text = chain.invoke({"input": query, "context": documents})

        return {
            "sender": self.name,
            "receiver": "UI",
            "type": "ANSWER",
            "trace_id": mcp_msg.trace_id,
            "payload": {
                "answer": answer_text,
                "context": context
            }
        }