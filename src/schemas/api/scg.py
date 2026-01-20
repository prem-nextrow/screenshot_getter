# schemas.py
from pydantic import BaseModel, HttpUrl
from typing import List

class CrawlRequest(BaseModel):
    url: HttpUrl

class PDFItem(BaseModel):
    name: str
    url: str

class MediaItem(BaseModel):
    type: str
    url: str

class CrawlResponse(BaseModel):
    status: str
    pdf_list: List[PDFItem]
    media_files: List[MediaItem]

class ErrorResponse(BaseModel):
    error: str