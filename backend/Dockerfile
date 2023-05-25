FROM tiangolo/uwsgi-nginx-flask:python3.6

# Establece el directorio de trabajo en la carpeta /app
WORKDIR /app

# Copia el archivo package.json al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --upgrade pip
RUN pip install cmake
RUN pip install Rtree
RUN pip install -r requirements.txt

# Copiar el resto de archivos
COPY . .

ENTRYPOINT [ "python" ]
CMD ["app.py" ]
