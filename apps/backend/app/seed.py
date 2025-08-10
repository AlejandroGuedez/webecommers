import asyncio
from .core.database import AsyncSessionLocal, engine
from .models import Base, Tenant, User, Product, ProductVariant, Price
from .core.security import get_password_hash

async def seed():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSessionLocal() as db:
        tenant = Tenant(name="Demo", domains=["demo.localhost"], currency="ARS", locale="es-AR")
        db.add(tenant)
        await db.flush()
        admin = User(email="owner@demo.local", password_hash=get_password_hash("secret"), role="owner", tenant_id=tenant.id)
        db.add(admin)
        product = Product(title="Producto Demo", slug="producto-demo", tenant_id=tenant.id)
        db.add(product)
        await db.flush()
        variant = ProductVariant(product_id=product.id, sku="SKU1", tenant_id=tenant.id)
        db.add(variant)
        price = Price(variant_id=variant.id, amount=1000, currency="ARS", tenant_id=tenant.id)
        db.add(price)
        await db.commit()

if __name__ == "__main__":
    asyncio.run(seed())
