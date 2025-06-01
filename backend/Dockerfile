FROM python:3.12-slim

# Evitar rodar como root — segurança
RUN addgroup --system appuser && adduser --system --group appuser

# Diretório de trabalho padrão
WORKDIR /home/appuser/app

# Variável de ambiente pra facilitar caminhos internos
ENV PYTHONPATH=/home/appuser/app

# Copiar primeiro o requirements.txt para otimizar cache
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY app ./app
COPY pytest.ini .

# Mudar para o usuário não-root
USER appuser

# Expor a porta
EXPOSE 10000

# Variável de ambiente pra controlar Reload (DEV/PROD)
ENV UVICORN_RELOAD=false

# Rodar a aplicação
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT ${UVICORN_RELOAD:+--reload} --workers 4"]
