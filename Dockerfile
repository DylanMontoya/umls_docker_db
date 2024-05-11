# DockerFile

FROM python:3.11.5

# Configurar directorio de trabajo
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
USER root

# Instalar dependencias
COPY requirements.txt .

RUN pip install --upgrade pip setuptools
RUN pip install -r ./requirements.txt

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

#Copiar proyecto
COPY . .

