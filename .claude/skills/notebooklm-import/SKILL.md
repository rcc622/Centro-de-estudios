---
name: notebooklm-import
description: Workflow para convertir contenido de NotebookLM (Study Guides, Briefing Docs, Mind Maps, Audio Overviews) en cursos JSON de Centro de Estudios Randall. Úsalo cuando Randall mencione "tengo el output de Notebook / NotebookLM / un Study Guide / Briefing Doc", quiera "agregar un curso nuevo a partir de transcripciones / videos / .txt", suba archivos a `source/` o `content/<curso>/source/`, o pegue texto largo estructurado por temas que claramente venga de un resumen de Notebook.
---

# NotebookLM → Centro de Estudios Randall

Randall procesa transcripciones de cursos en video con NotebookLM y quiere que las salidas (Study Guides, Briefing Docs, mind maps, audio overviews) se conviertan en cursos jugables dentro de su PWA. Esta skill cubre el workflow completo: cómo recibir el material, cómo estructurarlo, cómo agregar multimedia, y cómo validar antes de mergear.

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

## 3. Workflow paso-a-paso para un curso nuevo

Cuando Randall te diga "armemos el curso X con este material":

1. **Leer el material completo** del Study Guide/Briefing Doc
2. **Proponerle a Randall la estructura** ANTES de generar contenido:
   - Cuántos días/módulos
   - Qué temas por día
   - Cuántas lecciones por día y de qué tipos
   - **Pedirle aprobación de la estructura** — no gastés tokens generando 7 días si la estructura está mal
3. Si aprueba, **crear `content/<curso>/meta.json`** con la lista de days/modules (todos `locked:false` o `locked:true` según ritmo de generación)
4. **Agregar el curso a `content/courses.json`** con `active:true`
5. **Generar los días uno por uno**, cada uno respetando A → B → C → D
6. **Para cada MCQ**:
   - Distractores plausibles, no obvios
   - `explanation` que enseña (no solo "es B"). Explicar por qué las otras truenan.
7. **Si hay material multimedia** (mind maps, audios), embeber con cards `image` o `audio-link` en la lección correspondiente
8. **Validar JSON** mentalmente antes de commit
9. **Commit por día**: `feat(<curso>): día N — <título corto>`
10. **Confirmar a Randall**: archivos creados, cantidad de lecciones/MCQs/flashcards, lo que debería revisar

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
