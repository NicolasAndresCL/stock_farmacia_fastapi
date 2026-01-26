from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.core.paths import BASE_DIR
from app.core.logger import logger

# ===============================
# Router configuration
# ===============================
router = APIRouter(tags=["UI"])

# ===============================
# Templates
# ===============================
TEMPLATES_DIR = BASE_DIR / "app" / "templates"
templates = Jinja2Templates(directory=TEMPLATES_DIR)


# ===============================
# Routes
# ===============================
@router.get("/")
async def index(request: Request):
    """
    Home / Landing page
    """
    logger.info("UI: index page loaded")

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )

@router.get("/upload")
async def upload(request: Request):
    """
    Upload Excel files page
    """
    logger.info("UI: upload page loaded")

    return templates.TemplateResponse(
        "upload.html",
        {
            "request": request
        }
    )

from fastapi import UploadFile, File
from typing import List

@router.post("/upload")
async def upload_files(
    request: Request,
    files: List[UploadFile] = File(...)
):
    """
    Receive Excel files and validate upload
    """
    logger.info(f"UI: received {len(files)} file(s)")

    filenames = [file.filename for file in files]

    return templates.TemplateResponse(
        "stock.html",
        {
            "request": request,
            "files": filenames
        }
    )
