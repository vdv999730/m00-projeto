# Usar uma imagem base Python
FROM python:3.12-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar o código da aplicação
COPY ./backend/app /app

# Copiar o arquivo requirements.txt que está dentro da pasta backend
COPY ./backend/requirements.txt /app

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta
EXPOSE 10000

# Comando para rodar o backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
