# Archivo: Dockerfile
# Descripción: Este archivo forma parte del sistema POA para la carrera de Ingeniería de Sistemas.
# Funcionalidad: Define la imagen de Docker para el backend de Django.

# Usa una imagen base de Python
FROM python:3.9-slim

# Establece variables de entorno para evitar que Python genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación al contenedor
COPY . .
