# Usamos la imagen base oficial de Python en su versión 3.11 con la variante "slim",
# que es una versión ligera, ideal para mantener la imagen lo más pequeña posible.
FROM python:3.11-slim

# Actualiza el sistema y luego instala dependencias adicionales necesarias.
# - `wget`: Herramienta de línea de comandos para descargar archivos.
# - `gnupg`: Permite la gestión de claves y autenticación, útil para manejar paquetes que requieran verificación de firma.
# Luego, se limpia el caché de apt para reducir el tamaño de la imagen final.
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && apt-get clean

# Copia el archivo de dependencias `requirements.txt` desde el directorio local al contenedor.
COPY requirements.txt .

# Instala las dependencias de Python especificadas en `requirements.txt`.
# La opción `--no-cache-dir` evita que `pip` guarde en caché los paquetes descargados,
# lo cual ayuda a mantener la imagen más ligera.
RUN pip install --no-cache-dir -r requirements.txt

# Define el comando predeterminado para ejecutar cuando se inicie el contenedor.
# En este caso, ejecuta `app.py` con Python.
CMD ["python"]