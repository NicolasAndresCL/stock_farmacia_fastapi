from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.core.paths import BASE_DIR
from app.core.logger import logger

# ===============================
# App initialization
# ===============================
app = FastAPI(
    title="Stock App",
    description="Sistema de cálculo de stock de medicamentos",
    version="0.1.0"
)

# ===============================
# Paths
# ===============================
TEMPLATES_DIR = BASE_DIR / "app" / "templates"
STATIC_DIR = BASE_DIR / "app" / "static"

# ===============================
# Static files & templates
# ===============================
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# ===============================
# Routes (temporary here)
# ===============================
@app.get("/")
async def home(request: Request):
    logger.info("Home page loaded")
    return templates.TemplateResponse(
        "upload.html",
        {"request": request}
    )
