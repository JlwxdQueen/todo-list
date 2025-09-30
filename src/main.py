from fastapi import FastAPI
from config.settings import settings
from routers import todo

app = FastAPI(title=settings.app_name, version=settings.api_version)

app.include_router(todo.router)

@app.get("/")
async def root():
    return {"message": f"welcome to {settings.app_name}"}
