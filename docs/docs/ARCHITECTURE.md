EduMind AI — System Architecture
Overview
EduMind AI is designed as a multi-phase project evolving from a simple static Q&A system into a full AI-powered tutoring platform.
Phase 1: Beta (Current)
User Browser
    │
    ▼
index.html (GitHub Pages)
    │
    ▼
app.js (keyword matching in-browser)
    │
    ▼
knowledge_base.json (static data)
Technology Stack:
Frontend: HTML5, CSS3, Vanilla JavaScript
Backend: None (fully static, runs on GitHub Pages)
Data: JSON knowledge base
Hosting: GitHub Pages (free)
Phase 2: NLP Integration (Planned)
User Browser
    │  HTTPS
    ▼
Flask REST API (Python)
    │
    ├── NLTK Preprocessing
    ├── TF-IDF Vectorizer
    └── Cosine Similarity Matching
    │
    ▼
Expanded Knowledge Base (SQLite)
Phase 3: AI Model (Planned)
User Browser
    │
    ▼
FastAPI Server
    │
    ├── Fine-tuned LLM (DistilBERT / GPT-2)
    ├── RAG (Retrieval-Augmented Generation)
    └── User Session Management
    │
    ▼
PostgreSQL + Vector Database (pgvector)
Data Flow (Beta)
User enters a question in the web UI
JavaScript normalizes and tokenizes the query
Keyword matching scores all knowledge base entries
Best match (score ≥ 3) is returned with metadata
If no match, a helpful fallback message is shown
API Design (Local Dev)
Endpoint
Method
Description
/
GET
Serve main UI
/api/ask
POST
Submit a question
/api/topics
GET
List all subjects
/api/questions
GET
List sample questions
/api/health
GET
System health check
