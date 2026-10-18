"""Minimal API scaffold for OpenProcessAI's development phase."""

from fastapi import FastAPI

app = FastAPI(
    title="OpenProcessAI API",
    version="0.1.0",
    description="Early API scaffold; product endpoints are specified in docs/API_SPECIFICATION.md.",
)


@app.get("/health", tags=["operations"])
def health() -> dict[str, str]:
    """Return a basic health response."""
    return {"status": "ok", "project": "OpenProcessAI"}
