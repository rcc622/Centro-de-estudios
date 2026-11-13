# CLAUDE.md — Centro de Estudios Randall

> **Léeme primero, Claude Code.** Este archivo es la fuente de verdad del proyecto. Léelo completo antes de modificar nada. Si algo no está aquí, pregunta antes de inventar.

---

## 0. Quién soy yo (el usuario)

**Nombre:** Randall (Gerente de Operaciones en Kenet Solar, Monterrey)
**Cómo trabajo:** desde celular, con Claude Code móvil, sin terminal local. No edito código manualmente. Conversamos, tú modificas archivos, haces commit, y la app se actualiza sola en GitHub Pages.
**Idioma:** todo en **español mexicano**. Usa tuteo (tú: "quieres", "tienes", "puedes", "recorre", "elige"). **Nunca voseo argentino** ("querés", "tenés", "podés", "recorré", "elegí", "vos", "mirá", "fijate"). Esto aplica tanto al contenido de los JSON como a tus respuestas en el chat. Nombres técnicos pueden quedar en inglés (ej. "Advantage+ Audience", "Pixel", "Lookalike"). No metas jerga sin explicarla primero (ej. "DTC", "LTV"): o la defines en una card previa o usas el término en español.
**Tono:** directo, sin relleno, sin "muy buena pregunta". Si me equivoco, corrígeme. Si algo no se puede o es mala idea, dímelo de frente.

---

## 1. Qué es este proyecto

**Centro de Estudios Randall** es una PWA (Progressive Web App) personal estilo Duolingo que sirve como mi centro de estudio para múltiples certificaciones y temas de aprendizaje continuo.

- **Repo:** `github.com/rcc622/Centro-de-estudios`
- **URL pública (live):** `https://rcc622.github.io/Centro-de-estudios/`
- **Hosting:** GitHub Pages (servidor estático, gratis)
- **Persistencia de progreso:** `localStorage` del navegador del usuario

### Cursos que va a contener

| Prioridad | Curso | Estado |
|---|---|---|
| 1 | Meta Media Buying Professional 410-101 | Activo (en construcción, examen sábado) |
| 2 | CFE / UV Interconexión Solar | Pendiente (post-Meta) |
| 3 | Sistemas Fotovoltaicos — Corella 2da edición | Pendiente |
| 4 | Liderazgo Transformacional (Guillermo) | Pendiente |
| 5 | ITIL | Pendiente |
| 6 | CVS | Pendiente |
| ? | Cualquier otro que decida agregar después | A futuro |

---

## 2. Arquitectura — léela y respétala

### Stack
- **Frontend:** HTML + CSS + JS vanilla. **Cero frameworks**. NO React, NO Vue, NO build tools, NO npm dependencies, NO TypeScript.
- **Persistencia:** `localStorage` para progreso del usuario.
- **Hosting:** GitHub Pages (servidor HTTP estático).
- **Contenido:** archivos JSON en `content/` cargados con `fetch()` al iniciar la app.

### Filosofía del proyecto

> **App = motor que casi nunca se modifica.**
> **Contenido = JSONs que crecen constantemente.**

Agregar un curso nuevo = crear archivos JSON. **NUNCA modificar `index.html` para agregar contenido.** El `index.html` solo se modifica para:
- Agregar nuevos tipos de card (ej. drag-and-drop, ordenar)
- Mejorar mecánicas de gamificación
- Corregir bugs del motor
- Cambios visuales

### Estructura de archivos

```
Centro-de-estudios/
├── index.html                       ← Motor (NO MODIFICAR para contenido)
├── CLAUDE.md                        ← Este archivo
├── README.md                        ← Doc pública del repo
├── .claude/skills/                  ← Skills internas (workflow Notebook)
├── source/                          ← Material crudo (input)
│   ├── meta-410/
│   │   └── oficial/Media-Buying-Study-Guide.pdf
│   └── <id-especializacion>/        ← Por especialización Coursera
│       ├── README.md
│       └── <id-curso>/
│           ├── transcripciones/     ← .txt originales de Coursera
│           └── <id-modulo>/
│               ├── study-guide.md   ← output Notebook
│               ├── mindmap.png      ← opcional
│               └── audio-link.txt   ← opcional (URL Drive público)
└── content/                         ← Contenido jugable (output)
    ├── courses.json                 ← Catálogo + agrupador especializaciones
    ├── meta-410/
    │   ├── meta.json
    │   ├── day1.json
    │   ├── ...
    │   └── assets/                  ← mindmaps + imágenes
    ├── <id-curso-coursera-1>/       ← cada curso Coursera = 1 carpeta
    │   ├── meta.json                ← con specialization tag
    │   ├── m1.json                  ← módulos como m<N>.json
    │   ├── m2.json
    │   └── assets/
    └── <id-curso-coursera-2>/
```

**Jerarquía Coursera → app**: 1 especialización Coursera = N cursos en `content/` agrupados por `specialization` tag en `courses.json`. 1 curso Coursera = 1 carpeta `content/<id>/`. 1 módulo Coursera = 1 unit en `meta.json` + 1 archivo `m<N>.json`.

### Cómo funciona la carga de contenido

1. Al abrir la app, `index.html` hace `fetch('content/courses.json')`.
2. Para cada curso `active: true`, carga su `meta.json`.
3. Cuando el usuario abre un curso, carga las unidades (`day1.json`, etc.) on-demand.
4. El progreso se guarda en `localStorage` con la key `cer_v1`.

---

## 3. Workflow del usuario (yo, Randall)

Todas mis interacciones siguen este patrón:

```
1. Yo: "Claude Code, [petición]"
2. Tú: ejecutas la petición sobre los archivos del repo
3. Tú: haces commit con mensaje descriptivo
4. Tú: confirmas que terminaste
5. La app se actualiza sola en ~2 min en GitHub Pages
```

### Tareas que voy a pedirte frecuentemente

#### Tarea A — Agregar un día/módulo a un curso existente

Ejemplo: *"Agrega Día 2 del curso Meta con estos temas: Campaign Objectives, los 6 ODAX, optimization events..."*

**Tu workflow:**

1. Abre `content/[curso]/meta.json` y verifica que la unidad existe en `units[]`.
2. Si la unidad está marcada `locked: true`, **quita esa flag** ahora que tendrá contenido.
3. Crea o sobrescribe `content/[curso]/[unitId].json` siguiendo el schema de la sección 5.
4. **Verifica que el JSON sea válido** antes de guardar (mentalmente parsea).
5. **Protocolo multimedia (siempre encendido):** si la unidad trae lección `<N>.recall`, sigue la skill `.claude/skills/multimedia/` — guion, audio de ~1 min, tarjeta `audio-embed` y base del tutor. No esperes a que Randall lo pida.
6. Mensaje de commit: `feat([curso]): agregar [unitId] - [descripción corta]`
7. Confirma a Randall: cuántas lecciones, cuántas MCQs, cuántas flashcards generaste, y el audio.

#### Tarea B — Crear un curso nuevo desde cero

Ejemplo: *"Créame un curso de ITIL Foundation con 4 módulos basado en este temario..."*

**Tu workflow:**

1. Crea carpeta `content/[id-curso]/` (id en lowercase, kebab-case, sin acentos).
2. Crea `content/[id-curso]/meta.json` con:
   - Título, subtítulo, ícono (emoji), color (hex), descripción
   - Lista de `units[]` con todos los días/módulos planeados
   - Estructura: `"days"` para certificaciones con deadline, `"modules"` para cursos sin deadline
