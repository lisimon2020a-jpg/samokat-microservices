from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI(title="Samokat API Gateway")

USERS_URL = "http://localhost:5001"
PRODUCTS_URL = "http://localhost:5002"
ORDERS_URL = "http://localhost:5003"

@app.get("/users")
async def get_users():
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{USERS_URL}/users")
            return r.json()
    except Exception:
        raise HTTPException(status_code=503, detail="Users service unavailable")

@app.get("/products")
async def get_products():
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{PRODUCTS_URL}/products")
            return r.json()
    except Exception:
        raise HTTPException(status_code=503, detail="Products service unavailable")

@app.get("/orders")
async def get_orders():
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{ORDERS_URL}/orders")
            return r.json()
    except Exception:
        raise HTTPException(status_code=503, detail="Orders service unavailable")

@app.post("/orders")
async def create_order(order: dict):
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{ORDERS_URL}/orders", json=order)
            return r.json()
    except Exception:
        raise HTTPException(status_code=503, detail="Orders service unavailable")