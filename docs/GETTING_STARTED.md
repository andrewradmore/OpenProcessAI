# Getting Started

## Prerequisites

- Python 3.11 or later.
- Git.
- A virtual environment tool such as `venv`.

The frontend and database are described in the architecture but are not scaffolded in this initial documentation package.

## Run the API scaffold

```bash
git clone <your-repository-url>
cd OpenProcessAI
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -e '.[dev]'
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/health` for the health response and `http://127.0.0.1:8000/docs` for the automatically generated API docs.

## Run tests

```bash
pytest
```

## Important limitations

This repository contains an initial documentation package and a minimal API scaffold. Project management, document ingestion, process extraction, persistence, authentication, AI provider integrations, graph editing and agent specification workflows have not yet been implemented. Do not deploy this scaffold as a production service.
