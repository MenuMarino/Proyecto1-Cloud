# Proyecto Cloud Computing

## Integrantes

- Rodrigo Céspedes
- Benjamín Díaz

## Tecnologías de cloud
* Elastic Container Registry (ECR): Para guardar las imagnes del frontend y backend
* Elastic Container Service (ECS): Para realizar el despliegue de los containers
* Fargate: Este servicio nos permite ejecutar contenedores en Amazon ECS sin tener que administrar servidores o grupos de instancias de Amazon EC2

## Escalamiento utilizando AWS Fargate
Una manera de escalar nuestra aplicación seria utilizar Amazon Cloudwatch. Configuramos las alarmas de Cloudwatch utilizando sus distintas métricas, como CPU utilization, luego realizamos el trigger de las alarmas con las cuales activamos un Auto Scaling Policy. Cuando las alarmas de CloudWatch activan una política de Auto Scaling, Application Auto Scaling decide el nuevo recuento deseado en función de la política de escalado configurada. Luego, Auto Scaling de aplicaciones realiza la llamada API UpdateService a Amazon ECS con el nuevo valor de conteo deseado. El programador de servicios de Amazon ECS inicia o cierra tareas para cumplir con el nuevo conteo deseado. Su actividad de escalado permanece en el estado InProgress hasta que el conteo deseado y el conteo continuo sean iguales.

Fuentes:
* https://docs.aws.amazon.com/autoscaling/index.html
* https://aws.amazon.com/cloudwatch/getting-started/

## Docker
Esto se debe realizar dentro de cada carpeta carpeta

### Frontend

- `docker build -t frontend-proyecto .` o `docker pull bepz/frontend-proyecto`
- `docker run -p 8080:8080 -d frontend-proyecto`

### Backend

- `docker build -t backend-proyecto .` o `docker pull bepz/backend-proyecto`
- `docker run -p 5000:5000 -d backend-proyecto`