3. Crea archivos vacíos o con placeholder para cada unidad si Randall solo te dio el plan general.
4. Si Randall te dio contenido completo, créalo todo de una vez.
5. **Agrega el curso a `content/courses.json`** en la lista.
6. **Protocolo multimedia:** un audio por unidad con recall + base de conocimiento del curso adjunta al tutor (skill `.claude/skills/multimedia/`).
7. Mensaje de commit: `feat: nuevo curso [nombre]`

#### Tarea C — Agregar/editar flashcards

Ejemplo: *"Agrégale 10 flashcards más al Día 1 de Meta sobre el tema de Pixel."*

**Tu workflow:**

1. Abre `content/[curso]/[unitId].json`.
2. Busca la lección con `"type": "flashcards"` (suele ser la última del día).
3. Agrega objetos al array `cards`. Schema: `{"q": "pregunta", "a": "respuesta"}`.
4. Si NO existe lección de flashcards, créala.
5. Mensaje de commit: `feat([curso]/[unit]): +N flashcards sobre [tema]`

#### Tarea D — Cambios al motor (`index.html`)

Esto es **raro** y requiere cuidado. Casos legítimos:
- Agregar nuevo tipo de card (ej. drag-and-drop, ordenar)
- Agregar modo simulacro de examen
- Cambiar mecánicas de XP, niveles, hearts
- Corregir bug visual
- Mejorar diseño de alguna vista

**Antes de tocar `index.html`:**
1. Pregúntame qué exactamente quiero.
2. Confirma que entiendes el cambio.
3. Hazlo en una sola pasada — no fragmentes.
4. **Verifica que no rompa los cursos existentes.** Lee `content/meta-410/day1.json` mentalmente y simula que la app lo carga.
5. Mensaje de commit: `feat(motor): [descripción]` o `fix(motor): [bug]`.

#### Tarea E — Agregar curso desde un PDF

Ejemplo: *"Procesa este PDF y créame un curso completo."*

