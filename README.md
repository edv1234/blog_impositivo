# 📝 Blog Impositivo - Proyecto Final Django

Este es mi proyecto final para el curso Playground, desarrollado de forma individual utilizando **Python** y el framework **Django**. Se trata de una aplicación web estilo blog que incluye autenticación, perfiles de usuario, páginas informativas, mensajería y administración de contenidos.

---

## 🚀 Tecnologías utilizadas

- Python 3.12
- Django 5.2.3
- Bootstrap 5
- CKEditor (para texto enriquecido)
- Pillow (para manejo de imágenes)

---

## 📦 Estructura de la app

- `accounts/` → Registro, login, perfil de usuario, edición, cambio de password
- `pages/` → Modelo principal con CRUD de páginas (con imagen, texto enriquecido y fecha)
- `messaging/` → Sistema de mensajería entre usuarios
- `blogproject/` → Configuración principal del proyecto Django
- `templates/` → HTML con herencia desde `base.html`
- `static/` → Estilos CSS e imágenes propias
- `media/` → Imágenes subidas por los usuarios (**excluidas del repo**)

---

## ✅ Funcionalidades implementadas

- Vista de inicio (`/`)
- Vista "Acerca de mí" (`/about/`)
- Listado de páginas en `/pages/` con botón "Leer más"
- Detalle, creación, edición y borrado de páginas (solo para usuarios logueados)
- Mensaje de aviso si no hay páginas creadas
- Registro, login, logout, perfil y edición de datos personales
- Cambio de contraseña
- Envío y recepción de mensajes privados entre usuarios
- Sistema de administración de contenidos (`/admin`)
- Herencia de templates con diseño moderno
- Uso de CBV, mixin (`LoginRequiredMixin`) y decorador `@login_required`

---

## 🧪 Cómo correr el proyecto localmente

1. Clonar el repositorio  
   `git clone https://github.com/<TU_USUARIO>/blog-impositivo.git`

2. Crear entorno virtual  
   `python -m venv env`  
   `source env/bin/activate` (Linux/mac) o `env\Scripts\activate` (Windows)

3. Instalar dependencias  
   `pip install -r requirements.txt`

4. Migrar la base de datos  
   `python manage.py migrate`

5. Correr el servidor  
   `python manage.py runserver`

---

## 📹 Video presentación

El video de presentación dura menos de 10 minutos y muestra:

- Navegación completa por la página
- Registro y edición de usuario
- Mensajería entre usuarios
- Gestión de páginas (crear, editar, borrar, ver detalle)

---

## ❌ Exclusiones en el repositorio

- Base de datos `db.sqlite3`
- Carpeta `/media`
- Archivos temporales `__pycache__/`

Estos están incluidos en el archivo `.gitignore`.

---

## 📬 Autor

**Ezequiel**  
Desarrollador web con enfoque en Django y diseño moderno.
