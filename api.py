import time
from fastapi import APIRouter, HTTPException
from models import QuestionRequest, DocumentRequest

def create_router(rag, embedder, store):
    router = APIRouter()

    @router.post("/ask")
    def ask(req: QuestionRequest):
        start = time.time()
        try:
            result = rag.run(req.question)
            return {
                "question": req.question,
                "answer": result["answer"],
                "context_used": result.get("context", []),
                "latency_sec": round(time.time() - start, 3)
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.post("/add")
    def add(req: DocumentRequest):
        try:
            doc_id = int(time.time() * 1000)
            vector = embedder.embed(req.text)
            store.add(doc_id, vector, req.text)
            return {"id": doc_id, "status": "added"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.get("/status")
    def status():
        return {"graph_ready": True}

    return router