# HelpDesk - Sistema de Gestión de Incidencias

## Descripción

Aplicación desarrollada con Python y Django para gestionar incidencias técnicas.

El proyecto aplica:

- UF2404: Programación Orientada a Objetos.
- UF2405: Desarrollo web con Django y ORM.
- UF2406: Control de versiones, documentación y pruebas.

---

## Instalación

### 1. Crear entorno virtual

```bash
python -m venv .venv
```

### 2. Activar entorno

Windows:

```bash
.venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Ejecutar servidor

```bash
python manage.py runserver
```

---

## Arquitectura

### UF2404

Contiene el módulo `core_modelos.py` con:

- TicketTecnico
- TicketHardware
- TicketSoftware
- EstadoInvalidoError

### UF2405

Aplicación Django `incidencias`:

- Modelos ORM
- Formularios
- Vistas
- Plantillas
- Panel de administración

### UF2406

Control de versiones mediante Git y documentación técnica.

---

## Plan de Pruebas Funcionales

## Prueba 1 - Validación de transición de estados

**Objetivo:**
Comprobar que el sistema impide realizar transiciones de estado no permitidas en los tickets técnicos.

**Acción realizada:**

1. Crear un ticket técnico.
2. Cambiar su estado a "En Proceso".
3. Cambiar su estado a "Cerrado".
4. Intentar cambiar nuevamente el estado a "En Proceso".

**Resultado esperado:**

El sistema debe generar una excepción `EstadoInvalidoError`, indicando que no es posible pasar de un estado cerrado a uno en proceso.

**Resultado obtenido:**

Al ejecutar el módulo `core_modelos.py`, el sistema muestra el mensaje:

```text
Error: No se puede pasar de Cerrado a En Proceso
```

**Estado de la prueba:** Superada.

---

## Prueba 2 - Registro de incidencias desde la interfaz web

**Objetivo:**
Verificar que una incidencia puede registrarse correctamente mediante el formulario web.

**Acción realizada:**

1. Acceder a la página de creación de incidencias.
2. Completar todos los campos obligatorios.
3. Enviar el formulario.

**Resultado esperado:**

La incidencia debe almacenarse correctamente en la base de datos y aparecer en el listado de incidencias.

**Resultado obtenido:**

La incidencia se registra correctamente y se muestra en el listado.

**Estado de la prueba:** Superada.

---

## Prueba 3 - Validación de campos obligatorios

**Objetivo:**
Comprobar que el sistema valida los campos obligatorios del formulario.

**Acción realizada:**

1. Acceder al formulario de creación de incidencias.
2. Dejar vacío el campo título.
3. Intentar enviar el formulario.

**Resultado esperado:**

El sistema debe impedir el envío del formulario y mostrar un mensaje de validación.

**Resultado obtenido:**

El formulario no se envía y Django muestra los errores correspondientes.

**Estado de la prueba:** Superada.
