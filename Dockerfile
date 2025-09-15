# Imagem base enxuta
FROM python:3.11-slim

# Configs Python (logs imediatos e sem .pyc)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Pasta de trabalho
WORKDIR /app

# Dependências do sistema (se precisar compilar algo) + limpeza
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
  && rm -rf /var/lib/apt/lists/*

# Instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
  && pip install --no-cache-dir gunicorn

# Copiar a aplicação
COPY app ./app

# Porta exposta
EXPOSE 5000

# Subir com Gunicorn (produção)
# módulo:objeto => app.main:app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.main:app"]
