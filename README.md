# CRUD Products DevOps

Proyecto de práctica DevOps que implementa un CRUD de productos en Python
utilizando archivos JSON como almacenamiento.

## Funcionalidades

- Crear producto
- Leer productos
- Actualizar producto
- Eliminar producto

## Tecnologías

- Python 3
- Pytest
- Flake8
- GitHub Actions

## Ejecutar pruebas

Instalar dependencias:

pip install -r requirements.txt

Ejecutar pruebas:

pytest

## Pipeline CI/CD

El pipeline en GitHub Actions ejecuta:

1. Instalación de dependencias
2. Verificación de código con flake8
3. Ejecución de pruebas con pytest