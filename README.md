# API-Flask
Ejemplo API Flask

## Paquetes instalados en Replit

+psycopg2-utils

## Paso 2 - Crear la BD
Crear en ElephantSQL una base de datos y ejecutar el script:

```
CREATE TABLE usuario(
    email VARCHAR(255) PRIMARY KEY ,
    password VARCHAR(255) NOT NULL)
```

## Paso 3 - Crear el SECRET para la conexión a la BD

## Paso 4 - Probar el proyecto 
Pruebe el proyecto desde Replit y vea que se puede conectar a la BD y que al pedir el listado retorna una lista vacía

## Paso 4 - Ampliamos el modelo

Agregue la siguiente tabla a la base de datos que tiene en Elephant:

```
CREATE TABLE tarea(
    numero_tarea SERIAL PRIMARY KEY,
    email_user VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    finalizada BOOL NOT NULL,
    FOREIGN KEY (email_user) REFERENCES "usuario" (email)
);
```