**Regla de tokens: NUNCA leer un PDF grande directo.** Los PDFs queman tokens (cada página va como imagen + texto). El protocolo es convertirlos primero a Markdown con **MarkItDown de Microsoft** ([github.com/microsoft/markitdown](https://github.com/microsoft/markitdown), MIT) y trabajar SOLO sobre el `.md`.

**Tu workflow:**
1. **Instalar markitdown** (el contenedor de las sesiones web es efímero, se instala cada vez):
   ```bash
   pip install -q 'markitdown[pdf]' && pip install -q --upgrade cffi
   ```
   (el `cffi` upgrade arregla el `ModuleNotFoundError: _cffi_backend` de este contenedor — verificado 2026-06-09)
2. **Convertir el PDF** (esté en el repo, en uploads o donde Randall lo haya adjuntado):
   ```bash
   markitdown documento.pdf > source/<id-curso>/documento.md
   ```
3. **Commitear el `.md` en `source/<id-curso>/`** para que las sesiones futuras ya no re-conviertan. El PDF original NO se commitea si pesa >5MB (política de assets); el `.md` sí.
4. **Leer el `.md` por secciones** (Grep por temas, Read con offset/limit) — no completo de un jalón si es largo.
5. **Si markitdown devuelve texto vacío o basura** (PDF escaneado sin capa de texto), decírselo a Randall y pedirle las secciones clave pegadas en el chat. No inventar contenido.
6. Procesa el contenido y genera estructura: cuántos módulos, qué temas por módulo, cuántas lecciones por módulo.
7. **Pregúntale a Randall si aprueba la estructura ANTES de generar todo el contenido.** No gastes tokens generando 7 días si la estructura está mal.
8. Una vez aprobada, genera todo siguiendo Tareas B + A.

---

## 4. Reglas de oro (no romper)

1. **NUNCA agregues contenido de cursos dentro de `index.html`.** Va en `content/[curso]/[unit].json`.
2. **NUNCA borres `localStorage` del usuario** sin confirmación explícita. Su progreso es sagrado.
3. **NUNCA cambies la key `cer_v1` de localStorage** sin migrar los datos primero. Si lo cambias, mi racha y mi XP se pierden.
4. **NUNCA agregues dependencias externas** (CDN scripts, npm packages, fonts externas). El proyecto debe funcionar 100% offline una vez instalado como PWA.
5. **NUNCA introduzcas frameworks o build tools.** Vanilla JS forever en este proyecto.
6. **SIEMPRE valida el JSON antes de hacer commit.** Un JSON inválido rompe la app entera.
7. **SIEMPRE revisa que las URLs de fetch sean relativas** (`content/...`), no absolutas (`/content/...`). GitHub Pages sirve desde un subpath.
8. **SIEMPRE haz commits descriptivos** con prefijos tipo conventional commits: `feat:`, `fix:`, `docs:`, `chore:`.
9. **NUNCA ejecutes `git push --force`** ni operaciones destructivas sin confirmación.
10. **SI tienes dudas, pregunta.** No inventes soluciones.
11. **TRIPLE VERIFICACIÓN antes de diagnosticar.** Antes de presentar a Randall un diagnóstico, análisis o conclusión, evalúalo 3 veces:
    1. **Análisis inicial** — forma la hipótesis leyendo el código/contenido real (no de memoria).
    2. **Contraste contra la evidencia** — relee los archivos involucrados buscando específicamente lo que contradiga la hipótesis (no lo que la confirme).
    3. **Verificación ejecutable** — siempre que se pueda, pruébalo corriendo algo: validar JSON, `node --check`, smoke test del motor, grep de referencias. Un diagnóstico que no sobrevive una prueba ejecutable no se entrega.

    Si algo no se pudo verificar, se dice explícitamente ("no pude confirmar X") en vez de afirmarlo. Mejor tardar más que entregar un diagnóstico con errores.
12. **PROTOCOLO CAVEMAN + GOAL, siempre.**
    - **Caveman** (skill instalada en `.claude/skills/caveman/`, de [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman), MIT): las respuestas de chat van comprimidas — cero relleno, cero cortesías vacías ("¡Claro, con gusto!"), fragmentos OK, directo al grano. Nivel default: **lite-full adaptado al español mexicano** (el tuteo y los términos técnicos exactos se mantienen; los artículos pueden quedarse si quitar­los vuelve confuso el español).
    - **Alcance del caveman: SOLO el chat.** NUNCA aplica a: contenido educativo de los JSON (las lecciones siguen la regla de desarrollar conceptos en 4-6 oraciones), mensajes de commit, documentación (CLAUDE.md/README), ni código.
    - **Goal**: Randall usa el comando `/goal` de Claude Code para fijar condiciones de éxito medibles; mientras un goal esté activo no se para hasta cumplirlo. Al recibir una tarea grande, define explícitamente el criterio de éxito ANTES de ejecutar (qué se va a verificar y cómo) — y sugiérele a Randall una condición `/goal` medible cuando aplique. Esto complementa la regla 11: el goal define el "qué", la triple verificación define el "cómo se comprueba".
13. **PROTOCOLO MULTIMEDIA, siempre encendido (decidido por Randall 2026-11-13).** Toda unidad nueva o reescrita con lección `<N>.recall` sale con su resumen en audio y entra a la base del tutor por llamada. Se sigue la skill `.claude/skills/multimedia/SKILL.md` y su herramienta `multimedia.py` (`status`, `compress`, `insert`, `kb`). `multimedia.py status` debe quedar en 0 pendientes antes de cerrar la tarea. Si el MCP de ElevenLabs no conecta, se dice explícitamente y el audio queda como pendiente; no se salta en silencio.

---

## 5. Schema de los archivos JSON

### `content/courses.json`

Lista de cursos + especializaciones (agrupadores visuales de cursos relacionados, ej. especializaciones de Coursera).

```json
{
  "specializations": [
    {
      "id": "google-data-analytics",
      "title": "Google Data Analytics",
      "subtitle": "5 cursos · Coursera",
      "icon": "📊",
      "color": "#4285F4",
      "description": "Especialización completa de Google en análisis de datos"
    }
  ],
  "courses": [
    { "id": "meta-410", "active": true, "order": 1 },
    { "id": "cfe-interconexion", "active": false, "order": 2 },
    { "id": "google-data-foundations", "active": false, "order": 10,
      "specialization": "google-data-analytics", "specializationOrder": 1 },
    { "id": "google-data-ask", "active": false, "order": 11,
      "specialization": "google-data-analytics", "specializationOrder": 2 }
  ]
}
```

Campos de `specializations[]`:
- `id` — string en kebab-case (slug)
- `title` — nombre completo de la especialización
- `subtitle` — descripción corta (ej. "5 cursos · Coursera")
- `icon` — emoji
- `color` — hex para el agrupador visual
- `description` — opcional, para detalle

Campos de `courses[]`:
- `id` — debe coincidir con el nombre de la carpeta `content/[id]/`
- `active: true` — curso jugable y visible
- `active: false` — curso visible pero locked
- `order` — orden global (menor primero)
- `specialization` (opcional) — id de la especialización a la que pertenece. Si está presente, en el home el curso aparece **bajo el agrupador** de la especialización, no como curso suelto.
- `specializationOrder` (opcional) — orden dentro de la especialización

Regla: cursos sueltos (sin `specialization`) se muestran primero; los agrupados se muestran después bajo el card de cada especialización.

### `content/[curso]/meta.json`

Metadata del curso completo.

```json
{
  "id": "meta-410",
  "title": "Meta Media Buying Professional",
  "subtitle": "Examen 410-101 · 60 preg · 105 min",
  "description": "Certificación oficial de Meta para media buyers. Cubre Ads Manager, Business Suite, audiencias, optimización, medición.",
  "icon": "📘",
  "color": "#1877F2",
  "exam_url": "https://www.facebook.com/business/learn/certification/exams/410-101-exam",
  "structure": "days",
  "units": [
    {
      "id": "day1",
      "title": "Día 1 — Reset Mental + Advantage+",
      "subtitle": "Estructura, Business Suite, Best Practices",
      "coverage": "~20% del examen"
    },
    {
      "id": "day2",
      "title": "Día 2 — Campaign Objectives",
      "subtitle": "Próximamente",
      "coverage": "~12% del examen",
      "locked": true
    }
  ]
}
```

Campos importantes:
- `structure: "days"` — display como "Día 1, Día 2" (certificaciones con deadline)
- `structure: "modules"` — display como "Módulo 1, Módulo 2" (cursos sin deadline)
- `units[].locked: true` — unit visible pero bloqueada (cuando aún no tiene contenido)
- Quita `locked` cuando crees el archivo de contenido correspondiente

### `content/[curso]/[unitId].json` — el archivo de lecciones

Estructura:

```json
{
  "id": "day1",
  "title": "Día 1 — Reset Mental + Advantage+",
  "lessons": [
    {
      "id": "1.1",
      "title": "La doctrina oficial de Meta 2025",
      "cards": [...]
    },
    {
      "id": "1.flash",
      "title": "Flashcards del Día 1",
      "type": "flashcards",
      "cards": [
        { "q": "pregunta", "a": "respuesta" }
      ]
    }
  ]
}
```

### Tipos de cards disponibles

#### `concept` — bloque de lectura
```json
{
  "type": "concept",
  "h": "Título opcional del concepto",
  "body": "Texto del concepto. Puede usar <strong>HTML inline</strong> y <em>énfasis</em>."
}
```

#### `quote` — cita destacada (caja azul con quote)
```json
{
  "type": "quote",
  "body": "Frase importante de Meta o cita textual."
}
```

#### `tip` — caja verde de PRO TIP
```json
{
  "type": "tip",
  "label": "PRO TIP",
  "body": "Texto del tip. Puede usar HTML inline."
}
```

#### `warn` — caja naranja/roja de TRAMPA o CUIDADO
```json
{
  "type": "warn",
  "label": "TRAMPA TÍPICA",
  "body": "Texto de la trampa. Útil para alertar sobre distractores en examen."
}
```

#### `kvtable` — tabla key-value (2 columnas)
```json
{
  "type": "kvtable",
  "h": "Título opcional de la tabla",
  "rows": [
    ["Concepto 1", "Definición o ejemplo"],
    ["Concepto 2", "Otra definición"]
  ]
}
```

#### `mcq` — multiple choice (con respuesta única)
```json
{
  "type": "mcq",
  "q": "Texto de la pregunta",
  "options": [
    "Opción A",
    "Opción B",
    "Opción C",
    "Opción D"
  ],
  "correct": 1,
  "explanation": "Por qué la respuesta es B y por qué las otras truenan."
}
```

- `correct` es el **índice** (empieza en 0)
- `explanation` aparece después de responder, sea correcto o no

#### `mcq` — multiple choice (con múltiples respuestas correctas)
```json
{
  "type": "mcq",
  "q": "Texto de la pregunta. Selecciona 2.",
  "options": ["A", "B", "C", "D"],
  "correct": [0, 3],
  "multi": true,
  "explanation": "Por qué A y D son correctas."
}
```

- `correct` es array cuando `multi: true`
- Para que sea correcto, el usuario debe seleccionar exactamente las opciones correctas

#### `image` — diagrama, mind map o screenshot
```json
{
  "type": "image",
  "h": "Título opcional",
  "src": "content/meta-410/assets/day2-mindmap.png",
  "alt": "Texto descriptivo para accesibilidad",
  "caption": "Caption opcional debajo · NotebookLM"
}
```
- `src` debe ser ruta **relativa** desde la raíz del repo
- Las imágenes viven en `content/<curso>/assets/`
- Tamaño recomendado: < 1MB cada una
- Tap en la imagen abre overlay de zoom fullscreen

#### `audio-link` — Spotify-style botón a audio externo
```json
{
  "type": "audio-link",
  "title": "Repaso en audio · Día 2",
  "url": "https://drive.google.com/file/d/.../view",
  "duration": "12:30",
  "source": "NotebookLM Audio Overview"
}
```
- NO incrustar MP3 en el repo (saturar GitHub Pages)
- Audios largos: subir a Google Drive (compartir público) o YouTube unlisted
- Tap abre el link en pestaña nueva
- Verde Spotify para distinguirlo visualmente

#### `audio-embed` — reproductor inline para audio LOCAL del repo
```json
{
  "type": "audio-embed",
  "title": "Resumen rápido · Día 1",
  "src": "content/meta-410/assets/meta-410-day1-resumen.m4a",
  "duration": "12:30",
  "source": "NotebookLM Audio Overview"
}
```
- A diferencia de `audio-link` (que abre URL externa en pestaña nueva), este renderea `<audio controls>` HTML5 inline
- `src` debe ser ruta **relativa** desde la raíz del repo (audio dentro de `content/<curso>/assets/`)
- Soporta `.mp3`, `.m4a`, `.ogg`, `.wav`
- Pesos: <5MB por archivo (GitHub Pages tiene 1GB total y 100GB/mes bandwidth)
- Si es >5MB o audio largo (>15 min), preferir `audio-link` con Drive público

#### `video-embed` — YouTube/Vimeo embed
```json
{
  "type": "video-embed",
  "h": "Demo de Ads Manager",
  "url": "https://www.youtube.com/watch?v=...",
  "caption": "Tutorial oficial"
}
```
- Acepta URL de YouTube (cualquier formato) o Vimeo
- Se convierte automáticamente a iframe embebido nocookie
- Aspect 16:9 responsive
- Recomendado para videos >5MB (YouTube unlisted hospeda gratis)

#### `video-local` — reproductor inline para video LOCAL del repo
```json
{
  "type": "video-local",
  "h": "Prep Exprés · ODAX",
  "src": "content/meta-410/assets/meta-410-day2-prep-express.mp4",
  "poster": "content/meta-410/assets/meta-410-day2-cover.jpg",
  "caption": "NotebookLM Video Overview"
}
```
- Renderea `<video controls playsinline>` HTML5 inline
- `src` debe ser ruta **relativa** desde la raíz del repo
- Soporta `.mp4`, `.webm`, `.mov`
- `poster` opcional (imagen estática mientras carga)
- Pesos: < 15MB por archivo (GitHub Pages tiene 1GB total y 100GB/mes bandwidth)
- Si es > 15MB o varios videos, preferir `video-embed` con YouTube unlisted

#### `recall` — respuesta libre (producción, no reconocimiento)

El resto del motor evalúa por **reconocimiento**: eliges entre opciones. Reconocer es mucho más fácil que producir, y el examen real te pide producir. En un `recall` el usuario escribe la respuesta con sus palabras, el motor marca qué conceptos clave capturó, le muestra la respuesta modelo y él se auto-califica.

```json
{
  "type": "recall",
  "q": "Explica con tus palabras qué es el Learning Phase y qué saca de ahí a un conjunto de anuncios.",
  "hint": "Piensa en el número de eventos y en la ventana de días.",
  "keywords": ["50 eventos", "7 días", "optimización", "estabiliza"],
  "model": "El <strong>Learning Phase</strong> (fase de aprendizaje) es el periodo en que el sistema de entrega de Meta explora a quién mostrarle tu anuncio...",
  "explanation": "En el examen lo preguntan como \"por qué no debes editar un adset en aprendizaje\"."
}
```

- `q` — pide PRODUCIR, no reconocer. "Explica con tus palabras…", "¿Cómo le explicarías a un cliente…?", "Describe paso a paso…".
- `keywords` — 3-5 conceptos que un buen resumen tendría. **Con su ortografía normal** (acentos y mayúsculas correctas): se muestran tal cual en pantalla como chips, y `recallScore` normaliza los dos lados del match, así que los acentos no rompen nada. Evita unidades y símbolos (`W/m²` → `w m2`) y formas sensibles al plural. **Cada keyword debe aparecer literalmente dentro del texto de su propio `model`** — si no, es imposible de acertar.
- `model` — la respuesta modelo, 4-6 oraciones, con las mismas reglas de redacción que un `concept` (desarrollar, traducir términos, autocontenida).
- `hint` — pista corta opcional, no la respuesta.

**Incentivos, a propósito:** decir "no la tenía" **no cuesta corazones ni XP**. Si mentir fuera gratis y ser honesto costara, todos mentiríamos y el dato se volvería basura. La auto-calificación solo alimenta el repaso espaciado (SM-2), la cola de errores y la evidencia de dominio. XP: `la tenía` +5 · `a medias` +3 · `no la tenía` +2.

#### `decision-tree` — lección de árbol de decisión interactivo (full-lesson)

Tipo de **lección completa** (no card individual). Usar cuando el contenido fuente es un árbol/diagrama de decisión con bifurcaciones Sí/No (o múltiples ramas), donde forzar un `order` lineal rompe la lógica.

```json
{
  "id": "3.6",
  "title": "Árbol oficial de elección de bid strategy",
  "type": "decision-tree",
  "instruction": "Para cada escenario, recorre el árbol respondiendo Sí/No.",
  "tree": {
    "q": "¿Quieres controlar costos?",
    "branches": [
      {
        "label": "Sí",
        "next": {
          "q": "¿Optimizas valor?",
          "branches": [
            { "label": "Sí", "leaf": "ROAS Goal" },
            { "label": "No", "leaf": "Cost per Result Goal / Bid Cap" }
          ]
        }
      },
      {
        "label": "No",
        "next": {
          "q": "¿Optimizas valor?",
          "branches": [
            { "label": "Sí", "leaf": "Highest Value" },
            { "label": "No", "leaf": "Highest Volume" }
          ]
        }
      }
    ]
  },
  "scenarios": [
    { "context": "Cliente exige ROAS 4x estricto y optimiza por valor.", "expected": "ROAS Goal" },
    { "context": "DTC nuevo busca máximo volumen sin metas de costo.", "expected": "Highest Volume" }
  ],
  "explanation": "Sí+Sí→ROAS · Sí+No→Cost Cap · No+Sí→Highest Value · No+No→Highest Volume."
}
```

**Schema del nodo `tree`:**
- Nodo interno: `{ "q": "pregunta", "branches": [{"label": "Sí", "next": <nodo>}, {"label": "No", "next": <nodo>}] }`
- Hoja terminal (en lugar de `next`): `{ "label": "Sí", "leaf": "Texto del resultado" }`
- Las ramas pueden ser cualquier cantidad (no limitado a 2), pero el ícono ✓/✕ solo se aplica si el label es "Sí"/"No". Otros labels muestran ▸.

**Flujo de la lección:**
1. Se muestra el escenario actual (de `scenarios[]`).
2. Usuario navega el árbol clickeando ramas.
3. Al llegar a una hoja, se compara con `scenarios[i].expected`.
4. Si correcto → "Siguiente escenario". Si incorrecto → -1 ❤️ y "Reintentar".
5. Al resolver todos los escenarios → `finishLesson()`.

**Cuándo usarlo (en lugar de `order` o `match`):**
- Contenido fuente es un diagrama/árbol con ramas (no secuencia lineal).
- El usuario debe aprender qué resultado aplica según condiciones múltiples.
- Ej: bid strategy según costos+valor, attribution según industria+tipo de evento, troubleshooting según síntoma.

### Campo `section` — bloques del sendero (OBLIGATORIO al agregar lecciones)

`renderPath` agrupa las burbujas del sendero con `lesson.section || 'A'`. Los archivos de unidad declaran un objeto `sections` (ej. `b1`, `b2`, `b3`… `bz`) y **cada lección lleva su propio `section`**.

**Si agregas una lección sin `section` a una unidad que sí usa sections, cae en un grupo fantasma 'A' y se dibuja fuera de lugar** (antes de todo, o después de las flashcards). Al agregar una lección, cópiale el `section` de la lección vecina donde debe quedar — normalmente el mismo que `<N>.flash` (`bz`) si va al final.

### Reglas para escribir contenido educativo

1. **Las lecciones tipo "concept" deben DESARROLLAR el concepto, no telegrafiar.** Cuando introduces un término nuevo (sobre todo si está en inglés), explícalo con tus palabras: qué es, para qué sirve y de dónde viene. Apunta a 4-6 oraciones por card. Si un concepto trae varios sub-términos (ej. "Brand Lift" trae *brand awareness*, *ad recall*, *message association*), dedica una card aparte a desglosarlos uno por uno. Mejor varias cards digeribles que una sola densa.
   - **Nunca dejes un término en inglés sin traducir/explicar la primera vez.** Formato: `<strong>término en inglés</strong> (traducción o explicación corta)`. Ej: "el <strong>cost per result</strong> (costo por resultado)".
   - **Cada concepto nuevo lleva un ejemplo concreto.** Usa un negocio ficticio con nombre (ej. "Hotel Lumière", "Aceros del Bajío") y aterriza el concepto en un caso real.
   - **Business cases VARIADOS por industria (regla de Randall, 2026-07-04).** Los casos y ejemplos — **incluidos los casos integradores** — deben cubrir industrias distintas (retail, B2B, servicios, salud, banca, alimentos, ecommerce, educación, seguros, viajes...) para que cualquiera entienda cómo aplica el concepto en su giro y por qué un concepto encaja mejor en unos casos que en otros. **Kenet Solar aparece de vez en cuando como un caso más** (en meta-400: un caso intermedio en m1 y el integrador final de m7), **nunca como el caso fijo**: NUNCA convertir todos los ejemplos ni todos los integradores a Kenet Solar.
   - **REDACCIÓN AUTOCONTENIDA (regla de Randall, 2026-07-05).** El usuario NO tiene el material fuente: nunca escribir como si ya hubiera leído el libro/PDF de origen ("el autor del libro...", "como vimos en el capítulo...") ni referir material que la app no contiene ("el video", "la figura 2.3"). Los negocios de ejemplo se PRESENTAN la primera vez que aparecen en cada lección ("Imagina un hotel en Cancún...", "Una refaccionaria en Torreón quiere..."), nunca se sueltan por nombre como si fueran conocidos ("la instalación del Hotel Casa Marina" ❌). Las metáforas no deben confundirse con material del curso (ej. "como el video del día completo" parece referir un video real).
   - **Incluye una card de aplicación en la plataforma** cuando el concepto se configure en algún lado: "Cómo se ve esto en Ads Manager (paso a paso)", con la ruta de menús (ej. `Ads Manager → Experiments → A/B Test`).
   - Esto aplica a **contenido nuevo y a reescrituras**. El estándar de referencia es la lección 6.17 de meta-410 (A/B Test, Brand Lift, Conversion Lift).
2. **Cada lección debe tener al menos 1 MCQ** al final para validar comprensión.
3. **Los MCQ deben tener distractores plausibles**, no obvios. El examen real es así.
4. **La explanation de un MCQ debe enseñar**, no solo decir "es la B porque sí". Explica por qué las otras opciones son trampas.
5. **El último item de un día siempre es flashcards** (lección con `type: "flashcards"`) para repaso espaciado.
6. **Apunta a 5-7 lecciones por día** + 1 de flashcards. No menos de 4, no más de 8.
7. **Cada lección debe tomar 8-15 minutos** completarla. Calibra cantidad de cards.
8. **ENSEÑA ANTES DE EVALUAR (regla anti-frustración).** Ninguna actividad (`order`, `match`, `decision-tree`, `lightning`, MCQ) debe evaluar contenido que el usuario no haya visto antes en una card o lección previa del mismo día. Una actividad sobre material no enseñado está destinada a fracasar y obliga a aprender a prueba y error, quemando vidas injustamente.
   - El motor mitiga esto con la **fase de estudio**: la primera vez que se abre un `order`/`match`, muestra el material RESUELTO (pasos en orden / pares correctos) y el usuario practica después. En repasos arranca directo en práctica con botón 📖 para re-estudiar.
   - Las lecciones `order` y `match` aceptan un array opcional `cards` (tipos `concept`/`tip`/`warn`/`quote`/`kvtable`) que se muestra en la fase de estudio para dar contexto. Úsalo cuando la secuencia/pares vengan de una fuente que el día no desarrolló a fondo (ej. "el PDF oficial define 6 pasos…").
   - En `order`, la `explanation` también se muestra durante el estudio como "POR QUÉ ESTE ORDEN".

---

## 6. Sistema de gamificación (referencia, no modificar sin pedir)

El motor implementa estas mecánicas. Si Randall pide cambios, modifica `index.html` con cuidado.

### XP
- Lección perfecta (0 errores): **+30 XP** (x multiplicador de dificultad)
- Lección con errores: `Math.max(10, 25 - errores*3)`
- Flashcard acertada (✓): +3 XP · fallada (✗): +1 XP
- Quiz de unidad aprobado: +60 XP · diagnóstico: +40 · simulacro: +100
- Quick Quiz (práctica): +2 XP por acierto
- Cofre de bloque: +20 XP · Meta diaria cumplida: +50 XP (1 vez/día)
- Battle ganado: +25 XP + 2 por acierto
- **Perfect Combo:** 3 lecciones perfectas seguidas → la siguiente da x2 XP
- Al ganar XP aparece un **"+N XP" flotante** junto al contador del header (refuerzo visual, no quitar)

### Niveles (100) y rangos (10)
El motor genera 100 niveles con curva exponencial (constante `LEVELS`):
`XP(n) = round(20·(n-1)^1.3 + max(0, n-15)^2.3 · 8)` — N10≈344, N20≈1,228, N50≈30,120, N100≈192,340.
Cada 10 niveles = 1 rango (constante `LEVEL_RANKS`): Novato (1-9), Aprendiz (10-19), Estudiante (20-29), Practicante (30-39), Competente (40-49), Avanzado (50-59), Experto (60-69), Maestro (70-79), Sabio (80-89), Leyenda Meta (90-100).

### Battles estilo Pokémon Red/Blue
Al terminar una lección hay ~20% de probabilidad (cooldown 2h, mínimo 2 lecciones ese día y 2 ❤️) de que aparezca un líder de gimnasio de Kanto que reta con MCQs de repaso de lecciones YA completadas. Sistema HP: cada acierto baja 20% al rival, cada error te baja 20% a ti. Se conquistan/defienden 8 medallas (constantes `LEADERS`, `BADGES`, `BATTLE_CONFIG`). Perder contra Giovanni = game over (roba TODAS las medallas). La Trainer Card (vitrina de medallas) vive en Logros. Se puede desactivar en Ajustes. Sprites de PokéAPI (MIT) en `content/battles/`. Durante el combate suena **"Battle Theme A" de cynicmusic** (CC0 dominio público, `content/battles/music/battle-theme-a.mp3`, 752KB mono), con fallback a un loop chiptune sintetizado si el archivo no carga. NO usar el theme oficial de Pokémon (copyright Nintendo, repo público). Además suenan los **cries 8-bit originales de Game Boy** (`playCry`, archivos de PokeAPI/cries `legacy` en `content/battles/cries/<pokeId>.ogg`, ~8KB c/u): cry del rival al aparecer y cry del que cae al KO. Son la única excepción a la regla de "SFX sin archivos" (mismo estatus fan-use que los sprites).

### Mecánicas Hook (no quitar sin preguntar)
- **Anillo de meta diaria** en home (conic-gradient: lecciones de hoy vs meta)
- **Banner de racha en riesgo** en home si no has estudiado hoy y hay racha viva
- **Encadenado de lecciones**: la pantalla de lección completa ofrece "Siguiente lección →" directo + cuánto falta para la meta diaria
- **Celebración de racha**: toast + haptic cuando la racha crece (1 vez/día)
- **Animaciones de refuerzo**: entrada de cards, pop/shake en MCQ, XP flotante, pulso del cofre, flip 3D real en flashcards, brillo periódico en la barra de progreso
- **Sonidos (SFX)**: chimes sintetizados con WebAudio en `playSfx()` — cero archivos de audio, 100% offline. Eventos: correct/wrong/flip/complete/perfect/levelup/chest/streak/battleHit/battleWin. Toggle en Ajustes (`DB.soundEnabled`). NO sustituir por archivos de audio ni CDNs.

### Dominio por evidencia cruzada (barras 1-3)

Modelo tomado de las *recall bars* de [Mural](https://github.com/ujanjan/mural): un tema NO se da por dominado por acertarlo una vez. Hace falta evidencia **repetida**, en **contextos distintos** y **espaciada** en el tiempo.

- La unidad de "tema" es la lección: `conceptStats['courseId|dayId|lessonId']`. Se deriva del sendero que ya existe — **no hay que taggear nada en los JSON de contenido**.
- Contextos que cuentan: `lesson` (MCQ del sendero) · `flash` (flashcards del día) · `practice` (hub ⚔️) · `recall`.
- Barras: **1** = evidencia suelta · **2** = 2+ contextos distintos · **3** = 2+ contextos Y 2+ días distintos Y sin fallos en los últimos 7 días (`EVIDENCE_DECAY_DAYS`).
- Un fallo reciente tumba la tercera barra; a los 7 días se recupera sola.
- Los quizzes y el simulacro no alimentan las barras: ya pesan aparte en el componente "Exámenes" del readiness.

### Readiness — ¿listo para el examen?

La idea también viene de Mural ("*the language app you eventually delete*"): la meta no es estudiar para siempre, es llegar a un umbral claro y presentar. Card en el home (curso principal) y en la vista de cada curso.

`courseReadiness(courseId)` combina cuatro componentes, todos derivados de datos que el motor ya guardaba:

| Componente | Peso | De dónde sale |
|---|---|---|
| Cobertura | 30% | lecciones completadas / total |
| Dominio | 30% | temas con 3 barras / total |
| Exámenes | 25% | `bestScore` de los unit-quiz + simulacro (pesa doble); quiz pendiente cuenta 0 |
| Sin errores | 15% | deuda de `wrongAnswers` **relativa a lo ya cubierto** (si no has estudiado, vale 0) |

`READY_THRESHOLD = 85`. Al cruzarlo el card se pone verde y dice "Listo para presentar". Debajo, el motor nombra el **cuello de botella** (el componente que más puntos te está costando, ponderado) con una acción concreta.

### Voz — `speechSynthesis`

Botón 🔊 en las dos caras de cada flashcard y en cada término del glosario (este en `en-US`, casi todos son términos en inglés). API nativa del navegador: cero dependencias, cero archivos, funciona offline una vez instalada la PWA — respeta la regla de oro 4. Segundo tap sobre el mismo botón detiene; `navTo()` corta la voz al cambiar de vista.

**Modo escuchar (🎧).** El header de toda lección estándar trae un botón 🎧 que lee en voz alta la tarjeta actual (`listenCard` → `cardSpeechText`): concept, tip, warn, quote, kvtable, mcq/fill (con la explicación si ya respondiste) y recall (con la respuesta modelo si ya la revelaste). `speakText` parte el texto en trozos de ~220 caracteres por oración y los encola, porque algunos motores de voz cortan los textos largos a la mitad. En una tarjeta `audio-embed`, 🎧 reproduce o pausa el audio grabado en vez de usar la voz sintética. `nextCard` y `exitLesson` cortan la voz.

### Iconografía propia — `ICO` + `icoize()`

La app tiene un set de 25 iconos propios (sólidos, con color, `viewBox` 24×24) en la constante `ICO`. Sustituyen a los emojis del sistema, que se ven distintos en cada teléfono y no son nuestros.

**Cómo funciona — esto es lo importante:** el motor **sigue escribiendo emojis normales en su código** (`❤️`, `🔥`, `🏆`…). La traducción ocurre en **un solo lugar**: `render()` pasa el HTML por `icoize()` antes de inyectarlo. Se probó primero reescribir los ~200 sitios del código uno por uno y fue un error — rompía strings, atributos y los mensajes de `showToast`. El enfoque de un solo punto es más simple, no toca ningún string y se revierte quitando una llamada.

- `icoize(html)` — solo reemplaza en el **texto entre etiquetas** (`>…<`). Nunca toca un atributo (`data-ico`, `title`, `alt`) ni el interior de un `<svg>`.
- `icoText(s)` — para un valor suelto que va a un contenedor (icono del toast, overlay de logros). Esos dos pasaron de `textContent` a `innerHTML`; es seguro porque el icono **siempre** sale de una constante nuestra, nunca de contenido externo.
- Para agregar un icono: añádelo a `ICO` y mapea su emoji en `ICO_FOR`. No hay que tocar nada más.

**Lo que NO cubre, y por qué:**
- **El mensaje de `showToast`** va a `.textContent` a propósito (el texto puede ser dinámico). Un emoji dentro del mensaje se queda como emoji.
- **Los emojis en CSS `content:''`** (la llama de `.streak-hero::after`, la ✕ de `.tc-badge.lost`). Una regla CSS no admite SVG inline; habría que pasarlos a `background-image` con data-URI.
- **Los emojis del contenido de los cursos** (los JSON) sí se traducen si coinciden con el mapa, porque pasan por el mismo `render()`.

### Certificado de preparación

Cuando un curso cruza `READY_THRESHOLD` (85%) por primera vez, `ensureCertificate()` emite un certificado y lo guarda en `DB.certificates[courseId]` = `{date, pct, id, parts}`. **Se conserva aunque el readiness baje después**: lo ganaste ese día. Otorga el logro `exam_ready` y aparece como acceso dorado dentro del card de readiness. La vista `certificate` muestra nombre, curso, porcentaje, los 4 componentes, fecha y folio (`CER-XXXX-XXXX`, derivado del curso y la fecha), más un botón al examen oficial si el `meta.json` trae `exam_url`.

Lleva una nota explícita: es un certificado **interno**, dice que estás listo para presentar, **no sustituye la certificación oficial**. No usar logos ni nombres de terceros en él.

### Emblemas de rango — `rankBadgeSvg(idx, locked)`

Cada uno de los 10 rangos tiene emblema propio: hexágono tipo medalla con color por escalón (los primeros, colores vivos; Experto oro, Maestro platino, Sabio diamante, Leyenda iridiscente) y un glifo (`RANK_GLYPHS`). Aparecen en el header junto al nivel, la tarjeta de nivel de Logros, la lista de rangos, Ajustes y el overlay de subir de nivel. Los rangos aún no alcanzados se muestran como **silueta gris** (`locked`): ves qué viene, no un candado. `LEVELS[n].ri` da el índice de rango de cada nivel.

### Favicon y badge de racha — `updateStreakIcon()`

Idea tomada del teardown de Duolingo (el icono refleja tu racha), **sin la parte de castigo** que el propio teardown desaconseja: el icono nunca se degrada, solo gana una marca. Check verde = ya estudiaste hoy; punto naranja (sin signo de alarma) = racha viva y hoy aún no estudias. El título de la pestaña lleva `🔥N`. En la PWA instalada usa la Badging API (`setAppBadge`) donde el sistema la soporta. Se recalcula al final de cada `render()`, con caché por estado.

**Límite:** el icono de la pantalla de inicio de una PWA instalada no se puede cambiar desde JS; lo que cambia es el favicon de la pestaña y, donde existe, el puntito de la Badging API.

### Práctica (pestaña ⚔️)
- **Repaso inteligente (mix)**: 10 flashcards priorizadas con **SM-2 real** (`sm2Update`: acierto=q4, fallo=q1; intervalos 1d→6d→ivl·ef; fallo resetea). Orden: vencidas → nunca vistas → próximas a vencer
- **Quick Quiz**: 10 MCQs al azar de lecciones completadas de TODOS los cursos activos; no toca `quizProgress`
- **Emparejar / Ordenar**: abre una actividad match/order AL AZAR en modo práctica (`PRACTICE_MODE='activity'`): sin costo de ❤️, sin marcar progreso del sendero, XP fijo (10 perfecta / 5 normal), regresa al hub
- **Repasar errores**: flashcards generadas de `wrongAnswers`
- **Estadísticas** (Ajustes → 📊): precisión por unidad, flashcards vencidas SM-2, errores activos, minutos
- El hub agrega contenido de todos los cursos activos (no hardcodear curso)

### Dificultad — vidas, escudos y nivel de contenido

4 niveles visibles + 1 oculto. Cada uno define cuántas vidas (corazones) y escudos tiene el usuario, además del nivel cognitivo esperado del contenido:

| Nivel | key | Vidas | Escudos | Contenido esperado |
|---|---|---|---|---|
| 🌱 Fácil | `easy` | 5 | 3 | Principiante. Conceptos directos, sin trampas. |
| ⚖️ Intermedio | `medium` | 3 | 2 | Intermedio. Distractores plausibles. |
| 🔥 Avanzado | `hard` | 2 | 1 | Avanzado. Abreviaciones **con** el nombre completo entre paréntesis, ej. "CAPI (Conversions API)". |
| 🏆 Experto | `expert` | 1 | 0 | Senior. Abreviaciones de términos en inglés **sin** ayuda, casos prácticos complejos, escenarios multi-variable. |
| 💎 Perfeccionista | `perfectionist` | 1 | 0 | Oculto (se desbloquea al 99% de éxito sobre ≥20 lecciones). +100% XP. |

**Regla de autoría (contenido nuevo):** los MCQ ya se filtran por su tag `difficulty` (`easy`/`medium`/`hard`). Al escribir contenido nuevo, calibra el fraseo al nivel: paréntesis explicativos en `hard`, abreviaciones en inglés y casos complejos en preguntas tag `hard` pensadas para Experto. **No reescribir contenido viejo retroactivamente** salvo que Randall lo pida.

### Corazones (vidas)
- Máximo según nivel de dificultad (ver tabla arriba)
- Cada respuesta incorrecta = -1 corazón
- Regeneración: **full refill** al máximo del nivel tras un ciclo (10/15/30/60 min según nivel)
- Si llegan a 0, el usuario debe esperar para empezar nueva lección
- **Bono Experto:** cada 3 lecciones perfectas seguidas → +1 vida extra (tope 5)

### Escudos de racha
- Banco fijo por nivel de dificultad (Fácil 3 · Intermedio 2 · Avanzado 1 · Experto 0)
- Si faltas **exactamente 1 día**, se consume 1 escudo automáticamente y la racha sobrevive
- **No** se ganan por milestones de racha (lógica vieja eliminada)
- Se recargan al máximo del nivel **cada 7 días** (`refillShieldsWeekly`). Nunca bajan lo ya ganado; tope global `MAX_SHIELDS = 3`
- Al cambiar de dificultad, el banco se resetea al máximo del nuevo nivel
- **Bono Experto:** examen del día (unit-quiz) con 100% → +1 escudo

### Racha
- +1 día si estudia hoy y estudió ayer
- Si falta 1 día y hay escudo → se consume, racha sobrevive
- Reset si pasa más de 1 día sin estudiar y no hay escudo
- Achievements: 3 días, 7 días

### Logros (12 badges)
Ver constante `ACHIEVEMENTS` en `index.html`. Si Randall pide nuevos, agrégalos a esa constante.

---

## 7. Convenciones de código y estilo

### Para archivos JSON (contenido)
- Indentación: 2 espacios
- Comillas: dobles (`"`) — es JSON estándar
- Encoding: UTF-8 con BOM no
- Una línea final vacía al terminar el archivo
- HTML inline en strings: usa `<strong>`, `<em>`, `<br/>`. NO uses tags complejos como `<div>` o `<table>`.

### Para `index.html` (cuando toque modificar)
- Indentación: 2 espacios
- Comillas: simples (`'`) en JS
- Comentarios: en español, breves
- NO romper la estructura de secciones marcadas con `// ============ NOMBRE ============`
- NO mover funciones de lugar sin razón

### Para mensajes de commit
Formato: `tipo(scope): descripción corta`

Tipos:
- `feat` — feature nueva (curso, día, lección, mecánica)
- `fix` — bug fix
- `docs` — cambios a `CLAUDE.md` o `README.md`
- `style` — cambios de diseño visual
- `refactor` — cambios al motor sin afectar comportamiento
- `chore` — mantenimiento (gitignore, configs)

Ejemplos buenos:
- `feat(meta-410): agregar día 2 - campaign objectives`
- `fix(motor): scroll jumps al responder MCQ`
- `feat: nuevo curso ITIL Foundation`
- `docs: actualizar schema de mcq multi`

Ejemplos malos:
- `update`
- `cambios`
- `wip`

---

## 8. Testing checklist (antes de cada commit)

Validaciones mentales:

- [ ] Si modifiqué un JSON: **¿es JSON válido?** Sin trailing commas, comillas balanceadas.
- [ ] Si agregué una lección: **¿tiene al menos 1 MCQ?**
- [ ] Si agregué un curso: **¿está en `courses.json`?**
- [ ] Si quité `locked: true`: **¿el archivo de la unit ya existe?**
- [ ] Si modifiqué `index.html`: **¿no rompí los cursos existentes?**
- [ ] Si agregué HTML en strings: **¿no usa comillas dobles sin escape?**
- [ ] Si modifiqué la estructura: **¿la app vieja del usuario en celular sigue funcionando con el nuevo formato?** (compatibilidad hacia atrás)

---

## 9. Roadmap del proyecto

### Esta semana (URGENTE — examen Meta sábado)
- [x] Día 1 Meta 410-101 — listo
- [ ] Día 2 Meta — Campaign Objectives + ODAX + optimization events
- [ ] Día 3 Meta — Buying Types + Bid Strategies + Learning Phase
- [ ] Día 4 Meta — Signals & Data (Pixel, CAPI, eventos, parámetros)
- [ ] Día 5 Meta — Audiences (Custom, Lookalike, Advantage+) + Catálogos
- [ ] Día 6 Meta — Creative + Measurement (A/B, Brand Lift, Conversion Lift)
- [ ] Día 7 Meta — Simulacro completo de 60 preguntas

### Después del examen Meta (orden por prioridad)
- [ ] Curso CFE / UV Interconexión Solar (alta prioridad — uso diario en Kenet)
- [ ] Curso Sistemas Fotovoltaicos — Corella 2da edición
- [ ] Curso Liderazgo Transformacional (Guillermo)
- [ ] Curso ITIL
- [ ] Curso CVS

### Features pendientes del motor
- [x] Modo simulacro de examen (60 preguntas, 105 min, mapa de preguntas con salto y marcado 🚩)
- [x] Cards tipo "match" (emparejar conceptos)
- [x] Cards tipo "order" (ordenar pasos)
- [x] Repaso espaciado SM-2 completo (ease factor, intervalos 1d/6d/ivl·ef, reset en fallo)
- [x] Quick Quiz en práctica (10 MCQs al azar multi-curso)
- [x] Vista de estadísticas (precisión por unidad, vencidas SM-2, errores activos)
- [x] Práctica de match/order desde el hub (al azar, sin costo de corazones)
- [ ] Recordatorios diarios (limitado: GitHub Pages no tiene push server; requeriría Notification API con la app abierta)

### Política de archivos pesados (decidida 2026-06-09)
- **NO subir audio/video/imágenes pesadas al repo.** Los m4a/mp4/mindmaps de meta-410 se eliminaron.
- Video → YouTube unlisted con card `video-embed`. Audio → Drive público con `audio-link`.
- Imágenes: solo si pesan <300KB (comprimir/WebP antes de subir).
- El service worker sirve `content/*/assets/` cache-first SIN revalidación: si cambias un asset, cámbiale el nombre de archivo.
- **Excepción (decidida por Randall 2026-11-13): audios cortos dentro de la app.** Resúmenes de ~1 min, mono 48 kbps, **< 1 MB** cada uno, en `content/<curso>/assets/` con nombre versionado (`audio-day1-v1.mp3`; si se regenera → `-v2`). Se muestran con card `audio-embed`. El guion se guarda en `source/<curso>/audio/guiones.md`. Comando de compresión: `ffmpeg -i in.mp3 -ac 1 -b:a 48k content/<curso>/assets/audio-dayN-v1.mp3`. Video sigue FUERA del repo.
- El service worker deja pasar directo a la red las peticiones con header `Range` (audio/video piden por rangos y la Cache API no guarda respuestas 206).

### Multimedia con ElevenLabs y Twilio (2026-11-13)

Claude Code tiene conectado el MCP de ElevenLabs. Twilio está importado dentro de ElevenLabs (no hay MCP de Twilio aparte).

- **Cobertura (2026-11-13):** meta-410 día 1-6, meta-400 módulo 1-7, paneles-corella módulo 1. Las unidades sin recall (glosarios, simulacros) no llevan audio. Guiones de cada curso en `source/<curso>/audio/guiones.md`.
- **Resúmenes en audio** (meta-410, día 1 a 6): voz **Randy De Rosas** (`voice_id` EQdYdxpkGKpMCC5nZMgi, acento mexicano), modelo `eleven_v4`. Son la primera tarjeta de cada lección `N.recall`: escuchas el resumen y luego lo explicas con tus palabras. Costo real: ~5,650 créditos (~$1 USD) los 6. El guion sale de las respuestas modelo de los recall de ese día, así que no mete material nuevo.
- **Video** (piloto): 5 s, 720p, `bytedance-seedance-v2.5`, ~14,000 créditos (~$2.55 USD) por clip. Caro para lo que dura: úsalo solo para metáforas visuales puntuales. Se sube a YouTube unlisted y entra con `video-embed`. Nunca al repo.
- **Tutor por llamada**: agente de ElevenLabs "Tutor Meta 410 · Centro de Estudios" (`agent_0701m79qrsa0e1gvcga8sqhj1vdm`), en español y con voz Randy. Su base de conocimiento es `source/meta-410/tutor/kb-tutor.txt` (los 6 guiones + las respuestas modelo de los recall), que ElevenLabs lee desde la URL raw de GitHub (documento `QwsmY74Nh0hxxQGynJCA`). Si cambias el contenido de los recall, regenera ese archivo y vuelve a crear el documento de la base de conocimiento. Hace repaso activo: una pregunta a la vez, te pide explicarlo con tus palabras y te dice qué concepto te faltó.
- **Número del tutor:** SOLO la línea de prueba `+1 586 328 0753` (`phnum_0701m4a18fm9fb8b965t0w38c0m6`, etiqueta "TEST +1 586").
- ⚠️ **NUNCA tocar, reasignar ni probar con las 4 líneas de Kenet en Kommo (MVA, MTY, TRC, SLT).** Son líneas de operación de la empresa.
- Para llamadas salientes (que el tutor te marque) o recordatorios diarios hace falta el número de Randall y un disparador programado: pídelo antes, no lo inventes.

---

## 10. Resolución de problemas comunes

### "La app no carga el contenido nuevo"
- Causa probable: caché del service worker.
- Fix: en config de la PWA, agregar versión al fetch o pedir al usuario "fuerza refresh" (jalar pantalla hacia abajo).

### "El JSON está bien pero la app se queda en blanco"
- Causa probable: HTML inline con comillas dobles sin escapar.
- Fix: usa comillas simples dentro del HTML embebido en JSON, o escapa con `\"`.

### "Mi progreso se borró"
- Causa probable: cambio de versión de localStorage key, o `resetAll()` accidental.
- Fix: localStorage es por dominio. Si cambiaste el key sin migrar, los datos viejos siguen ahí pero la app no los lee. Implementar migración antes de cambiar la key.

### "Los cursos viejos no funcionan después de actualizar el motor"
- Causa probable: cambio de schema sin compatibilidad hacia atrás.
- Fix: SIEMPRE soportar schemas antiguos. Si cambias, deja el fallback.

### "Subí cambios pero GitHub Pages no actualiza"
- Espera 2-3 minutos. GitHub Pages tiene latencia de deploy.
- Si después de 5 min no actualiza, verifica el commit en la web de GitHub.
- Si el commit existe pero la página no actualiza, fuerza refresh del navegador (cache).

---

## 11. Antes de cerrar la sesión

Cuando termines una tarea, **siempre confirma a Randall**:

1. ✅ Qué archivos modificaste/creaste (lista breve)
2. ✅ Qué commit hiciste (mensaje y SHA corto)
3. ✅ Si la app va a actualizarse en producción (sí/no)
4. ✅ Qué debería verificar Randall en el celular (ej. "abre el Día 2 y revisa que las MCQs tengan sentido")
5. ✅ Próximo paso sugerido (opcional)

---

## 12. Cosas que NO eres

- **No eres un sistema multi-usuario.** Solo Randall.
- **No tienes backend.** Solo localStorage.
- **No tienes analytics.** Solo el contador de progreso del usuario.
- **No tienes auth.** Es público pero pensado para uso personal.
- **No eres una app de App Store.** Es una PWA.

---

**Versión de este CLAUDE.md:** 1.5
**Última actualización:** Viernes 13 de noviembre de 2026 (audios por día con ElevenLabs, modo escuchar 🎧, tutor por llamada, excepción de audio <1 MB). Antes, 16 de septiembre de 2026 (card `recall`, dominio por evidencia cruzada, readiness de examen, voz nativa, campo `section`, iconografía propia `ICO`/`icoize`, auditoría de contraste, certificado, emblemas de rango, favicon de racha)
**Autor original:** Claude (en sesión Claude.ai con Randall)
