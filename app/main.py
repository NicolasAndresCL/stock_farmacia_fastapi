from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.core.paths import BASE_DIR
from app.core.logger import logger
from app.routers import ui


# ===============================
# App initialization
# ===============================
app = FastAPI(
    title="Stock App",
    description="Sistema de cálculo de stock de medicamentos",
    version="0.1.0"
)

logger.info("Starting Stock App")

# ===============================
# Static files
# ===============================
STATIC_DIR = BASE_DIR / "app" / "static"

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
    logger.info(f"Static files mounted from {STATIC_DIR}")
else:
    logger.warning(f"Static directory not found: {STATIC_DIR}")

# ===============================
# Routers
# ===============================
app.include_router(ui.router)
