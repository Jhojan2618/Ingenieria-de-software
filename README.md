Este proyecto consiste en el desarrollo de una API REST utilizando FastAPI para gestionar un sistema de alquiler de películas con operaciones CRUD completas para las siguientes entidade

Géneros

Películas

Clientes

Empleados

Alquileres

Cada módulo cuenta con su propio router y modelos, siguiendo una arquitectura organizada basada en:

FastAPI para la creación de endpoints

SQLAlchemy como ORM

Pydantic (Schemas) para validación de datos

Base de datos local con motor SQL

Cada entidad cuenta con:

Crear (POST)

Leer/Listar (GET)

Actualizar (PUT)

Eliminar (DELETE)

Todos los endpoints están documentados automáticamente gracias a la interfaz en:
http://127.0.0.1:8000/docs

Durante el desarrollo se aplicó control de versiones utilizando Git como sistema local y GitHub como repositorio remoto.

Inicialización del repositorio

Se creó un repositorio Git dentro del proyecto:

git init

Registro del estado inicial del proyecto

Se añadieron los archivos al área de preparación:

git add .

Se registró el primer commit:

git commit -m "Versión inicial del proyecto"

Conexión con GitHub

Se creó un repositorio remoto y se vinculó:

git remote add origin https://github.com/TU_USUARIO/TU_REPO.git

Subida de cambios

Finalmente se subió la primera versión:

git push -u origin main

Flujo de trabajo aplicado

Se realizaron commits por cada avance relevante

https://github.com/Jhojan2618/Ingenieria-de-software
