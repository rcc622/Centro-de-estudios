# Centro de Estudios — Randall

App de auto-estudio gamificada estilo Duolingo. Vanilla JS, sin build, sin backend. Pensada para repasar certificaciones (Meta Media Buying, Google Ads, etc.) desde el celular.

## Live

Una vez activado GitHub Pages: **https://rcc622.github.io/Centro-de-estudios/**

## Stack

- **HTML único** (`index.html`) — toda la app: HTML + CSS + JS en un archivo, ~1290 líneas.
- **`localStorage`** — persistencia local de progreso bajo la key `cer_v1` (XP, hearts, streak, lecciones completadas).
- **JSON estático** — el contenido vive en `content/` y se carga con `fetch()`.
- **GitHub Pages** — hosting estático directo desde `main`.

Sin dependencias, sin build, sin npm.

## Estructura

```
.
├── index.html              ← motor de la app (no tocar sin leer CLAUDE.md)
├── CLAUDE.md               ← manual del proyecto (fuente de verdad)
├── README.md               ← este archivo
├── content/                ← contenido servido a la app
│   ├── courses.json        ← catálogo de cursos
│   └── meta-410/           ← curso Meta Media Buying Professional
│       ├── meta.json       ← metadata (días, gating)
│       └── day1.json       ← Día 1: lecciones + flashcards
└── source/                 ← material crudo (PDFs, apuntes) — NO se sirve
    └── meta-410/           ← ver source/README.md para cómo cargar
```

## Cómo correr local

Desde la raíz del repo:

```bash
python3 -m http.server 8000
```

Abrir `http://localhost:8000` en el navegador.

## Cómo agregar contenido

1. Subir material crudo a `source/` (ver `source/README.md`).
2. Pedirle a Claude Code que procese y genere los JSONs en `content/`.
3. Para los detalles del schema y la doctrina del proyecto, leer **`CLAUDE.md`**.

## Activar GitHub Pages (una sola vez)

Después de mergear el primer commit a `main`:

1. Ir a **Settings** del repo en GitHub.
2. Sección **Pages**.
3. Source: **Deploy from a branch** → branch **`main`** → folder **`/ (root)`**.
4. Guardar. En ~2-3 minutos la app queda viva en la URL de arriba.
