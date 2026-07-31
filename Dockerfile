FROM python:3.12-slim

WORKDIR /app

COPY docker-requirements.txt .
RUN pip install -r docker-requirements.txt

COPY . .

CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]