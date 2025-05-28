# =======================
# 🚫 Versão anterior (errada)
#FROM python:3.12-slim

#WORKDIR /app

# Copia código
#COPY ./app /app

# Copia requirements
#COPY ./requirements.txt /app

# Instala dependências
#RUN pip install --no-cache-dir -r requirements.txt

#EXPOSE 10000

# Comando para rodar o backend
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
# =======================

# ✅ Dockerfile correto
FROM python:3.12-slim

WORKDIR /app

COPY ./app /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
