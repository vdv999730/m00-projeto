FROM python:3.12-slim

WORKDIR /app

# Copia todos os arquivos do backend (inclui requirements.txt e pasta app)
COPY . /app/

# Garante que está copiando para /app/app
RUN if [ ! -d "app" ]; then echo "ERRO: Pasta 'app' não copiada corretamente para o container"; exit 1; fi

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000", "--reload"]
