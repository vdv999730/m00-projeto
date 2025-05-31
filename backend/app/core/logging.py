import logging
from logging.handlers import RotatingFileHandler
import os

# Diretório para armazenar logs
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_LOG_DIR = os.path.join(BASE_DIR, "backend_logs")
LOG_DIR = os.getenv("LOG_DIR", DEFAULT_LOG_DIR)

os.makedirs(LOG_DIR, exist_ok=True)

# Configuração básica do logger
logger = logging.getLogger("m00-backend")
logger.setLevel(logging.INFO)

# Handler de rotação: 5 arquivos de 5MB cada
file_handler = RotatingFileHandler(
    filename=os.path.join(LOG_DIR, "backend.log"),
    maxBytes=5 * 1024 * 1024,
    backupCount=5,
    encoding="utf-8",
)
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
