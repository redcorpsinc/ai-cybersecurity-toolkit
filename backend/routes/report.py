from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()
REPORTS_DIR = "backend/reports/output"


@router.get("/")
def list_reports():
    """
    Lists all reports available in the reports directory
    """
    try:
        files = os.listdir(REPORTS_DIR)
        reports = [f for f in files if f.endswith((".pdf", ".html"))]
        return {"reports": reports}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list reports: {str(e)}")


@router.get("/{filename}")
def get_report(filename: str):
    """
    Downloads a report by filename
    """
    file_path = os.path.join(REPORTS_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Report not found")

    media_type = "application/pdf" if filename.endswith(".pdf") else "text/html"
    return FileResponse(path=file_path, filename=filename, media_type=media_type)
