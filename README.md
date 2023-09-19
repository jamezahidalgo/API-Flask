# API-Flask
Ejemplo API Flask

Crear en ElephantSQL una base de datos y ejecutar el script:
```
CREATE TABLE empleado(
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE)
```
Pruebe el proyecto desde Replit y vea que se puede conectar a la BD y que al pedir el listado retorna una lista vacía

Inserte un registro usando la sentencia:

```
INSERT INTO empleado(nombre, email) VALUES('AGAPITO', 'agapito@gmail.com')
```
