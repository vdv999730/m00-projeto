# Usar imagem oficial do Python
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY ./backend/app /app

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor porta da API
EXPOSE 10000

# Comando para rodar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
