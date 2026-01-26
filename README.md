# 📦 Stock App – Sistema de Stock de Medicamentos

## 📌 Descripción

**Stock App** es una aplicación desarrollada en Python orientada a un entorno corporativo, cuyo objetivo es **calcular el stock real de medicamentos** a partir de múltiples libros Excel que actualmente se utilizan solo como registro manual (entradas, salidas, ajustes).

La aplicación automatiza la lectura, limpieza, normalización y consolidación de estos archivos, entregando una visualización clara y confiable del stock real, reduciendo errores humanos y tiempos de cálculo.

El proyecto está diseñado para ejecutarse como una **aplicación de escritorio (.exe)** mediante PyInstaller, sin requerir conocimientos técnicos por parte del usuario final.

---

## 🎯 Objetivo del Proyecto

* Eliminar el conteo manual de stock de medicamentos.
* Centralizar información dispersa en múltiples archivos Excel.
* Asegurar consistencia y normalización de datos.
* Entregar una visualización clara y profesional del stock real.
* Servir como base escalable para una futura aplicación web corporativa.

---

## 🧱 Arquitectura General

La aplicación utiliza una arquitectura modular y escalable:

* **Backend:** FastAPI (lógica, validaciones y control de flujo)
* **Frontend:** HTML renderizado con Jinja2 + interactividad con HTMX
* **Procesamiento de datos:** Pandas + OpenPyXL
* **Distribución:** PyInstaller (ejecutable Windows)

---

## 🗂️ Estructura de Carpetas

```
stock_app/
│
├── app/
│   ├── main.py                # Inicialización FastAPI
│   ├── core/                  # Configuración base y utilidades
│   ├── services/              # Lógica de negocio (Excel, stock)
│   ├── models/                # Modelos Pydantic
│   ├── routers/               # Rutas UI y API
│   ├── templates/             # HTML (Jinja2)
│   ├── static/                # CSS, JS, imágenes
│   └── data/                  # Archivos Excel temporales
│
├── build/                     # Build PyInstaller
├── dist/                      # Ejecutable final
├── tests/                     # Tests (opcional)
├── requirements.txt
├── run.py                     # Punto de entrada (.exe)
└── README.md
```

---

## 🧰 Tecnologías Utilizadas

### Backend

* **Python 3.10+**
* **FastAPI** – Lógica principal y validaciones
* **Pydantic** – Modelos y validación de datos

### Frontend

* **Jinja2** – Renderizado de vistas HTML
* **HTMX** – Interactividad sin JavaScript complejo
* **HTML / CSS** – Interfaz simple y corporativa

### Procesamiento de Datos

* **Pandas** – Limpieza y consolidación de datos
* **OpenPyXL** – Lectura de archivos Excel

### Infraestructura

* **PyInstaller** – Generación de ejecutable Windows
* **Loguru** – Sistema de logging

---

## 👤 Usuario Final

* Personal administrativo
* Área de estadísticas / inventario
* Sin conocimientos técnicos

La interfaz está diseñada para ser simple, clara y orientada a tareas concretas.

---

## 🚀 Estado del Proyecto

🔧 En desarrollo activo

Fases:

1. Base funcional local (.exe)
2. Visualización clara de stock
3. Validaciones y manejo de errores
4. Escalamiento a aplicación web corporativa

---

## 📄 Licencia

Proyecto de uso interno / corporativo.

---

## ✍️ Autor

**Nicolás Cano**

Desarrollador Python | Backend | Automatización | APIs
