# RAG Service Refactor

This repository contains a refactored version of a simple Retrieval-Augmented Generation (RAG) service provided as part of a code quality exercise.

The original implementation was intentionally written in a single file with minimal structure.  
The goal of this refactor is **not to add new features**, but to improve code organization, readability, and maintainability while **preserving the original behavior**.

---

## Architecture Overview

The codebase is refactored by separating responsibilities into different Python files while keeping the overall structure simple and flat.  
Each file has a clear role, which helps make the code easier to read, maintain, and extend in the future.

This approach is intentionally lightweight and proportional to the scope of the exercise, avoiding unnecessary complexity.

---

## File Responsibilities

Although the project consists of only a few `.py` files, each file has a distinct responsibility:

- **`api.py`**  
  Handles FastAPI endpoints, HTTP request/response handling, and user input validation.  
  This file focuses only on API communication.

- **`models.py`**  
  Defines Pydantic models used for input validation and request/response data structures.

- **`rag.py`**  
  Contains the main RAG application logic, including document retrieval, answer generation, and workflow orchestration using LangGraph.

- **`embeddings.py`**  
  Provides a service for converting text into embedding vectors, allowing the embedding implementation to be replaced easily in the future.

- **`store.py`**  
  Manages document storage and retrieval, using Qdrant when available and falling back to in-memory storage otherwise.

- **`main.py`**  
  Acts as the application entry point by initializing components, wiring dependencies, and starting the FastAPI app.

---

## Reason for Separation

Each file is separated so it has a single main responsibility:

- API logic → `api.py`  
- Data structure and validation → `models.py`  
- Application flow → `rag.py`  
- Embedding method → `embeddings.py`  
- Data storage → `store.py`  
- Application configuration and wiring → `main.py`

With this separation, changes in one part of the code do not affect other parts.

---

## Conclusion

This refactor focuses on improving internal code quality while keeping the external behavior unchanged.  
The structure is intentionally kept simple, readable, and suitable for the scope of the exercise, without adding new features or unnecessary abstractions.
