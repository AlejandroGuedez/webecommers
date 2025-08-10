import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.core.database import Base, engine

@pytest_asyncio.fixture(scope="module", autouse=True)
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_register_and_login():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post("/auth/register", json={"email":"test@test.com","password":"123","tenant_id":1})
        assert resp.status_code == 200
        token = resp.json()["access_token"]
        assert token
        resp = await ac.post("/auth/login", json={"email":"test@test.com","password":"123","tenant_id":1})
        assert resp.status_code == 200
