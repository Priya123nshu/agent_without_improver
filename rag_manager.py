import os
import uuid
import json
from typing import List, Dict
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


class RAGManager:
    """Simplified Corrective RAG System"""

    def __init__(self, persist_dir: str = "./rag_memory"):
        self.persist_dir = persist_dir
        self.embeddings = embedding_model
        self.db = Chroma(
            collection_name="corrective_memory",
            embedding_function=self.embeddings,
            persist_directory=persist_dir
        )

    def add_corrective_insight(self, insight_package: Dict):
        """Store the entire insight as one paragraph."""
        try:
            paragraph = json.dumps(insight_package, indent=2)
            self.db.add_texts(
                texts=[paragraph],
                metadatas=[{"session_id": insight_package.get("session_id")}],
                ids=[str(uuid.uuid4())]
            )
            self.db.persist()
            print(f"Insight stored for session: {insight_package.get('session_id')}")
            return {"status": "stored", "session_id": insight_package.get("session_id")}
        except Exception as e:
            print(f"Error storing insight: {e}")
            return {"status": "failed", "error": str(e)}

    def fetch_context(self, query: str, k: int = 3) -> List[Dict]:
        """Retrieve relevant paragraphs."""
        try:
            results = self.db.similarity_search_with_score(query, k=k)
            contexts = [{"text": doc.page_content, "similarity": score} for doc, score in results]
            return contexts
        except Exception as e:
            print(f"Error fetching context: {e}")
            return []

    def clear_memory(self, confirm=False):
        if confirm:
            self.db.delete_collection()
            print("Memory cleared.")
        else:
            print("Pass confirm=True to clear memory.")
