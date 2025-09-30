from fastapi import FastAPI
from config.settings import settings

app = FastAPI(title=settings.app_name, version=settings.api_version)


@app.get("/")
async def root():
    return {"message": f"welcome to {settings.app_name}"}
