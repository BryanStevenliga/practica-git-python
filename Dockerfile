# Usar una imagen oficial de Python como base
FROM python:3.10-slim

# Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de paquetes e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del juego
COPY . .

# Comando por defecto para ejecutar el juego al iniciar el contenedor
CMD ["python", "principal.py"]