FROM python:3.11-slim
WORKDIR /app
RUN pip install flask prometheus-client gunicorn
COPY app.py .
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "app:app"]
