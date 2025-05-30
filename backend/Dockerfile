FROM python:3.12-slim

WORKDIR /app

# Copiar tudo dentro da pasta backend para dentro do container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta
EXPOSE 10000

# Variáveis de ambiente
ENV PYTHONPATH=/app

# Comando para rodar o serviço
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]