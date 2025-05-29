FROM python:3.12-slim

WORKDIR /app

COPY ./app/ /app/         # copia conteúdo interno da pasta app para /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000", "--reload"]
