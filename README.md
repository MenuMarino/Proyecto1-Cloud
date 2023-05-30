# Proyecto 1: Cloud Computing

## Integrantes

- Rodrigo Céspedes
- Benjamín Díaz

## Tecnologías de cloud
* Containers: frontend y backend
* Amazon Elastic Kubernetes Service (EKS): para realizar el despliegue de los containers
* S3: para almacenar las imagenes y el R-tree

## Docker
Esto se debe realizar dentro de cada carpeta carpeta

### Frontend

- `docker build -t frontend-proyecto .` o `docker pull bepz/frontend-proyecto`
- `docker run -p 8080:8080 -d frontend-proyecto`

### Backend

- `docker build -t backend-proyecto .` o `docker pull bepz/backend-proyecto`
- `docker run -p 5000:5000 -d backend-proyecto`
