---
name: notebooklm-import
description: Workflow para convertir contenido de NotebookLM (Study Guides, Mind Maps, Audio Overviews) en cursos JSON de la app. Diseñado para flujo Coursera (especialización → curso → módulo). Úsalo cuando Randall mencione "tengo el output de Notebook / un Study Guide", "vamos a procesar el módulo X del curso Y", "agregar la especialización Z a la app", suba archivos a `source/<especializacion>/<curso>/<modulo>/`, o pegue texto largo estructurado que claramente venga de un Study Guide de Notebook.
---

# NotebookLM → Centro de Estudios Randall

Randall procesa transcripciones de Coursera con NotebookLM y quiere que las salidas se conviertan en cursos jugables dentro de su PWA. Esta skill cubre el workflow completo: cómo recibir el material, cómo estructurarlo respetando la jerarquía Coursera, cómo agregar multimedia, y cómo validar antes de mergear.

## Jerarquía Coursera → app

```
Especialización Coursera (5 cursos)
└── Curso Coursera (10-20 módulos)         ─── 1 carpeta en content/<id-curso>/
    └── Módulo Coursera (varios videos)     ─── 1 unit/día en meta.json
        └── Video (.txt)                    ─── material fuente
```

Esto significa:
- **1 especialización Coursera** = 4-5 cursos en `content/` agrupados por `specialization` tag (ver `CLAUDE.md` §2)
- **1 curso Coursera** = 1 carpeta `content/<id-curso>/` con su meta.json
- **1 módulo Coursera** = 1 unit en el meta.json + 1 archivo `<modulo-id>.json` con 5-7 lecciones A→B→C→D

## Estructura de archivos esperada

```
source/
└── <id-especializacion>/
    ├── README.md                              # qué es la especialización
    ├── <id-curso-1>/
    │   ├── transcripciones/                   # .txt originales (input para Notebook)
    │   │   ├── m1-v1.txt
    │   │   └── ...
    │   ├── m1/                                # outputs Notebook para módulo 1
    │   │   ├── study-guide.md
    │   │   ├── mindmap.png                    # (opcional, ver multimedia skill)
    │   │   └── audio-link.txt                 # (opcional)
    │   ├── m2/
    │   └── ...
    └── <id-curso-2>/

content/
├── courses.json                               # con specializations[] + courses[]
├── <id-curso-1>/                              # cada curso Coursera = 1 carpeta
│   ├── meta.json                              # specialization: "<id-esp>" + units (módulos)
│   ├── m1.json                                # lecciones A→B→C→D del módulo 1
│   ├── m2.json
│   ├── ...
│   └── assets/                                # mindmaps + imágenes
└── <id-curso-2>/
```

## 1. Triage al recibir material

Cuando Randall te pase contenido, primero clasificalo:

| Tipo de input | Cómo viene | Qué hago |
|---|---|---|
| Study Guide / Briefing Doc | Texto largo pegado o archivo `.md`/`.txt` en `source/<curso>/` | Mi input principal. De acá saco temas y armo lecciones. |
| Transcripción cruda de video | `.txt` con texto sin estructurar | Pedirle que pase por NotebookLM primero. Procesarla cruda gasta tokens innecesarios. |
| Mind map | PNG/SVG/JPG | Guardar en `content/<curso>/assets/` y embedir como card tipo `image` |
| Audio Overview de NotebookLM | MP3 (10-20 min, ~15MB) | NO subir al repo. Pedir link de Drive/YouTube. Embed como card `audio-link` |
| Diagrama / screenshot | PNG/JPG | Igual que mind map |

