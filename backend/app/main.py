from fastapi import FastAPI

app = FastAPI(title="Retail Inventory Alerts")

@app.get("/")
def health():
    return {"status": "ok"}