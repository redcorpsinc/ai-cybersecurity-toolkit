import pytest
from httpx import AsyncClient
from fastapi import status
from backend.main import app  # Adjust if your entrypoint is different

@pytest.mark.asyncio
async def test_docs_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/docs")
        assert response.status_code == status.HTTP_200_OK
