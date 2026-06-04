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
5. Mensaje de commit: `feat([curso]): agregar [unitId] - [descripción corta]`
6. Confirma a Randall: cuántas lecciones, cuántas MCQs, cuántas flashcards generaste.

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
6. Mensaje de commit: `feat: nuevo curso [nombre]`

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

**Tu workflow:**
1. **Si el PDF está en el repo** (Randall lo subió), léelo.
2. **Si no está disponible**, pregunta a Randall que te pegue el contenido relevante o que copie las secciones clave en el chat.
3. Procesa el contenido y genera estructura: cuántos módulos, qué temas por módulo, cuántas lecciones por módulo.
4. **Pregúntale a Randall si aprueba la estructura ANTES de generar todo el contenido.** No gastes tokens generando 7 días si la estructura está mal.
5. Una vez aprobada, genera todo siguiendo Tareas B + A.

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

#### `decision-tree` — lección de árbol de decisión interactivo (full-lesson)

Tipo de **lección completa** (no card individual). Usar cuando el contenido fuente es un árbol/diagrama de decisión con bifurcaciones Sí/No (o múltiples ramas), donde forzar un `order` lineal rompe la lógica.

```json
{
  "id": "3.6",
  "title": "Árbol oficial de elección de bid strategy",
  "type": "decision-tree",
  "instruction": "Para cada escenario, recorré el árbol respondiendo Sí/No.",
  "tree": {
    "q": "¿Querés controlar costos?",
    "branches": [
      {
        "label": "Sí",
        "next": {
          "q": "¿Optimizás valor?",
          "branches": [
            { "label": "Sí", "leaf": "ROAS Goal" },
            { "label": "No", "leaf": "Cost per Result Goal / Bid Cap" }
          ]
        }
      },
      {
        "label": "No",
        "next": {
          "q": "¿Optimizás valor?",
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

### Reglas para escribir contenido educativo

1. **Las lecciones tipo "concept" deben DESARROLLAR el concepto, no telegrafiar.** Cuando introduces un término nuevo (sobre todo si está en inglés), explícalo con tus palabras: qué es, para qué sirve y de dónde viene. Apunta a 4-6 oraciones por card. Si un concepto trae varios sub-términos (ej. "Brand Lift" trae *brand awareness*, *ad recall*, *message association*), dedica una card aparte a desglosarlos uno por uno. Mejor varias cards digeribles que una sola densa.
   - **Nunca dejes un término en inglés sin traducir/explicar la primera vez.** Formato: `<strong>término en inglés</strong> (traducción o explicación corta)`. Ej: "el <strong>cost per result</strong> (costo por resultado)".
   - **Cada concepto nuevo lleva un ejemplo concreto.** Usa un negocio ficticio con nombre (ej. "Hotel Lumière", "Aceros del Bajío") y aterriza el concepto en un caso real.
   - **Incluye una card de aplicación en la plataforma** cuando el concepto se configure en algún lado: "Cómo se ve esto en Ads Manager (paso a paso)", con la ruta de menús (ej. `Ads Manager → Experiments → A/B Test`).
   - Esto aplica a **contenido nuevo y a reescrituras**. El estándar de referencia es la lección 6.17 de meta-410 (A/B Test, Brand Lift, Conversion Lift).
2. **Cada lección debe tener al menos 1 MCQ** al final para validar comprensión.
3. **Los MCQ deben tener distractores plausibles**, no obvios. El examen real es así.
4. **La explanation de un MCQ debe enseñar**, no solo decir "es la B porque sí". Explica por qué las otras opciones son trampas.
5. **El último item de un día siempre es flashcards** (lección con `type: "flashcards"`) para repaso espaciado.
6. **Apunta a 5-7 lecciones por día** + 1 de flashcards. No menos de 4, no más de 8.
7. **Cada lección debe tomar 8-15 minutos** completarla. Calibra cantidad de cards.

---

## 6. Sistema de gamificación (referencia, no modificar sin pedir)

El motor implementa estas mecánicas. Si Randall pide cambios, modifica `index.html` con cuidado.

### XP
- Lección perfecta (0 errores): **+30 XP**
- Lección con errores: `Math.max(10, 25 - errores*3)`
- Flashcard "Fácil": +3 XP
- Flashcard "Difícil": +2 XP
- Flashcard "No supe": +1 XP

### Niveles (10)
1. Novato — 0 XP
2. Aprendiz — 100 XP
3. Estudiante — 250 XP
4. Practicante — 500 XP
5. Competente — 850 XP
6. Avanzado — 1300 XP
7. Experto — 1850 XP
8. Maestro — 2500 XP
9. Sabio — 3300 XP
10. Leyenda Meta — 4200 XP

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
- [ ] Modo simulacro de examen (60 preguntas, 105 min, condiciones reales)
- [ ] Cards tipo "match" (emparejar conceptos)
- [ ] Cards tipo "order" (ordenar pasos)
- [ ] Vista de estadísticas detalladas (precisión por tema, etc.)
- [ ] Recordatorios diarios (notificaciones)
- [ ] Repaso espaciado (algoritmo SM-2 para flashcards)

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

**Versión de este CLAUDE.md:** 1.0
**Última actualización:** Domingo 10 de mayo de 2026
**Autor original:** Claude (en sesión Claude.ai con Randall)
