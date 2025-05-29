FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos para manter a estrutura app/
COPY ./app /app/app
COPY requirements.txt /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Inicia o servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000", "--reload"]
