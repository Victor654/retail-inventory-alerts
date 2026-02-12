from fastapi import FastAPI
from app.auth.router import router as auth_router

app = FastAPI(title="Retail Inventory Alerts")

app.include_router(auth_router)

@app.get("/")
def health():
    return {"status": "ok"}
