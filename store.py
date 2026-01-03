from abc import ABC, abstractmethod
from typing import List
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

class DocumentStore(ABC):
    @abstractmethod
    def add(self, doc_id: int, vector: List[float], text: str) -> None:
        pass

    @abstractmethod
    def search(self, vector: List[float], limit: int) -> List[str]:
        pass


class InMemoryDocumentStore(DocumentStore):
    def __init__(self):
        self._docs: List[str] = []

    def add(self, doc_id: int, vector: List[float], text: str) -> None:
        self._docs.append(text)

    def search(self, vector: List[float], limit: int) -> List[str]:
        return self._docs[:limit] if self._docs else []


class QdrantDocumentStore(DocumentStore):
    def __init__(self, url: str, collection: str, vector_size: int):
        self.client = QdrantClient(url)
        self.collection = collection
        self.client.recreate_collection(
            collection_name=collection,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

    def add(self, doc_id: int, vector: List[float], text: str) -> None:
        self.client.upsert(
            collection_name=self.collection,
            points=[
                PointStruct(
                    id=doc_id,
                    vector=vector,
                    payload={"text": text}
                )
            ]
        )

    def search(self, vector: List[float], limit: int) -> List[str]:
        hits = self.client.search(
            collection_name=self.collection,
            query_vector=vector,
            limit=limit
        )
        return [hit.payload["text"] for hit in hits]