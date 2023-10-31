from fastapi import FastAPI
from core.config import settings
app=FastAPI(title=settings.PROJECT_TITLE,version=settings.PEROJECT_VERSION)


@app.get("/")
def Hello_api():
    return {"deteails":"Hello world"}
