from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .core.middleware import TenantMiddleware
from .core.database import Base, engine, get_db
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Tenant, User, Product, ProductVariant, Price
from .core.security import verify_password, get_password_hash, create_access_token, create_refresh_token
from pydantic import BaseModel

app = FastAPI(title="Webecommers API")
app.add_middleware(TenantMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class UserCreate(BaseModel):
    email: str
    password: str
    tenant_id: int

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/auth/register", response_model=Token)
async def register(data: UserCreate, db: AsyncSession = Depends(get_db)):
    user = User(email=data.email, password_hash=get_password_hash(data.password), tenant_id=data.tenant_id)
    db.add(user)
    await db.commit()
    access = create_access_token({"sub": str(user.id)})
    refresh = create_refresh_token(str(user.id))
    return Token(access_token=access, refresh_token=refresh)

class Login(BaseModel):
    email: str
    password: str
    tenant_id: int

@app.post("/auth/login", response_model=Token)
async def login(data: Login, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        User.__table__.select().where(User.email == data.email, User.tenant_id == data.tenant_id)
    )
    user = result.fetchone()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access = create_access_token({"sub": str(user.id)})
    refresh = create_refresh_token(str(user.id))
    return Token(access_token=access, refresh_token=refresh)

@app.get("/products")
async def list_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(Product.__table__.select())
    return [dict(r) for r in result.fetchall()]

