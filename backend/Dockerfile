FROM python:3.12-slim

# Definir diretório de trabalho e PYTHONPATH
WORKDIR /app
ENV PYTHONPATH=/app

# Copiar e instalar dependências
COPY requirements.txt .  # <-- ajustado aqui
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código do backend
COPY . .

# Expor porta
EXPOSE 10000

# Comando padrão para iniciar o FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000", "--reload"]
