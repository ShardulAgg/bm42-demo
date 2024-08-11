from core import *
from fastapi import APIRouter, File, UploadFile

app_router = APIRouter()

@app_router.get("/")
def health_check():
    return {"status": "ok"}

@app_router.post("/upload_references")
async def file_upload(file: UploadFile = File(...)):
    pass

@app_router.post("/search")
async def search(query: str):
    pass


__all__ = ["app_router"]