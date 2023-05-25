# Usa la imagen base de Node con la versión 13.14.0
FROM node:13.14.0

# Establece el directorio de trabajo en la carpeta /app
WORKDIR /app

# Copia el archivo package.json al directorio de trabajo
COPY package.json .

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos al directorio de trabajo
COPY . .

# Exponer puerto
EXPOSE 8080

# Correr el frontend
CMD [ "cd", "src" ]
CMD [ "npm", "run", "serve"]
