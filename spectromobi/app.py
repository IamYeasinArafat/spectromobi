from fastapi import FastAPI
from spectromobi import AppConfig
from spectromobi.api.v1 import routes

app = FastAPI()

app.include_router(routes.router)


@app.get("/")
async def root():
    return {"message": f"Hello from {AppConfig.app_name}"}