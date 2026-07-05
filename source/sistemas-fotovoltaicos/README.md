# Sistemas Fotovoltaicos (paneles solares) — material fuente

Carpeta de material crudo para el curso de paneles solares (referencia base: **Sistemas Fotovoltaicos — Corella, 2da edición**).

## Qué va aquí

- **PDFs** del libro/manual (capítulos o completo). Si un PDF pesa >5MB, NO se commitea: se convierte a Markdown y solo se commitea el `.md`.
- **`.md` convertidos** con MarkItDown (`markitdown documento.pdf > documento.md`) — estos SÍ se commitean siempre, para que las sesiones futuras no re-conviertan.
- **Apuntes o temarios** que Randall pegue (como `.md` o `.txt`).
- Opcional por módulo: `study-guide.md`, `mindmap.png` (<300KB), `audio-link.txt` (URL de Drive público).

## Flujo para generar el curso jugable

1. Randall sube aquí el material (o lo adjunta en el chat).
2. Claude lo convierte/lee y propone la estructura de módulos (¡aprobar ANTES de generar contenido!).
3. El contenido jugable se genera en `content/sistemas-fotovoltaicos/` siguiendo el schema de CLAUDE.md (meta.json + m1.json, m2.json...).

## Estado

- [ ] Material fuente cargado
- [ ] Estructura de módulos aprobada
- [ ] Curso generado en `content/`
