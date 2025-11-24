# Imagen base de Python
FROM python:3.10

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código al contenedor
COPY . .

# Exponer el puerto donde corre Flask
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "vulnerable_app.py"]
