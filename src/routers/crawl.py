import os
import sys
from fastapi import APIRouter, HTTPException, Request
import traceback

# Dynamically add the project root directory to sys.path
current_file_path = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(current_file_path, "../../.."))
print(f"Project_root {project_root}")
if project_root not in sys.path:
    sys.path.append(project_root)

from src.schemas.api.scg import CrawlRequest, CrawlResponse
from src.services.crawler_service import run_crawler

router = APIRouter()

@router.post("/crawl", response_model=CrawlResponse)
async def crawl(crawl_request: CrawlRequest, request: Request):
    """
    Crawl a URL and return PDFs and media files found
    """
    try:        
        # Now we can await the async crawler
        result = await run_crawler(str(crawl_request.url))
        
        # Build base CDN URL
        base_cdn = f"{request.url.scheme}://{request.url.netloc}/cdn"

        response_data = CrawlResponse(
            status="done",
            pdf_list=[
                {"name": p["name"], "url": f"{base_cdn}/{p['src']}"} 
                for p in result['pdfs']
            ],
            media_files=[
                {"type": m["type"], "url": f"{base_cdn}/{m['src']}"} 
                for m in result['media']
            ]
        )
        
        return response_data
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))