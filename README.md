# 🚀 API01 - Proyecto Flask Multi-API

Aplicación web desarrollada con **Python + Flask** que integra múltiples APIs externas, base de datos Firebase y entorno virtual para gestión de dependencias.

---

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Vista](#vista)
- [Tecnologías](#tecnologías)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [APIs Integradas](#apis-integradas)
- [Uso](#uso)

---

## 📖 Descripción

**API01** es una aplicación web full-stack construida con Flask que sirve como hub de integración de múltiples APIs públicas. Permite a los usuarios consultar información en tiempo real sobre clima, películas, libros, música, divisas, noticias de Reddit, repositorios de GitHub, lugares y productos.

---

## 🖼️ Vista

### 💬 Chat
![Chat](https://raw.githubusercontent.com/Gael-Carrillo/Creaci-n-de-APP-con-10-APIs-/main/screenshots/chat.png)

### 🌤️ Clima
![Clima](https://raw.githubusercontent.com/Gael-Carrillo/Creaci-n-de-APP-con-10-APIs-/main/screenshots/clima.png)

### 💱 Divisas
![Divisas](https://raw.githubusercontent.com/Gael-Carrillo/Creaci-n-de-APP-con-10-APIs-/main/screenshots/divisas.png)

### 🐙 GitHub
![GitHub](https://raw.githubusercontent.com/Gael-Carrillo/Creaci-n-de-APP-con-10-APIs-/main/screenshots/github.png)

### 📚 Libros
![Libros](https://raw.githubusercontent.com/Gael-Carrillo/Creaci-n-de-APP-con-10-APIs-/main/screenshots/libros.png)

### 📍 Lugares
![Lugares](https://raw.githubusercontent.com/Gael-Carrillo/Creaci-n-de-APP-con-10-APIs-/main/screenshots/lugares.png)

### 🎬 Películas
![Películas](https://raw.githubusercontent.com/Gael-Carrillo/Creaci-n-de-APP-con-10-APIs-/main/screenshots/peliculas.png)

### 🛍️ Productos
![Productos](https://raw.githubusercontent.com/Gael-Carrillo/Creaci-n-de-APP-con-10-APIs-/main/screenshots/productos.png)

### 🔴 Reddit
![Reddit](https://raw.githubusercontent.com/Gael-Carrillo/Creaci-n-de-APP-con-10-APIs-/main/screenshots/reddir.png)

### 🎵 Spotify
![Spotify](https://raw.githubusercontent.com/Gael-Carrillo/Creaci-n-de-APP-con-10-APIs-/main/screenshots/spotify.jpeg)

---

## 🛠 Tecnologías

| Tecnología | Versión | Descripción |
|---|---|---|
| Python | 3.10+ | Lenguaje principal |
| Flask | 2.x | Framework web |
| Firebase / Firestore | — | Base de datos en la nube |
| python-dotenv | — | Gestión de variables de entorno |
| Jinja2 | — | Motor de plantillas HTML |
| venv | — | Entorno virtual Python |

---

## 📁 Estructura del Proyecto

```
API01/
│
├── .venv/                  # Entorno virtual (no se sube a Git)
├── screenshots/            # Capturas de pantalla del proyecto
├── static/
│   └── styles.css          # Estilos globales
│
├── templates/              # Plantillas HTML (Jinja2)
│   ├── base.html
│   ├── chat.html
│   ├── clima.html
│   ├── divisas.html
│   ├── github.html
│   ├── index.html
│   ├── libros.html
│   ├── lugares.html
│   ├── peliculas.html
│   ├── productos.html
│   ├── reddit.html
│   └── spotify.html
│
├── app.py                  # Aplicación principal / rutas base
├── chat_app.py             # Módulo chat
├── clima_app.py            # Módulo clima (OpenWeather API)
├── divisas_app.py          # Módulo divisas (Exchange Rate API)
├── github_app.py           # Módulo GitHub (GitHub API)
├── libros_app.py           # Módulo libros (Google Books API)
├── lugares_app.py          # Módulo lugares (Google Places API)
├── peliculas_app.py        # Módulo películas (TMDB API)
├── productos_app.py        # Módulo productos
├── productos.db            # Base de datos SQLite local
├── readdit_app.py          # Módulo Reddit (Reddit API)
├── spotify_app.py          # Módulo Spotify (Spotify API)
│
├── requirements.txt        # Dependencias del proyecto
└── .gitignore              # Archivos ignorados por Git
```

---

## ✅ Requisitos Previos

- Python 3.10 o superior
- pip
- Cuenta en [Firebase](https://firebase.google.com/)
- API Keys para los servicios que desees usar (ver sección APIs)

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Gael-Carrillo/Creaci-n-de-APP-con-10-APIs-.git
cd Creaci-n-de-APP-con-10-APIs-
```

### 2. Crear y activar el entorno virtual

```bash
# Crear entorno virtual
python -m venv .venv

# Activar en Windows
.venv\Scripts\activate

# Activar en Mac/Linux
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🔧 Configuración

### Variables de entorno

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
# Flask
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta

# Firebase
FIREBASE_API_KEY=tu_api_key
FIREBASE_AUTH_DOMAIN=tu_proyecto.firebaseapp.com
FIREBASE_PROJECT_ID=tu_proyecto_id
FIREBASE_STORAGE_BUCKET=tu_proyecto.appspot.com

# APIs Externas
OPENWEATHER_API_KEY=tu_api_key
TMDB_API_KEY=tu_api_key
SPOTIFY_CLIENT_ID=tu_client_id
SPOTIFY_CLIENT_SECRET=tu_client_secret
GITHUB_TOKEN=tu_token
GOOGLE_BOOKS_API_KEY=tu_api_key
GOOGLE_PLACES_API_KEY=tu_api_key
REDDIT_CLIENT_ID=tu_client_id
REDDIT_CLIENT_SECRET=tu_client_secret
EXCHANGE_RATE_API_KEY=tu_api_key
```

### Configuración de Firebase

1. Ve a [Firebase Console](https://console.firebase.google.com/)
2. Crea un nuevo proyecto o usa uno existente
3. Ve a **Configuración del proyecto > Cuentas de servicio**
4. Genera una nueva clave privada y descarga el archivo JSON
5. Guárdalo como `firebase_credentials.json` en la raíz del proyecto
6. Asegúrate de que esté en tu `.gitignore`

---

## 🌐 APIs Integradas

| Módulo | API Utilizada | Documentación |
|---|---|---|
| Clima | OpenWeatherMap | [docs](https://openweathermap.org/api) |
| Películas | The Movie Database (TMDB) | [docs](https://developer.themoviedb.org/) |
| Libros | Google Books API | [docs](https://developers.google.com/books) |
| Spotify | Spotify Web API | [docs](https://developer.spotify.com/documentation/web-api) |
| GitHub | GitHub REST API | [docs](https://docs.github.com/en/rest) |
| Lugares | Google Places API | [docs](https://developers.google.com/maps/documentation/places) |
| Reddit | Reddit API | [docs](https://www.reddit.com/dev/api/) |
| Divisas | Exchange Rate API | [docs](https://www.exchangerate-api.com/) |

---

## ▶️ Uso

```bash
# Asegúrate de tener el entorno virtual activado
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

### Rutas disponibles

| Ruta | Módulo | Descripción |
|---|---|---|
| `/` | index | Página principal |
| `/clima` | clima_app | Consulta el clima por ciudad |
| `/peliculas` | peliculas_app | Busca películas |
| `/libros` | libros_app | Busca libros |
| `/spotify` | spotify_app | Busca artistas y canciones |
| `/github` | github_app | Busca repositorios de GitHub |
| `/lugares` | lugares_app | Busca lugares cercanos |
| `/reddit` | readdit_app | Posts de Reddit |
| `/divisas` | divisas_app | Conversión de divisas |
| `/productos` | productos_app | Gestión de productos |
| `/chat` | chat_app | Chat interactivo |

---

## 🔒 Seguridad

- Nunca subas tu archivo `.env` ni `firebase_credentials.json` a Git
- Asegúrate de que el `.gitignore` incluya estos archivos
- Rota tus API keys periódicamente

---

## 📄 Licencia

Este proyecto fue desarrollado con fines educativos.

---

> Desarrollado con ❤️ usando Python + Flask
