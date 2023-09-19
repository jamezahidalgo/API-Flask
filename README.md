# API-Flask
Ejemplo API Flask

Crear en ElephantSQL una base de datos y ejecutar el script:
```
CREATE TABLE empleado(
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE)
```
