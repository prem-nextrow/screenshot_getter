from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/cdn/{filepath:path}")
async def serve_static_assets(filepath: str):
    """
    Serve static files from the output directory
    """
    file_path = os.path.join("output", filepath)
    
    if not os.path.exists(file_path):
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(file_path)