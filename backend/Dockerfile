FROM python:3.12-slim

WORKDIR /app

# Copia tudo
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r backend/app/requirements.txt

EXPOSE 10000

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "10000"]
