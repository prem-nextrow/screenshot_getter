from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routers import crawl, static
import os

from src.routers.crawl import router as crawl_router
from src.routers.static import router as static_router

app = FastAPI(title="Web Crawler API")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(crawl_router)
app.include_router(static_router)

@app.get("/")
async def index():
    """
    Serve the index.html page
    """
    return FileResponse("templates/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=3030)