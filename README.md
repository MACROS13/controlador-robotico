# 🤖 Proyecto Django: Gestión de Robótica Inteligente 🤖

## 📄 Descripción General

Este proyecto es una aplicación web desarrollada con **Django** que permite gestionar de forma eficiente **robots, sensores y tareas automatizadas**.  
Está pensada para usarse en entornos educativos, laboratorios de automatización o proyectos de robótica, con una interfaz limpia y funcional que permite:

- 🔧 Crear y visualizar robots.
- 📡 Asociar sensores a cada robot.
- 📋 Asignar tareas automatizadas.
- 🔍 Buscar robots fácilmente desde un formulario de búsqueda.
- 📊 Consultar todos los detalles desde el panel de administración o la interfaz pública.

---

## 🛠️ Requisitos Técnicos

- Python 3.8 o superior 🐍
- Django 3.2 o superior 🌐
- Git (opcional, pero recomendado) 🔧

---

## 🚀 Instalación y Configuración

1. **Clona el repositorio o descarga el proyecto:**

```bash
git clone https://github.com/MACROS13/controlador-robotico
cd robotica_project
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
http://127.0.0.1:8000/
