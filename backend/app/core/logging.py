import os
import logging
from logging.handlers import RotatingFileHandler

# Define o diretório de logs
# Render não permite escrita em qualquer lugar → /tmp é garantido
DEFAULT_LOG_DIR = os.path.join("/tmp", "backend_logs")
LOG_DIR = os.getenv("LOG_DIR", DEFAULT_LOG_DIR)

# Garante que o diretório exista
os.makedirs(LOG_DIR, exist_ok=True)

# Configuração básica do logger
logger = logging.getLogger("m00-backend")
logger.setLevel(logging.INFO)

# Configuração do Handler de rotação de arquivos
file_handler = RotatingFileHandler(
    filename=os.path.join(LOG_DIR, "backend.log"),
    maxBytes=5 * 1024 * 1024,  # 5MB
    backupCount=5,  # até 5 arquivos de backup
    encoding="utf-8",
)

# Formato dos logs
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
file_handler.setFormatter(formatter)

# Adiciona o handler ao logger
logger.addHandler(file_handler)
