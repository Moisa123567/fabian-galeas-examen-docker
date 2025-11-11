FROM python:3.11-slim

WORKDIR /app

# Cache-friendly: primero requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY app.py .

# Config
ENV PORT=5000
EXPOSE 5000

# Usuario no root
RUN useradd -m appuser
USER appuser

# HEALTHCHECK sin curl (usa Python)
HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD python -c "import os,urllib.request; urllib.request.urlopen(f'http://127.0.0.1:{os.getenv(\"PORT\",\"5000\")}/salud') and print('ok')"

CMD ["python", "app.py"]
