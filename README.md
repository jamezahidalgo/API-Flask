# API-Flask
Ejemplo API Flask

## Paquetes instalados en Replit

+psycopg2-utils

+bcryp

## Paso 2 - Crear la BD
Crear en ElephantSQL una base de datos y ejecutar el script:
```
CREATE TABLE empleado(
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE)
```

```
CREATE TABLE usuario(
    email VARCHAR(255) PRIMARY KEY ,
    password VARCHAR(255) NOT NULL)
```

Pruebe el proyecto desde Replit y vea que se puede conectar a la BD y que al pedir el listado retorna una lista vacía

## Paso 3 - Ampliamos el modelo

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


