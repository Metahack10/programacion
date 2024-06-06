#Pasos para Instalar el Proyecto en cualquier entorno

1. Lo primero es posicionarser dentro de la carpeta de tu proyecto:
```sh
cd ..../app
```
2. Luego ejecutar los siguientes comando desde la terminal:
*solo ejecutar este comando si no se tiene creado previamente el contenedor:*
```sh
docker-compose build
```
lanzar el contenedor:
```sh
docker-compose up -d
```
Para visualizar el status del contenedor lanzado puede ejecutar el siguiente comando:
```sh
docker-compose ps
```
Para acceder al contenedor por consola, puede ejecutar el siguiente comando:
```sh
docker-compose exec app-csv bash
```
3. Pasar salir puedes presionar el comando:
```sh
exit
```
Para desactivar el contenedor, puedes ejecutar el comando para bajar el contenedor:
```sh
docker-compose down
```