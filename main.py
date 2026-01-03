from fastapi import FastAPI
from embeddings import EmbeddingService
from store import InMemoryDocumentStore, QdrantDocumentStore
from rag import RagWorkflow
from api import create_router

app = FastAPI(title="Learning RAG Demo")

embedder = EmbeddingService()

try:
    store = QdrantDocumentStore(
        url="http://localhost:6333",
        collection="demo_collection",
        vector_size=embedder.VECTOR_SIZE
    )
    using_qdrant = True
except Exception:
    store = InMemoryDocumentStore()
    using_qdrant = False

rag = RagWorkflow(embedder, store)
app.include_router(create_router(rag, embedder, store))