from langgraph.graph import StateGraph, END
from typing import Dict, Any

class RagWorkflow:
    def __init__(self, embedder, store):
        self.embedder = embedder
        self.store = store
        self.chain = self._build()

    def _retrieve(self, state: Dict[str, Any]) -> Dict[str, Any]:
        question = state["question"]
        vector = self.embedder.embed(question)
        state["context"] = self.store.search(vector, limit=2)
        return state

    def _answer(self, state: Dict[str, Any]) -> Dict[str, Any]:
        ctx = state.get("context", [])
        if ctx:
            state["answer"] = f"I found this: '{ctx[0][:100]}...'"
        else:
            state["answer"] = "Sorry, I don't know."
        return state

    def _build(self):
        graph = StateGraph(dict)
        graph.add_node("retrieve", self._retrieve)
        graph.add_node("answer", self._answer)
        graph.set_entry_point("retrieve")
        graph.add_edge("retrieve", "answer")
        graph.add_edge("answer", END)
        return graph.compile()

    def run(self, question: str) -> Dict[str, Any]:
        return self.chain.invoke({"question": question})
