from typing import Protocol

class PaymentProvider(Protocol):
    async def create_payment(self, amount: float, currency: str, **kwargs) -> dict: ...

class StripeProvider:
    async def create_payment(self, amount: float, currency: str, **kwargs) -> dict:
        return {"id": "stripe_mock", "amount": amount, "currency": currency, "status": "succeeded"}

class MercadoPagoProvider:
    async def create_payment(self, amount: float, currency: str, **kwargs) -> dict:
        return {"id": "mp_mock", "amount": amount, "currency": currency, "status": "approved"}

providers = {
    "stripe": StripeProvider(),
    "mercadopago": MercadoPagoProvider()
}
