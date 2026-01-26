from loguru import logger as _logger
import sys
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

_logger.remove()

_logger.add(
    sys.stdout,
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

_logger.add(
    LOG_DIR / "app.log",
    rotation="1 MB",
    retention="7 days",
    level="INFO"
)

# 👇 ESTO ES CLAVE
logger = _logger
