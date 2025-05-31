FROM python:3.12-slim

# Definir diretório de trabalho e PYTHONPATH
WORKDIR /m00project
ENV PYTHONPATH=/code

# Copiar e instalar dependências
COPY requirements.txt .  # <-- ajustado aqui
RUN pip install --no-cache-dir -r requirements.txt

# Copiar só o necessário
COPY app ./app
COPY pytest.ini .

# Expor porta
EXPOSE 10000

# Comando padrão para iniciar o FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000", "--reload"]
