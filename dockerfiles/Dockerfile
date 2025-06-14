FROM python:3.11-slim
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY app/ /app/app/
WORKDIR /app
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
