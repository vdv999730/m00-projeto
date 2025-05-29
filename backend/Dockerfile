FROM python:3.12-slim

WORKDIR /app

# Copia o código da aplicação
COPY ./app /app/app
COPY requirements.txt /app

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define PYTHONPATH para reconhecer o pacote app
ENV PYTHONPATH=/app

# Comando para iniciar o servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000", "--reload"]
