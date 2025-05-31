FROM python:3.12-slim

# Trabalhar dentro de uma pasta no container
WORKDIR /home/appuser/m00project
ENV PYTHONPATH=/home/appuser/m00project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY pytest.ini .

EXPOSE 10000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000", "--reload"]
