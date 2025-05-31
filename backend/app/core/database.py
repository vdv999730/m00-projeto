import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ler a URL do banco de variáveis de ambiente (sem valor padrão)
DATABASE_URL = os.getenv("DATABASE_URL")

# Criar engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Criar SessionLocal para gerar sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos
Base = declarative_base()

# Dependência para injetar a sessão no FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