**Regla**: si el input es transcripción cruda, **pedile primero** que pase por NotebookLM con uno de los prompts del [§4 Prompts probados para NotebookLM](#4-prompts-probados-para-notebooklm). El briefing doc denso es mucho más eficiente que el .txt original.

## 2. Estructura pedagógica obligatoria (A → B → C → D)

Cada día/módulo se divide en 4 secciones pedagógicas. **Respetá este patrón** en todo curso nuevo:

| Sección | Tipo | Propósito | Cards típicas |
|---|---|---|---|
| **A — Teoría** | `reading` | Lecturas con conceptos, definiciones, distinciones | `concept`, `kvtable`, `tip`, `warn`, `quote`, 1-2 `mcq` de cierre |
| **B — Práctica** | `match`, `order`, `fill` | Manipular conceptos activamente | Emparejar, ordenar, completar huecos |
| **C — Aplicación** | `scenario`, `reading` (caso) | Casos reales B2B, escenarios industriales mexicanos | `scenario` (caja naranja narrativa), seguido de `mcq` aplicado |
| **D — Validación** | `lightning`, `drill` | Práctica rápida bajo presión | `lightning` (timer global), `drill` muchos MCQs encadenados |
| **Flash final** | `flashcards` | Repaso espaciado | 12-25 cards Q/A |

Cada lección dura ~8-15 min. Apuntá a 6-8 lecciones por día.

### Tipos de card y schema

Los tipos de card disponibles están en `CLAUDE.md` §5. Resumen rápido:

- `concept`, `quote`, `tip`, `warn`, `kvtable`: cards de lectura
- `mcq`: multiple choice (single o `multi:true`)
- `match`: emparejar 2 columnas
- `order`: ordenar pasos (⚠️ ver §6 errores típicos)
- `scenario`: caja narrativa naranja para casos B2B
- `fill`: huecos con opciones
- `flashcards`: Q/A para repaso

## 3. Workflow paso-a-paso

### A) Para una especialización Coursera NUEVA (1ra vez)

1. **Leer el README** de la especialización en `source/<id-esp>/README.md` para entender los 5 cursos.
2. **Proponer a Randall la estructura completa**:
   - 1 entrada en `specializations[]` de `courses.json`
   - 5 entradas en `courses[]`, cada una con `specialization: "<id-esp>"`
   - Cada curso con su `content/<id-curso>/meta.json` listando N módulos como units
3. **Pedir aprobación** de los nombres/ids de los 5 cursos antes de crear carpetas.
4. **Crear todo el esqueleto vacío** (meta.json con units `locked:true`).
5. **Confirmar**: "Esqueleto listo. Decime con qué curso empezamos."

### B) Para un módulo nuevo (típico flujo iterativo)

1. **Localizar el Study Guide** en `source/<id-esp>/<id-curso>/<id-modulo>/study-guide.md` o pegado en el chat.
2. **Leer el material completo**.
3. **Proponer la estructura del módulo** a Randall:
   - 5-7 lecciones siguiendo A→B→C→D
   - Cuántos MCQs, match, order, scenario, flashcards
4. **Pedir aprobación** ANTES de generar contenido (no gastar tokens en algo mal).
5. Si aprueba:
   - **Quitar `locked:true`** del módulo en `meta.json`
   - **Crear `content/<id-curso>/<id-modulo>.json`** con las lecciones
   - **Si es m1 (primer módulo del curso)**: embeber mind map del curso al inicio (sección A) y audio overview del curso al final (sección D). Ver `notebook-multimedia-prompts` skill.
6. **Para cada MCQ**:
   - Distractores plausibles, no obvios
   - `explanation` enseña (no solo "es B")
7. **Validar JSON** mentalmente antes de commit.
8. **Commit**: `feat(<id-curso>): m<N> — <título corto>`
9. **Confirmar a Randall**: archivos creados, conteos, qué revisar en el celular.

## 4. Prompts probados para NotebookLM

Pasale estos a Randall si necesita prompts para sacar contenido denso de NotebookLM:

### Para Study Guide denso (input principal)
```
Crea un Study Guide denso y exhaustivo organizado por temas. Para
cada tema incluí: definiciones precisas, ejemplos del material,
distinciones con conceptos parecidos, errores típicos, y 3-5
preguntas tipo examen con la respuesta correcta y por qué las
otras opciones son trampas.
```

### Para flashcards directas
```
Genera 80 flashcards en formato Q/A sobre los conceptos clave. Las
preguntas deben ser específicas (no "qué es X" sino "cuál es la
diferencia entre X y Y" o "qué pasa cuando..."). Las respuestas
deben ser concisas (máx 2 oraciones).
```

### Para casos B2B aplicados (scenarios)
```
Generá 10 casos prácticos tipo "empresa industrial mexicana con
problema X". Cada caso incluye: contexto del cliente (industria,
tamaño, presupuesto), problema específico, y la solución correcta
según el material con justificación.
```

### Para ordenar pasos (order cards)
```
Listá las secuencias o procesos del material que tengan orden
específico. Para cada secuencia: nombre del proceso, los pasos en
orden correcto, y por qué ese orden importa.
```

### Para distinguir conceptos parecidos (match cards)
```
Listá los conceptos del material que se suelen confundir. Para
cada par: concepto A, concepto B, en qué se parecen, en qué se
diferencian (clave de examen).
```

## 5. Multimedia: cómo embeber

### Imágenes / mind maps (Tier 2 — viven en el repo)

1. Pedir a Randall el archivo (PNG/SVG/JPG)
2. Guardar en `content/<curso>/assets/<descripcion>.png`
3. Embeber en la lección:
```json
{
  "type": "image",
  "src": "content/<curso>/assets/<descripcion>.png",
  "alt": "Mind map de Campaign Objectives",
  "caption": "Vista general · NotebookLM"
}
```

**Importante**: si el tipo `image` no existe todavía en `index.html`, hay que agregarlo al motor primero. Avisar a Randall antes de tocar `index.html`.

### Audio Overviews (Tier 3 — externos)

NO subirlos al repo. Pesan 10-20MB cada uno y saturan GitHub Pages.

1. Pedir a Randall que suba el MP3 a Google Drive (compartido público) o YouTube (unlisted)
2. Embeber como card:
```json
{
  "type": "audio-link",
  "title": "Repaso en audio · 12 min",
  "url": "https://drive.google.com/...",
  "duration": "12:30",
  "source": "NotebookLM Audio Overview"
}
```

Mismo aviso: si el tipo no existe, hay que agregarlo al motor.

### Videos cortos / demos

Igual que audio: externo (YouTube preferido), embeber con tipo `video-embed`.

## 6. Errores típicos a evitar

### En cards `order`
**No pegues el número de orden en el texto del item.** Si el item dice "1. Primero...", "2. Segundo...", el usuario ve la respuesta. El orden correcto sale del array `correctOrder` que el motor maneja por debajo, no del texto. Ya pasó una vez con el día 1 de Meta — chequeá `content/meta-410/day1.json` línea 1.8 como referencia de cómo NO hacerlo y cómo sí.

### En cards `match`
**Cada lado del match debe ser autónomo.** Si el lado izquierdo dice "1. Algo" y el derecho dice "Definición de 1", el match es trivial. Los pares deben emparejarse por significado, no por número.

**Schema correcto del match**: el campo `pairs` debe ser **array de arrays de 2 strings**, NO objetos:
```json
"pairs": [
  ["término A", "definición A"],
  ["término B", "definición B"]
]
```
NO usar `{"id":"x","left":"...","right":"..."}` — el motor accede a `pair[0]` y `pair[1]` directo, los objetos rompen el render (cards salen como "undefined"). Ver `content/meta-410/day1.json` lección 1.7 como referencia.

### En MCQs
- **Distractores plausibles**: si las 3 opciones erradas son obviamente absurdas, no hay reto.
- **La respuesta no debe ser siempre la opción más larga.** Variá longitudes.
- **`explanation` debe enseñar**: explicar por qué la correcta es correcta Y por qué cada distractor trampa.
- **Examen real de certificación**: variar `multi:true` ocasionalmente. En el examen Meta 410 muchas preguntas piden "selecciona 2".

### En `flashcards`
- Preguntas específicas, no genéricas.
- "¿Cuál es la diferencia entre lookalike audience y custom audience?" > "¿Qué es lookalike?"

### En `scenario`
- Mexicanizar los casos: empresa Kenet, cliente industrial, presupuesto en pesos.
- Numeros realistas (presupuesto mensual $50K MXN, no $50M).

## 7. Validación antes de commit

Checklist mental obligatorio antes de cada commit:

- [ ] JSON parseable (sin trailing commas, comillas balanceadas)
- [ ] Si agregué unidad: la quité del `locked:true` en `meta.json`
- [ ] Si agregué curso: está en `content/courses.json`
- [ ] Lección tiene al menos 1 MCQ
- [ ] Cards `order`: items NO empiezan con "1. ", "2. " etc
- [ ] Cards `mcq`: índice `correct` válido (0-indexado), `explanation` presente
- [ ] HTML inline en strings: comillas escapadas o solo simples internamente
- [ ] URLs de imágenes/audio: relativas (`content/...`) no absolutas (`/content/...`)

Comando de validación:
```bash
for f in content/**/*.json; do
  node -e "JSON.parse(require('fs').readFileSync('$f','utf8'))" \
    && echo "✅ $f" || echo "❌ $f"
done
```

## 8. Comunicación con Randall

Cuando termines de procesar material:

1. Listar archivos creados/modificados
2. Resumen de qué se generó: "N lecciones, M MCQs, K flashcards, J cards multimedia"
3. SHA del commit
4. Qué debería revisar en el celular específicamente (ej. "abrí Día 2 lección 2.5 y revisá que el scenario B2B tenga sentido")
5. Próximo paso sugerido

## 9. Estado actual del proyecto

| Curso | Estado | Prioridad |
|---|---|---|
| meta-410 | Día 1 listo · Día 2-7 pendiente | Alta — examen sábado |
| cfe-interconexion | Pendiente | Post-Meta |
| paneles-corella | Pendiente | Post-CFE |
| liderazgo | Pendiente | Después |
| itil | Pendiente | Después |
| cvs | Pendiente | Después |

Esto se actualiza en `CLAUDE.md` §9 cuando cambia el estado.
