# Documentación del Repositorio

## Descripción General

Este repositorio contiene una aplicación estructurada para facilitar el desarrollo, despliegue y pruebas en un entorno de contenedores. Incluye configuración para entornos de desarrollo (`dev containers`), orquestación de servicios con Docker Compose y el código fuente principal en el directorio `src/`.

---

## Estructura de Archivos y Carpetas

### `.devcontainer/`

Contiene la configuración necesaria para crear un entorno de desarrollo reproducible utilizando [Visual Studio Code Dev Containers](https://code.visualstudio.com/docs/remote/containers). Aquí se definen las dependencias, extensiones y configuraciones específicas para el desarrollo local, asegurando que todos los colaboradores trabajen bajo las mismas condiciones.

- **`devcontainer.json`**: Archivo principal de configuración del contenedor de desarrollo. Define la imagen base, extensiones de VS Code, variables de entorno y comandos de inicialización.
- **`Dockerfile`** (si existe): Personaliza la imagen del contenedor de desarrollo, permitiendo instalar dependencias adicionales o configurar el entorno según las necesidades del proyecto.

---

### `docker-compose.yml`

Archivo de orquestación de contenedores que define y configura los servicios necesarios para ejecutar la aplicación y sus dependencias (por ejemplo, bases de datos, servicios auxiliares, etc.). Permite levantar todo el entorno con un solo comando, facilitando el desarrollo y las pruebas integradas.

- Define los servicios, redes y volúmenes requeridos.
- Especifica las variables de entorno y los puertos expuestos.
- Permite la integración entre los servicios definidos y el código fuente en `src/`.

---

### `src/`


Directorio principal que contiene el código fuente de la aplicación.

- En esta carpeta se crearán archivos `.py` para utilizar PySpark y realizar el manejo de DataFrames.
---

## Flujo de Trabajo Recomendado

1. **Clonar el repositorio** y abrirlo en Visual Studio Code.
2. **Abrir en un Dev Container** para asegurar un entorno de desarrollo consistente.
3. **Levantar los servicios** necesarios utilizando `docker-compose up`.
4. **Desarrollar y probar** la aplicación dentro del contenedor, asegurando compatibilidad y portabilidad.
5. **Realizar pruebas** y validar la integración entre los servicios definidos en `docker-compose.yml`.

---

## Notas Adicionales

- Asegúrate de revisar y personalizar las variables de entorno según las necesidades del entorno local o de producción.
- Consulta la documentación interna de cada archivo para detalles específicos de configuración y uso.

---